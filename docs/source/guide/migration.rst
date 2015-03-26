.. _guide_migration:

Migrating from Boto 2.x
=======================
Current Boto users can begin using Boto 3 right away. The two modules can
live side-by-side in the same project, which means that a piecemeal
approach can be used. New features can be written in Boto 3, or existing
code can be migrated over as needed, piece by piece.

High Level Concepts
-------------------
Boto 2.x modules are typically split into two categories, those which include a high-level object-oriented interface and those which include only a low-level interface which matches the underlying Amazon Web Services API. Some modules are completely high-level (like Amazon S3 or EC2), some include high-level code on top of a low-level connection (like Amazon DynamoDB), and others are 100% low-level (like Amazon Elastic Transcoder).

In Boto 3 this general low-level and high-level concept hasn't changed much, but there are two important points to understand.

Data Driven
~~~~~~~~~~~
First, in Boto 3 classes are created at runtime from JSON data files that describe AWS APIs and organizational structures built atop of them. These data files are loaded at runtime and can be modified and updated without the need of installing an entirely new SDK release.

A side effect of having all the services generated from JSON files is that there is now consistency between all AWS service modules. One important change is that *all* API call parameters must now be passed as **keyword arguments**, and these keyword arguments take the form defined by the upstream service. Though there are exceptions, this typically means ``UpperCamelCasing`` parameter names. You will see this in the service-specific migration guides linked to below.

Resource Objects
~~~~~~~~~~~~~~~~
Second, while every service now uses the runtime-generated low-level client, some services additionally have high-level generated objects that we refer to as ``Resources``. The lower-level is comparable to Boto 2.x layer 1 connection objects in that they provide a one to one mapping of API operations and return low-level responses. The higher level is comparable to the high-level customizations from Boto 2.x: an S3 ``Key``, an EC2 ``Instance``, and a DynamoDB ``Table`` are all considered resources in Boto 3. Just like a Boto 2.x ``S3Connection``'s ``list_buckets`` will return ``Bucket`` objects, the Boto 3 resource interface provides actions and collections that return resources. Some services may also have hand-written customizations built on top of the runtime-generated high-level resources (such as utilities for working with S3 multipart uploads).

::

    import boto, boto3

    # Low-level connections
    conn = boto.connect_elastictranscoder()
    client = boto3.client('elastictranscoder')

    # High-level connections & resource objects
    from boto.s3.bucket import Bucket
    s3_conn = boto.connect_s3()
    boto2_bucket = Bucket('mybucket')

    s3 = boto3.resource('s3')
    boto3_bucket = s3.Bucket('mybucket')

Installation & Configuration
----------------------------
The :ref:`guide_quickstart` guide provides instructions for installing Boto 3. You can also follow the instructions there to set up new credential files, or you can continue to use your existing Boto 2.x credentials. Please note that Boto 3, the AWS CLI, and several other SDKs all use the shared credentials file (usually at ``~/.aws/credentials``).

Once configured, you may begin using Boto 3::

    import boto3

    for bucket in boto3.resource('s3').buckets.all():
        print(bucket.name)

See the :ref:`guide_tutorial` and `Boto 3 Documentation <http://boto3.readthedocs.org/>`__ for more information.

The rest of this document will describe specific common usage scenarios of Boto 2 code and how to accomplish the same tasks with Boto 3.

Services
--------

.. toctree::
   :maxdepth: 2

   migrations3
   migrationec2
