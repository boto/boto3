.. _ref_custom_dynamodb:

================================
DynamoDB customization reference
================================

.. _ref_valid_dynamodb_types:

Valid DynamoDB types
--------------------

These are the valid item types to use with Boto3 Table Resource (:py:class:`dynamodb.Table`) and DynamoDB:

+----------------------------------------------+-----------------------------+
| Python Type                                  | DynamoDB Type               |
+==============================================+=============================+
| string                                       | String (S)                  |
+----------------------------------------------+-----------------------------+
| integer                                      | Number (N)                  |
+----------------------------------------------+-----------------------------+
| :py:class:`decimal.Decimal`                  | Number (N)                  |
+----------------------------------------------+-----------------------------+
| :py:class:`boto3.dynamodb.types.Binary`      | Binary (B)                  |
+----------------------------------------------+-----------------------------+
| boolean                                      | Boolean (BOOL)              |
+----------------------------------------------+-----------------------------+
| ``None``                                     | Null (NULL)                 |
+----------------------------------------------+-----------------------------+
| string set                                   | String Set (SS)             |
+----------------------------------------------+-----------------------------+
| integer set                                  | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`decimal.Decimal` set              | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`boto3.dynamodb.types.Binary` set  | Binary Set (BS)             |
+----------------------------------------------+-----------------------------+
| list                                         | List (L)                    |
+----------------------------------------------+-----------------------------+
| dict                                         | Map (M)                     |
+----------------------------------------------+-----------------------------+


Custom Boto3 types
------------------


.. autoclass:: boto3.dynamodb.types.Binary
   :members:
   :undoc-members:

.. _ref_dynamodb_conditions:

DynamoDB conditions
-------------------

.. note::

    Both :py:class:`~boto3.dynamodb.conditions.Key` and
    :py:class:`~boto3.dynamodb.conditions.Attr` conditions can be chained
    together using the logical operators: ``&`` (and), ``|`` (or), and ``~`` (not).

    Example::

        # Filter for users named 'John' who are over 25
        FilterExpression=Attr('name').eq('John') & Attr('age').gt(25)

        # Filter using OR
        FilterExpression=Attr('status').eq('active') | Attr('role').eq('admin')

        # Filter using NOT
        FilterExpression=~Attr('deleted').eq(True)

    See :ref:`dynamodb_guide` for more detailed usage examples.

.. autoclass:: boto3.dynamodb.conditions.Key
   :members:
   :undoc-members:
   :inherited-members:

.. autoclass:: boto3.dynamodb.conditions.Attr
   :members:
   :undoc-members:
   :inherited-members: