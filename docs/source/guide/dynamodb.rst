.. _dynamodb_guide:

Amazon DynamoDB
================
By following this guide, you will learn how to use the
:py:class:`DynamoDB.ServiceResource` and :py:class:`DynamoDB.Table`
resources in order to create tables, write items to tables, modify existing
items, retrieve items, and query/filter the items in the table.


Creating a new table
--------------------

In order to create a new table, use the
:py:meth:`DynamoDB.ServiceResource.create_table` method::

    import boto3
    
    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Create the DynamoDB table.
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')

    # Print out some data about the table.
    print(table.item_count)

Expected output::

    0

This creates a table named ``users`` that respectively has the hash and
range primary keys ``username`` and ``last_name``.
This method will return a :py:class:`DynamoDB.Table` resource to call
additional methods on the created table.


Using an existing table
-----------------------
It is also possible to create a :py:class:`DynamoDB.Table` resource from
an existing table::

    import boto3

    # Get the service resource.
    dynamodb = boto3.resource('dynamodb')

    # Instantiate a table resource object without actually
    # creating a DynamoDB table. Note that the attributes of this table
    # are lazy-loaded: a request is not made nor are the attribute
    # values populated until the attributes
    # on the table resource are accessed or its load() method is called.
    table = dynamodb.Table('users')

    # Print out some data about the table.
    # This will cause a request to be made to DynamoDB and its attribute
    # values will be set based on the response.
    print(table.creation_date_time)

Expected output (Please note that the actual times will probably not match up)::

    2015-06-26 12:42:45.149000-07:00


Creating a new item
-------------------

Once you have a :py:class:`DynamoDB.Table` resource you can add new items
to the table using :py:meth:`DynamoDB.Table.put_item`::

    table.put_item(
       Item={
            'username': 'janedoe',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'age': 25,
            'account_type': 'standard_user',
        }
    )

For all of the valid types that can be used for an item, refer to
:ref:`ref_valid_dynamodb_types`.


Getting an item
---------------
You can then retrieve the object using :py:meth:`DynamoDB.Table.get_item`::

    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print(item)


Expected output::

    {u'username': u'janedoe',
     u'first_name': u'Jane',
     u'last_name': u'Doe',
     u'account_type': u'standard_user',
     u'age': Decimal('25')}


Updating an item
----------------

You can then update attributes of the item in the table::

    table.update_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        },
        UpdateExpression='SET age = :val1',
        ExpressionAttributeValues={
            ':val1': 26
        }
    )

Then if you retrieve the item again, it will be updated appropriately::

    response = table.get_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )
    item = response['Item']
    print(item)


Expected output::

    {u'username': u'janedoe',
     u'first_name': u'Jane',
     u'last_name': u'Doe',
     u'account_type': u'standard_user',
     u'age': Decimal('26')}


Deleting an item
----------------
You can also delete the item using :py:meth:`DynamoDB.Table.delete_item`::
    
    table.delete_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )


Batch writing
-------------
If you are loading a lot of data at a time, you can make use of
:py:meth:`DynamoDB.Table.batch_writer` so you can both speed up the process and
reduce the number of write requests made to the service.

This method returns a handle to a batch writer object that will automatically
handle buffering and sending items in batches.  In addition, the
batch writer will also automatically handle any unprocessed items and
resend them as needed.  All you need to do is call ``put_item`` for any
items you want to add, and ``delete_item`` for any items you want to delete::

    with table.batch_writer() as batch:
        batch.put_item(
            Item={
                'account_type': 'standard_user',
                'username': 'johndoe',
                'first_name': 'John',
                'last_name': 'Doe',
                'age': 25,
                'address': {
                    'road': '1 Jefferson Street',
                    'city': 'Los Angeles',
                    'state': 'CA',
                    'zipcode': 90001
                }
            }
        )
        batch.put_item(
            Item={
                'account_type': 'super_user',
                'username': 'janedoering',
                'first_name': 'Jane',
                'last_name': 'Doering',
                'age': 40,
                'address': {
                    'road': '2 Washington Avenue',
                    'city': 'Seattle',
                    'state': 'WA',
                    'zipcode': 98109
                }
            }
        )
        batch.put_item(
            Item={
                'account_type': 'standard_user',
                'username': 'bobsmith',
                'first_name': 'Bob',
                'last_name':  'Smith',
                'age': 18,
                'address': {
                    'road': '3 Madison Lane',
                    'city': 'Louisville',
                    'state': 'KY',
                    'zipcode': 40213
                }
            }
        )
        batch.put_item(
            Item={
                'account_type': 'super_user',
                'username': 'alicedoe',
                'first_name': 'Alice',
                'last_name': 'Doe',
                'age': 27,
                'address': {
                    'road': '1 Jefferson Street',
                    'city': 'Los Angeles',
                    'state': 'CA',
                    'zipcode': 90001
                }
            }
        )

The batch writer is even able to handle a very large amount of writes to the
table.

::

    with table.batch_writer() as batch:
        for i in range(50):
            batch.put_item(
                Item={
                    'account_type': 'anonymous',
                    'username': 'user' + str(i),
                    'first_name': 'unknown',
                    'last_name': 'unknown'
                }
            )

The batch writer can help to de-duplicate request by specifying ``overwrite_by_pkeys=['partition_key', 'sort_key']``
if you want to bypass no duplication limitation of single batch write request as
``botocore.exceptions.ClientError: An error occurred (ValidationException) when calling the BatchWriteItem operation: Provided list of item keys contains duplicates``.

It will drop request items in the buffer if their primary keys(composite) values are
the same as newly added one, as eventually consistent with streams of individual
put/delete operations on the same item.

::

    with table.batch_writer(overwrite_by_pkeys=['partition_key', 'sort_key']) as batch:
        batch.put_item(
            Item={
                'partition_key': 'p1',
                'sort_key': 's1',
                'other': '111',
            }
        )
        batch.put_item(
            Item={
                'partition_key': 'p1',
                'sort_key': 's1',
                'other': '222',
            }
        )
        batch.delete_item(
            Key={
                'partition_key': 'p1',
                'sort_key': 's2'
            }
        )
        batch.put_item(
            Item={
                'partition_key': 'p1',
                'sort_key': 's2',
                'other': '444',
            }
        )

after de-duplicate:

::

    batch.put_item(
        Item={
            'partition_key': 'p1',
            'sort_key': 's1',
            'other': '222',
        }
    )
    batch.put_item(
        Item={
            'partition_key': 'p1',
            'sort_key': 's2',
            'other': '444',
        }
    )


Querying and scanning
---------------------

With the table full of items, you can then query or scan the items in the table
using the :py:meth:`DynamoDB.Table.query` or :py:meth:`DynamoDB.Table.scan`
methods respectively. To add conditions to scanning and querying the table,
you will need to import the :py:class:`boto3.dynamodb.conditions.Key` and
:py:class:`boto3.dynamodb.conditions.Attr` classes. The
:py:class:`boto3.dynamodb.conditions.Key` should be used when the
condition is related to the key of the item.
The :py:class:`boto3.dynamodb.conditions.Attr` should be used when the
condition is related to an attribute of the item::

    from boto3.dynamodb.conditions import Key, Attr
    

This queries for all of the users whose ``username`` key equals ``johndoe``::

    response = table.query(
        KeyConditionExpression=Key('username').eq('johndoe')
    )
    items = response['Items']
    print(items)


Expected output::

    [{u'username': u'johndoe',
      u'first_name': u'John',
      u'last_name': u'Doe',
      u'account_type': u'standard_user',
      u'age': Decimal('25'),
      u'address': {u'city': u'Los Angeles',
                   u'state': u'CA',
                   u'zipcode': Decimal('90001'),
                   u'road': u'1 Jefferson Street'}}]


Similarly you can scan the table based on attributes of the items. For
example, this scans for all the users whose ``age`` is less than ``27``::

    response = table.scan(
        FilterExpression=Attr('age').lt(27)
    )
    items = response['Items']
    print(items)


Expected output::

    [{u'username': u'johndoe',
      u'first_name': u'John',
      u'last_name': u'Doe',
      u'account_type': u'standard_user',
      u'age': Decimal('25'),
      u'address': {u'city': u'Los Angeles',
                   u'state': u'CA',
                   u'zipcode': Decimal('90001'),
                   u'road': u'1 Jefferson Street'}},
     {u'username': u'bobsmith',
      u'first_name': u'Bob',
      u'last_name': u'Smith',
      u'account_type': u'standard_user',
      u'age': Decimal('18'),
      u'address': {u'city': u'Louisville',
                   u'state': u'KY',
                   u'zipcode': Decimal('40213'),
                   u'road': u'3 Madison Lane'}}]


You are also able to chain conditions together using the logical operators:
``&`` (and), ``|`` (or), and ``~`` (not). For example, this scans for all
users whose ``first_name`` starts with ``J`` and whose ``account_type`` is
``super_user``::
    
    response = table.scan(
        FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
    )
    items = response['Items']
    print(items)


Expected output::

    [{u'username': u'janedoering',
      u'first_name': u'Jane',
      u'last_name': u'Doering',
      u'account_type': u'super_user',
      u'age': Decimal('40'),
      u'address': {u'city': u'Seattle',
                   u'state': u'WA',
                   u'zipcode': Decimal('98109'),
                   u'road': u'2 Washington Avenue'}}]


You can even scan based on conditions of a nested attribute. For example this
scans for all users whose ``state`` in their ``address`` is ``CA``::

    response = table.scan(
        FilterExpression=Attr('address.state').eq('CA')
    )
    items = response['Items']
    print(items)


Expected output::

    [{u'username': u'johndoe',
      u'first_name': u'John',
      u'last_name': u'Doe',
      u'account_type': u'standard_user',
      u'age': Decimal('25'),
      u'address': {u'city': u'Los Angeles',
                   u'state': u'CA',
                   u'zipcode': Decimal('90001'),
                   u'road': u'1 Jefferson Street'}},
     {u'username': u'alicedoe',
      u'first_name': u'Alice',
      u'last_name': u'Doe',
      u'account_type': u'super_user',
      u'age': Decimal('27'),
      u'address': {u'city': u'Los Angeles',
                   u'state': u'CA',
                   u'zipcode': Decimal('90001'),
                   u'road': u'1 Jefferson Street'}}]


For more information on the various conditions you can use for queries and
scans, refer to :ref:`ref_dynamodb_conditions`.


Deleting a table
----------------
Finally, if you want to delete your table call
:py:meth:`DynamoDB.Table.delete`::

    table.delete()
