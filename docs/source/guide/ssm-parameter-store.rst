###################################
AWS Systems Manager Parameter Store
###################################

This Python example shows you how to read values from the AWS Systems Manager Parameter Store.

The code uses the AWS SDK for Python to read the values

For more information about using an AWS Systems Manager Parameter Store, see 
`AWS Systems Manager Parameter Store <https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html>`_ 
in the *AWS Systems Manager User Guide*.

Prerequisite tasks
==================

To set up and run this example, you must first set up the following:

* Configure your AWS credentials, as described in :doc:`quickstart`.
* Create a parameter with the AWS Systems Manager Parameter Store, as described in the `AWS Systems Manager User Guide <https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html>`_

Retrieve the parameter value
=============================================

The following example shows how to:
 
* Retrieve a parameter value using 
  `get_parameter <https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm/client/get_parameter.html#SSM.Client.get_parameter>`_.
 
Example
-------

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError
    from typing import Optional


    def get_parameter(
        parameter_name: str = "MyParameterName",
        region_name: str = "us-west-2",
        decrypt: bool = True
    ) -> Optional[str]:
        """
        Retrieve a parameter value from AWS Systems Manager Parameter Store.

        Args:
            parameter_name (str): Name of the parameter to retrieve
            region_name (str): AWS region name
            decrypt (bool): Whether to decrypt the parameter value

        Returns:
            Optional[str]: Parameter value if successful, None if parameter not found or error occurs

        Raises:
            ClientError: If an AWS error occurs other than ParameterNotFound
        """
        try:
            ssm_client = boto3.client('ssm', region_name=region_name)
            response = ssm_client.get_parameter(
                Name=parameter_name,
                WithDecryption=decrypt
            )
            print(f"Successfully retrieved parameter: {parameter_name}")
            return response['Parameter']['Value']

        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'ParameterNotFound':
                print(f"Parameter not found: {parameter_name}")
                return None
            elif error_code == 'AccessDeniedException':
                print(f"Access denied to parameter: {parameter_name}")
                raise  # Re-raise access denied errors
            else:
                print(f"Error retrieving parameter: {str(e)}")
                raise  # Re-raise unexpected errors
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            raise

    # Example usage
    if __name__ == "__main__":
        try:
            value = get_parameter()
            if value:
                print(f"Parameter value: {value}")
        except ClientError as e:
            print(f"AWS Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            

     
