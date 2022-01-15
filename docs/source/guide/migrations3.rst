.. _guide_migration_s3:

Amazon S3
=========
Boto 2.x contains a number of customizations to make working with Amazon S3 buckets and keys easy. Boto3 exposes these same objects through its resources interface in a unified and consistent way.

Creating the connection
-----------------------
Boto3 has both low-level clients and higher-level resources. For Amazon S3, the higher-level resources are the most similar to Boto 2.x's ``s3`` module::

    # Boto 2.x
    import boto
    s3_connection = boto.connect_s3()

    # Boto3
    import boto3
    s3 = boto3.resource('s3')

Creating a bucket
-----------------
Creating a bucket in Boto 2 and Boto3 is very similar, except that in Boto3 all action parameters must be passed via keyword arguments and a bucket configuration must be specified manually::

    # Boto 2.x
    s3_connection.create_bucket('mybucket')
    s3_connection.create_bucket('mybucket', location=Location.USWest)

    # Boto3
    s3.create_bucket(Bucket='mybucket')
    s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'})

Storing data
------------
Storing data from a file, stream, or string is easy::

    # Boto 2.x
    from boto.s3.key import Key
    key = Key('hello.txt')
    key.set_contents_from_file('/tmp/hello.txt')

    # Boto3
    s3.Object('mybucket', 'hello.txt').put(Body=open('/tmp/hello.txt', 'rb'))


Accessing a bucket
------------------
Getting a bucket is easy with Boto3's resources, however these do not automatically validate whether a bucket exists::

    # Boto 2.x
    bucket = s3_connection.get_bucket('mybucket', validate=False)
    exists = s3_connection.lookup('mybucket')

    # Boto3
    import botocore
    bucket = s3.Bucket('mybucket')
    exists = True
    try:
        s3.meta.client.head_bucket(Bucket='mybucket')
    except botocore.exceptions.ClientError as e:
        # If a client error is thrown, then check that it was a 404 error.
        # If it was a 404 error, then the bucket does not exist.
        error_code = e.response['Error']['Code']
        if error_code == '404':
            exists = False

Deleting a bucket
-----------------
All of the keys in a bucket must be deleted before the bucket itself can be deleted::

    # Boto 2.x
    for key in bucket:
        key.delete()
    bucket.delete()

    # Boto3
    for key in bucket.objects.all():
        key.delete()
    bucket.delete()

Iteration of buckets and keys
-----------------------------
Bucket and key objects are no longer iterable, but now provide collection attributes which can be iterated::

    # Boto 2.x
    for bucket in s3_connection:
        for key in bucket:
            print(key.name)

    # Boto3
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print(key.key)

Access controls
---------------
Getting and setting canned access control values in Boto3 operates on an ``ACL`` resource object::

    # Boto 2.x
    bucket.set_acl('public-read')
    key.set_acl('public-read')

    # Boto3
    bucket.Acl().put(ACL='public-read')
    obj.Acl().put(ACL='public-read')

It's also possible to retrieve the policy grant information::

    # Boto 2.x
    acp = bucket.get_acl()
    for grant in acp.acl.grants:
        print(grant.display_name, grant.permission)

    # Boto3
    acl = bucket.Acl()
    for grant in acl.grants:
        print(grant['Grantee']['DisplayName'], grant['Permission'])

Boto3 lacks the grant shortcut methods present in Boto 2.x, but it is still fairly simple to add grantees::

    # Boto 2.x
    bucket.add_email_grant('READ', 'user@domain.tld')

    # Boto3
    bucket.Acl.put(GrantRead='emailAddress=user@domain.tld')

Key metadata
------------
It's possible to set arbitrary metadata on keys::

    # Boto 2.x
    key.set_metadata('meta1', 'This is my metadata value')
    print(key.get_metadata('meta1'))

    # Boto3
    key.put(Metadata={'meta1': 'This is my metadata value'})
    print(key.metadata['meta1'])

Managing CORS configurations
---------------------------
Allows you to manage the cross-origin resource sharing configuration for S3 buckets::

    # Boto 2.x
    cors = bucket.get_cors()

    config = CORSConfiguration()
    config.add_rule('GET', '*')
    bucket.set_cors(config)

    bucket.delete_cors()

    # Boto3
    cors = bucket.Cors()

    config = {
        'CORSRules': [
            {
                'AllowedMethods': ['GET'],
                'AllowedOrigins': ['*']
            }
        ]
    }
    cors.put(CORSConfiguration=config)

    cors.delete()
