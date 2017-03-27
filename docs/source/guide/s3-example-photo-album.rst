.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.
   
.. _aws-boto3-s3-uploading-photos:   

############################################
Uploading Photos to Amazon S3 from a Browser
############################################

This browser script example shows you how to upload photos into albums stored in an Amazon S3 bucket.

The Scenario
============

In this example, a simple HTML page provides a browser-based application for creating photo albums 
in an Amazon S3 bucket into which you can upload photos. The application lets you delete photos and 
albums that you add.

The browser script uses the SDK for JavaScript to interact with an Amazon S3 bucket. Use the following 
methods of the Amazon S3 client class to enable the photo album application:

* listObjects

* headObject

* putObject

* upload

* deleteObject

* deleteObjects

Prerequisite Tasks

To set up and run this example, you must first complete these tasks:

* Create an Amazon S3 bucket in the console that you will use to store the photos in the album. For 
  more information about creating a bucket in the console, see 
  `Creating a Bucket <>`_ 
  in the *Amazon Simple Storage Service Console User Guide*. Add List permissions for All Authorized AWS Users.

* Create an Amazon Cognito identity pool using Federated Identities with access enabled for unauthenticated 
  users. You need to include the identity pool ID in the code to obtain credentials for the browser 
  script. For more information about Amazon Cognito Federated Identities, see 
  `Amazon Cognito Identity: Using Federated Identites <>`_ in the *Amazon Cognito Developer Guide*.

* Create an IAM role whose policy grants permission to read and write to an Amazon S3 bucket. For more 
  information about creating an IAM role, see 
  `Creating a Role to Delegate Permissions to an AWS Service <>`_ in the *IAM User Guide*.

Use the following role policy when creating the IAM role.

.. code-block:: python

    {
       "Version": "2012-10-17",
       "Statement": [
          {
             "Effect": "Allow",
             "Action": [
                "s3:*"
             ],
             "Resource": [
                "arn:aws:s3:::BUCKET_NAME/*"
             ]
          }
       ]
    }

Configuring CORS

Before the browser script can access the Amazon S3 bucket, you must first set up its CORS configuration as follows.

.. code-block:: python
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>POST</AllowedMethod>
        <AllowedMethod>GET</AllowedMethod>
        <AllowedMethod>PUT</AllowedMethod>
        <AllowedMethod>DELETE</AllowedMethod>
        <AllowedMethod>HEAD</AllowedMethod>
        <AllowedHeader>*</AllowedHeader>
    </CORSRule>
</CORSConfiguration>

The Web Page

The HTML for the photo upload application consists of a <div> element within which the browser script creates the upload user interface.

.. code-block:: python
<!DOCTYPE html>
<html>
  <head>
    <script src="https://sdk.amazonaws.com/js/aws-sdk-2.7.20.min.js"></script>
    <script src="./app.js"></script>
    <script>
       function getHtml(template) {
          return template.join('\n');
       }
       listAlbums();
    </script>
  </head>
  <body>
    <h1>My Photo Albums App</h1>
    <div id="app"></div>
  </body>
</html>

Configuring the SDK

Obtain the credentials needed to configure the SDK by calling the CognitoIdentityCredentials method, providing the Amazon Cognito identity pool ID. Next, create an AWS.S3 service object.

.. code-block:: python
var albumBucketName = 'BUCKET_NAME';
var bucketRegion = 'REGION';
var IdentityPoolId = 'IDENTITY_POOL_ID';

AWS.config.update({
  region: bucketRegion,
  credentials: new AWS.CognitoIdentityCredentials({
    IdentityPoolId: IdentityPoolId
  })
});

var s3 = new AWS.S3({
  apiVersion: '2006-03-01',
  params: {Bucket: albumBucketName}
});

Nearly all of the rest of the code in this example is organized into a series of functions that gather and present information about the albums in the bucket, upload and display photos uploaded into albums, and delete photos and albums. Those functions are:

* listAlbums

* createAlbum

* viewAlbum

* addPhoto

* deleteAlbum

* deletePhoto

Listing Albums in the Bucket
============================

The application creates albums in the Amazon S3 bucket as objects whose keys begin with a forward slash character, indicating the object functions as a folder. To list all the existing albums in the bucket, the application's listAlbums function calls the listObjects method of the AWS.S3 service object while using commonPrefix so the call returns only objects used as albums.

The rest of the function takes the list of albums from the Amazon S3 bucket and generates the HTML needed to display the album list in the web page. It also enables deleting and opening individual albums.


Creating an Album in the Bucket
===============================

To create an album in the Amazon S3 bucket, the application's createAlbum function first validates the name given for the new album to ensure it contains suitable characters. The function then forms an Amazon S3 object key, passing it to the headObject method of the Amazon S3 service object. This method returns the metadata for the specified key, so if it returns data, then an object with that key already exists.

If the album doesn't already exist, the function calls the putObject method of the AWS.S3 service object to create the album. It then calls the viewAlbum function to display the new empty album.



Viewing an Album
================

To display the contents of an album in the Amazon S3 bucket, the application's viewAlbum function takes an album name and creates the Amazon S3 key for that album. The function then calls the listObjects method of the AWS.S3 service object to obtain a list of all the objects (photos) in the album.

The rest of the function takes the list of objects (photos) from the album and generates the HTML needed to display the photos in the web page. It also enables deleting individual photos and navigating back to the album list.



Adding Photos to an Album
=========================

To upload a photo to an album in the Amazon S3 bucket, the application's addPhoto function uses a file picker element in the web page to identify a file to upload. It then forms a key for the photo to upload from the current album name and the file name.

The function calls the upload method of the Amazon S3 service object to upload the photo. The ACL parameter is set to public-read so the application can fetch the photos in an album for display by their URL in the bucket. After uploading the photo, the function redisplays the album so the uploaded photo appears.


Deleting a Photo

To delete a photo from an album in the Amazon S3 bucket, the application's deletePhoto function calls the deleteObject method of the Amazon S3 service object. This deletes the photo specified by the photoKey value passed to the function.

.. code-block:: python
function deletePhoto(albumName, photoKey) {
  s3.deleteObject({Key: photoKey}, function(err, data) {
    if (err) {
      return alert('There was an error deleting your photo: ', err.message);
    }
    alert('Successfully deleted photo.');
    viewAlbum(albumName);
  });
}

Deleting an Album
=================

To delete an album in the Amazon S3 bucket, the application's deleteAlbum function calls the deleteObjects method of the Amazon S3 service object.

