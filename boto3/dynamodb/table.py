# Copyright 2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# https://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import logging

logger = logging.getLogger(__name__)


def register_table_methods(base_classes, **kwargs):
    base_classes.insert(0, TableResource)


# This class can be used to add any additional methods we want
# onto a table resource.  Ideally to avoid creating a new
# base class for every method we can just update this
# class instead.  Just be sure to move the bulk of the
# actual method implementation to another class.
class TableResource:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def batch_writer(
        self, overwrite_by_pkeys=None, return_consumed_capacity=None
    ):
        """Create a batch writer object.

        This method creates a context manager for writing
        objects to Amazon DynamoDB in batch.

        The batch writer will automatically handle buffering and sending items
        in batches.  In addition, the batch writer will also automatically
        handle any unprocessed items and resend them as needed.  All you need
        to do is call ``put_item`` for any items you want to add, and
        ``delete_item`` for any items you want to delete.

        Example usage::

            with table.batch_writer() as batch:
                for _ in range(1000000):
                    batch.put_item(Item={'HashKey': '...',
                                         'Otherstuff': '...'})
                # You can also delete_items in a batch.
                batch.delete_item(Key={'HashKey': 'SomeHashKey'})

        :type overwrite_by_pkeys: list(string)
        :param overwrite_by_pkeys: De-duplicate request items in buffer
            if match new request item on specified primary keys. i.e
            ``["partition_key1", "sort_key2", "sort_key3"]``
        :type return_consumed_capacity: string
        :param return_consumed_capacity: Determines the level of detail
            about either provisioned or on-demand throughput consumption
            that is returned in the response:
            INDEXES - The response includes the aggregate
                ConsumedCapacity for the operation, together with
                ConsumedCapacity for each table and secondary index that
                was accessed.
            TOTAL - The response includes only the aggregate
                ConsumedCapacity for the operation.
            NONE - No ConsumedCapacity details are included in the
                response.

        """
        return BatchWriter(
            self.name,
            self.meta.client,
            overwrite_by_pkeys=overwrite_by_pkeys,
            return_consumed_capacity=return_consumed_capacity,
        )


class BatchWriter:
    """Automatically handle batch writes to DynamoDB for a single table."""

    def __init__(
        self,
        table_name,
        client,
        flush_amount=25,
        overwrite_by_pkeys=None,
        return_consumed_capacity=None,
    ):
        """

        :type table_name: str
        :param table_name: The name of the table.  The class handles
            batch writes to a single table.

        :type client: ``botocore.client.Client``
        :param client: A botocore client.  Note this client
            **must** have the dynamodb customizations applied
            to it for transforming AttributeValues into the
            wire protocol.  What this means in practice is that
            you need to use a client that comes from a DynamoDB
            resource if you're going to instantiate this class
            directly, i.e
            ``boto3.resource('dynamodb').Table('foo').meta.client``.

        :type flush_amount: int
        :param flush_amount: The number of items to keep in
            a local buffer before sending a batch_write_item
            request to DynamoDB.

        :type overwrite_by_pkeys: list(string)
        :param overwrite_by_pkeys: De-duplicate request items in buffer
            if match new request item on specified primary keys. i.e
            ``["partition_key1", "sort_key2", "sort_key3"]``

        :type return_consumed_capacity: string
        :param return_consumed_capacity: Determines the level of detail
            about either provisioned or on-demand throughput consumption
            that is returned in the response:
            INDEXES - The response includes the aggregate
                ConsumedCapacity for the operation, together with
                ConsumedCapacity for each table and secondary index that
                was accessed.
            TOTAL - The response includes only the aggregate
                ConsumedCapacity for the operation.
            NONE - No ConsumedCapacity details are included in the
                response.
        """
        self._table_name = table_name
        self._client = client
        self._items_buffer = []
        self._flush_amount = flush_amount
        self._overwrite_by_pkeys = overwrite_by_pkeys
        self.return_consumed_capacity = return_consumed_capacity
        self.consumed_capacity = None

    def put_item(self, Item):
        self._add_request_and_process({'PutRequest': {'Item': Item}})

    def delete_item(self, Key):
        self._add_request_and_process({'DeleteRequest': {'Key': Key}})

    def _add_request_and_process(self, request):
        if self._overwrite_by_pkeys:
            self._remove_dup_pkeys_request_if_any(request)
        self._items_buffer.append(request)
        self._flush_if_needed()

    def _remove_dup_pkeys_request_if_any(self, request):
        pkey_values_new = self._extract_pkey_values(request)
        for item in self._items_buffer:
            if self._extract_pkey_values(item) == pkey_values_new:
                self._items_buffer.remove(item)
                logger.debug(
                    "With overwrite_by_pkeys enabled, skipping " "request:%s",
                    item,
                )

    def _extract_pkey_values(self, request):
        if request.get('PutRequest'):
            return [
                request['PutRequest']['Item'][key]
                for key in self._overwrite_by_pkeys
            ]
        elif request.get('DeleteRequest'):
            return [
                request['DeleteRequest']['Key'][key]
                for key in self._overwrite_by_pkeys
            ]
        return None

    def _flush_if_needed(self):
        if len(self._items_buffer) >= self._flush_amount:
            self._flush()

    def _flush(self):
        items_to_send = self._items_buffer[: self._flush_amount]
        self._items_buffer = self._items_buffer[self._flush_amount :]
        params = {
            'RequestItems': {self._table_name: items_to_send},
        }
        if self.return_consumed_capacity is not None:
            params['ReturnConsumedCapacity'] = self.return_consumed_capacity
        response = self._client.batch_write_item(**params)
        consumed_capacity = response.get('ConsumedCapacity')
        if consumed_capacity is not None:
            self._update_consumed_capacity_array(consumed_capacity)
        unprocessed_items = response['UnprocessedItems']
        if not unprocessed_items:
            unprocessed_items = {}
        item_list = unprocessed_items.get(self._table_name, [])
        # Any unprocessed_items are immediately added to the
        # next batch we send.
        self._items_buffer.extend(item_list)
        logger.debug(
            "Batch write sent %s, unprocessed: %s",
            len(items_to_send),
            len(self._items_buffer),
        )

    def _update_consumed_capacity_array(self, new_consumed_capacity):
        if self.consumed_capacity is None:
            self.consumed_capacity = new_consumed_capacity
        elif new_consumed_capacity:
            self.aggg_consumed_capacity_objects(
                self.consumed_capacity[0], new_consumed_capacity[0]
            )

    @staticmethod
    def aggg_consumed_capacity_objects(
        total_consumed_capacity, consumed_capacity
    ):
        # Merge total capacities
        BatchWriter._agg_capacity_objects(
            total_consumed_capacity, consumed_capacity
        )

        # Merge table capacities
        if 'Table' in consumed_capacity:
            if 'Table' not in total_consumed_capacity:
                total_consumed_capacity['Table'] = {}
            BatchWriter._agg_capacity_objects(
                total_consumed_capacity['Table'],
                consumed_capacity['Table'],
            )

        # Merge indexes capacities
        index_types = ['LocalSecondaryIndexes', 'GlobalSecondaryIndexes']
        for index_type in index_types:
            if index_type in consumed_capacity:
                if index_type not in total_consumed_capacity:
                    total_consumed_capacity[index_type] = consumed_capacity[
                        index_type
                    ]
                else:
                    for index_name in consumed_capacity[index_type]:
                        if (
                            index_name
                            not in total_consumed_capacity[index_type]
                        ):
                            total_consumed_capacity[index_type][
                                index_name
                            ] = {}
                        BatchWriter._agg_capacity_objects(
                            total_consumed_capacity[index_type][index_name],
                            consumed_capacity[index_type][index_name],
                        )

    @staticmethod
    def _agg_capacity_objects(total_consumed_capacity, consumed_capacity):
        capacity_unit_keys = [
            'CapacityUnits',
            'ReadCapacityUnits',
            'WriteCapacityUnits',
        ]
        for key in capacity_unit_keys:
            if key in consumed_capacity:
                total_consumed_capacity[key] = (
                    total_consumed_capacity.get(key, 0)
                    + consumed_capacity[key]
                )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        # When we exit, we need to keep flushing whatever's left
        # until there's nothing left in our items buffer.
        while self._items_buffer:
            self._flush()
