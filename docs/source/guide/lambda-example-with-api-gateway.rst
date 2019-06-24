.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto3-lambda-examples-with-api-gateway:

***************************************************************
Create an AWS Lambda Function and an API Gateway REST Interface
***************************************************************

The example program creates a basic AWS Lambda function. The program also 
creates a REST API interface for the function.

Each section describes a single function from the `example's source
file <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/lambda/lambda_with_api_gateway.py>`_.

Also available is the `Lambda function source 
file <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/python/example_code/lambda/basic_lambda_function.py>`_.


A Basic Lambda Function
=======================

The source code for a basic AWS Lambda function is shown below. The function 
activates logging which results in messages being output to an Amazon 
CloudWatch log file.

The function demonstrates how to pass arguments to and from a Lambda function.
When the function is invoked by an HTTP ``PUT`` operation, it returns the input
parameters passed to it in the ``event`` argument. For all other types of
invocation (``GET``, ``POST``, etc.), the function returns some hard-coded
key-value pairs.

.. code-block:: python

    import logging
    logging.basicConfig(format='%(levelname)s: %(asctime)s: %(message)s')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)


    def lambda_handler(event, context):
        """Basic Lambda function template

        :param event: Dict (usually) of parameters passed to the function
        :param context: LambdaContext object of runtime data
        :return: Dict of key:value pairs
        """

        # Log the values received in the event argument
        logger.info(f'Request event: {event}')

        # Define default hard-coded return values
        response = {
            'uid': 'Example function ID',
            'return_val01': 'Return value #1',
            'return_val02': 'Return Value #2',
        }

        # Retrieve type of invocation (GET, PUT, etc.)
        if 'http_verb' in event:
            operation = event['http_verb'].upper()
            if operation == 'PUT':
                # Return the values passed to the function
                response = {
                    'uid': event['functionID'],
                    'return_val01': event['parameters']['parm01'],
                    'return_val02': event['parameters']['parm02'],
                }

        logger.info(f'Response={response}')
        return response


Deploy a Lambda Function
========================

To deploy a Lambda function, perform the following steps.

1. Store the Lambda source file and all dependent packages in a ZIP file. This
   ZIP file is called a deployment package.
#. Create an AWS IAM role for the Lambda function and grant any required
   permissions, such as the ability to write to AWS CloudWatch logs.
#. Deploy the function's deployment package. This operation typically entails
   copying the deployment package ZIP file to an S3 bucket. Alternatively, the 
   contents of the ZIP file can be loaded into memory and passed to the AWS 
   deployment method. The basic Lambda function used by the example is small, so 
   the technique of loading the ZIP file into memory is demonstrated.

The example code performs each of the above steps. For complete details,
refer to the source file linked at the beginning of this section.

.. code-block:: python

    def create_lambda_function(function_name, srcfile, handler_name, role_name):
        """Create a Lambda function

        It is assumed that srcfile includes an extension, such as source.py or
        source.js. The filename minus the extension is used to construct the
        ZIP file deployment package, e.g., source.zip.

        If the role_name exists, the existing role is used. Otherwise, an
        appropriate role is created.

        :param function_name: Lambda function name
        :param srcfile: Lambda source file
        :param handler_name: Lambda handler name
        :param role_name: Lambda role name
        :return: String ARN of the created Lambda function. If error, returns None.
        """

        # Parse the filename and extension in srcfile
        filename, _ = os.path.splitext(srcfile)

        # Create a deployment package
        deployment_package = f'{filename}.zip'
        if not create_lambda_deployment_package(srcfile, deployment_package):
            return None

        # Create Lambda IAM role if necessary
        if iam_role_exists(role_name):
            # Retrieve its ARN
            iam_role_arn = get_iam_role_arn(role_name)
        else:
            iam_role_arn = create_iam_role_for_lambda(role_name)
            if iam_role_arn is None:
                # Error creating IAM role
                return None

        # Deploy the Lambda function
        microservice = deploy_lambda_function(function_name, iam_role_arn,
                                              f'{filename}.{handler_name}',
                                              deployment_package)
        if microservice is None:
            return None
        lambda_arn = microservice['FunctionArn']
        logging.info(f'Created Lambda function: {function_name}')
        logging.info(f'ARN: {lambda_arn}')
        return lambda_arn


Invoke the Lambda Function
==========================

After being deployed, the Lambda function can be directly invoked from a
Python script by calling the AWS SDK for Python ``invoke`` function.

.. code-block:: python

    def invoke_lambda_function_synchronous(name, parameters):
        """Invoke a Lambda function synchronously

        :param name: Lambda function name or ARN or partial ARN
        :param parameters: Dict of parameters and values to pass to function
        :return: Dict of response parameters and values. If error, returns None.
        """

        # Convert the parameters from dict -> string -> bytes
        params_bytes = json.dumps(parameters).encode()

        # Invoke the Lambda function
        lambda_client = boto3.client('lambda')
        try:
            response = lambda_client.invoke(FunctionName=name,
                                            InvocationType='RequestResponse',
                                            LogType='Tail',
                                            Payload=params_bytes)
        except ClientError as e:
            logging.error(e)
            return None
        return response


Create a REST API for the Lambda Function
=========================================

Although a Lambda function can be invoked directly from a Python script, calling 
the function through a REST interface created by the API Gateway is usually 
preferable for the following reasons.

* The script can invoke the Lambda function using simple HTTP requests and 
  standard HTTP verbs rather than using the AWS SDK for Python.
* The API Gateway interface enables additional functionality, such as throttling
  excessive requests, authorizing requests, and transforming request and response 
  data.
* The close coupling that results between the Lambda function and invoking it
  directly can make changing the Lambda function more difficult. Decoupling
  the Lambda function by calling it through a REST API enables the function to 
  be painlessly updated at any time.

The basic steps necessary to create an API Gateway REST API for the Lambda 
function are listed below.

1. Initialize the API by calling the AWS SDK for Python ``create_rest_api``
   method. The method creates the basic infrastructure for the API, including
   a root resource, which is referenced by a slash character ('/').
#. Retrieve the ID of the root resource by calling the ``get_resources`` method. 
   The ID is used to set up additional components of the REST API.
#. Define any desired child resources under the root resource by calling the 
   ``create_resource`` method. The example program creates a single child resource
   called ``example``.
#. Define the desired methods the API must recognize, such as ``GET`` or
   ``PUT``. The methods are defined by calling ``put_method``. The example program 
   recognizes all HTTP verbs by defining the ``ANY`` method.
#. Specify the content type returned in a method's response by calling 
   ``put_method_response``. The example program sets the response content type 
   to JSON for each recognized method.
#. Set the Lambda function as the destination of the REST method by calling 
   the ``put_integration`` method.
#. Specify the content type returned by the Lambda function by calling the 
   ``put_integration_response`` method. The example Lambda function formats its
   response data as JSON.
#. Deploy the REST API by calling the ``create_deployment`` method. The method 
   specifies the name of a stage, such as ``dev`` or ``prod``.
#. Finally, the Lambda function is granted the necessary permissions so it can 
   be invoked by the API Gateway service.

The example's ``create_rest_api`` method performs each of the above steps. It
returns a REST API URL that can be referenced in a browser or application to
invoke the API and the Lambda function that lies behind it.

.. code-block:: python

    def create_rest_api(api_name, lambda_name):
        """Create a REST API for a Lambda function

        The REST API defines a child called /example and a stage called prod.

        :param api_name: Name of the REST API
        :param lambda_name: Name of existing Lambda function
        :return: URL of API. If error, returns None.
        """

        # Specify child resource name under root and stage name
        child_resource_name = 'example'
        stage_name = 'prod'

        # Create initial REST API
        api_client = boto3.client('apigateway')
        try:
            result = api_client.create_rest_api(name=api_name)
        except ClientError as e:
            logging.error(e)
            return None
        api_id = result['id']
        logging.info(f'Created REST API: {result["name"]}, ID: {api_id}')

        # Get the ID of the API's root resource
        try:
            result = api_client.get_resources(restApiId=api_id)
        except ClientError as e:
            logging.error(e)
            return None
        root_id = None
        for item in result['items']:
            if item['path'] == '/':
                root_id = item['id']
        if root_id is None:
            logging.error('Could not retrieve the ID of the API\'s root resource.')
            return None

        # Define a child resource called /example under the root resource
        try:
            result = api_client.create_resource(restApiId=api_id,
                                                parentId=root_id,
                                                pathPart=child_resource_name)
        except ClientError as e:
            logging.error(e)
            return None
        example_id = result['id']

        # Define an ANY method on the /example resource
        try:
            api_client.put_method(restApiId=api_id,
                                resourceId=example_id,
                                httpMethod='ANY',
                                authorizationType='NONE')
        except ClientError as e:
            logging.error(e)
            return None

        # Set the content-type of the API's ANY method response to JSON
        content_type = {'application/json': 'Empty'}
        try:
            api_client.put_method_response(restApiId=api_id,
                                        resourceId=example_id,
                                        httpMethod='ANY',
                                        statusCode='200',
                                        responseModels=content_type)
        except ClientError as e:
            logging.error(e)
            return None

        # Set the Lambda function as the destination for the ANY method
        # Extract the Lambda region and AWS account ID from the Lambda ARN
        # ARN format="arn:aws:lambda:REGION:ACCOUNT_ID:function:FUNCTION_NAME"
        lambda_arn = get_lambda_arn(lambda_name)
        if lambda_arn is None:
            return None
        sections = lambda_arn.split(':')
        region = sections[3]
        account_id = sections[4]
        # Construct the Lambda function's URI
        lambda_uri = f'arn:aws:apigateway:{region}:lambda:path/2015-03-31/' \
            f'functions/{lambda_arn}/invocations'
        try:
            api_client.put_integration(restApiId=api_id,
                                    resourceId=example_id,
                                    httpMethod='ANY',
                                    type='AWS',
                                    integrationHttpMethod='POST',
                                    uri=lambda_uri)
        except ClientError as e:
            logging.error(e)
            return None

        # Set the content-type of the Lambda function to JSON
        content_type = {'application/json': ''}
        try:
            api_client.put_integration_response(restApiId=api_id,
                                                resourceId=example_id,
                                                httpMethod='ANY',
                                                statusCode='200',
                                                responseTemplates=content_type)
        except ClientError as e:
            logging.error(e)
            return None

        # Deploy the API
        try:
            api_client.create_deployment(restApiId=api_id,
                                        stageName=stage_name)
        except ClientError as e:
            logging.error(e)
            return None

        # Grant invoke permissions on the Lambda function so it can be called by
        # API Gateway.
        # Note: To retrieve the Lambda function's permissions, call
        # Lambda.Client.get_policy()
        source_arn = f'arn:aws:execute-api:{region}:{account_id}:{api_id}/*/*/{child_resource_name}'
        lambda_client = boto3.client('lambda')
        try:
            lambda_client.add_permission(FunctionName=lambda_name,
                                        StatementId=f'{lambda_name}-invoke',
                                        Action='lambda:InvokeFunction',
                                        Principal='apigateway.amazonaws.com',
                                        SourceArn=source_arn)
        except ClientError as e:
            logging.error(e)
            return None

        # Construct the API URL
        api_url = f'https://{api_id}.execute-api.{region}.amazonaws.com/{stage_name}/{child_resource_name}'
        logging.info(f'API base URL: {api_url}')
        return api_url


Invoke the REST API from a Python Script
========================================

The example calls the REST API by using the popular Python ``requests``
package. This package is not part of the Python standard library and must be
installed separately, for example, with the ``pip`` command.

::

    pip install requests

Some example arguments are defined and passed to the REST API in a ``PUT``
request. The returned response data is logged to the console and also to a
CloudWatch log file.

.. code-block:: python

    # Define parameters to pass to the API/Lambda function
    lambda_parms = {'http_verb': 'PUT',
                    'functionID': lambda_arn,
                    'parameters': {
                        'parm01': 'Lambda parameter #1',
                        'parm02': 'Lambda parameter #2',
                    }}

    # Invoke the REST API
    # Use requests package (pip install requests)
    https_response = requests.put(api_url, data=json.dumps(lambda_parms))
    logging.info(f'API status code: {https_response.status_code}')
    logging.info(f'Returned text: {https_response.text}')
