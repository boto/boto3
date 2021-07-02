=========
CHANGELOG
=========

1.17.105
========

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``ec2``: [``botocore``] This release removes network-insights-boundary


1.17.104
========

* api-change:``sagemaker``: [``botocore``] SageMaker model registry now supports up to 5 containers and associated environment variables.
* api-change:``sqs``: [``botocore``] Documentation updates for Amazon SQS.
* api-change:``ec2``: [``botocore``] Adding a new reserved field to support future infrastructure improvements for Amazon EC2 Fleet.


1.17.103
========

* api-change:``autoscaling``: [``botocore``] Amazon EC2 Auto Scaling infrastructure improvements and optimizations.
* api-change:``kendra``: [``botocore``] Amazon Kendra Enterprise Edition now offered in smaller more granular units to enable customers with smaller workloads. Virtual Storage Capacity units now offer scaling in increments of 100,000 documents (up to 30GB) per unit and Virtual Query Units offer scaling increments of 8,000 queries per day.
* api-change:``mediapackage-vod``: [``botocore``] Add support for Widevine DRM on CMAF packaging configurations. Both Widevine and FairPlay DRMs can now be used simultaneously, with CBCS encryption.
* api-change:``ssm-contacts``: [``botocore``] Fixes the tag key length range to 128 chars,  tag value length to 256 chars; Adds support for UTF-8 chars for contact and channel names, Allows users to unset name in UpdateContact API; Adds throttling exception to StopEngagement API, validation exception to APIs UntagResource, ListTagsForResource
* api-change:``databrew``: [``botocore``] Adds support for the output of job results to the AWS Glue Data Catalog.
* api-change:``servicediscovery``: [``botocore``] AWS Cloud Map now allows configuring the TTL of the SOA record for a hosted zone to control the negative caching for new services.


1.17.102
========

* api-change:``sagemaker``: [``botocore``] Sagemaker Neo now supports running compilation jobs using customer's Amazon VPC
* api-change:``glue``: [``botocore``] Add JSON Support for Glue Schema Registry
* api-change:``redshift``: [``botocore``] Added InvalidClusterStateFault to the DisableLogging API, thrown when calling the API on a non available cluster.
* api-change:``mediaconvert``: [``botocore``] MediaConvert adds support for HDR10+, ProRes 4444,  and XAVC outputs, ADM/DAMF support for Dolby Atmos ingest, and alternative audio and WebVTT caption ingest via HLS inputs. MediaConvert also now supports creating trickplay outputs for Roku devices for HLS, CMAF, and DASH output groups.


1.17.101
========

* api-change:``proton``: [``botocore``] Added waiters for template registration, service operations, and environment deployments.
* api-change:``amplifybackend``: [``botocore``] Imports an existing backend authentication resource.
* api-change:``snowball``: [``botocore``] AWS Snow Family customers can remotely monitor and operate their connected AWS Snowcone devices. AWS Snowball Edge Storage Optimized customers can now import and export their data using NFS.


1.17.100
========

* api-change:``chime``: [``botocore``] Adds EventIngestionUrl field to MediaPlacement
* api-change:``cloud9``: [``botocore``] Minor update to AWS Cloud9 documentation to allow correct parsing of outputted text
* api-change:``connect``: [``botocore``] Released Amazon Connect quick connects management API for general availability (GA). For more information, see https://docs.aws.amazon.com/connect/latest/APIReference/Welcome.html
* api-change:``dax``: [``botocore``] Add support for encryption in transit to DAX clusters.
* api-change:``wafv2``: [``botocore``] Added support for 15 new text transformation.
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports SharePoint 2013 and SharePoint 2016 when using a SharePoint data source.
* api-change:``securityhub``: [``botocore``] Added new resource details for ECS clusters and ECS task definitions. Added additional information for S3 buckets, Elasticsearch domains, and API Gateway V2 stages.
* api-change:``transfer``: [``botocore``] Customers can successfully use legacy clients with Transfer Family endpoints enabled for FTPS and FTP behind routers, firewalls, and load balancers by providing a Custom IP address used for data channel communication.
* api-change:``codebuild``: [``botocore``] BucketOwnerAccess is currently not supported


1.17.99
=======

* api-change:``docdb``: [``botocore``] DocumentDB documentation-only edits
* api-change:``cloud9``: [``botocore``] Updated documentation for CreateEnvironmentEC2 to explain that because Amazon Linux AMI has ended standard support as of December 31, 2020, we recommend you choose Amazon Linux 2--which includes long term support through 2023--for new AWS Cloud9 environments.
* api-change:``quicksight``: [``botocore``] Releasing new APIs for AWS QuickSight Folders
* api-change:``mediatailor``: [``botocore``] Update GetChannelSchedule to return information on ad breaks.
* api-change:``cloudfront``: [``botocore``] Amazon CloudFront adds support for a new security policy, TLSv1.2_2021.
* api-change:``license-manager``: [``botocore``] AWS License Manager now allows license administrators and end users to communicate to each other by setting custom status reasons when updating the status on a granted license.
* api-change:``ec2``: [``botocore``] This release adds support for provisioning your own IP (BYOIP) range in multiple regions. This feature is in limited Preview for this release. Contact your account manager if you are interested in this feature.
* api-change:``events``: [``botocore``] Added the following parameters to ECS targets: CapacityProviderStrategy, EnableECSManagedTags, EnableExecuteCommand, PlacementConstraints, PlacementStrategy, PropagateTags, ReferenceId, and Tags
* api-change:``cloudsearch``: [``botocore``] This release replaces previous generation CloudSearch instances with equivalent new instances that provide better stability at the same price.
* api-change:``codeguru-reviewer``: [``botocore``] Adds support for S3 based full repository analysis and changed lines scan.


1.17.98
=======

* api-change:``cloudformation``: [``botocore``] CloudFormation registry service now supports 3rd party public type sharing


1.17.97
=======

* api-change:``kendra``: [``botocore``] Amazon Kendra now supports the indexing of web documents for search through the web crawler.
* api-change:``sagemaker``: [``botocore``] Enable ml.g4dn instance types for SageMaker Batch Transform and SageMaker Processing
* api-change:``rds``: [``botocore``] This release enables Database Activity Streams for RDS Oracle
* api-change:``chime``: [``botocore``] This release adds a new API UpdateSipMediaApplicationCall, to update an in-progress call for SipMediaApplication.


1.17.96
=======

* api-change:``kms``: [``botocore``] Adds support for multi-Region keys
* api-change:``ec2``: [``botocore``] This release adds support for VLAN-tagged network traffic over an Elastic Network Interface (ENI). This feature is in limited Preview for this release. Contact your account manager if you are interested in this feature.
* api-change:``rds``: [``botocore``] This release enables fast cloning in Aurora Serverless. You can now clone between Aurora Serverless clusters and Aurora Provisioned clusters.
* api-change:``mediatailor``: [``botocore``] Adds AWS Secrets Manager Access Token Authentication for Source Locations


1.17.95
=======

* api-change:``redshift-data``: [``botocore``] Redshift Data API service now supports SQL parameterization.
* api-change:``connect``: [``botocore``] This release adds new sets of APIs: AssociateBot, DisassociateBot, and ListBots. You can use it to programmatically add an Amazon Lex bot or Amazon Lex V2 bot on the specified Amazon Connect instance
* api-change:``ec2``: [``botocore``] EC2 M5n, M5dn, R5n, R5dn metal instances with 100 Gbps network performance and Elastic Fabric Adapter (EFA) for ultra low latency
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version


1.17.94
=======

* api-change:``lookoutmetrics``: [``botocore``] Added "LEARNING" status for anomaly detector and updated description for "Offset" parameter in MetricSet APIs.
* api-change:``iotanalytics``: [``botocore``] Adds support for data store partitions.
* api-change:``greengrassv2``: [``botocore``] We have verified the APIs being released here and are ready to release


1.17.93
=======

* api-change:``ec2``: [``botocore``] Amazon EC2 adds new AMI property to flag outdated AMIs
* api-change:``medialive``: [``botocore``] AWS MediaLive now supports OCR-based conversion of DVB-Sub and SCTE-27 image-based source captions to WebVTT, and supports ingest of ad avail decorations in HLS input manifests.
* api-change:``mediaconnect``: [``botocore``] When you enable source failover, you can now designate one of two sources as the primary source. You can choose between two failover modes to prevent any disruption to the video stream. Merge combines the sources into a single stream. Failover allows switching between a primary and a backup stream.


1.17.92
=======

* api-change:``sagemaker``: [``botocore``] Using SageMaker Edge Manager with AWS IoT Greengrass v2 simplifies accessing, maintaining, and deploying models to your devices. You can now create deployable IoT Greengrass components during edge packaging jobs. You can choose to create a device fleet with or without creating an AWS IoT role alias.
* api-change:``appmesh``: [``botocore``] AppMesh now supports additional routing capabilities in match and rewrites for Gateway Routes and Routes. Additionally, App Mesh also supports specifying DNS Response Types in Virtual Nodes.
* api-change:``redshift``: [``botocore``] Added InvalidClusterStateFault to the ModifyAquaConfiguration API, thrown when calling the API on a non available cluster.
* api-change:``chime``: [``botocore``] This SDK release adds support for UpdateAccount API to allow users to update their default license on Chime account.
* api-change:``ec2``: [``botocore``] This release adds a new optional parameter connectivityType (public, private) for the CreateNatGateway API. Private NatGateway does not require customers to attach an InternetGateway to the VPC and can be used for communication with other VPCs and on-premise networks.
* api-change:``ram``: [``botocore``] AWS Resource Access Manager (RAM) is releasing new field isResourceTypeDefault in ListPermissions and GetPermission response, and adding permissionArn parameter to GetResourceShare request to filter by permission attached
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Release BatchGetRecord API for AWS SageMaker Feature Store Runtime.
* api-change:``cognito-idp``: [``botocore``] Amazon Cognito now supports targeted sign out through refresh token revocation
* api-change:``appflow``: [``botocore``] Adding MAP_ALL task type support.
* api-change:``managedblockchain``: [``botocore``] This release supports KMS customer-managed Customer Master Keys (CMKs) on member-specific Hyperledger Fabric resources.


1.17.91
=======

* api-change:``transfer``: [``botocore``] Documentation updates for the AWS Transfer Family service.
* api-change:``personalize-events``: [``botocore``] Support for unstructured text inputs in the items dataset to to automatically extract key information from product/content description as an input when creating solution versions.
* api-change:``proton``: [``botocore``] This is the initial SDK release for AWS Proton
* api-change:``kendra``: [``botocore``] AWS Kendra now supports checking document status.


1.17.90
=======

* api-change:``fsx``: [``botocore``] This release adds support for auditing end-user access to files, folders, and file shares using Windows event logs, enabling customers to meet their security and compliance needs.
* api-change:``servicecatalog``: [``botocore``] increase max pagesize for List/Search apis
* api-change:``macie2``: [``botocore``] This release of the Amazon Macie API introduces stricter validation of S3 object criteria for classification jobs.
* api-change:``cognito-idp``: [``botocore``] Documentation updates for cognito-idp


1.17.89
=======

* api-change:``sagemaker``: [``botocore``] AWS SageMaker - Releasing new APIs related to Callback steps in model building pipelines. Adds experiment integration to model building pipelines.
* api-change:``glue``: [``botocore``] Add SampleSize variable to S3Target to enable s3-sampling feature through API.
* api-change:``personalize``: [``botocore``] Update regex validation in kmsKeyArn and s3 path API parameters for AWS Personalize APIs
* api-change:``eks``: [``botocore``] Added updateConfig option that allows customers to control upgrade velocity in Managed Node Group.


1.17.88
=======

* api-change:``rds``: [``botocore``] Documentation updates for RDS: fixing an outdated link to the RDS documentation in DBInstance$DBInstanceStatus
* api-change:``pi``: [``botocore``] The new GetDimensionKeyDetails action retrieves the attributes of the specified dimension group for a DB instance or data source.
* api-change:``cloudtrail``: [``botocore``] AWS CloudTrail supports data events on new service resources, including Amazon DynamoDB tables and S3 Object Lambda access points.
* api-change:``medialive``: [``botocore``] Add support for automatically setting the H.264 adaptive quantization and GOP B-frame fields.
* api-change:``autoscaling``: [``botocore``] Documentation updates for Amazon EC2 Auto Scaling
* api-change:``qldb``: [``botocore``] Documentation updates for Amazon QLDB


1.17.87
=======

* api-change:``s3``: [``botocore``] S3 Inventory now supports Bucket Key Status
* api-change:``s3control``: [``botocore``] Amazon S3 Batch Operations now supports S3 Bucket Keys.
* api-change:``route53resolver``: [``botocore``] Documentation updates for Route 53 Resolver
* api-change:``ssm``: [``botocore``] Documentation updates for ssm to fix customer reported issue
* api-change:``forecast``: [``botocore``] Added optional field AutoMLOverrideStrategy to CreatePredictor API that allows users to customize AutoML strategy. If provided in CreatePredictor request, this field is visible in DescribePredictor and GetAccuracyMetrics responses.


1.17.86
=======

* api-change:``autoscaling``: [``botocore``] You can now launch EC2 instances with GP3 volumes when using Auto Scaling groups with Launch Configurations
* api-change:``lightsail``: [``botocore``] Documentation updates for Lightsail
* api-change:``ecs``: [``botocore``] Documentation updates for Amazon ECS.
* api-change:``docdb``: [``botocore``] This SDK release adds support for DocDB global clusters.
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``braket``: [``botocore``] Introduction of a RETIRED status for devices.


1.17.85
=======

* api-change:``sns``: [``botocore``] This release adds SMS sandbox in Amazon SNS and the ability to view all configured origination numbers. The SMS sandbox provides a safe environment for sending SMS messages, without risking your reputation as an SMS sender.
* api-change:``polly``: [``botocore``] Amazon Polly adds new Canadian French voice - Gabrielle. Gabrielle is available as Neural voice only.
* api-change:``ec2``: [``botocore``] Added idempotency to CreateNetworkInterface using the ClientToken parameter.
* api-change:``iotwireless``: [``botocore``] Added six new public customer logging APIs to allow customers to set/get/reset log levels at resource type and resource id level. The log level set from the APIs will be used to filter log messages that can be emitted to CloudWatch in customer accounts.
* api-change:``servicediscovery``: [``botocore``] Bugfixes - The DiscoverInstances API operation now provides an option to return all instances for health-checked services when there are no healthy instances available.


1.17.84
=======

* api-change:``lookoutmetrics``: [``botocore``] Allowing dot(.) character in table name for RDS and Redshift as source connector.
* api-change:``location``: [``botocore``] Adds support for calculation of routes, resource tagging and customer provided KMS keys.
* api-change:``datasync``: [``botocore``] Added SecurityDescriptorCopyFlags option that allows for control of which components of SMB security descriptors are copied from source to destination objects.


1.17.83
=======

* api-change:``iotevents-data``: [``botocore``] Releasing new APIs for AWS IoT Events Alarms
* api-change:``devicefarm``: [``botocore``] Introduces support for using our desktop testing service with applications hosted within your Virtual Private Cloud (VPC).
* api-change:``kendra``: [``botocore``] Amazon Kendra now suggests popular queries in order to help guide query typing and help overall accuracy.
* api-change:``iotsitewise``: [``botocore``] IoT SiteWise Monitor Portal API updates to add alarms feature configuration.
* api-change:``resource-groups``: [``botocore``] Documentation updates for Resource Groups.
* api-change:``lightsail``: [``botocore``] Documentation updates for Lightsail
* api-change:``iotevents``: [``botocore``] Releasing new APIs for AWS IoT Events Alarms
* api-change:``fsx``: [``botocore``] This release adds LZ4 data compression support to FSx for Lustre to reduce storage consumption of both file system storage and file system backups.
* api-change:``sqs``: [``botocore``] Documentation updates for Amazon SQS for General Availability of high throughput for FIFO queues.


1.17.82
=======

* api-change:``ec2``: [``botocore``] This release removes resource ids and tagging support for VPC security group rules.


1.17.81
=======

* api-change:``qldb``: [``botocore``] Support STANDARD permissions mode in CreateLedger and DescribeLedger. Add UpdateLedgerPermissionsMode to update permissions mode on existing ledgers.
* api-change:``cloudfront``: [``botocore``] Documentation fix for CloudFront
* api-change:``outposts``: [``botocore``] Add ConflictException to DeleteOutpost, CreateOutpost
* api-change:``mwaa``: [``botocore``] Adds scheduler count selection for Environments using Airflow version 2.0.2 or later.
* api-change:``ec2``: [``botocore``] This release adds resource ids and tagging support for VPC security group rules.
* api-change:``ecs``: [``botocore``] The release adds support for registering External instances to your Amazon ECS clusters.
* api-change:``acm-pca``: [``botocore``] This release enables customers to store CRLs in S3 buckets with Block Public Access enabled. The release adds the S3ObjectAcl parameter to the CreateCertificateAuthority and UpdateCertificateAuthority APIs to allow customers to choose whether their CRL will be publicly available.


1.17.80
=======

* api-change:``transfer``: [``botocore``] AWS Transfer Family customers can now use AWS Managed Active Directory or AD Connector to authenticate their end users, enabling seamless migration of file transfer workflows that rely on AD authentication, without changing end users' credentials or needing a custom authorizer.
* api-change:``iot``: [``botocore``] This release includes support for a new feature: Job templates for AWS IoT Device Management Jobs. The release includes job templates as a new resource and APIs for managing job templates.
* api-change:``workspaces``: [``botocore``] Adds support for Linux device types in WorkspaceAccessProperties


1.17.79
=======

* api-change:``quicksight``: [``botocore``] Add new parameters on RegisterUser and UpdateUser APIs to assign or update external ID associated to QuickSight users federated through web identity.
* api-change:``ce``: [``botocore``] Introduced FindingReasonCodes, PlatformDifferences, DiskResourceUtilization and NetworkResourceUtilization to GetRightsizingRecommendation action
* api-change:``compute-optimizer``: [``botocore``] Adds support for 1) additional instance types, 2) additional instance metrics, 3) finding reasons for instance recommendations, and 4) platform differences between a current instance and a recommended instance type.
* api-change:``ec2``: [``botocore``] This release adds support for creating and managing EC2 On-Demand Capacity Reservations on Outposts.
* api-change:``logs``: [``botocore``] This release provides dimensions and unit support for metric filters.


1.17.78
=======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3
* api-change:``forecast``: [``botocore``] Updated attribute statistics in DescribeDatasetImportJob response to support Long values
* api-change:``opsworkscm``: [``botocore``] New PUPPET_API_CRL attribute returned by DescribeServers API; new EngineVersion of 2019 available for Puppet Enterprise servers.


1.17.77
=======

* api-change:``personalize``: [``botocore``] Added new API to stop a solution version creation that is pending or in progress for Amazon Personalize
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``quicksight``: [``botocore``] Add ARN based Row Level Security support to CreateDataSet/UpdateDataSet APIs.
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).


1.17.76
=======

* api-change:``kinesisanalyticsv2``: [``botocore``] Kinesis Data Analytics now allows rapid iteration on Apache Flink stream processing through the Kinesis Data Analytics Studio feature.
* api-change:``rekognition``: [``botocore``] Amazon Rekognition Custom Labels adds support for customer managed encryption, using AWS Key Management Service, of image files copied into the service and files written back to the customer.
* api-change:``iam``: [``botocore``] Add pagination to ListUserTags operation
* api-change:``eks``: [``botocore``] Update the EKS AddonActive waiter.
* api-change:``autoscaling``: [``botocore``] With this release, customers can easily use Predictive Scaling as a policy directly through Amazon EC2 Auto Scaling configurations to proactively scale their applications ahead of predicted demand.
* api-change:``lightsail``: [``botocore``] Documentation updates for Amazon Lightsail.


1.17.75
=======

* api-change:``support``: [``botocore``] Documentation updates for support
* api-change:``apprunner``: [``botocore``] AWS App Runner is a service that provides a fast, simple, and cost-effective way to deploy from source code or a container image directly to a scalable and secure web application in the AWS Cloud.
* api-change:``compute-optimizer``: [``botocore``] This release enables compute optimizer to support exporting  recommendations to Amazon S3 for EBS volumes and Lambda Functions.
* api-change:``personalize``: [``botocore``] Amazon Personalize now supports the ability to optimize a solution for a custom objective in addition to maximizing relevance.
* api-change:``license-manager``: [``botocore``] AWS License Manager now supports periodic report generation.
* api-change:``iotsitewise``: [``botocore``] Documentation updates for AWS IoT SiteWise.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version


1.17.74
=======

* api-change:``mediaconnect``: [``botocore``] MediaConnect now supports JPEG XS for AWS Cloud Digital Interface (AWS CDI) uncompressed workflows, allowing you to establish a bridge between your on-premises live video network and the AWS Cloud.
* api-change:``sagemaker-a2i-runtime``: [``botocore``] Documentation updates for Amazon A2I Runtime model
* api-change:``applicationcostprofiler``: [``botocore``] APIs for AWS Application Cost Profiler.
* api-change:``neptune``: [``botocore``] Neptune support for CopyTagsToSnapshots
* api-change:``iotdeviceadvisor``: [``botocore``] AWS IoT Core Device Advisor is fully managed test capability for IoT devices. Device manufacturers can use Device Advisor to test their IoT devices for reliable and secure connectivity with AWS IoT.
* api-change:``elasticache``: [``botocore``] Documentation updates for elasticache


1.17.73
=======

* api-change:``events``: [``botocore``] Update InputTransformer variable limit from 10 to 100 variables.
* enhancement:``s3``: [``botocore``] Block endpoint resolution of clients configured with S3 pseudo-regions (e.g. ``aws-global``, ``s3-external-1``) that will never resolve to a correct access point endpoint.
* api-change:``macie2``: [``botocore``] This release of the Amazon Macie API adds support for defining run-time, S3 bucket criteria for classification jobs. It also adds resources for querying data about AWS resources that Macie monitors.
* api-change:``es``: [``botocore``] Adds support for cold storage.
* api-change:``securityhub``: [``botocore``] Updated descriptions to add notes on array lengths.
* api-change:``detective``: [``botocore``] Updated descriptions of array parameters to add the restrictions on the array and value lengths.
* api-change:``transcribe``: [``botocore``] Transcribe Medical now supports identification of PHI entities within transcripts
* api-change:``imagebuilder``: [``botocore``] Text-only updates for bundled documentation feedback tickets - spring 2021.
* enhancement:FIPS: [``botocore``] Add validation to only attempt to connect to FIPS endpoints with a FIPS pseudo-region if the pseudo-region is explicitly known to the SDK.


1.17.72
=======

* api-change:``ec2``: [``botocore``] High Memory virtual instances are powered by Intel Sky Lake CPUs and offer up to 12TB of memory.


1.17.71
=======

* api-change:``ssm-incidents``: [``botocore``] AWS Systems Manager Incident Manager enables faster resolution of critical application availability and performance issues, management of contacts and post-incident analysis
* api-change:``ssm-contacts``: [``botocore``] AWS Systems Manager Incident Manager enables faster resolution of critical application availability and performance issues, management of contacts and post incident analysis
* api-change:``s3control``: [``botocore``] Documentation updates for Amazon S3-control


1.17.70
=======

* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for Kantar SNAP File Audio Watermarking with a Kantar Watermarking account, and Display Definition Segment(DDS) segment data controls for DVB-Sub caption outputs.
* api-change:``ecs``: [``botocore``] This release contains updates for Amazon ECS.
* api-change:``codeartifact``: [``botocore``] Documentation updates for CodeArtifact
* api-change:``eks``: [``botocore``] This release updates create-nodegroup and update-nodegroup-config APIs for adding/updating taints on managed nodegroups.
* api-change:``iotwireless``: [``botocore``] Add three new optional fields to support filtering and configurable sub-band in WirelessGateway APIs. The filtering is for all the RF region supported. The sub-band configuration is only applicable to LoRa gateways of US915 or AU915 RF region.
* api-change:``ssm``: [``botocore``] This release adds new APIs to associate, disassociate and list related items in SSM OpsCenter; and this release adds DisplayName as a version-level attribute for SSM Documents and introduces two new document types: ProblemAnalysis, ProblemAnalysisTemplate.
* api-change:``kinesisanalyticsv2``: [``botocore``] Amazon Kinesis Analytics now supports ListApplicationVersions and DescribeApplicationVersion API for Apache Flink applications
* api-change:``config``: [``botocore``] Adds paginator to multiple APIs: By default, the paginator allows user to iterate over the results and allows the CLI to return up to 1000 results.


1.17.69
=======

* api-change:``lakeformation``: [``botocore``] This release adds Tag Based Access Control to AWS Lake Formation service
* api-change:``lookoutmetrics``: [``botocore``] Enforcing UUID style for parameters that are already in UUID format today. Documentation specifying eventual consistency of lookoutmetrics resources.
* api-change:``connect``: [``botocore``] Adds tagging support for Connect APIs CreateIntegrationAssociation and CreateUseCase.


1.17.68
=======

* api-change:``servicediscovery``: [``botocore``] Bugfix: Improved input validation for RegisterInstance action, InstanceId field
* api-change:``kafka``: [``botocore``] IAM Access Control for Amazon MSK enables you to create clusters that use IAM to authenticate clients and to allow or deny Apache Kafka actions for those clients.
* api-change:``ssm``: [``botocore``] SSM feature release - ChangeCalendar integration with StateManager.
* api-change:``snowball``: [``botocore``] AWS Snow Family adds APIs for ordering and managing Snow jobs with long term pricing


1.17.67
=======

* api-change:``auditmanager``: [``botocore``] This release updates the CreateAssessmentFrameworkControlSet and UpdateAssessmentFrameworkControlSet API data types. For both of these data types, the control set name is now a required attribute.
* api-change:``nimble``: [``botocore``] Documentation Updates for Amazon Nimble Studio.
* api-change:``kinesisanalyticsv2``: [``botocore``] Amazon Kinesis Analytics now supports RollbackApplication for Apache Flink applications to revert the application to the previous running version
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot now provides the ability to automatically deploy the best model to an endpoint


1.17.66
=======

* api-change:``finspace``: [``botocore``] Documentation updates for FinSpace API.
* api-change:``finspace-data``: [``botocore``] Documentation updates for FinSpaceData API.


1.17.65
=======

* api-change:``devops-guru``: [``botocore``] Added GetCostEstimation and StartCostEstimation to get the monthly resource usage cost and added ability to view resource health by AWS service name and to search insights be AWS service name.
* api-change:``acm-pca``: [``botocore``] This release adds the KeyStorageSecurityStandard parameter to the CreateCertificateAuthority API to allow customers to mandate a security standard to which the CA key will be stored within.
* api-change:``health``: [``botocore``] Documentation updates for health
* api-change:``chime``: [``botocore``] This release adds the ability to search for and order international phone numbers for Amazon Chime SIP media applications.
* api-change:``sagemaker``: [``botocore``] Enable retrying Training and Tuning Jobs that fail with InternalServerError by setting RetryStrategy.


1.17.64
=======

* api-change:``finspace-data``: [``botocore``] Update FinSpace Data serviceAbbreviation


1.17.63
=======

* api-change:``finspace-data``: [``botocore``] This is the initial SDK release for the data APIs for Amazon FinSpace. Amazon FinSpace is a data management and analytics application for the financial services industry (FSI).
* api-change:``mturk``: [``botocore``] Update mturk client to latest version
* api-change:``chime``: [``botocore``] Added new BatchCreateChannelMembership API to support multiple membership creation for channels
* api-change:``finspace``: [``botocore``] This is the initial SDK release for the management APIs for Amazon FinSpace. Amazon FinSpace is a data management and analytics service for the financial services industry (FSI).
* api-change:``securityhub``: [``botocore``] Updated ASFF to add the following new resource details objects: AwsEc2NetworkAcl, AwsEc2Subnet, and AwsElasticBeanstalkEnvironment.


1.17.62
=======

* api-change:``personalize``: [``botocore``] Update URL for dataset export job documentation.
* api-change:``marketplace-catalog``: [``botocore``] Allows user defined names for Changes in a ChangeSet. Users can use ChangeNames to reference properties in another Change within a ChangeSet. This feature allows users to make changes to an entity when the entity identifier is not yet available while constructing the StartChangeSet request.
* api-change:``forecast``: [``botocore``] Added new DeleteResourceTree operation that helps in deleting all the child resources of a given resource including the given resource.
* api-change:``robomaker``: [``botocore``] Adds ROS2 Foxy as a supported Robot Software Suite Version and Gazebo 11 as a supported Simulation Software Suite Version
* api-change:``cloudfront``: [``botocore``] CloudFront now supports CloudFront Functions, a native feature of CloudFront that enables you to write lightweight functions in JavaScript for high-scale, latency-sensitive CDN customizations.
* api-change:``customer-profiles``: [``botocore``] This release introduces GetMatches and MergeProfiles APIs to fetch and merge duplicate profiles


1.17.61
=======

* api-change:``macie2``: [``botocore``] The Amazon Macie API now provides S3 bucket metadata that indicates whether a bucket policy requires server-side encryption of objects when objects are uploaded to the bucket.
* api-change:``organizations``: [``botocore``] Minor text updates for AWS Organizations API Reference
* api-change:``ecs``: [``botocore``] Add support for EphemeralStorage on TaskDefinition and TaskOverride
* api-change:``chime``: [``botocore``] Increase AppInstanceUserId length to 64 characters


1.17.60
=======

* api-change:``connect``: [``botocore``] Updated max number of tags that can be attached from 200 to 50. MaxContacts is now an optional parameter for the UpdateQueueMaxContact API.
* api-change:``mediapackage-vod``: [``botocore``] MediaPackage now offers the option to place your Sequence Parameter Set (SPS), Picture Parameter Set (PPS), and Video Parameter Set (VPS) encoder metadata in every video segment instead of in the init fragment for DASH and CMAF endpoints.
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio is a virtual studio service that empowers visual effects, animation, and interactive content teams to create content securely within a scalable, private cloud service.
* api-change:``iotsitewise``: [``botocore``] AWS IoT SiteWise interpolation API will get interpolated values for an asset property per specified time interval during a period of time.
* api-change:``cloudformation``: [``botocore``] Add CallAs parameter to GetTemplateSummary to enable use with StackSets delegated administrator integration


1.17.59
=======

* api-change:``auditmanager``: [``botocore``] This release restricts using backslashes in control, assessment, and framework names. The controlSetName field of the UpdateAssessmentFrameworkControlSet API now allows strings without backslashes.


1.17.58
=======

* api-change:``ec2``: [``botocore``] Adding support for Red Hat Enterprise Linux with HA for Reserved Instances.
* api-change:``iotwireless``: [``botocore``] Add a new optional field MessageType to support Sidewalk devices in SendDataToWirelessDevice API
* api-change:``kinesisanalyticsv2``: [``botocore``] Amazon Kinesis Data Analytics now supports custom application maintenance configuration using UpdateApplicationMaintenanceConfiguration API for Apache Flink applications. Customers will have visibility when their application is under maintenance status using 'MAINTENANCE' application status.
* api-change:``personalize``: [``botocore``] Added support for exporting data imported into an Amazon Personalize dataset to a specified data source (Amazon S3 bucket).
* api-change:``mediaconvert``: [``botocore``] Documentation updates for mediaconvert
* api-change:``codeguru-reviewer``: [``botocore``] Include KMS Key Details in Repository Association APIs to enable usage of customer managed KMS Keys.
* api-change:``glue``: [``botocore``] Adding Kafka Client Auth Related Parameters
* api-change:``eks``: [``botocore``] This release updates existing Amazon EKS input validation so customers will see an InvalidParameterException instead of a ParamValidationError when they enter 0 for minSize and/or desiredSize. It also adds LaunchTemplate information to update responses and a new "CUSTOM" value for AMIType.


1.17.57
=======

* api-change:``mediapackage``: [``botocore``] Add support for Widevine DRM on CMAF origin endpoints. Both Widevine and FairPlay DRMs can now be used simultaneously, with CBCS encryption.
* api-change:``sns``: [``botocore``] Amazon SNS adds two new attributes, TemplateId and EntityId, for using sender IDs to send SMS messages to destinations in India.


1.17.56
=======

* api-change:``forecast``: [``botocore``] This release adds EstimatedTimeRemaining minutes field to the DescribeDatasetImportJob, DescribePredictor, DescribeForecast API response which denotes the time remaining to complete the job IN_PROGRESS.
* api-change:``securityhub``: [``botocore``] Replaced the term "master" with "administrator". Added new actions to replace AcceptInvitation, GetMasterAccount, and DisassociateFromMasterAccount. In Member, replaced MasterId with AdministratorId.
* api-change:``cognito-idp``: [``botocore``] Documentation updates for cognito-idp
* api-change:``elasticache``: [``botocore``] This release introduces log delivery of Redis slow log from Amazon ElastiCache.


1.17.55
=======

* api-change:``detective``: [``botocore``] Added parameters to track the data volume in bytes for a member account. Deprecated the existing parameters that tracked the volume as a percentage of the allowed volume for a behavior graph. Changes reflected in MemberDetails object.
* api-change:``redshift``: [``botocore``] Add operations: AddPartner, DescribePartners, DeletePartner, and UpdatePartnerStatus to support tracking integration status with data partners.
* api-change:``groundstation``: [``botocore``] Support new S3 Recording Config allowing customers to write downlink data directly to S3.
* api-change:``kendra``: [``botocore``] Amazon Kendra now enables users to override index-level boosting configurations for each query.
* api-change:``cloudformation``: [``botocore``] Added support for creating and updating stack sets with self-managed permissions from templates that reference macros.


1.17.54
=======

* api-change:``savingsplans``: [``botocore``] Added support for Amazon SageMaker in Machine Learning Savings Plans
* api-change:``ce``: [``botocore``] Adding support for Sagemaker savings plans in GetSavingsPlansPurchaseRecommendation API


1.17.53
=======

* api-change:``sts``: [``botocore``] STS now supports assume role with Web Identity using JWT token length upto 20000 characters
* api-change:``dms``: [``botocore``] AWS DMS added support of TLS for Kafka endpoint. Added Describe endpoint setting API for DMS endpoints.


1.17.52
=======

* api-change:``mediaconnect``: [``botocore``] For flows that use Listener protocols, you can now easily locate an output's outbound IP address for a private internet. Additionally, MediaConnect now supports the Waiters feature that makes it easier to poll for the status of a flow until it reaches its desired state.
* api-change:``config``: [``botocore``] Add exception for DeleteRemediationConfiguration and DescribeRemediationExecutionStatus
* api-change:``route53``: [``botocore``] Documentation updates for route53
* api-change:``codestar-connections``: [``botocore``] This release adds tagging support for CodeStar Connections Host resources


1.17.51
=======

* api-change:``lightsail``: [``botocore``] Documentation updates for Amazon Lightsail.
* api-change:``sts``: [``botocore``] This release adds the SourceIdentity parameter that can be set when assuming a role.
* api-change:``comprehendmedical``: [``botocore``] The InferICD10CM API now returns TIME_EXPRESSION entities that refer to medical conditions.
* api-change:``rds``: [``botocore``] Clarify that enabling or disabling automated backups causes a brief downtime, not an outage.
* api-change:``redshift``: [``botocore``] Added support to enable AQUA in Amazon Redshift clusters.


1.17.50
=======

* api-change:``fsx``: [``botocore``] Support for cross-region and cross-account backup copies
* api-change:``codebuild``: [``botocore``] AWS CodeBuild now allows you to set the access permissions for build artifacts, project artifacts, and log files that are uploaded to an Amazon S3 bucket that is owned by another account.


1.17.49
=======

* api-change:``redshift``: [``botocore``] Add support for case sensitive table level restore
* api-change:``ec2``: [``botocore``] Add paginator support to DescribeStoreImageTasks and update documentation.
* api-change:``shield``: [``botocore``] CreateProtection now throws InvalidParameterException instead of InternalErrorException when system tags (tag with keys prefixed with "aws:") are passed in.


1.17.48
=======

* api-change:``lookoutequipment``: [``botocore``] This release introduces support for Amazon Lookout for Equipment.
* api-change:``kinesis-video-archived-media``: [``botocore``] Documentation updates for archived.kinesisvideo
* api-change:``robomaker``: [``botocore``] This release allows RoboMaker customers to specify custom tools to run with their simulation job
* api-change:``appstream``: [``botocore``] This release provides support for image updates
* api-change:``ram``: [``botocore``] Documentation updates for AWS RAM resource sharing
* api-change:``customer-profiles``: [``botocore``] Documentation updates for Put-Integration API
* api-change:``autoscaling``: [``botocore``] Amazon EC2 Auto Scaling announces Warm Pools that help applications to scale out faster by pre-initializing EC2 instances and save money by requiring fewer continuously running instances


1.17.47
=======

* api-change:``storagegateway``: [``botocore``] File Gateway APIs now support FSx for Windows as a cloud storage.
* api-change:``accessanalyzer``: [``botocore``] IAM Access Analyzer now analyzes your CloudTrail events to identify actions and services that have been used by an IAM entity (user or role) and generates an IAM policy that is based on that activity.
* api-change:``elasticache``: [``botocore``] This release adds tagging support for all AWS ElastiCache resources except Global Replication Groups.
* api-change:``ivs``: [``botocore``] This release adds support for the Auto-Record to S3 feature. Amazon IVS now enables you to save your live video to Amazon S3.
* api-change:``mgn``: [``botocore``] Add new service - Application Migration Service.


1.17.46
=======

* api-change:``ssm``: [``botocore``] Supports removing a label or labels from a parameter, enables ScheduledEndTime and ChangeDetails for StartChangeRequestExecution API, supports critical/security/other noncompliant count for patch API.
* api-change:``medialive``: [``botocore``] MediaLive VPC outputs update to include Availability Zones, Security groups, Elastic Network Interfaces, and Subnet Ids in channel response
* api-change:``ec2``: [``botocore``] This release adds support for storing EBS-backed AMIs in S3 and restoring them from S3 to enable cross-partition copying of AMIs
* api-change:``cloud9``: [``botocore``] Documentation updates for Cloud9


1.17.45
=======

* api-change:``auditmanager``: [``botocore``] AWS Audit Manager has updated the GetAssessment API operation to include a new response field called userRole. The userRole field indicates the role information and IAM ARN of the API caller.
* api-change:``medialive``: [``botocore``] MediaLive now support HTML5 Motion Graphics overlay
* api-change:``appflow``: [``botocore``] Added destination properties for Zendesk.


1.17.44
=======

* api-change:``mediapackage``: [``botocore``] SPEKE v2 is an upgrade to the existing SPEKE API to support multiple encryption keys, based on an encryption contract selected by the customer.
* api-change:``imagebuilder``: [``botocore``] This release adds support for Block Device Mappings for container image builds, and adds distribution configuration support for EC2 launch templates in AMI builds.


1.17.43
=======

* api-change:``route53resolver``: [``botocore``] Route 53 Resolver DNS Firewall is a firewall service that allows you to filter and regulate outbound DNS traffic for your VPCs.
* api-change:``mediaconvert``: [``botocore``] MediaConvert now supports HLS ingest, sidecar WebVTT ingest, Teletext color & style passthrough to TTML subtitles, TTML to WebVTT subtitle conversion with style, & DRC profiles in AC3 audio.
* api-change:``lightsail``: [``botocore``] - This release adds support for state detail for Amazon Lightsail container services.
* api-change:``kendra``: [``botocore``] AWS Kendra's ServiceNow data source now supports OAuth 2.0 authentication and knowledge article filtering via a ServiceNow query.
* api-change:``lex-models``: [``botocore``] Lex now supports the ja-JP locale
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``fms``: [``botocore``] Added Firewall Manager policy support for AWS Route 53 Resolver DNS Firewall.
* api-change:``ec2``: [``botocore``] VPC Flow Logs Service adds a new API, GetFlowLogsIntegrationTemplate, which generates CloudFormation templates for Athena. For more info, see https://docs.aws.amazon.com/console/vpc/flow-logs/athena
* api-change:``wafv2``: [``botocore``] Added support for ScopeDownStatement for ManagedRuleGroups, Labels, LabelMatchStatement, and LoggingFilter. For more information on these features, see the AWS WAF Developer Guide.


1.17.42
=======

* api-change:``iot``: [``botocore``] Added ability to prefix search on attribute value for ListThings API.
* api-change:``pricing``: [``botocore``] Minor documentation and link updates.
* api-change:``transcribe``: [``botocore``] Amazon Transcribe now supports creating custom language models in the following languages: British English (en-GB), Australian English (en-AU), Indian Hindi (hi-IN), and US Spanish (es-US).
* api-change:``cloudhsm``: [``botocore``] Minor documentation and link updates.
* api-change:``comprehend``: [``botocore``] Support for customer managed KMS encryption of Comprehend custom models
* api-change:``cognito-sync``: [``botocore``] Minor documentation updates and link updates.
* api-change:``batch``: [``botocore``] AWS Batch adds support for Amazon EFS File System
* api-change:``detective``: [``botocore``] Added the ability to assign tag values to Detective behavior graphs. Tag values can be used for attribute-based access control, and for cost allocation for billing.
* api-change:``iotwireless``: [``botocore``] Add Sidewalk support to APIs: GetWirelessDevice, ListWirelessDevices, GetWirelessDeviceStatistics. Add Gateway connection status in GetWirelessGatewayStatistics API.
* api-change:``cloudformation``: [``botocore``] 1. Added a new parameter RegionConcurrencyType in OperationPreferences. 2. Changed the name of AccountUrl to AccountsUrl in DeploymentTargets parameter.
* api-change:``cloud9``: [``botocore``] Add ImageId input parameter to CreateEnvironmentEC2 endpoint. New parameter enables creation of environments with different AMIs.
* api-change:``directconnect``: [``botocore``] This release adds MACsec support to AWS Direct Connect
* api-change:``redshift``: [``botocore``] Enable customers to share access to their Redshift clusters from other VPCs (including VPCs from other accounts).
* api-change:``workmail``: [``botocore``] This release adds support for mobile device access rules management in Amazon WorkMail.
* api-change:``datapipeline``: [``botocore``] Minor documentation updates and link updates.
* api-change:``machinelearning``: [``botocore``] Minor documentation updates and link updates.


1.17.41
=======

* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot now supports 1) feature importance reports for AutoML jobs and 2) PartialFailures for AutoML jobs
* api-change:``ec2-instance-connect``: [``botocore``] Adding support to push SSH keys to the EC2 serial console in order to allow an SSH connection to your Amazon EC2 instance's serial port.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``databrew``: [``botocore``] This SDK release adds two new dataset features: 1) support for specifying a database connection as a dataset input 2) support for dynamic datasets that accept configurable parameters in S3 path.
* api-change:``frauddetector``: [``botocore``] This release adds support for Batch Predictions in Amazon Fraud Detector.
* api-change:``ec2``: [``botocore``] ReplaceRootVolume feature enables customers to replace the EBS root volume of a running instance to a previously known state. Add support to grant account-level access to the EC2 serial console
* api-change:``config``: [``botocore``] Adding new APIs to support ConformancePack Compliance CI in Aggregators
* api-change:``pinpoint``: [``botocore``] Added support for journey pause/resume, journey updatable import segment and journey quiet time wait.


1.17.40
=======

* api-change:``wafv2``: [``botocore``] Added custom request handling and custom response support in rule actions and default action; Added the option to inspect the web request body as parsed and filtered JSON.
* api-change:``iam``: [``botocore``] AWS Identity and Access Management GetAccessKeyLastUsed API will throw a custom error if customer public key is not found for access keys.
* api-change:``glue``: [``botocore``] Allow Dots in Registry and Schema Names for CreateRegistry, CreateSchema; Fixed issue when duplicate keys are present and not returned as part of QuerySchemaVersionMetadata.
* api-change:``docdb``: [``botocore``] This release adds support for Event Subscriptions to DocumentDB.
* api-change:``location``: [``botocore``] Amazon Location added support for specifying pricing plan information on resources in alignment with our cost model.


1.17.39
=======

* api-change:``iotwireless``: [``botocore``] Support tag-on-create for WirelessDevice.
* api-change:``customer-profiles``: [``botocore``] This release adds an optional parameter named FlowDefinition in PutIntegrationRequest.
* api-change:``events``: [``botocore``] Add support for SageMaker Model Builder Pipelines Targets to EventBridge
* api-change:``transcribe``: [``botocore``] Amazon Transcribe now supports tagging words that match your vocabulary filter for batch transcription.


1.17.38
=======

* api-change:``lookoutmetrics``: [``botocore``] Allowing uppercase alphabets for RDS and Redshift database names.


1.17.37
=======

* api-change:``sqs``: [``botocore``] Documentation updates for Amazon SQS
* api-change:``rekognition``: [``botocore``] This release introduces AWS tagging support for Amazon Rekognition collections, stream processors, and Custom Label models.
* api-change:``sagemaker``: [``botocore``] This feature allows customer to specify the environment variables in their CreateTrainingJob requests.
* api-change:``medialive``: [``botocore``] EML now supports handling HDR10 and HLG 2020 color space from a Link input.
* api-change:``lookoutmetrics``: [``botocore``] Amazon Lookout for Metrics is now generally available. You can use Lookout for Metrics to monitor your data for anomalies. For more information, see the Amazon Lookout for Metrics Developer Guide.
* api-change:``alexaforbusiness``: [``botocore``] Added support for enabling and disabling data retention in the CreateProfile and UpdateProfile APIs and retrieving the state of data retention for a profile in the GetProfile API.


1.17.36
=======

* api-change:``ssm``: [``botocore``] This release allows SSM Explorer customers to enable OpsData sources across their organization when creating a resource data sync.
* api-change:``route53``: [``botocore``] Documentation updates for route53
* bugfix:S3: [``botocore``] Fix an issue with XML newline normalization in PutBucketLifecycleConfiguration requests.
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3
* api-change:``s3control``: [``botocore``] Documentation updates for s3-control
* api-change:``ec2``: [``botocore``] maximumEfaInterfaces added to DescribeInstanceTypes API
* api-change:``greengrass``: [``botocore``] Updated the parameters to make name required for CreateGroup API.


1.17.35
=======

* api-change:``ce``: [``botocore``] You can now create cost categories with inherited value rules and specify default values for any uncategorized costs.
* api-change:``fis``: [``botocore``] Updated maximum allowed size of action parameter from 64 to 1024
* api-change:``redshift``: [``botocore``] Removed APIs to control AQUA on clusters.
* api-change:``iam``: [``botocore``] Documentation updates for IAM operations and descriptions.
* api-change:``gamelift``: [``botocore``] GameLift adds support for using event notifications to monitor game session placements. Specify an SNS topic or use CloudWatch Events to track activity for a game session queue.


1.17.34
=======

* api-change:``ec2``: [``botocore``] This release adds support for UEFI boot on selected AMD- and Intel-based EC2 instances.
* api-change:``redshift``: [``botocore``] Added support to enable AQUA in Amazon Redshift clusters.
* api-change:``codeartifact``: [``botocore``] Documentation updates for CodeArtifact
* api-change:``macie2``: [``botocore``] This release of the Amazon Macie API adds support for publishing sensitive data findings to AWS Security Hub and specifying which categories of findings to publish to Security Hub.


1.17.33
=======

* api-change:``sagemaker``: [``botocore``] Adding authentication support for pulling images stored in private Docker registries to build containers for real-time inference.
* api-change:``ec2``: [``botocore``] X2gd instances are the next generation of memory-optimized instances powered by AWS-designed, Arm-based AWS Graviton2 processors.


1.17.32
=======

* bugfix:s3: [``botocore``] Updated mislabeled exceptions for S3 Object Lambda


1.17.31
=======

* api-change:``autoscaling``: [``botocore``] Amazon EC2 Auto Scaling Instance Refresh now supports phased deployments.
* api-change:``s3``: [``botocore``] S3 Object Lambda is a new S3 feature that enables users to apply their own custom code to process the output of a standard S3 GET request by automatically invoking a Lambda function with a GET request
* api-change:``redshift``: [``botocore``] Add new fields for additional information about VPC endpoint for clusters with reallocation enabled, and a new field for total storage capacity for all clusters.
* api-change:``s3control``: [``botocore``] S3 Object Lambda is a new S3 feature that enables users to apply their own custom code to process the output of a standard S3 GET request by automatically invoking a Lambda function with a GET request
* api-change:``securityhub``: [``botocore``] New object for separate provider and customer values. New objects track S3 Public Access Block configuration and identify sensitive data. BatchImportFinding requests are limited to 100 findings.


1.17.30
=======

* api-change:``sagemaker``: [``botocore``] Support new target device ml_eia2 in SageMaker CreateCompilationJob API
* api-change:``batch``: [``botocore``] Making serviceRole an optional parameter when creating a compute environment. If serviceRole is not provided then Service Linked Role will be created (or reused if it already exists).


1.17.29
=======

* api-change:``lambda``: [``botocore``] Allow empty list for function response types
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``mediaconnect``: [``botocore``] This release adds support for the SRT-listener protocol on sources and outputs.
* api-change:``accessanalyzer``: [``botocore``] This release adds support for the ValidatePolicy API. IAM Access Analyzer is adding over 100 policy checks and actionable recommendations that help you validate your policies during authoring.
* api-change:``mediatailor``: [``botocore``] MediaTailor channel assembly is a new manifest-only service that allows you to assemble linear streams using your existing VOD content.
* api-change:``mwaa``: [``botocore``] This release adds UPDATE_FAILED and UNAVAILABLE MWAA environment states.
* api-change:``gamelift``: [``botocore``] GameLift expands to six new AWS Regions, adds support for multi-location fleets to streamline management of hosting resources, and lets you customize more of the game session placement process.


1.17.28
=======

* api-change:``fis``: [``botocore``] Initial release of AWS Fault Injection Simulator, a managed service that enables you to perform fault injection experiments on your AWS workloads
* api-change:``codedeploy``: [``botocore``] AWS CodeDeploy can now detect instances running an outdated revision of your application and automatically update them with the latest revision.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``ecs``: [``botocore``] This is for ecs exec feature release which includes two new APIs - execute-command and update-cluster and an AWS CLI customization for execute-command API


1.17.27
=======

* api-change:``mediatailor``: [``botocore``] MediaTailor channel assembly is a new manifest-only service that allows you to assemble linear streams using your existing VOD content.
* api-change:``workspaces``: [``botocore``] Adds API support for WorkSpaces bundle management operations.
* api-change:``cur``: [``botocore``] - Added optional billingViewArn field for OSG.


1.17.26
=======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``network-firewall``: [``botocore``] Update network-firewall client to latest version


1.17.25
=======

* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version


1.17.24
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``iotwireless``: [``botocore``] Update iotwireless client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version


1.17.23
=======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.17.22
=======

* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``network-firewall``: [``botocore``] Update network-firewall client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``appflow``: [``botocore``] Update appflow client to latest version


1.17.21
=======

* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``mwaa``: [``botocore``] Update mwaa client to latest version


1.17.20
=======

* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``wellarchitected``: [``botocore``] Update wellarchitected client to latest version


1.17.19
=======

* api-change:``iotwireless``: [``botocore``] Update iotwireless client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* bugfix:S3: [``botocore``] Fix an issue with XML newline normalization that could result in the DeleteObjects operation incorrectly deleting the wrong keys.
* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version


1.17.18
=======

* enhancement:DynamoDB: Add a `__bytes__` method to the `Binary` DynamoDB type.
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.17.17
=======

* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``sso-admin``: [``botocore``] Update sso-admin client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.17.16
=======

* api-change:``databrew``: [``botocore``] Update databrew client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version


1.17.15
=======

* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``appflow``: [``botocore``] Update appflow client to latest version
* api-change:``ecr-public``: [``botocore``] Update ecr-public client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version


1.17.14
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``redshift-data``: [``botocore``] Update redshift-data client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.17.13
=======

* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.17.12
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version


1.17.11
=======

* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.17.10
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``lookoutvision``: [``botocore``] Update lookoutvision client to latest version


1.17.9
======

* api-change:``devops-guru``: [``botocore``] Update devops-guru client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.17.8
======

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``redshift-data``: [``botocore``] Update redshift-data client to latest version
* api-change:``workmailmessageflow``: [``botocore``] Update workmailmessageflow client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version


1.17.7
======

* api-change:``personalize-events``: [``botocore``] Update personalize-events client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.17.6
======

* api-change:``databrew``: [``botocore``] Update databrew client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.17.5
======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``qldb-session``: [``botocore``] Update qldb-session client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version


1.17.4
======

* api-change:``dataexchange``: [``botocore``] Update dataexchange client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``ivs``: [``botocore``] Update ivs client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.17.3
======

* api-change:``macie``: [``botocore``] Update macie client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.17.2
======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``appflow``: [``botocore``] Update appflow client to latest version
* api-change:``emr-containers``: [``botocore``] Update emr-containers client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.17.1
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``databrew``: [``botocore``] Update databrew client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``auditmanager``: [``botocore``] Update auditmanager client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version


1.17.0
======

* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* feature:Python: Dropped support for Python 3.4 and 3.5
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``lookoutvision``: [``botocore``] Update lookoutvision client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* feature:Python: [``botocore``] Dropped support for Python 3.4 and 3.5
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``location``: [``botocore``] Update location client to latest version
* enhancement:s3: [``botocore``] Amazon S3 now supports AWS PrivateLink, providing direct access to S3 via a private endpoint within your virtual private network.
* api-change:``iotwireless``: [``botocore``] Update iotwireless client to latest version


1.16.63
=======

* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.16.62
=======

* api-change:``wellarchitected``: [``botocore``] Update wellarchitected client to latest version
* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``databrew``: [``botocore``] Update databrew client to latest version
* bugfix:Validator: [``botocore``] Fix showing incorrect max-value in error message for range and length value validation
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.16.61
=======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``customer-profiles``: [``botocore``] Update customer-profiles client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version
* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.16.60
=======

* api-change:``backup``: [``botocore``] Update backup client to latest version


1.16.59
=======

* api-change:``greengrassv2``: [``botocore``] Update greengrassv2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.16.58
=======

* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version


1.16.57
=======

* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.16.56
=======

* api-change:``sns``: [``botocore``] Update sns client to latest version


1.16.55
=======

* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``cognito-identity``: [``botocore``] Update cognito-identity client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.16.54
=======

* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.16.53
=======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``auditmanager``: [``botocore``] Update auditmanager client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.16.52
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version


1.16.51
=======

* api-change:``devops-guru``: [``botocore``] Update devops-guru client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.16.50
=======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version


1.16.49
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version


1.16.48
=======

* api-change:``healthlake``: [``botocore``] Update healthlake client to latest version
* api-change:``cloudsearch``: [``botocore``] Update cloudsearch client to latest version


1.16.47
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.16.46
=======

* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.16.45
=======

* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version


1.16.44
=======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version


1.16.43
=======

* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.16.42
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``iotwireless``: [``botocore``] Update iotwireless client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.16.41
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``service-quotas``: [``botocore``] Update service-quotas client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``connectparticipant``: [``botocore``] Update connectparticipant client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``qldb-session``: [``botocore``] Update qldb-session client to latest version
* api-change:``outposts``: [``botocore``] Update outposts client to latest version
* api-change:``servicecatalog-appregistry``: [``botocore``] Update servicecatalog-appregistry client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version


1.16.40
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* bugfix:SSO: [``botocore``] Fixed timestamp format for SSO credential expirations
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.16.39
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``route53resolver``: [``botocore``] Update route53resolver client to latest version
* api-change:``sqs``: [``botocore``] Update sqs client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version


1.16.38
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``amp``: [``botocore``] Update amp client to latest version
* api-change:``location``: [``botocore``] Update location client to latest version
* api-change:``wellarchitected``: [``botocore``] Update wellarchitected client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version


1.16.37
=======

* api-change:``iotwireless``: [``botocore``] Update iotwireless client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``greengrassv2``: [``botocore``] Update greengrassv2 client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``iotdeviceadvisor``: [``botocore``] Update iotdeviceadvisor client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``amp``: [``botocore``] Update amp client to latest version
* api-change:``iotfleethub``: [``botocore``] Update iotfleethub client to latest version


1.16.36
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``devops-guru``: [``botocore``] Update devops-guru client to latest version


1.16.35
=======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``pi``: [``botocore``] Update pi client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version


1.16.34
=======

* api-change:``networkmanager``: [``botocore``] Update networkmanager client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.16.33
=======

* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.16.32
=======

* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``auditmanager``: [``botocore``] Update auditmanager client to latest version
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker-edge``: [``botocore``] Update sagemaker-edge client to latest version
* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``healthlake``: [``botocore``] Update healthlake client to latest version
* api-change:``emr-containers``: [``botocore``] Update emr-containers client to latest version


1.16.31
=======

* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``servicecatalog-appregistry``: [``botocore``] Update servicecatalog-appregistry client to latest version


1.16.30
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.16.29
=======

* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``amplifybackend``: [``botocore``] Update amplifybackend client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version


1.16.28
=======

* api-change:``customer-profiles``: [``botocore``] Update customer-profiles client to latest version


1.16.27
=======

* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Update sagemaker-featurestore-runtime client to latest version
* api-change:``ecr-public``: [``botocore``] Update ecr-public client to latest version
* api-change:``honeycode``: [``botocore``] Update honeycode client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``amplifybackend``: [``botocore``] Update amplifybackend client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``lookoutvision``: [``botocore``] Update lookoutvision client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``connect-contact-lens``: [``botocore``] Update connect-contact-lens client to latest version
* api-change:``profile``: [``botocore``] Update profile client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``appintegrations``: [``botocore``] Update appintegrations client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``devops-guru``: [``botocore``] Update devops-guru client to latest version


1.16.26
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.16.25
=======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``appflow``: [``botocore``] Update appflow client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``timestream-write``: [``botocore``] Update timestream-write client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``mwaa``: [``botocore``] Update mwaa client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version


1.16.24
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``translate``: [``botocore``] Update translate client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``signer``: [``botocore``] Update signer client to latest version
* api-change:``codestar-connections``: [``botocore``] Update codestar-connections client to latest version
* api-change:``codeartifact``: [``botocore``] Update codeartifact client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``timestream-query``: [``botocore``] Update timestream-query client to latest version
* api-change:``sso-admin``: [``botocore``] Update sso-admin client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``outposts``: [``botocore``] Update outposts client to latest version
* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.16.23
=======

* api-change:``servicecatalog-appregistry``: [``botocore``] Update servicecatalog-appregistry client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``cognito-identity``: [``botocore``] Update cognito-identity client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.16.22
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version


1.16.21
=======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* bugfix:Retry: [``botocore``] Fix bug where retries were attempted on any response with an "Error" key.
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version
* api-change:``outposts``: [``botocore``] Update outposts client to latest version


1.16.20
=======

* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``network-firewall``: [``botocore``] Update network-firewall client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.16.19
=======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``iotsecuretunneling``: [``botocore``] Update iotsecuretunneling client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``synthetics``: [``botocore``] Update synthetics client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version


1.16.18
=======

* api-change:``textract``: [``botocore``] Update textract client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.16.17
=======

* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``servicecatalog-appregistry``: [``botocore``] Update servicecatalog-appregistry client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.16.16
=======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``databrew``: [``botocore``] Update databrew client to latest version
* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version


1.16.15
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.16.14
=======

* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version


1.16.13
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version


1.16.12
=======

* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version


1.16.11
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.16.10
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.16.9
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``braket``: [``botocore``] Update braket client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.16.8
======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``codeartifact``: [``botocore``] Update codeartifact client to latest version
* api-change:``marketplacecommerceanalytics``: [``botocore``] Update marketplacecommerceanalytics client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.16.7
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version


1.16.6
======

* api-change:``glue``: [``botocore``] Update glue client to latest version


1.16.5
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``neptune``: [``botocore``] Update neptune client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version


1.16.4
======

* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.16.3
======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``appflow``: [``botocore``] Update appflow client to latest version


1.16.2
======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.16.1
======

* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version


1.16.0
======

* api-change:``backup``: [``botocore``] Update backup client to latest version
* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* feature:imds: [``botocore``] Updated InstanceMetadataFetcher to use custom ipv6 uri as endpoint if envvar or config set
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.15.18
=======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.15.17
=======

* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``groundstation``: [``botocore``] Update groundstation client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.15.16
=======

* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.15.15
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.15.14
=======

* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.15.13
=======

* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``marketplace-catalog``: [``botocore``] Update marketplace-catalog client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.15.12
=======

* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.15.11
=======

* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``personalize-events``: [``botocore``] Update personalize-events client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.15.10
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version


1.15.9
======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``s3outposts``: [``botocore``] Update s3outposts client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.15.8
======

* api-change:``timestream-write``: [``botocore``] Update timestream-write client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``schemas``: [``botocore``] Update schemas client to latest version
* api-change:``timestream-query``: [``botocore``] Update timestream-query client to latest version


1.15.7
======

* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.15.6
======

* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version


1.15.5
======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``textract``: [``botocore``] Update textract client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``savingsplans``: [``botocore``] Update savingsplans client to latest version
* api-change:``synthetics``: [``botocore``] Update synthetics client to latest version


1.15.4
======

* api-change:``translate``: [``botocore``] Update translate client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version


1.15.3
======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version


1.15.2
======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.15.1
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``sso-admin``: [``botocore``] Update sso-admin client to latest version
* api-change:``codestar-connections``: [``botocore``] Update codestar-connections client to latest version


1.15.0
======

* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* feature:dependency: [``botocore``] botocore has removed docutils as a required dependency


1.14.63
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.14.62
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.14.61
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``docdb``: [``botocore``] Update docdb client to latest version


1.14.60
=======

* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.14.59
=======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``ebs``: [``botocore``] Update ebs client to latest version
* api-change:``sso-admin``: [``botocore``] Update sso-admin client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.14.58
=======

* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``redshift-data``: [``botocore``] Update redshift-data client to latest version


1.14.57
=======

* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.14.56
=======

* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.14.55
=======

* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version


1.14.54
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.14.53
=======

* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version


1.14.52
=======

* api-change:``sqs``: [``botocore``] Update sqs client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.51
=======

* api-change:``cur``: [``botocore``] Update cur client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.14.50
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.14.49
=======

* api-change:``appflow``: [``botocore``] Update appflow client to latest version
* api-change:``route53resolver``: [``botocore``] Update route53resolver client to latest version


1.14.48
=======

* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version


1.14.47
=======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version


1.14.46
=======

* api-change:``lakeformation``: [``botocore``] Update lakeformation client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ivs``: [``botocore``] Update ivs client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.14.45
=======

* api-change:``identitystore``: [``botocore``] Update identitystore client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version


1.14.44
=======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``kinesis``: [``botocore``] Update kinesis client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``elb``: [``botocore``] Update elb client to latest version
* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version


1.14.43
=======

* api-change:``braket``: [``botocore``] Update braket client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.14.42
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``braket``: [``botocore``] Update braket client to latest version


1.14.41
=======

* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``cloud9``: [``botocore``] Update cloud9 client to latest version


1.14.40
=======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.39
=======

* api-change:``savingsplans``: [``botocore``] Update savingsplans client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.38
=======

* api-change:``sms``: [``botocore``] Update sms client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.14.37
=======

* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``personalize-events``: [``botocore``] Update personalize-events client to latest version


1.14.36
=======

* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.14.35
=======

* api-change:``health``: [``botocore``] Update health client to latest version


1.14.34
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.14.33
=======

* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version


1.14.32
=======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version


1.14.31
=======

* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.14.30
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``ivs``: [``botocore``] Update ivs client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version


1.14.29
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.14.28
=======

* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``mq``: [``botocore``] Update mq client to latest version


1.14.27
=======

* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.14.26
=======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.14.25
=======

* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version


1.14.24
=======

* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``groundstation``: [``botocore``] Update groundstation client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version


1.14.23
=======

* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.22
=======

* enhancement:examples: [``botocore``] Pull in latest examples from EFS.


1.14.21
=======

* api-change:``ivs``: [``botocore``] Update ivs client to latest version


1.14.20
=======

* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``ebs``: [``botocore``] Update ebs client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version


1.14.19
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.14.18
=======

* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``lakeformation``: [``botocore``] Update lakeformation client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version


1.14.17
=======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version


1.14.16
=======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.14.15
=======

* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.14.14
=======

* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.13
=======

* api-change:``codestar-connections``: [``botocore``] Update codestar-connections client to latest version
* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.14.12
=======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.14.11
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.14.10
=======

* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``honeycode``: [``botocore``] Update honeycode client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.14.9
======

* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.14.8
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``sqs``: [``botocore``] Update sqs client to latest version


1.14.7
======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.14.6
======

* api-change:``support``: [``botocore``] Update support client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version


1.14.5
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.14.4
======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``dataexchange``: [``botocore``] Update dataexchange client to latest version
* api-change:``qldb``: [``botocore``] Update qldb client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``polly``: [``botocore``] Update polly client to latest version


1.14.3
======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.14.2
======

* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.14.1
======

* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``iot-data``: [``botocore``] Update iot-data client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.14.0
======

* api-change:``macie2``: [``botocore``] Update macie2 client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``codeartifact``: [``botocore``] Update codeartifact client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version
* feature:SSO: [``botocore``] Added support for the SSO credential provider. This allows the SDK to retrieve temporary AWS credentials from a profile configured to use SSO credentials.
* api-change:``dlm``: [``botocore``] Update dlm client to latest version


1.13.26
=======

* api-change:``transfer``: [``botocore``] Update transfer client to latest version


1.13.25
=======

* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version


1.13.24
=======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.13.23
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.13.22
=======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.13.21
=======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.13.20
=======

* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``worklink``: [``botocore``] Update worklink client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.13.19
=======

* api-change:``marketplace-catalog``: [``botocore``] Update marketplace-catalog client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``qldb-session``: [``botocore``] Update qldb-session client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version


1.13.18
=======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.13.17
=======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``macie``: [``botocore``] Update macie client to latest version


1.13.16
=======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version


1.13.15
=======

* api-change:``synthetics``: [``botocore``] Update synthetics client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.13.14
=======

* api-change:``backup``: [``botocore``] Update backup client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version


1.13.13
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version


1.13.12
=======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``qldb``: [``botocore``] Update qldb client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.13.11
=======

* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version


1.13.10
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version


1.13.9
======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``macie2``: [``botocore``] Update macie2 client to latest version


1.13.8
======

* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* enchancement:Endpoints: [``botocore``] Improved endpoint resolution for clients with unknown regions


1.13.7
======

* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version


1.13.6
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version


1.13.5
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version


1.13.4
======

* api-change:``codestar-connections``: [``botocore``] Update codestar-connections client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version


1.13.3
======

* api-change:``support``: [``botocore``] Update support client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.13.2
======

* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version


1.13.1
======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.13.0
======

* api-change:``schemas``: [``botocore``] Update schemas client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* feature:Exceptions: [``botocore``] Added support for parsing modeled exception fields.
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.12.49
=======

* api-change:``iotsitewise``: [``botocore``] Update iotsitewise client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version


1.12.48
=======

* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.12.47
=======

* bugfix:Resource: fixes `#2361 <https://github.com/boto/boto3/issues/2361>`__
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``dataexchange``: [``botocore``] Update dataexchange client to latest version
* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.12.46
=======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``elastic-inference``: [``botocore``] Update elastic-inference client to latest version


1.12.45
=======

* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ram``: [``botocore``] Update ram client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version


1.12.44
=======

* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version


1.12.43
=======

* api-change:``route53domains``: [``botocore``] Update route53domains client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.12.42
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``synthetics``: [``botocore``] Update synthetics client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version


1.12.41
=======

* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version


1.12.40
=======

* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sagemaker-a2i-runtime``: [``botocore``] Update sagemaker-a2i-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``mgh``: [``botocore``] Update mgh client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.12.39
=======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``migrationhub-config``: [``botocore``] Update migrationhub-config client to latest version


1.12.38
=======

* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version


1.12.37
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version


1.12.36
=======

* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.12.35
=======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.12.34
=======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version


1.12.33
=======

* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``elastic-inference``: [``botocore``] Update elastic-inference client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version


1.12.32
=======

* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version


1.12.31
=======

* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.12.30
=======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version


1.12.29
=======

* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version


1.12.28
=======

* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.12.27
=======

* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version


1.12.26
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.12.25
=======

* api-change:``outposts``: [``botocore``] Update outposts client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version


1.12.24
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.12.23
=======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.12.22
=======

* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* bugfix:Stubber: [``botocore``] fixes `#1884 <https://github.com/boto/botocore/issues/1884>`__
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.12.21
=======

* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version


1.12.20
=======

* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.12.19
=======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.12.18
=======

* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* enhancement:timezones: [``botocore``] Improved timezone parsing for Windows with new fallback method (#1939)
* api-change:``marketplacecommerceanalytics``: [``botocore``] Update marketplacecommerceanalytics client to latest version


1.12.17
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.12.16
=======

* api-change:``signer``: [``botocore``] Update signer client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.12.15
=======

* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.12.14
=======

* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.12.13
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.12.12
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version


1.12.11
=======

* api-change:``config``: [``botocore``] Update config client to latest version


1.12.10
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``sagemaker-a2i-runtime``: [``botocore``] Update sagemaker-a2i-runtime client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``workdocs``: [``botocore``] Update workdocs client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version
* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version


1.12.9
======

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version


1.12.8
======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version


1.12.7
======

* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``outposts``: [``botocore``] Update outposts client to latest version


1.12.6
======

* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version


1.12.5
======

* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.12.4
======

* api-change:``savingsplans``: [``botocore``] Update savingsplans client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.12.3
======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version


1.12.2
======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.12.1
======

* api-change:``cloud9``: [``botocore``] Update cloud9 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.12.0
======

* feature:retries: [``botocore``] Add support for retry modes, including ``standard`` and ``adaptive`` modes (`#1972 <https://github.com/boto/botocore/issues/1972>`__)
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version


1.11.17
=======

* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version


1.11.16
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``neptune``: [``botocore``] Update neptune client to latest version


1.11.15
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version


1.11.14
=======

* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version


1.11.13
=======

* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.11.12
=======

* api-change:``ebs``: [``botocore``] Update ebs client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.11.11
=======

* api-change:``groundstation``: [``botocore``] Update groundstation client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``forecastquery``: [``botocore``] Update forecastquery client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version


1.11.10
=======

* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.11.9
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.11.8
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version


1.11.7
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``marketplacecommerceanalytics``: [``botocore``] Update marketplacecommerceanalytics client to latest version


1.11.6
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.11.5
======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``neptune``: [``botocore``] Update neptune client to latest version
* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.11.4
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version


1.11.3
======

* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.11.2
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.11.1
======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version


1.11.0
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* feature:Python: Dropped support for Python 2.6 and 3.3.
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* feature:Python: [``botocore``] Dropped support for Python 2.6 and 3.3.
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.10.50
=======

* api-change:``logs``: [``botocore``] Update logs client to latest version


1.10.49
=======

* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``translate``: [``botocore``] Update translate client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version


1.10.48
=======

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``mgh``: [``botocore``] Update mgh client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version


1.10.47
=======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.46
=======

* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version


1.10.45
=======

* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version


1.10.44
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.10.43
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``codestar-connections``: [``botocore``] Update codestar-connections client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.42
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version


1.10.41
=======

* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.40
=======

* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.39
=======

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``detective``: [``botocore``] Update detective client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version


1.10.38
=======

* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version


1.10.37
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.36
=======

* api-change:``kendra``: [``botocore``] Update kendra client to latest version


1.10.35
=======

* bugfix:s3: [``botocore``] Add stricter validation to s3 control account id parameter.
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version


1.10.34
=======

* bugfix:s3: [``botocore``] Fixed an issue where the request path was set incorrectly if access point name was present in key path.


1.10.33
=======

* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``kinesis-video-signaling``: [``botocore``] Update kinesis-video-signaling client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version


1.10.32
=======

* api-change:``ebs``: [``botocore``] Update ebs client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.10.31
=======

* api-change:``textract``: [``botocore``] Update textract client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``outposts``: [``botocore``] Update outposts client to latest version
* api-change:``kendra``: [``botocore``] Update kendra client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``networkmanager``: [``botocore``] Update networkmanager client to latest version
* api-change:``compute-optimizer``: [``botocore``] Update compute-optimizer client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``frauddetector``: [``botocore``] Update frauddetector client to latest version
* api-change:``sagemaker-a2i-runtime``: [``botocore``] Update sagemaker-a2i-runtime client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] Update codeguru-reviewer client to latest version
* api-change:``codeguruprofiler``: [``botocore``] Update codeguruprofiler client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.10.30
=======

* api-change:``accessanalyzer``: [``botocore``] Update accessanalyzer client to latest version


1.10.29
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``imagebuilder``: [``botocore``] Update imagebuilder client to latest version
* api-change:``schemas``: [``botocore``] Update schemas client to latest version


1.10.28
=======

* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``elastic-inference``: [``botocore``] Update elastic-inference client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version


1.10.27
=======

* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``wafv2``: [``botocore``] Update wafv2 client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``iotsecuretunneling``: [``botocore``] Update iotsecuretunneling client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``appconfig``: [``botocore``] Update appconfig client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``ram``: [``botocore``] Update ram client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version


1.10.26
=======

* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.10.25
=======

* bugfix:IMDS metadata: [``botocore``] Add 405 case to metadata fetching logic.


1.10.24
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``connectparticipant``: [``botocore``] Update connectparticipant client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version


1.10.23
=======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version
* api-change:``mgh``: [``botocore``] Update mgh client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``migrationhub-config``: [``botocore``] Update migrationhub-config client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version


1.10.22
=======

* bugfix:IMDS: [``botocore``] Fix regression in IMDS credential resolution. Fixes `#1892 <https://github.com/boto/botocore/issues/1892>`__.


1.10.21
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.10.20
=======

* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.10.19
=======

* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version


1.10.18
=======

* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.10.17
=======

* api-change:``sesv2``: [``botocore``] Update sesv2 client to latest version
* api-change:``dataexchange``: [``botocore``] Update dataexchange client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``cloudsearch``: [``botocore``] Update cloudsearch client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version


1.10.16
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``marketplace-catalog``: [``botocore``] Update marketplace-catalog client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.10.15
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version


1.10.14
=======

* api-change:``cognito-identity``: [``botocore``] Update cognito-identity client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version


1.10.13
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``sso``: [``botocore``] Update sso client to latest version
* api-change:``sso-oidc``: [``botocore``] Update sso-oidc client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version


1.10.12
=======

* api-change:``savingsplans``: [``botocore``] Update savingsplans client to latest version


1.10.11
=======

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``savingsplans``: [``botocore``] Update savingsplans client to latest version
* api-change:``signer``: [``botocore``] Update signer client to latest version


1.10.10
=======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``codestar-notifications``: [``botocore``] Update codestar-notifications client to latest version


1.10.9
======

* api-change:``dax``: [``botocore``] Update dax client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.10.8
======

* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.10.7
======

* api-change:``support``: [``botocore``] Update support client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.10.6
======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.10.5
======

* api-change:``cloud9``: [``botocore``] Update cloud9 client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.10.4
======

* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.10.3
======

* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version


1.10.2
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* enhancement:``sts``: [``botocore``] Add support for configuring the use of regional STS endpoints.
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.10.1
======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.10.0
======

* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* feature:``botocore.vendored.requests``: [``botocore``] Removed vendored version of ``requests`` (`#1829 <https://github.com/boto/botocore/issues/1829>`__)


1.9.253
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version


1.9.252
=======

* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.251
=======

* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``marketplacecommerceanalytics``: [``botocore``] Update marketplacecommerceanalytics client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.9.250
=======

* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version


1.9.249
=======

* api-change:``personalize``: [``botocore``] Update personalize client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.9.248
=======

* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version


1.9.247
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version


1.9.246
=======

* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.245
=======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version


1.9.244
=======

* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version


1.9.243
=======

* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.242
=======

* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.9.241
=======

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.9.240
=======

* api-change:``docdb``: [``botocore``] Update docdb client to latest version


1.9.239
=======

* api-change:``waf``: [``botocore``] Update waf client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``mq``: [``botocore``] Update mq client to latest version


1.9.238
=======

* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.237
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version


1.9.236
=======

* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.9.235
=======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version


1.9.234
=======

* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.9.233
=======

* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.232
=======

* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.231
=======

* api-change:``ram``: [``botocore``] Update ram client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version


1.9.230
=======

* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.9.229
=======

* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.228
=======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``workmailmessageflow``: [``botocore``] Update workmailmessageflow client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.9.227
=======

* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``ses``: [``botocore``] Update ses client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version


1.9.226
=======

* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.9.225
=======

* api-change:``qldb``: [``botocore``] Update qldb client to latest version
* api-change:``marketplacecommerceanalytics``: [``botocore``] Update marketplacecommerceanalytics client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``qldb-session``: [``botocore``] Update qldb-session client to latest version


1.9.224
=======

* api-change:``kinesisanalytics``: [``botocore``] Update kinesisanalytics client to latest version


1.9.223
=======

* api-change:``config``: [``botocore``] Update config client to latest version


1.9.222
=======

* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.9.221
=======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version


1.9.220
=======

* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``apigatewaymanagementapi``: [``botocore``] Update apigatewaymanagementapi client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.219
=======

* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.218
=======

* api-change:``sqs``: [``botocore``] Update sqs client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.217
=======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.9.216
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version


1.9.215
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.9.214
=======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.213
=======

* api-change:``forecast``: [``botocore``] Update forecast client to latest version
* api-change:``forecastquery``: [``botocore``] Update forecastquery client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``sqs``: [``botocore``] Update sqs client to latest version


1.9.212
=======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.9.211
=======

* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``cur``: [``botocore``] Update cur client to latest version


1.9.210
=======

* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.209
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.9.208
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.207
=======

* api-change:``appsync``: [``botocore``] Update appsync client to latest version


1.9.206
=======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.9.205
=======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.204
=======

* api-change:``lakeformation``: [``botocore``] Update lakeformation client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.9.203
=======

* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version


1.9.202
=======

* api-change:``batch``: [``botocore``] Update batch client to latest version


1.9.201
=======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.200
=======

* api-change:``sts``: [``botocore``] Update sts client to latest version
* enhancement:Credentials: [``botocore``] Add support for a credential provider that handles resolving credentials via STS AssumeRoleWithWebIdentity


1.9.199
=======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version


1.9.198
=======

* bugfix:S3: [``botocore``] Fix an issue that would cause S3 list_object_versions to sometimes fail parsing responses with certain key values.
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version


1.9.197
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.196
=======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.195
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.9.194
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version


1.9.193
=======

* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version


1.9.192
=======

* bugfix:Dependency: [``botocore``] Fixed dependency issue with broken docutils aws/aws-cli`#4332 <https://github.com/boto/botocore/issues/4332>`__


1.9.191
=======

* api-change:``sqs``: [``botocore``] Update sqs client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version


1.9.190
=======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.189
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.9.188
=======

* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.9.187
=======

* api-change:``events``: [``botocore``] Update events client to latest version


1.9.186
=======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``glacier``: [``botocore``] Update glacier client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.9.185
=======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version


1.9.184
=======

* api-change:``ce``: [``botocore``] Update ce client to latest version


1.9.183
=======

* api-change:``swf``: [``botocore``] Update swf client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.182
=======

* enhancement:CSM: [``botocore``] Support configuration of the host used in client side metrics via AWS_CSM_HOST
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version


1.9.181
=======

* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.180
=======

* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.9.179
=======

* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``ec2-instance-connect``: [``botocore``] Update ec2-instance-connect client to latest version


1.9.178
=======

* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.9.177
=======

* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version


1.9.176
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.9.175
=======

* api-change:``application-insights``: [``botocore``] Update application-insights client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``service-quotas``: [``botocore``] Update service-quotas client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version


1.9.174
=======

* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``kinesis-video-media``: [``botocore``] Update kinesis-video-media client to latest version


1.9.173
=======

* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``iotevents-data``: [``botocore``] Update iotevents-data client to latest version
* api-change:``opsworks``: [``botocore``] Update opsworks client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version


1.9.172
=======

* api-change:``eks``: [``botocore``] Update eks client to latest version


1.9.171
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``resourcegroupstaggingapi``: [``botocore``] Update resourcegroupstaggingapi client to latest version


1.9.170
=======

* api-change:``neptune``: [``botocore``] Update neptune client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* bugfix:Paginator: [``botocore``] Fixes a bug where pagination tokens with three consecutive underscores would result in a parsing failure. Resolves boto/boto3`#1984 <https://github.com/boto/boto3/issues/1984>`__.


1.9.169
=======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.9.168
=======

* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.9.167
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.9.166
=======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.9.165
=======

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``personalize-runtime``: [``botocore``] Update personalize-runtime client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``personalize-events``: [``botocore``] Update personalize-events client to latest version
* api-change:``personalize``: [``botocore``] Update personalize client to latest version


1.9.164
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.163
=======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ses``: [``botocore``] Update ses client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version


1.9.162
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version


1.9.161
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version


1.9.160
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.159
=======

* api-change:``iotevents-data``: [``botocore``] Update iotevents-data client to latest version
* api-change:``iotevents``: [``botocore``] Update iotevents client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version


1.9.158
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``iotthingsgraph``: [``botocore``] Update iotthingsgraph client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.157
=======

* api-change:``groundstation``: [``botocore``] Update groundstation client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.9.156
=======

* api-change:``mediastore-data``: [``botocore``] Update mediastore-data client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version


1.9.155
=======

* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.154
=======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``worklink``: [``botocore``] Update worklink client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version


1.9.153
=======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.9.152
=======

* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``mediapackage-vod``: [``botocore``] Update mediapackage-vod client to latest version


1.9.151
=======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.9.150
=======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.9.149
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* enhancement:Environment Variables: [``botocore``] Ignore env var credentials is values are empty (`#1680 <https://github.com/boto/botocore/issues/1680>`__)
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.148
=======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.147
=======

* api-change:``datasync``: [``botocore``] Update datasync client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version


1.9.146
=======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version


1.9.145
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``kinesisanalytics``: [``botocore``] Update kinesisanalytics client to latest version
* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version


1.9.144
=======

* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.9.143
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version


1.9.142
=======

* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.141
=======

* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version


1.9.140
=======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.139
=======

* api-change:``neptune``: [``botocore``] Update neptune client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``managedblockchain``: [``botocore``] Update managedblockchain client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version


1.9.138
=======

* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.137
=======

* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version


1.9.136
=======

* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version


1.9.135
=======

* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``textract``: [``botocore``] Update textract client to latest version


1.9.134
=======

* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.9.133
=======

* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``worklink``: [``botocore``] Update worklink client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.9.132
=======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.131
=======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version


1.9.130
=======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``iot1click-devices``: [``botocore``] Update iot1click-devices client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.9.129
=======

* api-change:``eks``: [``botocore``] Update eks client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version


1.9.128
=======

* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version


1.9.127
=======

* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version


1.9.126
=======

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.125
=======

* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version


1.9.124
=======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version


1.9.123
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.9.122
=======

* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.9.121
=======

* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``iot1click-devices``: [``botocore``] Update iot1click-devices client to latest version


1.9.120
=======

* api-change:``iot1click-projects``: [``botocore``] Update iot1click-projects client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.9.119
=======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version


1.9.118
=======

* api-change:``cognito-identity``: [``botocore``] Update cognito-identity client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version


1.9.117
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.9.116
=======

* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``chime``: [``botocore``] Update chime client to latest version


1.9.115
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.9.114
=======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version


1.9.113
=======

* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version


1.9.112
=======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.9.111
=======

* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.9.110
=======

* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.109
=======

* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.108
=======

* api-change:``textract``: [``botocore``] Update textract client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version


1.9.107
=======

* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.106
=======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version


1.9.105
=======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version


1.9.104
=======

* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version


1.9.103
=======

* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``cur``: [``botocore``] Update cur client to latest version


1.9.102
=======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version


1.9.101
=======

* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``cloud9``: [``botocore``] Update cloud9 client to latest version


1.9.100
=======

* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version
* api-change:``workdocs``: [``botocore``] Update workdocs client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``kinesis-video-media``: [``botocore``] Update kinesis-video-media client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version


1.9.99
======

* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.9.98
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* enhancement:Paginator: [``botocore``] Add additional paginators for CloudFormation
* api-change:``efs``: [``botocore``] Update efs client to latest version


1.9.97
======

* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version


1.9.96
======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.9.95
======

* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.94
======

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version


1.9.93
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version


1.9.92
======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version


1.9.91
======

* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version


1.9.90
======

* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version


1.9.89
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version


1.9.88
======

* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.87
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version


1.9.86
======

* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version


1.9.85
======

* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``sms-voice``: [``botocore``] Update sms-voice client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version


1.9.84
======

* api-change:``worklink``: [``botocore``] Update worklink client to latest version
* api-change:``apigatewaymanagementapi``: [``botocore``] Update apigatewaymanagementapi client to latest version
* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version


1.9.83
======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.82
======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.81
======

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.9.80
======

* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``backup``: [``botocore``] Update backup client to latest version


1.9.79
======

* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.78
======

* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.9.77
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.9.76
======

* api-change:``docdb``: [``botocore``] Update docdb client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.9.75
======

* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version


1.9.74
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.9.73
======

* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version


1.9.72
======

* enhancement:Paginator: [``botocore``] Added over 400 new paginators.
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version


1.9.71
======

* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``sms-voice``: [``botocore``] Update sms-voice client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version


1.9.70
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* enhancement:EndpointDiscovery: [``botocore``] Add a config option, ``endpoint_discovery_enabled``, for automatically discovering endpoints
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version


1.9.69
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version


1.9.68
======

* api-change:``apigatewayv2``: [``botocore``] Update apigatewayv2 client to latest version
* bugfix:Credentials: [``botocore``] Fixes an issue where credentials would be checked when creating an anonymous client. Fixes `#1472 <https://github.com/boto/botocore/issues/1472>`__
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version
* enhancement:StreamingBody: [``botocore``] Support iterating lines from a streaming response body with CRLF line endings
* api-change:``apigatewaymanagementapi``: [``botocore``] Update apigatewaymanagementapi client to latest version


1.9.67
======

* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``ecr``: [``botocore``] Update ecr client to latest version


1.9.66
======

* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version


1.9.65
======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version


1.9.64
======

* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.9.63
======

* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.9.62
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* enhancement:AssumeRole: [``botocore``] Add support for duration_seconds when assuming a role in the config file (`#1600 <https://github.com/boto/botocore/issues/1600>`__).
* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.9.61
======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.60
======

* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version


1.9.59
======

* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.9.58
======

* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.9.57
======

* bugfix:s3: [``botocore``] Add md5 header injection to new operations that require it
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.9.56
======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version
* api-change:``kafka``: [``botocore``] Update kafka client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version


1.9.55
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``appmesh``: [``botocore``] Update appmesh client to latest version
* api-change:``license-manager``: [``botocore``] Update license-manager client to latest version
* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.9.54
======

* api-change:``securityhub``: [``botocore``] Update securityhub client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``fsx``: [``botocore``] Update fsx client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.9.53
======

* api-change:``meteringmarketplace``: [``botocore``] Update meteringmarketplace client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version
* api-change:``translate``: [``botocore``] Update translate client to latest version
* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``kinesisanalytics``: [``botocore``] Update kinesisanalytics client to latest version
* api-change:``comprehendmedical``: [``botocore``] Update comprehendmedical client to latest version
* api-change:``mediaconnect``: [``botocore``] Update mediaconnect client to latest version
* api-change:``kinesisanalyticsv2``: [``botocore``] Update kinesisanalyticsv2 client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.52
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``sms``: [``botocore``] Update sms client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``globalaccelerator``: [``botocore``] Update globalaccelerator client to latest version


1.9.51
======

* api-change:``amplify``: [``botocore``] Update amplify client to latest version
* api-change:``transfer``: [``botocore``] Update transfer client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version
* api-change:``robomaker``: [``botocore``] Update robomaker client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``datasync``: [``botocore``] Update datasync client to latest version


1.9.50
======

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.9.49
======

* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``rds-data``: [``botocore``] Update rds-data client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``quicksight``: [``botocore``] Update quicksight client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version


1.9.48
======

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``workdocs``: [``botocore``] Update workdocs client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.9.47
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.9.46
======

* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``sms-voice``: [``botocore``] Update sms-voice client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``s3control``: [``botocore``] Update s3control client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``ram``: [``botocore``] Update ram client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``route53resolver``: [``botocore``] Update route53resolver client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version


1.9.45
======

* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.44
======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.9.43
======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``batch``: [``botocore``] Update batch client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.42
======

* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version


1.9.41
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version


1.9.40
======

* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.39
======

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``pinpoint-email``: [``botocore``] Update pinpoint-email client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* bugfix:session config: [``botocore``] Added the default session configuration tuples back to session.session_vars_map.


1.9.38
======

* api-change:``eks``: [``botocore``] Update eks client to latest version
* enhancement:Configuration: [``botocore``] Added new configuration provider methods allowing for more flexibility in how a botocore session loads a particular configuration value.
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version


1.9.37
======

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``clouddirectory``: [``botocore``] Update clouddirectory client to latest version


1.9.36
======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* enhancement:Exceptions: [``botocore``] Add the ability to pickle botocore exceptions (`834 <https://github.com/boto/botocore/issues/834>`__)


1.9.35
======

* api-change:``mediastore-data``: [``botocore``] Update mediastore-data client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version


1.9.34
======

* api-change:``chime``: [``botocore``] Update chime client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version


1.9.33
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.32
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.31
======

* api-change:``codestar``: [``botocore``] Update codestar client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.9.30
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.29
======

* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version


1.9.28
======

* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.27
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.9.26
======

* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version


1.9.25
======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version


1.9.24
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.9.23
======

* api-change:``cloudtrail``: [``botocore``] Update cloudtrail client to latest version


1.9.22
======

* api-change:``athena``: [``botocore``] Update athena client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version


1.9.21
======

* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.9.20
======

* enhancement:TLS: [``botocore``] Added support for configuring a client certificate and key when establishing TLS connections.
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* bugfix:InstanceMetadataFetcher: [``botocore``] Fix failure to retry on empty credentials and invalid JSON returned from IMDS `1049 <https://github.com/boto/botocore/issues/1049>`__ `1403 <https://github.com/boto/botocore/issues/1403>`__


1.9.19
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``iot-jobs-data``: [``botocore``] Update iot-jobs-data client to latest version


1.9.18
======

* api-change:``ds``: [``botocore``] Update ds client to latest version


1.9.17
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* enhancement:HTTP Session: [``botocore``] Added the ability to enable TCP Keepalive via the shared config file's ``tcp_keepalive`` option.
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version


1.9.16
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version


1.9.15
======

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.9.14
======

* api-change:``codestar``: [``botocore``] Update codestar client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.13
======

* api-change:``mq``: [``botocore``] Update mq client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* enhancement:Event: [``botocore``] Add the `before-send` event which allows finalized requests to be inspected before being sent across the wire and allows for custom responses to be returned.
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version


1.9.12
======

* api-change:``sqs``: [``botocore``] Update sqs client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.11
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version


1.9.10
======

* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.9.9
=====

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.9.8
=====

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.9.7
=====

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version


1.9.6
=====

* bugfix:Serialization: [``botocore``] Fixes `#1557 <https://github.com/boto/botocore/issues/1557>`__. Fixed a regression in serialization where request bodies would be improperly encoded.
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.9.5
=====

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``elastictranscoder``: [``botocore``] Update elastictranscoder client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``elasticache``: [``botocore``] Update elasticache client to latest version


1.9.4
=====

* enhancement:s3: [``botocore``] Adds encoding and decoding handlers for ListObjectsV2 `#1552 <https://github.com/boto/botocore/issues/1552>`__
* api-change:``polly``: [``botocore``] Update polly client to latest version


1.9.3
=====

* api-change:``ses``: [``botocore``] Update ses client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``fms``: [``botocore``] Update fms client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.9.2
=====

* api-change:``opsworkscm``: [``botocore``] Update opsworkscm client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.9.1
=====

* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version


1.9.0
=====

* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* feature:Events: [``botocore``] This migrates the event system to using sevice ids instead of either client name or endpoint prefix. This prevents issues that might arise when a service changes their endpoint prefix, also fixes a long-standing bug where you could not register an event to a particular service if it happened to share its endpoint prefix with another service (e.g. ``autoscaling`` and ``application-autoscaling`` both use the endpoint prefix ``autoscaling``). Please see the `upgrade notes <https://botocore.amazonaws.com/v1/documentation/api/latest/index.html#upgrade-notes>`_ to determine if you are impacted and how to proceed if you are.
* feature:Events: This migrates the event system to using sevice ids instead of either client name or endpoint prefix. This prevents issues that might arise when a service changes their endpoint prefix, also fixes a long-standing bug where you could not register an event to a particular service if it happened to share its endpoint prefix with another service (e.g. ``autoscaling`` and ``application-autoscaling`` both use the endpoint prefix ``autoscaling``). Please see the `upgrade notes <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/upgrading.html>`_ to determine if you are impacted and how to proceed if you are.


1.8.9
=====

* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.8.8
=====

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``elb``: [``botocore``] Update elb client to latest version


1.8.7
=====

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.8.6
=====

* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.8.5
=====

* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* bugfix:signing: [``botocore``] Fix an issue where mixed endpoint casing could cause a SigV4 signature mismatch.


1.8.4
=====

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version


1.8.3
=====

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version


1.8.2
=====

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``signer``: [``botocore``] Update signer client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version


1.8.1
=====

* api-change:``glue``: [``botocore``] Update glue client to latest version


1.8.0
=====

* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* feature:urllib3: [``botocore``] The vendored version of requests and urllib3 are no longer being used and botocore now has a direct dependency on newer versions of upstream urllib3.


1.7.84
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version
* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.7.83
======

* api-change:``snowball``: [``botocore``] Update snowball client to latest version


1.7.82
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version


1.7.81
======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.7.80
======

* api-change:``dax``: [``botocore``] Update dax client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.7.79
======

* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.7.78
======

* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.7.77
======

* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version


1.7.76
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.7.75
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.7.74
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``dax``: [``botocore``] Update dax client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.7.73
======

* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.7.72
======

* api-change:``logs``: [``botocore``] Update logs client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.7.71
======

* api-change:``health``: [``botocore``] Update health client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.7.70
======

* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.7.69
======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``kinesis``: [``botocore``] Update kinesis client to latest version
* api-change:``resource-groups``: [``botocore``] Update resource-groups client to latest version


1.7.68
======

* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.7.67
======

* api-change:``kms``: [``botocore``] Update kms client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``connect``: [``botocore``] Update connect client to latest version


1.7.66
======

* api-change:``directconnect``: [``botocore``] Update directconnect client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``mq``: [``botocore``] Update mq client to latest version
* enhancment:Timestamp Serialization: [``botocore``] Support explicit timestamp serialization per timestamp shape.
* api-change:``glacier``: [``botocore``] Update glacier client to latest version


1.7.65
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.7.64
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.7.63
======

* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.7.62
======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version


1.7.61
======

* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version


1.7.60
======

* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version


1.7.59
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``snowball``: [``botocore``] Update snowball client to latest version


1.7.58
======

* api-change:``kinesisvideo``: [``botocore``] Update kinesisvideo client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``kinesis-video-archived-media``: [``botocore``] Update kinesis-video-archived-media client to latest version


1.7.57
======

* api-change:``iam``: [``botocore``] Update iam client to latest version
* api-change:``dlm``: [``botocore``] Update dlm client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.7.56
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version


1.7.55
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``opsworks``: [``botocore``] Update opsworks client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.7.54
======

* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version


1.7.53
======

* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.7.52
======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version


1.7.51
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.7.50
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version


1.7.49
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.7.48
======

* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``lambda``: [``botocore``] Update lambda client to latest version


1.7.47
======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``comprehend``: [``botocore``] Update comprehend client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* enhancement:StreamingResponses: [``botocore``] Add ``iter_lines()`` and ``iter_chunks()`` to streaming responses (`#1195 <https://github.com/boto/botocore/issues/1195>`__)


1.7.46
======

* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``inspector``: [``botocore``] Update inspector client to latest version


1.7.45
======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.7.44
======

* api-change:``clouddirectory``: [``botocore``] Update clouddirectory client to latest version


1.7.43
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``macie``: [``botocore``] Update macie client to latest version
* api-change:``neptune``: [``botocore``] Update neptune client to latest version


1.7.42
======

* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.7.41
======

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version


1.7.40
======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version


1.7.39
======

* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version


1.7.38
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version


1.7.37
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.7.36
======

* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``clouddirectory``: [``botocore``] Update clouddirectory client to latest version


1.7.35
======

* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version


1.7.34
======

* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.7.33
======

* api-change:``polly``: [``botocore``] Update polly client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``shield``: [``botocore``] Update shield client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.7.32
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``mgh``: [``botocore``] Update mgh client to latest version
* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``eks``: [``botocore``] Update eks client to latest version


1.7.31
======

* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``mediatailor``: [``botocore``] Update mediatailor client to latest version
* api-change:``sns``: [``botocore``] Update sns client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version


1.7.30
======

* api-change:``neptune``: [``botocore``] Update neptune client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.7.29
======

* api-change:``pi``: [``botocore``] Update pi client to latest version


1.7.28
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.7.27
======

* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.7.26
======

* api-change:``inspector``: [``botocore``] Update inspector client to latest version
* enhancement:Credentials: [``botocore``] Disable proxy configuration when fetching container credentials
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.7.25
======

* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version


1.7.24
======

* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``ses``: [``botocore``] Update ses client to latest version


1.7.23
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version


1.7.22
======

* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version


1.7.21
======

* api-change:``config``: [``botocore``] Update config client to latest version


1.7.20
======

* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``iot1click-devices``: [``botocore``] Update iot1click-devices client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``iot1click-projects``: [``botocore``] Update iot1click-projects client to latest version


1.7.19
======

* api-change:``firehose``: [``botocore``] Update firehose client to latest version


1.7.18
======

* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version


1.7.17
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version


1.7.16
======

* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.7.15
======

* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.7.14
======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version


1.7.13
======

* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``appsync``: [``botocore``] Update appsync client to latest version


1.7.12
======

* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.7.11
======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* api-change:``route53domains``: [``botocore``] Update route53domains client to latest version
* api-change:``workspaces``: [``botocore``] Update workspaces client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version


1.7.10
======

* api-change:``glacier``: [``botocore``] Update glacier client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version


1.7.9
=====

* api-change:``rekognition``: [``botocore``] Update rekognition client to latest version
* api-change:``xray``: [``botocore``] Update xray client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version


1.7.8
=====

* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version


1.7.7
=====

* api-change:``iotanalytics``: [``botocore``] Update iotanalytics client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version


1.7.6
=====

* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``firehose``: [``botocore``] Update firehose client to latest version


1.7.5
=====

* api-change:``ce``: [``botocore``] Update ce client to latest version
* api-change:``codepipeline``: [``botocore``] Update codepipeline client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* bugfix:dynamodb: Fixes a bug causing dynamodb operations with no output to throw errors.


1.7.4
=====

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``workmail``: [``botocore``] Update workmail client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``mediapackage``: [``botocore``] Update mediapackage client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.7.3
=====

* api-change:``clouddirectory``: [``botocore``] Update clouddirectory client to latest version


1.7.2
=====

* api-change:``batch``: [``botocore``] Update batch client to latest version


1.7.1
=====

* enhancement:shield: [``botocore``] Added paginator for list_protections operation.
* api-change:``ssm``: [``botocore``] Update ssm client to latest version


1.7.0
=====

* api-change:``s3``: [``botocore``] Update s3 client to latest version
* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version
* api-change:``secretsmanager``: [``botocore``] Update secretsmanager client to latest version
* api-change:``acm-pca``: [``botocore``] Update acm-pca client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* feature:s3: Add support for S3 Select. Amazon S3 Select is an Amazon S3 feature that makes it easy to retrieve specific data from the contents of an object using simple SQL expressions without having to retrieve the entire object. With this release of the Amazon S3 SDK, S3 Select API (SelectObjectContent) is now generally available in all public regions. This release supports retrieval of a subset of data using SQL clauses, like SELECT and WHERE, from delimited text files and JSON objects in Amazon S3 through the SelectObjectContent API available in AWS S3 SDK.
* api-change:``fms``: [``botocore``] Update fms client to latest version


1.6.23
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version
* api-change:``translate``: [``botocore``] Update translate client to latest version


1.6.22
======

* api-change:``cloudfront``: [``botocore``] Update cloudfront client to latest version
* api-change:``apigateway``: [``botocore``] Update apigateway client to latest version
* api-change:``es``: [``botocore``] Update es client to latest version


1.6.21
======

* api-change:``connect``: [``botocore``] Update connect client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version


1.6.20
======

* api-change:``greengrass``: [``botocore``] Update greengrass client to latest version
* api-change:``cloudformation``: [``botocore``] Update cloudformation client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version


1.6.19
======

* api-change:``mturk``: [``botocore``] Update mturk client to latest version
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``iam``: [``botocore``] Update iam client to latest version


1.6.18
======

* api-change:``acm``: [``botocore``] Update acm client to latest version


1.6.17
======

* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* bugfix:``s3``: [``botocore``] Fix bug where invalid head_object requests would cause an infinite loop (alternate fix to `#1400 <https://github.com/boto/botocore/issues/1400>`__)


1.6.16
======

* api-change:``rds``: [``botocore``] Update rds client to latest version


1.6.15
======

* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version


1.6.14
======

* bugfix:``s3``: [``botocore``] Fix regression in redirects in using wrong region


1.6.13
======

* bugfix:s3: [``botocore``] Fixed a bug where head object and bucket calls would attempt redirects incorrectly.
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version


1.6.12
======

* api-change:``ce``: [``botocore``] Update ce client to latest version
* enhancement:Credentials: [``botocore``] Add the ability to disable fetching credentials from EC2 metadata by setting the environment variable AWS_EC2_METADATA_DISABLED to 'true'.
* api-change:``config``: [``botocore``] Update config client to latest version
* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* bugfix:Credentials: [``botocore``] Fix a race condition related to assuming a role for the first time (`#1405 <https://github.com/boto/botocore/pull/1405>`__)
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.6.11
======

* api-change:``elasticbeanstalk``: [``botocore``] Update elasticbeanstalk client to latest version


1.6.10
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version
* api-change:``organizations``: [``botocore``] Update organizations client to latest version
* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version


1.6.9
=====

* api-change:``lightsail``: [``botocore``] Update lightsail client to latest version


1.6.8
=====

* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version


1.6.7
=====

* api-change:``cloudhsmv2``: [``botocore``] Update cloudhsmv2 client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``iot``: [``botocore``] Update iot client to latest version
* api-change:``redshift``: [``botocore``] Update redshift client to latest version


1.6.6
=====

* api-change:``pinpoint``: [``botocore``] Update pinpoint client to latest version
* api-change:``ecs``: [``botocore``] Update ecs client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``mgh``: [``botocore``] Update mgh client to latest version


1.6.5
=====

* api-change:``medialive``: [``botocore``] Update medialive client to latest version


1.6.4
=====

* api-change:``ecs``: [``botocore``] Update ecs client to latest version


1.6.3
=====

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``storagegateway``: [``botocore``] Update storagegateway client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version


1.6.2
=====

* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version


1.6.1
=====

* api-change:``ecr``: [``botocore``] Update ecr client to latest version


1.6.0
=====

* enhancement:Stubber: [``botocore``] Added the ability to add items to response metadata with the stubber.
* api-change:``sts``: [``botocore``] Update sts client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version
* feature:``s3``: [``botocore``] Default to virtual hosted addressing regardless of signature version (boto/botocore`#1387 <https://github.com/boto/botocore/issues/1387>`__)


1.5.36
======

* api-change:``appstream``: [``botocore``] Update appstream client to latest version


1.5.35
======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``ce``: [``botocore``] Update ce client to latest version


1.5.34
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``serverlessrepo``: [``botocore``] Update serverlessrepo client to latest version
* api-change:``codecommit``: [``botocore``] Update codecommit client to latest version


1.5.33
======

* api-change:``autoscaling``: [``botocore``] Update autoscaling client to latest version
* api-change:``waf-regional``: [``botocore``] Update waf-regional client to latest version
* api-change:``waf``: [``botocore``] Update waf client to latest version


1.5.32
======

* api-change:``config``: [``botocore``] Update config client to latest version


1.5.31
======

* api-change:``rds``: [``botocore``] Update rds client to latest version


1.5.30
======

* api-change:``mediaconvert``: [``botocore``] Update mediaconvert client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version


1.5.29
======

* api-change:``appsync``: [``botocore``] Update appsync client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version


1.5.28
======

* api-change:``glacier``: [``botocore``] Update glacier client to latest version
* api-change:``route53``: [``botocore``] Update route53 client to latest version


1.5.27
======

* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* api-change:``cognito-idp``: [``botocore``] Update cognito-idp client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``kms``: [``botocore``] Update kms client to latest version


1.5.26
======

* api-change:``lex-runtime``: [``botocore``] Update lex-runtime client to latest version
* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``lex-models``: [``botocore``] Update lex-models client to latest version


1.5.25
======

* api-change:``ds``: [``botocore``] Update ds client to latest version
* api-change:``appstream``: [``botocore``] Update appstream client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``budgets``: [``botocore``] Update budgets client to latest version
* api-change:``gamelift``: [``botocore``] Update gamelift client to latest version
* api-change:``dynamodb``: [``botocore``] Update dynamodb client to latest version
* api-change:``dms``: [``botocore``] Update dms client to latest version
* api-change:``mediastore``: [``botocore``] Update mediastore client to latest version


1.5.24
======

* api-change:``servicediscovery``: [``botocore``] Update servicediscovery client to latest version
* api-change:``servicecatalog``: [``botocore``] Update servicecatalog client to latest version
* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``glue``: [``botocore``] Update glue client to latest version


1.5.23
======

* api-change:``cloud9``: [``botocore``] Update cloud9 client to latest version
* api-change:``acm``: [``botocore``] Update acm client to latest version
* api-change:``kinesis``: [``botocore``] Update kinesis client to latest version
* api-change:``opsworks``: [``botocore``] Update opsworks client to latest version


1.5.22
======

* api-change:``mturk``: [``botocore``] Update mturk client to latest version
* api-change:``medialive``: [``botocore``] Update medialive client to latest version
* api-change:``devicefarm``: [``botocore``] Update devicefarm client to latest version


1.5.21
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* api-change:``codebuild``: [``botocore``] Update codebuild client to latest version
* api-change:``alexaforbusiness``: [``botocore``] Update alexaforbusiness client to latest version
* bugfix:Presign: [``botocore``] Fix issue where some events were not fired during the presigning of a request thus not including a variety of customizations (`#1340 <https://github.com/boto/botocore/issues/1340>`__)
* enhancement:Credentials: [``botocore``] Improved error message when the source profile for an assume role is misconfigured. Fixes aws/aws-cli`#2763 <https://github.com/aws/aws-cli/issues/2763>`__
* api-change:``guardduty``: [``botocore``] Update guardduty client to latest version
* enhancment:Paginator: [``botocore``] Added paginators for a number of services where the result key is unambiguous.


1.5.20
======

* api-change:``budgets``: [``botocore``] Update budgets client to latest version


1.5.19
======

* api-change:``glue``: [``botocore``] Update glue client to latest version
* api-change:``transcribe``: [``botocore``] Update transcribe client to latest version


1.5.18
======

* api-change:``sagemaker``: [``botocore``] Update sagemaker client to latest version


1.5.17
======

* api-change:``ec2``: [``botocore``] Update ec2 client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version


1.5.16
======

* api-change:``application-autoscaling``: [``botocore``] Update application-autoscaling client to latest version
* api-change:``autoscaling-plans``: [``botocore``] Update autoscaling-plans client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version


1.5.15
======

* api-change:``lambda``: [``botocore``] Update lambda client to latest version
* enhancement:cloudformation get_template template body ordering: [``botocore``] fixes boto/boto3`#1378 <https://github.com/boto/boto3/issues/1378>`__


1.5.14
======

* api-change:``glue``: [``botocore``] Update glue client to latest version


1.5.13
======

* api-change:``ssm``: [``botocore``] Update ssm client to latest version
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``rds``: [``botocore``] Update rds client to latest version
* api-change:``elb``: [``botocore``] Update elb client to latest version


1.5.12
======

* api-change:``kms``: [``botocore``] Update kms client to latest version


1.5.11
======

* api-change:``ds``: [``botocore``] Update ds client to latest version


1.5.10
======

* api-change:``route53``: [``botocore``] Update route53 client to latest version
* api-change:``discovery``: [``botocore``] Update discovery client to latest version
* api-change:``codedeploy``: [``botocore``] Update codedeploy client to latest version


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
* bugfix:s3: Port ``s3.transfer`` module to use ``s3transfer`` package. Please refer to `Upgrading Notes <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/upgrading.html>`_ when upgrading. In porting the logic over, various performance issues and bugs were fixed.
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

