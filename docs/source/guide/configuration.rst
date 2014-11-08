.. _guide_configuration:

Configuration
=============
Boto can be configured in multiple ways. Regardless of the source or sources
that you choose, you **must** have AWS credentials and a region set in
order to make requests.

Interactive Configuration
-------------------------
If you have the `AWS CLI <http://aws.amazon.com/cli/>`_, then you can use
its interactive ``configure`` command to set up your credentials and
default region::

    aws configure

Follow the prompts and it will generate configuration files in the
correct locations for you.

Configuration Sources
---------------------
There are multiple sources from which configuration data can be loaded.
The general order in which they are checked is as follows:

1. Environment variables
2. Configuration files
3. EC2 Instance metadata
4. Method Parameters

Available Options
-----------------
The available options for various configuration sources are listed below.

Environment Variables
~~~~~~~~~~~~~~~~~~~~~

``AWS_ACCESS_KEY_ID``
    The access key for your AWS account.

``AWS_SECRET_ACCESS_KEY``
    The secret key for your AWS account.

``BOTO_DEFAULT_REGION``
    The default region to use, e.g. `us-east-1`.

``BOTO_DEFAULT_PROFILE``
    The default credential and configuration profile to use, if any.

``BOTO_DATA_PATH``
    The data path from which to load service and resource JSON files.

Configuration Files
~~~~~~~~~~~~~~~~~~~
There are two configuration files that Boto checks. The first is the
shared credential file, which holds only credentials and is shared between
various SDKs and tools like Boto and the AWS CLI. By default, this
file is located at ``~/.aws/credentials``::

    [default]
    # The access key for your AWS account
    aws_access_key_id=<YOUR ACCESS KEY ID>

    # The secret key for your AWS account
    aws_secret_access_key=<YOUR SECRET KEY>

Credentials can also be set for individual profiles::

    [dev-profile]
    # The access key for your dev-profile account
    aws_access_key_id=<YOUR ACCESS KEY ID>

    # The secret key for your dev-profile account
    aws_secret_access_key=<YOUR SECRET KEY>

The second configuration file stores all settings which are not
credentials. Its default location is ``~/.aws/config``::

    [default]
    # The default region when making requests
    region=<REGION NAME>

It also supports profiles, but these are prefixed with the word
``profile`` because this file supports sections other than profiles::

    [profile dev-profile]
    # The default region when using the dev-profile account
    region=<REGION NAME>


Method Parameters
~~~~~~~~~~~~~~~~~
When creating a session, client, or resource you can pass in credential
and configuration options::

    from boto3.session import Session

    session = Session(aws_access_key_id='<YOUR ACCESS KEY ID>',
                      aws_secret_access_key='<YOUR SECRET KEY>',
                      region_name='<REGION NAME>')

    ec2 = session.resource('ec2')
    ec2_us_west_2 = session.resource('ec2', region_name='us-west-2')

    print('Default region:')
    for instance in ec2.instances.all():
        print(instance.id)

    print('US West 2 region:')
    for instance in ec2_us_west_2.instances.all():
        print(instance.id)

For a list of all options, look at the :py:class:`~boto3.session.Session`
documentation.
