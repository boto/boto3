.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.


#################
Downloading files
#################

The methods provided by the AWS SDK for Python to download files are similar 
to those provided to upload files.

The ``download_file`` method accepts the names of the bucket and object to 
download and the filename to save the file to.

.. code-block:: python

    import boto3

    s3 = boto3.client('s3')
    s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')


The ``download_fileobj`` method accepts a writeable file-like object. The file 
object must be opened in binary mode, not text mode.

.. code-block:: python

    s3 = boto3.client('s3')
    with open('FILE_NAME', 'wb') as f:
        s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)


Like their upload cousins, the download methods are provided by the 
S3 ``Client``, ``Bucket``, and ``Object`` classes, and each class provides 
identical functionality. Use whichever class is convenient.

Also like the upload methods, the download methods support the optional 
``ExtraArgs`` and ``Callback`` parameters.

The list of valid ``ExtraArgs`` settings for the download methods is 
specified in the ``ALLOWED_DOWNLOAD_ARGS`` attribute of the ``S3Transfer`` 
object at :py:attr:`boto3.s3.transfer.S3Transfer.ALLOWED_DOWNLOAD_ARGS`.

The download method's ``Callback`` parameter is used for the same purpose 
as the upload method's. The upload and download methods can both invoke the 
same ``Callback`` class.


