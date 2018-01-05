=========
CHANGELOG
=========

1.5.9
=====

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version


1.5.8
=====

* api-change:``rds``: [``botocore``] Update rds client to latest version


1.5.7
=====

* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.5.6
=====

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.5.5
=====

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* enhancement:Paginator: [``botocore``] Added paginator support for lambda list aliases operation.
* api-change:``kinesisanalytics``: [``botocore``] Update kinesisanalytics client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.5.4
=====

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version


1.5.3
=====

* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``mediastore-data``: [``botocore``] Update mediastore-data client to latest version


1.5.2
=====

* bugfix:presigned-url: [``botocore``] Fixes a bug where content-type would be set on presigned requests for query services.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version


1.5.1
=====

* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.5.0
=====

* bugfix:Filters: Fixes a bug where parameters passed to resource collections could be mutated after the collections were created.
* api-change:``ses``: [``botocore``] Update ses client to latest version
* enhancement:credentials: [``botocore``] Moved the JSONFileCache from the CLI into botocore so that it can be used without importing from the cli.
* feature:``botocore`` dependency: Update dependency strategy to always take a floor on the most recent version of ``botocore``. This means whenever there is a release of ``botocore``, ``boto3`` will release as well to account for the new version of ``botocore``.
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version


1.4.8
=====

* enhancement:``botocore``: Raised minor version dependency for botocore


1.4.7
=====

* enhancement:``botocore``: Raised minor version dependency for botocore


1.4.6
=====

* enhancement:Logging: Switch log levels from INFO to DEBUG (`#1208 <https://github.com/boto/boto3/issues/1208>`__)


1.4.5
=====

* enhancement:s3: Add a LifecycleConfiguration resource to resolve issues with the existing Lifecycle resource.


1.4.3
=====

* feature:``s3``: Add ability to disable thread use with ``use_threads`` option
* bugfix:Resource: Fix resource hashing.


1.4.2
=====

* feature:ec2: Update client to latest version


1.4.1
=====

* feature:Session: Expose available_profiles property for Session (``#704 <https://github.com/boto/boto3/issues/704>`__)
* bugfix:s3: Fix issue when transfers would not exit quickly from signals
* bugfix:``sqs.Queue``: Fix issue in DeadLetterSourceQueues collection


1.4.0
=====

* feature:DynamoDB: Add request auto de-duplication based on specified primary keys for batch_writer. (`#605 <https://github.com/boto/boto3/issues/605>`__)
* feature:s3: Add managed file-like object uploads to S3 client, Bucket, and Object.
* bugfix:Session: Fixed Session.__repr__ region argument name.
* feature:s3: Add managed copies to S3 client, Bucket, and Object.
* feature:s3: Add managed downloads to file-like objects in the S3 client, Bucket, and Object.
* bugfix:s3: Port ``s3.transfer`` module to use ``s3transfer`` package. Please refer to `Upgrading Notes <https://boto3.readthedocs.io/en/latest/guide/upgrading.html>`_ when upgrading. In porting the logic over, various performance issues and bugs were fixed.
* feature:s3: Add ``io_chunksize`` parameter to ``TransferConfig``


1.3.1
=====

* feature:S3: Add custom load to ObjectSummary
* feature:Session: Add method to get session credentials
* bugfix:DynamoDB: Ensure batch writer never sends more than flush_amount (`#483 <https://github.com/boto/boto3/issues/483>`__)
* feature:Resources: Add get_available_subresources to Resources (`#113 <https://github.com/boto/boto3/issues/113>`__)


1.3.0
=====

* feature:``EC2``: Update resource model to include ``Route`` resources. (`issue 532 <https://github.com/boto/boto3/pull/532>`__)


1.2.5
=====

* bugfix:``S3``: Forward ``extra_args`` when using multipart downloads. (`issue 503 <https://github.com/boto/boto3/pull/503>`__)


1.2.4
=====

* feature:``Session``: Add ``region_name`` property on session. (`issue 414 <https://github.com/boto/boto3/pull/414>`__)
* bugfix:``S3``: Fix issue with hanging downloads. (`issue 471 <https://github.com/boto/boto3/pull/471>`__)


1.2.3
=====

* feature:``CloudWatch``: Add resource model. (`issue 412 <https://github.com/boto/boto3/pull/412>`__)
* feature:``S3``: Add a start_restore() on Object and ObjectSummary resources. (`issue 408 <https://github.com/boto/boto3/pull/408>`__)
* feature:Documentation: Add examples for S3. (`issue 402 <https://github.com/boto/boto3/pull/402>`__)
* bugfix:Collections: Fix regression where filters could not be chained. (`issue 401 <https://github.com/boto/boto3/pull/401>`__)
* bugfix:``S3``: Progress callback will be triggered when rewinding stream. (`issue 395 <https://github.com/boto/boto3/pull/395>`__)


1.2.2
=====

* feature:Dependencies: Relax version constraint of ``futures`` to support version 3.x.
* feature:Resources: Allow ``config`` object to be provided when creating resources (`issue 325 <https://github.com/boto/boto3/pull/325>`__)
* feature:Documentation: Add docstrings for resource collections and waiters (`issue 267 <https://github.com/boto/boto3/pull/267>`__, `issue 261 <https://github.com/boto/boto3/pull/261>`__)


1.2.1
=====

* bugfix:setup.cfg: Fix issue in formatting that broke PyPI distributable


1.2.0
=====

* feature:Docstrings: Add docstrings for resource identifiers, attributes, references, and subresources. (`issue 239 <https://github.com/boto/boto3/pull/239>`__)
* feature:``S3``: Add ability to configure host addressing style when making requests to Amazon S3. (`botocore issue 673 <https://github.com/boto/botocore/pull/673>`__)
* bugfix:``IAM``: Fix model issue with attached groups, roles, and policies. (`issue 304 <https://github.com/boto/boto3/pull/304>`__)
* bugfix:``EC2.ServiceResource.create_key_pair``: Fix model issue where creating key pair does not have a ``key_material`` on ``KeyPair`` resource. (`issue 290 <https://github.com/boto/boto3/pull/290>`__)


1.1.4
=====

* bugfix:Identifier: Make resource identifiers immutable. (`issue 246 <https://github.com/boto/boto3/pull/246>`__)
* feature:S3: Both S3 Bucket and Object obtain upload_file() and download_file() (`issue 243 <https://github.com/boto/boto3/pull/243>`__)


1.1.3
=====

* feature:``aws storagegateway``: Add support for resource tagging.
* feature:timeouts: Add support for customizable timeouts.


1.1.2
=====

* feature:``session.Session``: Add ``events`` property to access session's event emitter. (`issue 204 <https://github.com/boto/boto3/pull/204>`__)
* bugfix:``Glacier.Account``: Fix issue with resource model. (`issue 196 <https://github.com/boto/boto3/pull/196>`__)
* bugfix:``DynamoDB``: Fix misspelling of error class to ``DynamoDBOperationNotSupportedError``. (`issue 218 <https://github.com/boto/boto3/pull/218>`__)


1.1.1
=====

* bugfix:``EC2.ServiceResource.create_tags``: Fix issue when creating multiple tags. (`issue 160 <https://github.com/boto/boto3/pull/160>`__)


1.1.0
=====

* bugfix:``EC2.Vpc.filter``: Fix issue with clobbering of ``Filtering`` paramter. (`issue 154 <https://github.com/boto/boto3/pull/154>`__)


0.0.22
======

* bugfix:``s3.client.upload_file``: Fix double invocation of callbacks when using signature version 4. (`issue 133 <https://github.com/boto/boto3/pull/133>`__)
* bugfix:: ``s3.Bucket.load`` (`issue 128 <https://github.com/boto/boto3/pull/128>`__)


0.0.21
======

* bugfix:Installation: Fix regression when installing via older versions of pip on python 2.6. (`issue 132 <https://github.com/boto/boto3/pull/132>`__)


0.0.20
======

* feature:ec2: Update resource model. (`issue 129 <https://github.com/boto/boto3/pull/129>`__)


0.0.19
======

* breakingchange:Collections: Remove the ``page_count`` and ``limit`` arguments from ``all()``. Undocument support for the two arguments in the ``filter()`` method. (`issue 119 <https://github.com/boto/boto3/pull/119>`__)
* feature:DynamoDB: Add batch writer. (`issue 118 <https://github.com/boto/boto3/pull/118>`__)


0.0.18
======

* feature:DynamoDB: Add document level interface for Table resource (`issue 103 <https://github.com/boto/boto3/pull/103>`__)
* feature:DynamoDB: Add ConditionExpression interface for querying and filtering Table resource. (`issue 103 <https://github.com/boto/boto3/pull/103>`__)
* feature:Clients: Add support for passing of ``botocore.client.Config`` object to instantiation of clients.


0.0.17
======

* feature:Botocore: Update to Botocore 0.107.0.


0.0.16
======

* bugfix:Packaging: Fix release sdist and whl files from 0.0.15.
* feature:Amazon Dynamodb: Add resource model for Amazon DynamoDB.


0.0.15
======

* bugfix:Packaging: Fix an issue with the Amazon S3 ``upload_file`` and ``download_file`` customization. (`issue 85 <https://github.com/boto/boto3/pull/85>`__)
* bugfix:Resource: Fix an issue with the Amazon S3 ``BucketNofitication`` resource.
* feature:Botocore: Update to Botocore 0.103.0.


0.0.14
======

* feature:Resources: Update to the latest resource models for
* feature:Amazon S3: Add an ``upload_file`` and ``download_file`` to S3 clients that transparently handle parallel multipart transfers.
* feature:Botocore: Update to Botocore 0.102.0.


0.0.13
======

* feature:Botocore: Update to Botocore 0.100.0.


0.0.12
======

* feature:Resources: Add the ability to load resource data from a ``has`` relationship. This saves a call to ``load`` when available, and otherwise fixes a problem where there was no way to get at certain resource data. (`issue 74 <https://github.com/boto/boto3/pull/72>`__,
* feature:Botocore: Update to Botocore 0.99.0


0.0.11
======

* feature:Resources: Add Amazon EC2 support for ClassicLink actions and add a delete action to EC2 ``Volume`` resources.
* feature:Resources: Add a ``load`` operation and ``user`` reference to AWS IAM's ``CurrentUser`` resource. (`issue 72 <https://github.com/boto/boto3/pull/72>`__,
* feature:Resources: Add resources for AWS IAM managed policies. (`issue 71 <https://github.com/boto/boto3/pull/71>`__)
* feature:Botocore: Update to Botocore 0.97.0


0.0.10
======

* bugfix:Documentation: Name collisions are now handled at the resource model layer instead of the factory, meaning that the documentation now uses the correct names. (`issue 67 <https://github.com/boto/boto3/pull/67>`__)
* feature:Session: Add a ``region_name`` option when creating a session. (`issue 69 <https://github.com/boto/boto3/pull/69>`__, `issue 21 <https://github.com/boto/boto3/issues/21>`__)
* feature:Botocore: Update to Botocore 0.94.0


0.0.9
=====

* feature:Botocore: Update to Botocore 0.92.0


0.0.8
=====

* bugfix:Resources: Fix Amazon S3 resource identifier order. (`issue 62 <https://github.com/boto/boto3/pull/62>`__)
* bugfix:Resources: Fix collection resource hydration path. (`issue 61 <https://github.com/boto/boto3/pull/61>`__)
* bugfix:Resources: Re-enable service-level access to all resources, allowing e.g. ``obj = s3.Object('bucket', 'key')``. (`issue 60 <https://github.com/boto/boto3/pull/60>`__)
* feature:Botocore: Update to Botocore 0.87.0


0.0.7
=====

* feature:Resources: Enable support for Amazon Glacier.
* feature:Resources: Support plural references and nested JMESPath queries for data members when building parameters and identifiers. (`issue 52 <https://github.com/boto/boto3/pull/52>`__)
* feature:Resources: Update to the latest resource JSON format. This is a **backward-incompatible** change as not all resources are exposed at the service level anymore. For example, ``s3.Object('bucket', 'key')`` is now ``s3.Bucket('bucket').Object('key')``. (`issue 51 <https://github.com/boto/boto3/pull/51>`__)
* feature:Resources: Make ``resource.meta`` a proper object. This allows you to do things like ``resource.meta.client``. This is a **backward- incompatible** change. (`issue 45 <https://github.com/boto/boto3/pull/45>`__)
* feature:Dependency: Update to JMESPath 0.6.1
* feature:Botocore: Update to Botocore 0.86.0


0.0.6
=====

* feature:Amazon SQS: Add ``purge`` action to queue resources
* feature:Waiters: Add documentation for client and resource waiters (`issue 44 <https://github.com/boto/boto3/pull/44>`__)
* feature:Waiters: Add support for resource waiters (`issue 43 <https://github.com/boto/boto3/pull/43>`__)
* bugfix:Installation: Remove dependency on the unused ``six`` module (`issue 42 <https://github.com/boto/boto3/pull/42>`__)
* feature:Botocore: Update to Botocore 0.80.0


0.0.5
=====

* feature:Resources: Add support for batch actions on collections. (`issue 32 <https://github.com/boto/boto3/pull/32>`__)
* feature:Botocore: Update to Botocore 0.78.0


0.0.4
=====

* feature:Botocore: Update to Botocore 0.77.0
* feature:EC2: Update `Amazon EC2 <http
* feature:Resources: Support `belongsTo` resource reference as well as `path` specified in an action's resource definition.
* bugfix:SQS: Fix an issue accessing SQS message bodies (`issue 33 <https://github.com/boto/boto3/issues/33>`__)


0.0.3
=====

* feature:Botocore: Update to Botocore 0.76.0.


0.0.2
=====

* feature:Resources: Adds resources for `AWS CloudFormation <http://aws.amazon.com/cloudformation/>`_ and `AWS OpsWorks <http://aws.amazon.com/opsworks/>`_.
* feature:Botocore: Update to Botocore 0.73.0 and JMESPath 0.5.0
* feature:Clients: Adds support for `AWS CodeDeploy <http://aws.amazon.com/codedeploy/>`_, `AWS Config <http://aws.amazon.com/config/>`_, `AWS KMS <http://aws.amazon.com/kms/>`_, `AWS Lambda <http://aws.amazon.com/lambda/>`_.
* feature:UserAgent: Make requests with a customized HTTP user-agent


0.0.1
=====

* feature:Resources: Supports S3, EC2, SQS, SNS, and IAM resources
* feature:Clients: Supports low-level clients for most services

