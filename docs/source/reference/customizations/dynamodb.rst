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
| float *(see note below)*                     | Number (N)                  |
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
| float set *(see note below)*                 | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`decimal.Decimal` set              | Number Set (NS)             |
+----------------------------------------------+-----------------------------+
| :py:class:`boto3.dynamodb.types.Binary` set  | Binary Set (BS)             |
+----------------------------------------------+-----------------------------+
| list                                         | List (L)                    |
+----------------------------------------------+-----------------------------+
| dict                                         | Map (M)                     |
+----------------------------------------------+-----------------------------+

  **Note:**  In Python, the 'float' data type provides an approximation 
  of the computer hardware representation of binary fractions.  
  This issue is explained in the Python documentation section titled `Floating Point Arithmetic`_.
  Because of this, float values are converted to Decimal using create_decimal_from_float_ 
  and may be an inexact and/or rounded representation of the true value.
  
.. _Floating Point Arithmetic: https://docs.python.org/3/tutorial/floatingpoint.html
.. _create_decimal_from_float: https://docs.python.org/3/library/decimal.html#decimal.Context.create_decimal_from_float


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
