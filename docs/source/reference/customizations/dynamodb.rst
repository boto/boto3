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

.. autoclass:: boto3.dynamodb.conditions.Key
   :members:
   :undoc-members:
   :inherited-members:

.. autoclass:: boto3.dynamodb.conditions.Attr
   :members:
   :undoc-members:
   :inherited-members:
