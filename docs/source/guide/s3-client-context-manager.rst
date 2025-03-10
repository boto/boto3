.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


###############
S3 Client Context Manager
###############

Following the pythonic-way, you may want to flexibly and easily manage resource release using a context manager for
the `boto3.client` instances you create.

The following is an example of creating a simple context manager for an S3 client:

.. code-block:: python

    from contextlib import contextmanager
    from typing import Optional

    import boto3


    @contextmanager
    def s3_client(**kwargs):
        client = None
        try:
            client = boto3.client("s3", **kwargs)
            yield client
        finally:
            if client:
                client.close()


Using the `s3_client` context manager you can easily create service functions that implement the necessary
actions with the storage.

.. code-block:: python

    def s3_get_object(
        key: str,
        # Your global constants from project settings here.
        bucket_name: str = AWS_BUCKET_NAME,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        endpoint_url=AWS_ENDPOINT_URL,
    ):
    with s3_client(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            endpoint_url=endpoint_url,
    ) as s3_cli:
        return s3_cli.get_object(Bucket=bucket_name, Key=key)


    # Usage example:
    key = "path/to/somefile"
    s3_obj = s3_get_object(key)

