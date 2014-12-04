Changelog
=========

0.0.4 - 2014-12-04
------------------

* feature: Update to Botocore 0.77.0

  * Add support for Kinesis PutRecords operation. It writes multiple
    data records from a producer into an Amazon Kinesis stream in a
    single call.
  * Add support for IAM GetAccountAuthorizationDetails operation. It
    retrieves information about all IAM users, groups, and roles in
    your account, including their relationships to one another and
    their attached policies.
  * Add support for updating the comment of a Route53 hosted zone.
  * Fix base64 serialization for JSON protocol services.
  * Fix issue where certain timestamps were not being accepted as valid input
  (`botocore issue 389 <https://github.com/boto/botocore/pull/389>`__)

* feature: Update `Amazon EC2 <http://aws.amazon.com/ec2/>`_ resource model.
* feature: Support `belongsTo` resource reference as well as `path`
  specified in an action's resource definition.
* bugfix: Fix an issue accessing SQS message bodies
  (`issue 33 <https://github.com/boto/boto3/issues/33>`__)

0.0.3 - 2014-11-26
------------------

* feature: Update to Botocore 0.76.0.

  * Add support for using AWS Data Pipeline templates to create
    pipelines and bind values to parameters in the pipeline
  * Add support to Amazon Elastic Transcoder client for encryption of files
    in Amazon S3.
  * Fix issue where Amazon S3 requests were not being
    resigned correctly when using Signature Version 4.
    (`botocore issue 388 <https://github.com/boto/botocore/pull/388>`__)
  * Add support for custom response parsing in Botocore clients.
    (`botocore issue 387 <https://github.com/boto/botocore/pull/387>`__)

0.0.2 - 2014-11-20
------------------

* Adds resources for
  `AWS CloudFormation <http://aws.amazon.com/cloudformation/>`_ and
  `AWS OpsWorks <http://aws.amazon.com/opsworks/>`_.
* Update to Botocore 0.73.0 and JMESPath 0.5.0
* Adds support for
  `AWS CodeDeploy <http://aws.amazon.com/codedeploy/>`_,
  `AWS Config <http://aws.amazon.com/config/>`_,
  `AWS KMS <http://aws.amazon.com/kms/>`_,
  `AWS Lambda <http://aws.amazon.com/lambda/>`_.
* Make requests with a customized HTTP user-agent

0.0.1 - 2014-11-11
------------------

* Initial developer preview refresh of Boto 3
* Supports S3, EC2, SQS, SNS, and IAM resources
* Supports low-level clients for most services
