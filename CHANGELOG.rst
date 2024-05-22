=========
CHANGELOG
=========

1.34.111
========

* api-change:``chatbot``: [``botocore``] This change adds support for tagging Chatbot configurations.
* api-change:``cloudformation``: [``botocore``] Added DeletionMode FORCE_DELETE_STACK for deleting a stack that is stuck in DELETE_FAILED state due to resource deletion failure.
* api-change:``kms``: [``botocore``] This release includes feature to import customer's asymmetric (RSA, ECC and SM2) and HMAC keys into KMS in China.
* api-change:``opensearch``: [``botocore``] This release adds support for enabling or disabling a data source configured as part of Zero-ETL integration with Amazon S3, by setting its status.
* api-change:``wafv2``: [``botocore``] You can now use Security Lake to collect web ACL traffic data.


1.34.110
========

* api-change:``cloudfront``: [``botocore``] Model update; no change to SDK functionality.
* api-change:``glue``: [``botocore``] Add Maintenance window to CreateJob and UpdateJob APIs and JobRun response. Add a new Job Run State for EXPIRED.
* api-change:``lightsail``: [``botocore``] This release adds support for Amazon Lightsail instances to switch between dual-stack or IPv4 only and IPv6-only public IP address types.
* api-change:``mailmanager``: [``botocore``] This release includes a new Amazon SES feature called Mail Manager, which is a set of email gateway capabilities designed to help customers strengthen their organization's email infrastructure, simplify email workflow management, and streamline email compliance control.
* api-change:``pi``: [``botocore``] Performance Insights added a new input parameter called AuthorizedActions to support the fine-grained access feature. Performance Insights also restricted the acceptable input characters.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for Db2 license through AWS Marketplace.
* api-change:``storagegateway``: [``botocore``] Added new SMBSecurityStrategy enum named MandatoryEncryptionNoAes128, new mode enforces encryption and disables AES 128-bit algorithums.


1.34.109
========

* api-change:``bedrock-agent``: [``botocore``] This release adds support for using Guardrails with Bedrock Agents.
* api-change:``bedrock-agent-runtime``: [``botocore``] This release adds support for using Guardrails with Bedrock Agents.
* api-change:``controltower``: [``botocore``] Added ListControlOperations API and filtering support for ListEnabledControls API. Updates also includes added metadata for enabled controls and control operations.
* api-change:``osis``: [``botocore``] Add support for creating an OpenSearch Ingestion pipeline that is attached to a provided VPC. Add information about the destinations of an OpenSearch Ingestion pipeline to the GetPipeline and ListPipelines APIs.
* api-change:``rds``: [``botocore``] This release adds support for EngineLifecycleSupport on DBInstances, DBClusters, and GlobalClusters.
* api-change:``secretsmanager``: [``botocore``] add v2 smoke tests and smithy smokeTests trait for SDK testing


1.34.108
========

* api-change:``application-autoscaling``: [``botocore``] add v2 smoke tests and smithy smokeTests trait for SDK testing.
* api-change:``codebuild``: [``botocore``] Aws CodeBuild now supports 36 hours build timeout
* api-change:``elbv2``: [``botocore``] This release adds dualstack-without-public-ipv4 IP address type for ALB.
* api-change:``lakeformation``: [``botocore``] Introduces a new API, GetDataLakePrincipal, that returns the identity of the invoking principal
* api-change:``transfer``: [``botocore``] Enable use of CloudFormation traits in Smithy model to improve generated CloudFormation schema from the Smithy API model.


1.34.107
========

* api-change:``acm-pca``: [``botocore``] This release adds support for waiters to fail on AccessDeniedException when having insufficient permissions
* api-change:``connect``: [``botocore``] Adding Contact Flow metrics to the GetMetricDataV2 API
* api-change:``kafka``: [``botocore``] AWS MSK support for Broker Removal.
* api-change:``mwaa``: [``botocore``] Amazon MWAA now supports Airflow web server auto scaling to automatically handle increased demand from REST APIs, Command Line Interface (CLI), or more Airflow User Interface (UI) users. Customers can specify maximum and minimum web server instances during environment creation and update workflow.
* api-change:``quicksight``: [``botocore``] This release adds DescribeKeyRegistration and UpdateKeyRegistration APIs to manage QuickSight Customer Managed Keys (CMK).
* api-change:``sagemaker``: [``botocore``] Introduced WorkerAccessConfiguration to SageMaker Workteam. This allows customers to configure resource access for workers in a workteam.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for AWS Secrets Manager
* bugfix:retries: [``botocore``] Fix backoff calculation for truncated binary exponential backoff (`#3178 <https://github.com/boto/botocore/issues/3178>`__)


1.34.106
========

* api-change:``bedrock-agent-runtime``: [``botocore``] Updating Bedrock Knowledge Base Metadata & Filters feature with two new filters listContains and stringContains
* api-change:``codebuild``: [``botocore``] CodeBuild Reserved Capacity VPC Support
* api-change:``datasync``: [``botocore``] Task executions now display a CANCELLING status when an execution is in the process of being cancelled.
* api-change:``grafana``: [``botocore``] This release adds new ServiceAccount and ServiceAccountToken APIs.
* api-change:``medical-imaging``: [``botocore``] Added support for importing medical imaging data from Amazon S3 buckets across accounts and regions.
* api-change:``securityhub``: [``botocore``] Documentation-only update for AWS Security Hub


1.34.105
========

* api-change:``connect``: [``botocore``] Amazon Connect provides enhanced search capabilities for flows & flow modules on the Connect admin website and programmatically using APIs. You can search for flows and flow modules by name, description, type, status, and tags, to filter and identify a specific flow in your Connect instances.
* api-change:``s3``: [``botocore``] Updated a few x-id in the http uri traits


1.34.104
========

* api-change:``events``: [``botocore``] Amazon EventBridge introduces KMS customer-managed key (CMK) encryption support for custom and partner events published on EventBridge Event Bus (including default bus) and UpdateEventBus API.
* api-change:``vpc-lattice``: [``botocore``] This release adds TLS Passthrough support. It also increases max number of target group per rule to 10.


1.34.103
========

* api-change:``discovery``: [``botocore``] add v2 smoke tests and smithy smokeTests trait for SDK testing
* api-change:``greengrassv2``: [``botocore``] Mark ComponentVersion in ComponentDeploymentSpecification as required.
* api-change:``sagemaker``: [``botocore``] Introduced support for G6 instance types on Sagemaker Notebook Instances and on SageMaker Studio for JupyterLab and CodeEditor applications.
* api-change:``sso-oidc``: [``botocore``] Updated request parameters for PKCE support.


1.34.102
========

* api-change:``bedrock-agent-runtime``: [``botocore``] This release adds support to provide guardrail configuration and modify inference parameters that are then used in RetrieveAndGenerate API in Agents for Amazon Bedrock.
* api-change:``pinpoint``: [``botocore``] This release adds support for specifying email message headers for Email Templates, Campaigns, Journeys and Send Messages.
* api-change:``route53resolver``: [``botocore``] Update the DNS Firewall settings to correct a spelling issue.
* api-change:``ssm-sap``: [``botocore``] Added support for application-aware start/stop of SAP applications running on EC2 instances, with SSM for SAP
* api-change:``verifiedpermissions``: [``botocore``] Adds policy effect and actions fields to Policy API's.


1.34.101
========

* api-change:``cognito-idp``: [``botocore``] Add EXTERNAL_PROVIDER enum value to UserStatusType.
* api-change:``ec2``: [``botocore``] Adding Precision Hardware Clock (PHC) to public API DescribeInstanceTypes
* api-change:``ecr``: [``botocore``] This release adds pull through cache rules support for GitLab container registry in Amazon ECR.
* api-change:``fms``: [``botocore``] The policy scope resource tag is always a string value, either a non-empty string or an empty string.
* api-change:``polly``: [``botocore``] Add new engine - generative - that builds the most expressive conversational voices.
* api-change:``sqs``: [``botocore``] This release adds MessageSystemAttributeNames to ReceiveMessageRequest to replace AttributeNames.


1.34.100
========

* api-change:``b2bi``: [``botocore``] Documentation update to clarify the MappingTemplate definition.
* api-change:``budgets``: [``botocore``] This release adds tag support for budgets and budget actions.
* api-change:``resiliencehub``: [``botocore``] AWS Resilience Hub has expanded its drift detection capabilities by introducing a new type of drift detection - application resource drift. This new enhancement detects changes, such as the addition or deletion of resources within the application's input sources.
* api-change:``route53profiles``: [``botocore``] Doc only update for Route 53 profiles that fixes some link  issues


1.34.99
=======

* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive now supports configuring how SCTE 35 passthrough triggers segment breaks in HLS and MediaPackage output groups. Previously, messages triggered breaks in all these output groups. The new option is to trigger segment breaks only in groups that have SCTE 35 passthrough enabled.


1.34.98
=======

* api-change:``bedrock-agent``: [``botocore``] This release adds support for using Provisioned Throughput with Bedrock Agents.
* api-change:``connect``: [``botocore``] This release adds 5 new APIs for managing attachments: StartAttachedFileUpload, CompleteAttachedFileUpload, GetAttachedFile, BatchGetAttachedFileMetadata, DeleteAttachedFile. These APIs can be used to programmatically upload and download attachments to Connect resources, like cases.
* api-change:``connectcases``: [``botocore``] This feature supports the release of Files related items
* api-change:``datasync``: [``botocore``] Updated guidance on using private or self-signed certificate authorities (CAs) with AWS DataSync object storage locations.
* api-change:``inspector2``: [``botocore``] This release adds CSV format to GetCisScanReport for Inspector v2
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Inference now supports m6i, c6i, r6i, m7i, c7i, r7i and g5 instance types for Batch Transform Jobs
* api-change:``sesv2``: [``botocore``] Adds support for specifying replacement headers per BulkEmailEntry in SendBulkEmail in SESv2.


1.34.97
=======

* api-change:``dynamodb``: [``botocore``] This release adds support to specify an optional, maximum OnDemandThroughput for DynamoDB tables and global secondary indexes in the CreateTable or UpdateTable APIs. You can also override the OnDemandThroughput settings by calling the ImportTable, RestoreFromPointInTime, or RestoreFromBackup APIs.
* api-change:``ec2``: [``botocore``] This release includes a new API for retrieving the public endorsement key of the EC2 instance's Nitro Trusted Platform Module (NitroTPM).
* api-change:``personalize``: [``botocore``] This releases ability to delete users and their data, including their metadata and interactions data, from a dataset group.
* api-change:``redshift-serverless``: [``botocore``] Update Redshift Serverless List Scheduled Actions Output Response to include Namespace Name.


1.34.96
=======

* api-change:``bedrock-agent``: [``botocore``] This release adds support for using MongoDB Atlas as a vector store when creating a knowledge base.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``personalize-runtime``: [``botocore``] This release adds support for a Reason attribute for predicted items generated by User-Personalization-v2.
* api-change:``securityhub``: [``botocore``] Updated CreateMembers API request with limits.
* api-change:``sesv2``: [``botocore``] Fixes ListContacts and ListImportJobs APIs to use POST instead of GET.


1.34.95
=======

* api-change:``chime-sdk-voice``: [``botocore``] Due to changes made by the Amazon Alexa service, GetSipMediaApplicationAlexaSkillConfiguration and PutSipMediaApplicationAlexaSkillConfiguration APIs are no longer available for use. For more information, refer to the Alexa Smart Properties page.
* api-change:``codeartifact``: [``botocore``] Add support for the Ruby package format.
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports the network firewall service stream exception policy feature for accounts within your organization.
* api-change:``omics``: [``botocore``] Add support for workflow sharing and dynamic run storage
* api-change:``opensearch``: [``botocore``] This release enables customers to create Route53 A and AAAA alias record types to point custom endpoint domain to OpenSearch domain's dualstack search endpoint.
* api-change:``pinpoint-sms-voice-v2``: [``botocore``] Amazon Pinpoint has added two new features Multimedia services (MMS) and protect configurations. Use the three new MMS APIs to send media messages to a mobile phone which includes image, audio, text, or video files. Use the ten new protect configurations APIs to block messages to specific countries.
* api-change:``qbusiness``: [``botocore``] This is a general availability (GA) release of Amazon Q Business. Q Business enables employees in an enterprise to get comprehensive answers to complex questions and take actions through a unified, intuitive web-based chat experience - using an enterprise's existing content, data, and systems.
* api-change:``quicksight``: [``botocore``] New Q embedding supporting Generative Q&A
* api-change:``route53resolver``: [``botocore``] Release of FirewallDomainRedirectionAction parameter on the Route 53 DNS Firewall Rule.  This allows customers to configure a DNS Firewall rule to inspect all the domains in the DNS redirection chain (default) , such as CNAME, ALIAS, DNAME, etc., or just the first domain and trust the rest.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Training now supports the use of attribute-based access control (ABAC) roles for training job execution roles. Amazon SageMaker Inference now supports G6 instance types.
* api-change:``signer``: [``botocore``] Documentation updates for AWS Signer. Adds cross-account signing constraint and definitions for cross-account actions.


1.34.94
=======

* api-change:``amplify``: [``botocore``] Updating max results limit for listing any resources (Job, Artifacts, Branch, BackendResources, DomainAssociation) to 50 with the exception of list apps that where max results can be up to 100.
* api-change:``connectcases``: [``botocore``] This feature releases DeleteField, DeletedLayout, and DeleteTemplate API's
* api-change:``inspector2``: [``botocore``] Update Inspector2 to include new Agentless API parameters.
* api-change:``timestream-query``: [``botocore``] This change allows users to update and describe account settings associated with their accounts.
* api-change:``transcribe``: [``botocore``] This update provides error messaging for generative call summarization in Transcribe Call Analytics
* api-change:``trustedadvisor``: [``botocore``] This release adds the BatchUpdateRecommendationResourceExclusion API to support batch updates of Recommendation Resource exclusion statuses and introduces a new exclusion status filter to the ListRecommendationResources and ListOrganizationRecommendationResources APIs.


1.34.93
=======

* api-change:``codepipeline``: [``botocore``] Add ability to manually and automatically roll back a pipeline stage to a previously successful execution.
* api-change:``cognito-idp``: [``botocore``] Add LimitExceededException to SignUp errors
* api-change:``connectcampaigns``: [``botocore``] This release adds support for specifying if Answering Machine should wait for prompt sound.
* api-change:``marketplace-entitlement``: [``botocore``] Releasing minor endpoint updates.
* api-change:``oam``: [``botocore``] This release introduces support for Source Accounts to define which Metrics and Logs to share with the Monitoring Account
* api-change:``rds``: [``botocore``] SupportsLimitlessDatabase field added to describe-db-engine-versions to indicate whether the DB engine version supports Aurora Limitless Database.
* api-change:``support``: [``botocore``] Releasing minor endpoint updates.


1.34.92
=======

* api-change:``appsync``: [``botocore``] UpdateGraphQLAPI documentation update and datasource introspection secret arn update
* api-change:``fms``: [``botocore``] AWS Firewall Manager adds support for network ACL policies to manage Amazon Virtual Private Cloud (VPC) network access control lists (ACLs) for accounts in your organization.
* api-change:``ivs``: [``botocore``] Bug Fix: IVS does not support arns with the `svs` prefix
* api-change:``ivs-realtime``: [``botocore``] Bug Fix: IVS Real Time does not support ARNs using the `svs` prefix.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for setting local time zones for RDS for Db2 DB instances.
* api-change:``stepfunctions``: [``botocore``] Add new ValidateStateMachineDefinition operation, which performs syntax checking on the definition of a Amazon States Language (ASL) state machine.


1.34.91
=======

* api-change:``datasync``: [``botocore``] This change allows users to disable and enable the schedules associated with their tasks.
* api-change:``ec2``: [``botocore``] Launching capability for customers to enable or disable automatic assignment of public IPv4 addresses to their network interface
* api-change:``emr-containers``: [``botocore``] EMRonEKS Service support for SecurityConfiguration enforcement for Spark Jobs.
* api-change:``entityresolution``: [``botocore``] Support Batch Unique IDs Deletion.
* api-change:``gamelift``: [``botocore``] Amazon GameLift releases container fleets support for public preview. Deploy Linux-based containerized game server software for hosting on Amazon GameLift.
* api-change:``ssm``: [``botocore``] Add SSM DescribeInstanceProperties API to public AWS SDK.


1.34.90
=======

* api-change:``bedrock``: [``botocore``] This release introduces Model Evaluation and Guardrails for Amazon Bedrock.
* api-change:``bedrock-agent``: [``botocore``] Introducing the ability to create multiple data sources per knowledge base, specify S3 buckets as data sources from external accounts, and exposing levers to define the deletion behavior of the underlying vector store data.
* api-change:``bedrock-agent-runtime``: [``botocore``] This release introduces zero-setup file upload support for the RetrieveAndGenerate API. This allows you to chat with your data without setting up a Knowledge Base.
* api-change:``bedrock-runtime``: [``botocore``] This release introduces Guardrails for Amazon Bedrock.
* api-change:``ce``: [``botocore``] Added additional metadata that might be applicable to your reservation recommendations.
* api-change:``ec2``: [``botocore``] This release introduces EC2 AMI Deregistration Protection, a new AMI property that can be enabled by customers to protect an AMI against an unintended deregistration. This release also enables the AMI owners to view the AMI 'LastLaunchedTime' in DescribeImages API.
* api-change:``pi``: [``botocore``] Clarifies how aggregation works for GetResourceMetrics in the Performance Insights API.
* api-change:``rds``: [``botocore``] Fix the example ARN for ModifyActivityStreamRequest
* api-change:``sqs``: [``botocore``] This release enables customers to call SQS using AWS JSON-1.0 protocol
* api-change:``workspaces-web``: [``botocore``] Added InstanceType and MaxConcurrentSessions parameters on CreatePortal and UpdatePortal Operations as well as the ability to read Customer Managed Key & Additional Encryption Context parameters on supported resources (Portal, BrowserSettings, UserSettings, IPAccessSettings)


1.34.89
=======

* api-change:``bedrock-agent``: [``botocore``] Releasing the support for simplified configuration and return of control
* api-change:``bedrock-agent-runtime``: [``botocore``] Releasing the support for simplified configuration and return of control
* api-change:``payment-cryptography``: [``botocore``] Adding support to TR-31/TR-34 exports for optional headers, allowing customers to add additional metadata (such as key version and KSN) when exporting keys from the service.
* api-change:``redshift-serverless``: [``botocore``] Updates description of schedule field for scheduled actions.
* api-change:``route53profiles``: [``botocore``] Route 53 Profiles allows you to apply a central DNS configuration across many VPCs regardless of account.
* api-change:``sagemaker``: [``botocore``] This release adds support for Real-Time Collaboration and Shared Space for JupyterLab App on SageMaker Studio.
* api-change:``servicediscovery``: [``botocore``] This release adds examples to several Cloud Map actions.
* api-change:``transfer``: [``botocore``] Adding new API to support remote directory listing using SFTP connector


1.34.88
=======

* api-change:``glue``: [``botocore``] Adding RowFilter in the response for GetUnfilteredTableMetadata API
* api-change:``internetmonitor``: [``botocore``] This update introduces the GetInternetEvent and ListInternetEvents APIs, which provide access to internet events displayed on the Amazon CloudWatch Internet Weather Map.
* api-change:``personalize``: [``botocore``] This releases auto training capability while creating a solution and automatically syncing latest solution versions when creating/updating a campaign


1.34.87
=======

* api-change:``drs``: [``botocore``] Outpost ARN added to Source Server and Recovery Instance
* api-change:``emr-serverless``: [``botocore``] This release adds the capability to publish detailed Spark engine metrics to Amazon Managed Service for Prometheus (AMP) for  enhanced monitoring for Spark jobs.
* api-change:``guardduty``: [``botocore``] Added IPv6Address fields for local and remote IP addresses
* api-change:``quicksight``: [``botocore``] This release adds support for the Cross Sheet Filter and Control features, and support for warnings in asset imports for any permitted errors encountered during execution
* api-change:``rolesanywhere``: [``botocore``] This release introduces the PutAttributeMapping and DeleteAttributeMapping APIs. IAM Roles Anywhere now provides the capability to define a set of mapping rules, allowing customers to specify which data is extracted from their X.509 end-entity certificates.
* api-change:``sagemaker``: [``botocore``] Removed deprecated enum values and updated API documentation.
* api-change:``workspaces``: [``botocore``] Adds new APIs for managing and sharing WorkSpaces BYOL configuration across accounts.


1.34.86
=======

* api-change:``ec2``: [``botocore``] Documentation updates for Elastic Compute Cloud (EC2).
* api-change:``qbusiness``: [``botocore``] This release adds support for IAM Identity Center (IDC) as the identity gateway for Q Business. It also allows users to provide an explicit intent for Q Business to identify how the Chat request should be handled.


1.34.85
=======

* api-change:``bedrock-agent``: [``botocore``] For Create Agent API, the agentResourceRoleArn parameter is no longer required.
* api-change:``emr-serverless``: [``botocore``] This release adds support for shuffle optimized disks that allow larger disk sizes and higher IOPS to efficiently run shuffle heavy workloads.
* api-change:``entityresolution``: [``botocore``] Cross Account Resource Support .
* api-change:``iotwireless``: [``botocore``] Add PublicGateways in the GetWirelessStatistics call response, indicating the LoRaWAN public network accessed by the device.
* api-change:``lakeformation``: [``botocore``] This release adds Lake Formation managed RAM support for the 4 APIs - "DescribeLakeFormationIdentityCenterConfiguration", "CreateLakeFormationIdentityCenterConfiguration", "DescribeLakeFormationIdentityCenterConfiguration", and "DeleteLakeFormationIdentityCenterConfiguration"
* api-change:``m2``: [``botocore``] Adding new ListBatchJobRestartPoints API and support for restart batch job.
* api-change:``mediapackagev2``: [``botocore``] Dash v2 is a MediaPackage V2 feature to support egressing on DASH manifest format.
* api-change:``outposts``: [``botocore``] This release adds new APIs to allow customers to configure their Outpost capacity at order-time.
* api-change:``wellarchitected``: [``botocore``] AWS Well-Architected now has a Connector for Jira to allow customers to efficiently track workload risks and improvement efforts and create closed-loop mechanisms.
* enhancement:AWSCRT: [``botocore``] Update awscrt version to 0.20.9


1.34.84
=======

* api-change:``cloudformation``: [``botocore``] Adding support for the new parameter "IncludePropertyValues" in the CloudFormation DescribeChangeSet API. When this parameter is included, the DescribeChangeSet response will include more detailed information such as before and after values for the resource properties that will change.
* api-change:``config``: [``botocore``] Updates documentation for AWS Config
* api-change:``glue``: [``botocore``] Modifying request for GetUnfilteredTableMetadata for view-related fields.
* api-change:``healthlake``: [``botocore``] Added new CREATE_FAILED status for data stores. Added new errorCause to DescribeFHIRDatastore API and ListFHIRDatastores API response for additional insights into data store creation and deletion workflows.
* api-change:``iotfleethub``: [``botocore``] Documentation updates for AWS IoT Fleet Hub to clarify that Fleet Hub supports organization instance of IAM Identity Center.
* api-change:``kms``: [``botocore``] This feature supports the ability to specify a custom rotation period for automatic key rotations, the ability to perform on-demand key rotations, and visibility into your key material rotations.
* api-change:``mediatailor``: [``botocore``] Added InsertionMode to PlaybackConfigurations. This setting controls whether players can use stitched or guided ad insertion. The default for players that do not specify an insertion mode is stitched.
* api-change:``neptune-graph``: [``botocore``] Update to API documentation to resolve customer reported issues.
* api-change:``outposts``: [``botocore``] This release adds EXPEDITORS as a valid shipment carrier.
* api-change:``redshift``: [``botocore``] Adds support for Amazon Redshift DescribeClusterSnapshots API to include Snapshot ARN response field.
* api-change:``transfer``: [``botocore``] This change releases support for importing self signed certificates to the Transfer Family for sending outbound file transfers over TLS/HTTPS.


1.34.83
=======

* api-change:``batch``: [``botocore``] This release adds the task properties field to attempt details and the name field on EKS container detail.
* api-change:``cloudfront``: [``botocore``] CloudFront origin access control extends support to AWS Lambda function URLs and AWS Elemental MediaPackage v2 origins.
* api-change:``cloudwatch``: [``botocore``] This release adds support for Metric Characteristics for CloudWatch Anomaly Detection. Anomaly Detector now takes Metric Characteristics object with Periodic Spikes boolean field that tells Anomaly Detection that spikes that repeat at the same time every week are part of the expected pattern.
* api-change:``codebuild``: [``botocore``] Support access tokens for Bitbucket sources
* api-change:``iam``: [``botocore``] For CreateOpenIDConnectProvider API, the ThumbprintList parameter is no longer required.
* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive introduces workflow monitor, a new feature that enables the visualization and monitoring of your media workflows. Create signal maps of your existing workflows and monitor them by creating notification and monitoring template groups.
* api-change:``omics``: [``botocore``] This release adds support for retrieval of S3 direct access metadata on sequence stores and read sets, and adds support for SHA256up and SHA512up HealthOmics ETags.
* api-change:``pipes``: [``botocore``] LogConfiguration ARN validation fixes
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for Standard Edition 2 support in RDS Custom for Oracle.
* api-change:``s3control``: [``botocore``] Documentation updates for Amazon S3-control.


1.34.82
=======

* api-change:``cleanrooms``: [``botocore``] AWS Clean Rooms Differential Privacy is now fully available. Differential privacy protects against user-identification attempts.
* api-change:``connect``: [``botocore``] This release adds new Submit Auto Evaluation Action for Amazon Connect Rules.
* api-change:``networkmonitor``: [``botocore``] Examples were added to CloudWatch Network Monitor commands.
* api-change:``qconnect``: [``botocore``] This release adds a new QiC public API updateSession and updates an existing QiC public API createSession
* api-change:``rekognition``: [``botocore``] Added support for ContentType to content moderation detections.
* api-change:``supplychain``: [``botocore``] This release includes API SendDataIntegrationEvent for AWS Supply Chain
* api-change:``workspaces-thin-client``: [``botocore``] Adding tags field to SoftwareSet. Removing tags fields from Summary objects. Changing the list of exceptions in tagging APIs. Fixing an issue where the SDK returns empty tags in Get APIs.


1.34.81
=======

* api-change:``codebuild``: [``botocore``] Add new webhook filter types for GitHub webhooks
* api-change:``mediaconvert``: [``botocore``] This release includes support for bringing your own fonts to use for burn-in or DVB-Sub captioning workflows.
* api-change:``pinpoint``: [``botocore``] The OrchestrationSendingRoleArn has been added to the email channel and is used to send emails from campaigns or journeys.
* api-change:``rds``: [``botocore``] This release adds support for specifying the CA certificate to use for the new db instance when restoring from db snapshot, restoring from s3, restoring to point in time, and creating a db instance read replica.


1.34.80
=======

* api-change:``controlcatalog``: [``botocore``] This is the initial SDK release for AWS Control Catalog, a central catalog for AWS managed controls. This release includes 3 new APIs - ListDomains, ListObjectives, and ListCommonControls - that vend high-level data to categorize controls across the AWS platform.
* api-change:``mgn``: [``botocore``] Added USE_SOURCE as default option to LaunchConfigurationTemplate bootMode parameter.
* api-change:``networkmonitor``: [``botocore``] Updated the allowed monitorName length for CloudWatch Network Monitor.


1.34.79
=======

* api-change:``quicksight``: [``botocore``] Adding IAMIdentityCenterInstanceArn parameter to CreateAccountSubscription
* api-change:``resource-groups``: [``botocore``] Added a new QueryErrorCode RESOURCE_TYPE_NOT_SUPPORTED that is returned by the ListGroupResources operation if the group query contains unsupported resource types.
* api-change:``verifiedpermissions``: [``botocore``] Adding BatchIsAuthorizedWithToken API which supports multiple authorization requests against a PolicyStore given a bearer token.


1.34.78
=======

* api-change:``b2bi``: [``botocore``] Adding support for X12 5010 HIPAA EDI version and associated transaction sets.
* api-change:``cleanrooms``: [``botocore``] Feature: New schemaStatusDetails field to the existing Schema object that displays a status on Schema API responses to show whether a schema is queryable or not. New BatchGetSchemaAnalysisRule API to retrieve multiple schemaAnalysisRules using a single API call.
* api-change:``ec2``: [``botocore``] Amazon EC2 G6 instances powered by NVIDIA L4 Tensor Core GPUs can be used for a wide range of graphics-intensive and machine learning use cases. Gr6 instances also feature NVIDIA L4 GPUs and can be used for graphics workloads with higher memory requirements.
* api-change:``emr-containers``: [``botocore``] This release adds support for integration with EKS AccessEntry APIs to enable automatic Cluster Access for EMR on EKS.
* api-change:``ivs``: [``botocore``] API update to include an SRT ingest endpoint and passphrase for all channels.
* api-change:``verifiedpermissions``: [``botocore``] Adds GroupConfiguration field to Identity Source API's


1.34.77
=======

* api-change:``cleanroomsml``: [``botocore``] The release includes a public SDK for AWS Clean Rooms ML APIs, making them globally available to developers worldwide.
* api-change:``cloudformation``: [``botocore``] This release would return a new field - PolicyAction in cloudformation's existed DescribeChangeSetResponse, showing actions we are going to apply on the physical resource (e.g., Delete, Retain) according to the user's template
* api-change:``datazone``: [``botocore``] This release supports the feature of dataQuality to enrich asset with dataQualityResult in Amazon DataZone.
* api-change:``docdb``: [``botocore``] This release adds Global Cluster Switchover capability which enables you to change your global cluster's primary AWS Region, the region that serves writes, while preserving the replication between all regions in the global cluster.
* api-change:``groundstation``: [``botocore``] This release adds visibilityStartTime and visibilityEndTime to DescribeContact and ListContacts responses.
* api-change:``lambda``: [``botocore``] Add Ruby 3.3 (ruby3.3) support to AWS Lambda
* api-change:``medialive``: [``botocore``] Cmaf Ingest outputs are now supported in Media Live
* api-change:``medical-imaging``: [``botocore``] SearchImageSets API now supports following enhancements - Additional support for searching on UpdatedAt and SeriesInstanceUID - Support for searching existing filters between dates/times - Support for sorting the search result by Ascending/Descending - Additional parameters returned in the response
* api-change:``transfer``: [``botocore``] Add ability to specify Security Policies for SFTP Connectors


1.34.76
=======

* api-change:``ecs``: [``botocore``] Documentation only update for Amazon ECS.
* api-change:``glue``: [``botocore``] Adding View related fields to responses of read-only Table APIs.
* api-change:``ivschat``: [``botocore``] Doc-only update. Changed "Resources" to "Key Concepts" in docs and updated text.
* api-change:``rolesanywhere``: [``botocore``] This release increases the limit on the roleArns request parameter for the *Profile APIs that support it. This parameter can now take up to 250 role ARNs.
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub


1.34.75
=======

* api-change:``cloudwatch``: [``botocore``] This release adds support for CloudWatch Anomaly Detection on cross-account metrics. SingleMetricAnomalyDetector and MetricDataQuery inputs to Anomaly Detection APIs now take an optional AccountId field.
* api-change:``datazone``: [``botocore``] This release supports the feature of AI recommendations for descriptions to enrich the business data catalog in Amazon DataZone.
* api-change:``deadline``: [``botocore``] AWS Deadline Cloud is a new fully managed service that helps customers set up, deploy, and scale rendering projects in minutes, so they can improve the efficiency of their rendering pipelines and take on more projects.
* api-change:``emr``: [``botocore``] This release fixes a broken link in the documentation.
* api-change:``lightsail``: [``botocore``] This release adds support to upgrade the TLS version of the distribution.


1.34.74
=======

* api-change:``b2bi``: [``botocore``] Supporting new EDI X12 transaction sets for X12 versions 4010, 4030, and 5010.
* api-change:``codebuild``: [``botocore``] Add new fleet status code for Reserved Capacity.
* api-change:``codeconnections``: [``botocore``] Duplicating the CodeStar Connections service into the new, rebranded AWS CodeConnections service.
* api-change:``internetmonitor``: [``botocore``] This release adds support to allow customers to track cross account monitors through ListMonitor, GetMonitor, ListHealthEvents, GetHealthEvent, StartQuery APIs.
* api-change:``iotwireless``: [``botocore``] Add support for retrieving key historical and live metrics for LoRaWAN devices and gateways
* api-change:``marketplace-catalog``: [``botocore``] This release enhances the ListEntities API to support ResaleAuthorizationId filter and sort for OfferEntity in the request and the addition of a ResaleAuthorizationId field in the response of OfferSummary.
* api-change:``neptune-graph``: [``botocore``] Add the new API Start-Import-Task for Amazon Neptune Analytics.
* api-change:``sagemaker``: [``botocore``] This release adds support for custom images for the CodeEditor App on SageMaker Studio


1.34.73
=======

* api-change:``codecatalyst``: [``botocore``] This release adds support for understanding pending changes to subscriptions by including two new response parameters for the GetSubscription API for Amazon CodeCatalyst.
* api-change:``compute-optimizer``: [``botocore``] This release enables AWS Compute Optimizer to analyze and generate recommendations with a new customization preference, Memory Utilization.
* api-change:``ec2``: [``botocore``] Amazon EC2 C7gd, M7gd and R7gd metal instances with up to 3.8 TB of local NVMe-based SSD block-level storage have up to 45% improved real-time NVMe storage performance than comparable Graviton2-based instances.
* api-change:``eks``: [``botocore``] Add multiple customer error code to handle customer caused failure when managing EKS node groups
* api-change:``guardduty``: [``botocore``] Add EC2 support for GuardDuty Runtime Monitoring auto management.
* api-change:``neptune-graph``: [``botocore``] Update ImportTaskCancelled waiter to evaluate task state correctly and minor documentation changes.
* api-change:``oam``: [``botocore``] This release adds support for sharing AWS::InternetMonitor::Monitor resources.
* api-change:``quicksight``: [``botocore``] Amazon QuickSight: Adds support for setting up VPC Endpoint restrictions for accessing QuickSight Website.


1.34.72
=======

* api-change:``batch``: [``botocore``] This feature allows AWS Batch to support configuration of imagePullSecrets and allowPrivilegeEscalation for jobs running on EKS
* api-change:``bedrock-agent``: [``botocore``] This changes introduces metadata documents statistics and also updates the documentation for bedrock agent.
* api-change:``bedrock-agent-runtime``: [``botocore``] This release introduces filtering support on Retrieve and RetrieveAndGenerate APIs.
* api-change:``elasticache``: [``botocore``] Added minimum capacity to  Amazon ElastiCache Serverless. This feature allows customer to ensure minimum capacity even without current load
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager


1.34.71
=======

* api-change:``bedrock-agent-runtime``: [``botocore``] This release adds support to customize prompts sent through the RetrieveAndGenerate API in Agents for Amazon Bedrock.
* api-change:``ce``: [``botocore``] Adds support for backfill of cost allocation tags, with new StartCostAllocationTagBackfill and ListCostAllocationTagBackfillHistory API.
* api-change:``ec2``: [``botocore``] Documentation updates for Elastic Compute Cloud (EC2).
* api-change:``ecs``: [``botocore``] This is a documentation update for Amazon ECS.
* api-change:``finspace``: [``botocore``] Add new operation delete-kx-cluster-node and add status parameter to list-kx-cluster-node operation.


1.34.70
=======

* api-change:``codebuild``: [``botocore``] Supporting GitLab and GitLab Self Managed as source types in AWS CodeBuild.
* api-change:``ec2``: [``botocore``] Added support for ModifyInstanceMetadataDefaults and GetInstanceMetadataDefaults to set Instance Metadata Service account defaults
* api-change:``ecs``: [``botocore``] Documentation only update for Amazon ECS.
* api-change:``emr-containers``: [``botocore``] This release increases the number of supported job template parameters from 20 to 100.
* api-change:``globalaccelerator``: [``botocore``] AWS Global Accelerator now supports cross-account sharing for bring your own IP addresses.
* api-change:``medialive``: [``botocore``] Exposing TileMedia H265 options
* api-change:``sagemaker``: [``botocore``] Introduced support for the following new instance types on SageMaker Studio for JupyterLab and CodeEditor applications: m6i, m6id, m7i, c6i, c6id, c7i, r6i, r6id, r7i, and p5


1.34.69
=======

* api-change:``firehose``: [``botocore``] Updates Amazon Firehose documentation for message regarding Enforcing Tags IAM Policy.
* api-change:``kendra``: [``botocore``] Documentation update, March 2024. Corrects some docs for Amazon Kendra.
* api-change:``pricing``: [``botocore``] Add ResourceNotFoundException to ListPriceLists and GetPriceListFileUrl APIs
* api-change:``rolesanywhere``: [``botocore``] This release relaxes constraints on the durationSeconds request parameter for the *Profile APIs that support it. This parameter can now take on values that go up to 43200.
* api-change:``securityhub``: [``botocore``] Added new resource detail object to ASFF, including resource for LastKnownExploitAt


1.34.68
=======

* api-change:``codeartifact``: [``botocore``] This release adds Package groups to CodeArtifact so you can more conveniently configure package origin controls for multiple packages.


1.34.67
=======

* api-change:``accessanalyzer``: [``botocore``] This release adds support for policy validation and external access findings for DynamoDB tables and streams. IAM Access Analyzer helps you author functional and secure resource-based policies and identify cross-account access. Updated service API, documentation, and paginators.
* api-change:``codebuild``: [``botocore``] This release adds support for new webhook events (RELEASED and PRERELEASED) and filter types (TAG_NAME and RELEASE_NAME).
* api-change:``connect``: [``botocore``] This release updates the *InstanceStorageConfig APIs to support a new ResourceType: REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS. Use this resource type to enable streaming for real-time analysis of chat contacts and to associate a Kinesis stream where real-time analysis chat segments will be published.
* api-change:``dynamodb``: [``botocore``] This release introduces 3 new APIs ('GetResourcePolicy', 'PutResourcePolicy' and 'DeleteResourcePolicy') and modifies the existing 'CreateTable' API for the resource-based policy support. It also modifies several APIs to accept a 'TableArn' for the 'TableName' parameter.
* api-change:``managedblockchain-query``: [``botocore``] AMB Query: update GetTransaction to include transactionId as input
* api-change:``savingsplans``: [``botocore``] Introducing the Savings Plans Return feature enabling customers to return their Savings Plans within 7 days of purchase.


1.34.66
=======

* api-change:``cloudformation``: [``botocore``] Documentation update, March 2024. Corrects some formatting.
* api-change:``ec2``: [``botocore``] This release adds the new DescribeMacHosts API operation for getting information about EC2 Mac Dedicated Hosts. Users can now see the latest macOS versions that their underlying Apple Mac can support without needing to be updated.
* api-change:``finspace``: [``botocore``] Adding new attributes readWrite and onDemand to dataview models for Database Maintenance operations.
* api-change:``logs``: [``botocore``] Update LogSamples field in Anomaly model to be a list of LogEvent
* api-change:``managedblockchain-query``: [``botocore``] Introduces a new API for Amazon Managed Blockchain Query: ListFilteredTransactionEvents.


1.34.65
=======

* api-change:``cloudformation``: [``botocore``] This release supports for a new API ListStackSetAutoDeploymentTargets, which provider auto-deployment configuration as a describable resource. Customers can now view the specific combinations of regions and OUs that are being auto-deployed.
* api-change:``kms``: [``botocore``] Adds the ability to use the default policy name by omitting the policyName parameter in calls to PutKeyPolicy and GetKeyPolicy
* api-change:``mediatailor``: [``botocore``] This release adds support to allow customers to show different content within a channel depending on metadata associated with the viewer.
* api-change:``rds``: [``botocore``] This release launches the ModifyIntegration API and support for data filtering for zero-ETL Integrations.
* api-change:``s3``: [``botocore``] Fix two issues with response root node names.
* api-change:``timestream-query``: [``botocore``] Documentation updates, March 2024


1.34.64
=======

* api-change:``backup``: [``botocore``] This release introduces a boolean attribute ManagedByAWSBackupOnly as part of ListRecoveryPointsByResource api to filter the recovery points based on ownership. This attribute can be used to filter out the recovery points protected by AWSBackup.
* api-change:``codebuild``: [``botocore``] AWS CodeBuild now supports overflow behavior on Reserved Capacity.
* api-change:``connect``: [``botocore``] This release adds Hierarchy based Access Control fields to Security Profile public APIs and adds support for UserAttributeFilter to SearchUsers API.
* api-change:``ec2``: [``botocore``] Add media accelerator and neuron device information on the describe instance types API.
* api-change:``kinesisanalyticsv2``: [``botocore``] Support for Flink 1.18 in Managed Service for Apache Flink
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3.
* api-change:``sagemaker``: [``botocore``] Adds m6i, m6id, m7i, c6i, c6id, c7i, r6i r6id, r7i, p5 instance type support to Sagemaker Notebook Instances and miscellaneous wording fixes for previous Sagemaker documentation.
* api-change:``workspaces-thin-client``: [``botocore``] Removed unused parameter kmsKeyArn from UpdateDeviceRequest


1.34.63
=======

* api-change:``amplify``: [``botocore``] Documentation updates for Amplify. Identifies the APIs available only to apps created using Amplify Gen 1.
* api-change:``ec2-instance-connect``: [``botocore``] This release includes a new exception type "SerialConsoleSessionUnsupportedException" for SendSerialConsoleSSHPublicKey API.
* api-change:``elbv2``: [``botocore``] This release allows you to configure HTTP client keep-alive duration for communication between clients and Application Load Balancers.
* api-change:``fis``: [``botocore``] This release adds support for previewing target resources before running a FIS experiment. It also adds resource ARNs for actions, experiments, and experiment templates to API responses.
* api-change:``iot-roborunner``: [``botocore``] The iot-roborunner client has been removed following the deprecation of the service.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for EBCDIC collation for RDS for Db2.
* api-change:``secretsmanager``: [``botocore``] Doc only update for Secrets Manager
* api-change:``timestream-influxdb``: [``botocore``] This is the initial SDK release for Amazon Timestream for InfluxDB. Amazon Timestream for InfluxDB is a new time-series database engine that makes it easy for application developers and DevOps teams to run InfluxDB databases on AWS for near real-time time-series applications using open source APIs.
* enhancement:``urllib3``: [``botocore``] Added support for urllib3 2.2.1+ in Python 3.10+


1.34.62
=======

* api-change:``ivs-realtime``: [``botocore``] adds support for multiple new composition layout configuration options (grid, pip)
* api-change:``kinesisanalyticsv2``: [``botocore``] Support new RuntimeEnvironmentUpdate parameter within UpdateApplication API allowing callers to change the Flink version upon which their application runs.
* api-change:``s3``: [``botocore``] This release makes the default option for S3 on Outposts request signing to use the SigV4A algorithm when using AWS Common Runtime (CRT).


1.34.61
=======

* api-change:``cloudformation``: [``botocore``] CloudFormation documentation update for March, 2024
* api-change:``connect``: [``botocore``] This release increases MaxResults limit to 500 in request for SearchUsers, SearchQueues and SearchRoutingProfiles APIs of Amazon Connect.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``kafka``: [``botocore``] Added support for specifying the starting position of topic replication in MSK-Replicator.
* api-change:``ssm``: [``botocore``] March 2024 doc-only updates for Systems Manager.


1.34.60
=======

* api-change:``codestar-connections``: [``botocore``] Added a sync configuration enum to disable publishing of deployment status to source providers (PublishDeploymentStatus). Added a sync configuration enum (TriggerStackUpdateOn) to only trigger changes.
* api-change:``elasticache``: [``botocore``] Revisions to API text that are now to be carried over to SDK text, changing usages of "SFO" in code examples to "us-west-1", and some other typos.
* api-change:``mediapackagev2``: [``botocore``] This release enables customers to safely update their MediaPackage v2 channel groups, channels and origin endpoints using entity tags.


1.34.59
=======

* api-change:``batch``: [``botocore``] This release adds JobStateTimeLimitActions setting to the Job Queue API. It allows you to configure an action Batch can take for a blocking job in front of the queue after the defined period of time. The new parameter applies for ECS, EKS, and FARGATE Job Queues.
* api-change:``bedrock-agent-runtime``: [``botocore``] Documentation update for Bedrock Runtime Agent
* api-change:``cloudtrail``: [``botocore``] Added exceptions to CreateTrail, DescribeTrails, and ListImportFailures APIs.
* api-change:``codebuild``: [``botocore``] This release adds support for a new webhook event: PULL_REQUEST_CLOSED.
* api-change:``cognito-idp``: [``botocore``] Add ConcurrentModificationException to SetUserPoolMfaConfig
* api-change:``guardduty``: [``botocore``] Add RDS Provisioned and Serverless Usage types
* api-change:``transfer``: [``botocore``] Added DES_EDE3_CBC to the list of supported encryption algorithms for messages sent with an AS2 connector.


1.34.58
=======

* api-change:``appconfig``: [``botocore``] AWS AppConfig now supports dynamic parameters, which enhance the functionality of AppConfig Extensions by allowing you to provide parameter values to your Extensions at the time you deploy your configuration.
* api-change:``ec2``: [``botocore``] This release adds an optional parameter to RegisterImage and CopyImage APIs to support tagging AMIs at the time of creation.
* api-change:``grafana``: [``botocore``] Adds support for the new GrafanaToken as part of the Amazon Managed Grafana Enterprise plugins upgrade to associate your AWS account with a Grafana Labs account.
* api-change:``lambda``: [``botocore``] Documentation updates for AWS Lambda
* api-change:``payment-cryptography-data``: [``botocore``] AWS Payment Cryptography EMV Decrypt Feature  Release
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for io2 storage for Multi-AZ DB clusters
* api-change:``snowball``: [``botocore``] Doc-only update for change to EKS-Anywhere ordering.
* api-change:``wafv2``: [``botocore``] You can increase the max request body inspection size for some regional resources. The size setting is in the web ACL association config. Also, the AWSManagedRulesBotControlRuleSet EnableMachineLearning setting now takes a Boolean instead of a primitive boolean type, for languages like Java.
* api-change:``workspaces``: [``botocore``] Added note for user decoupling


1.34.57
=======

* api-change:``dynamodb``: [``botocore``] Doc only updates for DynamoDB documentation
* api-change:``imagebuilder``: [``botocore``] Add PENDING status to Lifecycle Execution resource status. Add StartTime and EndTime to ListLifecycleExecutionResource API response.
* api-change:``mwaa``: [``botocore``] Amazon MWAA adds support for Apache Airflow v2.8.1.
* api-change:``rds``: [``botocore``] Updated the input of CreateDBCluster and ModifyDBCluster to support setting CA certificates. Updated the output of DescribeDBCluster to show current CA certificate setting value.
* api-change:``redshift``: [``botocore``] Update for documentation only. Covers port ranges, definition updates for data sharing, and definition updates to cluster-snapshot documentation.
* api-change:``verifiedpermissions``: [``botocore``] Deprecating details in favor of configuration for GetIdentitySource and ListIdentitySources APIs.


1.34.56
=======

* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway
* api-change:``chatbot``: [``botocore``] Minor update to documentation.
* api-change:``organizations``: [``botocore``] This release contains an endpoint addition
* api-change:``sesv2``: [``botocore``] Adds support for providing custom headers within SendEmail and SendBulkEmail for SESv2.


1.34.55
=======

* api-change:``cloudformation``: [``botocore``] Add DetailedStatus field to DescribeStackEvents and DescribeStacks APIs
* api-change:``fsx``: [``botocore``] Added support for creating FSx for NetApp ONTAP file systems with up to 12 HA pairs, delivering up to 72 GB/s of read throughput and 12 GB/s of write throughput.
* api-change:``organizations``: [``botocore``] Documentation update for AWS Organizations


1.34.54
=======

* api-change:``accessanalyzer``: [``botocore``] Fixed a typo in description field.
* api-change:``autoscaling``: [``botocore``] With this release, Amazon EC2 Auto Scaling groups, EC2 Fleet, and Spot Fleet improve the default price protection behavior of attribute-based instance type selection of Spot Instances, to consistently select from a wide range of instance types.
* api-change:``ec2``: [``botocore``] With this release, Amazon EC2 Auto Scaling groups, EC2 Fleet, and Spot Fleet improve the default price protection behavior of attribute-based instance type selection of Spot Instances, to consistently select from a wide range of instance types.


1.34.53
=======

* api-change:``docdb-elastic``: [``botocore``] Launched Elastic Clusters Readable Secondaries, Start/Stop, Configurable Shard Instance count, Automatic Backups and Snapshot Copying
* api-change:``eks``: [``botocore``] Added support for new AL2023 AMIs to the supported AMITypes.
* api-change:``lexv2-models``: [``botocore``] This release makes AMAZON.QnAIntent generally available in Amazon Lex. This generative AI feature leverages large language models available through Amazon Bedrock to automate frequently asked questions (FAQ) experience for end-users.
* api-change:``migrationhuborchestrator``: [``botocore``] Adds new CreateTemplate, UpdateTemplate and DeleteTemplate APIs.
* api-change:``quicksight``: [``botocore``] TooltipTarget for Combo chart visuals; ColumnConfiguration limit increase to 2000; Documentation Update
* api-change:``sagemaker``: [``botocore``] Adds support for ModelDataSource in Model Packages to support unzipped models. Adds support to specify SourceUri for models which allows registration of models without mandating a container for hosting. Using SourceUri, customers can decouple the model from hosting information during registration.
* api-change:``securitylake``: [``botocore``] Add capability to update the Data Lake's MetaStoreManager Role in order to perform required data lake updates to use Iceberg table format in their data lake or update the role for any other reason.


1.34.52
=======

* api-change:``batch``: [``botocore``] This release adds Batch support for configuration of multicontainer jobs in ECS, Fargate, and EKS. This support is available for all types of jobs, including both array jobs and multi-node parallel jobs.
* api-change:``bedrock-agent-runtime``: [``botocore``] This release adds support to override search strategy performed by the Retrieve and RetrieveAndGenerate APIs for Amazon Bedrock Agents
* api-change:``ce``: [``botocore``] This release introduces the new API 'GetApproximateUsageRecords', which retrieves estimated usage records for hourly granularity or resource-level data at daily granularity.
* api-change:``ec2``: [``botocore``] This release increases the range of MaxResults for GetNetworkInsightsAccessScopeAnalysisFindings to 1,000.
* api-change:``iot``: [``botocore``] This release reduces the maximum results returned per query invocation from 500 to 100 for the SearchIndex API. This change has no implications as long as the API is invoked until the nextToken is NULL.
* api-change:``wafv2``: [``botocore``] AWS WAF now supports configurable time windows for request aggregation with rate-based rules. Customers can now select time windows of 1 minute, 2 minutes or 10 minutes, in addition to the previously supported 5 minutes.


1.34.51
=======

* api-change:``amplifyuibuilder``: [``botocore``] We have added the ability to tag resources after they are created


1.34.50
=======

* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway.
* api-change:``drs``: [``botocore``] Added volume status to DescribeSourceServer replicated volumes.
* api-change:``kafkaconnect``: [``botocore``] Adds support for tagging, with new TagResource, UntagResource and ListTagsForResource APIs to manage tags and updates to existing APIs to allow tag on create. This release also adds support for the new DeleteWorkerConfiguration API.
* api-change:``rds``: [``botocore``] This release adds support for gp3 data volumes for Multi-AZ DB Clusters.


1.34.49
=======

* api-change:``appsync``: [``botocore``] Documentation only updates for AppSync
* api-change:``qldb``: [``botocore``] Clarify possible values for KmsKeyArn and EncryptionDescription.
* api-change:``rds``: [``botocore``] Add pattern and length based validations for DBShardGroupIdentifier
* api-change:``rum``: [``botocore``] Doc-only update for new RUM metrics that were added


1.34.48
=======

* api-change:``internetmonitor``: [``botocore``] This release adds IPv4 prefixes to health events
* api-change:``kinesisvideo``: [``botocore``] Increasing NextToken parameter length restriction for List APIs from 512 to 1024.


1.34.47
=======

* api-change:``iotevents``: [``botocore``] Increase the maximum length of descriptions for Inputs, Detector Models, and Alarm Models
* api-change:``lookoutequipment``: [``botocore``] This release adds a field exposing model quality to read APIs for models. It also adds a model quality field to the API response when creating an inference scheduler.
* api-change:``medialive``: [``botocore``] MediaLive now supports the ability to restart pipelines in a running channel.
* api-change:``ssm``: [``botocore``] This release adds support for sharing Systems Manager parameters with other AWS accounts.


1.34.46
=======

* api-change:``dynamodb``: [``botocore``] Publishing quick fix for doc only update.
* api-change:``firehose``: [``botocore``] This release updates a few Firehose related APIs.
* api-change:``lambda``: [``botocore``] Add .NET 8 (dotnet8) Runtime support to AWS Lambda.


1.34.45
=======

* api-change:``amplify``: [``botocore``] This release contains API changes that enable users to configure their Amplify domains with their own custom SSL/TLS certificate.
* api-change:``chatbot``: [``botocore``] This release adds support for AWS Chatbot. You can now monitor, operate, and troubleshoot your AWS resources with interactive ChatOps using the AWS SDK.
* api-change:``config``: [``botocore``] Documentation updates for the AWS Config CLI
* api-change:``ivs``: [``botocore``] Changed description for latencyMode in Create/UpdateChannel and Channel/ChannelSummary.
* api-change:``keyspaces``: [``botocore``] Documentation updates for Amazon Keyspaces
* api-change:``mediatailor``: [``botocore``] MediaTailor: marking #AdBreak.OffsetMillis as required.


1.34.44
=======

* api-change:``connectparticipant``: [``botocore``] Doc only update to GetTranscript API reference guide to inform users about presence of events in the chat transcript.
* api-change:``emr``: [``botocore``] adds fine grained control over Unhealthy Node Replacement to Amazon ElasticMapReduce
* api-change:``firehose``: [``botocore``] This release adds support for Data Message Extraction for decompressed CloudWatch logs, and to use a custom file extension or time zone for S3 destinations.
* api-change:``lambda``: [``botocore``] Documentation-only updates for Lambda to clarify a number of existing actions and properties.
* api-change:``rds``: [``botocore``] Doc only update for a valid option in DB parameter group
* api-change:``sns``: [``botocore``] This release marks phone numbers as sensitive inputs.


1.34.43
=======

* api-change:``artifact``: [``botocore``] This is the initial SDK release for AWS Artifact. AWS Artifact provides on-demand access to compliance and third-party compliance reports. This release includes access to List and Get reports, along with their metadata. This release also includes access to AWS Artifact notifications settings.
* api-change:``codepipeline``: [``botocore``] Add ability to override timeout on action level.
* api-change:``detective``: [``botocore``] Doc only updates for content enhancement
* api-change:``guardduty``: [``botocore``] Marked fields IpAddressV4, PrivateIpAddress, Email as Sensitive.
* api-change:``healthlake``: [``botocore``] This release adds a new response parameter, JobProgressReport, to the DescribeFHIRImportJob and ListFHIRImportJobs API operation. JobProgressReport provides details on the progress of the import job on the server.
* api-change:``opensearch``: [``botocore``] Adds additional supported instance types.
* api-change:``polly``: [``botocore``] Amazon Polly adds 1 new voice - Burcu (tr-TR)
* api-change:``sagemaker``: [``botocore``] This release adds a new API UpdateClusterSoftware for SageMaker HyperPod. This API allows users to patch HyperPod clusters with latest platform softwares.
* api-change:``secretsmanager``: [``botocore``] Doc only update for Secrets Manager
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.42
=======

* api-change:``controltower``: [``botocore``] Adds support for new Baseline and EnabledBaseline APIs for automating multi-account governance.
* api-change:``lookoutequipment``: [``botocore``] This feature allows customers to see pointwise model diagnostics results for their models.
* api-change:``qbusiness``: [``botocore``] This release adds the metadata-boosting feature, which allows customers to easily fine-tune the underlying ranking of retrieved RAG passages in order to optimize Q&A answer relevance. It also adds new feedback reasons for the PutFeedback API.


1.34.41
=======

* bugfix:ContainerProvider: [``botocore``] Properly refreshes token from file from EKS in ContainerProvider
* api-change:``lightsail``: [``botocore``] This release adds support to upgrade the major version of a database.
* api-change:``marketplace-catalog``: [``botocore``] AWS Marketplace Catalog API now supports setting intent on requests
* api-change:``resource-explorer-2``: [``botocore``] Resource Explorer now uses newly supported IPv4 'amazonaws.com' endpoints by default.
* api-change:``securitylake``: [``botocore``] Documentation updates for Security Lake
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.40
=======

* api-change:``appsync``: [``botocore``] Adds support for new options on GraphqlAPIs, Resolvers and  Data Sources for emitting Amazon CloudWatch metrics for enhanced monitoring of AppSync APIs.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``neptune-graph``: [``botocore``] Adding a new option "parameters" for data plane api ExecuteQuery to support running parameterized query via SDK.
* api-change:``route53domains``: [``botocore``] This release adds bill contact support for RegisterDomain, TransferDomain, UpdateDomainContact and GetDomainDetail API.


1.34.39
=======

* api-change:``amp``: [``botocore``] Overall documentation updates.
* api-change:``batch``: [``botocore``] This feature allows Batch to support configuration of repository credentials for jobs running on ECS
* api-change:``braket``: [``botocore``] Creating a job will result in DeviceOfflineException when using an offline device, and DeviceRetiredException when using a retired device.
* api-change:``cost-optimization-hub``: [``botocore``] Adding includeMemberAccounts field to the response of ListEnrollmentStatuses API.
* api-change:``ecs``: [``botocore``] Documentation only update for Amazon ECS.
* api-change:``iot``: [``botocore``] This release allows AWS IoT Core users to enable Online Certificate Status Protocol (OCSP) Stapling for TLS X.509 Server Certificates when creating and updating AWS IoT Domain Configurations with Custom Domain.
* api-change:``pricing``: [``botocore``] Add Throttling Exception to all APIs.


1.34.38
=======

* api-change:``codepipeline``: [``botocore``] Add ability to execute pipelines with new parallel & queued execution modes and add support for triggers with filtering on branches and file paths.
* api-change:``quicksight``: [``botocore``] General Interactions for Visuals; Waterfall Chart Color Configuration; Documentation Update
* api-change:``workspaces``: [``botocore``] This release introduces User-Decoupling feature. This feature allows Workspaces Core customers to provision workspaces without providing users. CreateWorkspaces and DescribeWorkspaces APIs will now take a new optional parameter "WorkspaceName".


1.34.37
=======

* api-change:``datasync``: [``botocore``] AWS DataSync now supports manifests for specifying files or objects to transfer.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``redshift``: [``botocore``] LisRecommendations API to fetch Amazon Redshift Advisor recommendations.


1.34.36
=======

* api-change:``appsync``: [``botocore``] Support for environment variables in AppSync GraphQL APIs
* api-change:``ecs``: [``botocore``] This release is a documentation only update to address customer issues.
* api-change:``es``: [``botocore``] This release adds clear visibility to the customers on the changes that they make on the domain.
* api-change:``logs``: [``botocore``] This release adds a new field, logGroupArn, to the response of the logs:DescribeLogGroups action.
* api-change:``opensearch``: [``botocore``] This release adds clear visibility to the customers on the changes that they make on the domain.
* api-change:``wafv2``: [``botocore``] You can now delete an API key that you've created for use with your CAPTCHA JavaScript integration API.


1.34.35
=======

* api-change:``glue``: [``botocore``] Introduce Catalog Encryption Role within Glue Data Catalog Settings. Introduce SASL/PLAIN as an authentication method for Glue Kafka connections
* api-change:``workspaces``: [``botocore``] Added definitions of various WorkSpace states


1.34.34
=======

* api-change:``dynamodb``: [``botocore``] Any number of users can execute up to 50 concurrent restores (any type of restore) in a given account.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Canvas adds GenerativeAiSettings support for CanvasAppSettings.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.33
=======

* api-change:``cognito-idp``: [``botocore``] Added CreateIdentityProvider and UpdateIdentityProvider details for new SAML IdP features
* api-change:``ivs``: [``botocore``] This release introduces a new resource Playback Restriction Policy which can be used to geo-restrict or domain-restrict channel stream playback when associated with a channel.  New APIs to support this resource were introduced in the form of Create/Delete/Get/Update/List.
* api-change:``managedblockchain-query``: [``botocore``] This release adds support for transactions that have not reached finality. It also removes support for the status property from the response of the GetTransaction operation. You can use the confirmationStatus and executionStatus properties to determine the status of the transaction.
* api-change:``mediaconvert``: [``botocore``] This release includes support for broadcast-mixed audio description tracks.
* api-change:``neptune-graph``: [``botocore``] Adding new APIs in SDK for Amazon Neptune Analytics. These APIs include operations to execute, cancel, list queries and get the graph summary.


1.34.32
=======

* api-change:``cloudformation``: [``botocore``] CloudFormation IaC generator allows you to scan existing resources in your account and select resources to generate a template for a new or existing CloudFormation stack.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``glue``: [``botocore``] Update page size limits for GetJobRuns and GetTriggers APIs.
* api-change:``ssm``: [``botocore``] This release adds an optional Duration parameter to StateManager Associations. This allows customers to specify how long an apply-only-on-cron association execution should run. Once the specified Duration is out all the ongoing cancellable commands or automations are cancelled.


1.34.31
=======

* api-change:``datazone``: [``botocore``] Add new skipDeletionCheck to DeleteDomain. Add new skipDeletionCheck to DeleteProject which also automatically deletes dependent objects
* api-change:``route53``: [``botocore``] Update the SDKs for text changes in the APIs.


1.34.30
=======

* api-change:``autoscaling``: [``botocore``] EC2 Auto Scaling customers who use attribute based instance-type selection can now intuitively define their Spot instances price protection limit as a percentage of the lowest priced On-Demand instance type.
* api-change:``comprehend``: [``botocore``] Comprehend PII analysis now supports Spanish input documents.
* api-change:``ec2``: [``botocore``] EC2 Fleet customers who use attribute based instance-type selection can now intuitively define their Spot instances price protection limit as a percentage of the lowest priced On-Demand instance type.
* api-change:``mwaa``: [``botocore``] This release adds MAINTENANCE environment status for Amazon MWAA environments.
* api-change:``rds``: [``botocore``] Introduced support for the InsufficientDBInstanceCapacityFault error in the RDS RestoreDBClusterFromSnapshot and RestoreDBClusterToPointInTime API methods. This provides enhanced error handling, ensuring a more robust experience.
* api-change:``snowball``: [``botocore``] Modified description of createaddress to include direction to add path when providing a JSON file.


1.34.29
=======

* api-change:``connect``: [``botocore``] Update list and string length limits for predefined attributes.
* api-change:``inspector2``: [``botocore``] This release adds ECR container image scanning based on their lastRecordedPullTime.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now provides an API to programmatically delete tuning jobs.


1.34.28
=======

* api-change:``acm-pca``: [``botocore``] AWS Private CA now supports an option to omit the CDP extension from issued certificates, when CRL revocation is enabled.
* api-change:``lightsail``: [``botocore``] This release adds support for IPv6-only instance plans.


1.34.27
=======

* api-change:``ec2``: [``botocore``] Introduced a new clientToken request parameter on CreateNetworkAcl and CreateRouteTable APIs. The clientToken parameter allows idempotent operations on the APIs.
* api-change:``ecs``: [``botocore``] Documentation updates for Amazon ECS.
* api-change:``outposts``: [``botocore``] DeviceSerialNumber parameter is now optional in StartConnection API
* api-change:``rds``: [``botocore``] This release adds support for Aurora Limitless Database.
* api-change:``storagegateway``: [``botocore``] Add DeprecationDate and SoftwareVersion to response of ListGateways.


1.34.26
=======

* api-change:``inspector2``: [``botocore``] This release adds support for CIS scans on EC2 instances.


1.34.25
=======

* enhancement:documentation: [``botocore``] Updates the GitHub issue creation link in our README


1.34.24
=======

* api-change:``appconfigdata``: [``botocore``] Fix FIPS Endpoints in aws-us-gov.
* api-change:``cloud9``: [``botocore``] Doc-only update around removing AL1 from list of available AMIs for Cloud9
* api-change:``cloudfront-keyvaluestore``: [``botocore``] This release improves upon the DescribeKeyValueStore API by returning two additional fields, Status of the KeyValueStore and the FailureReason in case of failures during creation of KeyValueStore.
* api-change:``connectcases``: [``botocore``] This release adds the ability to view audit history on a case and introduces a new parameter, performedBy, for CreateCase and UpdateCase API's.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``ecs``: [``botocore``] This release adds support for Transport Layer Security (TLS) and Configurable Timeout to ECS Service Connect. TLS facilitates privacy and data security for inter-service communications, while Configurable Timeout allows customized per-request timeout and idle timeout for Service Connect services.
* api-change:``finspace``: [``botocore``] Allow customer to set zip default through command line arguments.
* api-change:``organizations``: [``botocore``] Doc only update for quota increase change
* api-change:``rds``: [``botocore``] Introduced support for the InsufficientDBInstanceCapacityFault error in the RDS CreateDBCluster API method. This provides enhanced error handling, ensuring a more robust experience when creating database clusters with insufficient instance capacity.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.23
=======

* api-change:``athena``: [``botocore``] Introducing new NotebookS3LocationUri parameter to Athena ImportNotebook API. Payload is no longer required and either Payload or NotebookS3LocationUri needs to be provided (not both) for a successful ImportNotebook API call. If both are provided, an InvalidRequestException will be thrown.
* api-change:``codebuild``: [``botocore``] Release CodeBuild Reserved Capacity feature
* api-change:``dynamodb``: [``botocore``] This release adds support for including ApproximateCreationDateTimePrecision configurations in EnableKinesisStreamingDestination API, adds the same as an optional field in the response of DescribeKinesisStreamingDestination, and adds support for a new UpdateKinesisStreamingDestination API.
* api-change:``qconnect``: [``botocore``] Increased Quick Response name max length to 100


1.34.22
=======

* api-change:``b2bi``: [``botocore``] Increasing TestMapping inputFileContent file size limit to 5MB and adding file size limit 250KB for TestParsing input file. This release also includes exposing InternalServerException for Tag APIs.
* api-change:``cloudtrail``: [``botocore``] This release adds a new API ListInsightsMetricData to retrieve metric data from CloudTrail Insights.
* api-change:``connect``: [``botocore``] GetMetricDataV2 now supports 3 groupings
* api-change:``drs``: [``botocore``] Removed invalid and unnecessary default values.
* api-change:``firehose``: [``botocore``] Allow support for Snowflake as a Kinesis Data Firehose delivery destination.
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Increase BatchGetRecord limits from 10 items to 100 items


1.34.21
=======

* api-change:``dynamodb``: [``botocore``] Updating note for enabling streams for UpdateTable.
* api-change:``keyspaces``: [``botocore``] This release adds support for Multi-Region Replication with provisioned tables, and Keyspaces auto scaling APIs


1.34.20
=======

* api-change:``iot``: [``botocore``] Revert release of LogTargetTypes
* api-change:``iotfleetwise``: [``botocore``] Updated APIs: SignalNodeType query parameter has been added to ListSignalCatalogNodesRequest and ListVehiclesResponse has been extended with attributes field.
* api-change:``macie2``: [``botocore``] This release adds support for analyzing Amazon S3 objects that are encrypted using dual-layer server-side encryption with AWS KMS keys (DSSE-KMS). It also adds support for reporting DSSE-KMS details in statistics and metadata about encryption settings for S3 buckets and objects.
* api-change:``payment-cryptography``: [``botocore``] Provide an additional option for key exchange using RSA wrap/unwrap in addition to tr-34/tr-31 in ImportKey and ExportKey operations. Added new key usage (type) TR31_M1_ISO_9797_1_MAC_KEY, for use with Generate/VerifyMac dataplane operations  with ISO9797 Algorithm 1 MAC calculations.
* api-change:``personalize-runtime``: [``botocore``] Documentation updates for Amazon Personalize
* api-change:``personalize``: [``botocore``] Documentation updates for Amazon Personalize.
* api-change:``rekognition``: [``botocore``] This release adds ContentType and TaxonomyLevel attributes to DetectModerationLabels and GetMediaAnalysisJob API responses.
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub


1.34.19
=======

* api-change:``sagemaker``: [``botocore``] This release will have ValidationException thrown if certain invalid app types are provided. The release will also throw ValidationException if more than 10 account ids are provided in VpcOnlyTrustedAccounts.


1.34.18
=======

* api-change:``connect``: [``botocore``] Supervisor Barge for Chat is now supported through the MonitorContact API.
* api-change:``connectparticipant``: [``botocore``] Introduce new Supervisor participant role
* api-change:``location``: [``botocore``] Location SDK documentation update. Added missing fonts to the MapConfiguration data type. Updated note for the SubMunicipality property in the place data type.
* api-change:``mwaa``: [``botocore``] This Amazon MWAA feature release includes new fields in CreateWebLoginToken response model. The new fields IamIdentity and AirflowIdentity will let you match identifications, as the Airflow identity length is currently hashed to 64 characters.
* api-change:``s3control``: [``botocore``] S3 On Outposts team adds dualstack endpoints support for S3Control and S3Outposts API calls.
* api-change:``supplychain``: [``botocore``] This release includes APIs CreateBillOfMaterialsImportJob and GetBillOfMaterialsImportJob.
* api-change:``transfer``: [``botocore``] AWS Transfer Family now supports static IP addresses for SFTP & AS2 connectors and for async MDNs on AS2 servers.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.17
=======

* api-change:``ec2``: [``botocore``] This release adds support for adding an ElasticBlockStorage volume configurations in ECS RunTask/StartTask/CreateService/UpdateService APIs. The configuration allows for attaching EBS volumes to ECS Tasks.
* api-change:``ecs``: [``botocore``] This release adds support for adding an ElasticBlockStorage volume configurations in ECS RunTask/StartTask/CreateService/UpdateService APIs. The configuration allows for attaching EBS volumes to ECS Tasks.
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``iot``: [``botocore``] Add ConflictException to Update APIs of AWS IoT Software Package Catalog
* api-change:``iotfleetwise``: [``botocore``] The following dataTypes have been removed: CUSTOMER_DECODED_INTERFACE in NetworkInterfaceType; CUSTOMER_DECODED_SIGNAL_INFO_IS_NULL in SignalDecoderFailureReason; CUSTOMER_DECODED_SIGNAL_NETWORK_INTERFACE_INFO_IS_NULL in NetworkInterfaceFailureReason; CUSTOMER_DECODED_SIGNAL in SignalDecoderType
* api-change:``secretsmanager``: [``botocore``] Doc only update for Secrets Manager
* api-change:``workspaces``: [``botocore``] Added AWS Workspaces RebootWorkspaces API - Extended Reboot documentation update


1.34.16
=======

* api-change:``connectcampaigns``: [``botocore``] Minor pattern updates for Campaign and Dial Request API fields.
* api-change:``location``: [``botocore``] This release adds API support for custom layers for the maps service APIs: CreateMap, UpdateMap, DescribeMap.
* api-change:``logs``: [``botocore``] Add support for account level subscription filter policies to PutAccountPolicy, DescribeAccountPolicies, and DeleteAccountPolicy APIs. Additionally, PutAccountPolicy has been modified with new optional "selectionCriteria" parameter for resource selection.
* api-change:``qconnect``: [``botocore``] QueryAssistant and GetRecommendations will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024 you will need to create a new Assistant in the Connect console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.
* api-change:``redshift-serverless``: [``botocore``] Updates to ConfigParameter for RSS workgroup, removal of use_fips_ssl
* api-change:``route53``: [``botocore``] Route53 now supports geoproximity routing in AWS regions
* api-change:``wisdom``: [``botocore``] QueryAssistant and GetRecommendations will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024 you will need to create a new Assistant in the Connect console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.


1.34.15
=======

* api-change:``codebuild``: [``botocore``] Aws CodeBuild now supports new compute type BUILD_GENERAL1_XLARGE
* api-change:``ec2``: [``botocore``] Amazon EC2 R7iz bare metal instances are powered by custom 4th generation Intel Xeon Scalable processors.
* api-change:``route53resolver``: [``botocore``] This release adds support for query type configuration on firewall rules that enables customers for granular action (ALLOW, ALERT, BLOCK) by DNS query type.


1.34.14
=======

* api-change:``connect``: [``botocore``] Minor trait updates for User APIs
* api-change:``kms``: [``botocore``] Documentation updates for AWS Key Management Service (KMS).
* api-change:``redshift-serverless``: [``botocore``] use_fips_ssl and require_ssl parameter support for Workgroup, UpdateWorkgroup, and CreateWorkgroup


1.34.13
=======

* api-change:``config``: [``botocore``] Updated ResourceType enum with new resource types onboarded by AWS Config in November and December 2023.
* api-change:``docdb``: [``botocore``] Adding PerformanceInsightsEnabled and PerformanceInsightsKMSKeyId fields to DescribeDBInstances Response.
* api-change:``ecs``: [``botocore``] This release adds support for managed instance draining which facilitates graceful termination of Amazon ECS instances.
* api-change:``es``: [``botocore``] This release adds support for new or existing Amazon OpenSearch domains to enable TLS 1.3 or TLS 1.2 with perfect forward secrecy cipher suites for domain endpoints.
* api-change:``lightsail``: [``botocore``] This release adds support to set up an HTTPS endpoint on an instance.
* api-change:``opensearch``: [``botocore``] This release adds support for new or existing Amazon OpenSearch domains to enable TLS 1.3 or TLS 1.2 with perfect forward secrecy cipher suites for domain endpoints.
* api-change:``sagemaker``: [``botocore``] Adding support for provisioned throughput mode for SageMaker Feature Groups
* api-change:``servicecatalog``: [``botocore``] Added Idempotency token support to Service Catalog  AssociateServiceActionWithProvisioningArtifact, DisassociateServiceActionFromProvisioningArtifact, DeleteServiceAction API
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.12
=======

* api-change:``connect``: [``botocore``] Amazon Connect, Contact Lens Evaluation API increase evaluation notes max length to 3072.
* api-change:``mediaconvert``: [``botocore``] This release includes video engine updates including HEVC improvements, support for ingesting VP9 encoded video in MP4 containers, and support for user-specified 3D LUTs.


1.34.11
=======

* api-change:``apprunner``: [``botocore``] AWS App Runner adds Python 3.11 and Node.js 18 runtimes.
* api-change:``location``: [``botocore``] This release introduces a new parameter to bypasses an API key's expiry conditions and delete the key.
* api-change:``quicksight``: [``botocore``] Add LinkEntityArn support for different partitions; Add UnsupportedUserEditionException in UpdateDashboardLinks API; Add support for New Reader Experience Topics


1.34.10
=======

* api-change:``codestar-connections``: [``botocore``] New integration with the GitLab self-managed provider type.
* api-change:``kinesis-video-archived-media``: [``botocore``] NoDataRetentionException thrown when GetImages requested for a Stream that does not retain data (that is, has a DataRetentionInHours of 0).
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Studio now supports Docker access from within app container


1.34.9
======

* api-change:``emr``: [``botocore``] Update emr client to latest version


1.34.8
======

* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.7
======

* api-change:``bedrock-agent``: [``botocore``] Adding Claude 2.1 support to Bedrock Agents
* api-change:``glue``: [``botocore``] This release adds additional configurations for Query Session Context on the following APIs: GetUnfilteredTableMetadata, GetUnfilteredPartitionMetadata, GetUnfilteredPartitionsMetadata.
* api-change:``lakeformation``: [``botocore``] This release adds additional configurations on GetTemporaryGlueTableCredentials for Query Session Context.
* api-change:``mediaconnect``: [``botocore``] This release adds the DescribeSourceMetadata API. This API can be used to view the stream information of the flow's source.
* api-change:``networkmonitor``: [``botocore``] CloudWatch Network Monitor is a new service within CloudWatch that will help network administrators and operators continuously monitor network performance metrics such as round-trip-time and packet loss between their AWS-hosted applications and their on-premises locations.
* api-change:``omics``: [``botocore``] Provides minor corrections and an updated description of APIs.
* api-change:``secretsmanager``: [``botocore``] Update endpoint rules and examples.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.6
======

* enhancement:AWSCRT: [``botocore``] Update awscrt version to 0.19.19
* api-change:``amp``: [``botocore``] This release updates Amazon Managed Service for Prometheus APIs to support customer managed KMS keys.
* api-change:``appintegrations``: [``botocore``] The Amazon AppIntegrations service adds DeleteApplication API for deleting applications, and updates APIs to support third party applications reacting to workspace events and make data requests to Amazon Connect for agent and contact events.
* api-change:``bedrock-agent``: [``botocore``] This release introduces Amazon Aurora as a vector store on Knowledge Bases for Amazon Bedrock
* api-change:``codecommit``: [``botocore``] AWS CodeCommit now supports customer managed keys from AWS Key Management Service. UpdateRepositoryEncryptionKey is added for updating the key configuration. CreateRepository, GetRepository, BatchGetRepositories are updated with new input or output parameters.
* api-change:``connect``: [``botocore``] Adds APIs to manage User Proficiencies and Predefined Attributes. Enhances StartOutboundVoiceContact API input. Introduces SearchContacts API. Enhances DescribeContact API. Adds an API to update Routing Attributes in QueuePriority and QueueTimeAdjustmentSeconds.
* api-change:``medialive``: [``botocore``] MediaLive now supports the ability to configure the audio that an AWS Elemental Link UHD device produces, when the device is configured as the source for a flow in AWS Elemental MediaConnect.
* api-change:``neptune-graph``: [``botocore``] Adds Waiters for successful creation and deletion of Graph, Graph Snapshot, Import Task and Private Endpoints for Neptune Analytics
* api-change:``rds-data``: [``botocore``] This release adds support for using RDS Data API with Aurora PostgreSQL Serverless v2 and provisioned DB clusters.
* api-change:``rds``: [``botocore``] This release adds support for using RDS Data API with Aurora PostgreSQL Serverless v2 and provisioned DB clusters.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Training now provides model training container access for debugging purposes. Amazon SageMaker Search now provides the ability to use visibility conditions to limit resource access to a single domain or multiple domains.


1.34.5
======

* api-change:``appstream``: [``botocore``] This release introduces configurable clipboard, allowing admins to specify the maximum length of text that can be copied by the users from their device to the remote session and vice-versa.
* api-change:``eks``: [``botocore``] Add support for cluster insights, new EKS capability that surfaces potentially upgrade impacting issues.
* api-change:``guardduty``: [``botocore``] This release 1) introduces a new API: GetOrganizationStatistics , and 2) adds a new UsageStatisticType TOP_ACCOUNTS_BY_FEATURE for GetUsageStatistics API
* api-change:``managedblockchain-query``: [``botocore``] Adding Confirmation Status and Execution Status to GetTransaction Response.
* api-change:``mediatailor``: [``botocore``] Adds the ability to configure time shifting on MediaTailor channels using the TimeShiftConfiguration field
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Canada West (Calgary) Region (ca-west-1) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.4
======

* api-change:``appsync``: [``botocore``] This release adds additional configurations on GraphQL APIs for limits on query depth, resolver count, and introspection
* api-change:``chime-sdk-meetings``: [``botocore``] Add meeting features to specify a maximum camera resolution, a maximum content sharing resolution, and a maximum number of attendees for a given meeting.
* api-change:``ec2``: [``botocore``] Provision BYOIPv4 address ranges and advertise them by specifying the network border groups option in Los Angeles, Phoenix and Dallas AWS Local Zones.
* api-change:``fsx``: [``botocore``] Added support for FSx for OpenZFS on-demand data replication across AWS accounts and/or regions.Added the IncludeShared attribute for DescribeSnapshots.Added the CopyStrategy attribute for OpenZFSVolumeConfiguration.
* api-change:``marketplace-catalog``: [``botocore``] AWS Marketplace now supports a new API, BatchDescribeEntities, which returns metadata and content for multiple entities.
* api-change:``rds``: [``botocore``] RDS - The release adds two new APIs: DescribeDBRecommendations and ModifyDBRecommendation


1.34.3
======

* api-change:``cognito-idp``: [``botocore``] Amazon Cognito now supports trigger versions that define the fields in the request sent to pre token generation Lambda triggers.
* api-change:``eks``: [``botocore``] Add support for EKS Cluster Access Management.
* api-change:``quicksight``: [``botocore``] A docs-only release to add missing entities to the API reference.
* api-change:``route53resolver``: [``botocore``] Add DOH protocols in resolver endpoints.


1.34.2
======

* api-change:``cloud9``: [``botocore``] Updated Cloud9 API documentation for AL2023 release
* api-change:``connect``: [``botocore``] Adds relatedContactId field to StartOutboundVoiceContact API input. Introduces PauseContact API and ResumeContact API for Task contacts. Adds pause duration, number of pauses, timestamps for last paused and resumed events to DescribeContact API response. Adds new Rule type and new Rule action.
* api-change:``connectcases``: [``botocore``] Increase number of fields that can be included in CaseEventIncludedData from 50 to 200
* api-change:``kms``: [``botocore``] Documentation updates for AWS Key Management Service
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation by adding code examples
* api-change:``sagemaker``: [``botocore``] This release 1) introduces a new API: DeleteCompilationJob , and 2) adds InfraCheckConfig for Create/Describe training job API


1.34.1
======

* api-change:``appstream``: [``botocore``] This release includes support for images of Windows Server 2022 platform.
* api-change:``b2bi``: [``botocore``] Documentation updates for AWS B2B Data Interchange
* api-change:``billingconductor``: [``botocore``] Billing Conductor is releasing a new API, GetBillingGroupCostReport, which provides the ability to retrieve/view the Billing Group Cost Report broken down by attributes for a specific billing group.
* api-change:``connect``: [``botocore``] This release adds support for more granular billing using tags (key:value pairs)
* api-change:``controltower``: [``botocore``] Documentation updates for AWS Control Tower.
* api-change:``firehose``: [``botocore``] This release, 1) adds configurable buffering hints for the Splunk destination, and 2) reduces the minimum configurable buffering interval for supported destinations
* api-change:``gamelift``: [``botocore``] Amazon GameLift adds the ability to add and update the game properties of active game sessions.
* api-change:``iot``: [``botocore``] This release adds the ability to self-manage certificate signing in AWS IoT Core fleet provisioning using the new certificate provider resource.
* api-change:``neptune-graph``: [``botocore``] This is the initial SDK release for Amazon Neptune Analytics
* api-change:``opensearch``: [``botocore``] Updating documentation for Amazon OpenSearch Service support for new zero-ETL integration with Amazon S3.
* api-change:``quicksight``: [``botocore``] Update Dashboard Links support; SingleAxisOptions support; Scatterplot Query limit support.
* api-change:``workspaces``: [``botocore``] Updated note to ensure customers understand running modes.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.34.0
======

* feature:Python: End of support for Python 3.7
* feature:Python: [``botocore``] End of support for Python 3.7
* api-change:``drs``: [``botocore``] Adding AgentVersion to SourceServer and RecoveryInstance structures


1.33.13
=======

* api-change:``imagebuilder``: [``botocore``] This release adds the Image Workflows feature to give more flexibility and control over the image building and testing process.
* api-change:``location``: [``botocore``] This release 1)  adds sub-municipality field in Places API for searching and getting places information, and 2) allows optimizing route calculation based on expected arrival time.
* api-change:``logs``: [``botocore``] This release introduces the StartLiveTail API to tail ingested logs in near real time.


1.33.12
=======

* api-change:``neptune``: [``botocore``] This release adds a new parameter configuration setting to the Neptune cluster related APIs that can be leveraged to switch between the underlying supported storage modes.
* api-change:``pinpoint``: [``botocore``] This release includes Amazon Pinpoint API documentation updates pertaining to campaign message sending rate limits.
* api-change:``securityhub``: [``botocore``] Added new resource detail objects to ASFF, including resources for AwsDynamoDbTable, AwsEc2ClientVpnEndpoint, AwsMskCluster, AwsS3AccessPoint, AwsS3Bucket
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.33.11
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``ec2``: [``botocore``] M2 Mac instances are built on Apple M2 Mac mini computers. I4i instances are powered by 3rd generation Intel Xeon Scalable processors. C7i compute optimized, M7i general purpose and R7i memory optimized instances are powered by custom 4th Generation Intel Xeon Scalable processors.
* api-change:``finspace``: [``botocore``] Releasing Scaling Group, Dataview, and Volume APIs


1.33.10
=======

* api-change:``codedeploy``: [``botocore``] This release adds support for two new CodeDeploy features: 1) zonal deployments for Amazon EC2 in-place deployments, 2) deployments triggered by Auto Scaling group termination lifecycle hook events.


1.33.9
======

* api-change:``backup``: [``botocore``] AWS Backup - Features: Add VaultType to the output of DescribeRecoveryPoint, ListRecoveryPointByBackupVault API and add ResourceType to the input of ListRestoreJobs API
* api-change:``comprehend``: [``botocore``] Documentation updates for Trust and Safety features.
* api-change:``connect``: [``botocore``] Releasing Tagging Support for Instance Management APIS
* api-change:``ec2``: [``botocore``] Releasing the new cpuManufacturer attribute within the DescribeInstanceTypes API response which notifies our customers with information on who the Manufacturer is for the processor attached to the instance, for example: Intel.
* api-change:``payment-cryptography``: [``botocore``] AWS Payment Cryptography IPEK feature release


1.33.8
======

* api-change:``athena``: [``botocore``] Adding IdentityCenter enabled request for interactive query
* api-change:``cleanroomsml``: [``botocore``] Updated service title from cleanroomsml to CleanRoomsML.
* api-change:``cloudformation``: [``botocore``] Documentation update, December 2023
* api-change:``ec2``: [``botocore``] Adds A10G, T4G, and H100 as accelerator name options and Habana as an accelerator manufacturer option for attribute based selection


1.33.7
======

* api-change:``billingconductor``: [``botocore``] This release adds the ability to specify a linked account of the billing group for the custom line item resource.
* api-change:``braket``: [``botocore``] This release enhances service support to create quantum tasks and hybrid jobs associated with Braket Direct Reservations.
* api-change:``cloud9``: [``botocore``] This release adds the requirement to include the imageId parameter in the CreateEnvironmentEC2 API call.
* api-change:``cloudformation``: [``botocore``] Including UPDATE_* states as a success status for CreateStack waiter.
* api-change:``finspace``: [``botocore``] Release General Purpose type clusters
* api-change:``medialive``: [``botocore``] Adds support for custom color correction on channels using 3D LUT files.
* api-change:``servicecatalog-appregistry``: [``botocore``] Documentation-only updates for Dawn
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.33.6
======

* api-change:``qconnect``: [``botocore``] This release adds the PutFeedback API and allows providing feedback against the specified assistant for the specified target.
* api-change:``rbin``: [``botocore``] Added resource identifier in the output and updated error handling.
* api-change:``verifiedpermissions``: [``botocore``] Adds description field to PolicyStore API's and namespaces field to GetSchema.


1.33.5
======

* api-change:``arc-zonal-shift``: [``botocore``] This release adds a new capability, zonal autoshift. You can configure zonal autoshift so that AWS shifts traffic for a resource away from an Availability Zone, on your behalf, when AWS determines that there is an issue that could potentially affect customers in the Availability Zone.
* api-change:``glue``: [``botocore``] Adds observation and analyzer support to the GetDataQualityResult and BatchGetDataQualityResult APIs.
* api-change:``sagemaker``: [``botocore``] This release adds support for 1/ Code Editor, based on Code-OSS, Visual Studio Code Open Source, a new fully managed IDE option in SageMaker Studio  2/ JupyterLab, a new fully managed JupyterLab IDE experience in SageMaker Studio


1.33.4
======

* bugfix:``s3transfer``: Raise floor for ``s3transfer`` to 0.8.2 to avoid any conflicts with the awscrt
* api-change:``marketplace-agreement``: [``botocore``] The AWS Marketplace Agreement Service provides an API interface that helps AWS Marketplace sellers manage their agreements, including listing, filtering, and viewing details about their agreements.
* api-change:``marketplace-catalog``: [``botocore``] This release enhances the ListEntities API to support new entity type-specific strongly typed filters in the request and entity type-specific strongly typed summaries in the response.
* api-change:``marketplace-deployment``: [``botocore``] AWS Marketplace Deployment is a new service that provides essential features that facilitate the deployment of software, data, and services procured through AWS Marketplace.
* api-change:``redshift-serverless``: [``botocore``] This release adds the following support for Amazon Redshift Serverless: 1) cross-account cross-VPCs, 2) copying snapshots across Regions, 3) scheduling snapshot creation, and 4) restoring tables from a recovery point.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.33.3
======

* api-change:``application-autoscaling``: [``botocore``] Amazon SageMaker customers can now use Application Auto Scaling to automatically scale the number of Inference Component copies across an endpoint to meet the varying demand of their workloads.
* api-change:``cleanrooms``: [``botocore``] AWS Clean Rooms now provides differential privacy to protect against user-identification attempts and machine learning modeling to allow two parties to identify similar users in their data.
* api-change:``cleanroomsml``: [``botocore``] Public Preview SDK release of AWS Clean Rooms ML APIs
* api-change:``opensearch``: [``botocore``] Launching Amazon OpenSearch Service support for new zero-ETL integration with Amazon S3. Customers can now manage their direct query data sources to Amazon S3 programatically
* api-change:``opensearchserverless``: [``botocore``] Amazon OpenSearch Serverless collections support an additional attribute called standby-replicas. This allows to specify whether a collection should have redundancy enabled.
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] This release adds following support 1/ Improved SDK tooling for model deployment. 2/ New Inference Component based features to lower inference costs and latency 3/ SageMaker HyperPod management. 4/ Additional parameters for FM Fine Tuning in Autopilot
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.33.2
======

* api-change:``accessanalyzer``: [``botocore``] This release adds support for external access findings for S3 directory buckets to help you easily identify cross-account access. Updated service API, documentation, and paginators.
* api-change:``bedrock-agent-runtime``: [``botocore``] This release introduces Agents for Amazon Bedrock Runtime
* api-change:``bedrock-agent``: [``botocore``] This release introduces Agents for Amazon Bedrock
* api-change:``bedrock-runtime``: [``botocore``] This release adds support for minor versions/aliases for invoke model identifier.
* api-change:``bedrock``: [``botocore``] This release adds support for customization types, model life cycle status and minor versions/aliases for model identifiers.
* api-change:``connect``: [``botocore``] Added support for following capabilities: Amazon Connect's in-app, web, and video calling. Two-way SMS integrations. Contact Lens real-time chat analytics feature. Amazon Connect Analytics Datalake capability. Capability to configure real time chat rules.
* api-change:``customer-profiles``: [``botocore``] This release introduces DetectProfileObjectType API to auto generate object type mapping.
* api-change:``qbusiness``: [``botocore``] Amazon Q - a generative AI powered application that your employees can use to ask questions and get answers from knowledge spread across disparate content repositories, summarize reports, write articles, take actions, and much more - all within their company's connected content repositories.
* api-change:``qconnect``: [``botocore``] Amazon Q in Connect, an LLM-enhanced evolution of Amazon Connect Wisdom. This release adds generative AI support to Amazon Q Connect QueryAssistant and GetRecommendations APIs.
* api-change:``s3``: [``botocore``] Adds support for S3 Express One Zone.
* api-change:``s3control``: [``botocore``] Adds support for S3 Express One Zone, and InvocationSchemaVersion 2.0 for S3 Batch Operations.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.33.1
======

* api-change:``elasticache``: [``botocore``] Launching Amazon ElastiCache Serverless that enables you to create a cache in under a minute without any capacity management. ElastiCache Serverless monitors the cache's memory, CPU, and network usage and scales both vertically and horizontally to support your application's requirements.


1.33.0
======

* enhancement:Versioning: Bump boto3 from 1.29.7 to 1.33.0 to match Botocore versioning scheme.
* feature:``s3``: Boto3 will now opt into using the awscrt on select EC2 instance types for s3 transfers.
* feature:Versioning: [``botocore``] With the release of Botocore 1.33.0, Boto3 and Botocore will share the same version number.
* api-change:``appsync``: [``botocore``] This update enables introspection of Aurora cluster databases using the RDS Data API
* api-change:``b2bi``: [``botocore``] This is the initial SDK release for AWS B2B Data Interchange.
* api-change:``backup``: [``botocore``] AWS Backup now supports restore testing, a new feature that allows customers to automate restore testing and validating their backups. Additionally, this release adds support for EBS Snapshots Archive tier.
* api-change:``controltower``: [``botocore``] This release adds the following support: 1. The EnableControl API can configure controls that are configurable.  2. The GetEnabledControl API shows the configured parameters on an enabled control. 3. The new UpdateEnabledControl API can change parameters on an enabled control.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``fis``: [``botocore``] AWS FIS adds support for multi-account experiments & empty target resolution. This release also introduces the CreateTargetAccountConfiguration API that allows experiments across multiple AWS accounts, and the ListExperimentResolvedTargets API to list target details.
* api-change:``glue``: [``botocore``] add observations support to DQ CodeGen config model + update document for connectiontypes supported by ConnectorData entities
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for support for RDS for Db2.
* api-change:``securityhub``: [``botocore``] Adds and updates APIs to support central configuration. This feature allows the Security Hub delegated administrator to configure Security Hub for their entire AWS Org across multiple regions from a home Region. With this release, findings also include account name and application metadata.
* api-change:``transcribe``: [``botocore``] This release adds support for AWS HealthScribe APIs within Amazon Transcribe
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.7
======

* enhancement:AWSCRT: [``botocore``] Update awscrt version to 0.19.17
* api-change:``accessanalyzer``: [``botocore``] IAM Access Analyzer now continuously monitors IAM roles and users in your AWS account or organization to generate findings for unused access. Additionally, IAM Access Analyzer now provides custom policy checks to validate that IAM policies adhere to your security standards ahead of deployments.
* api-change:``amp``: [``botocore``] This release adds support for the Amazon Managed Service for Prometheus collector, a fully managed, agentless Prometheus metrics scraping capability.
* api-change:``bcm-data-exports``: [``botocore``] Users can create, read, update, delete Exports of billing and cost management data.  Users can get details of Export Executions and details of Tables for exporting.  Tagging support is provided for Exports
* api-change:``cloudtrail``: [``botocore``] CloudTrail Lake now supports federating event data stores. giving users the ability to run queries against their event data using Amazon Athena.
* api-change:``codestar-connections``: [``botocore``] This release adds support for the CloudFormation Git sync feature. Git sync enables updating a CloudFormation stack from a template stored in a Git repository.
* api-change:``compute-optimizer``: [``botocore``] This release enables AWS Compute Optimizer to analyze and generate recommendations with customization and discounts preferences.
* api-change:``config``: [``botocore``] Support Periodic Recording for Configuration Recorder
* api-change:``controltower``: [``botocore``] Add APIs to create and manage a landing zone.
* api-change:``cost-optimization-hub``: [``botocore``] This release launches Cost Optimization Hub, a new AWS Billing and Cost Management feature that helps you consolidate and prioritize cost optimization recommendations across your AWS Organizations member accounts and AWS Regions, so that you can get the most out of your AWS spend.
* api-change:``detective``: [``botocore``] Added new APIs in Detective to support resource investigations
* api-change:``ecs``: [``botocore``] Adds a new 'type' property to the Setting structure. Adds a new AccountSetting - guardDutyActivate for ECS.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``eks-auth``: [``botocore``] This release adds support for EKS Pod Identity feature. EKS Pod Identity makes it easy for customers to obtain IAM permissions for their applications running in the EKS clusters.
* api-change:``eks``: [``botocore``] This release adds support for EKS Pod Identity feature. EKS Pod Identity makes it easy for customers to obtain IAM permissions for the applications running in their EKS clusters.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``freetier``: [``botocore``] This is the initial SDK release for the AWS Free Tier GetFreeTierUsage API
* api-change:``fsx``: [``botocore``] Added support for FSx for ONTAP scale-out file systems and FlexGroup volumes. Added the HAPairs field and ThroughputCapacityPerHAPair for filesystem. Added AggregateConfiguration (containing Aggregates and ConstituentsPerAggregate) and SizeInBytes for volume.
* api-change:``guardduty``: [``botocore``] Add support for Runtime Monitoring for ECS and ECS-EC2.
* api-change:``iotfleetwise``: [``botocore``] AWS IoT FleetWise introduces new APIs for vision system data, such as data collected from cameras, radars, and lidars. You can now model and decode complex data types.
* api-change:``lakeformation``: [``botocore``] This release adds four new APIs "DescribeLakeFormationIdentityCenterConfiguration", "CreateLakeFormationIdentityCenterConfiguration", "DescribeLakeFormationIdentityCenterConfiguration", and "DeleteLakeFormationIdentityCenterConfiguration", and also updates the corresponding documentation.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``logs``: [``botocore``] Added APIs to Create, Update, Get, List and Delete LogAnomalyDetectors and List and Update Anomalies in Detector. Added LogGroupClass attribute for LogGroups to classify loggroup as Standard loggroup with all capabilities or InfrequentAccess loggroup with limited capabilities.
* api-change:``managedblockchain``: [``botocore``] Add optional NetworkType property to Accessor APIs
* api-change:``personalize-events``: [``botocore``] This release enables PutActions and PutActionInteractions
* api-change:``personalize-runtime``: [``botocore``] Enables metadata in recommendations and next best action recommendations
* api-change:``personalize``: [``botocore``] Enables metadata in recommendations, recommendations with themes, and next best action recommendations
* api-change:``quicksight``: [``botocore``] This release launches new APIs for trusted identity propagation setup and supports creating datasources using trusted identity propagation as authentication method for QuickSight accounts configured with IAM Identity Center.
* api-change:``redshift``: [``botocore``] This release adds support for multi-data warehouse writes through data sharing.
* api-change:``repostspace``: [``botocore``] Initial release of AWS re:Post Private
* api-change:``s3``: [``botocore``] Adding new params - Key and Prefix, to S3 API operations for supporting S3 Access Grants. Note - These updates will not change any of the existing S3 API functionality.
* api-change:``s3control``: [``botocore``] Introduce Amazon S3 Access Grants, a new S3 access control feature that maps identities in directories such as Active Directory, or AWS Identity and Access Management (IAM) Principals, to datasets in S3.
* api-change:``secretsmanager``: [``botocore``] AWS Secrets Manager has released the BatchGetSecretValue API, which allows customers to fetch up to 20 Secrets with a single request using a list of secret names or filters.
* api-change:``securityhub``: [``botocore``] Adds and updates APIs to support customizable security controls. This feature allows Security Hub customers to provide custom parameters for security controls. With this release, findings for controls that support custom parameters will include the parameters used to generate the findings.
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``transcribe``: [``botocore``] This release adds support for transcriptions from audio sources in 64 new languages and introduces generative call summarization in Transcribe Call Analytics (Post call)
* api-change:``workspaces-thin-client``: [``botocore``] Initial release of Amazon WorkSpaces Thin Client
* api-change:``workspaces``: [``botocore``] The release introduces Multi-Region Resilience one-way data replication that allows you to replicate data from your primary WorkSpace to a standby WorkSpace in another AWS Region. DescribeWorkspaces now returns the status of data replication.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.6
======

* bugfix:sqs: [``botocore``] Rolled back recent change to wire format protocol
* api-change:``kinesis``: [``botocore``] This release adds support for resource based policies on streams and consumers.
* api-change:``s3control``: [``botocore``] Amazon S3 Batch Operations now manages buckets or prefixes in a single step.
* api-change:``sagemaker``: [``botocore``] This feature adds the end user license agreement status as a model access configuration parameter.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.5
======

* api-change:``cloudfront-keyvaluestore``: [``botocore``] This release adds support for CloudFront KeyValueStore, a globally managed key value datastore associated with CloudFront Functions.
* api-change:``cloudfront``: [``botocore``] This release adds support for CloudFront KeyValueStore, a globally managed key value datastore associated with CloudFront Functions.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``inspector-scan``: [``botocore``] This release adds support for the new Amazon Inspector Scan API. The new Inspector Scan API can synchronously scan SBOMs adhering to the CycloneDX v1.5 format.
* api-change:``iotsitewise``: [``botocore``] Adds 1/ user-defined unique identifier for asset and model metadata, 2/ asset model components, and 3/ query API for asset metadata and telemetry data. Supports 4/ multi variate anomaly detection using Amazon Lookout for Equipment, 5/ warm storage tier, and 6/ buffered ingestion of time series data.
* api-change:``iottwinmaker``: [``botocore``] This release adds following support. 1. New APIs for metadata bulk operations. 2. Modify the component type API to support composite component types - nesting component types within one another. 3. New list APIs for components and properties. 4. Support the larger scope digital twin modeling.
* api-change:``s3``: [``botocore``] Add support for automatic date based partitioning in S3 Server Access Logs.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.4
======

* enhancement:IMDS: [``botocore``] Adds a config option to opt out of IMDSv1 fallback
* api-change:``codestar-connections``: [``botocore``] This release updates a few CodeStar Connections related APIs.
* api-change:``docdb``: [``botocore``] Amazon DocumentDB updates for new cluster storage configuration: Amazon DocumentDB I/O-Optimized.
* api-change:``ec2``: [``botocore``] This release adds support for Security group referencing over Transit gateways, enabling you to simplify Security group management and control of instance-to-instance traffic across VPCs that are connected by Transit gateway.


1.29.3
======

* api-change:``macie``: [``botocore``] The macie client has been removed following the deprecation of the service.
* api-change:``appmesh``: [``botocore``] Change the default value of these fields from 0 to null: MaxConnections, MaxPendingRequests, MaxRequests, HealthCheckThreshold, PortNumber, and HealthCheckPolicy -> port. Users are not expected to perceive the change, except that badRequestException is thrown when required fields missing configured.
* api-change:``athena``: [``botocore``] Adding SerivicePreProcessing time metric
* api-change:``cloud9``: [``botocore``] A minor doc only update related to changing the date of an API change.
* api-change:``cloudformation``: [``botocore``] This release adds a new flag ImportExistingResources to CreateChangeSet. Specify this parameter on a CREATE- or UPDATE-type change set to import existing resources with custom names instead of recreating them.
* api-change:``codepipeline``: [``botocore``] CodePipeline now supports overriding source revisions to achieve manual re-deploy of a past revision
* api-change:``codestar-connections``: [``botocore``] This release adds support for the CloudFormation Git sync feature. Git sync enables updating a CloudFormation stack from a template stored in a Git repository.
* api-change:``connect``: [``botocore``] This release adds WISDOM_QUICK_RESPONSES as new IntegrationType of Connect IntegrationAssociation resource and bug fixes.
* api-change:``dlm``: [``botocore``] Added support for SAP HANA in Amazon Data Lifecycle Manager EBS snapshot lifecycle policies with pre and post scripts.
* api-change:``ec2``: [``botocore``] This release adds new features for Amazon VPC IP Address Manager (IPAM) Allowing a choice between Free and Advanced Tiers, viewing public IP address insights across regions and in Amazon Cloudwatch, use IPAM to plan your subnet IPs within a VPC and bring your own autonomous system number to IPAM.
* api-change:``ecr``: [``botocore``] Documentation and operational updates for Amazon ECR, adding support for pull through cache rules for upstream registries that require authentication.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``internetmonitor``: [``botocore``] Adds new querying capabilities for running data queries on a monitor
* api-change:``ivs``: [``botocore``] type & defaulting refinement to various range properties
* api-change:``ivschat``: [``botocore``] type & defaulting refinement to various range properties
* api-change:``kinesisvideo``: [``botocore``] Docs only build to bring up-to-date with public docs.
* api-change:``location``: [``botocore``] Remove default value and allow nullable for request parameters having minimum value larger than zero.
* api-change:``medialive``: [``botocore``] MediaLive has now added support for per-output static image overlay.
* api-change:``mgn``: [``botocore``] Removed invalid and unnecessary default values.
* api-change:``osis``: [``botocore``] Add support for enabling a persistent buffer when creating or updating an OpenSearch Ingestion pipeline. Add tags to Pipeline and PipelineSummary response models.
* api-change:``pipes``: [``botocore``] TargetParameters now properly supports BatchJobParameters.ArrayProperties.Size and BatchJobParameters.RetryStrategy.Attempts being optional, and EcsTaskParameters.Overrides.EphemeralStorage.SizeInGiB now properly required when setting EphemeralStorage
* api-change:``rds``: [``botocore``] This release adds support for option groups and replica enhancements to Amazon RDS Custom.
* api-change:``redshift-serverless``: [``botocore``] Updated SDK for Amazon Redshift Serverless, which provides the ability to configure a connection with IAM Identity Center to manage user and group access to databases.
* api-change:``redshift``: [``botocore``] Updated SDK for Amazon Redshift, which you can use to configure a connection with IAM Identity Center to manage access to databases. With these, you can create a connection through a managed application. You can also change a managed application, delete it, or get information about an existing one.
* api-change:``s3``: [``botocore``] Removes all default 0 values for numbers and false values for booleans
* api-change:``sso-admin``: [``botocore``] Improves support for configuring RefreshToken and TokenExchange grants on applications.
* api-change:``sso-oidc``: [``botocore``] Adding support for `sso-oauth:CreateTokenWithIAM`.
* api-change:``sts``: [``botocore``] API updates for the AWS Security Token Service
* api-change:``trustedadvisor``: [``botocore``] AWS Trusted Advisor introduces new APIs to enable you to programmatically access Trusted Advisor best practice checks, recommendations, and prioritized recommendations. Trusted Advisor APIs enable you to integrate Trusted Advisor with your operational tools to automate your workloads.
* api-change:``verifiedpermissions``: [``botocore``] Adding BatchIsAuthorized API which supports multiple authorization requests against a PolicyStore
* api-change:``wisdom``: [``botocore``] This release adds QuickResponse as a new Wisdom resource and Wisdom APIs for import, create, read, search, update and delete QuickResponse resources.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.2
======

* api-change:``codecatalyst``: [``botocore``] This release includes updates to the Dev Environment APIs to include an optional vpcConnectionName parameter that supports using Dev Environments with Amazon VPC.
* api-change:``dlm``: [``botocore``] This release adds support for Amazon Data Lifecycle Manager default policies for EBS snapshots and EBS-backed AMIs.
* api-change:``ec2``: [``botocore``] Enable use of tenant-specific PublicSigningKeyUrl from device trust providers and onboard jumpcloud as a new device trust provider.
* api-change:``fsx``: [``botocore``] Enables customers to update their PerUnitStorageThroughput on their Lustre file systems.
* api-change:``glue``: [``botocore``] Introduces new column statistics APIs to support statistics generation for tables within the Glue Data Catalog.
* api-change:``imagebuilder``: [``botocore``] This release adds the Image Lifecycle Management feature to automate the process of deprecating, disabling and deleting outdated images and their associated resources.
* api-change:``iot``: [``botocore``] GA release the ability to index and search devices based on their GeoLocation data. With GeoQueries you can narrow your search to retrieve devices located in the desired geographic boundary.
* api-change:``ivs-realtime``: [``botocore``] This release introduces server side composition and recording for stages.
* api-change:``kafka``: [``botocore``] Added a new API response field which determines if there is an action required from the customer regarding their cluster.
* api-change:``lambda``: [``botocore``] Adds support for logging configuration in Lambda Functions. Customers will have more control how their function logs are captured and to which cloud watch log group they are delivered also.
* api-change:``macie2``: [``botocore``] This release adds support for configuring Macie to assume an IAM role when retrieving sample occurrences of sensitive data reported by findings.
* api-change:``mediapackage``: [``botocore``] DRM_TOP_LEVEL_COMPACT allows placing content protection elements at the MPD level and referenced at the AdaptationSet level
* api-change:``pinpoint-sms-voice-v2``: [``botocore``] Amazon Pinpoint now offers additional operations as part of version 2 of the SMS and voice APIs. This release includes 26 new APIs to create and manage phone number registrations, add verified destination numbers, and request sender IDs.
* api-change:``polly``: [``botocore``] Add new engine - long-form - dedicated for longer content, such as news articles, training materials, or marketing videos.
* api-change:``quicksight``: [``botocore``] Custom permission support for QuickSight roles; Three new datasources STARBURST, TRINO, BIGQUERY; Lenient mode changes the default behavior to allow for exporting and importing with certain UI allowed errors, Support for permissions and tags export and import.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Studio now supports Trainium instance types - trn1.2xlarge, trn1.32xlarge, trn1n.32xlarge.
* api-change:``ssm-incidents``: [``botocore``] Introduces new APIs ListIncidentFindings and BatchGetIncidentFindings to use findings related to an incident.
* api-change:``ssm``: [``botocore``] This release introduces the ability to filter automation execution steps which have parent steps. In addition, runbook variable information is returned by GetAutomationExecution and parent step information is returned by the DescribeAutomationStepExecutions API.
* api-change:``sso-admin``: [``botocore``] Instances bound to a single AWS account, API operations for managing instances and applications, and assignments to applications are now supported. Trusted identity propagation is also supported, with new API operations for managing trusted token issuers and application grants and scopes.
* api-change:``transfer``: [``botocore``] Introduced S3StorageOptions for servers to enable directory listing optimizations and added Type fields to logical directory mappings.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.29.1
======

* enhancement:Package Size: [``botocore``] The botocore .whl file distributed on PyPI now provides compressed service models to improve total size on disk.
* api-change:``autoscaling``: [``botocore``] This release introduces Instance Maintenance Policy, a new EC2 Auto Scaling capability that allows customers to define whether instances are launched before or after existing instances are terminated during instance replacement operations.
* api-change:``cloudtrail``: [``botocore``] The Lake Repricing feature lets customers configure a BillingMode for an event data store. The BillingMode determines the cost for ingesting and storing events and the default and maximum retention period for the event data store.
* api-change:``codecatalyst``: [``botocore``] This release adds functionality for retrieving information about workflows and workflow runs and starting workflow runs in Amazon CodeCatalyst.
* api-change:``ec2``: [``botocore``] AWS EBS now supports Snapshot Lock, giving users the ability to lock an EBS Snapshot to prohibit deletion of the snapshot. This release introduces the LockSnapshot, UnlockSnapshot & DescribeLockedSnapshots APIs to manage lock configuration for snapshots. The release also includes the dl2q_24xlarge.
* api-change:``finspace-data``: [``botocore``] Adding deprecated trait to APIs in this name space.
* api-change:``finspace``: [``botocore``] Adding deprecated trait on Dataset Browser Environment APIs
* api-change:``lambda``: [``botocore``] Add Java 21 (java21) support to AWS Lambda
* api-change:``mwaa``: [``botocore``] This Amazon MWAA release adds support for customer-managed VPC endpoints. This lets you choose whether to create, and manage your environment's VPC endpoints, or to have Amazon MWAA create, and manage them for you.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for support for upgrading RDS for MySQL snapshots from version 5.7 to version 8.0.
* api-change:``redshift``: [``botocore``] The custom domain name SDK for Amazon Redshift provisioned clusters is updated with additional required parameters for modify and delete operations. Additionally, users can provide domain names with longer top-level domains.
* api-change:``s3control``: [``botocore``] Add 5 APIs to create, update, get, list, delete S3 Storage Lens group(eg. CreateStorageLensGroup), 3 APIs for tagging(TagResource,UntagResource,ListTagsForResource), and update to StorageLensConfiguration to allow metrics to be aggregated on Storage Lens groups.
* api-change:``ssm-sap``: [``botocore``] Update the default value of MaxResult to 50.


1.29.0
======

* feature:ContainerProvider: [``botocore``] Added Support for EKS container credentials
* api-change:``backup``: [``botocore``] AWS Backup - Features: Provide Job Summary for your backup activity.
* api-change:``cleanrooms``: [``botocore``] This feature provides the ability for the collaboration creator to configure either the member who can run queries or a different member in the collaboration to be billed for query compute costs.
* api-change:``connect``: [``botocore``] Introducing SegmentAttributes parameter for StartChatContact API
* api-change:``glue``: [``botocore``] Introduces new storage optimization APIs to support automatic compaction of Apache Iceberg tables.
* api-change:``iot``: [``botocore``] This release introduces new attributes in API CreateSecurityProfile, UpdateSecurityProfile and DescribeSecurityProfile to support management of Metrics Export for AWS IoT Device Defender Detect.
* api-change:``lambda``: [``botocore``] Add Python 3.12 (python3.12) support to AWS Lambda
* api-change:``mediatailor``: [``botocore``] Removed unnecessary default values.
* api-change:``pipes``: [``botocore``] Added support (via new LogConfiguration field in CreatePipe and UpdatePipe APIs) for logging to Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), and Amazon Kinesis Data Firehose
* api-change:``resource-explorer-2``: [``botocore``] Resource Explorer supports multi-account search. You can now use Resource Explorer to search and discover resources across AWS accounts within your organization or organizational unit.
* api-change:``sagemaker``: [``botocore``] This release makes Model Registry Inference Specification fields as not required.
* api-change:``signer``: [``botocore``] Documentation updates for AWS Signer
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.85
=======

* enhancement:AWSCRT: [``botocore``] Update awscrt version to 0.19.12
* api-change:``dataexchange``: [``botocore``] Removed Required trait for DataSet.OriginDetails.ProductId.
* api-change:``dms``: [``botocore``] Added new Db2 LUW Target endpoint with related endpoint settings. New executeTimeout endpoint setting for mysql endpoint. New ReplicationDeprovisionTime field for serverless describe-replications.
* api-change:``ec2``: [``botocore``] Adds the new EC2 DescribeInstanceTopology API, which you can use to retrieve the network topology of your running instances on select platform types to determine their relative proximity to each other.
* api-change:``ecs``: [``botocore``] Adds a Client Token parameter to the ECS RunTask API. The Client Token parameter allows for idempotent RunTask requests.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``servicecatalog-appregistry``: [``botocore``] When the customer associates a resource collection to their application with this new feature, then a new application tag will be applied to all supported resources that are part of that collection. This allows customers to more easily find the application that is associated with those resources.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.84
=======

* enhancement:AWSCRT: [``botocore``] Update awscrt version to 0.19.10
* api-change:``controltower``: [``botocore``] AWS Control Tower supports tagging for enabled controls. This release introduces TagResource, UntagResource and ListTagsForResource APIs to manage tags in existing enabled controls. It updates EnabledControl API to tag resources at creation time.
* api-change:``cur``: [``botocore``] This release adds support for tagging and customers can now tag report definitions. Additionally, ReportStatus is now added to report definition to show when the last delivered time stamp and if it succeeded or not.
* api-change:``ec2``: [``botocore``] EC2 adds API updates to enable ENA Express at instance launch time.
* api-change:``fms``: [``botocore``] Adds optimizeUnassociatedWebACL flag to ManagedServiceData, updates third-party firewall examples, and other minor documentation updates.
* api-change:``marketplace-entitlement``: [``botocore``] Update marketplace-entitlement client to latest version
* api-change:``mediaconvert``: [``botocore``] This release includes the ability to specify any input source as the primary input for corresponding follow modes, and allows users to specify fit and fill behaviors without resizing content.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for zero-ETL integrations.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.83
=======

* api-change:``cloudformation``: [``botocore``] Added new ConcurrencyMode feature for AWS CloudFormation StackSets for faster deployments to target accounts.
* api-change:``cloudtrail``: [``botocore``] The Insights in Lake feature lets customers enable CloudTrail Insights on a source CloudTrail Lake event data store and create a destination event data store to collect Insights events based on unusual management event activity in the source event data store.
* api-change:``comprehend``: [``botocore``] This release adds support for toxicity detection and prompt safety classification.
* api-change:``connect``: [``botocore``] This release adds the ability to integrate customer lambda functions with Connect attachments for scanning and updates the ListIntegrationAssociations API to support filtering on IntegrationArn.
* api-change:``ec2``: [``botocore``] AWS EBS now supports Block Public Access for EBS Snapshots. This release introduces the EnableSnapshotBlockPublicAccess, DisableSnapshotBlockPublicAccess and GetSnapshotBlockPublicAccessState APIs to manage account-level public access settings for EBS Snapshots in an AWS Region.
* api-change:``eks``: [``botocore``] Adding EKS Anywhere subscription related operations.
* api-change:``lambda``: [``botocore``] Add Custom runtime on Amazon Linux 2023 (provided.al2023) support to AWS Lambda.
* api-change:``logs``: [``botocore``] Update to support new APIs for delivery of logs from AWS services.
* api-change:``omics``: [``botocore``] Support UBAM filetype for Omics Storage and make referenceArn optional
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.82
=======

* api-change:``sqs``: [``botocore``] This release enables customers to call SQS using AWS JSON-1.0 protocol and bug fix.


1.28.81
=======

* api-change:``connect``: [``botocore``] This release clarifies in our public documentation that InstanceId is a requirement for SearchUsers API requests.
* api-change:``connectcases``: [``botocore``] This release adds the ability to add/view comment authors through CreateRelatedItem and SearchRelatedItems API. For more information see https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html
* api-change:``datasync``: [``botocore``] This change allows for 0 length access keys and secret keys for object storage locations. Users can now pass in empty string credentials.
* api-change:``guardduty``: [``botocore``] Added API support for new GuardDuty EKS Audit Log finding types.
* api-change:``lambda``: [``botocore``] Add Node 20 (nodejs20.x) support to AWS Lambda.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``omics``: [``botocore``] Adding Run UUID and Run Output URI: GetRun and StartRun API response has two new fields "uuid" and "runOutputUri".
* api-change:``rds``: [``botocore``] This Amazon RDS release adds support for patching the OS of an RDS Custom for Oracle DB instance. You can now upgrade the database or operating system using the modify-db-instance command.
* api-change:``redshift-serverless``: [``botocore``] Added a new parameter in the workgroup that helps you control your cost for compute resources. This feature provides a ceiling for RPUs that Amazon Redshift Serverless can scale up to. When automatic compute scaling is required, having a higher value for MaxRPU can enhance query throughput.
* api-change:``resiliencehub``: [``botocore``] AWS Resilience Hub enhances Resiliency Score, providing actionable recommendations to improve application resilience. Amazon Elastic Kubernetes Service (EKS) operational recommendations have been added to help improve the resilience posture of your applications.
* api-change:``sqs``: [``botocore``] This release enables customers to call SQS using AWS JSON-1.0 protocol.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.80
=======

* api-change:``dataexchange``: [``botocore``] Updated SendDataSetNotificationRequest Comment to be maximum length 4096.
* api-change:``dlm``: [``botocore``] Added support for pre and post scripts in Amazon Data Lifecycle Manager EBS snapshot lifecycle policies.
* api-change:``rds``: [``botocore``] This Amazon RDS release adds support for the multi-tenant configuration. In this configuration, an RDS DB instance can contain multiple tenant databases. In RDS for Oracle, a tenant database is a pluggable database (PDB).
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.79
=======

* api-change:``ce``: [``botocore``] This release extends the GetReservationPurchaseRecommendation API to support recommendations for Amazon MemoryDB reservations.
* api-change:``codebuild``: [``botocore``] AWS CodeBuild now supports AWS Lambda compute.
* api-change:``connect``: [``botocore``] Added new API that allows Amazon Connect Outbound Campaigns to create contacts in Amazon Connect when ingesting your dial requests.
* api-change:``docdb``: [``botocore``] Update the input of CreateDBInstance and ModifyDBInstance to support setting CA Certificates. Update the output of DescribeDBInstance and DescribeDBEngineVersions to show current and supported CA certificates.
* api-change:``iam``: [``botocore``] Add partitional endpoint for iso-e.
* api-change:``mwaa``: [``botocore``] This release adds support for Apache Airflow version 2.7.2. This version release includes support for deferrable operators and triggers.
* api-change:``polly``: [``botocore``] Amazon Polly adds new US English voices - Danielle and Gregory. Danielle and Gregory are available as Neural voices only.
* api-change:``route53``: [``botocore``] Add partitional endpoints for iso-e and iso-f.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.78
=======

* api-change:``config``: [``botocore``] Updated ResourceType enum with new resource types onboarded by AWS Config in October 2023.
* api-change:``connect``: [``botocore``] Amazon Connect Chat introduces Create Persistent Contact Association API, allowing customers to choose when to resume previous conversations from previous chats, eliminating the need to repeat themselves and allowing agents to provide personalized service with access to entire conversation history.
* api-change:``iotwireless``: [``botocore``] Added LoRaWAN version 1.0.4 support
* api-change:``launch-wizard``: [``botocore``] AWS Launch Wizard is a service that helps reduce the time it takes to deploy applications to the cloud while providing a guided deployment experience.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.77
=======

* api-change:``apprunner``: [``botocore``] AWS App Runner now supports using dual-stack address type for the public endpoint of your incoming traffic.
* api-change:``connect``: [``botocore``] GetMetricDataV2 API: Update to include new metrics PERCENT_NON_TALK_TIME, PERCENT_TALK_TIME, PERCENT_TALK_TIME_AGENT, PERCENT_TALK_TIME_CUSTOMER
* api-change:``gamelift``: [``botocore``] Amazon GameLift adds support for shared credentials, which allows applications that are deployed on managed EC2 fleets to interact with other AWS resources.
* api-change:``glue``: [``botocore``] This release introduces Google BigQuery Source and Target in AWS Glue CodeGenConfigurationNode.
* api-change:``network-firewall``: [``botocore``] This release introduces the stateless rule analyzer, which enables you to analyze your stateless rules for asymmetric routing.
* api-change:``quicksight``: [``botocore``] This release introduces Float Decimal Type as SubType in QuickSight SPICE datasets and Custom week start and Custom timezone options in Analysis and Dashboard
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.76
=======

* api-change:``connect``: [``botocore``] Adds the BatchGetFlowAssociation API which returns flow associations (flow-resource) corresponding to the list of resourceArns supplied in the request. This release also adds IsDefault, LastModifiedRegion and LastModifiedTime fields to the responses of several Describe and List APIs.
* api-change:``globalaccelerator``: [``botocore``] Global Accelerator now support accelerators with cross account endpoints.
* api-change:``rds``: [``botocore``] This release adds support for customized networking resources to Amazon RDS Custom.
* api-change:``redshift``: [``botocore``] Added support for Multi-AZ deployments for Provisioned RA3 clusters that provide 99.99% SLA availability.
* api-change:``sagemaker``: [``botocore``] Support for batch transform input in Model dashboard


1.28.75
=======

* api-change:``amplify``: [``botocore``] Add backend field to CreateBranch and UpdateBranch requests. Add pagination support for ListApps, ListDomainAssociations, ListBranches, and ListJobs
* api-change:``application-insights``: [``botocore``] Automate attaching managed policies
* api-change:``ec2``: [``botocore``] Capacity Blocks for ML are a new EC2 purchasing option for reserving GPU instances on a future date to support short duration machine learning (ML) workloads. Capacity Blocks automatically place instances close together inside Amazon EC2 UltraClusters for low-latency, high-throughput networking.
* api-change:``m2``: [``botocore``] Added name filter ability for ListDataSets API, added ForceUpdate for Updating environment and BatchJob submission using S3BatchJobIdentifier
* api-change:``neptunedata``: [``botocore``] Minor change to not retry CancelledByUserException
* api-change:``translate``: [``botocore``] Added support for Brevity translation settings feature.


1.28.74
=======

* api-change:``connect``: [``botocore``] This release adds InstanceId field for phone number APIs.
* api-change:``dataexchange``: [``botocore``] We added a new API action: SendDataSetNotification.
* api-change:``datasync``: [``botocore``] Platform version changes to support AL1 deprecation initiative.
* api-change:``finspace``: [``botocore``] Introducing new API UpdateKxClusterCodeConfiguration, introducing new cache types for clusters and introducing new deployment modes for updating clusters.
* api-change:``mediapackagev2``: [``botocore``] This feature allows customers to create a combination of manifest filtering, startover and time delay configuration that applies to all egress requests by default.
* api-change:``rds``: [``botocore``] This release launches the CreateIntegration, DeleteIntegration, and DescribeIntegrations APIs to manage zero-ETL Integrations.
* api-change:``redshift-serverless``: [``botocore``] Added support for custom domain names for Amazon Redshift Serverless workgroups. This feature enables customers to create a custom domain name and use ACM to generate fully secure connections to it.
* api-change:``resiliencehub``: [``botocore``] Introduced the ability to filter applications by their last assessment date and time and have included metrics for the application's estimated workload Recovery Time Objective (RTO) and estimated workload Recovery Point Objective (RPO).
* api-change:``s3outposts``: [``botocore``] Updated ListOutpostsWithS3 API response to include S3OutpostArn for use with AWS RAM.
* api-change:``wisdom``: [``botocore``] This release added necessary API documents on creating a Wisdom knowledge base to integrate with S3.


1.28.73
=======

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``neptune``: [``botocore``] Update TdeCredentialPassword type to SensitiveString
* api-change:``pinpoint``: [``botocore``] Updated documentation to describe the case insensitivity for EndpointIds.
* api-change:``redshift``: [``botocore``] added support to create a dual stack cluster
* api-change:``wafv2``: [``botocore``] Updates the descriptions for the calls that manage web ACL associations, to provide information for customer-managed IAM policies.


1.28.72
=======

* api-change:``appstream``: [``botocore``] This release introduces multi-session fleets, allowing customers to provision more than one user session on a single fleet instance.
* api-change:``ec2``: [``botocore``] Launching GetSecurityGroupsForVpc API. This API gets security groups that can be associated by the AWS account making the request with network interfaces in the specified VPC.
* api-change:``network-firewall``: [``botocore``] Network Firewall now supports inspection of outbound SSL/TLS traffic.
* api-change:``opensearch``: [``botocore``] You can specify ipv4 or dualstack IPAddressType for cluster endpoints. If you specify IPAddressType as dualstack, the new endpoint will be visible under the 'EndpointV2' parameter and will support IPv4 and IPv6 requests. Whereas, the 'Endpoint' will continue to serve IPv4 requests.
* api-change:``redshift``: [``botocore``] Add Redshift APIs GetResourcePolicy, DeleteResourcePolicy, PutResourcePolicy and DescribeInboundIntegrations for the new Amazon Redshift Zero-ETL integration feature, which can be used to control data ingress into Redshift namespace, and view inbound integrations.
* api-change:``sagemaker``: [``botocore``] Amazon Sagemaker Autopilot now supports Text Generation jobs.
* api-change:``sns``: [``botocore``] Message Archiving and Replay is now supported in Amazon SNS for FIFO topics.
* api-change:``ssm-sap``: [``botocore``] AWS Systems Manager for SAP added support for registration and discovery of SAP ABAP applications
* api-change:``transfer``: [``botocore``] No API changes from previous release. This release migrated the model to Smithy keeping all features unchanged.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.28.71
=======

* enhancement:Configuration: [``botocore``] Adds client context params support to ``Config``.
* api-change:``connectcases``: [``botocore``] Increase maximum length of CommentBody to 3000, and increase maximum length of StringValue to 1500
* api-change:``groundstation``: [``botocore``] This release will allow KMS alias names to be used when creating Mission Profiles
* api-change:``iam``: [``botocore``] Updates to GetAccessKeyLastUsed action to replace NoSuchEntity error with AccessDeniedException error.


1.28.70
=======

* api-change:``codepipeline``: [``botocore``] Add ability to trigger pipelines from git tags, define variables at pipeline level and new pipeline type V2.
* api-change:``ec2``: [``botocore``] This release updates the documentation for InstanceInterruptionBehavior and HibernationOptionsRequest to more accurately describe the behavior of these two parameters when using Spot hibernation.
* api-change:``eks``: [``botocore``] Added support for Cluster Subnet and Security Group mutability.
* api-change:``iam``: [``botocore``] Add the partitional endpoint for IAM in iso-f.
* api-change:``migrationhub-config``: [``botocore``] This release introduces DeleteHomeRegionControl API that customers can use to delete the Migration Hub Home Region configuration
* api-change:``migrationhubstrategy``: [``botocore``] This release introduces multi-data-source feature in Migration Hub Strategy Recommendations. This feature now supports vCenter as a data source to fetch inventory in addition to ADS and Import from file workflow that is currently supported with MHSR collector.
* api-change:``opensearchserverless``: [``botocore``] This release includes the following new APIs: CreateLifecyclePolicy, UpdateLifecyclePolicy, BatchGetLifecyclePolicy, DeleteLifecyclePolicy, ListLifecyclePolicies and BatchGetEffectiveLifecyclePolicy to support the data lifecycle management feature.


1.28.69
=======

* api-change:``marketplacecommerceanalytics``: [``botocore``] The StartSupportDataExport operation has been deprecated as part of the Product Support Connection deprecation. As of December 2022, Product Support Connection is no longer supported.
* api-change:``networkmanager``: [``botocore``] This release adds API support for Tunnel-less Connect (NoEncap Protocol) for AWS Cloud WAN
* api-change:``redshift-serverless``: [``botocore``] This release adds support for customers to see the patch version and workgroup version in Amazon Redshift Serverless.
* api-change:``rekognition``: [``botocore``] Amazon Rekognition introduces StartMediaAnalysisJob, GetMediaAnalysisJob, and ListMediaAnalysisJobs operations to run a bulk analysis of images with a Detect Moderation model.


1.28.68
=======

* api-change:``appconfig``: [``botocore``] Update KmsKeyIdentifier constraints to support AWS KMS multi-Region keys.
* api-change:``appintegrations``: [``botocore``] Updated ScheduleConfig to be an optional input to CreateDataIntegration to support event driven downloading of files from sources such as Amazon s3 using Amazon Connect AppIntegrations.
* api-change:``connect``: [``botocore``] This release adds support for updating phone number metadata, such as phone number description.
* api-change:``discovery``: [``botocore``] This release introduces three new APIs: StartBatchDeleteConfigurationTask, DescribeBatchDeleteConfigurationTask, and BatchDeleteAgents.
* api-change:``medical-imaging``: [``botocore``] Updates on documentation links
* api-change:``ssm``: [``botocore``] This release introduces a new API: DeleteOpsItem. This allows deletion of an OpsItem.


1.28.67
=======

* api-change:``gamesparks``: [``botocore``] The gamesparks client has been removed following the deprecation of the service.
* api-change:``ec2``: [``botocore``] Amazon EC2 C7a instances, powered by 4th generation AMD EPYC processors, are ideal for high performance, compute-intensive workloads such as high performance computing. Amazon EC2 R7i instances are next-generation memory optimized and powered by custom 4th Generation Intel Xeon Scalable processors.
* api-change:``managedblockchain-query``: [``botocore``] This release adds support for Ethereum Sepolia network
* api-change:``neptunedata``: [``botocore``] Doc changes to add IAM action mappings for the data actions.
* api-change:``omics``: [``botocore``] This change enables customers to retrieve failure reasons with detailed status messages for their failed runs
* api-change:``opensearch``: [``botocore``] Added Cluster Administrative options for node restart, opensearch process restart and opensearch dashboard restart for Multi-AZ without standby domains
* api-change:``quicksight``: [``botocore``] This release adds the following: 1) Trino and Starburst Database Connectors 2) Custom total for tables and pivot tables 3) Enable restricted folders 4) Add rolling dates for time equality filters 5) Refine DataPathValue and introduce DataPathType 6) Add SeriesType to ReferenceLineDataConfiguration
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``servicecatalog``: [``botocore``] Introduce support for EXTERNAL product and provisioning artifact type in CreateProduct and CreateProvisioningArtifact APIs.
* api-change:``verifiedpermissions``: [``botocore``] Improving Amazon Verified Permissions Create experience
* api-change:``workspaces``: [``botocore``] Documentation updates for WorkSpaces


1.28.66
=======

* api-change:``cloud9``: [``botocore``] Update to imageId parameter behavior and dates updated.
* api-change:``dynamodb``: [``botocore``] Updating descriptions for several APIs.
* api-change:``kendra``: [``botocore``] Changes for a new feature in Amazon Kendra's Query API to Collapse/Expand query results
* api-change:``rds``: [``botocore``] This release adds support for upgrading the storage file system configuration on the DB instance using a blue/green deployment or a read replica.
* api-change:``wisdom``: [``botocore``] This release adds an max limit of 25 recommendation ids for NotifyRecommendationsReceived API.


1.28.65
=======

* api-change:``codepipeline``: [``botocore``] Add retryMode ALL_ACTIONS to RetryStageExecution API that retries a failed stage starting from first action in the stage
* api-change:``discovery``: [``botocore``] This release introduces three new APIs: StartBatchDeleteConfigurationTask, DescribeBatchDeleteConfigurationTask, and BatchDeleteAgents.
* api-change:``ecs``: [``botocore``] Documentation only updates to address Amazon ECS tickets.
* api-change:``globalaccelerator``: [``botocore``] Fixed error where ListCustomRoutingEndpointGroups did not have a paginator
* api-change:``guardduty``: [``botocore``] Add domainWithSuffix finding field to dnsRequestAction
* api-change:``kafka``: [``botocore``] AWS Managed Streaming for Kafka is launching MSK Replicator, a new feature that enables customers to reliably replicate data across Amazon MSK clusters in same or different AWS regions. You can now use SDK to create, list, describe, delete, update, and manage tags of MSK Replicators.
* api-change:``route53-recovery-cluster``: [``botocore``] Adds Owner field to ListRoutingControls API.
* api-change:``route53-recovery-control-config``: [``botocore``] Adds permissions for GetResourcePolicy to support returning details about AWS Resource Access Manager resource policies for shared resources.


1.28.64
=======

* api-change:``cloudformation``: [``botocore``] SDK and documentation updates for UpdateReplacePolicy
* api-change:``drs``: [``botocore``] Updated exsiting API to allow AWS Elastic Disaster Recovery support of launching recovery into existing EC2 instances.
* api-change:``entityresolution``: [``botocore``] This launch expands our matching techniques to include provider-based matching to help customer match, link, and enhance records with minimal data movement. With data service providers, we have removed the need for customers to build bespoke integrations,.
* api-change:``managedblockchain-query``: [``botocore``] This release introduces two new APIs: GetAssetContract and ListAssetContracts. This release also adds support for Bitcoin Testnet.
* api-change:``mediapackagev2``: [``botocore``] This release allows customers to manage MediaPackage v2 resource using CloudFormation.
* api-change:``opensearch``: [``botocore``] This release allows customers to list and associate optional plugin packages with compatible Amazon OpenSearch Service clusters for enhanced functionality.
* api-change:``redshift-serverless``: [``botocore``] Added support for managing credentials of serverless namespace admin using AWS Secrets Manager.
* api-change:``redshift``: [``botocore``] Added support for managing credentials of provisioned cluster admin using AWS Secrets Manager.
* api-change:``sesv2``: [``botocore``] This release provides enhanced visibility into your SES identity verification status. This will offer you more actionable insights, enabling you to promptly address any verification-related issues.
* api-change:``transfer``: [``botocore``] Documentation updates for AWS Transfer Family
* api-change:``xray``: [``botocore``] This releases enhances GetTraceSummaries API to support new TimeRangeType Service to query trace summaries by segment end time.


1.28.63
=======

* api-change:``auditmanager``: [``botocore``] This release introduces a new limit to the awsAccounts parameter. When you create or update an assessment, there is now a limit of 200 AWS accounts that can be specified in the assessment scope.
* api-change:``autoscaling``: [``botocore``] Update the NotificationMetadata field to only allow visible ascii characters. Add paginators to DescribeInstanceRefreshes, DescribeLoadBalancers, and DescribeLoadBalancerTargetGroups
* api-change:``config``: [``botocore``] Add enums for resource types supported by Config
* api-change:``controltower``: [``botocore``] Added new EnabledControl resource details to ListEnabledControls API and added new GetEnabledControl API.
* api-change:``customer-profiles``: [``botocore``] Adds sensitive trait to various shapes in Customer Profiles Calculated Attribute API model.
* api-change:``ec2``: [``botocore``] This release adds Ubuntu Pro as a supported platform for On-Demand Capacity Reservations and adds support for setting an Amazon Machine Image (AMI) to disabled state. Disabling the AMI makes it private if it was previously shared, and prevents new EC2 instance launches from it.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``glue``: [``botocore``] Extending version control support to GitLab and Bitbucket from AWSGlue
* api-change:``inspector2``: [``botocore``] Add MacOs ec2 platform support
* api-change:``ivs-realtime``: [``botocore``] Update GetParticipant to return additional metadata.
* api-change:``lambda``: [``botocore``] Adds support for Lambda functions to access Dual-Stack subnets over IPv6, via an opt-in flag in CreateFunction and UpdateFunctionConfiguration APIs
* api-change:``location``: [``botocore``] This release adds endpoint updates for all AWS Location resource operations.
* api-change:``machinelearning``: [``botocore``] This release marks Password field as sensitive
* api-change:``pricing``: [``botocore``] Documentation updates for Price List
* api-change:``rds``: [``botocore``] This release adds support for adding a dedicated log volume to open-source RDS instances.
* api-change:``rekognition``: [``botocore``] Amazon Rekognition introduces support for Custom Moderation. This allows the enhancement of accuracy for detect moderation labels operations by creating custom adapters tuned on customer data.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Canvas adds KendraSettings and DirectDeploySettings support for CanvasAppSettings
* api-change:``textract``: [``botocore``] This release adds 9 new APIs for adapter and adapter version management, 3 new APIs for tagging, and updates AnalyzeDocument and StartDocumentAnalysis API parameters for using adapters.
* api-change:``transcribe``: [``botocore``] This release is to enable m4a format to customers
* api-change:``workspaces``: [``botocore``] Updated the CreateWorkspaces action documentation to clarify that the PCoIP protocol is only available for Windows bundles.


1.28.62
=======

* enhancement:Dependencies: [``botocore``] Add support for urllib3 2.0 for Python 3.10+
* api-change:``ec2``: [``botocore``] Documentation updates for Elastic Compute Cloud (EC2).
* api-change:``fsx``: [``botocore``] After performing steps to repair the Active Directory configuration of a file system, use this action to initiate the process of attempting to recover to the file system.
* api-change:``marketplace-catalog``: [``botocore``] This release adds support for Document type as an alternative for stringified JSON for StartChangeSet, DescribeChangeSet and DescribeEntity APIs
* api-change:``quicksight``: [``botocore``] NullOption in FilterListConfiguration; Dataset schema/table max length increased; Support total placement for pivot table visual; Lenient mode relaxes the validation to create resources with definition; Data sources can be added to folders; Redshift data sources support IAM Role-based authentication
* api-change:``transfer``: [``botocore``] This release updates the max character limit of PreAuthenticationLoginBanner and PostAuthenticationLoginBanner to 4096 characters


1.28.61
=======

* api-change:``omics``: [``botocore``] Add Etag Support for Omics Storage in ListReadSets and GetReadSetMetadata API
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for corrections and minor improvements.
* api-change:``route53``: [``botocore``] Add hostedzonetype filter to ListHostedZones API.
* api-change:``securityhub``: [``botocore``] Added new resource detail objects to ASFF, including resources for AwsEventsEventbus, AwsEventsEndpoint, AwsDmsEndpoint, AwsDmsReplicationTask, AwsDmsReplicationInstance, AwsRoute53HostedZone, and AwsMskCluster
* api-change:``storagegateway``: [``botocore``] Add SoftwareVersion to response of DescribeGatewayInformation.
* api-change:``workspaces``: [``botocore``] This release introduces Manage applications. This feature allows users to manage their WorkSpaces applications by associating or disassociating their WorkSpaces with applications. The DescribeWorkspaces API will now additionally return OperatingSystemName in its responses.


1.28.60
=======

* api-change:``appconfig``: [``botocore``] AWS AppConfig introduces KMS customer-managed key (CMK) encryption support for data saved to AppConfig's hosted configuration store.
* api-change:``datazone``: [``botocore``] Initial release of Amazon DataZone
* api-change:``mediatailor``: [``botocore``] Updates DescribeVodSource to include a list of ad break opportunities in the response
* api-change:``mgn``: [``botocore``] This release includes the following new APIs: ListConnectors, CreateConnector,  UpdateConnector, DeleteConnector and UpdateSourceServer to support the source action framework feature.
* api-change:``sagemaker``: [``botocore``] Adding support for AdditionalS3DataSource, a data source used for training or inference that is in addition to the input dataset or model data.


1.28.59
=======

* api-change:``connect``: [``botocore``] GetMetricDataV2 API: Update to include new metrics CONTACTS_RESOLVED_IN_X , AVG_HOLD_TIME_ALL_CONTACTS , AVG_RESOLUTION_TIME , ABANDONMENT_RATE , AGENT_NON_RESPONSE_WITHOUT_CUSTOMER_ABANDONS with added features: Interval Period, TimeZone, Negate MetricFilters, Extended date time range.
* api-change:``location``: [``botocore``] Amazon Location Service adds support for bounding polygon queries. Additionally, the GeofenceCount field has been added to the DescribeGeofenceCollection API response.
* api-change:``mediaconvert``: [``botocore``] This release adds the ability to replace video frames without modifying the audio essence.
* api-change:``oam``: [``botocore``] This release adds support for sharing AWS::ApplicationInsights::Application resources.
* api-change:``sagemaker``: [``botocore``] This release allows users to run Selective Execution in SageMaker Pipelines without SourcePipelineExecutionArn if selected steps do not have any dependent steps.
* api-change:``wellarchitected``: [``botocore``] AWS Well-Architected now supports Review Templates that allows you to create templates with pre-filled answers for Well-Architected and Custom Lens best practices.


1.28.58
=======

* api-change:``bedrock-runtime``: [``botocore``] Add model timeout exception for InvokeModelWithResponseStream API and update validator for invoke model identifier.
* api-change:``bedrock``: [``botocore``] Provisioned throughput feature with Amazon and third-party base models, and update validators for model identifier and taggable resource ARNs.
* api-change:``ec2``: [``botocore``] Introducing Amazon EC2 R7iz instances with 3.9 GHz sustained all-core turbo frequency and deliver up to 20% better performance than previous generation z1d instances.
* api-change:``managedblockchain``: [``botocore``] Remove Rinkeby as option from Ethereum APIs
* api-change:``rds``: [``botocore``] Adds DefaultCertificateForNewLaunches field in the DescribeCertificates API response.
* api-change:``sso``: [``botocore``] Fix FIPS Endpoints in aws-us-gov.
* api-change:``sts``: [``botocore``] STS API updates for assumeRole
* api-change:``transfer``: [``botocore``] Documentation updates for AWS Transfer Family


1.28.57
=======

* api-change:``bedrock-runtime``: [``botocore``] Run Inference: Added support to run the inference on models.  Includes set of APIs for running inference in streaming and non-streaming mode.
* api-change:``bedrock``: [``botocore``] Model Invocation logging added to enable or disable logs in customer account. Model listing and description support added. Provisioned Throughput feature added. Custom model support added for creating custom models. Also includes list, and delete functions for custom model.
* api-change:``budgets``: [``botocore``] Update DescribeBudgets and DescribeBudgetNotificationsForAccount MaxResults limit to 1000.
* api-change:``ec2``: [``botocore``] Adds support for Customer Managed Key encryption for Amazon Verified Access resources
* api-change:``iotfleetwise``: [``botocore``] AWS IoT FleetWise now supports encryption through a customer managed AWS KMS key. The PutEncryptionConfiguration and GetEncryptionConfiguration APIs were added.
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Feature Store supports read/write of records with collection type features.
* api-change:``sagemaker``: [``botocore``] Online store feature groups supports Standard and InMemory tier storage types for low latency storage for real-time data retrieval. The InMemory tier supports collection types List, Set, and Vector.
* api-change:``wafv2``: [``botocore``] Correct and improve the documentation for the FieldToMatch option JA3 fingerprint.


1.28.56
=======

* api-change:``cognito-idp``: [``botocore``] The UserPoolType Status field is no longer used.
* api-change:``firehose``: [``botocore``] Features : Adding support for new data ingestion source to Kinesis Firehose - AWS Managed Services Kafka.
* api-change:``iot``: [``botocore``] Added support for IoT Rules Engine Kafka Action Headers
* api-change:``textract``: [``botocore``] This release adds new feature - Layout to Analyze Document API which can automatically extract layout elements such as titles, paragraphs, headers, section headers, lists, page numbers, footers, table areas, key-value areas and figure areas and order the elements as a human would read.


1.28.55
=======

* api-change:``appintegrations``: [``botocore``] The Amazon AppIntegrations service adds a set of APIs (in preview) to manage third party applications to be used in Amazon Connect agent workspace.
* api-change:``apprunner``: [``botocore``] This release allows an App Runner customer to specify a custom source directory to run the build & start command. This change allows App Runner to support monorepo based repositories
* api-change:``codedeploy``: [``botocore``] CodeDeploy now supports In-place and Blue/Green EC2 deployments with multiple Classic Load Balancers and multiple Target Groups.
* api-change:``connect``: [``botocore``] This release updates a set of Amazon Connect APIs that provides the ability to integrate third party applications in the Amazon Connect agent workspace.
* api-change:``dynamodb``: [``botocore``] Amazon DynamoDB now supports Incremental Export as an enhancement to the existing Export Table
* api-change:``ec2``: [``botocore``] The release includes AWS verified access to support FIPs compliance in North America regions
* api-change:``lakeformation``: [``botocore``] This release adds three new API support "CreateLakeFormationOptIn", "DeleteLakeFormationOptIn" and "ListLakeFormationOptIns", and also updates the corresponding documentation.
* api-change:``pinpoint``: [``botocore``] Update documentation for RemoveAttributes to more accurately reflect its behavior when attributes are deleted.
* api-change:``s3``: [``botocore``] This release adds a new field COMPLETED to the ReplicationStatus Enum. You can now use this field to validate the replication status of S3 objects using the AWS SDK.


1.28.54
=======

* api-change:``amplifyuibuilder``: [``botocore``] Support for generating code that is compatible with future versions of amplify project dependencies.
* api-change:``chime-sdk-media-pipelines``: [``botocore``] Adds support for sending WebRTC audio to Amazon Kineses Video Streams.
* api-change:``emr-serverless``: [``botocore``] This release adds support for application-wide default job configurations.
* api-change:``finspace-data``: [``botocore``] Adding sensitive trait to attributes. Change max SessionDuration from 720 to 60. Correct "ApiAccess" attribute to "apiAccess" to maintain consistency between APIs.
* api-change:``quicksight``: [``botocore``] Added ability to tag users upon creation.
* api-change:``ssm``: [``botocore``] This release updates the enum values for ResourceType in SSM DescribeInstanceInformation input and ConnectionStatus in GetConnectionStatus output.
* api-change:``wafv2``: [``botocore``] You can now perform an exact match against the web request's JA3 fingerprint.


1.28.53
=======

* api-change:``braket``: [``botocore``] This release adds support to view the device queue depth (the number of queued quantum tasks and hybrid jobs on a device) and queue position for a quantum task and hybrid job.
* api-change:``dms``: [``botocore``] new vendors for DMS CSF: MongoDB, MariaDB, DocumentDb and Redshift
* api-change:``ec2``: [``botocore``] EC2 M2 Pro Mac instances are powered by Apple M2 Pro Mac Mini computers featuring 12 core CPU, 19 core GPU, 32 GiB of memory, and 16 core Apple Neural Engine and uniquely enabled by the AWS Nitro System through high-speed Thunderbolt connections.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``guardduty``: [``botocore``] Add `EKS_CLUSTER_NAME` to filter and sort key.
* api-change:``mediaconvert``: [``botocore``] This release supports the creation of of audio-only tracks in CMAF output groups.


1.28.52
=======

* api-change:``appconfig``: [``botocore``] Enabling boto3 paginators for list APIs and adding documentation around ServiceQuotaExceededException errors
* api-change:``apprunner``: [``botocore``] This release adds improvements for managing App Runner auto scaling configuration resources. New APIs: UpdateDefaultAutoScalingConfiguration and ListServicesForAutoScalingConfiguration. Updated API: DeleteAutoScalingConfiguration.
* api-change:``codeartifact``: [``botocore``] Add support for the Swift package format.
* api-change:``kinesisvideo``: [``botocore``] Updated DescribeMediaStorageConfiguration, StartEdgeConfigurationUpdate, ImageGenerationConfiguration$SamplingInterval, and UpdateMediaStorageConfiguration to match AWS Docs.
* api-change:``logs``: [``botocore``] Add ClientToken to QueryDefinition CFN Handler in CWL
* api-change:``s3``: [``botocore``] Fix an issue where the SDK can fail to unmarshall response due to NumberFormatException
* api-change:``servicediscovery``: [``botocore``] Adds a new DiscoverInstancesRevision API and also adds InstanceRevision field to the DiscoverInstances API response.
* api-change:``sso-oidc``: [``botocore``] Update FIPS endpoints in aws-us-gov.


1.28.51
=======

* api-change:``ec2``: [``botocore``] This release adds support for C7i, and R7a instance types.
* api-change:``outposts``: [``botocore``] This release adds the InstanceFamilies field to the ListAssets response.
* api-change:``sagemaker``: [``botocore``] This release adds support for one-time model monitoring schedules that are executed immediately without delay, explicit data analysis windows for model monitoring schedules and exclude features attributes to remove features from model monitor analysis.


1.28.50
=======

* api-change:``discovery``: [``botocore``] Add sensitive protection for customer information
* api-change:``macie2``: [``botocore``] This release changes the default managedDataIdentifierSelector setting for new classification jobs to RECOMMENDED. By default, new classification jobs now use the recommended set of managed data identifiers.
* api-change:``workmail``: [``botocore``] This release includes four new APIs UpdateUser, UpdateGroup, ListGroupsForEntity and DescribeEntity, along with RemoteUsers and some enhancements to existing APIs.


1.28.49
=======

* api-change:``appstream``: [``botocore``] This release introduces app block builder, allowing customers to provision a resource to package applications into an app block
* api-change:``connect``: [``botocore``] New rule type (OnMetricDataUpdate) has been added
* api-change:``datasync``: [``botocore``] Documentation-only updates for AWS DataSync.
* api-change:``sagemaker``: [``botocore``] This release introduces Skip Model Validation for Model Packages


1.28.48
=======

* api-change:``appstream``: [``botocore``] This release introduces multi-session fleets, allowing customers to provision more than one user session on a single fleet instance.
* api-change:``cloudformation``: [``botocore``] Documentation updates for AWS CloudFormation
* api-change:``entityresolution``: [``botocore``] Changed "ResolutionTechniques" and "MappedInputFields" in workflow and schema mapping operations to be required fields.
* api-change:``lookoutequipment``: [``botocore``] This release adds APIs for the new scheduled retraining feature.


1.28.47
=======

* api-change:``cloud9``: [``botocore``] Update to include information on Ubuntu 18 deprecation.
* api-change:``drs``: [``botocore``] Updated existing APIs and added new ones to support using AWS Elastic Disaster Recovery post-launch actions. Added support for new regions.
* api-change:``firehose``: [``botocore``] DocumentIdOptions has been added for the Amazon OpenSearch destination.
* api-change:``guardduty``: [``botocore``] Add `managementType` field to ListCoverage API response.
* api-change:``internetmonitor``: [``botocore``] This release updates the Amazon CloudWatch Internet Monitor API domain name.
* api-change:``ivs-realtime``: [``botocore``] Doc only update that changes description for ParticipantToken.
* api-change:``simspaceweaver``: [``botocore``] Edited the introductory text for the API reference.
* api-change:``xray``: [``botocore``] Add StartTime field in GetTraceSummaries API response for each TraceSummary.


1.28.46
=======

* api-change:``ec2``: [``botocore``] This release adds support for restricting public sharing of AMIs through AMI Block Public Access
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports confidence score buckets for retrieved passage results using the Retrieve API.


1.28.45
=======

* api-change:``ecr``: [``botocore``] This release will have ValidationException be thrown from ECR LifecyclePolicy APIs in regions LifecyclePolicy is not supported, this includes existing Amazon Dedicated Cloud (ADC) regions. This release will also change Tag: TagValue and Tag: TagKey to required.
* api-change:``medialive``: [``botocore``] AWS Elemental Link now supports attaching a Link UHD device to a MediaConnect flow.
* api-change:``quicksight``: [``botocore``] This release launches new updates to QuickSight KPI visuals - support for sparklines, new templated layout and new targets for conditional formatting rules.


1.28.44
=======

* api-change:``fsx``: [``botocore``] Amazon FSx documentation fixes
* api-change:``sagemaker``: [``botocore``] Autopilot APIs will now support holiday featurization for Timeseries models. The models will now hold holiday metadata and should be able to accommodate holiday effect during inference.
* api-change:``sso-admin``: [``botocore``] Content updates to IAM Identity Center API for China Regions.
* api-change:``workspaces``: [``botocore``] A new field "ErrorDetails" will be added to the output of "DescribeWorkspaceImages" API call. This field provides in-depth details about the error occurred during image import process. These details include the possible causes of the errors and troubleshooting information.


1.28.43
=======

* api-change:``neptunedata``: [``botocore``] Minor changes to send unsigned requests to Neptune clusters
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub
* api-change:``simspaceweaver``: [``botocore``] BucketName and ObjectKey are now required for the S3Location data type. BucketName is now required for the S3Destination data type.


1.28.42
=======

* api-change:``appflow``: [``botocore``] Adding OAuth2.0 support for servicenow connector.
* api-change:``ec2``: [``botocore``] This release adds 'outpost' location type to the DescribeInstanceTypeOfferings API, allowing customers that have been allowlisted for outpost to query their offerings in the API.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``medialive``: [``botocore``] Adds advanced Output Locking options for Epoch Locking: Custom Epoch and Jam Sync Time
* api-change:``wafv2``: [``botocore``] The targeted protection level of the Bot Control managed rule group now provides optional, machine-learning analysis of traffic statistics to detect some bot-related activity. You can enable or disable the machine learning functionality through the API.


1.28.41
=======

* api-change:``billingconductor``: [``botocore``] This release adds support for line item filtering in for the custom line item resource.
* api-change:``cloud9``: [``botocore``] Added support for Ubuntu 22.04 that was not picked up in a previous Trebuchet request. Doc-only update.
* api-change:``compute-optimizer``: [``botocore``] This release adds support to provide recommendations for G4dn and P3 instances that use NVIDIA GPUs.
* api-change:``ec2``: [``botocore``] Introducing Amazon EC2 C7gd, M7gd, and R7gd Instances with up to 3.8 TB of local NVMe-based SSD block-level storage. These instances are powered by AWS Graviton3 processors, delivering up to 25% better performance over Graviton2-based instances.
* api-change:``ecs``: [``botocore``] Documentation only update for Amazon ECS.
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``rds``: [``botocore``] Add support for feature integration with AWS Backup.
* api-change:``sagemaker``: [``botocore``] SageMaker Neo now supports data input shape derivation for Pytorch 2.0  and XGBoost compilation job for cloud instance targets. You can skip DataInputConfig field during compilation job creation. You can also access derived information from model in DescribeCompilationJob response.
* api-change:``vpc-lattice``: [``botocore``] This release adds Lambda event structure version config support for LAMBDA target groups. It also adds newline support for auth policies.


1.28.40
=======

* api-change:``chime-sdk-media-pipelines``: [``botocore``] This release adds support for the Voice Analytics feature for customer-owned KVS streams as part of the Amazon Chime SDK call analytics.
* api-change:``connect``: [``botocore``] Amazon Connect adds the ability to read, create, update, delete, and list view resources, and adds the ability to read, create, delete, and list view versions.
* api-change:``identitystore``: [``botocore``] New Identity Store content for China Region launch
* api-change:``neptunedata``: [``botocore``] Removed the descriptive text in the introduction.


1.28.39
=======

* api-change:``chime-sdk-media-pipelines``: [``botocore``] This release adds support for feature Voice Enhancement for Call Recording as part of Amazon Chime SDK call analytics.
* api-change:``cloudhsm``: [``botocore``] Deprecating CloudHSM Classic API Service.
* api-change:``connectcampaigns``: [``botocore``] Amazon Connect outbound campaigns has launched agentless dialing mode which enables customers to make automated outbound calls without agent engagement. This release updates three of the campaign management API's to support the new agentless dialing mode and the new dialing capacity field.
* api-change:``connectparticipant``: [``botocore``] Amazon Connect Participant Service adds the ability to get a view resource using a view token, which is provided in a participant message, with the release of the DescribeView API.
* api-change:``customer-profiles``: [``botocore``] Adds sensitive trait to various shapes in Customer Profiles API model.
* api-change:``ecs``: [``botocore``] This release adds support for an account-level setting that you can use to configure the number of days for AWS Fargate task retirement.
* api-change:``grafana``: [``botocore``] Marking SAML RoleValues attribute as sensitive and updating VpcConfiguration attributes to match documentation.
* api-change:``health``: [``botocore``] Adds new API DescribeEntityAggregatesForOrganization that retrieves entity aggregates across your organization. Also adds support for resource status filtering in DescribeAffectedEntitiesForOrganization, resource status aggregates in the DescribeEntityAggregates response, and new resource statuses.
* api-change:``ivs``: [``botocore``] Updated "type" description for CreateChannel, UpdateChannel, Channel, and ChannelSummary.
* api-change:``kafkaconnect``: [``botocore``] Minor model changes for Kafka Connect as well as endpoint updates.
* api-change:``payment-cryptography-data``: [``botocore``] Make KeyCheckValue field optional when using asymmetric keys as Key Check Values typically only apply to symmetric keys
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version


1.28.38
=======

* api-change:``appflow``: [``botocore``] Add SAP source connector parallel and pagination feature
* api-change:``apprunner``: [``botocore``] App Runner adds support for Bitbucket. You can now create App Runner connection that connects to your Bitbucket repositories and deploy App Runner service with the source code stored in a Bitbucket repository.
* api-change:``auditmanager``: [``botocore``] This release marks some assessment metadata as sensitive. We added a sensitive trait to the following attributes: assessmentName, emailAddress, scope, createdBy, lastUpdatedBy, and userName.
* api-change:``cleanrooms``: [``botocore``] This release decouples member abilities in a collaboration. With this change, the member who can run queries no longer needs to be the same as the member who can receive results.
* api-change:``datasync``: [``botocore``] AWS DataSync introduces Task Reports, a new feature that provides detailed reports of data transfer operations for each task execution.
* api-change:``neptunedata``: [``botocore``] Allows customers to execute data plane actions like bulk loading graphs, issuing graph queries using Gremlin and openCypher directly from the SDK.
* api-change:``network-firewall``: [``botocore``] Network Firewall increasing pagination token string length
* api-change:``pca-connector-ad``: [``botocore``] The Connector for AD allows you to use a fully-managed AWS Private CA as a drop-in replacement for your self-managed enterprise CAs without local agents or proxy servers. Enterprises that use AD to manage Windows environments can reduce their private certificate authority (CA) costs and complexity.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Canvas adds IdentityProviderOAuthSettings support for CanvasAppSettings


1.28.37
=======

* api-change:``cognito-idp``: [``botocore``] Added API example requests and responses for several operations. Fixed the validation regex for user pools Identity Provider name.
* api-change:``fsx``: [``botocore``] Documentation updates for project quotas.
* api-change:``omics``: [``botocore``] Add RetentionMode support for Runs.
* api-change:``sesv2``: [``botocore``] Adds support for the new Export and Message Insights features: create, get, list and cancel export jobs; get message insights.


1.28.36
=======

* api-change:``backup``: [``botocore``] Add support for customizing time zone for backup window in backup plan rules.
* api-change:``compute-optimizer``: [``botocore``] This release enables AWS Compute Optimizer to analyze and generate licensing optimization recommendations for sql server running on EC2 instances.
* api-change:``organizations``: [``botocore``] Documentation updates for permissions and links.
* api-change:``securitylake``: [``botocore``] Remove incorrect regex enforcement on pagination tokens.
* api-change:``service-quotas``: [``botocore``] Service Quotas now supports viewing the applied quota value and requesting a quota increase for a specific resource in an AWS account.
* api-change:``workspaces-web``: [``botocore``] WorkSpaces Web now enables Admins to configure which cookies are synchronized from an end-user's local browser to the in-session browser. In conjunction with a browser extension, this feature enables enhanced Single-Sign On capability by reducing the number of times an end-user has to authenticate.


1.28.35
=======

* api-change:``cloudtrail``: [``botocore``] Add ThrottlingException with error code 429 to handle CloudTrail Delegated Admin request rate exceeded on organization resources.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``detective``: [``botocore``] Added protections to interacting with fields containing customer information.


1.28.34
=======

* api-change:``ec2``: [``botocore``] Amazon EC2 M7a instances, powered by 4th generation AMD EPYC processors, deliver up to 50% higher performance compared to M6a instances. Amazon EC2 Hpc7a instances, powered by 4th Gen AMD EPYC processors, deliver up to 2.5x better performance compared to Amazon EC2 Hpc6a instances.
* api-change:``glue``: [``botocore``] Added API attributes that help in the monitoring of sessions.
* api-change:``mediaconvert``: [``botocore``] This release includes additional audio channel tags in Quicktime outputs, support for film grain synthesis for AV1 outputs, ability to create audio-only FLAC outputs, and ability to specify Amazon S3 destination storage class.
* api-change:``medialive``: [``botocore``] MediaLive now supports passthrough of KLV data to a HLS output group with a TS container. MediaLive now supports setting an attenuation mode for AC3 audio when the coding mode is 3/2 LFE. MediaLive now supports specifying whether to include filler NAL units in RTMP output group settings.
* api-change:``mediatailor``: [``botocore``] Adds new source location AUTODETECT_SIGV4 access type.
* api-change:``quicksight``: [``botocore``] Excel support in Snapshot Export APIs. Removed Required trait for some insight Computations. Namespace-shared Folders support. Global Filters support. Table pin Column support.
* api-change:``rds``: [``botocore``] This release updates the supported versions for Percona XtraBackup in Aurora MySQL.
* api-change:``s3control``: [``botocore``] Updates to endpoint ruleset tests to address Smithy validation issues and standardize the capitalization of DualStack.
* api-change:``verifiedpermissions``: [``botocore``] Documentation updates for Amazon Verified Permissions.


1.28.33
=======

* api-change:``apigateway``: [``botocore``] This release adds RootResourceId to GetRestApi response.
* api-change:``ec2``: [``botocore``] Marking fields as sensitive on BundleTask and GetPasswordData
* api-change:``polly``: [``botocore``] Amazon Polly adds 1 new voice - Zayd (ar-AE)


1.28.32
=======

* api-change:``ce``: [``botocore``] This release adds the LastUpdatedDate and LastUsedDate timestamps to help you manage your cost allocation tags.
* api-change:``globalaccelerator``: [``botocore``] Global Accelerator now supports Client Ip Preservation for Network Load Balancer endpoints.
* api-change:``rds``: [``botocore``] Adding parameters to CreateCustomDbEngineVersion reserved for future use.
* api-change:``verifiedpermissions``: [``botocore``] Documentation updates for Amazon Verified Permissions. Increases max results per page for ListPolicyStores, ListPolicies, and ListPolicyTemplates APIs from 20 to 50.


1.28.31
=======

* api-change:``cloud9``: [``botocore``] Doc only update to add Ubuntu 22.04 as an Image ID option for Cloud9
* api-change:``ec2``: [``botocore``] The DeleteKeyPair API has been updated to return the keyPairId when an existing key pair is deleted.
* api-change:``finspace``: [``botocore``] Allow customers to manage outbound traffic from their Kx Environment when attaching a transit gateway by providing network acl entries. Allow the customer to choose how they want to update the databases on a cluster allowing updates to possibly be faster than usual.
* api-change:``rds``: [``botocore``] Adding support for RDS Aurora Global Database Unplanned Failover
* api-change:``route53domains``: [``botocore``] Fixed typos in description fields


1.28.30
=======

* api-change:``codecommit``: [``botocore``] Add new ListFileCommitHistory operation to retrieve commits which introduced changes to a specific file.
* api-change:``securityhub``: [``botocore``] Added Inspector Lambda code Vulnerability section to ASFF, including GeneratorDetails, EpssScore, ExploitAvailable, and CodeVulnerabilities.


1.28.29
=======

* api-change:``ec2``: [``botocore``] Adds support for SubnetConfigurations to allow users to select their own IPv4 and IPv6 addresses for Interface VPC endpoints
* api-change:``gamelift``: [``botocore``] Amazon GameLift updates its instance types support.


1.28.28
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version


1.28.27
=======

* enhancement:Python: Added provisional Python 3.12 support to Boto3
* enhancement:Python: [``botocore``] Added provisional Python 3.12 support to Botocore
* api-change:``chime-sdk-meetings``: [``botocore``] Updated API documentation to include additional exceptions.
* api-change:``ec2``: [``botocore``] Documentation updates for Elastic Compute Cloud (EC2).
* api-change:``glue``: [``botocore``] AWS Glue Crawlers can now accept SerDe overrides from a custom csv classifier. The two SerDe options are LazySimpleSerDe and OpenCSVSerDe. In case, the user wants crawler to do the selection, "None" can be selected for this purpose.
* api-change:``pi``: [``botocore``] AWS Performance Insights for Amazon RDS is launching Performance Analysis On Demand, a new feature that allows you to analyze database performance metrics and find out the performance issues. You can now use SDK to create, list, get, delete, and manage tags of performance analysis reports.
* api-change:``route53domains``: [``botocore``] Provide explanation if CheckDomainTransferability return false. Provide requestId if a request is already submitted.  Add sensitive protection for customer information
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now provides SupportedResponseMIMETypes from DescribeInferenceRecommendationsJob response


1.28.26
=======

* api-change:``mediapackage``: [``botocore``] Fix SDK logging of certain fields.
* api-change:``omics``: [``botocore``] This release provides support for annotation store versioning and cross account sharing for Omics Analytics
* api-change:``transfer``: [``botocore``] Documentation updates for AWS Transfer Family


1.28.25
=======

* api-change:``amplifybackend``: [``botocore``] Adds sensitive trait to required input shapes.
* api-change:``config``: [``botocore``] Updated ResourceType enum with new resource types onboarded by AWS Config in July 2023.
* api-change:``ec2``: [``botocore``] Amazon EC2 P5 instances, powered by the latest NVIDIA H100 Tensor Core GPUs, deliver the highest performance in EC2 for deep learning (DL) and HPC applications. M7i-flex and M7i instances are next-generation general purpose instances powered by custom 4th Generation Intel Xeon Scalable processors.
* api-change:``quicksight``: [``botocore``] New Authentication method for Account subscription - IAM Identity Center. Hierarchy layout support, default column width support and related style properties for pivot table visuals. Non-additive topic field aggregations for Topic API
* api-change:``ses``: [``botocore``] Update ses client to latest version
* api-change:``swf``: [``botocore``] This release adds new API parameters to override workflow task list for workflow executions.


1.28.24
=======

* api-change:``cloudtrail``: [``botocore``] Documentation updates for CloudTrail.
* api-change:``connect``: [``botocore``] This release adds APIs to provision agents that are global / available in multiple AWS regions and distribute them across these regions by percentage.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``omics``: [``botocore``] This release adds instanceType to GetRunTask & ListRunTasks responses.
* api-change:``secretsmanager``: [``botocore``] Add additional InvalidRequestException to list of possible exceptions for ListSecret.
* api-change:``transfer``: [``botocore``] Documentation updates for AW Transfer Family


1.28.23
=======

* api-change:``chime-sdk-voice``: [``botocore``] Updating CreatePhoneNumberOrder, UpdatePhoneNumber and BatchUpdatePhoneNumbers APIs, adding phone number name
* api-change:``fsx``: [``botocore``] For FSx for Lustre, add new data repository task type, RELEASE_DATA_FROM_FILESYSTEM, to release files that have been archived to S3. For FSx for Windows, enable support for configuring and updating SSD IOPS, and for updating storage type. For FSx for OpenZFS, add new deployment type, MULTI_AZ_1.
* api-change:``globalaccelerator``: [``botocore``] Documentation update for dualstack EC2 endpoint support
* api-change:``guardduty``: [``botocore``] Added autoEnable ALL to UpdateOrganizationConfiguration and DescribeOrganizationConfiguration APIs.
* api-change:``sagemaker``: [``botocore``] This release adds support for cross account access for SageMaker Model Cards through AWS RAM.


1.28.22
=======

* api-change:``backup``: [``botocore``] This release introduces a new logically air-gapped vault (Preview) in AWS Backup that stores immutable backup copies, which are locked by default and isolated with encryption using AWS owned keys. Logically air-gapped vault (Preview) allows secure recovery of application data across accounts.
* api-change:``elasticache``: [``botocore``] Added support for cluster mode in online migration and test migration API
* api-change:``servicecatalog``: [``botocore``] Introduce support for HashiCorp Terraform Cloud in Service Catalog by addying TERRAFORM_CLOUD product type in CreateProduct and CreateProvisioningArtifact API.


1.28.21
=======

* api-change:``detective``: [``botocore``] Updated the email validation regex to be in line with the TLD name specifications.
* api-change:``ivs-realtime``: [``botocore``] Add QUOTA_EXCEEDED and PUBLISHER_NOT_FOUND to EventErrorCode for stage health events.
* api-change:``kinesis-video-archived-media``: [``botocore``] This release enables minimum of Images SamplingInterval to be as low as 200 milliseconds in Kinesis Video Stream Image feature.
* api-change:``kinesisvideo``: [``botocore``] This release enables minimum of Images SamplingInterval to be as low as 200 milliseconds in Kinesis Video Stream Image feature.
* api-change:``rekognition``: [``botocore``] This release adds code snippets for Amazon Rekognition Custom Labels.


1.28.20
=======

* api-change:``acm-pca``: [``botocore``] Documentation correction for AWS Private CA
* api-change:``connect``: [``botocore``] Added a new API UpdateRoutingProfileAgentAvailabilityTimer to update agent availability timer of a routing profile.
* api-change:``datasync``: [``botocore``] Display cloud storage used capacity at a cluster level.
* api-change:``ecs``: [``botocore``] This is a documentation update to address various tickets.
* api-change:``sagemaker``: [``botocore``] Including DataCaptureConfig key in the Amazon Sagemaker Search's transform job object


1.28.19
=======

* api-change:``autoscaling``: [``botocore``] Documentation changes related to Amazon EC2 Auto Scaling APIs.
* api-change:``cloud9``: [``botocore``] Updated the deprecation date for Amazon Linux. Doc only update.
* api-change:``dms``: [``botocore``] The release makes public API for DMS Schema Conversion feature.
* api-change:``ec2``: [``botocore``] This release adds new parameter isPrimaryIPv6 to  allow assigning an IPv6 address as a primary IPv6 address to a network interface which cannot be changed to give equivalent functionality available for network interfaces with primary IPv4 address.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker now supports running training jobs on p5.48xlarge instance types.


1.28.18
=======

* api-change:``budgets``: [``botocore``] As part of CAE tagging integration we need to update our budget names regex filter to prevent customers from using "/action/" in their budget names.
* api-change:``cognito-idp``: [``botocore``] New feature that logs Cognito user pool error messages to CloudWatch logs.
* api-change:``glue``: [``botocore``] This release includes additional Glue Streaming KAKFA SASL property types.
* api-change:``resiliencehub``: [``botocore``] Drift Detection capability added when applications policy has moved from a meet to breach state. Customers will be able to exclude operational recommendations and receive credit in their resilience score. Customers can now add ARH permissions to an existing or new role.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender introduces a new API GetScalingConfigurationRecommendation to recommend auto scaling policies based on completed Inference Recommender jobs.


1.28.17
=======

* api-change:``batch``: [``botocore``] This release adds support for price capacity optimized allocation strategy for Spot Instances.
* api-change:``dms``: [``botocore``] Adding new API describe-engine-versions which provides information about the lifecycle of a replication instance's version.
* api-change:``internetmonitor``: [``botocore``] This release adds a new feature for Amazon CloudWatch Internet Monitor that enables customers to set custom thresholds, for performance and availability drops, for impact limited to a single city-network to trigger creation of a health event.
* api-change:``medialive``: [``botocore``] AWS Elemental Link devices now report their Availability Zone. Link devices now support the ability to change their Availability Zone.
* api-change:``polly``: [``botocore``] Amazon Polly adds new French Belgian voice - Isabelle. Isabelle is available as Neural voice only.
* api-change:``rds``: [``botocore``] Added support for deleted clusters PiTR.
* api-change:``sagemaker``: [``botocore``] Add Stairs TrafficPattern and FlatInvocations to RecommendationJobStoppingConditions


1.28.16
=======

* api-change:``amplifyuibuilder``: [``botocore``] Amplify Studio releases GraphQL support for codegen job action.
* api-change:``autoscaling``: [``botocore``] You can now configure an instance refresh to set its status to 'failed' when it detects that a specified CloudWatch alarm has gone into the ALARM state. You can also choose to roll back the instance refresh automatically when the alarm threshold is met.
* api-change:``cleanrooms``: [``botocore``] This release introduces custom SQL queries - an expanded set of SQL you can run. This release adds analysis templates, a new resource for storing pre-defined custom SQL queries ahead of time. This release also adds the Custom analysis rule, which lets you approve analysis templates for querying.
* api-change:``codestar-connections``: [``botocore``] New integration with the Gitlab provider type.
* api-change:``drs``: [``botocore``] Add support for in-aws right sizing
* api-change:``inspector2``: [``botocore``] This release adds 1 new API: BatchGetFindingDetails to retrieve enhanced vulnerability intelligence details for findings.
* api-change:``lookoutequipment``: [``botocore``] This release includes new import resource, model versioning and resource policy features.
* api-change:``omics``: [``botocore``] Add CreationType filter for ListReadSets
* api-change:``rds``: [``botocore``] This release adds support for Aurora MySQL local write forwarding, which allows for forwarding of write operations from reader DB instances to the writer DB instance.
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Israel (Tel Aviv) Region (il-central-1) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``scheduler``: [``botocore``] This release introduces automatic deletion of schedules in EventBridge Scheduler. If configured, EventBridge Scheduler automatically deletes a schedule after the schedule has completed its last invocation.


1.28.15
=======

* enhancement:HTTP: [``botocore``] Move 100-continue behavior to use `HTTPConnections` request interface.
* api-change:``application-insights``: [``botocore``] This release enable customer to add/remove/update more than one workload for a component
* api-change:``cloudformation``: [``botocore``] This SDK release is for the feature launch of AWS CloudFormation RetainExceptOnCreate. It adds a new parameter retainExceptOnCreate in the following APIs: CreateStack, UpdateStack, RollbackStack, ExecuteChangeSet.
* api-change:``cloudfront``: [``botocore``] Add a new JavaScript runtime version for CloudFront Functions.
* api-change:``connect``: [``botocore``] This release adds support for new number types.
* api-change:``kafka``: [``botocore``] Amazon MSK has introduced new versions of ListClusterOperations and DescribeClusterOperation APIs. These v2 APIs provide information and insights into the ongoing operations of both MSK Provisioned and MSK Serverless clusters.
* api-change:``pinpoint``: [``botocore``] Added support for sending push notifications using the FCM v1 API with json credentials. Amazon Pinpoint customers can now deliver messages to Android devices using both FCM v1 API and the legacy FCM/GCM API


1.28.14
=======

* enhancement:compression: [``botocore``] Adds support for the ``requestcompression`` operation trait.
* api-change:``sqs``: [``botocore``] Documentation changes related to SQS APIs.


1.28.13
=======

* api-change:``autoscaling``: [``botocore``] This release updates validation for instance types used in the AllowedInstanceTypes and ExcludedInstanceTypes parameters of the InstanceRequirements property of a MixedInstancesPolicy.
* api-change:``ebs``: [``botocore``] SDK and documentation updates for Amazon Elastic Block Store API
* api-change:``ec2``: [``botocore``] SDK and documentation updates for Amazon Elastic Block Store APIs
* api-change:``eks``: [``botocore``] Add multiple customer error code to handle customer caused failure when managing EKS node groups
* api-change:``sagemaker``: [``botocore``] Expose ProfilerConfig attribute in SageMaker Search API response.


1.28.12
=======

* api-change:``cloudcontrol``: [``botocore``] Updates the documentation for CreateResource.
* api-change:``entityresolution``: [``botocore``] AWS Entity Resolution can effectively match a source record from a customer relationship management (CRM) system with a source record from a marketing system containing campaign information.
* api-change:``glue``: [``botocore``] Release Glue Studio Snowflake Connector Node for SDK/CLI
* api-change:``healthlake``: [``botocore``] Updating the HealthLake service documentation.
* api-change:``managedblockchain-query``: [``botocore``] Amazon Managed Blockchain (AMB) Query provides serverless access to standardized, multi-blockchain datasets with developer-friendly APIs.
* api-change:``mediaconvert``: [``botocore``] This release includes general updates to user documentation.
* api-change:``omics``: [``botocore``] The service is renaming as a part of AWS Health.
* api-change:``opensearchserverless``: [``botocore``] This release adds new collection type VectorSearch.
* api-change:``polly``: [``botocore``] Amazon Polly adds 1 new voice - Lisa (nl-BE)
* api-change:``route53``: [``botocore``] Update that corrects the documents for received feedback.


1.28.11
=======

* api-change:``billingconductor``: [``botocore``] Added support for Auto-Assocate Billing Groups for CreateBillingGroup, UpdateBillingGroup, and ListBillingGroups.
* api-change:``customer-profiles``: [``botocore``] Amazon Connect Customer Profiles now supports rule-based resolution to match and merge similar profiles into unified profiles, helping companies deliver faster and more personalized customer service by providing access to relevant customer information for agents and automated experiences.
* api-change:``datasync``: [``botocore``] AWS DataSync now supports Microsoft Azure Blob Storage locations.
* api-change:``dynamodb``: [``botocore``] Documentation updates for DynamoDB
* api-change:``ec2``: [``botocore``] This release adds an instance's peak and baseline network bandwidth as well as the memory sizes of an instance's inference accelerators to DescribeInstanceTypes.
* api-change:``emr-serverless``: [``botocore``] This release adds support for publishing application logs to CloudWatch.
* api-change:``lambda``: [``botocore``] Add Python 3.11 (python3.11) support to AWS Lambda
* api-change:``rds``: [``botocore``] This release adds support for monitoring storage optimization progress on the DescribeDBInstances API.
* api-change:``sagemaker``: [``botocore``] Mark ContentColumn and TargetLabelColumn as required Targets in TextClassificationJobConfig in CreateAutoMLJobV2API
* api-change:``securityhub``: [``botocore``] Add support for CONTAINS and NOT_CONTAINS comparison operators for Automation Rules string filters and map filters
* api-change:``sts``: [``botocore``] API updates for the AWS Security Token Service
* api-change:``transfer``: [``botocore``] This release adds support for SFTP Connectors.
* api-change:``wisdom``: [``botocore``] This release added two new data types: AssistantIntegrationConfiguration, and SessionIntegrationConfiguration to support Wisdom integration with Amazon Connect Chat


1.28.10
=======

* api-change:``apigatewayv2``: [``botocore``] Documentation updates for Amazon API Gateway.
* api-change:``ce``: [``botocore``] This release introduces the new API 'GetSavingsPlanPurchaseRecommendationDetails', which retrieves the details for a Savings Plan recommendation. It also updates the existing API 'GetSavingsPlansPurchaseRecommendation' to include the recommendation detail ID.
* api-change:``chime-sdk-media-pipelines``: [``botocore``] AWS Media Pipeline compositing enhancement and Media Insights Pipeline auto language identification.
* api-change:``cloudformation``: [``botocore``] This release supports filtering by DRIFT_STATUS for existing API ListStackInstances and adds support for a new API ListStackInstanceResourceDrifts. Customers can now view resource drift information from their StackSet management accounts.
* api-change:``ec2``: [``botocore``] Add "disabled" enum value to SpotInstanceState.
* api-change:``glue``: [``botocore``] Added support for Data Preparation Recipe node in Glue Studio jobs
* api-change:``quicksight``: [``botocore``] This release launches new Snapshot APIs for CSV and PDF exports, adds support for info icon for filters and parameters in Exploration APIs, adds modeled exception to the DeleteAccountCustomization API, and introduces AttributeAggregationFunction's ability to add UNIQUE_VALUE aggregation in tooltips.


1.28.9
======

* api-change:``glue``: [``botocore``] This release adds support for AWS Glue Crawler with Apache Hudi Tables, allowing Crawlers to discover Hudi Tables in S3 and register them in Glue Data Catalog for query engines to query against.
* api-change:``mediaconvert``: [``botocore``] This release includes improvements to Preserve 444 handling, compatibility of HEVC sources without frame rates, and general improvements to MP4 outputs.
* api-change:``rds``: [``botocore``] Adds support for the DBSystemID parameter of CreateDBInstance to RDS Custom for Oracle.
* api-change:``workspaces``: [``botocore``] Fixed VolumeEncryptionKey descriptions


1.28.8
======

* api-change:``codecatalyst``: [``botocore``] This release adds support for updating and deleting spaces and projects in Amazon CodeCatalyst. It also adds support for creating, getting, and deleting source repositories in CodeCatalyst projects.
* api-change:``connectcases``: [``botocore``] This release adds the ability to assign a case to a queue or user.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``route53resolver``: [``botocore``] This release adds support for Route 53 On Outposts, a new feature that allows customers to run Route 53 Resolver and Resolver endpoints locally on their Outposts.
* api-change:``s3``: [``botocore``] Improve performance of S3 clients by simplifying and optimizing endpoint resolution.
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Cross account support for SageMaker Feature Store
* api-change:``sagemaker``: [``botocore``] Cross account support for SageMaker Feature Store
* api-change:``securitylake``: [``botocore``] Adding support for Tags on Create and Resource Tagging API.
* api-change:``transcribe``: [``botocore``] Added API argument --toxicity-detection to startTranscriptionJob API, which allows users to view toxicity scores of submitted audio.


1.28.7
======

* enhancement:AWSCRT: [``botocore``] Upgrade awscrt version to 0.16.26
* api-change:``savingsplans``: [``botocore``] Savings Plans endpoints update


1.28.6
======

* api-change:``cloudformation``: [``botocore``] SDK and documentation updates for GetTemplateSummary API (unrecognized resources)
* api-change:``ec2``: [``botocore``] Amazon EC2 documentation updates.
* api-change:``grafana``: [``botocore``] Amazon Managed Grafana now supports grafanaVersion update for existing workspaces with UpdateWorkspaceConfiguration API. DescribeWorkspaceConfiguration API additionally returns grafanaVersion. A new ListVersions API lists available versions or, if given a workspaceId, the versions it can upgrade to.
* api-change:``medical-imaging``: [``botocore``] General Availability (GA) release of AWS Health Imaging, enabling customers to store, transform, and analyze medical imaging data at petabyte-scale.
* api-change:``ram``: [``botocore``] This release adds support for securely sharing with AWS service principals.
* api-change:``ssm-sap``: [``botocore``] Added support for SAP Hana High Availability discovery (primary and secondary nodes) and Backint agent installation with SSM for SAP.
* api-change:``wafv2``: [``botocore``] Added the URI path to the custom aggregation keys that you can specify for a rate-based rule.


1.28.5
======

* api-change:``codeguru-security``: [``botocore``] Documentation updates for CodeGuru Security.
* api-change:``connect``: [``botocore``] GetMetricDataV2 API: Update to include Contact Lens Conversational Analytics Metrics
* api-change:``es``: [``botocore``] Regex Validation on the ElasticSearch Engine Version attribute
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``m2``: [``botocore``] Allows UpdateEnvironment to update the environment to 0 host capacity. New GetSignedBluinsightsUrl API
* api-change:``snowball``: [``botocore``] Adds support for RACK_5U_C. This is the first AWS Snow Family device designed to meet U.S. Military Ruggedization Standards (MIL-STD-810H) with 208 vCPU device in a portable, compact 5U, half-rack width form-factor.
* api-change:``translate``: [``botocore``] Added DOCX word document support to TranslateDocument API


1.28.4
======

* api-change:``codeartifact``: [``botocore``] Doc only update for AWS CodeArtifact
* api-change:``docdb``: [``botocore``] Added major version upgrade option in ModifyDBCluster API
* api-change:``ec2``: [``botocore``] Add Nitro TPM support on DescribeInstanceTypes
* api-change:``glue``: [``botocore``] Adding new supported permission type flags to get-unfiltered endpoints that callers may pass to indicate support for enforcing Lake Formation fine-grained access control on nested column attributes.
* api-change:``ivs``: [``botocore``] This release provides the flexibility to configure what renditions or thumbnail qualities to record when creating recording configuration.
* api-change:``lakeformation``: [``botocore``] Adds supports for ReadOnlyAdmins and AllowFullTableExternalDataAccess. Adds NESTED_PERMISSION and NESTED_CELL_PERMISSION to SUPPORTED_PERMISSION_TYPES enum. Adds CREATE_LF_TAG on catalog resource and ALTER, DROP, and GRANT_WITH_LF_TAG_EXPRESSION on LF Tag resource.


1.28.3
======

* api-change:``cognito-idp``: [``botocore``] API model updated in Amazon Cognito
* api-change:``connect``: [``botocore``] Add support for deleting Queues and Routing Profiles.
* api-change:``datasync``: [``botocore``] Added LunCount to the response object of DescribeStorageSystemResourcesResponse, LunCount represents the number of LUNs on a storage system resource.
* api-change:``dms``: [``botocore``] Enhanced PostgreSQL target endpoint settings for providing Babelfish support.
* api-change:``ec2``: [``botocore``] This release adds support for the C7gn and Hpc7g instances. C7gn instances are powered by AWS Graviton3 processors and the fifth-generation AWS Nitro Cards. Hpc7g instances are powered by AWS Graviton 3E processors and provide up to 200 Gbps network bandwidth.
* api-change:``fsx``: [``botocore``] Amazon FSx for NetApp ONTAP now supports SnapLock, an ONTAP feature that enables you to protect your files in a volume by transitioning them to a write once, read many (WORM) state.
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``mediatailor``: [``botocore``] Adds categories to MediaTailor channel assembly alerts
* api-change:``personalize``: [``botocore``] This release provides ability to customers to change schema associated with their datasets in Amazon Personalize
* api-change:``proton``: [``botocore``] This release adds support for deployment history for Proton provisioned resources
* api-change:``s3``: [``botocore``] S3 Inventory now supports Object Access Control List and Object Owner as available object metadata fields in inventory reports.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Canvas adds WorkspeceSettings support for CanvasAppSettings
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager


1.28.2
======

* bugfix:s3: [``botocore``] Fix s3 presigned URLs for operations with query components (`#2962 <https://github.com/boto/botocore/issues/2962>`__)
* api-change:``cognito-idp``: [``botocore``] API model updated in Amazon Cognito


1.28.1
======

* api-change:``dms``: [``botocore``] Releasing DMS Serverless. Adding support for PostgreSQL 15.x as source and target endpoint. Adding support for DocDB Elastic Clusters with sharded collections, PostgreSQL datatype mapping customization and disabling hostname validation of the certificate authority in Kafka endpoint settings
* api-change:``glue``: [``botocore``] This release enables customers to create new Apache Iceberg tables and associated metadata in Amazon S3 by using native AWS Glue CreateTable operation.
* api-change:``logs``: [``botocore``] Add CMK encryption support for CloudWatch Logs Insights query result data
* api-change:``medialive``: [``botocore``] This release enables the use of Thumbnails in AWS Elemental MediaLive.
* api-change:``mediatailor``: [``botocore``] The AWS Elemental MediaTailor SDK for Channel Assembly has added support for EXT-X-CUE-OUT and EXT-X-CUE-IN tags to specify ad breaks in HLS outputs, including support for EXT-OATCLS, EXT-X-ASSET, and EXT-X-CUE-OUT-CONT accessory tags.


1.28.0
======

* enhancement:configprovider: [``botocore``] Always use shallow copy of session config value store for clients
* feature:configuration: [``botocore``] Configure the endpoint URL in the shared configuration file or via an environment variable for a specific AWS service or all AWS services.
* bugfix:configprovider: [``botocore``] Fix bug when deep copying config value store where overrides were not preserved
* api-change:``ec2``: [``botocore``] Add Nitro Enclaves support on DescribeInstanceTypes
* api-change:``location``: [``botocore``] This release adds support for authenticating with Amazon Location Service's Places & Routes APIs with an API Key. Also, with this release developers can publish tracked device position updates to Amazon EventBridge.
* api-change:``outposts``: [``botocore``] Added paginator support to several APIs. Added the ISOLATED enum value to AssetState.
* api-change:``quicksight``: [``botocore``] This release includes below three changes: small multiples axes improvement, field based coloring, removed required trait from Aggregation function for TopBottomFilter.
* api-change:``rds``: [``botocore``] Updates Amazon RDS documentation for creating DB instances and creating Aurora global clusters.


1.27.1
======

* api-change:``comprehendmedical``: [``botocore``] Update to Amazon Comprehend Medical documentation.
* api-change:``connect``: [``botocore``] GetMetricDataV2 API: Channels filters do not count towards overall limitation of 100 filter values.
* api-change:``kms``: [``botocore``] Added Dry Run Feature to cryptographic and cross-account mutating KMS APIs (14 in all). This feature allows users to test their permissions and parameters before making the actual API call.
* api-change:``mgn``: [``botocore``] This release introduces the Global view feature and new Replication state APIs.
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub


1.27.0
======

* feature:Useragent: [``botocore``] Update User-Agent header format
* api-change:``batch``: [``botocore``] This feature allows customers to use AWS Batch with Linux with ARM64 CPU Architecture and X86_64 CPU Architecture with Windows OS on Fargate Platform.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now accepts new fields SupportedEndpointType and ServerlessConfiguration to support serverless endpoints.


1.26.165
========

* api-change:``amp``: [``botocore``] AWS SDK service model  generation tool version upgrade.
* api-change:``ecs``: [``botocore``] Added new field  "credentialspecs" to the ecs task definition to support gMSA of windows/linux in both domainless and domain-joined mode
* api-change:``ivs``: [``botocore``] Corrects the HTTP response code in the generated docs for PutMetadata and DeleteRecordingConfiguration APIs.
* api-change:``mediaconvert``: [``botocore``] This release includes improved color handling of overlays and general updates to user documentation.
* api-change:``sagemaker``: [``botocore``] This release adds support for rolling deployment in SageMaker Inference.
* api-change:``transfer``: [``botocore``] Add outbound Basic authentication support to AS2 connectors
* api-change:``verifiedpermissions``: [``botocore``] This release corrects several broken links in the documentation.


1.26.164
========

* api-change:``appstream``: [``botocore``] This release introduces app block builder, allowing customers to provision a resource to package applications into an app block
* api-change:``chime``: [``botocore``] The Amazon Chime SDK APIs in the Chime namespace are no longer supported.  Customers should use APIs in the dedicated Amazon Chime SDK namespaces: ChimeSDKIdentity, ChimeSDKMediaPipelines, ChimeSDKMeetings, ChimeSDKMessaging, and ChimeSDKVoice.
* api-change:``cleanrooms``: [``botocore``] This release adds support for the OR operator in RSQL join match conditions and the ability to control which operators (AND, OR) are allowed in a join match condition.
* api-change:``dynamodb``: [``botocore``] This release adds ReturnValuesOnConditionCheckFailure parameter to PutItem, UpdateItem, DeleteItem, ExecuteStatement, BatchExecuteStatement and ExecuteTransaction APIs. When set to ALL_OLD,  API returns a copy of the item as it was when a conditional write failed
* api-change:``gamelift``: [``botocore``] Amazon GameLift now supports game builds that use the Amazon Linux 2023 (AL2023) operating system.
* api-change:``glue``: [``botocore``] This release adds support for AWS Glue Crawler with Iceberg Tables, allowing Crawlers to discover Iceberg Tables in S3 and register them in Glue Data Catalog for query engines to query against.
* api-change:``sagemaker``: [``botocore``] Adding support for timeseries forecasting in the CreateAutoMLJobV2 API.


1.26.163
========

* api-change:``internetmonitor``: [``botocore``] This release adds a new feature for Amazon CloudWatch Internet Monitor that enables customers to set custom thresholds, for performance and availability drops, for triggering when to create a health event.
* api-change:``kinesisanalyticsv2``: [``botocore``] Support for new runtime environment in Kinesis Data Analytics Studio: Zeppelin-0.10, Apache Flink-1.15
* api-change:``lambda``: [``botocore``] Surface ResourceConflictException in DeleteEventSourceMapping
* api-change:``omics``: [``botocore``] Add Common Workflow Language (CWL) as a supported language for Omics workflows
* api-change:``rds``: [``botocore``] Amazon Relational Database Service (RDS) now supports joining a RDS for SQL Server instance to a self-managed Active Directory.
* api-change:``s3``: [``botocore``] The S3 LISTObjects, ListObjectsV2 and ListObjectVersions API now supports a new optional header x-amz-optional-object-attributes. If header contains RestoreStatus as the value, then S3 will include Glacier restore status i.e. isRestoreInProgress and RestoreExpiryDate in List response.
* api-change:``sagemaker``: [``botocore``] This release adds support for Model Cards Model Registry integration.


1.26.162
========

* bugfix:Parsers: [``botocore``] Fixes datetime parse error handling for out-of-range and negative timestamps (`#2564 <https://github.com/boto/botocore/issues/2564>`__).
* api-change:``appfabric``: [``botocore``] Initial release of AWS AppFabric for connecting SaaS applications for better productivity and security.
* api-change:``appflow``: [``botocore``] This release adds support to bypass SSO with the SAPOData connector when connecting to an SAP instance.
* api-change:``emr-serverless``: [``botocore``] This release adds support to update the release label of an EMR Serverless application to upgrade it to a different version of Amazon EMR via UpdateApplication API.
* api-change:``ivs``: [``botocore``] IVS customers can now revoke the viewer session associated with an auth token, to prevent and stop playback using that token.
* api-change:``kinesisvideo``: [``botocore``] General Availability (GA) release of Kinesis Video Streams at Edge, enabling customers to provide a configuration for the Kinesis Video Streams EdgeAgent running on an on-premise IoT device. Customers can now locally record from cameras and stream videos to the cloud on a configured schedule.
* api-change:``macie2``: [``botocore``] This release adds support for configuring new classification jobs to use the set of managed data identifiers that we recommend for jobs. For the managed data identifier selection type (managedDataIdentifierSelector), specify RECOMMENDED.
* api-change:``privatenetworks``: [``botocore``] This release allows Private5G customers to choose different commitment plans (60-days, 1-year, 3-years) when placing new orders, enables automatic renewal option for 1-year and 3-years commitments. It also allows customers to update the commitment plan of an existing radio unit.
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] Introducing TTL for online store records for feature groups.
* api-change:``sagemaker``: [``botocore``] Introducing TTL for online store records in feature groups.
* api-change:``ssm``: [``botocore``] Systems Manager doc-only update for June 2023.
* api-change:``verifiedpermissions``: [``botocore``] This update fixes several broken links to the Cedar documentation.


1.26.161
========

* api-change:``connect``: [``botocore``] This release provides a way to search for existing tags within an instance. Before tagging a resource, ensure consistency by searching for pre-existing key:value pairs.
* api-change:``glue``: [``botocore``] Timestamp Starting Position For Kinesis and Kafka Data Sources in a Glue Streaming Job
* api-change:``guardduty``: [``botocore``] Add support for user.extra.sessionName in Kubernetes Audit Logs Findings.
* api-change:``iam``: [``botocore``] Support for a new API "GetMFADevice" to present MFA device metadata such as device certifications
* api-change:``pinpoint``: [``botocore``] Added time zone estimation support for journeys


1.26.160
========

* api-change:``devops-guru``: [``botocore``] This release adds support for encryption via customer managed keys.
* api-change:``fsx``: [``botocore``] Update to Amazon FSx documentation.
* api-change:``rds``: [``botocore``] Documentation improvements for create, describe, and modify DB clusters and DB instances.
* api-change:``verifiedpermissions``: [``botocore``] Added improved descriptions and new code samples to SDK documentation.


1.26.159
========

* api-change:``chime-sdk-identity``: [``botocore``] AppInstanceBots can be configured to be invoked or not using the Target or the CHIME.mentions attribute for ChannelMessages
* api-change:``chime-sdk-messaging``: [``botocore``] ChannelMessages can be made visible to sender and intended recipient rather than all channel members with the target attribute. For example, a user can send messages to a bot and receive messages back in a group channel without other members seeing them.
* api-change:``kendra``: [``botocore``] Introducing Amazon Kendra Retrieve API that can be used to retrieve relevant passages or text excerpts given an input query.
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version


1.26.158
========

* api-change:``dynamodb``: [``botocore``] Documentation updates for DynamoDB
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``inspector2``: [``botocore``] This release adds support for Software Bill of Materials (SBOM) export and the general availability of code scanning for AWS Lambda functions.
* api-change:``mediaconvert``: [``botocore``] This release introduces the bandwidth reduction filter for the HEVC encoder, increases the limits of outputs per job, and updates support for the Nagra SDK to version 1.14.7.
* api-change:``mq``: [``botocore``] The Cross Region Disaster Recovery feature allows to replicate a brokers state from one region to another in order to provide customers with multi-region resiliency in the event of a regional outage.
* api-change:``sagemaker``: [``botocore``] This release provides support in SageMaker for output files in training jobs to be uploaded without compression and enable customer to deploy uncompressed model from S3 to real-time inference Endpoints. In addition, ml.trn1n.32xlarge is added to supported instance type list in training job.
* api-change:``transfer``: [``botocore``] This release adds a new parameter StructuredLogDestinations to CreateServer, UpdateServer APIs.


1.26.157
========

* api-change:``appflow``: [``botocore``] This release adds new API to reset connector metadata cache
* api-change:``config``: [``botocore``] Updated ResourceType enum with new resource types onboarded by AWS Config in May 2023.
* api-change:``ec2``: [``botocore``] Adds support for targeting Dedicated Host allocations by assetIds in AWS Outposts
* api-change:``lambda``: [``botocore``] This release adds RecursiveInvocationException to the Invoke API and InvokeWithResponseStream API.
* api-change:``redshift``: [``botocore``] Added support for custom domain names for Redshift Provisioned clusters. This feature enables customers to create a custom domain name and use ACM to generate fully secure connections to it.


1.26.156
========

* api-change:``cloudformation``: [``botocore``] Specify desired CloudFormation behavior in the event of ChangeSet execution failure using the CreateChangeSet OnStackFailure parameter
* api-change:``ec2``: [``botocore``] API changes to AWS Verified Access to include data from trust providers in logs
* api-change:``ecs``: [``botocore``] Documentation only update to address various tickets.
* api-change:``glue``: [``botocore``] This release adds support for creating cross region table/database resource links
* api-change:``pricing``: [``botocore``] This release updates the PriceListArn regex pattern.
* api-change:``route53domains``: [``botocore``] Update MaxItems upper bound to 1000 for ListPricesRequest
* api-change:``sagemaker``: [``botocore``] Amazon Sagemaker Autopilot releases CreateAutoMLJobV2 and DescribeAutoMLJobV2 for Autopilot customers with ImageClassification, TextClassification and Tabular problem type config support.


1.26.155
========

* api-change:``account``: [``botocore``] Improve pagination support for ListRegions
* api-change:``connect``: [``botocore``] Updates the *InstanceStorageConfig APIs to support a new ResourceType: SCREEN_RECORDINGS to enable screen recording and specify the storage configurations for publishing the recordings. Also updates DescribeInstance and ListInstances APIs to include InstanceAccessUrl attribute in the API response.
* api-change:``discovery``: [``botocore``] Add Amazon EC2 instance recommendations export
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``s3``: [``botocore``] This release adds SDK support for request-payer request header and request-charged response header in the "GetBucketAccelerateConfiguration", "ListMultipartUploads", "ListObjects", "ListObjectsV2" and "ListObjectVersions" S3 APIs.


1.26.154
========

* api-change:``auditmanager``: [``botocore``] This release introduces 2 Audit Manager features: CSV exports and new manual evidence options. You can now export your evidence finder results in CSV format. In addition, you can now add manual evidence to a control by entering free-form text or uploading a file from your browser.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``guardduty``: [``botocore``] Updated descriptions for some APIs.
* api-change:``location``: [``botocore``] Amazon Location Service adds categories to places, including filtering on those categories in searches. Also, you can now add metadata properties to your geofences.


1.26.153
========

* api-change:``cloudtrail``: [``botocore``] This feature allows users to view dashboards for CloudTrail Lake event data stores.
* api-change:``codeguru-security``: [``botocore``] Initial release of Amazon CodeGuru Security APIs
* api-change:``drs``: [``botocore``] Added APIs to support network replication and recovery using AWS Elastic Disaster Recovery.
* api-change:``ec2``: [``botocore``] This release introduces a new feature, EC2 Instance Connect Endpoint, that enables you to connect to a resource over TCP, without requiring the resource to have a public IPv4 address.
* api-change:``imagebuilder``: [``botocore``] Change the Image Builder ImagePipeline dateNextRun field to more accurately describe the data.
* api-change:``lightsail``: [``botocore``] This release adds pagination for the Get Certificates API operation.
* api-change:``s3``: [``botocore``] Integrate double encryption feature to SDKs.
* api-change:``securityhub``: [``botocore``] Add support for Security Hub Automation Rules
* api-change:``simspaceweaver``: [``botocore``] This release fixes using aws-us-gov ARNs in API calls and adds documentation for snapshot APIs.
* api-change:``verifiedpermissions``: [``botocore``] GA release of Amazon Verified Permissions.
* api-change:``wafv2``: [``botocore``] You can now detect and block fraudulent account creation attempts with the new AWS WAF Fraud Control account creation fraud prevention (ACFP) managed rule group AWSManagedRulesACFPRuleSet.
* api-change:``wellarchitected``: [``botocore``] AWS Well-Architected now supports Profiles that help customers prioritize which questions to focus on first by providing a list of prioritized questions that are better aligned with their business goals and outcomes.


1.26.152
========

* api-change:``amplifyuibuilder``: [``botocore``] AWS Amplify UIBuilder is launching Codegen UI, a new feature that enables you to generate your amplify uibuilder components and forms.
* api-change:``dynamodb``: [``botocore``] Documentation updates for DynamoDB
* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version
* api-change:``fsx``: [``botocore``] Amazon FSx for NetApp ONTAP now supports joining a storage virtual machine (SVM) to Active Directory after the SVM has been created.
* api-change:``opensearch``: [``botocore``] This release adds support for SkipUnavailable connection property for cross cluster search
* api-change:``rekognition``: [``botocore``] This release adds support for improved accuracy with user vector in Amazon Rekognition Face Search. Adds new APIs: AssociateFaces, CreateUser, DeleteUser, DisassociateFaces, ListUsers, SearchUsers, SearchUsersByImage. Also adds new face metadata that can be stored: user vector.
* api-change:``sagemaker``: [``botocore``] Sagemaker Neo now supports compilation for inferentia2 (ML_INF2) and Trainium1 (ML_TRN1) as available targets. With these devices, you can run your workloads at highest performance with lowest cost. inferentia2 (ML_INF2) is available in CMH and Trainium1 (ML_TRN1) is available in IAD currently


1.26.151
========

* api-change:``acm-pca``: [``botocore``] Document-only update to refresh CLI  documentation for AWS Private CA. No change to the service.
* api-change:``connect``: [``botocore``] This release adds search APIs for Prompts, Quick Connects and Hours of Operations, which can be used to search for those resources within a Connect Instance.


1.26.150
========

* api-change:``athena``: [``botocore``] You can now define custom spark properties at start of the session for use cases like cluster encryption, table formats, and general Spark tuning.
* api-change:``comprehendmedical``: [``botocore``] This release supports a new set of entities and traits.
* api-change:``payment-cryptography-data``: [``botocore``] Initial release of AWS Payment Cryptography DataPlane Plane service for performing cryptographic operations typically used during card payment processing.
* api-change:``payment-cryptography``: [``botocore``] Initial release of AWS Payment Cryptography Control Plane service for creating and managing cryptographic keys used during card payment processing.
* api-change:``servicecatalog``: [``botocore``] New parameter added in ServiceCatalog DescribeProvisioningArtifact api - IncludeProvisioningArtifactParameters. This parameter can be used to return information about the parameters used to provision the product
* api-change:``timestream-write``: [``botocore``] This release adds the capability for customers to define how their data should be partitioned, optimizing for certain access patterns. This definition will take place as a part of the table creation.


1.26.149
========

* api-change:``cloudformation``: [``botocore``] AWS CloudFormation StackSets is updating the deployment experience for all stackset operations to skip suspended AWS accounts during deployments. StackSets will skip target AWS accounts that are suspended and set the Detailed Status of the corresponding stack instances as SKIPPED_SUSPENDED_ACCOUNT
* api-change:``customer-profiles``: [``botocore``] This release introduces event stream related APIs.
* api-change:``directconnect``: [``botocore``] This update corrects the jumbo frames mtu values from 9100 to 8500 for transit virtual interfaces.
* api-change:``emr-containers``: [``botocore``] EMR on EKS adds support for log rotation of Spark container logs with EMR-6.11.0 onwards, to the StartJobRun API.
* api-change:``iotdeviceadvisor``: [``botocore``] AWS IoT Core Device Advisor now supports new Qualification Suite test case list. With this update, customers can more easily create new qualification test suite with an empty rootGroup input.
* api-change:``logs``: [``botocore``] This change adds support for account level data protection policies using 3 new APIs, PutAccountPolicy, DeleteAccountPolicy and DescribeAccountPolicy. DescribeLogGroup API has been modified to indicate if account level policy is applied to the LogGroup via "inheritedProperties" list in the response.


1.26.148
========

* api-change:``connect``: [``botocore``] GetMetricDataV2 API is now available in AWS GovCloud(US) region.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``iam``: [``botocore``] This release updates the AccountAlias regex pattern with the same length restrictions enforced by the length constraint.
* api-change:``inspector2``: [``botocore``] Adds new response properties and request parameters for 'last scanned at' on the ListCoverage operation. This feature allows you to search and view the date of which your resources were last scanned by Inspector.
* api-change:``iot-data``: [``botocore``] Update thing shadow name regex to allow '$' character
* api-change:``iot``: [``botocore``] Adding IoT Device Management Software Package Catalog APIs to register, store, and report system software packages, along with their versions and metadata in a centralized location.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``quicksight``: [``botocore``] QuickSight support for pivot table field collapse state, radar chart range scale and multiple scope options in conditional formatting.
* api-change:``signer``: [``botocore``] AWS Signer is launching Container Image Signing, a new feature that enables you to sign and verify container images. This feature enables you to validate that only container images you approve are used in your enterprise.
* api-change:``sqs``: [``botocore``] Amazon SQS adds three new APIs - StartMessageMoveTask, CancelMessageMoveTask, and ListMessageMoveTasks to automate redriving messages from dead-letter queues to source queues or a custom destination.


1.26.147
========

* api-change:``cloudformation``: [``botocore``] AWS CloudFormation StackSets provides customers with three new APIs to activate, deactivate, and describe AWS Organizations trusted access which is needed to get started with service-managed StackSets.
* api-change:``ec2``: [``botocore``] Making InstanceTagAttribute as the required parameter for the DeregisterInstanceEventNotificationAttributes and RegisterInstanceEventNotificationAttributes APIs.
* api-change:``finspace``: [``botocore``] Releasing new Managed kdb Insights APIs
* api-change:``frauddetector``: [``botocore``] Added new variable types, new DateTime data type, and new rules engine functions for interacting and working with DateTime data types.
* api-change:``keyspaces``: [``botocore``] This release adds support for MRR GA launch, and includes multiregion support in create-keyspace, get-keyspace, and list-keyspace.
* api-change:``kms``: [``botocore``] This release includes feature to import customer's asymmetric (RSA and ECC) and HMAC keys into KMS.  It also includes feature to allow customers to specify number of days to schedule a KMS key deletion as a policy condition key.
* api-change:``lambda``: [``botocore``] Add Ruby 3.2 (ruby3.2) Runtime support to AWS Lambda.
* api-change:``mwaa``: [``botocore``] This release adds ROLLING_BACK and CREATING_SNAPSHOT environment statuses for Amazon MWAA environments.


1.26.146
========

* api-change:``athena``: [``botocore``] This release introduces the DeleteCapacityReservation API and the ability to manage capacity reservations using CloudFormation
* api-change:``cloudtrail``: [``botocore``] This feature allows users to start and stop event ingestion on a CloudTrail Lake event data store.
* api-change:``sagemaker``: [``botocore``] This release adds Selective Execution feature that allows SageMaker Pipelines users to run selected steps in a pipeline.
* api-change:``wafv2``: [``botocore``] Added APIs to describe managed products. The APIs retrieve information about rule groups that are managed by AWS and by AWS Marketplace sellers.


1.26.145
========

* api-change:``alexaforbusiness``: [``botocore``] Alexa for Business has been deprecated and is no longer supported.
* api-change:``appflow``: [``botocore``] Added ability to select DataTransferApiType for DescribeConnector and CreateFlow requests when using Async supported connectors. Added supportedDataTransferType to DescribeConnector/DescribeConnectors/ListConnector response.
* api-change:``customer-profiles``: [``botocore``] This release introduces calculated attribute related APIs.
* api-change:``ivs``: [``botocore``] API Update for IVS Advanced Channel type
* api-change:``sagemaker``: [``botocore``] Amazon Sagemaker Autopilot adds support for Parquet file input to NLP text classification jobs.
* api-change:``wafv2``: [``botocore``] Corrected the information for the header order FieldToMatch setting


1.26.144
========

* api-change:``config``: [``botocore``] Resource Types Exclusion feature launch by AWS Config
* api-change:``frauddetector``: [``botocore``] This release enables publishing event predictions from Amazon Fraud Detector (AFD) to Amazon EventBridge. For example, after getting predictions from AFD, Amazon EventBridge rules can be configured to trigger notification through an SNS topic, send a message with SES, or trigger Lambda workflows.
* api-change:``healthlake``: [``botocore``] This release adds a new request parameter to the CreateFHIRDatastore API operation. IdentityProviderConfiguration specifies how you want to authenticate incoming requests to your Healthlake Data Store.
* api-change:``m2``: [``botocore``] Adds an optional create-only 'roleArn' property to Application resources.  Enables PS and PO data set org types.
* api-change:``rds``: [``botocore``] This release adds support for changing the engine for Oracle using the ModifyDbInstance API
* api-change:``servicecatalog``: [``botocore``] Documentation updates for ServiceCatalog.
* api-change:``workspaces-web``: [``botocore``] WorkSpaces Web now allows you to control which IP addresses your WorkSpaces Web portal may be accessed from.


1.26.143
========

* api-change:``chime-sdk-voice``: [``botocore``] Added optional CallLeg field to StartSpeakerSearchTask API request
* api-change:``glue``: [``botocore``] Added Runtime parameter to allow selection of Ray Runtime
* api-change:``groundstation``: [``botocore``] Updating description of GetMinuteUsage to be clearer.
* api-change:``iotfleetwise``: [``botocore``] Campaigns now support selecting Timestream or S3 as the data destination, Signal catalogs now support "Deprecation" keyword released in VSS v2.1 and "Comment" keyword released in VSS v3.0
* api-change:``location``: [``botocore``] This release adds API support for political views for the maps service APIs: CreateMap, UpdateMap, DescribeMap.
* api-change:``memorydb``: [``botocore``] Amazon MemoryDB for Redis now supports AWS Identity and Access Management authentication access to Redis clusters starting with redis-engine version 7.0
* api-change:``personalize``: [``botocore``] This release provides support for the exclusion of certain columns for training when creating a solution and creating or updating a recommender with Amazon Personalize.
* api-change:``polly``: [``botocore``] Amazon Polly adds 2 new voices - Sofie (da-DK) and Niamh (en-IE)
* api-change:``securityhub``: [``botocore``] Added new resource detail objects to ASFF, including resources for AwsGuardDutyDetector, AwsAmazonMqBroker, AwsEventSchemasRegistry, AwsAppSyncGraphQlApi and AwsStepFunctionStateMachine.
* api-change:``wafv2``: [``botocore``] This SDK release provides customers the ability to use Header Order as a field to match.


1.26.142
========

* bugfix:``Polly``: [``botocore``] Remove `Content-Type` header from ``synthesize_speech`` URL presigning.
* api-change:``connect``: [``botocore``] Documentation update for a new Initiation Method value in DescribeContact API
* api-change:``iotwireless``: [``botocore``] Add Multicast Group support in Network Analyzer Configuration.
* api-change:``sagemaker``: [``botocore``] Added ml.p4d and ml.inf1 as supported instance type families for SageMaker Notebook Instances.


1.26.141
========

* api-change:``application-autoscaling``: [``botocore``] With this release, ElastiCache customers will be able to use predefined metricType "ElastiCacheDatabaseCapacityUsageCountedForEvictPercentage" for their ElastiCache instances.
* api-change:``codepipeline``: [``botocore``] Add PollingDisabledAt time information in PipelineMetadata object of GetPipeline API.
* api-change:``gamelift``: [``botocore``] GameLift FleetIQ users can now filter game server claim requests to exclude servers on instances that are draining.
* api-change:``glue``: [``botocore``] Added ability to create data quality rulesets for shared, cross-account Glue Data Catalog tables. Added support for dataset comparison rules through a new parameter called AdditionalDataSources. Enhanced the data quality results with a map containing profiled metric values.
* api-change:``migration-hub-refactor-spaces``: [``botocore``] This SDK update allows for path parameter syntax to be passed to the CreateRoute API. Path parameter syntax require parameters to be enclosed in {} characters. This update also includes a new AppendSourcePath field which lets users forward the source path to the Service URL endpoint.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now supports enabling Autotune for tuning jobs which can choose tuning job configurations.


1.26.140
========

* api-change:``appsync``: [``botocore``] This release introduces AppSync Merged APIs, which provide the ability to compose multiple source APIs into a single federated/merged API.
* api-change:``connect``: [``botocore``] Amazon Connect Evaluation Capabilities: validation improvements
* api-change:``cur``: [``botocore``] Add support for split cost allocation data on a report.
* api-change:``sagemaker``: [``botocore``] SageMaker now provides an instantaneous deployment recommendation through the DescribeModel API


1.26.139
========

* api-change:``fms``: [``botocore``] Fixes issue that could cause calls to GetAdminScope and ListAdminAccountsForOrganization to return a 500 Internal Server error.
* api-change:``sagemaker``: [``botocore``] Added ModelNameEquals, ModelPackageVersionArnEquals in request and ModelName, SamplePayloadUrl, ModelPackageVersionArn in response of ListInferenceRecommendationsJobs API. Added Invocation timestamps in response of DescribeInferenceRecommendationsJob API & ListInferenceRecommendationsJobSteps API.
* api-change:``translate``: [``botocore``] Added support for calling TranslateDocument API.


1.26.138
========

* api-change:``backup``: [``botocore``] Added support for tags on restore.
* api-change:``pinpoint``: [``botocore``] Amazon Pinpoint is deprecating the tags parameter in the UpdateSegment, UpdateCampaign, UpdateEmailTemplate, UpdateSmsTemplate, UpdatePushTemplate, UpdateInAppTemplate and UpdateVoiceTemplate. Amazon Pinpoint will end support tags parameter by May 22, 2023.
* api-change:``quicksight``: [``botocore``] Add support for Asset Bundle, Geospatial Heatmaps.


1.26.137
========

* api-change:``backup``: [``botocore``] Add  ResourceArn, ResourceType, and BackupVaultName to ListRecoveryPointsByLegalHold API response.
* api-change:``connectcases``: [``botocore``] This release adds the ability to create fields with type Url through the CreateField API. For more information see https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html
* api-change:``mediapackagev2``: [``botocore``] Adds support for the MediaPackage Live v2 API
* api-change:``sesv2``: [``botocore``] This release allows customers to update scaling mode property of dedicated IP pools with PutDedicatedIpPoolScalingAttributes call.


1.26.136
========

* api-change:``athena``: [``botocore``] Removing SparkProperties from EngineConfiguration object for StartSession API call
* api-change:``cloudtrail``: [``botocore``] Add ConflictException to PutEventSelectors, add (Channel/EDS)ARNInvalidException to Tag APIs. These exceptions provide customers with more specific error messages instead of internal errors.
* api-change:``compute-optimizer``: [``botocore``] In this launch, we add support for showing integration status with external metric providers such as Instana, Datadog ...etc in GetEC2InstanceRecommendations and ExportEC2InstanceRecommendations apis
* api-change:``connect``: [``botocore``] You can programmatically create and manage prompts using APIs, for example, to extract prompts stored within Amazon Connect and add them to your Amazon S3 bucket. AWS CloudTrail, AWS CloudFormation and tagging are supported.
* api-change:``ec2``: [``botocore``] Add support for i4g.large, i4g.xlarge, i4g.2xlarge, i4g.4xlarge, i4g.8xlarge and i4g.16xlarge instances powered by AWS Graviton2 processors that deliver up to 15% better compute performance than our other storage-optimized instances.
* api-change:``ecs``: [``botocore``] Documentation only release to address various tickets.
* api-change:``mediaconvert``: [``botocore``] This release introduces a new MXF Profile for XDCAM which is strictly compliant with the SMPTE RDD 9 standard and improved handling of output name modifiers.
* api-change:``rds``: [``botocore``] RDS documentation update for the EngineVersion parameter of ModifyDBSnapshot
* api-change:``sagemaker-geospatial``: [``botocore``] This release makes ExecutionRoleArn a required field in the StartEarthObservationJob API.
* api-change:``sts``: [``botocore``] API updates for the AWS Security Token Service


1.26.135
========

* api-change:``detective``: [``botocore``] Added and updated API operations in Detective to support the integration of ASFF Security Hub findings.
* api-change:``directconnect``: [``botocore``] This release includes an update to the mtu value for CreateTransitVirtualInterface from 9001 mtu to 8500 mtu.
* api-change:``glue``: [``botocore``] Add Support for Tags for Custom Entity Types
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``wafv2``: [``botocore``] My AWS Service (placeholder) - You can now rate limit web requests based on aggregation keys other than IP addresses, and you can aggregate using combinations of keys. You can also rate limit all requests that match a scope-down statement, without further aggregation.


1.26.134
========

* bugfix:EndpointProvider: [``botocore``] Fixed bug in virtual addressing for S3 Buckets `#2938 <https://github.com/boto/botocore/issues/2938>`__
* api-change:``athena``: [``botocore``] You can now define custom spark properties at start of the session for use cases like cluster encryption, table formats, and general Spark tuning.
* api-change:``codecatalyst``: [``botocore``] With this release, the users can list the active sessions connected to their Dev Environment on AWS CodeCatalyst
* api-change:``kafka``: [``botocore``] Added a fix to make clusterarn a required field in ListClientVpcConnections and RejectClientVpcConnection APIs
* api-change:``rekognition``: [``botocore``] This release adds a new EyeDirection attribute in Amazon Rekognition DetectFaces and IndexFaces APIs which predicts the yaw and pitch angles of a person's eye gaze direction for each face detected in the image.
* api-change:``rolesanywhere``: [``botocore``] Adds support for custom notification settings in a trust anchor. Introduces PutNotificationSettings and ResetNotificationSettings API's. Updates DurationSeconds max value to 3600.
* api-change:``transfer``: [``botocore``] This release introduces the ability to require both password and SSH key when users authenticate to your Transfer Family servers that use the SFTP protocol.


1.26.133
========

* bugfix:endpoints: [``botocore``] Include params set in provide-client-param event handlers in dynamic context params for endpoint resolution.
* api-change:``connect``: [``botocore``] This release updates GetMetricDataV2 API, to support metric data up-to last 35 days
* api-change:``elasticache``: [``botocore``] Added support to modify the cluster mode configuration for the existing ElastiCache ReplicationGroups. Customers can now modify the configuration from cluster mode disabled to cluster mode enabled.
* api-change:``es``: [``botocore``] This release fixes DescribePackages API error with null filter value parameter.
* api-change:``health``: [``botocore``] Add support for regional endpoints
* api-change:``ivs-realtime``: [``botocore``] Add methods for inspecting and debugging stages: ListStageSessions, GetStageSession, ListParticipants, GetParticipant, and ListParticipantEvents.
* api-change:``omics``: [``botocore``] This release provides support for Ready2Run and GPU workflows, an improved read set filter, the direct upload of read sets into Omics Storage, and annotation parsing for analytics stores.
* api-change:``opensearch``: [``botocore``] This release fixes DescribePackages API error with null filter value parameter.
* api-change:``route53resolver``: [``botocore``] Update FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``support``: [``botocore``] This release adds 2 new Support APIs, DescribeCreateCaseOptions and DescribeSupportedLanguages. You can use these new APIs to get available support languages.


1.26.132
========

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``rds``: [``botocore``] Amazon Relational Database Service (RDS) updates for the new Aurora I/O-Optimized storage type for Amazon Aurora DB clusters
* api-change:``swf``: [``botocore``] This release adds a new API parameter to exclude old history events from decision tasks.


1.26.131
========

* enhancement:endpoints: [``botocore``] Fix cache implementation to reduce memory consumption.
* api-change:``application-autoscaling``: [``botocore``] With this release, Amazon SageMaker Serverless Inference customers can use Application Auto Scaling to auto scale the provisioned concurrency of their serverless endpoints.
* api-change:``glue``: [``botocore``] This release adds AmazonRedshift Source and Target nodes in addition to DynamicTransform OutputSchemas
* api-change:``sagemaker``: [``botocore``] This release includes support for (1) Provisioned Concurrency for Amazon SageMaker Serverless Inference and (2) UpdateEndpointWeightsAndCapacities API for Serverless endpoints.


1.26.130
========

* api-change:``glue``: [``botocore``] Support large worker types G.4x and G.8x for Glue Spark
* api-change:``guardduty``: [``botocore``] Add AccessDeniedException 403 Error message code to support 3 Tagging related APIs
* api-change:``iotsitewise``: [``botocore``] Provide support for 20,000 max results for GetAssetPropertyValueHistory/BatchGetAssetPropertyValueHistory and 15 minute aggregate resolution for GetAssetPropertyAggregates/BatchGetAssetPropertyAggregates
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.


1.26.129
========

* api-change:``ec2``: [``botocore``] This release adds support the inf2 and trn1n instances. inf2 instances are purpose built for deep learning inference while trn1n instances are powered by AWS Trainium accelerators and they build on the capabilities of Trainium-powered trn1 instances.
* api-change:``inspector2``: [``botocore``] Amazon Inspector now allows customers to search its vulnerability intelligence database if any of the Inspector scanning types are activated.
* api-change:``mediatailor``: [``botocore``] This release adds support for AFTER_LIVE_EDGE mode configuration for avail suppression, and adding a fill-policy setting that sets the avail suppression to PARTIAL_AVAIL or FULL_AVAIL_ONLY when AFTER_LIVE_EDGE is enabled.
* api-change:``sqs``: [``botocore``] Revert previous SQS protocol change.


1.26.128
========

* bugfix:``sqs``: [``botocore``] Rolled back recent change to wire format protocol


1.26.127
========

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``config``: [``botocore``] Updated ResourceType enum with new resource types onboarded by AWS Config in April 2023.
* api-change:``connect``: [``botocore``] Remove unused InvalidParameterException from CreateParticipant API
* api-change:``ecs``: [``botocore``] Documentation update for new error type NamespaceNotFoundException for CreateCluster and UpdateCluster
* api-change:``network-firewall``: [``botocore``] This release adds support for the Suricata REJECT option in midstream exception configurations.
* api-change:``opensearch``: [``botocore``] DescribeDomainNodes: A new API that provides configuration information for nodes part of the domain
* api-change:``quicksight``: [``botocore``] Add support for Topic, Dataset parameters and VPC
* api-change:``rekognition``: [``botocore``] This release adds a new attribute FaceOccluded. Additionally, you can now select attributes individually (e.g. ["DEFAULT", "FACE_OCCLUDED", "AGE_RANGE"] instead of ["ALL"]), which can reduce response time.
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3
* api-change:``sagemaker``: [``botocore``] We added support for ml.inf2 and ml.trn1 family of instances on Amazon SageMaker for deploying machine learning (ML) models for Real-time and Asynchronous inference. You can use these instances to achieve high performance at a low cost for generative artificial intelligence (AI) models.
* api-change:``securityhub``: [``botocore``] Add support for Finding History.
* api-change:``sqs``: [``botocore``] This release enables customers to call SQS using AWS JSON-1.0 protocol.


1.26.126
========

* api-change:``appsync``: [``botocore``] Private API support for AWS AppSync. With Private APIs, you can now create GraphQL APIs that can only be accessed from your Amazon Virtual Private Cloud ("VPC").
* api-change:``ec2``: [``botocore``] Adds an SDK paginator for GetNetworkInsightsAccessScopeAnalysisFindings
* api-change:``inspector2``: [``botocore``] This feature provides deep inspection for linux based instance
* api-change:``iottwinmaker``: [``botocore``] This release adds a field for GetScene API to return error code and message from dependency services.
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall now supports policy level HOME_NET variable overrides.
* api-change:``opensearch``: [``botocore``] Amazon OpenSearch Service adds the option to deploy a domain across multiple Availability Zones, with each AZ containing a complete copy of data and with nodes in one AZ acting as a standby. This option provides 99.99% availability and consistent performance in the event of infrastructure failure.
* api-change:``wellarchitected``: [``botocore``] This release deepens integration with AWS Service Catalog AppRegistry to improve workload resource discovery.


1.26.125
========

* api-change:``appflow``: [``botocore``] This release adds new API to cancel flow executions.
* api-change:``connect``: [``botocore``] Amazon Connect Service Rules API update: Added OnContactEvaluationSubmit event source to support user configuring evaluation form rules.
* api-change:``ecs``: [``botocore``] Documentation only update to address Amazon ECS tickets.
* api-change:``kendra``: [``botocore``] AWS Kendra now supports configuring document fields/attributes via the GetQuerySuggestions API. You can now base query suggestions on the contents of document fields.
* api-change:``resiliencehub``: [``botocore``] This release will improve resource level transparency in applications by discovering previously hidden resources.
* api-change:``sagemaker``: [``botocore``] Amazon Sagemaker Autopilot supports training models with sample weights and additional objective metrics.


1.26.124
========

* api-change:``compute-optimizer``: [``botocore``] support for tag filtering within compute optimizer. ability to filter recommendation results by tag and tag key value pairs. ability to filter by inferred workload type added.
* api-change:``kms``: [``botocore``] This release makes the NitroEnclave request parameter Recipient and the response field for CiphertextForRecipient available in AWS SDKs. It also adds the regex pattern for CloudHsmClusterId validation.


1.26.123
========

* api-change:``appflow``: [``botocore``] Adds Jwt Support for Salesforce Credentials.
* api-change:``athena``: [``botocore``] You can now use capacity reservations on Amazon Athena to run SQL queries on fully-managed compute capacity.
* api-change:``directconnect``: [``botocore``] This release corrects the jumbo frames MTU from 9100 to 8500.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``grafana``: [``botocore``] This release adds support for the grafanaVersion parameter in CreateWorkspace.
* api-change:``iot``: [``botocore``] This release allows AWS IoT Core users to specify a TLS security policy when creating and updating AWS IoT Domain Configurations.
* api-change:``rekognition``: [``botocore``] Added support for aggregating moderation labels by video segment timestamps for Stored Video Content Moderation APIs and added additional information about the job to all Stored Video Get API responses.
* api-change:``simspaceweaver``: [``botocore``] Added a new CreateSnapshot API. For the StartSimulation API, SchemaS3Location is now optional, added a new SnapshotS3Location parameter. For the DescribeSimulation API, added SNAPSHOT_IN_PROGRESS simulation state, deprecated SchemaError, added new fields: StartError and SnapshotS3Location.
* api-change:``wafv2``: [``botocore``] You can now associate a web ACL with a Verified Access instance.
* api-change:``workspaces``: [``botocore``] Added Windows 11 to support Microsoft_Office_2019


1.26.122
========

* api-change:``ec2``: [``botocore``] This release adds support for AMD SEV-SNP on EC2 instances.
* api-change:``emr-containers``: [``botocore``] This release adds GetManagedEndpointSessionCredentials, a new API that allows customers to generate an auth token to connect to a managed endpoint, enabling features such as self-hosted Jupyter notebooks for EMR on EKS.
* api-change:``guardduty``: [``botocore``] Added API support to initiate on-demand malware scan on specific resources.
* api-change:``iotdeviceadvisor``: [``botocore``] AWS IoT Core Device Advisor now supports MQTT over WebSocket. With this update, customers can run all three test suites of AWS IoT Core Device Advisor - qualification, custom, and long duration tests - using Signature Version 4 for MQTT over WebSocket.
* api-change:``kafka``: [``botocore``] Amazon MSK has added new APIs that allows multi-VPC private connectivity and cluster policy support for Amazon MSK clusters that simplify connectivity and access between your Apache Kafka clients hosted in different VPCs and AWS accounts and your Amazon MSK clusters.
* api-change:``lambda``: [``botocore``] Add Java 17 (java17) support to AWS Lambda
* api-change:``marketplace-catalog``: [``botocore``] Enabled Pagination for List Entities and List Change Sets operations
* api-change:``osis``: [``botocore``] Documentation updates for OpenSearch Ingestion
* api-change:``qldb``: [``botocore``] Documentation updates for Amazon QLDB
* api-change:``sagemaker``: [``botocore``] Added ml.p4d.24xlarge and ml.p4de.24xlarge as supported instances for SageMaker Studio
* api-change:``xray``: [``botocore``] Updated X-Ray documentation with Resource Policy API descriptions.


1.26.121
========

* api-change:``osis``: [``botocore``] Initial release for OpenSearch Ingestion


1.26.120
========

* api-change:``chime-sdk-messaging``: [``botocore``] Remove non actionable field from UpdateChannelReadMarker and DeleteChannelRequest.  Add precise exceptions to DeleteChannel and DeleteStreamingConfigurations error cases.
* api-change:``connect``: [``botocore``] Amazon Connect, Contact Lens Evaluation API release including ability to manage forms and to submit contact evaluations.
* api-change:``datasync``: [``botocore``] This release adds 13 new APIs to support AWS DataSync Discovery GA.
* api-change:``ds``: [``botocore``] New field added in AWS Managed Microsoft AD DescribeSettings response and regex pattern update for UpdateSettings value.  Added length validation to RemoteDomainName.
* api-change:``pinpoint``: [``botocore``] Adds support for journey runs and querying journey execution metrics based on journey runs. Adds execution metrics to campaign activities. Updates docs for Advanced Quiet Time.


1.26.119
========

* api-change:``appflow``: [``botocore``] Increased the max length for RefreshToken and AuthCode from 2048 to 4096.
* api-change:``codecatalyst``: [``botocore``] Documentation updates for Amazon CodeCatalyst.
* api-change:``ec2``: [``botocore``] API changes to AWS Verified Access related to identity providers' information.
* api-change:``mediaconvert``: [``botocore``] This release introduces a noise reduction pre-filter, linear interpolation deinterlace mode, video pass-through, updated default job settings, and expanded LC-AAC Stereo audio bitrate ranges.
* api-change:``rekognition``: [``botocore``] Added new status result to Liveness session status.


1.26.118
========

* api-change:``connect``: [``botocore``] This release adds a new API CreateParticipant. For Amazon Connect Chat, you can use this new API to customize chat flow experiences.
* api-change:``ecs``: [``botocore``] Documentation update to address various Amazon ECS tickets.
* api-change:``fms``: [``botocore``] AWS Firewall Manager adds support for multiple administrators. You can now delegate more than one administrator per organization.


1.26.117
========

* api-change:``chime-sdk-media-pipelines``: [``botocore``] This release adds support for specifying the recording file format in an S3 recording sink configuration.
* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for Hindi and Thai languages and additional Amazon Transcribe parameters to the StartMeetingTranscription API.
* api-change:``chime``: [``botocore``] Adds support for Hindi and Thai languages and additional Amazon Transcribe parameters to the StartMeetingTranscription API.
* api-change:``gamelift``: [``botocore``] Amazon GameLift supports creating Builds for Windows 2016 operating system.
* api-change:``guardduty``: [``botocore``] This release adds support for the new Lambda Protection feature.
* api-change:``iot``: [``botocore``] Support additional OTA states in GetOTAUpdate API
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Canvas adds ModelRegisterSettings support for CanvasAppSettings.
* api-change:``snowball``: [``botocore``] Adds support for Amazon S3 compatible storage. AWS Snow Family customers can now use Amazon S3 compatible storage on Snowball Edge devices. Also adds support for V3_5S. This is a refreshed AWS Snowball Edge Storage Optimized device type with 210TB SSD (customer usable).
* api-change:``wafv2``: [``botocore``] You can now create encrypted API keys to use in a client application integration of the JavaScript CAPTCHA API . You can also retrieve a list of your API keys and the JavaScript application integration URL.


1.26.116
========

* api-change:``comprehend``: [``botocore``] This release supports native document models for custom classification, in addition to plain-text models. You train native document models using documents (PDF, Word, images) in their native format.
* api-change:``ecs``: [``botocore``] This release supports the Account Setting "TagResourceAuthorization" that allows for enhanced Tagging security controls.
* api-change:``ram``: [``botocore``] This release adds support for customer managed permissions. Customer managed permissions enable customers to author and manage tailored permissions for resources shared using RAM.
* api-change:``rds``: [``botocore``] Adds support for the ImageId parameter of CreateCustomDBEngineVersion to RDS Custom for Oracle
* api-change:``s3``: [``botocore``] Provides support for "Snow" Storage class.
* api-change:``s3control``: [``botocore``] Provides support for overriding endpoint when region is "snow". This will enable bucket APIs for Amazon S3 Compatible storage on Snow Family devices.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager


1.26.115
========

* api-change:``appflow``: [``botocore``] This release adds a Client Token parameter to the following AppFlow APIs: Create/Update Connector Profile, Create/Update Flow, Start Flow, Register Connector, Update Connector Registration. The Client Token parameter allows idempotent operations for these APIs.
* api-change:``drs``: [``botocore``] Changed existing APIs and added new APIs to support using an account-level launch configuration template with AWS Elastic Disaster Recovery.
* api-change:``dynamodb``: [``botocore``] Documentation updates for DynamoDB API
* api-change:``emr-serverless``: [``botocore``] The GetJobRun API has been updated to include the job's billed resource utilization. This utilization shows the aggregate vCPU, memory and storage that AWS has billed for the job run. The billed resources include a 1-minute minimum usage for workers, plus additional storage over 20 GB per worker.
* api-change:``internetmonitor``: [``botocore``] This release includes a new configurable value, TrafficPercentageToMonitor, which allows users to adjust the amount of traffic monitored by percentage
* api-change:``iotwireless``: [``botocore``] Supports the new feature of LoRaWAN roaming, allows to configure MaxEirp for LoRaWAN gateway, and allows to configure PingSlotPeriod for LoRaWAN multicast group
* api-change:``lambda``: [``botocore``] Add Python 3.10 (python3.10) support to AWS Lambda


1.26.114
========

* api-change:``ecs``: [``botocore``] This release supports  ephemeral storage for AWS Fargate Windows containers.
* api-change:``lambda``: [``botocore``] This release adds SnapStart related exceptions to InvokeWithResponseStream API. IAM access related documentation is also added for this API.
* api-change:``migration-hub-refactor-spaces``: [``botocore``] Doc only update for Refactor Spaces environments without network bridge feature.
* api-change:``rds``: [``botocore``] This release adds support of modifying the engine mode of database clusters.


1.26.113
========

* api-change:``chime-sdk-voice``: [``botocore``] This release adds tagging support for Voice Connectors and SIP Media Applications
* api-change:``mediaconnect``: [``botocore``] Gateway is a new feature of AWS Elemental MediaConnect. Gateway allows the deployment of on-premises resources for the purpose of transporting live video to and from the AWS Cloud.


1.26.112
========

* api-change:``groundstation``: [``botocore``] AWS Ground Station Wideband DigIF GA Release
* api-change:``managedblockchain``: [``botocore``] Removal of the Ropsten network. The Ethereum foundation ceased support of Ropsten on December 31st, 2022..


1.26.111
========

* api-change:``ecr-public``: [``botocore``] This release will allow using registry alias as registryId in BatchDeleteImage request.
* api-change:``emr-serverless``: [``botocore``] This release extends GetJobRun API to return job run timeout (executionTimeoutMinutes) specified during StartJobRun call (or default timeout of 720 minutes if none was specified).
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``iot-data``: [``botocore``] This release adds support for MQTT5 user properties when calling the AWS IoT GetRetainedMessage API
* api-change:``wafv2``: [``botocore``] For web ACLs that protect CloudFront protections, the default request body inspection size is now 16 KB, and you can use the new association configuration to increase the inspection size further, up to 64 KB. Sizes over 16 KB can incur additional costs.


1.26.110
========

* api-change:``connect``: [``botocore``] This release adds the ability to configure an agent's routing profile to receive contacts from multiple channels at the same time via extending the UpdateRoutingProfileConcurrency, CreateRoutingProfile and DescribeRoutingProfile APIs.
* api-change:``ecs``: [``botocore``] This release adds support for enabling FIPS compliance on Amazon ECS Fargate tasks
* api-change:``marketplace-catalog``: [``botocore``] Added three new APIs to support resource sharing: GetResourcePolicy, PutResourcePolicy, and DeleteResourcePolicy. Added new OwnershipType field to ListEntities request to let users filter on entities that are shared with them. Increased max page size of ListEntities response from 20 to 50 results.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK now supports conversion of 608 paint-on captions to pop-on captions for SCC sources.
* api-change:``omics``: [``botocore``] Remove unexpected API changes.
* api-change:``rekognition``: [``botocore``] This release adds support for Face Liveness APIs in Amazon Rekognition. Updates UpdateStreamProcessor to return ResourceInUseException Exception. Minor updates to API documentation.


1.26.109
========

* api-change:``dlm``: [``botocore``] Updated timestamp format for GetLifecyclePolicy API
* api-change:``docdb``: [``botocore``] This release adds a new parameter 'DBClusterParameterGroupName' to 'RestoreDBClusterFromSnapshot' API to associate the name of the DB cluster parameter group while performing restore.
* api-change:``fsx``: [``botocore``] Amazon FSx for Lustre now supports creating data repository associations on Persistent_1 and Scratch_2 file systems.
* api-change:``lambda``: [``botocore``] This release adds a new Lambda InvokeWithResponseStream API to support streaming Lambda function responses. The release also adds a new InvokeMode parameter to Function Url APIs to control whether the response will be streamed or buffered.
* api-change:``quicksight``: [``botocore``] This release has two changes: adding the OR condition to tag-based RLS rules in CreateDataSet and UpdateDataSet; adding RefreshSchedule and Incremental RefreshProperties operations for users to programmatically configure SPICE dataset ingestions.
* api-change:``redshift-data``: [``botocore``] Update documentation of API descriptions as needed in support of temporary credentials with IAM identity.
* api-change:``servicecatalog``: [``botocore``] Updates description for property


1.26.108
========

* api-change:``cloudformation``: [``botocore``] Including UPDATE_COMPLETE as a failed status for DeleteStack waiter.
* api-change:``greengrassv2``: [``botocore``] Add support for SUCCEEDED value in coreDeviceExecutionStatus field. Documentation updates for Greengrass V2.
* api-change:``proton``: [``botocore``] This release adds support for the AWS Proton service sync feature. Service sync enables managing an AWS Proton service (creating and updating instances) and all of it's corresponding service instances from a Git repository.
* api-change:``rds``: [``botocore``] Adds and updates the SDK examples


1.26.107
========

* api-change:``apprunner``: [``botocore``] App Runner adds support for seven new vCPU and memory configurations.
* api-change:``config``: [``botocore``] This release adds resourceType enums for types released in March 2023.
* api-change:``ecs``: [``botocore``] This is a document only updated to add information about Amazon Elastic Inference (EI).
* api-change:``identitystore``: [``botocore``] Documentation updates for Identity Store CLI command reference.
* api-change:``ivs-realtime``: [``botocore``] Fix ParticipantToken ExpirationTime format
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall now supports IPv6-only subnets.
* api-change:``servicecatalog``: [``botocore``] removed incorrect product type value
* api-change:``vpc-lattice``: [``botocore``] This release removes the entities in the API doc model package for auth policies.


1.26.106
========

* api-change:``amplifyuibuilder``: [``botocore``] Support StorageField and custom displays for data-bound options in form builder. Support non-string operands for predicates in collections. Support choosing client to get token from.
* api-change:``autoscaling``: [``botocore``] Documentation updates for Amazon EC2 Auto Scaling
* api-change:``dataexchange``: [``botocore``] This release updates the value of MaxResults.
* api-change:``ec2``: [``botocore``] C6in, M6in, M6idn, R6in and R6idn bare metal instances are powered by 3rd Generation Intel Xeon Scalable processors and offer up to 200 Gbps of network bandwidth.
* api-change:``elastic-inference``: [``botocore``] Updated public documentation for the Describe and Tagging APIs.
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Asynchronous Inference now allows customer's to receive failure model responses in S3 and receive success/failure model responses in SNS notifications.
* api-change:``wafv2``: [``botocore``] This release rolls back association config feature for webACLs that protect CloudFront protections.


1.26.105
========

* api-change:``glue``: [``botocore``] Add support for database-level federation
* api-change:``lakeformation``: [``botocore``] Add support for database-level federation
* api-change:``license-manager``: [``botocore``] This release adds grant override options to the CreateGrantVersion API. These options can be used to specify grant replacement behavior during grant activation.
* api-change:``mwaa``: [``botocore``] This Amazon MWAA release adds the ability to customize the Apache Airflow environment by launching a shell script at startup. This shell script is hosted in your environment's Amazon S3 bucket. Amazon MWAA runs the script before installing requirements and initializing the Apache Airflow process.
* api-change:``servicecatalog``: [``botocore``] This release introduces Service Catalog support for Terraform open source. It enables 1. The notify* APIs to Service Catalog. These APIs are used by the terraform engine to notify the result of the provisioning engine execution. 2. Adds a new TERRAFORM_OPEN_SOURCE product type in CreateProduct API.
* api-change:``wafv2``: [``botocore``] For web ACLs that protect CloudFront protections, the default request body inspection size is now 16 KB, and you can use the new association configuration to increase the inspection size further, up to 64 KB. Sizes over 16 KB can incur additional costs.


1.26.104
========

* api-change:``ec2``: [``botocore``] Documentation updates for EC2 On Demand Capacity Reservations
* api-change:``internetmonitor``: [``botocore``] This release adds a new feature for Amazon CloudWatch Internet Monitor that enables customers to deliver internet measurements to Amazon S3 buckets as well as CloudWatch Logs.
* api-change:``resiliencehub``: [``botocore``] Adding EKS related documentation for appTemplateBody
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] In this release, you can now chose between soft delete and hard delete when calling the DeleteRecord API, so you have more flexibility when it comes to managing online store data.
* api-change:``sms``: [``botocore``] Deprecating AWS Server Migration Service.


1.26.103
========

* api-change:``athena``: [``botocore``] Make DefaultExecutorDpuSize and CoordinatorDpuSize  fields optional  in StartSession
* api-change:``autoscaling``: [``botocore``] Amazon EC2 Auto Scaling now supports Elastic Load Balancing traffic sources with the AttachTrafficSources, DetachTrafficSources, and DescribeTrafficSources APIs. This release also introduces a new activity status, "WaitingForConnectionDraining", for VPC Lattice to the DescribeScalingActivities API.
* api-change:``batch``: [``botocore``] This feature allows Batch on EKS to support configuration of Pod Labels through Metadata for Batch on EKS Jobs.
* api-change:``compute-optimizer``: [``botocore``] This release adds support for HDD EBS volume types and io2 Block Express. We are also adding support for 61 new instance types and instances that have non consecutive runtime.
* api-change:``drs``: [``botocore``] Adding a field to the replication configuration APIs to support the auto replicate new disks feature. We also deprecated RetryDataReplication.
* api-change:``ec2``: [``botocore``] This release adds support for Tunnel Endpoint Lifecycle control, a new feature that provides Site-to-Site VPN customers with better visibility and control of their VPN tunnel maintenance updates.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``glue``: [``botocore``] This release adds support for AWS Glue Data Quality, which helps you evaluate and monitor the quality of your data and includes the API for creating, deleting, or updating data quality rulesets, runs and evaluations.
* api-change:``guardduty``: [``botocore``] Added EKS Runtime Monitoring feature support to existing detector, finding APIs and introducing new Coverage APIs
* api-change:``imagebuilder``: [``botocore``] Adds support for new image workflow details and image vulnerability detection.
* api-change:``ivs``: [``botocore``] Amazon Interactive Video Service (IVS) now offers customers the ability to configure IVS channels to allow insecure RTMP ingest.
* api-change:``kendra``: [``botocore``] AWS Kendra now supports featured results for a query.
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall added TLS inspection configurations to allow TLS traffic inspection.
* api-change:``sagemaker-geospatial``: [``botocore``] Amazon SageMaker geospatial capabilities now supports server-side encryption with customer managed KMS key and SageMaker notebooks with a SageMaker geospatial image in a Amazon SageMaker Domain with VPC only mode.
* api-change:``vpc-lattice``: [``botocore``] General Availability (GA) release of Amazon VPC Lattice
* api-change:``wellarchitected``: [``botocore``] AWS Well-Architected SDK now supports getting consolidated report metrics and generating a consolidated report PDF.


1.26.102
========

* api-change:``opensearchserverless``: [``botocore``] This release includes two new exception types "ServiceQuotaExceededException" and "OcuLimitExceededException".
* api-change:``rds``: [``botocore``] Add support for creating a read replica DB instance from a Multi-AZ DB cluster.


1.26.101
========

* api-change:``iot-data``: [``botocore``] Add endpoint ruleset support for cn-north-1.
* api-change:``ssm-contacts``: [``botocore``] This release adds 12 new APIs as part of Oncall Schedule feature release, adds support for a new contact type: ONCALL_SCHEDULE. Check public documentation for AWS ssm-contacts for more information
* api-change:``ssm-incidents``: [``botocore``] Increased maximum length of "TriggerDetails.rawData" to 10K characters and "IncidentSummary" to 8K characters.


1.26.100
========

* api-change:``athena``: [``botocore``] Enforces a minimal level of encryption for the workgroup for query and calculation results that are written to Amazon S3. When enabled, workgroup users can set encryption only to the minimum level set by the administrator or higher when they submit queries.
* api-change:``chime-sdk-voice``: [``botocore``] Documentation updates for Amazon Chime SDK Voice.
* api-change:``connect``: [``botocore``] This release introduces support for RelatedContactId in the StartChatContact API. Interactive message and interactive message response have been added to the list of supported message content types for this API as well.
* api-change:``connectparticipant``: [``botocore``] This release provides an update to the SendMessage API to handle interactive message response content-types.
* api-change:``iotwireless``: [``botocore``] Introducing new APIs that enable Sidewalk devices to communicate with AWS IoT Core through Sidewalk gateways. This will empower AWS customers to connect Sidewalk devices with other AWS IoT Services, creating  possibilities for seamless integration and advanced device management.
* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive now supports ID3 tag insertion for audio only HLS output groups. AWS Elemental Link devices now support tagging.
* api-change:``sagemaker``: [``botocore``] Fixed some improperly rendered links in SDK documentation.
* api-change:``securityhub``: [``botocore``] Added new resource detail objects to ASFF, including resources for AwsEksCluster, AWSS3Bucket, AwsEc2RouteTable and AwsEC2Instance.
* api-change:``servicecatalog-appregistry``: [``botocore``] In this release, we started supporting ARN in applicationSpecifier and attributeGroupSpecifier. GetAttributeGroup, ListAttributeGroups and ListAttributeGroupsForApplication APIs will now have CreatedBy field in the response.
* api-change:``voice-id``: [``botocore``] Amazon Connect Voice ID now supports multiple fraudster watchlists. Every domain has a default watchlist where all existing fraudsters are placed by default. Custom watchlists may now be created, managed, and evaluated against for known fraudster detection.


1.26.99
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``comprehend``: [``botocore``] This release adds a new field (FlywheelArn) to the EntitiesDetectionJobProperties object. The FlywheelArn field is returned in the DescribeEntitiesDetectionJob and ListEntitiesDetectionJobs responses when the EntitiesDetection job is started with a FlywheelArn instead of an EntityRecognizerArn .
* api-change:``rds``: [``botocore``] Added error code CreateCustomDBEngineVersionFault for when the create custom engine version for Custom engines fails.


1.26.98
=======

* api-change:``batch``: [``botocore``] This feature allows Batch to support configuration of ephemeral storage size for jobs running on FARGATE
* api-change:``chime-sdk-identity``: [``botocore``] AppInstanceBots can be used to add a bot powered by Amazon Lex to chat channels.  ExpirationSettings provides automatic resource deletion for AppInstanceUsers.
* api-change:``chime-sdk-media-pipelines``: [``botocore``] This release adds Amazon Chime SDK call analytics. Call analytics include voice analytics, which provides speaker search and voice tone analysis. These capabilities can be used with Amazon Transcribe and Transcribe Call Analytics to generate machine-learning-powered insights from real-time audio.
* api-change:``chime-sdk-messaging``: [``botocore``] ExpirationSettings provides automatic resource deletion for Channels.
* api-change:``chime-sdk-voice``: [``botocore``] This release adds Amazon Chime SDK call analytics. Call analytics include voice analytics, which provides speaker search and voice tone analysis. These capabilities can be used with Amazon Transcribe and Transcribe Call Analytics to generate machine-learning-powered insights from real-time audio.
* api-change:``codeartifact``: [``botocore``] Repository CreationTime is added to the CreateRepository and ListRepositories API responses.
* api-change:``guardduty``: [``botocore``] Adds AutoEnableOrganizationMembers attribute to DescribeOrganizationConfiguration and UpdateOrganizationConfiguration APIs.
* api-change:``ivs-realtime``: [``botocore``] Initial release of the Amazon Interactive Video Service RealTime API.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK now supports passthrough of ID3v2 tags for audio inputs to audio-only HLS outputs.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds two new APIs - CreateAutoMLJobV2 and DescribeAutoMLJobV2. Amazon SageMaker Notebook Instances now supports the ml.geospatial.interactive instance type.
* api-change:``servicediscovery``: [``botocore``] Reverted the throttling exception RequestLimitExceeded for AWS Cloud Map APIs introduced in SDK version 1.12.424 2023-03-09 to previous exception specified in the ErrorCode.
* api-change:``textract``: [``botocore``] The AnalyzeDocument - Tables feature adds support for new elements in the API: table titles, footers, section titles, summary cells/tables, and table type.


1.26.97
=======

* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``iottwinmaker``: [``botocore``] This release adds support of adding metadata when creating a new scene or updating an existing scene.
* api-change:``networkmanager``: [``botocore``] This release includes an update to create-transit-gateway-route-table-attachment, showing example usage for TransitGatewayRouteTableArn.
* api-change:``pipes``: [``botocore``] This release improves validation on the ARNs in the API model
* api-change:``resiliencehub``: [``botocore``] This release provides customers with the ability to import resources from within an EKS cluster and assess the resiliency of EKS cluster workloads.
* api-change:``ssm``: [``botocore``] This Patch Manager release supports creating, updating, and deleting Patch Baselines for AmazonLinux2023, AlmaLinux.


1.26.96
=======

* api-change:``chime-sdk-messaging``: [``botocore``] Amazon Chime SDK messaging customers can now manage streaming configuration for messaging data for archival and analysis.
* api-change:``cleanrooms``: [``botocore``] GA Release of AWS Clean Rooms, Added Tagging Functionality
* api-change:``ec2``: [``botocore``] This release adds support for AWS Network Firewall, AWS PrivateLink, and Gateway Load Balancers to Amazon VPC Reachability Analyzer, and it makes the path destination optional as long as a destination address in the filter at source is provided.
* api-change:``iotsitewise``: [``botocore``] Provide support for tagging of data streams and enabling tag based authorization for property alias
* api-change:``mgn``: [``botocore``] This release introduces the Import and export feature and expansion of the post-launch actions


1.26.95
=======

* api-change:``application-autoscaling``: [``botocore``] With this release customers can now tag their Application Auto Scaling registered targets with key-value pairs and manage IAM permissions for all the tagged resources centrally.
* api-change:``neptune``: [``botocore``] This release makes following few changes. db-cluster-identifier is now a required parameter of create-db-instance. describe-db-cluster will now return PendingModifiedValues and GlobalClusterIdentifier fields in the response.
* api-change:``s3outposts``: [``botocore``] S3 On Outposts added support for endpoint status, and a failed endpoint reason, if any
* api-change:``workdocs``: [``botocore``] This release adds a new API, SearchResources, which enable users to search through metadata and content of folders, documents, document versions and comments in a WorkDocs site.


1.26.94
=======

* api-change:``billingconductor``: [``botocore``] This release adds a new filter to ListAccountAssociations API and a new filter to ListBillingGroups API.
* api-change:``config``: [``botocore``] This release adds resourceType enums for types released from October 2022 through February 2023.
* api-change:``dms``: [``botocore``] S3 setting to create AWS Glue Data Catalog. Oracle setting to control conversion of timestamp column. Support for Kafka SASL Plain authentication. Setting to map boolean from PostgreSQL to Redshift. SQL Server settings to force lob lookup on inline LOBs and to control access of database logs.


1.26.93
=======

* api-change:``guardduty``: [``botocore``] Updated 9 APIs for feature enablement to reflect expansion of GuardDuty to features. Added new APIs and updated existing APIs to support RDS Protection GA.
* api-change:``resource-explorer-2``: [``botocore``] Documentation updates for APIs.
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version


1.26.92
=======

* api-change:``migrationhubstrategy``: [``botocore``] This release adds the binary analysis that analyzes IIS application DLLs on Windows and Java applications on Linux to provide anti-pattern report without configuring access to the source code.
* api-change:``s3control``: [``botocore``] Added support for S3 Object Lambda aliases.
* api-change:``securitylake``: [``botocore``] Make Create/Get/ListSubscribers APIs return resource share ARN and name so they can be used to validate the RAM resource share to accept. GetDatalake can be used to track status of UpdateDatalake and DeleteDatalake requests.


1.26.91
=======

* api-change:``application-autoscaling``: [``botocore``] Application Auto Scaling customers can now use mathematical functions to customize the metric used with Target Tracking policies within the policy configuration itself, saving the cost and effort of publishing the customizations as a separate metric.
* api-change:``dataexchange``: [``botocore``] This release enables data providers to license direct access to S3 objects encrypted with Customer Managed Keys (CMK) in AWS KMS through AWS Data Exchange. Subscribers can use these keys to decrypt, then use the encrypted S3 objects shared with them, without creating or managing copies.
* api-change:``directconnect``: [``botocore``] describe-direct-connect-gateway-associations includes a new status, updating, indicating that the association is currently in-process of updating.
* api-change:``ec2``: [``botocore``] This release adds a new DnsOptions key (PrivateDnsOnlyForInboundResolverEndpoint) to CreateVpcEndpoint and ModifyVpcEndpoint APIs.
* api-change:``iam``: [``botocore``] Documentation only updates to correct customer-reported issues
* api-change:``keyspaces``: [``botocore``] Adding support for client-side timestamps


1.26.90
=======

* api-change:``appintegrations``: [``botocore``] Adds FileConfiguration to Amazon AppIntegrations CreateDataIntegration supporting scheduled downloading of third party files into Amazon Connect from sources such as Microsoft SharePoint.
* api-change:``lakeformation``: [``botocore``] This release updates the documentation regarding Get/Update DataCellsFilter
* api-change:``s3control``: [``botocore``] Added support for cross-account Multi-Region Access Points. Added support for S3 Replication for S3 on Outposts.
* api-change:``tnb``: [``botocore``] This release adds tagging support to the following Network Instance APIs : Instantiate, Update, Terminate.
* api-change:``wisdom``: [``botocore``] This release extends Wisdom CreateKnowledgeBase API to support SharePoint connector type by removing the @required trait for objectField


1.26.89
=======

* api-change:``ivschat``: [``botocore``] This release adds a new exception returned when calling AWS IVS chat UpdateLoggingConfiguration. Now UpdateLoggingConfiguration can return ConflictException when invalid updates are made in sequence to Logging Configurations.
* api-change:``secretsmanager``: [``botocore``] The type definitions of SecretString and SecretBinary now have a minimum length of 1 in the model to match the exception thrown when you pass in empty values.


1.26.88
=======

* api-change:``codeartifact``: [``botocore``] This release introduces the generic package format, a mechanism for storing arbitrary binary assets. It also adds a new API, PublishPackageVersion, to allow for publishing generic packages.
* api-change:``connect``: [``botocore``] This release adds a new API, GetMetricDataV2, which returns metric data for Amazon Connect.
* api-change:``evidently``: [``botocore``] Updated entity override documentation
* api-change:``networkmanager``: [``botocore``] This update provides example usage for TransitGatewayRouteTableArn.
* api-change:``quicksight``: [``botocore``] This release has two changes: add state persistence feature for embedded dashboard and console in GenerateEmbedUrlForRegisteredUser API; add properties for hidden collapsed row dimensions in PivotTableOptions.
* api-change:``redshift-data``: [``botocore``] Added support for Redshift Serverless workgroup-arn wherever the WorkgroupName parameter is available.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Inference now allows SSM access to customer's model container by setting the "EnableSSMAccess" parameter for a ProductionVariant in CreateEndpointConfig API.
* api-change:``servicediscovery``: [``botocore``] Updated all AWS Cloud Map APIs to provide consistent throttling exception (RequestLimitExceeded)
* api-change:``sesv2``: [``botocore``] This release introduces a new recommendation in Virtual Deliverability Manager Advisor, which detects missing or misconfigured Brand Indicator for Message Identification (BIMI) DNS records for customer sending identities.


1.26.87
=======

* api-change:``athena``: [``botocore``] A new field SubstatementType is added to GetQueryExecution API, so customers have an error free way to detect the query type and interpret the result.
* api-change:``dynamodb``: [``botocore``] Adds deletion protection support to DynamoDB tables. Tables with deletion protection enabled cannot be deleted. Deletion protection is disabled by default, can be enabled via the CreateTable or UpdateTable APIs, and is visible in TableDescription. This setting is not replicated for Global Tables.
* api-change:``ec2``: [``botocore``] Introducing Amazon EC2 C7g, M7g and R7g instances, powered by the latest generation AWS Graviton3 processors and deliver up to 25% better performance over Graviton2-based instances.
* api-change:``lakeformation``: [``botocore``] This release adds two new API support "GetDataCellsFiler" and "UpdateDataCellsFilter", and also updates the corresponding documentation.
* api-change:``mediapackage-vod``: [``botocore``] This release provides the date and time VOD resources were created.
* api-change:``mediapackage``: [``botocore``] This release provides the date and time live resources were created.
* api-change:``route53resolver``: [``botocore``] Add dual-stack and IPv6 support for Route 53 Resolver Endpoint,Add IPv6 target IP in Route 53 Resolver Forwarding Rule
* api-change:``sagemaker``: [``botocore``] There needs to be a user identity to specify the SageMaker user who perform each action regarding the entity. However, these is a not a unified concept of user identity across SageMaker service that could be used today.


1.26.86
=======

* api-change:``dms``: [``botocore``] This release adds DMS Fleet Advisor Target Recommendation APIs and exposes functionality for DMS Fleet Advisor. It adds functionality to start Target Recommendation calculation.
* api-change:``location``: [``botocore``] Documentation update for the release of 3 additional map styles for use with Open Data Maps: Open Data Standard Dark, Open Data Visualization Light & Open Data Visualization Dark.


1.26.85
=======

* api-change:``account``: [``botocore``] AWS Account alternate contact email addresses can now have a length of 254 characters and contain the character "|".
* api-change:``ivs``: [``botocore``] Updated text description in DeleteChannel, Stream, and StreamSummary.


1.26.84
=======

* api-change:``dynamodb``: [``botocore``] Documentation updates for DynamoDB.
* api-change:``ec2``: [``botocore``] This release adds support for a new boot mode for EC2 instances called 'UEFI Preferred'.
* api-change:``macie2``: [``botocore``] Documentation updates for Amazon Macie
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has improved handling for different input and output color space combinations.
* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive adds support for Nielsen watermark timezones.
* api-change:``transcribe``: [``botocore``] Amazon Transcribe now supports role access for these API operations: CreateVocabulary, UpdateVocabulary, CreateVocabularyFilter, and UpdateVocabularyFilter.


1.26.83
=======

* api-change:``iot``: [``botocore``] A recurring maintenance window is an optional configuration used for rolling out the job document to all devices in the target group observing a predetermined start time, duration, and frequency that the maintenance window occurs.
* api-change:``migrationhubstrategy``: [``botocore``] This release updates the File Import API to allow importing servers already discovered by customers with reduced pre-requisites.
* api-change:``organizations``: [``botocore``] This release introduces a new reason code, ACCOUNT_CREATION_NOT_COMPLETE, to ConstraintViolationException in CreateOrganization API.
* api-change:``pi``: [``botocore``] This release adds a new field PeriodAlignment to allow the customer specifying the returned timestamp of time periods to be either the start or end time.
* api-change:``pipes``: [``botocore``] This release fixes some input parameter range and patterns.
* api-change:``sagemaker``: [``botocore``] Add a new field "EndpointMetrics" in SageMaker Inference Recommender "ListInferenceRecommendationsJobSteps" API response.


1.26.82
=======

* api-change:``codecatalyst``: [``botocore``] Published Dev Environments StopDevEnvironmentSession API
* api-change:``pricing``: [``botocore``] This release adds 2 new APIs - ListPriceLists which returns a list of applicable price lists, and GetPriceListFileUrl which outputs a URL to retrieve your price lists from the generated file from ListPriceLists
* api-change:``s3outposts``: [``botocore``] S3 on Outposts introduces a new API ListOutpostsWithS3, with this API you can list all your Outposts with S3 capacity.


1.26.81
=======

* enhancement:Documentation: Splits service documentation into multiple sub-pages for better organization and faster loading time.
* enhancement:Documentation: [``botocore``] Splits service documentation into multiple sub-pages for better organization and faster loading time.
* api-change:``comprehend``: [``botocore``] Amazon Comprehend now supports flywheels to help you train and manage new model versions for custom models.
* api-change:``ec2``: [``botocore``] This release allows IMDS support to be set to v2-only on an existing AMI, so that all future instances launched from that AMI will use IMDSv2 by default.
* api-change:``kms``: [``botocore``] AWS KMS is deprecating the RSAES_PKCS1_V1_5 wrapping algorithm option in the GetParametersForImport API that is used in the AWS KMS Import Key Material feature. AWS KMS will end support for this wrapping algorithm by October 1, 2023.
* api-change:``lightsail``: [``botocore``] This release adds Lightsail for Research feature support, such as GUI session access, cost estimates, stop instance on idle, and disk auto mount.
* api-change:``managedblockchain``: [``botocore``] This release adds support for tagging to the accessor resource in Amazon Managed Blockchain
* api-change:``omics``: [``botocore``] Minor model changes to accomodate batch imports feature


1.26.80
=======

* api-change:``devops-guru``: [``botocore``] This release adds the description field on ListAnomaliesForInsight and DescribeAnomaly API responses for proactive anomalies.
* api-change:``drs``: [``botocore``] New fields were added to reflect availability zone data in source server and recovery instance description commands responses, as well as source server launch status.
* api-change:``internetmonitor``: [``botocore``] CloudWatch Internet Monitor is a a new service within CloudWatch that will help application developers and network engineers continuously monitor internet performance metrics such as availability and performance between their AWS-hosted applications and end-users of these applications
* api-change:``lambda``: [``botocore``] This release adds the ability to create ESMs with Document DB change streams as event source. For more information see  https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html.
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has added support for HDR10 to SDR tone mapping, and animated GIF video input sources.
* api-change:``timestream-write``: [``botocore``] This release adds the ability to ingest batched historical data or migrate data in bulk from S3 into Timestream using CSV files.


1.26.79
=======

* api-change:``connect``: [``botocore``] StartTaskContact API now supports linked task creation with a new optional RelatedContactId parameter
* api-change:``connectcases``: [``botocore``] This release adds the ability to delete domains through the DeleteDomain API. For more information see https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html
* api-change:``redshift``: [``botocore``] Documentation updates for Redshift API bringing it in line with IAM best practices.
* api-change:``securityhub``: [``botocore``] New Security Hub APIs and updates to existing APIs that help you consolidate control findings and enable and disable controls across all supported standards
* api-change:``servicecatalog``: [``botocore``] Documentation updates for Service Catalog


1.26.78
=======

* api-change:``appflow``: [``botocore``] This release enables the customers to choose whether to use Private Link for Metadata and Authorization call when using a private Salesforce connections
* api-change:``ecs``: [``botocore``] This release supports deleting Amazon ECS task definitions that are in the INACTIVE state.
* api-change:``grafana``: [``botocore``] Doc-only update. Updated information on attached role policies for customer provided roles
* api-change:``guardduty``: [``botocore``] Updated API and data types descriptions for CreateFilter, UpdateFilter, and TriggerDetails.
* api-change:``iotwireless``: [``botocore``] In this release, we add additional capabilities for the FUOTA which allows user to configure the fragment size, the sending interval and the redundancy ratio of the FUOTA tasks
* api-change:``location``: [``botocore``] This release adds support for using Maps APIs with an API Key in addition to AWS Cognito. This includes support for adding, listing, updating and deleting API Keys.
* api-change:``macie2``: [``botocore``] This release adds support for a new finding type, Policy:IAMUser/S3BucketSharedWithCloudFront, and S3 bucket metadata that indicates if a bucket is shared with an Amazon CloudFront OAI or OAC.
* api-change:``wafv2``: [``botocore``] You can now associate an AWS WAF v2 web ACL with an AWS App Runner service.


1.26.77
=======

* api-change:``chime-sdk-voice``: [``botocore``] This release introduces support for Voice Connector media metrics in the Amazon Chime SDK Voice namespace
* api-change:``cloudfront``: [``botocore``] CloudFront now supports block lists in origin request policies so that you can forward all headers, cookies, or query string from viewer requests to the origin *except* for those specified in the block list.
* api-change:``datasync``: [``botocore``] AWS DataSync has relaxed the minimum length constraint of AccessKey for Object Storage locations to 1.
* api-change:``opensearch``: [``botocore``] This release lets customers configure Off-peak window and software update related properties for a new/existing domain. It enhances the capabilities of StartServiceSoftwareUpdate API; adds 2 new APIs - ListScheduledActions & UpdateScheduledAction; and allows Auto-tune to make use of Off-peak window.
* api-change:``rum``: [``botocore``] CloudWatch RUM now supports CloudWatch Custom Metrics
* api-change:``ssm``: [``botocore``] Document only update for Feb 2023


1.26.76
=======

* api-change:``quicksight``: [``botocore``] S3 data sources now accept a custom IAM role.
* api-change:``resiliencehub``: [``botocore``] In this release we improved resilience hub application creation and maintenance by introducing new resource and app component crud APIs, improving visibility and maintenance of application input sources and added support for additional information attributes to be provided by customers.
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub
* api-change:``tnb``: [``botocore``] This is the initial SDK release for AWS Telco Network Builder (TNB). AWS Telco Network Builder is a network automation service that helps you deploy and manage telecom networks.


1.26.75
=======

* bugfix:SSO: [``botocore``] Fixes aws/aws-cli`#7496 <https://github.com/aws/aws-cli/issues/7496>`__ by using the correct profile name rather than the one set in the session.
* api-change:``auditmanager``: [``botocore``] This release introduces a ServiceQuotaExceededException to the UpdateAssessmentFrameworkShare API operation.
* api-change:``connect``: [``botocore``] Reasons for failed diff has been approved by SDK Reviewer


1.26.74
=======

* api-change:``apprunner``: [``botocore``] This release supports removing MaxSize limit for AutoScalingConfiguration.
* api-change:``glue``: [``botocore``] Release of Delta Lake Data Lake Format for Glue Studio Service


1.26.73
=======

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``grafana``: [``botocore``] With this release Amazon Managed Grafana now supports inbound Network Access Control that helps you to restrict user access to your Grafana workspaces
* api-change:``ivs``: [``botocore``] Doc-only update. Updated text description in DeleteChannel, Stream, and StreamSummary.
* api-change:``wafv2``: [``botocore``] Added a notice for account takeover prevention (ATP). The interface incorrectly lets you to configure ATP response inspection in regional web ACLs in Region US East (N. Virginia), without returning an error. ATP response inspection is only available in web ACLs that protect CloudFront distributions.


1.26.72
=======

* api-change:``cloudtrail``: [``botocore``] This release adds an InsufficientEncryptionPolicyException type to the StartImport endpoint
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``frauddetector``: [``botocore``] This release introduces Lists feature which allows customers to reference a set of values in Fraud Detector's rules. With Lists, customers can dynamically manage these attributes in real time. Lists can be created/deleted and its contents can be modified using the Fraud Detector API.
* api-change:``glue``: [``botocore``] Fix DirectJDBCSource not showing up in CLI code gen
* api-change:``privatenetworks``: [``botocore``] This release introduces a new StartNetworkResourceUpdate API, which enables return/replacement of hardware from a NetworkSite.
* api-change:``rds``: [``botocore``] Database Activity Stream support for RDS for SQL Server.
* api-change:``wafv2``: [``botocore``] For protected CloudFront distributions, you can now use the AWS WAF Fraud Control account takeover prevention (ATP) managed rule group to block new login attempts from clients that have recently submitted too many failed login attempts.


1.26.71
=======

* api-change:``appconfig``: [``botocore``] AWS AppConfig now offers the option to set a version label on hosted configuration versions. Version labels allow you to identify specific hosted configuration versions based on an alternate versioning scheme that you define.
* api-change:``datasync``: [``botocore``] With this launch, we are giving customers the ability to use older SMB protocol versions, enabling them to use DataSync to copy data to and from their legacy storage arrays.
* api-change:``ec2``: [``botocore``] With this release customers can turn host maintenance on or off when allocating or modifying a supported dedicated host. Host maintenance is turned on by default for supported hosts.


1.26.70
=======

* api-change:``account``: [``botocore``] This release of the Account Management API enables customers to view and manage whether AWS Opt-In Regions are enabled or disabled for their Account. For more information, see https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html
* api-change:``appconfigdata``: [``botocore``] AWS AppConfig now offers the option to set a version label on hosted configuration versions. If a labeled hosted configuration version is deployed, its version label is available in the GetLatestConfiguration response.
* api-change:``snowball``: [``botocore``] Adds support for EKS Anywhere on Snowball. AWS Snow Family customers can now install EKS Anywhere service on Snowball Edge Compute Optimized devices.


1.26.69
=======

* api-change:``autoscaling``: [``botocore``] You can now either terminate/replace, ignore, or wait for EC2 Auto Scaling instances on standby or protected from scale in. Also, you can also roll back changes from a failed instance refresh.
* api-change:``connect``: [``botocore``] This update provides the Wisdom session ARN for contacts enabled for Wisdom in the chat channel.
* api-change:``ec2``: [``botocore``] Adds support for waiters that automatically poll for an imported snapshot until it reaches the completed state.
* api-change:``polly``: [``botocore``] Amazon Polly adds two new neural Japanese voices - Kazuha, Tomoko
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds support for selecting algorithms in CreateAutoMLJob API.
* api-change:``sns``: [``botocore``] This release adds support for SNS X-Ray active tracing as well as other updates.


1.26.68
=======

* api-change:``chime-sdk-meetings``: [``botocore``] Documentation updates for Chime Meetings SDK
* api-change:``emr-containers``: [``botocore``] EMR on EKS allows configuring retry policies for job runs through the StartJobRun API. Using retry policies, a job cause a driver pod to be restarted automatically if it fails or is deleted. The job's status can be seen in the DescribeJobRun and ListJobRun APIs and monitored using CloudWatch events.
* api-change:``evidently``: [``botocore``] Updated entity overrides parameter to accept up to 2500 overrides or a total of 40KB.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``lightsail``: [``botocore``] Documentation updates for Lightsail
* api-change:``migration-hub-refactor-spaces``: [``botocore``] This release adds support for creating environments with a network fabric type of NONE
* api-change:``workdocs``: [``botocore``] Doc only update for the WorkDocs APIs.
* api-change:``workspaces``: [``botocore``] Removed Windows Server 2016 BYOL and made changes based on IAM campaign.


1.26.67
=======

* api-change:``backup``: [``botocore``] This release added one attribute (resource name) in the output model of our 9 existing APIs in AWS backup so that customers will see the resource name at the output. No input required from Customers.
* api-change:``cloudfront``: [``botocore``] CloudFront Origin Access Control extends support to AWS Elemental MediaStore origins.
* api-change:``glue``: [``botocore``] DirectJDBCSource + Glue 4.0 streaming options
* api-change:``lakeformation``: [``botocore``] This release removes the LFTagpolicyResource expression limits.


1.26.66
=======

* api-change:``transfer``: [``botocore``] Updated the documentation for the ImportCertificate API call, and added examples.


1.26.65
=======

* api-change:``compute-optimizer``: [``botocore``] AWS Compute optimizer can now infer if Kafka is running on an instance.
* api-change:``customer-profiles``: [``botocore``] This release deprecates the PartyType and Gender enum data types from the Profile model and replaces them with new PartyTypeString and GenderString attributes, which accept any string of length up to 255.
* api-change:``frauddetector``: [``botocore``] My AWS Service (Amazon Fraud Detector) - This release introduces Cold Start Model Training which optimizes training for small datasets and adds intelligent methods for treating unlabeled data. You can now train Online Fraud Insights or Transaction Fraud Insights models with minimal historical-data.
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has added improved scene change detection capabilities and a bandwidth reduction filter, along with video quality enhancements, to the AVC encoder.
* api-change:``outposts``: [``botocore``] Adds OrderType to Order structure. Adds PreviousOrderId and PreviousLineItemId to LineItem structure. Adds new line item status REPLACED. Increases maximum length of pagination token.


1.26.64
=======

* enhancement:AWSCRT: [``botocore``] Upgrade awscrt version to 0.16.9
* api-change:``proton``: [``botocore``] Add new GetResourcesSummary API
* api-change:``redshift``: [``botocore``] Corrects descriptions of the parameters for the API operations RestoreFromClusterSnapshot, RestoreTableFromClusterSnapshot, and CreateCluster.


1.26.63
=======

* api-change:``appconfig``: [``botocore``] AWS AppConfig introduces KMS customer-managed key (CMK) encryption of configuration data, along with AWS Secrets Manager as a new configuration data source. S3 objects using SSE-KMS encryption and SSM Parameter Store SecureStrings are also now supported.
* api-change:``connect``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``ec2``: [``botocore``] Documentation updates for EC2.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``keyspaces``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``quicksight``: [``botocore``] QuickSight support for Radar Chart and Dashboard Publish Options
* api-change:``redshift``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``sso-admin``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.


1.26.62
=======

* bugfix:``s3``: [``botocore``] boto3 no longer overwrites user supplied `Content-Encoding` with `aws-chunked` when user also supplies `ChecksumAlgorithm`.
* api-change:``devops-guru``: [``botocore``] This release adds filter support ListAnomalyForInsight API.
* api-change:``forecast``: [``botocore``] This release will enable customer select INCREMENTAL as ImportModel in Forecast's CreateDatasetImportJob API. Verified latest SDK containing required attribute, following https://w.amazon.com/bin/view/AWS-Seer/Launch/Trebuchet/
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``mediatailor``: [``botocore``] The AWS Elemental MediaTailor SDK for Channel Assembly has added support for program updates, and the ability to clip the end of VOD sources in programs.
* api-change:``sns``: [``botocore``] Additional attributes added for set-topic-attributes.


1.26.61
=======

* api-change:``accessanalyzer``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``appsync``: [``botocore``] This release introduces the feature to support EventBridge as AppSync data source.
* api-change:``cloudtrail-data``: [``botocore``] Add CloudTrail Data Service to enable users to ingest activity events from non-AWS sources into CloudTrail Lake.
* api-change:``cloudtrail``: [``botocore``] Add new "Channel" APIs to enable users to manage channels used for CloudTrail Lake integrations, and "Resource Policy" APIs to enable users to manage the resource-based permissions policy attached to a channel.
* api-change:``codeartifact``: [``botocore``] This release introduces a new DeletePackage API, which enables deletion of a package and all of its versions from a repository.
* api-change:``connectparticipant``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``ec2``: [``botocore``] This launch allows customers to associate up to 8 IP addresses to their NAT Gateways to increase the limit on concurrent connections to a single destination by eight times from 55K to 440K.
* api-change:``groundstation``: [``botocore``] DigIF Expansion changes to the Customer APIs.
* api-change:``iot``: [``botocore``] Added support for IoT Rules Engine Cloudwatch Logs action batch mode.
* api-change:``kinesis``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``opensearch``: [``botocore``] Amazon OpenSearch Service adds the option for a VPC endpoint connection between two domains when the local domain uses OpenSearch version 1.3 or 2.3. You can now use remote reindex to copy indices from one VPC domain to another without a reverse proxy.
* api-change:``outposts``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``polly``: [``botocore``] Amazon Polly adds two new neural American English voices - Ruth, Stephen
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now supports more completion criteria for Hyperparameter Optimization.
* api-change:``securityhub``: [``botocore``] New fields have been added to the AWS Security Finding Format. Compliance.SecurityControlId is a unique identifier for a security control across standards. Compliance.AssociatedStandards contains all enabled standards in which a security control is enabled.
* api-change:``support``: [``botocore``] This fixes incorrect endpoint construction when a customer is explicitly setting a region.


1.26.60
=======

* api-change:``clouddirectory``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``cloudformation``: [``botocore``] This feature provides a method of obtaining which regions a stackset has stack instances deployed in.
* api-change:``discovery``: [``botocore``] Update ImportName validation to 255 from the current length of 100
* api-change:``dlm``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``ec2``: [``botocore``] We add Prefix Lists as a new route destination option for LocalGatewayRoutes. This will allow customers to create routes to Prefix Lists. Prefix List routes will allow customers to group individual CIDR routes with the same target into a single route.
* api-change:``imagebuilder``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``kafka``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``mediaconvert``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``swf``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.


1.26.59
=======

* api-change:``application-autoscaling``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``appstream``: [``botocore``] Fixing the issue where Appstream waiters hang for fleet_started and fleet_stopped.
* api-change:``elasticbeanstalk``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``fis``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``glacier``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``greengrass``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.
* api-change:``greengrassv2``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) in SDK.
* api-change:``mediatailor``: [``botocore``] This release introduces the As Run logging type, along with API and documentation updates.
* api-change:``outposts``: [``botocore``] Adding support for payment term in GetOrder, CreateOrder responses.
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] This release supports running SageMaker Training jobs with container images that are in a private Docker registry.
* api-change:``serverlessrepo``: [``botocore``] Enabled FIPS endpoints for GovCloud (US) regions in SDK.


1.26.58
=======

* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``iotfleetwise``: [``botocore``] Add model validation to BatchCreateVehicle and BatchUpdateVehicle operations that invalidate requests with an empty vehicles list.
* api-change:``s3``: [``botocore``] Allow FIPS to be used with path-style URLs.


1.26.57
=======

* api-change:``cloudformation``: [``botocore``] Enabled FIPS aws-us-gov endpoints in SDK.
* api-change:``ec2``: [``botocore``] This release adds new functionality that allows customers to provision IPv6 CIDR blocks through Amazon VPC IP Address Manager (IPAM) as well as allowing customers to utilize IPAM Resource Discovery APIs.
* api-change:``m2``: [``botocore``] Add returnCode, batchJobIdentifier in GetBatchJobExecution response, for user to view the batch job execution result & unique identifier from engine. Also removed unused headers from REST APIs
* api-change:``polly``: [``botocore``] Add 5 new neural voices - Sergio (es-ES), Andres (es-MX), Remi (fr-FR), Adriano (it-IT) and Thiago (pt-BR).
* api-change:``redshift-serverless``: [``botocore``] Added query monitoring rules as possible parameters for create and update workgroup operations.
* api-change:``s3control``: [``botocore``] Add additional endpoint tests for S3 Control. Fix missing endpoint parameters for PutBucketVersioning and GetBucketVersioning. Prior to this fix, those operations may have resulted in an invalid endpoint being resolved.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now decouples from Model Registry and could accept Model Name to invoke inference recommendations job; Inference Recommender now provides CPU/Memory Utilization metrics data in recommendation output.
* api-change:``sts``: [``botocore``] Doc only change to update wording in a key topic


1.26.56
=======

* api-change:``databrew``: [``botocore``] Enabled FIPS us-gov-west-1 endpoints in SDK.
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Asia Pacific (Melbourne) Region (ap-southeast-4) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``ssm-sap``: [``botocore``] This release provides updates to documentation and support for listing operations performed by AWS Systems Manager for SAP.


1.26.55
=======

* api-change:``lambda``: [``botocore``] Release Lambda RuntimeManagementConfig, enabling customers to better manage runtime updates to their Lambda functions. This release adds two new APIs, GetRuntimeManagementConfig and PutRuntimeManagementConfig, as well as support on existing Create/Get/Update function APIs.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Inference now supports P4de instance types.


1.26.54
=======

* api-change:``ec2``: [``botocore``] C6in, M6in, M6idn, R6in and R6idn instances are powered by 3rd Generation Intel Xeon Scalable processors (code named Ice Lake) with an all-core turbo frequency of 3.5 GHz.
* api-change:``ivs``: [``botocore``] API and Doc update. Update to arns field in BatchGetStreamKey. Also updates to operations and structures.
* api-change:``quicksight``: [``botocore``] This release adds support for data bars in QuickSight table and increases pivot table field well limit.


1.26.53
=======

* api-change:``appflow``: [``botocore``] Adding support for Salesforce Pardot connector in Amazon AppFlow.
* api-change:``codeartifact``: [``botocore``] Documentation updates for CodeArtifact
* api-change:``connect``: [``botocore``] Amazon Connect Chat introduces Persistent Chat, allowing customers to resume previous conversations with context and transcripts carried over from previous chats, eliminating the need to repeat themselves and allowing agents to provide personalized service with access to entire conversation history.
* api-change:``connectparticipant``: [``botocore``] This release updates Amazon Connect Participant's GetTranscript api to provide transcripts of past chats on a persistent chat session.
* api-change:``ec2``: [``botocore``] Adds SSM Parameter Resource Aliasing support to EC2 Launch Templates. Launch Templates can now store parameter aliases in place of AMI Resource IDs. CreateLaunchTemplateVersion and DescribeLaunchTemplateVersions now support a convenience flag, ResolveAlias, to return the resolved parameter value.
* api-change:``glue``: [``botocore``] Release Glue Studio Hudi Data Lake Format for SDK/CLI
* api-change:``groundstation``: [``botocore``] Add configurable prepass and postpass times for DataflowEndpointGroup. Add Waiter to allow customers to wait for a contact that was reserved through ReserveContact
* api-change:``logs``: [``botocore``] Bug fix - Removed the regex pattern validation from CoralModel to avoid potential security issue.
* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive adds support for SCTE 35 preRollMilliSeconds.
* api-change:``opensearch``: [``botocore``] This release adds the enhanced dry run option, that checks for validation errors that might occur when deploying configuration changes and provides a summary of these errors, if any. The feature will also indicate whether a blue/green deployment will be required to apply a change.
* api-change:``panorama``: [``botocore``] Added AllowMajorVersionUpdate option to OTAJobConfig to make appliance software major version updates opt-in.
* api-change:``sagemaker``: [``botocore``] HyperParameterTuningJobs now allow passing environment variables into the corresponding TrainingJobs


1.26.52
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``ivschat``: [``botocore``] Updates the range for a Chat Room's maximumMessageRatePerSecond field.
* api-change:``wafv2``: [``botocore``] Improved the visibility of the guidance for updating AWS WAF resources, such as web ACLs and rule groups.


1.26.51
=======

* api-change:``billingconductor``: [``botocore``] This release adds support for SKU Scope for pricing plans.
* api-change:``cloud9``: [``botocore``] Added minimum value to AutomaticStopTimeMinutes parameter.
* api-change:``imagebuilder``: [``botocore``] Add support for AWS Marketplace product IDs as input during CreateImageRecipe for the parent-image parameter. Add support for listing third-party components.
* api-change:``network-firewall``: [``botocore``] Network Firewall now allows creation of dual stack endpoints, enabling inspection of IPv6 traffic.


1.26.50
=======

* api-change:``connect``: [``botocore``] This release updates the responses of UpdateContactFlowContent, UpdateContactFlowMetadata, UpdateContactFlowName and DeleteContactFlow API with empty responses.
* api-change:``ec2``: [``botocore``] Documentation updates for EC2.
* api-change:``outposts``: [``botocore``] This release adds POWER_30_KVA as an option for PowerDrawKva. PowerDrawKva is part of the RackPhysicalProperties structure in the CreateSite request.
* api-change:``resource-groups``: [``botocore``] AWS Resource Groups customers can now turn on Group Lifecycle Events in their AWS account. When you turn this on, Resource Groups monitors your groups for changes to group state or membership. Those changes are sent to Amazon EventBridge as events that you can respond to using rules you create.


1.26.49
=======

* api-change:``cleanrooms``: [``botocore``] Initial release of AWS Clean Rooms
* api-change:``lambda``: [``botocore``] Add support for MaximumConcurrency parameter for SQS event source. Customers can now limit the maximum concurrent invocations for their SQS Event Source Mapping.
* api-change:``logs``: [``botocore``] Bug fix: logGroupName is now not a required field in GetLogEvents, FilterLogEvents, GetLogGroupFields, and DescribeLogStreams APIs as logGroupIdentifier can be provided instead
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has added support for compact DASH manifest generation, audio normalization using TruePeak measurements, and the ability to clip the sample range in the color corrector.
* api-change:``secretsmanager``: [``botocore``] Update documentation for new ListSecrets and DescribeSecret parameters


1.26.48
=======

* api-change:``kendra``: [``botocore``] This release adds support to new document types - RTF, XML, XSLT, MS_EXCEL, CSV, JSON, MD


1.26.47
=======

* api-change:``location``: [``botocore``] This release adds support for two new route travel models, Bicycle and Motorcycle which can be used with Grab data source.
* api-change:``rds``: [``botocore``] This release adds support for configuring allocated storage on the CreateDBInstanceReadReplica, RestoreDBInstanceFromDBSnapshot, and RestoreDBInstanceToPointInTime APIs.


1.26.46
=======

* api-change:``ecr-public``: [``botocore``] This release for Amazon ECR Public makes several change to bring the SDK into sync with the API.
* api-change:``kendra-ranking``: [``botocore``] Introducing Amazon Kendra Intelligent Ranking, a new set of Kendra APIs that leverages Kendra semantic ranking capabilities to improve the quality of search results from other search services (i.e. OpenSearch, ElasticSearch, Solr).
* api-change:``network-firewall``: [``botocore``] Network Firewall now supports the Suricata rule action reject, in addition to the actions pass, drop, and alert.
* api-change:``ram``: [``botocore``] Enabled FIPS aws-us-gov endpoints in SDK.
* api-change:``workspaces-web``: [``botocore``] This release adds support for a new portal authentication type: AWS IAM Identity Center (successor to AWS Single Sign-On).


1.26.45
=======

* api-change:``acm-pca``: [``botocore``] Added revocation parameter validation: bucket names must match S3 bucket naming rules and CNAMEs conform to RFC2396 restrictions on the use of special characters in URIs.
* api-change:``auditmanager``: [``botocore``] This release introduces a new data retention option in your Audit Manager settings. You can now use the DeregistrationPolicy parameter to specify if you want to delete your data when you deregister Audit Manager.


1.26.44
=======

* api-change:``amplifybackend``: [``botocore``] Updated GetBackendAPIModels response to include ModelIntrospectionSchema json string
* api-change:``apprunner``: [``botocore``] This release adds support of securely referencing secrets and configuration data that are stored in Secrets Manager and SSM Parameter Store by adding them as environment secrets in your App Runner service.
* api-change:``connect``: [``botocore``] Documentation update for a new Initiation Method value in DescribeContact API
* api-change:``emr-serverless``: [``botocore``] Adds support for customized images. You can now provide runtime images when creating or updating EMR Serverless Applications.
* api-change:``lightsail``: [``botocore``] Documentation updates for Amazon Lightsail.
* api-change:``mwaa``: [``botocore``] MWAA supports Apache Airflow version 2.4.3.
* api-change:``rds``: [``botocore``] This release adds support for specifying which certificate authority (CA) to use for a DB instance's server certificate during DB instance creation, as well as other CA enhancements.


1.26.43
=======

* api-change:``application-autoscaling``: [``botocore``] Customers can now use the existing DescribeScalingActivities API to also see the detailed and machine-readable reasons for Application Auto Scaling not scaling their resources and, if needed, take the necessary corrective actions.
* api-change:``logs``: [``botocore``] Update to remove sequenceToken as a required field in PutLogEvents calls.
* api-change:``ssm``: [``botocore``] Adding support for QuickSetup Document Type in Systems Manager


1.26.42
=======

* api-change:``securitylake``: [``botocore``] Allow CreateSubscriber API to take string input that allows setting more descriptive SubscriberDescription field. Make souceTypes field required in model level for UpdateSubscriberRequest as it is required for every API call on the backend. Allow ListSubscribers take any String as nextToken param.


1.26.41
=======

* api-change:``cloudfront``: [``botocore``] Extend response headers policy to support removing headers from viewer responses
* api-change:``iotfleetwise``: [``botocore``] Update documentation - correct the epoch constant value of default value for expiryTime field in CreateCampaign request.


1.26.40
=======

* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``secretsmanager``: [``botocore``] Added owning service filter, include planned deletion flag, and next rotation date response parameter in ListSecrets.
* api-change:``wisdom``: [``botocore``] This release extends Wisdom CreateContent and StartContentUpload APIs to support PDF and MicrosoftWord docx document uploading.


1.26.39
=======

* api-change:``elasticache``: [``botocore``] This release allows you to modify the encryption in transit setting, for existing Redis clusters. You can now change the TLS configuration of your Redis clusters without the need to re-build or re-provision the clusters or impact application availability.
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall now provides status messages for firewalls to help you troubleshoot when your endpoint fails.
* api-change:``rds``: [``botocore``] This release adds support for Custom Engine Version (CEV) on RDS Custom SQL Server.
* api-change:``route53-recovery-control-config``: [``botocore``] Added support for Python paginators in the route53-recovery-control-config List* APIs.


1.26.38
=======

* api-change:``memorydb``: [``botocore``] This release adds support for MemoryDB Reserved nodes which provides a significant discount compared to on-demand node pricing. Reserved nodes are not physical nodes, but rather a billing discount applied to the use of on-demand nodes in your account.
* api-change:``transfer``: [``botocore``] Add additional operations to throw ThrottlingExceptions


1.26.37
=======

* api-change:``connect``: [``botocore``] Support for Routing Profile filter, SortCriteria, and grouping by Routing Profiles for GetCurrentMetricData API. Support for RoutingProfiles, UserHierarchyGroups, and Agents as filters, NextStatus and AgentStatusName for GetCurrentUserData. Adds ApproximateTotalCount to both APIs.
* api-change:``connectparticipant``: [``botocore``] Amazon Connect Chat introduces the Message Receipts feature. This feature allows agents and customers to receive message delivered and read receipts after they send a chat message.
* api-change:``detective``: [``botocore``] This release adds a missed AccessDeniedException type to several endpoints.
* api-change:``fsx``: [``botocore``] Fix a bug where a recent release might break certain existing SDKs.
* api-change:``inspector2``: [``botocore``] Amazon Inspector adds support for scanning NodeJS 18.x and Go 1.x AWS Lambda function runtimes.


1.26.36
=======

* api-change:``compute-optimizer``: [``botocore``] This release enables AWS Compute Optimizer to analyze and generate optimization recommendations for ecs services running on Fargate.
* api-change:``connect``: [``botocore``] Amazon Connect Chat introduces the Idle Participant/Autodisconnect feature, which allows users to set timeouts relating to the activity of chat participants, using the new UpdateParticipantRoleConfig API.
* api-change:``iotdeviceadvisor``: [``botocore``] This release adds the following new features: 1) Documentation updates for IoT Device Advisor APIs. 2) Updated required request parameters for IoT Device Advisor APIs. 3) Added new service feature: ability to provide the test endpoint when customer executing the StartSuiteRun API.
* api-change:``kinesis-video-webrtc-storage``: [``botocore``] Amazon Kinesis Video Streams offers capabilities to stream video and audio in real-time via WebRTC to the cloud for storage, playback, and analytical processing. Customers can use our enhanced WebRTC SDK and cloud APIs to enable real-time streaming, as well as media ingestion to the cloud.
* api-change:``rds``: [``botocore``] Add support for managing master user password in AWS Secrets Manager for the DBInstance and DBCluster.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager


1.26.35
=======

* api-change:``connect``: [``botocore``] Amazon Connect Chat now allows for JSON (application/json) message types to be sent as part of the initial message in the StartChatContact API.
* api-change:``connectparticipant``: [``botocore``] Amazon Connect Chat now allows for JSON (application/json) message types to be sent in the SendMessage API.
* api-change:``license-manager-linux-subscriptions``: [``botocore``] AWS License Manager now offers cross-region, cross-account tracking of commercial Linux subscriptions on AWS. This includes subscriptions purchased as part of EC2 subscription-included AMIs, on the AWS Marketplace, or brought to AWS via Red Hat Cloud Access Program.
* api-change:``macie2``: [``botocore``] This release adds support for analyzing Amazon S3 objects that use the S3 Glacier Instant Retrieval (Glacier_IR) storage class.
* api-change:``sagemaker``: [``botocore``] This release enables adding RStudio Workbench support to an existing Amazon SageMaker Studio domain. It allows setting your RStudio on SageMaker environment configuration parameters and also updating the RStudioConnectUrl and RStudioPackageManagerUrl parameters for existing domains
* api-change:``scheduler``: [``botocore``] Updated the ListSchedules and ListScheduleGroups APIs to allow the NamePrefix field to start with a number. Updated the validation for executionRole field to support any role name.
* api-change:``ssm``: [``botocore``] Doc-only updates for December 2022.
* api-change:``support``: [``botocore``] Documentation updates for the AWS Support API
* api-change:``transfer``: [``botocore``] This release adds support for Decrypt as a workflow step type.


1.26.34
=======

* api-change:``batch``: [``botocore``] Adds isCancelled and isTerminated to DescribeJobs response.
* api-change:``ec2``: [``botocore``] Adds support for pagination in the EC2 DescribeImages API.
* api-change:``lookoutequipment``: [``botocore``] This release adds support for listing inference schedulers by status.
* api-change:``medialive``: [``botocore``] This release adds support for two new features to AWS Elemental MediaLive. First, you can now burn-in timecodes to your MediaLive outputs. Second, we now now support the ability to decode Dolby E audio when it comes in on an input.
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio now supports configuring session storage volumes and persistence, as well as backup and restore sessions through launch profiles.
* api-change:``resource-explorer-2``: [``botocore``] Documentation updates for AWS Resource Explorer.
* api-change:``route53domains``: [``botocore``] Use Route 53 domain APIs to change owner, create/delete DS record, modify IPS tag, resend authorization. New: AssociateDelegationSignerToDomain, DisassociateDelegationSignerFromDomain, PushDomain, ResendOperationAuthorization. Updated: UpdateDomainContact, ListOperations, CheckDomainTransferability.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds support for new objective metrics in CreateAutoMLJob API.
* api-change:``transcribe``: [``botocore``] Enable our batch transcription jobs for Swedish and Vietnamese.


1.26.33
=======

* api-change:``athena``: [``botocore``] Add missed InvalidRequestException in GetCalculationExecutionCode,StopCalculationExecution APIs. Correct required parameters (Payload and Type) in UpdateNotebook API. Change Notebook size from 15 Mb to 10 Mb.
* api-change:``ecs``: [``botocore``] This release adds support for alarm-based rollbacks in ECS, a new feature that allows customers to add automated safeguards for Amazon ECS service rolling updates.
* api-change:``kinesis-video-webrtc-storage``: [``botocore``] Amazon Kinesis Video Streams offers capabilities to stream video and audio in real-time via WebRTC to the cloud for storage, playback, and analytical processing. Customers can use our enhanced WebRTC SDK and cloud APIs to enable real-time streaming, as well as media ingestion to the cloud.
* api-change:``kinesisvideo``: [``botocore``] Amazon Kinesis Video Streams offers capabilities to stream video and audio in real-time via WebRTC to the cloud for storage, playback, and analytical processing. Customers can use our enhanced WebRTC SDK and cloud APIs to enable real-time streaming, as well as media ingestion to the cloud.
* api-change:``rds``: [``botocore``] Add support for --enable-customer-owned-ip to RDS create-db-instance-read-replica API for RDS on Outposts.
* api-change:``sagemaker``: [``botocore``] AWS Sagemaker - Sagemaker Images now supports Aliases as secondary identifiers for ImageVersions. SageMaker Images now supports additional metadata for ImageVersions for better images management.


1.26.32
=======

* enhancement:s3: s3.transfer methods accept path-like objects as input
* api-change:``appflow``: [``botocore``] This release updates the ListConnectorEntities API action so that it returns paginated responses that customers can retrieve with next tokens.
* api-change:``cloudfront``: [``botocore``] Updated documentation for CloudFront
* api-change:``datasync``: [``botocore``] AWS DataSync now supports the use of tags with task executions. With this new feature, you can apply tags each time you execute a task, giving you greater control and management over your task executions.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``guardduty``: [``botocore``] This release provides the valid characters for the Description and Name field.
* api-change:``iotfleetwise``: [``botocore``] Updated error handling for empty resource names in "UpdateSignalCatalog" and "GetModelManifest" operations.
* api-change:``sagemaker``: [``botocore``] AWS sagemaker - Features: This release adds support for random seed, it's an integer value used to initialize a pseudo-random number generator. Setting a random seed will allow the hyperparameter tuning search strategies to produce more consistent configurations for the same tuning job.


1.26.31
=======

* api-change:``backup-gateway``: [``botocore``] This release adds support for VMware vSphere tags, enabling customer to protect VMware virtual machines using tag-based policies for AWS tags mapped from vSphere tags. This release also adds support for customer-accessible gateway-hypervisor interaction log and upload bandwidth rate limit schedule.
* api-change:``connect``: [``botocore``] Added support for "English - New Zealand" and "English - South African" to be used with Amazon Connect Custom Vocabulary APIs.
* api-change:``ecs``: [``botocore``] This release adds support for container port ranges in ECS, a new capability that allows customers to provide container port ranges to simplify use cases where multiple ports are in use in a container. This release updates TaskDefinition mutation APIs and the Task description APIs.
* api-change:``eks``: [``botocore``] Add support for Windows managed nodes groups.
* api-change:``glue``: [``botocore``] This release adds support for AWS Glue Crawler with native DeltaLake tables, allowing Crawlers to classify Delta Lake format tables and catalog them for query engines to query against.
* api-change:``kinesis``: [``botocore``] Added StreamARN parameter for Kinesis Data Streams APIs. Added a new opaque pagination token for ListStreams. SDKs will auto-generate Account Endpoint when accessing Kinesis Data Streams.
* api-change:``location``: [``botocore``] This release adds support for a new style, "VectorOpenDataStandardLight" which can be used with the new data source, "Open Data Maps (Preview)".
* api-change:``m2``: [``botocore``] Adds an optional create-only `KmsKeyId` property to Environment and Application resources.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now allows customers to load tests their models on various instance types using private VPC.
* api-change:``securityhub``: [``botocore``] Added new resource details objects to ASFF, including resources for AwsEc2LaunchTemplate, AwsSageMakerNotebookInstance, AwsWafv2WebAcl and AwsWafv2RuleGroup.
* api-change:``translate``: [``botocore``] Raised the input byte size limit of the Text field in the TranslateText API to 10000 bytes.


1.26.30
=======

* api-change:``ce``: [``botocore``] This release supports percentage-based thresholds on Cost Anomaly Detection alert subscriptions.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``networkmanager``: [``botocore``] Appliance Mode support for AWS Cloud WAN.
* api-change:``redshift-data``: [``botocore``] This release adds a new --client-token field to ExecuteStatement and BatchExecuteStatement operations. Customers can now run queries with the additional client token parameter to ensures idempotency.
* api-change:``sagemaker-metrics``: [``botocore``] Update SageMaker Metrics documentation.


1.26.29
=======

* api-change:``cloudtrail``: [``botocore``] Merging mainline branch for service model into mainline release branch. There are no new APIs.
* api-change:``rds``: [``botocore``] This deployment adds ClientPasswordAuthType field to the Auth structure of the DBProxy.


1.26.28
=======

* bugfix:Endpoint provider: [``botocore``] Updates ARN parsing ``resourceId`` delimiters
* api-change:``customer-profiles``: [``botocore``] This release allows custom strings in PartyType and Gender through 2 new attributes in the CreateProfile and UpdateProfile APIs: PartyTypeString and GenderString.
* api-change:``ec2``: [``botocore``] This release updates DescribeFpgaImages to show supported instance types of AFIs in its response.
* api-change:``kinesisvideo``: [``botocore``] This release adds support for public preview of Kinesis Video Stream at Edge enabling customers to provide configuration for the Kinesis Video Stream EdgeAgent running on an on-premise IoT device. Customers can now locally record from cameras and stream videos to the cloud on configured schedule.
* api-change:``lookoutvision``: [``botocore``] This documentation update adds kms:GenerateDataKey as a required permission to StartModelPackagingJob.
* api-change:``migration-hub-refactor-spaces``: [``botocore``] This release adds support for Lambda alias service endpoints. Lambda alias ARNs can now be passed into CreateService.
* api-change:``rds``: [``botocore``] Update the RDS API model to support copying option groups during the CopyDBSnapshot operation
* api-change:``rekognition``: [``botocore``] Adds support for "aliases" and "categories", inclusion and exclusion filters for labels and label categories, and aggregating labels by video segment timestamps for Stored Video Label Detection APIs.
* api-change:``sagemaker-metrics``: [``botocore``] This release introduces support SageMaker Metrics APIs.
* api-change:``wafv2``: [``botocore``] Documents the naming requirement for logging destinations that you use with web ACLs.


1.26.27
=======

* api-change:``iotfleetwise``: [``botocore``] Deprecated assignedValue property for actuators and attributes.  Added a message to invalid nodes and invalid decoder manifest exceptions.
* api-change:``logs``: [``botocore``] Doc-only update for CloudWatch Logs, for Tagging Permissions clarifications
* api-change:``medialive``: [``botocore``] Link devices now support buffer size (latency) configuration. A higher latency value means a longer delay in transmitting from the device to MediaLive, but improved resiliency. A lower latency value means a shorter delay, but less resiliency.
* api-change:``mediapackage-vod``: [``botocore``] This release provides the approximate number of assets in a packaging group.


1.26.26
=======

* enhancement:Endpoint Provider Standard Library: [``botocore``] Correct spelling of 'library' in ``StandardLibrary`` class
* api-change:``autoscaling``: [``botocore``] Adds support for metric math for target tracking scaling policies, saving you the cost and effort of publishing a custom metric to CloudWatch. Also adds support for VPC Lattice by adding the Attach/Detach/DescribeTrafficSources APIs and a new health check type to the CreateAutoScalingGroup API.
* api-change:``iottwinmaker``: [``botocore``] This release adds the following new features: 1) New APIs for managing a continuous sync of assets and asset models from AWS IoT SiteWise. 2) Support user friendly names for component types (ComponentTypeName) and properties (DisplayName).
* api-change:``migrationhubstrategy``: [``botocore``] This release adds known application filtering, server selection for assessments, support for potential recommendations, and indications for configuration and assessment status. For more information, see the AWS Migration Hub documentation at https://docs.aws.amazon.com/migrationhub/index.html


1.26.25
=======

* api-change:``ce``: [``botocore``] This release adds the LinkedAccountName field to the GetAnomalies API response under RootCause
* api-change:``cloudfront``: [``botocore``] Introducing UpdateDistributionWithStagingConfig that can be used to promote the staging configuration to the production.
* api-change:``eks``: [``botocore``] Adds support for EKS add-ons configurationValues fields and DescribeAddonConfiguration function
* api-change:``kms``: [``botocore``] Updated examples and exceptions for External Key Store (XKS).


1.26.24
=======

* api-change:``billingconductor``: [``botocore``] This release adds the Tiering Pricing Rule feature.
* api-change:``connect``: [``botocore``] This release provides APIs that enable you to programmatically manage rules for Contact Lens conversational analytics and third party applications. For more information, see   https://docs.aws.amazon.com/connect/latest/APIReference/rules-api.html
* api-change:``dynamodb``: [``botocore``] Endpoint Ruleset update: Use http instead of https for the "local" region.
* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version
* api-change:``rds``: [``botocore``] This release adds the BlueGreenDeploymentNotFoundFault to the AddTagsToResource, ListTagsForResource, and RemoveTagsFromResource operations.
* api-change:``sagemaker-featurestore-runtime``: [``botocore``] For online + offline Feature Groups, added ability to target PutRecord and DeleteRecord actions to only online store, or only offline store. If target store parameter is not specified, actions will apply to both stores.


1.26.23
=======

* api-change:``ce``: [``botocore``] This release introduces two new APIs that offer a 1-click experience to refresh Savings Plans recommendations. The two APIs are StartSavingsPlansPurchaseRecommendationGeneration and ListSavingsPlansPurchaseRecommendationGeneration.
* api-change:``ec2``: [``botocore``] Documentation updates for EC2.
* api-change:``ivschat``: [``botocore``] Adds PendingVerification error type to messaging APIs to block the resource usage for accounts identified as being fraudulent.
* api-change:``rds``: [``botocore``] This release adds the InvalidDBInstanceStateFault to the RestoreDBClusterFromSnapshot operation.
* api-change:``transcribe``: [``botocore``] Amazon Transcribe now supports creating custom language models in the following languages: Japanese (ja-JP) and German (de-DE).


1.26.22
=======

* api-change:``appsync``: [``botocore``] Fixes the URI for the evaluatecode endpoint to include the /v1 prefix (ie. "/v1/dataplane-evaluatecode").
* api-change:``ecs``: [``botocore``] Documentation updates for Amazon ECS
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports Fortigate Cloud Native Firewall as a Service as a third-party policy type.
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has added support for configurable ID3 eMSG box attributes and the ability to signal them with InbandEventStream tags in DASH and CMAF outputs.
* api-change:``medialive``: [``botocore``] Updates to Event Signaling and Management (ESAM) API and documentation.
* api-change:``polly``: [``botocore``] Add language code for Finnish (fi-FI)
* api-change:``proton``: [``botocore``] CreateEnvironmentAccountConnection RoleArn input is now optional
* api-change:``redshift-serverless``: [``botocore``] Add Table Level Restore operations for Amazon Redshift Serverless. Add multi-port support for Amazon Redshift Serverless endpoints. Add Tagging support to Snapshots and Recovery Points in Amazon Redshift Serverless.
* api-change:``sns``: [``botocore``] This release adds the message payload-filtering feature to the SNS Subscribe, SetSubscriptionAttributes, and GetSubscriptionAttributes API actions


1.26.21
=======

* api-change:``codecatalyst``: [``botocore``] This release adds operations that support customers using the AWS Toolkits and Amazon CodeCatalyst, a unified software development service that helps developers develop, deploy, and maintain applications in the cloud. For more information, see the documentation.
* api-change:``comprehend``: [``botocore``] Comprehend now supports semi-structured documents (such as PDF files or image files) as inputs for custom analysis using the synchronous APIs (ClassifyDocument and DetectEntities).
* api-change:``gamelift``: [``botocore``] GameLift introduces a new feature, GameLift Anywhere. GameLift Anywhere allows you to integrate your own compute resources with GameLift. You can also use GameLift Anywhere to iteratively test your game servers without uploading the build to GameLift for every iteration.
* api-change:``pipes``: [``botocore``] AWS introduces new Amazon EventBridge Pipes which allow you to connect sources (SQS, Kinesis, DDB, Kafka, MQ) to Targets (14+ EventBridge Targets) without any code, with filtering, batching, input transformation, and an optional Enrichment stage (Lambda, StepFunctions, ApiGateway, ApiDestinations)
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version


1.26.20
=======

* api-change:``accessanalyzer``: [``botocore``] This release adds support for S3 cross account access points. IAM Access Analyzer will now produce public or cross account findings when it detects bucket delegation to external account access points.
* api-change:``athena``: [``botocore``] This release includes support for using Apache Spark in Amazon Athena.
* api-change:``dataexchange``: [``botocore``] This release enables data providers to license direct access to data in their Amazon S3 buckets or AWS Lake Formation data lakes through AWS Data Exchange. Subscribers get read-only access to the data and can use it in downstream AWS services, like Amazon Athena, without creating or managing copies.
* api-change:``docdb-elastic``: [``botocore``] Launched Amazon DocumentDB Elastic Clusters. You can now use the SDK to create, list, update and delete Amazon DocumentDB Elastic Cluster resources
* api-change:``glue``: [``botocore``] This release adds support for AWS Glue Data Quality, which helps you evaluate and monitor the quality of your data and includes the API for creating, deleting, or updating data quality rulesets, runs and evaluations.
* api-change:``s3control``: [``botocore``] Amazon S3 now supports cross-account access points. S3 bucket owners can now allow trusted AWS accounts to create access points associated with their bucket.
* api-change:``sagemaker-geospatial``: [``botocore``] This release provides Amazon SageMaker geospatial APIs to build, train, deploy and visualize geospatial models.
* api-change:``sagemaker``: [``botocore``] Added Models as part of the Search API. Added Model shadow deployments in realtime inference, and shadow testing in managed inference. Added support for shared spaces, geospatial APIs, Model Cards, AutoMLJobStep in pipelines, Git repositories on user profiles and domains, Model sharing in Jumpstart.


1.26.19
=======

* api-change:``ec2``: [``botocore``] This release adds support for AWS Verified Access and the Hpc6id Amazon EC2 compute optimized instance type, which features 3rd generation Intel Xeon Scalable processors.
* api-change:``firehose``: [``botocore``] Allow support for the Serverless offering for Amazon OpenSearch Service as a Kinesis Data Firehose delivery destination.
* api-change:``kms``: [``botocore``] AWS KMS introduces the External Key Store (XKS), a new feature for customers who want to protect their data with encryption keys stored in an external key management system under their control.
* api-change:``omics``: [``botocore``] Amazon Omics is a new, purpose-built service that can be used by healthcare and life science organizations to store, query, and analyze omics data. The insights from that data can be used to accelerate scientific discoveries and improve healthcare.
* api-change:``opensearchserverless``: [``botocore``] Publish SDK for Amazon OpenSearch Serverless
* api-change:``securitylake``: [``botocore``] Amazon Security Lake automatically centralizes security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your account. Security Lake makes it easier to analyze security data, so you can improve the protection of your workloads, applications, and data
* api-change:``simspaceweaver``: [``botocore``] AWS SimSpace Weaver is a new service that helps customers build spatial simulations at new levels of scale - resulting in virtual worlds with millions of dynamic entities. See the AWS SimSpace Weaver developer guide for more details on how to get started. https://docs.aws.amazon.com/simspaceweaver


1.26.18
=======

* api-change:``arc-zonal-shift``: [``botocore``] Amazon Route 53 Application Recovery Controller Zonal Shift is a new service that makes it easy to shift traffic away from an Availability Zone in a Region. See the developer guide for more information: https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html
* api-change:``compute-optimizer``: [``botocore``] Adds support for a new recommendation preference that makes it possible for customers to optimize their EC2 recommendations by utilizing an external metrics ingestion service to provide metrics.
* api-change:``config``: [``botocore``] With this release, you can use AWS Config to evaluate your resources for compliance with Config rules before they are created or updated. Using Config rules in proactive mode enables you to test and build compliant resource templates or check resource configurations at the time they are provisioned.
* api-change:``ec2``: [``botocore``] Introduces ENA Express, which uses AWS SRD and dynamic routing to increase throughput and minimize latency, adds support for trust relationships between Reachability Analyzer and AWS Organizations to enable cross-account analysis, and adds support for Infrastructure Performance metric subscriptions.
* api-change:``eks``: [``botocore``] Adds support for additional EKS add-ons metadata and filtering fields
* api-change:``fsx``: [``botocore``] This release adds support for 4GB/s / 160K PIOPS FSx for ONTAP file systems and 10GB/s / 350K PIOPS FSx for OpenZFS file systems (Single_AZ_2). For FSx for ONTAP, this also adds support for DP volumes, snapshot policy, copy tags to backups, and Multi-AZ route table updates.
* api-change:``glue``: [``botocore``] This release allows the creation of Custom Visual Transforms (Dynamic Transforms) to be created via AWS Glue CLI/SDK.
* api-change:``inspector2``: [``botocore``] This release adds support for Inspector to scan AWS Lambda.
* api-change:``lambda``: [``botocore``] Adds support for Lambda SnapStart, which helps improve the startup performance of functions. Customers can now manage SnapStart based functions via CreateFunction and UpdateFunctionConfiguration APIs
* api-change:``license-manager-user-subscriptions``: [``botocore``] AWS now offers fully-compliant, Amazon-provided licenses for Microsoft Office Professional Plus 2021 Amazon Machine Images (AMIs) on Amazon EC2. These AMIs are now available on the Amazon EC2 console and on AWS Marketplace to launch instances on-demand without any long-term licensing commitments.
* api-change:``macie2``: [``botocore``] Added support for configuring Macie to continually sample objects from S3 buckets and inspect them for sensitive data. Results appear in statistics, findings, and other data that Macie provides.
* api-change:``quicksight``: [``botocore``] This release adds new Describe APIs and updates Create and Update APIs to support the data model for Dashboards, Analyses, and Templates.
* api-change:``s3control``: [``botocore``] Added two new APIs to support Amazon S3 Multi-Region Access Point failover controls: GetMultiRegionAccessPointRoutes and SubmitMultiRegionAccessPointRoutes. The failover control APIs are supported in the following Regions: us-east-1, us-west-2, eu-west-1, ap-southeast-2, and ap-northeast-1.
* api-change:``securityhub``: [``botocore``] Adding StandardsManagedBy field to DescribeStandards API response


1.26.17
=======

* bugfix:dynamodb: Fixes duplicate serialization issue in DynamoDB BatchWriter
* api-change:``backup``: [``botocore``] AWS Backup introduces support for legal hold and application stack backups. AWS Backup Audit Manager introduces support for cross-Region, cross-account reports.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``drs``: [``botocore``] Non breaking changes to existing APIs, and additional APIs added to support in-AWS failing back using AWS Elastic Disaster Recovery.
* api-change:``ecs``: [``botocore``] This release adds support for ECS Service Connect, a new capability that simplifies writing and operating resilient distributed applications. This release updates the TaskDefinition, Cluster, Service mutation APIs with Service connect constructs and also adds a new ListServicesByNamespace API.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``iot-data``: [``botocore``] This release adds support for MQTT5 properties to AWS IoT HTTP Publish API.
* api-change:``iot``: [``botocore``] Job scheduling enables the scheduled rollout of a Job with start and end times and a customizable end behavior when end time is reached. This is available for continuous and snapshot jobs. Added support for MQTT5 properties to AWS IoT TopicRule Republish Action.
* api-change:``iotwireless``: [``botocore``] This release includes a new feature for customers to calculate the position of their devices by adding three new APIs: UpdateResourcePosition, GetResourcePosition, and GetPositionEstimate.
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports preview of table information from HTML tables in the search results. The most relevant cells with their corresponding rows, columns are displayed as a preview in the search result. The most relevant table cell or cells are also highlighted in table preview.
* api-change:``logs``: [``botocore``] Updates to support CloudWatch Logs data protection and CloudWatch cross-account observability
* api-change:``mgn``: [``botocore``] This release adds support for Application and Wave management. We also now support custom post-launch actions.
* api-change:``oam``: [``botocore``] Amazon CloudWatch Observability Access Manager is a new service that allows configuration of the CloudWatch cross-account observability feature.
* api-change:``organizations``: [``botocore``] This release introduces delegated administrator for AWS Organizations, a new feature to help you delegate the management of your Organizations policies, enabling you to govern your AWS organization in a decentralized way. You can now allow member accounts to manage Organizations policies.
* api-change:``rds``: [``botocore``] This release enables new Aurora and RDS feature called Blue/Green Deployments that makes updates to databases safer, simpler and faster.
* api-change:``textract``: [``botocore``] This release adds support for classifying and splitting lending documents by type, and extracting information by using the Analyze Lending APIs. This release also includes support for summarized information of the processed lending document package, in addition to per document results.
* api-change:``transcribe``: [``botocore``] This release adds support for 'inputType' for post-call and real-time (streaming) Call Analytics within Amazon Transcribe.


1.26.16
=======

* api-change:``grafana``: [``botocore``] This release includes support for configuring a Grafana workspace to connect to a datasource within a VPC as well as new APIs for configuring Grafana settings.
* api-change:``rbin``: [``botocore``] This release adds support for Rule Lock for Recycle Bin, which allows you to lock retention rules so that they can no longer be modified or deleted.


1.26.15
=======

* bugfix:Endpoints: [``botocore``] Resolve endpoint with default partition when no region is set
* bugfix:s3: [``botocore``] fixes missing x-amz-content-sha256 header for s3 object lambda
* api-change:``appflow``: [``botocore``] Adding support for Amazon AppFlow to transfer the data to Amazon Redshift databases through Amazon Redshift Data API service. This feature will support the Redshift destination connector on both public and private accessible Amazon Redshift Clusters and Amazon Redshift Serverless.
* api-change:``kinesisanalyticsv2``: [``botocore``] Support for Apache Flink 1.15 in Kinesis Data Analytics.


1.26.14
=======

* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Asia Pacific (Hyderabad) Region (ap-south-2) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.


1.26.13
=======

* api-change:``appflow``: [``botocore``] AppFlow provides a new API called UpdateConnectorRegistration to update a custom connector that customers have previously registered. With this API, customers no longer need to unregister and then register a connector to make an update.
* api-change:``auditmanager``: [``botocore``] This release introduces a new feature for Audit Manager: Evidence finder. You can now use evidence finder to quickly query your evidence, and add the matching evidence results to an assessment report.
* api-change:``chime-sdk-voice``: [``botocore``] Amazon Chime Voice Connector, Voice Connector Group and PSTN Audio Service APIs are now available in the Amazon Chime SDK Voice namespace. See https://docs.aws.amazon.com/chime-sdk/latest/dg/sdk-available-regions.html for more details.
* api-change:``cloudfront``: [``botocore``] CloudFront API support for staging distributions and associated traffic management policies.
* api-change:``connect``: [``botocore``] Added AllowedAccessControlTags and TagRestrictedResource for Tag Based Access Control on Amazon Connect Webpage
* api-change:``dynamodb``: [``botocore``] Updated minor fixes for DynamoDB documentation.
* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version
* api-change:``ec2``: [``botocore``] This release adds support for copying an Amazon Machine Image's tags when copying an AMI.
* api-change:``glue``: [``botocore``] AWSGlue Crawler - Adding support for Table and Column level Comments with database level datatypes for JDBC based crawler.
* api-change:``iot-roborunner``: [``botocore``] AWS IoT RoboRunner is a new service that makes it easy to build applications that help multi-vendor robots work together seamlessly. See the IoT RoboRunner developer guide for more details on getting started. https://docs.aws.amazon.com/iotroborunner/latest/dev/iotroborunner-welcome.html
* api-change:``quicksight``: [``botocore``] This release adds the following: 1) Asset management for centralized assets governance 2) QuickSight Q now supports public embedding 3) New Termination protection flag to mitigate accidental deletes 4) Athena data sources now accept a custom IAM role 5) QuickSight supports connectivity to Databricks
* api-change:``sagemaker``: [``botocore``] Added DisableProfiler flag as a new field in ProfilerConfig
* api-change:``servicecatalog``: [``botocore``] This release 1. adds support for Principal Name Sharing with Service Catalog portfolio sharing. 2. Introduces repo sourced products which are created and managed with existing SC APIs. These products are synced to external repos and auto create new product versions based on changes in the repo.
* api-change:``ssm-sap``: [``botocore``] AWS Systems Manager for SAP provides simplified operations and management of SAP applications such as SAP HANA. With this release, SAP customers and partners can automate and simplify their SAP system administration tasks such as backup/restore of SAP HANA.
* api-change:``stepfunctions``: [``botocore``] Update stepfunctions client to latest version
* api-change:``transfer``: [``botocore``] Adds a NONE encryption algorithm type to AS2 connectors, providing support for skipping encryption of the AS2 message body when a HTTPS URL is also specified.


1.26.12
=======

* api-change:``amplify``: [``botocore``] Adds a new value (WEB_COMPUTE) to the Platform enum that allows customers to create Amplify Apps with Server-Side Rendering support.
* api-change:``appflow``: [``botocore``] AppFlow simplifies the preparation and cataloging of SaaS data into the AWS Glue Data Catalog where your data can be discovered and accessed by AWS analytics and ML services. AppFlow now also supports data field partitioning and file size optimization to improve query performance and reduce cost.
* api-change:``appsync``: [``botocore``] This release introduces the APPSYNC_JS runtime, and adds support for JavaScript in AppSync functions and AppSync pipeline resolvers.
* api-change:``dms``: [``botocore``] Adds support for Internet Protocol Version 6 (IPv6) on DMS Replication Instances
* api-change:``ec2``: [``botocore``] This release adds a new optional parameter "privateIpAddress" for the CreateNatGateway API. PrivateIPAddress will allow customers to select a custom Private IPv4 address instead of having it be auto-assigned.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``emr-serverless``: [``botocore``] Adds support for AWS Graviton2 based applications. You can now select CPU architecture when creating new applications or updating existing ones.
* api-change:``ivschat``: [``botocore``] Adds LoggingConfiguration APIs for IVS Chat - a feature that allows customers to store and record sent messages in a chat room to S3 buckets, CloudWatch logs, or Kinesis firehose.
* api-change:``lambda``: [``botocore``] Add Node 18 (nodejs18.x) support to AWS Lambda.
* api-change:``personalize``: [``botocore``] This release provides support for creation and use of metric attributions in AWS Personalize
* api-change:``polly``: [``botocore``] Add two new neural voices - Ola (pl-PL) and Hala (ar-AE).
* api-change:``rum``: [``botocore``] CloudWatch RUM now supports custom events. To use custom events, create an app monitor or update an app monitor with CustomEvent Status as ENABLED.
* api-change:``s3control``: [``botocore``] Added 34 new S3 Storage Lens metrics to support additional customer use cases.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager.
* api-change:``securityhub``: [``botocore``] Added SourceLayerArn and SourceLayerHash field for security findings.  Updated AwsLambdaFunction Resource detail
* api-change:``servicecatalog-appregistry``: [``botocore``] This release adds support for tagged resource associations, which allows you to associate a group of resources with a defined resource tag key and value to the application.
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``textract``: [``botocore``] This release adds support for specifying and extracting information from documents using the Signatures feature within Analyze Document API
* api-change:``workspaces``: [``botocore``] The release introduces CreateStandbyWorkspaces, an API that allows you to create standby WorkSpaces associated with a primary WorkSpace in another Region. DescribeWorkspaces now includes related WorkSpaces properties. DescribeWorkspaceBundles and CreateWorkspaceBundle now return more bundle details.


1.26.11
=======

* api-change:``batch``: [``botocore``] Documentation updates related to Batch on EKS
* api-change:``billingconductor``: [``botocore``] This release adds a new feature BillingEntity pricing rule.
* api-change:``cloudformation``: [``botocore``] Added UnsupportedTarget HandlerErrorCode for use with CFN Resource Hooks
* api-change:``comprehendmedical``: [``botocore``] This release supports new set of entities and traits. It also adds new category (BEHAVIORAL_ENVIRONMENTAL_SOCIAL).
* api-change:``connect``: [``botocore``] This release adds a new MonitorContact API for initiating monitoring of ongoing Voice and Chat contacts.
* api-change:``eks``: [``botocore``] Adds support for customer-provided placement groups for Kubernetes control plane instances when creating local EKS clusters on Outposts
* api-change:``elasticache``: [``botocore``] for Redis now supports AWS Identity and Access Management authentication access to Redis clusters starting with redis-engine version 7.0
* api-change:``iottwinmaker``: [``botocore``] This release adds the following: 1) ExecuteQuery API allows users to query their AWS IoT TwinMaker Knowledge Graph 2) Pricing plan APIs allow users to configure and manage their pricing mode 3) Support for property groups and tabular property values in existing AWS IoT TwinMaker APIs.
* api-change:``personalize-events``: [``botocore``] This release provides support for creation and use of metric attributions in AWS Personalize
* api-change:``proton``: [``botocore``] Add support for sorting and filtering in ListServiceInstances
* api-change:``rds``: [``botocore``] This release adds support for container databases (CDBs) to Amazon RDS Custom for Oracle. A CDB contains one PDB at creation. You can add more PDBs using Oracle SQL. You can also customize your database installation by setting the Oracle base, Oracle home, and the OS user name and group.
* api-change:``ssm-incidents``: [``botocore``] Add support for PagerDuty integrations on ResponsePlan, IncidentRecord, and RelatedItem APIs
* api-change:``ssm``: [``botocore``] This release adds support for cross account access in CreateOpsItem, UpdateOpsItem and GetOpsItem. It introduces new APIs to setup resource policies for SSM resources: PutResourcePolicy, GetResourcePolicies and DeleteResourcePolicy.
* api-change:``transfer``: [``botocore``] Allow additional operations to throw ThrottlingException
* api-change:``xray``: [``botocore``] This release adds new APIs - PutResourcePolicy, DeleteResourcePolicy, ListResourcePolicies for supporting resource based policies for AWS X-Ray.


1.26.10
=======

* bugfix:s3: [``botocore``] fixes missing x-amz-content-sha256 header for s3 on outpost
* enhancement:sso: [``botocore``] Add support for loading sso-session profiles from the aws config
* api-change:``connect``: [``botocore``] This release updates the APIs: UpdateInstanceAttribute, DescribeInstanceAttribute, and ListInstanceAttributes. You can use it to programmatically enable/disable enhanced contact monitoring using attribute type ENHANCED_CONTACT_MONITORING on the specified Amazon Connect instance.
* api-change:``greengrassv2``: [``botocore``] Adds new parent target ARN paramater to CreateDeployment, GetDeployment, and ListDeployments APIs for the new subdeployments feature.
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Europe (Spain) Region (eu-south-2) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``ssmsap``: [``botocore``] AWS Systems Manager for SAP provides simplified operations and management of SAP applications such as SAP HANA. With this release, SAP customers and partners can automate and simplify their SAP system administration tasks such as backup/restore of SAP HANA.
* api-change:``workspaces``: [``botocore``] This release introduces ModifyCertificateBasedAuthProperties, a new API that allows control of certificate-based auth properties associated with a WorkSpaces directory. The DescribeWorkspaceDirectories API will now additionally return certificate-based auth properties in its responses.


1.26.9
======

* api-change:``customer-profiles``: [``botocore``] This release enhances the SearchProfiles API by providing functionality to search for profiles using multiple keys and logical operators.
* api-change:``lakeformation``: [``botocore``] This release adds a new parameter "Parameters" in the DataLakeSettings.
* api-change:``managedblockchain``: [``botocore``] Updating the API docs data type: NetworkEthereumAttributes, and the operations DeleteNode, and CreateNode to also include the supported Goerli network.
* api-change:``proton``: [``botocore``] Add support for CodeBuild Provisioning
* api-change:``rds``: [``botocore``] This release adds support for restoring an RDS Multi-AZ DB cluster snapshot to a Single-AZ deployment or a Multi-AZ DB instance deployment.
* api-change:``workdocs``: [``botocore``] Added 2 new document related operations, DeleteDocumentVersion and RestoreDocumentVersions.
* api-change:``xray``: [``botocore``] This release enhances GetServiceGraph API to support new type of edge to represent links between SQS and Lambda in event-driven applications.


1.26.8
======

* api-change:``glue``: [``botocore``] Added links related to enabling job bookmarks.
* api-change:``iot``: [``botocore``] This release add new api listRelatedResourcesForAuditFinding and new member type IssuerCertificates for Iot device device defender Audit.
* api-change:``license-manager``: [``botocore``] AWS License Manager now supports onboarded Management Accounts or Delegated Admins to view granted licenses aggregated from all accounts in the organization.
* api-change:``marketplace-catalog``: [``botocore``] Added three new APIs to support tagging and tag-based authorization: TagResource, UntagResource, and ListTagsForResource. Added optional parameters to the StartChangeSet API to support tagging a resource while making a request to create it.
* api-change:``rekognition``: [``botocore``] Adding support for ImageProperties feature to detect dominant colors and image brightness, sharpness, and contrast, inclusion and exclusion filters for labels and label categories, new fields to the API response, "aliases" and "categories"
* api-change:``securityhub``: [``botocore``] Documentation updates for Security Hub
* api-change:``ssm-incidents``: [``botocore``] RelatedItems now have an ID field which can be used for referencing them else where. Introducing event references in TimelineEvent API and increasing maximum length of "eventData" to 12K characters.


1.26.7
======

* api-change:``autoscaling``: [``botocore``] This release adds a new price capacity optimized allocation strategy for Spot Instances to help customers optimize provisioning of Spot Instances via EC2 Auto Scaling, EC2 Fleet, and Spot Fleet. It allocates Spot Instances based on both spare capacity availability and Spot Instance price.
* api-change:``ec2``: [``botocore``] This release adds a new price capacity optimized allocation strategy for Spot Instances to help customers optimize provisioning of Spot Instances via EC2 Auto Scaling, EC2 Fleet, and Spot Fleet. It allocates Spot Instances based on both spare capacity availability and Spot Instance price.
* api-change:``ecs``: [``botocore``] This release adds support for task scale-in protection with updateTaskProtection and getTaskProtection APIs. UpdateTaskProtection API can be used to protect a service managed task from being terminated by scale-in events and getTaskProtection API to get the scale-in protection status of a task.
* api-change:``es``: [``botocore``] Amazon OpenSearch Service now offers managed VPC endpoints to connect to your Amazon OpenSearch Service VPC-enabled domain in a Virtual Private Cloud (VPC). This feature allows you to privately access OpenSearch Service domain without using public IPs or requiring traffic to traverse the Internet.
* api-change:``resource-explorer-2``: [``botocore``] Text only updates to some Resource Explorer descriptions.
* api-change:``scheduler``: [``botocore``] AWS introduces the new Amazon EventBridge Scheduler. EventBridge Scheduler is a serverless scheduler that allows you to create, run, and manage tasks from one central, managed service.


1.26.6
======

* api-change:``connect``: [``botocore``] This release adds new fields SignInUrl, UserArn, and UserId to GetFederationToken response payload.
* api-change:``connectcases``: [``botocore``] This release adds the ability to disable templates through the UpdateTemplate API. Disabling templates prevents customers from creating cases using the template. For more information see https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html
* api-change:``ec2``: [``botocore``] Amazon EC2 Trn1 instances, powered by AWS Trainium chips, are purpose built for high-performance deep learning training. u-24tb1.112xlarge and u-18tb1.112xlarge High Memory instances are purpose-built to run large in-memory databases.
* api-change:``groundstation``: [``botocore``] This release adds the preview of customer-provided ephemeris support for AWS Ground Station, allowing space vehicle owners to provide their own position and trajectory information for a satellite.
* api-change:``mediapackage-vod``: [``botocore``] This release adds "IncludeIframeOnlyStream" for Dash endpoints.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.26.5
======

* api-change:``acm``: [``botocore``] Support added for requesting elliptic curve certificate key algorithm types P-256 (EC_prime256v1) and P-384 (EC_secp384r1).
* api-change:``billingconductor``: [``botocore``] This release adds the Recurring Custom Line Item feature along with a new API ListCustomLineItemVersions.
* api-change:``ec2``: [``botocore``] This release enables sharing of EC2 Placement Groups across accounts and within AWS Organizations using Resource Access Manager
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports importing existing AWS Network Firewall firewalls into Firewall Manager policies.
* api-change:``lightsail``: [``botocore``] This release adds support for Amazon Lightsail to automate the delegation of domains registered through Amazon Route 53 to Lightsail DNS management and to automate record creation for DNS validation of Lightsail SSL/TLS certificates.
* api-change:``opensearch``: [``botocore``] Amazon OpenSearch Service now offers managed VPC endpoints to connect to your Amazon OpenSearch Service VPC-enabled domain in a Virtual Private Cloud (VPC). This feature allows you to privately access OpenSearch Service domain without using public IPs or requiring traffic to traverse the Internet.
* api-change:``polly``: [``botocore``] Amazon Polly adds new voices: Elin (sv-SE), Ida (nb-NO), Laura (nl-NL) and Suvi (fi-FI). They are available as neural voices only.
* api-change:``resource-explorer-2``: [``botocore``] This is the initial SDK release for AWS Resource Explorer. AWS Resource Explorer lets your users search for and discover your AWS resources across the AWS Regions in your account.
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Europe (Zurich) Region (eu-central-2) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.26.4
======

* api-change:``athena``: [``botocore``] Adds support for using Query Result Reuse
* api-change:``autoscaling``: [``botocore``] This release adds support for two new attributes for attribute-based instance type selection - NetworkBandwidthGbps and AllowedInstanceTypes.
* api-change:``cloudtrail``: [``botocore``] This release includes support for configuring a delegated administrator to manage an AWS Organizations organization CloudTrail trails and event data stores, and AWS Key Management Service encryption of CloudTrail Lake event data stores.
* api-change:``ec2``: [``botocore``] This release adds support for two new attributes for attribute-based instance type selection - NetworkBandwidthGbps and AllowedInstanceTypes.
* api-change:``elasticache``: [``botocore``] Added support for IPv6 and dual stack for Memcached and Redis clusters. Customers can now launch new Redis and Memcached clusters with IPv6 and dual stack networking support.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``mediaconvert``: [``botocore``] The AWS Elemental MediaConvert SDK has added support for setting the SDR reference white point for HDR conversions and conversion of HDR10 to DolbyVision without mastering metadata.
* api-change:``ssm``: [``botocore``] This release includes support for applying a CloudWatch alarm to multi account multi region Systems Manager Automation
* api-change:``wafv2``: [``botocore``] The geo match statement now adds labels for country and region. You can match requests at the region level by combining a geo match statement with label match statements.
* api-change:``wellarchitected``: [``botocore``] This release adds support for integrations with AWS Trusted Advisor and AWS Service Catalog AppRegistry to improve workload discovery and speed up your workload reviews.
* api-change:``workspaces``: [``botocore``] This release adds protocols attribute to workspaces properties data type. This enables customers to migrate workspaces from PC over IP (PCoIP) to WorkSpaces Streaming Protocol (WSP) using create and modify workspaces public APIs.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.26.3
======

* api-change:``ec2``: [``botocore``] This release adds API support for the recipient of an AMI account share to remove shared AMI launch permissions.
* api-change:``emr-containers``: [``botocore``] Adding support for Job templates. Job templates allow you to create and store templates to configure Spark applications parameters. This helps you ensure consistent settings across applications by reusing and enforcing configuration overrides in data pipelines.
* api-change:``logs``: [``botocore``] Doc-only update for bug fixes and support of export to buckets encrypted with SSE-KMS
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.26.2
======

* api-change:``memorydb``: [``botocore``] Adding support for r6gd instances for MemoryDB Redis with data tiering. In a cluster with data tiering enabled, when available memory capacity is exhausted, the least recently used data is automatically tiered to solid state drives for cost-effective capacity scaling with minimal performance impact.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker now supports running training jobs on ml.trn1 instance types.
* api-change:``endpoint-rules``: [``botocore``] Update endpoint-rules client to latest version


1.26.1
======

* api-change:``iotsitewise``: [``botocore``] This release adds the ListAssetModelProperties and ListAssetProperties APIs. You can list all properties that belong to a single asset model or asset using these two new APIs.
* api-change:``s3control``: [``botocore``] S3 on Outposts launches support for Lifecycle configuration for Outposts buckets. With S3 Lifecycle configuration, you can mange objects so they are stored cost effectively. You can manage objects using size-based rules and specify how many noncurrent versions bucket will retain.
* api-change:``sagemaker``: [``botocore``] This release updates Framework model regex for ModelPackage to support new Framework version xgboost, sklearn.
* api-change:``ssm-incidents``: [``botocore``] Adds support for tagging replication-set on creation.


1.26.0
======

* feature:Endpoints: [``botocore``] Migrate all services to use new AWS Endpoint Resolution framework
* Enhancement:Endpoints: [``botocore``] Discontinued use of `sslCommonName` hosts as detailed in 1.27.0 (see `#2705 <https://github.com/boto/botocore/issues/2705>`__ for more info)
* api-change:``rds``: [``botocore``] Relational Database Service - This release adds support for configuring Storage Throughput on RDS database instances.
* api-change:``textract``: [``botocore``] Add ocr results in AnalyzeIDResponse as blocks


1.25.5
======

* api-change:``apprunner``: [``botocore``] This release adds support for private App Runner services. Services may now be configured to be made private and only accessible from a VPC. The changes include a new VpcIngressConnection resource and several new and modified APIs.
* api-change:``connect``: [``botocore``] Amazon connect now support a new API DismissUserContact to dismiss or remove terminated contacts in Agent CCP
* api-change:``ec2``: [``botocore``] Elastic IP transfer is a new Amazon VPC feature that allows you to transfer your Elastic IP addresses from one AWS Account to another.
* api-change:``iot``: [``botocore``] This release adds the Amazon Location action to IoT Rules Engine.
* api-change:``logs``: [``botocore``] SDK release to support tagging for destinations and log groups with TagResource. Also supports tag on create with PutDestination.
* api-change:``sesv2``: [``botocore``] This release includes support for interacting with the Virtual Deliverability Manager, allowing you to opt in/out of the feature and to retrieve recommendations and metric data.
* api-change:``textract``: [``botocore``] This release introduces additional support for 30+ normalized fields such as vendor address and currency. It also includes OCR output in the response and accuracy improvements for the already supported fields in previous version


1.25.4
======

* api-change:``apprunner``: [``botocore``] AWS App Runner adds .NET 6, Go 1, PHP 8.1 and Ruby 3.1 runtimes.
* api-change:``appstream``: [``botocore``] This release includes CertificateBasedAuthProperties in CreateDirectoryConfig and UpdateDirectoryConfig.
* api-change:``cloud9``: [``botocore``] Update to the documentation section of the Cloud9 API Reference guide.
* api-change:``cloudformation``: [``botocore``] This release adds more fields to improves visibility of AWS CloudFormation StackSets information in following APIs: ListStackInstances, DescribeStackInstance, ListStackSetOperationResults, ListStackSetOperations, DescribeStackSetOperation.
* api-change:``gamesparks``: [``botocore``] Add LATEST as a possible GameSDK Version on snapshot
* api-change:``mediatailor``: [``botocore``] This release introduces support for SCTE-35 segmentation descriptor messages which can be sent within time signal messages.


1.25.3
======

* api-change:``ec2``: [``botocore``] Feature supports the replacement of instance root volume using an updated AMI without requiring customers to stop their instance.
* api-change:``fms``: [``botocore``] Add support NetworkFirewall Managed Rule Group Override flag in GetViolationDetails API
* api-change:``glue``: [``botocore``] Added support for custom datatypes when using custom csv classifier.
* api-change:``redshift``: [``botocore``] This release clarifies use for the ElasticIp parameter of the CreateCluster and RestoreFromClusterSnapshot APIs.
* api-change:``sagemaker``: [``botocore``] This change allows customers to provide a custom entrypoint script for the docker container to be run while executing training jobs, and provide custom arguments to the entrypoint script.
* api-change:``wafv2``: [``botocore``] This release adds the following: Challenge rule action, to silently verify client browsers; rule group rule action override to any valid rule action, not just Count; token sharing between protected applications for challenge/CAPTCHA token; targeted rules option for Bot Control managed rule group.


1.25.2
======

* api-change:``iam``: [``botocore``] Doc only update that corrects instances of CLI not using an entity.
* api-change:``kafka``: [``botocore``] This release adds support for Tiered Storage. UpdateStorage allows you to control the Storage Mode for supported storage tiers.
* api-change:``neptune``: [``botocore``] Added a new cluster-level attribute to set the capacity range for Neptune Serverless instances.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now supports specifying Grid Search strategy for tuning jobs, which evaluates all hyperparameter combinations exhaustively based on the categorical hyperparameters provided.


1.25.1
======

* api-change:``accessanalyzer``: [``botocore``] This release adds support for six new resource types in IAM Access Analyzer to help you easily identify public and cross-account access to your AWS resources. Updated service API, documentation, and paginators.
* api-change:``location``: [``botocore``] Added new map styles with satellite imagery for map resources using HERE as a data provider.
* api-change:``mediatailor``: [``botocore``] This release is a documentation update
* api-change:``rds``: [``botocore``] Relational Database Service - This release adds support for exporting DB cluster data to Amazon S3.
* api-change:``workspaces``: [``botocore``] This release adds new enums for supporting Workspaces Core features, including creating Manual running mode workspaces, importing regular Workspaces Core images and importing g4dn Workspaces Core images.


1.25.0
======

* feature:Endpoints: [``botocore``] Implemented new endpoint ruleset system to dynamically derive endpoints and settings for services
* api-change:``acm-pca``: [``botocore``] AWS Private Certificate Authority (AWS Private CA) now offers usage modes which are combination of features to address specific use cases.
* api-change:``batch``: [``botocore``] This release adds support for AWS Batch on Amazon EKS.
* api-change:``datasync``: [``botocore``] Added support for self-signed certificates when using object storage locations; added BytesCompressed to the TaskExecution response.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now supports a new API ListInferenceRecommendationJobSteps to return the details of all the benchmark we create for an inference recommendation job.


1.24.96
=======

* api-change:``cognito-idp``: [``botocore``] This release adds a new "DeletionProtection" field to the UserPool in Cognito. Application admins can configure this value with either ACTIVE or INACTIVE value. Setting this field to ACTIVE will prevent a user pool from accidental deletion.
* api-change:``sagemaker``: [``botocore``] CreateInferenceRecommenderjob API now supports passing endpoint details directly, that will help customers to identify the max invocation and max latency they can achieve for their model and the associated endpoint along with getting recommendations on other instances.


1.24.95
=======

* api-change:``devops-guru``: [``botocore``] This release adds information about the resources DevOps Guru is analyzing.
* api-change:``globalaccelerator``: [``botocore``] Global Accelerator now supports AddEndpoints and RemoveEndpoints operations for standard endpoint groups.
* api-change:``resiliencehub``: [``botocore``] In this release, we are introducing support for regional optimization for AWS Resilience Hub applications. It also includes a few documentation updates to improve clarity.
* api-change:``rum``: [``botocore``] CloudWatch RUM now supports Extended CloudWatch Metrics with Additional Dimensions


1.24.94
=======

* api-change:``chime-sdk-messaging``: [``botocore``] Documentation updates for Chime Messaging SDK
* api-change:``cloudtrail``: [``botocore``] This release includes support for exporting CloudTrail Lake query results to an Amazon S3 bucket.
* api-change:``config``: [``botocore``] This release adds resourceType enums for AppConfig, AppSync, DataSync, EC2, EKS, Glue, GuardDuty, SageMaker, ServiceDiscovery, SES, Route53 types.
* api-change:``connect``: [``botocore``] This release adds API support for managing phone numbers that can be used across multiple AWS regions through telephony traffic distribution.
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``managedblockchain``: [``botocore``] Adding new Accessor APIs for Amazon Managed Blockchain
* api-change:``s3``: [``botocore``] Updates internal logic for constructing API endpoints. We have added rule-based endpoints and internal model parameters.
* api-change:``s3control``: [``botocore``] Updates internal logic for constructing API endpoints. We have added rule-based endpoints and internal model parameters.
* api-change:``support-app``: [``botocore``] This release adds the RegisterSlackWorkspaceForOrganization API. You can use the API to register a Slack workspace for an AWS account that is part of an organization.
* api-change:``workspaces-web``: [``botocore``] WorkSpaces Web now supports user access logging for recording session start, stop, and URL navigation.


1.24.93
=======

* api-change:``frauddetector``: [``botocore``] Documentation Updates for Amazon Fraud Detector
* api-change:``sagemaker``: [``botocore``] This change allows customers to enable data capturing while running a batch transform job, and configure monitoring schedule to monitoring the captured data.
* api-change:``servicediscovery``: [``botocore``] Updated the ListNamespaces API to support the NAME and HTTP_NAME filters, and the BEGINS_WITH filter condition.
* api-change:``sesv2``: [``botocore``] This release allows subscribers to enable Dedicated IPs (managed) to send email via a fully managed dedicated IP experience. It also adds identities' VerificationStatus in the response of GetEmailIdentity and ListEmailIdentities APIs, and ImportJobs counts in the response of ListImportJobs API.


1.24.92
=======

* api-change:``greengrass``: [``botocore``] This change allows customers to specify FunctionRuntimeOverride in FunctionDefinitionVersion. This configuration can be used if the runtime on the device is different from the AWS Lambda runtime specified for that function.
* api-change:``sagemaker``: [``botocore``] This release adds support for C7g, C6g, C6gd, C6gn, M6g, M6gd, R6g, and R6gn Graviton instance types in Amazon SageMaker Inference.


1.24.91
=======

* api-change:``mediaconvert``: [``botocore``] MediaConvert now supports specifying the minimum percentage of the HRD buffer available at the end of each encoded video segment.


1.24.90
=======

* api-change:``amplifyuibuilder``: [``botocore``] We are releasing the ability for fields to be configured as arrays.
* api-change:``appflow``: [``botocore``] With this update, you can choose which Salesforce API is used by Amazon AppFlow to transfer data to or from your Salesforce account. You can choose the Salesforce REST API or Bulk API 2.0. You can also choose for Amazon AppFlow to pick the API automatically.
* api-change:``connect``: [``botocore``] This release adds support for a secondary email and a mobile number for Amazon Connect instance users.
* api-change:``ds``: [``botocore``] This release adds support for describing and updating AWS Managed Microsoft AD set up.
* api-change:``ecs``: [``botocore``] Documentation update to address tickets.
* api-change:``guardduty``: [``botocore``] Add UnprocessedDataSources to CreateDetectorResponse which specifies the data sources that couldn't be enabled during the CreateDetector request. In addition, update documentations.
* api-change:``iam``: [``botocore``] Documentation updates for the AWS Identity and Access Management API Reference.
* api-change:``iotfleetwise``: [``botocore``] Documentation update for AWS IoT FleetWise
* api-change:``medialive``: [``botocore``] AWS Elemental MediaLive now supports forwarding SCTE-35 messages through the Event Signaling and Management (ESAM) API, and can read those SCTE-35 messages from an inactive source.
* api-change:``mediapackage-vod``: [``botocore``] This release adds SPEKE v2 support for MediaPackage VOD. Speke v2 is an upgrade to the existing SPEKE API to support multiple encryption keys, based on an encryption contract selected by the customer.
* api-change:``panorama``: [``botocore``] Pause and resume camera stream processing with SignalApplicationInstanceNodeInstances. Reboot an appliance with CreateJobForDevices. More application state information in DescribeApplicationInstance response.
* api-change:``rds-data``: [``botocore``] Doc update to reflect no support for schema parameter on BatchExecuteStatement API
* api-change:``ssm-incidents``: [``botocore``] Update RelatedItem enum to support Tasks
* api-change:``ssm``: [``botocore``] Support of AmazonLinux2022 by Patch Manager
* api-change:``transfer``: [``botocore``] This release adds an option for customers to configure workflows that are triggered when files are only partially received from a client due to premature session disconnect.
* api-change:``translate``: [``botocore``] This release enables customers to specify multiple target languages in asynchronous batch translation requests.
* api-change:``wisdom``: [``botocore``] This release updates the GetRecommendations API to include a trigger event list for classifying and grouping recommendations.


1.24.89
=======

* api-change:``codeguru-reviewer``: [``botocore``] Documentation update to replace broken link.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``greengrassv2``: [``botocore``] This release adds error status details for deployments and components that failed on a device and adds features to improve visibility into component installation.
* api-change:``quicksight``: [``botocore``] Amazon QuickSight now supports SecretsManager Secret ARN in place of CredentialPair for DataSource creation and update. This release also has some minor documentation updates and removes CountryCode as a required parameter in GeoSpatialColumnGroup


1.24.88
=======

* api-change:``resiliencehub``: [``botocore``] Documentation change for AWS Resilience Hub. Doc-only update to fix Documentation layout


1.24.87
=======

* api-change:``glue``: [``botocore``] This SDK release adds support to sync glue jobs with source control provider. Additionally, a new parameter called SourceControlDetails will be added to Job model.
* api-change:``network-firewall``: [``botocore``] StreamExceptionPolicy configures how AWS Network Firewall processes traffic when a network connection breaks midstream
* api-change:``outposts``: [``botocore``] This release adds the Asset state information to the ListAssets response. The ListAssets request supports filtering on Asset state.


1.24.86
=======

* api-change:``connect``: [``botocore``] Updated the CreateIntegrationAssociation API to support the CASES_DOMAIN IntegrationType.
* api-change:``connectcases``: [``botocore``] This release adds APIs for Amazon Connect Cases. Cases allows your agents to quickly track and manage customer issues that require multiple interactions, follow-up tasks, and teams in your contact center.  For more information, see https://docs.aws.amazon.com/cases/latest/APIReference/Welcome.html
* api-change:``ec2``: [``botocore``] Added EnableNetworkAddressUsageMetrics flag for ModifyVpcAttribute, DescribeVpcAttribute APIs.
* api-change:``ecs``: [``botocore``] Documentation updates to address various Amazon ECS tickets.
* api-change:``s3control``: [``botocore``] S3 Object Lambda adds support to allow customers to intercept HeadObject and ListObjects requests and introduce their own compute. These requests were previously proxied to S3.
* api-change:``workmail``: [``botocore``] This release adds support for impersonation roles in Amazon WorkMail.


1.24.85
=======

* api-change:``accessanalyzer``: [``botocore``] AWS IAM Access Analyzer policy validation introduces new checks for role trust policies. As customers author a policy, IAM Access Analyzer policy validation evaluates the policy for any issues to make it easier for customers to author secure policies.
* api-change:``ec2``: [``botocore``] Adding an imdsSupport attribute to EC2 AMIs
* api-change:``snowball``: [``botocore``] Adds support for V3_5C. This is a refreshed AWS Snowball Edge Compute Optimized device type with 28TB SSD, 104 vCPU and 416GB memory (customer usable).


1.24.84
=======

* api-change:``codedeploy``: [``botocore``] This release allows you to override the alarm configurations when creating a deployment.
* api-change:``devops-guru``: [``botocore``] This release adds filter feature on AddNotificationChannel API, enable customer to configure the SNS notification messages by Severity or MessageTypes
* api-change:``dlm``: [``botocore``] This release adds support for archival of single-volume snapshots created by Amazon Data Lifecycle Manager policies
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``sagemaker``: [``botocore``] A new parameter called ExplainerConfig is added to CreateEndpointConfig API to enable SageMaker Clarify online explainability feature.
* api-change:``sso-oidc``: [``botocore``] Documentation updates for the IAM Identity Center OIDC CLI Reference.


1.24.83
=======

* api-change:``acm``: [``botocore``] This update returns additional certificate details such as certificate SANs and allows sorting in the ListCertificates API.
* api-change:``ec2``: [``botocore``] u-3tb1 instances are powered by Intel Xeon Platinum 8176M (Skylake) processors and are purpose-built to run large in-memory databases.
* api-change:``emr-serverless``: [``botocore``] This release adds API support to debug Amazon EMR Serverless jobs in real-time with live application UIs
* api-change:``fsx``: [``botocore``] This release adds support for Amazon File Cache.
* api-change:``migrationhuborchestrator``: [``botocore``] Introducing AWS MigrationHubOrchestrator. This is the first public release of AWS MigrationHubOrchestrator.
* api-change:``polly``: [``botocore``] Added support for the new Cantonese voice - Hiujin. Hiujin is available as a Neural voice only.
* api-change:``proton``: [``botocore``] This release adds an option to delete pipeline provisioning repositories using the UpdateAccountSettings API
* api-change:``sagemaker``: [``botocore``] SageMaker Training Managed Warm Pools let you retain provisioned infrastructure to reduce latency for repetitive training workloads.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``translate``: [``botocore``] This release enables customers to access control rights on Translate resources like Parallel Data and Custom Terminology using Tag Based Authorization.
* api-change:``workspaces``: [``botocore``] This release includes diagnostic log uploading feature. If it is enabled, the log files of WorkSpaces Windows client will be sent to Amazon WorkSpaces automatically for troubleshooting. You can use modifyClientProperty api to enable/disable this feature.


1.24.82
=======

* api-change:``ce``: [``botocore``] This release is to support retroactive Cost Categories. The new field will enable you to retroactively apply new and existing cost category rules to previous months.
* api-change:``kendra``: [``botocore``] My AWS Service (placeholder) - Amazon Kendra now provides a data source connector for DropBox. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-dropbox.html
* api-change:``location``: [``botocore``] This release adds place IDs, which are unique identifiers of places, along with a new GetPlace operation, which can be used with place IDs to find a place again later. UnitNumber and UnitType are also added as new properties of places.


1.24.81
=======

* api-change:``cur``: [``botocore``] This release adds two new support regions(me-central-1/eu-south-2) for OSG.
* api-change:``iotfleetwise``: [``botocore``] General availability (GA) for AWS IoT Fleetwise. It adds AWS IoT Fleetwise to AWS SDK. For more information, see https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/Welcome.html.
* api-change:``ssm``: [``botocore``] This release includes support for applying a CloudWatch alarm to Systems Manager capabilities like Automation, Run Command, State Manager, and Maintenance Windows.


1.24.80
=======

* api-change:``apprunner``: [``botocore``] AWS App Runner adds a Node.js 16 runtime.
* api-change:``ec2``: [``botocore``] Letting external AWS customers provide ImageId as a Launch Template override in FleetLaunchTemplateOverridesRequest
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``lightsail``: [``botocore``] This release adds Instance Metadata Service (IMDS) support for Lightsail instances.
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio adds support for on-demand Amazon Elastic Compute Cloud (EC2) G3 and G5 instances, allowing customers to utilize additional GPU instance types for their creative projects.
* api-change:``ssm``: [``botocore``] This release adds new SSM document types ConformancePackTemplate and CloudFormation
* api-change:``wafv2``: [``botocore``] Add the default specification for ResourceType in ListResourcesForWebACL.


1.24.79
=======

* api-change:``backup-gateway``: [``botocore``] Changes include: new GetVirtualMachineApi to fetch a single user's VM, improving ListVirtualMachines to fetch filtered VMs as well as all VMs, and improving GetGatewayApi to now also return the gateway's MaintenanceStartTime.
* api-change:``devicefarm``: [``botocore``] This release adds the support for VPC-ENI based connectivity for private devices on AWS Device Farm.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``glue``: [``botocore``] Added support for S3 Event Notifications for Catalog Target Crawlers.
* api-change:``identitystore``: [``botocore``] Documentation updates for the Identity Store CLI Reference.


1.24.78
=======

* api-change:``comprehend``: [``botocore``] Amazon Comprehend now supports synchronous mode for targeted sentiment API operations.
* api-change:``s3control``: [``botocore``] S3 on Outposts launches support for object versioning for Outposts buckets. With S3 Versioning, you can preserve, retrieve, and restore every version of every object stored in your buckets. You can recover from both unintended user actions and application failures.
* api-change:``sagemaker``: [``botocore``] SageMaker now allows customization on Canvas Application settings, including enabling/disabling time-series forecasting and specifying an Amazon Forecast execution role at both the Domain and UserProfile levels.


1.24.77
=======

* api-change:``ec2``: [``botocore``] This release adds support for blocked paths to Amazon VPC Reachability Analyzer.


1.24.76
=======

* api-change:``cloudtrail``: [``botocore``] This release includes support for importing existing trails into CloudTrail Lake.
* api-change:``ec2``: [``botocore``] This release adds CapacityAllocations field to DescribeCapacityReservations
* api-change:``mediaconnect``: [``botocore``] This change allows the customer to use the SRT Caller protocol as part of their flows
* api-change:``rds``: [``botocore``] This release adds support for Amazon RDS Proxy with SQL Server compatibility.


1.24.75
=======

* api-change:``codestar-notifications``: [``botocore``] This release adds tag based access control for the UntagResource API.
* api-change:``ecs``: [``botocore``] This release supports new task definition sizes.


1.24.74
=======

* api-change:``dynamodb``: [``botocore``] Increased DynamoDB transaction limit from 25 to 100.
* api-change:``ec2``: [``botocore``] This feature allows customers to create tags for vpc-endpoint-connections and vpc-endpoint-service-permissions.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now supports specifying Hyperband strategy for tuning jobs, which uses a multi-fidelity based tuning strategy to stop underperforming hyperparameter configurations early.


1.24.73
=======

* api-change:``amplifyuibuilder``: [``botocore``] Amplify Studio UIBuilder is introducing forms functionality. Forms can be configured from Data Store models, JSON, or from scratch. These forms can then be generated in your project and used like any other React components.
* api-change:``ec2``: [``botocore``] This update introduces API operations to manage and create local gateway route tables, CoIP pools, and VIF group associations.


1.24.72
=======

* api-change:``customer-profiles``: [``botocore``] Added isUnstructured in response for Customer Profiles Integration APIs
* api-change:``drs``: [``botocore``] Fixed the data type of lagDuration that is returned in Describe Source Server API
* api-change:``ec2``: [``botocore``] Two new features for local gateway route tables: support for static routes targeting Elastic Network Interfaces and direct VPC routing.
* api-change:``evidently``: [``botocore``] This release adds support for the client-side evaluation - powered by AWS AppConfig feature.
* api-change:``kendra``: [``botocore``] This release enables our customer to choose the option of Sharepoint 2019 for the on-premise Sharepoint connector.
* api-change:``transfer``: [``botocore``] This release introduces the ability to have multiple server host keys for any of your Transfer Family servers that use the SFTP protocol.


1.24.71
=======

* api-change:``eks``: [``botocore``] Adding support for local Amazon EKS clusters on Outposts


1.24.70
=======

* api-change:``cloudtrail``: [``botocore``] This release adds CloudTrail getChannel and listChannels APIs to allow customer to view the ServiceLinkedChannel configurations.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``pi``: [``botocore``] Increases the maximum values of two RDS Performance Insights APIs. The maximum value of the Limit parameter of DimensionGroup is 25. The MaxResult maximum is now 25 for the following APIs: DescribeDimensionKeys, GetResourceMetrics, ListAvailableResourceDimensions, and ListAvailableResourceMetrics.
* api-change:``redshift``: [``botocore``] This release updates documentation for AQUA features and other description updates.


1.24.69
=======

* api-change:``ec2``: [``botocore``] This release adds support to send VPC Flow Logs to kinesis-data-firehose as new destination type
* api-change:``emr-containers``: [``botocore``] EMR on EKS now allows running Spark SQL using the newly introduced Spark SQL Job Driver in the Start Job Run API
* api-change:``lookoutmetrics``: [``botocore``] Release dimension value filtering feature to allow customers to define dimension filters for including only a subset of their dataset to be used by LookoutMetrics.
* api-change:``medialive``: [``botocore``] This change exposes API settings which allow Dolby Atmos and Dolby Vision to be used when running a channel using Elemental Media Live
* api-change:``route53``: [``botocore``] Amazon Route 53 now supports the Middle East (UAE) Region (me-central-1) for latency records, geoproximity records, and private DNS for Amazon VPCs in that region.
* api-change:``sagemaker``: [``botocore``] This release adds Mode to AutoMLJobConfig.
* api-change:``ssm``: [``botocore``] This release adds support for Systems Manager State Manager Association tagging.


1.24.68
=======

* api-change:``dataexchange``: [``botocore``] Documentation updates for AWS Data Exchange.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``eks``: [``botocore``] Adds support for EKS Addons ResolveConflicts "preserve" flag. Also adds new update failed status for EKS Addons.
* api-change:``fsx``: [``botocore``] Documentation update for Amazon FSx.
* api-change:``inspector2``: [``botocore``] This release adds new fields like fixAvailable, fixedInVersion and remediation to the finding model. The requirement to have vulnerablePackages in the finding model has also been removed. The documentation has been updated to reflect these changes.
* api-change:``iotsitewise``: [``botocore``] Allow specifying units in Asset Properties
* api-change:``sagemaker``: [``botocore``] SageMaker Hosting now allows customization on ML instance storage volume size, model data download timeout and inference container startup ping health check timeout for each ProductionVariant in CreateEndpointConfig API.
* api-change:``sns``: [``botocore``] Amazon SNS introduces the Data Protection Policy APIs, which enable customers to attach a data protection policy to an SNS topic. This allows topic owners to enable the new message data protection feature to audit and block sensitive data that is exchanged through their topics.


1.24.67
=======

* api-change:``identitystore``: [``botocore``] Documentation updates for the Identity Store CLI Reference.
* api-change:``sagemaker``: [``botocore``] This release adds HyperParameterTuningJob type in Search API.


1.24.66
=======

* api-change:``cognito-idp``: [``botocore``] This release adds a new "AuthSessionValidity" field to the UserPoolClient in Cognito. Application admins can configure this value for their users' authentication duration, which is currently fixed at 3 minutes, up to 15 minutes. Setting this field will also apply to the SMS MFA authentication flow.
* api-change:``connect``: [``botocore``] This release adds search APIs for Routing Profiles and Queues, which can be used to search for those resources within a Connect Instance.
* api-change:``mediapackage``: [``botocore``] Added support for AES_CTR encryption to CMAF origin endpoints
* api-change:``sagemaker``: [``botocore``] This release enables administrators to attribute user activity and API calls from Studio notebooks, Data Wrangler and Canvas to specific users even when users share the same execution IAM role.  ExecutionRoleIdentityConfig at Sagemaker domain level enables this feature.


1.24.65
=======

* api-change:``codeguru-reviewer``: [``botocore``] Documentation updates to fix formatting issues in CLI and SDK documentation.
* api-change:``controltower``: [``botocore``] This release contains the first SDK for AWS Control Tower. It introduces  a new set of APIs: EnableControl, DisableControl, GetControlOperation, and ListEnabledControls.
* api-change:``route53``: [``botocore``] Documentation updates for Amazon Route 53.


1.24.64
=======

* api-change:``cloudfront``: [``botocore``] Update API documentation for CloudFront origin access control (OAC)
* api-change:``identitystore``: [``botocore``] Expand IdentityStore API to support Create, Read, Update, Delete and Get operations for User, Group and GroupMembership resources.
* api-change:``iotthingsgraph``: [``botocore``] This release deprecates all APIs of the ThingsGraph service
* api-change:``ivs``: [``botocore``] IVS Merge Fragmented Streams. This release adds support for recordingReconnectWindow field in IVS recordingConfigurations. For more information see https://docs.aws.amazon.com/ivs/latest/APIReference/Welcome.html
* api-change:``rds-data``: [``botocore``] Documentation updates for RDS Data API
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now accepts Inference Recommender fields: Domain, Task, Framework, SamplePayloadUrl, SupportedContentTypes, SupportedInstanceTypes, directly in our CreateInferenceRecommendationsJob API through ContainerConfig


1.24.63
=======

* enhancement:Endpoints: [``botocore``] Deprecate SSL common name
* api-change:``greengrassv2``: [``botocore``] Adds topologyFilter to ListInstalledComponentsRequest which allows filtration of components by ROOT or ALL (including root and dependency components). Adds lastStatusChangeTimestamp to ListInstalledComponents response to show the last time a component changed state on a device.
* api-change:``identitystore``: [``botocore``] Documentation updates for the Identity Store CLI Reference.
* api-change:``lookoutequipment``: [``botocore``] This release adds new apis for providing labels.
* api-change:``macie2``: [``botocore``] This release of the Amazon Macie API adds support for using allow lists to define specific text and text patterns to ignore when inspecting data sources for sensitive data.
* api-change:``sso-admin``: [``botocore``] Documentation updates for the AWS IAM Identity Center CLI Reference.
* api-change:``sso``: [``botocore``] Documentation updates for the AWS IAM Identity Center Portal CLI Reference.


1.24.62
=======

* api-change:``fsx``: [``botocore``] Documentation updates for Amazon FSx for NetApp ONTAP.
* api-change:``voice-id``: [``botocore``] Amazon Connect Voice ID now detects voice spoofing.  When a prospective fraudster tries to spoof caller audio using audio playback or synthesized speech, Voice ID will return a risk score and outcome to indicate the how likely it is that the voice is spoofed.


1.24.61
=======

* api-change:``mediapackage``: [``botocore``] This release adds Ads AdTriggers and AdsOnDeliveryRestrictions to describe calls for CMAF endpoints on MediaPackage.
* api-change:``rds``: [``botocore``] Removes support for RDS Custom from DBInstanceClass in ModifyDBInstance


1.24.60
=======

* enhancement:Identity: [``botocore``] TokenProvider added for bearer auth support
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``gamelift``: [``botocore``] This release adds support for eight EC2 local zones as fleet locations; Atlanta, Chicago, Dallas, Denver, Houston, Kansas City (us-east-1-mci-1a), Los Angeles, and Phoenix. It also adds support for C5d, C6a, C6i, and R5d EC2 instance families.
* api-change:``iotwireless``: [``botocore``] This release includes a new feature for the customers to enable the LoRa gateways to send out beacons for Class B devices and an option to select one or more gateways for Class C devices when sending the LoRaWAN downlink messages.
* api-change:``ivschat``: [``botocore``] Documentation change for IVS Chat API Reference. Doc-only update to add a paragraph on ARNs to the Welcome section.
* api-change:``panorama``: [``botocore``] Support sorting and filtering in ListDevices API, and add more fields to device listings and single device detail
* api-change:``sso-oidc``: [``botocore``] Updated required request parameters on IAM Identity Center's OIDC CreateToken action.


1.24.59
=======

* api-change:``cloudfront``: [``botocore``] Adds support for CloudFront origin access control (OAC), making it possible to restrict public access to S3 bucket origins in all AWS Regions, those with SSE-KMS, and more.
* api-change:``config``: [``botocore``] AWS Config now supports ConformancePackTemplate documents in SSM Docs for the deployment and update of conformance packs.
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``ivs``: [``botocore``] Documentation Change for IVS API Reference - Doc-only update to type field description for CreateChannel and UpdateChannel actions and for Channel data type. Also added Amazon Resource Names (ARNs) paragraph to Welcome section.
* api-change:``quicksight``: [``botocore``] Added a new optional property DashboardVisual under ExperienceConfiguration parameter of GenerateEmbedUrlForAnonymousUser and GenerateEmbedUrlForRegisteredUser API operations. This supports embedding of specific visuals in QuickSight dashboards.
* api-change:``transfer``: [``botocore``] Documentation updates for AWS Transfer Family


1.24.58
=======

* api-change:``rds``: [``botocore``] RDS for Oracle supports Oracle Data Guard switchover and read replica backups.
* api-change:``sso-admin``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)


1.24.57
=======

* api-change:``docdb``: [``botocore``] Update document for volume clone
* api-change:``ec2``: [``botocore``] R6a instances are powered by 3rd generation AMD EPYC (Milan) processors delivering all-core turbo frequency of 3.6 GHz. C6id, M6id, and R6id instances are powered by 3rd generation Intel Xeon Scalable processor (Ice Lake) delivering all-core turbo frequency of 3.5 GHz.
* api-change:``forecast``: [``botocore``] releasing What-If Analysis APIs and update ARN regex pattern to be more strict in accordance with security recommendation
* api-change:``forecastquery``: [``botocore``] releasing What-If Analysis APIs
* api-change:``iotsitewise``: [``botocore``] Enable non-unique asset names under different hierarchies
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``securityhub``: [``botocore``] Added new resource details objects to ASFF, including resources for AwsBackupBackupVault, AwsBackupBackupPlan and AwsBackupRecoveryPoint. Added FixAvailable, FixedInVersion and Remediation  to Vulnerability.
* api-change:``support-app``: [``botocore``] This is the initial SDK release for the AWS Support App in Slack.


1.24.56
=======

* api-change:``connect``: [``botocore``] This release adds SearchSecurityProfiles API which can be used to search for Security Profile resources within a Connect Instance.
* api-change:``ivschat``: [``botocore``] Documentation Change for IVS Chat API Reference - Doc-only update to change text/description for tags field.
* api-change:``kendra``: [``botocore``] This release adds support for a new authentication type - Personal Access Token (PAT) for confluence server.
* api-change:``lookoutmetrics``: [``botocore``] This release is to make GetDataQualityMetrics API publicly available.


1.24.55
=======

* api-change:``chime-sdk-media-pipelines``: [``botocore``] The Amazon Chime SDK now supports live streaming of real-time video from the Amazon Chime SDK sessions to streaming platforms such as Amazon IVS and Amazon Elemental MediaLive. We have also added support for concatenation to create a single media capture file.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``cognito-idp``: [``botocore``] This change is being made simply to fix the public documentation based on the models. We have included the PasswordChange and ResendCode events, along with the Pass, Fail and InProgress status. We have removed the Success and Failure status which are never returned by our APIs.
* api-change:``dynamodb``: [``botocore``] This release adds support for importing data from S3 into a new DynamoDB table
* api-change:``ec2``: [``botocore``] This release adds support for VPN log options , a new feature allowing S2S VPN connections to send IKE activity logs to CloudWatch Logs
* api-change:``networkmanager``: [``botocore``] Add TransitGatewayPeeringAttachmentId property to TransitGatewayPeering Model


1.24.54
=======

* api-change:``appmesh``: [``botocore``] AWS App Mesh release to support Multiple Listener and Access Log Format feature
* api-change:``connectcampaigns``: [``botocore``] Updated exceptions for Amazon Connect Outbound Campaign api's.
* api-change:``kendra``: [``botocore``] This release adds Zendesk connector (which allows you to specify Zendesk SAAS platform as data source), Proxy Support for Sharepoint and Confluence Server (which allows you to specify the proxy configuration if proxy is required to connect to your Sharepoint/Confluence Server as data source).
* api-change:``lakeformation``: [``botocore``] This release adds a new API support "AssumeDecoratedRoleWithSAML" and also release updates the corresponding documentation.
* api-change:``lambda``: [``botocore``] Added support for customization of Consumer Group ID for MSK and Kafka Event Source Mappings.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``rds``: [``botocore``] Adds support for Internet Protocol Version 6 (IPv6) for RDS Aurora database clusters.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager.


1.24.53
=======

* api-change:``rekognition``: [``botocore``] This release adds APIs which support copying an Amazon Rekognition Custom Labels model and managing project policies across AWS account.
* api-change:``servicecatalog``: [``botocore``] Documentation updates for Service Catalog


1.24.52
=======

* enhancement:AWSCRT: [``botocore``] Upgrade awscrt version to 0.14.0
* api-change:``cloudfront``: [``botocore``] Adds Http 3 support to distributions
* api-change:``identitystore``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)
* api-change:``sso``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)
* api-change:``wisdom``: [``botocore``] This release introduces a new API PutFeedback that allows submitting feedback to Wisdom on content relevance.


1.24.51
=======

* api-change:``amp``: [``botocore``] This release adds log APIs that allow customers to manage logging for their Amazon Managed Service for Prometheus workspaces.
* api-change:``chime-sdk-messaging``: [``botocore``] The Amazon Chime SDK now supports channels with up to one million participants with elastic channels.
* api-change:``ivs``: [``botocore``] Updates various list api MaxResults ranges
* api-change:``personalize-runtime``: [``botocore``] This release provides support for promotions in AWS Personalize runtime.
* api-change:``rds``: [``botocore``] Adds support for RDS Custom to DBInstanceClass in ModifyDBInstance


1.24.50
=======

* api-change:``backupstorage``: [``botocore``] This is the first public release of AWS Backup Storage. We are exposing some previously-internal APIs for use by external services. These APIs are not meant to be used directly by customers.
* api-change:``glue``: [``botocore``] Add support for Python 3.9 AWS Glue Python Shell jobs
* api-change:``privatenetworks``: [``botocore``] This is the initial SDK release for AWS Private 5G. AWS Private 5G is a managed service that makes it easy to deploy, operate, and scale your own private mobile network at your on-premises location.


1.24.49
=======

* api-change:``dlm``: [``botocore``] This release adds support for excluding specific data (non-boot) volumes from multi-volume snapshot sets created by snapshot lifecycle policies
* api-change:``ec2``: [``botocore``] This release adds support for excluding specific data (non-root) volumes from multi-volume snapshot sets created from instances.


1.24.48
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``location``: [``botocore``] Amazon Location Service now allows circular geofences in BatchPutGeofence, PutGeofence, and GetGeofence  APIs.
* api-change:``sagemaker-a2i-runtime``: [``botocore``] Fix bug with parsing ISO-8601 CreationTime in Java SDK in DescribeHumanLoop
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Automatic Model Tuning now supports specifying multiple alternate EC2 instance types to make tuning jobs more robust when the preferred instance type is not available due to insufficient capacity.


1.24.47
=======

* api-change:``glue``: [``botocore``] Add an option to run non-urgent or non-time sensitive Glue Jobs on spare capacity
* api-change:``identitystore``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)
* api-change:``iotwireless``: [``botocore``] AWS IoT Wireless release support for sidewalk data reliability.
* api-change:``pinpoint``: [``botocore``] Adds support for Advance Quiet Time in Journeys. Adds RefreshOnSegmentUpdate and WaitForQuietTime to JourneyResponse.
* api-change:``quicksight``: [``botocore``] A series of documentation updates to the QuickSight API reference.
* api-change:``sso-admin``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)
* api-change:``sso-oidc``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)
* api-change:``sso``: [``botocore``] Documentation updates to reflect service rename - AWS IAM Identity Center (successor to AWS Single Sign-On)


1.24.46
=======

* enhancement:Lambda: [``botocore``] Add support for Trace ID in Lambda environments
* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for Tags on Amazon Chime SDK WebRTC sessions
* api-change:``config``: [``botocore``] Add resourceType enums for Athena, GlobalAccelerator, Detective and EC2 types
* api-change:``dms``: [``botocore``] Documentation updates for Database Migration Service (DMS).
* api-change:``iot``: [``botocore``] The release is to support attach a provisioning template to CACert for JITP function,  Customer now doesn't have to hardcode a roleArn and templateBody during register a CACert to enable JITP.


1.24.45
=======

* api-change:``cognito-idp``: [``botocore``] Add a new exception type, ForbiddenException, that is returned when request is not allowed
* api-change:``wafv2``: [``botocore``] You can now associate an AWS WAF web ACL with an Amazon Cognito user pool.


1.24.44
=======

* api-change:``license-manager-user-subscriptions``: [``botocore``] This release supports user based subscription for Microsoft Visual Studio Professional and Enterprise on EC2.
* api-change:``personalize``: [``botocore``] This release adds support for incremental bulk ingestion for the Personalize CreateDatasetImportJob API.


1.24.43
=======

* api-change:``config``: [``botocore``] Documentation update for PutConfigRule and PutOrganizationConfigRule
* api-change:``workspaces``: [``botocore``] This release introduces ModifySamlProperties, a new API that allows control of SAML properties associated with a WorkSpaces directory. The DescribeWorkspaceDirectories API will now additionally return SAML properties in its responses.


1.24.42
=======

* bugfix:TraceId: [``botocore``] Rollback bugfix for obeying _X_AMZN_TRACE_ID env var


1.24.41
=======

* bugfix:Config: [``botocore``] Obey _X_AMZN_TRACE_ID environment variable instead of _X_AMZ_TRACE_ID
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``fsx``: [``botocore``] Documentation updates for Amazon FSx
* api-change:``shield``: [``botocore``] AWS Shield Advanced now supports filtering for ListProtections and ListProtectionGroups.


1.24.40
=======

* api-change:``ec2``: [``botocore``] Documentation updates for VM Import/Export.
* api-change:``es``: [``botocore``] This release adds support for gp3 EBS (Elastic Block Store) storage.
* api-change:``lookoutvision``: [``botocore``] This release introduces support for image segmentation models and updates CPU accelerator options for models hosted on edge devices.
* api-change:``opensearch``: [``botocore``] This release adds support for gp3 EBS (Elastic Block Store) storage.


1.24.39
=======

* api-change:``auditmanager``: [``botocore``] This release adds an exceeded quota exception to several APIs. We added a ServiceQuotaExceededException for the following operations: CreateAssessment, CreateControl, CreateAssessmentFramework, and UpdateAssessmentStatus.
* api-change:``chime``: [``botocore``] Chime VoiceConnector will now support ValidateE911Address which will allow customers to prevalidate their addresses included in their SIP invites for emergency calling
* api-change:``config``: [``botocore``] This release adds ListConformancePackComplianceScores API to support the new compliance score feature, which provides a percentage of the number of compliant rule-resource combinations in a conformance pack compared to the number of total possible rule-resource combinations in the conformance pack.
* api-change:``globalaccelerator``: [``botocore``] Global Accelerator now supports dual-stack accelerators, enabling support for IPv4 and IPv6 traffic.
* api-change:``marketplace-catalog``: [``botocore``] The SDK for the StartChangeSet API will now automatically set and use an idempotency token in the ClientRequestToken request parameter if the customer does not provide it.
* api-change:``polly``: [``botocore``] Amazon Polly adds new English and Hindi voice - Kajal. Kajal is available as Neural voice only.
* api-change:``ssm``: [``botocore``] Adding doc updates for OpsCenter support in Service Setting actions.
* api-change:``workspaces``: [``botocore``] Added CreateWorkspaceImage API to create a new WorkSpace image from an existing WorkSpace.


1.24.38
=======

* api-change:``appsync``: [``botocore``] Adds support for a new API to evaluate mapping templates with mock data, allowing you to remotely unit test your AppSync resolvers and functions.
* api-change:``detective``: [``botocore``] Added the ability to get data source package information for the behavior graph. Graph administrators can now start (or stop) optional datasources on the behavior graph.
* api-change:``guardduty``: [``botocore``] Amazon GuardDuty introduces a new Malware Protection feature that triggers malware scan on selected EC2 instance resources, after the service detects a potentially malicious activity.
* api-change:``lookoutvision``: [``botocore``] This release introduces support for the automatic scaling of inference units used by Amazon Lookout for Vision models.
* api-change:``macie2``: [``botocore``] This release adds support for retrieving (revealing) sample occurrences of sensitive data that Amazon Macie detects and reports in findings.
* api-change:``rds``: [``botocore``] Adds support for using RDS Proxies with RDS for MariaDB databases.
* api-change:``rekognition``: [``botocore``] This release introduces support for the automatic scaling of inference units used by Amazon Rekognition Custom Labels models.
* api-change:``securityhub``: [``botocore``] Documentation updates for AWS Security Hub
* api-change:``transfer``: [``botocore``] AWS Transfer Family now supports Applicability Statement 2 (AS2), a network protocol used for the secure and reliable transfer of critical Business-to-Business (B2B) data over the public internet using HTTP/HTTPS as the transport mechanism.


1.24.37
=======

* api-change:``autoscaling``: [``botocore``] Documentation update for Amazon EC2 Auto Scaling.


1.24.36
=======

* api-change:``account``: [``botocore``] This release enables customers to manage the primary contact information for their AWS accounts. For more information, see https://docs.aws.amazon.com/accounts/latest/reference/API_Operations.html
* api-change:``ec2``: [``botocore``] Added support for EC2 M1 Mac instances. For more information, please visit aws.amazon.com/mac.
* api-change:``iotdeviceadvisor``: [``botocore``] Added new service feature (Early access only) - Long Duration Test, where customers can test the IoT device to observe how it behaves when the device is in operation for longer period.
* api-change:``medialive``: [``botocore``] Link devices now support remote rebooting. Link devices now support maintenance windows. Maintenance windows allow a Link device to install software updates without stopping the MediaLive channel. The channel will experience a brief loss of input from the device while updates are installed.
* api-change:``rds``: [``botocore``] This release adds the "ModifyActivityStream" API with support for audit policy state locking and unlocking.
* api-change:``transcribe``: [``botocore``] Remove unsupported language codes for StartTranscriptionJob and update VocabularyFileUri for UpdateMedicalVocabulary


1.24.35
=======

* api-change:``athena``: [``botocore``] This feature allows customers to retrieve runtime statistics for completed queries
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``dms``: [``botocore``] Documentation updates for Database Migration Service (DMS).
* api-change:``docdb``: [``botocore``] Enable copy-on-write restore type
* api-change:``ec2-instance-connect``: [``botocore``] This release includes a new exception type "EC2InstanceUnavailableException" for SendSSHPublicKey and SendSerialConsoleSSHPublicKey APIs.
* api-change:``frauddetector``: [``botocore``] The release introduces Account Takeover Insights (ATI) model. The ATI model detects fraud relating to account takeover. This release also adds support for new variable types: ARE_CREDENTIALS_VALID and SESSION_ID and adds new structures to Model Version APIs.
* api-change:``iotsitewise``: [``botocore``] Added asynchronous API to ingest bulk historical and current data into IoT SiteWise.
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides Oauth2 support for SharePoint Online. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html
* api-change:``network-firewall``: [``botocore``] Network Firewall now supports referencing dynamic IP sets from stateful rule groups, for IP sets stored in Amazon VPC prefix lists.
* api-change:``rds``: [``botocore``] Adds support for creating an RDS Proxy for an RDS for MariaDB database.


1.24.34
=======

* api-change:``acm-pca``: [``botocore``] AWS Certificate Manager (ACM) Private Certificate Authority (PCA) documentation updates
* api-change:``iot``: [``botocore``] GA release the ability to enable/disable IoT Fleet Indexing for Device Defender and Named Shadow information, and search them through IoT Fleet Indexing APIs. This includes Named Shadow Selection as a part of the UpdateIndexingConfiguration API.


1.24.33
=======

* api-change:``devops-guru``: [``botocore``] Added new APIs for log anomaly detection feature.
* api-change:``glue``: [``botocore``] Documentation updates for AWS Glue Job Timeout and Autoscaling
* api-change:``sagemaker-edge``: [``botocore``] Amazon SageMaker Edge Manager provides lightweight model deployment feature to deploy machine learning models on requested devices.
* api-change:``sagemaker``: [``botocore``] Fixed an issue with cross account QueryLineage
* api-change:``workspaces``: [``botocore``] Increased the character limit of the login message from 850 to 2000 characters.


1.24.32
=======

* api-change:``discovery``: [``botocore``] Add AWS Agentless Collector details to the GetDiscoverySummary API response
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``elasticache``: [``botocore``] Adding AutoMinorVersionUpgrade in the DescribeReplicationGroups API
* api-change:``kms``: [``botocore``] Added support for the SM2 KeySpec in China Partition Regions
* api-change:``mediapackage``: [``botocore``] This release adds "IncludeIframeOnlyStream" for Dash endpoints and increases the number of supported video and audio encryption presets for Speke v2
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Edge Manager provides lightweight model deployment feature to deploy machine learning models on requested devices.
* api-change:``sso-admin``: [``botocore``] AWS SSO now supports attaching customer managed policies and a permissions boundary to your permission sets. This release adds new API operations to manage and view the customer managed policies and the permissions boundary for a given permission set.


1.24.31
=======

* api-change:``datasync``: [``botocore``] Documentation updates for AWS DataSync regarding configuring Amazon FSx for ONTAP location security groups and SMB user permissions.
* api-change:``drs``: [``botocore``] Changed existing APIs to allow choosing a dynamic volume type for replicating volumes, to reduce costs for customers.
* api-change:``evidently``: [``botocore``] This release adds support for the new segmentation feature.
* api-change:``wafv2``: [``botocore``] This SDK release provide customers ability to add sensitivity level for WAF SQLI Match Statements.


1.24.30
=======

* api-change:``athena``: [``botocore``] This release updates data types that contain either QueryExecutionId, NamedQueryId or ExpectedBucketOwner. Ids must be between 1 and 128 characters and contain only non-whitespace characters. ExpectedBucketOwner must be 12-digit string.
* api-change:``codeartifact``: [``botocore``] This release introduces Package Origin Controls, a mechanism used to counteract Dependency Confusion attacks. Adds two new APIs, PutPackageOriginConfiguration and DescribePackage, and updates the ListPackage, DescribePackageVersion and ListPackageVersion APIs in support of the feature.
* api-change:``config``: [``botocore``] Update ResourceType enum with values for Route53Resolver, Batch, DMS, Workspaces, Stepfunctions, SageMaker, ElasticLoadBalancingV2, MSK types
* api-change:``ec2``: [``botocore``] This release adds flow logs for Transit Gateway to  allow customers to gain deeper visibility and insights into network traffic through their Transit Gateways.
* api-change:``fms``: [``botocore``] Adds support for strict ordering in stateful rule groups in Network Firewall policies.
* api-change:``glue``: [``botocore``] This release adds an additional worker type for Glue Streaming jobs.
* api-change:``inspector2``: [``botocore``] This release adds support for Inspector V2 scan configurations through the get and update configuration APIs. Currently this allows configuring ECR automated re-scan duration to lifetime or 180 days or 30 days.
* api-change:``kendra``: [``botocore``] This release adds AccessControlConfigurations which allow you to redefine your document level access control without the need for content re-indexing.
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio adds support for IAM-based access to AWS resources for Nimble Studio components and custom studio components. Studio Component scripts use these roles on Nimble Studio workstation to mount filesystems, access S3 buckets, or other configured resources in the Studio's AWS account
* api-change:``outposts``: [``botocore``] This release adds the ShipmentInformation and AssetInformationList fields to the GetOrder API response.
* api-change:``sagemaker``: [``botocore``] This release adds support for G5, P4d, and C6i instance types in Amazon SageMaker Inference and increases the number of hyperparameters that can be searched from 20 to 30 in Amazon SageMaker Automatic Model Tuning


1.24.29
=======

* api-change:``appconfig``: [``botocore``] Adding Create, Get, Update, Delete, and List APIs for new two new resources: Extensions and ExtensionAssociations.


1.24.28
=======

* api-change:``networkmanager``: [``botocore``] This release adds general availability API support for AWS Cloud WAN.


1.24.27
=======

* api-change:``ec2``: [``botocore``] Build, manage, and monitor a unified global network that connects resources running across your cloud and on-premises environments using the AWS Cloud WAN APIs.
* api-change:``redshift-serverless``: [``botocore``] Removed prerelease language for GA launch.
* api-change:``redshift``: [``botocore``] This release adds a new --snapshot-arn field for describe-cluster-snapshots, describe-node-configuration-options, restore-from-cluster-snapshot, authorize-snapshot-acsess, and revoke-snapshot-acsess APIs. It allows customers to give a Redshift snapshot ARN or a Redshift Serverless ARN as input.


1.24.26
=======

* api-change:``backup``: [``botocore``] This release adds support for authentication using IAM user identity instead of passed IAM role, identified by excluding the IamRoleArn field in the StartRestoreJob API. This feature applies to only resource clients with a destructive restore nature (e.g. SAP HANA).


1.24.25
=======

* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for AppKeys and TenantIds in Amazon Chime SDK WebRTC sessions
* api-change:``dms``: [``botocore``] New api to migrate event subscriptions to event bridge rules
* api-change:``iot``: [``botocore``] This release adds support to register a CA certificate without having to provide a verification certificate. This also allows multiple AWS accounts to register the same CA in the same region.
* api-change:``iotwireless``: [``botocore``] Adds 5 APIs: PutPositionConfiguration, GetPositionConfiguration, ListPositionConfigurations, UpdatePosition, GetPosition for the new Positioning Service feature which enables customers to configure solvers to calculate position of LoRaWAN devices, or specify position of LoRaWAN devices & gateways.
* api-change:``sagemaker``: [``botocore``] Heterogeneous clusters: the ability to launch training jobs with multiple instance types. This enables running component of the training job on the instance type that is most suitable for it. e.g. doing data processing and augmentation on CPU instances and neural network training on GPU instances


1.24.24
=======

* api-change:``cloudformation``: [``botocore``] My AWS Service (placeholder) - Add a new feature Account-level Targeting for StackSet operation
* api-change:``synthetics``: [``botocore``] This release introduces Group feature, which enables users to group cross-region canaries.


1.24.23
=======

* api-change:``config``: [``botocore``] Updating documentation service limits
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``quicksight``: [``botocore``] This release allows customers to programmatically create QuickSight accounts with Enterprise and Enterprise + Q editions. It also releases allowlisting domains for embedding QuickSight dashboards at runtime through the embedding APIs.
* api-change:``rds``: [``botocore``] Adds waiters support for DBCluster.
* api-change:``rolesanywhere``: [``botocore``] IAM Roles Anywhere allows your workloads such as servers, containers, and applications to obtain temporary AWS credentials and use the same IAM roles and policies that you have configured for your AWS workloads to access AWS resources.
* api-change:``ssm-incidents``: [``botocore``] Adds support for tagging incident-record on creation by providing incident tags in the template within a response-plan.


1.24.22
=======

* api-change:``dms``: [``botocore``] Added new features for AWS DMS version 3.4.7 that includes new endpoint settings for S3, OpenSearch, Postgres, SQLServer and Oracle.
* api-change:``rds``: [``botocore``] Adds support for additional retention periods to Performance Insights.


1.24.21
=======

* api-change:``athena``: [``botocore``] This feature introduces the API support for Athena's parameterized query and BatchGetPreparedStatement API.
* api-change:``customer-profiles``: [``botocore``] This release adds the optional MinAllowedConfidenceScoreForMerging parameter to the CreateDomain, UpdateDomain, and GetAutoMergingPreview APIs in Customer Profiles. This parameter is used as a threshold to influence the profile auto-merging step of the Identity Resolution process.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``glue``: [``botocore``] This release adds tag as an input of CreateDatabase
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for alfresco
* api-change:``mwaa``: [``botocore``] Documentation updates for Amazon Managed Workflows for Apache Airflow.
* api-change:``pricing``: [``botocore``] Documentation update for GetProducts Response.
* api-change:``wellarchitected``: [``botocore``] Added support for UpdateGlobalSettings API. Added status filter to ListWorkloadShares and ListLensShares.
* api-change:``workmail``: [``botocore``] This release adds support for managing user availability configurations in Amazon WorkMail.


1.24.20
=======

* api-change:``appstream``: [``botocore``] Includes support for StreamingExperienceSettings in CreateStack and UpdateStack APIs
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``medialive``: [``botocore``] This release adds support for automatic renewal of MediaLive reservations at the end of each reservation term. Automatic renewal is optional. This release also adds support for labelling accessibility-focused audio and caption tracks in HLS outputs.
* api-change:``redshift-serverless``: [``botocore``] Add new API operations for Amazon Redshift Serverless, a new way of using Amazon Redshift without needing to manually manage provisioned clusters. The new operations let you interact with Redshift Serverless resources, such as create snapshots, list VPC endpoints, delete resource policies, and more.
* api-change:``sagemaker``: [``botocore``] This release adds: UpdateFeatureGroup, UpdateFeatureMetadata, DescribeFeatureMetadata APIs; FeatureMetadata type in Search API; LastModifiedTime, LastUpdateStatus, OnlineStoreTotalSizeBytes in DescribeFeatureGroup API.
* api-change:``translate``: [``botocore``] Added ListLanguages API which can be used to list the languages supported by Translate.


1.24.19
=======

* api-change:``datasync``: [``botocore``] AWS DataSync now supports Amazon FSx for NetApp ONTAP locations.
* api-change:``ec2``: [``botocore``] This release adds a new spread placement group to EC2 Placement Groups: host level spread, which spread instances between physical hosts, available to Outpost customers only. CreatePlacementGroup and DescribePlacementGroups APIs were updated with a new parameter: SpreadLevel to support this feature.
* api-change:``finspace-data``: [``botocore``] Release new API GetExternalDataViewAccessDetails
* api-change:``polly``: [``botocore``] Add 4 new neural voices - Pedro (es-US), Liam (fr-CA), Daniel (de-DE) and Arthur (en-GB).


1.24.18
=======

* api-change:``iot``: [``botocore``] This release ease the restriction for the input of tag value to align with AWS standard, now instead of min length 1, we change it to min length 0.


1.24.17
=======

* api-change:``glue``: [``botocore``] This release enables the new ListCrawls API for viewing the AWS Glue Crawler run history.
* api-change:``rds-data``: [``botocore``] Documentation updates for RDS Data API


1.24.16
=======

* api-change:``lookoutequipment``: [``botocore``] This release adds visualizations to the scheduled inference results. Users will be able to see interference results, including diagnostic results from their running inference schedulers.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has released support for automatic DolbyVision metadata generation when converting HDR10 to DolbyVision.
* api-change:``mgn``: [``botocore``] New and modified APIs for the Post-Migration Framework
* api-change:``migration-hub-refactor-spaces``: [``botocore``] This release adds the new API UpdateRoute that allows route to be updated to ACTIVE/INACTIVE state. In addition, CreateRoute API will now allow users to create route in ACTIVE/INACTIVE state.
* api-change:``sagemaker``: [``botocore``] SageMaker Ground Truth now supports Virtual Private Cloud. Customers can launch labeling jobs and access to their private workforce in VPC mode.


1.24.15
=======

* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway
* api-change:``pricing``: [``botocore``] This release introduces 1 update to the GetProducts API. The serviceCode attribute is now required when you use the GetProductsRequest.
* api-change:``transfer``: [``botocore``] Until today, the service supported only RSA host keys and user keys. Now with this launch, Transfer Family has expanded the support for ECDSA and ED25519 host keys and user keys, enabling customers to support a broader set of clients by choosing RSA, ECDSA, and ED25519 host and user keys.


1.24.14
=======

* api-change:``ec2``: [``botocore``] This release adds support for Private IP VPNs, a new feature allowing S2S VPN connections to use private ip addresses as the tunnel outside ip address over Direct Connect as transport.
* api-change:``ecs``: [``botocore``] Amazon ECS UpdateService now supports the following parameters: PlacementStrategies, PlacementConstraints and CapacityProviderStrategy.
* api-change:``wellarchitected``: [``botocore``] Adds support for lens tagging, Adds support for multiple helpful-resource urls and multiple improvement-plan urls.


1.24.13
=======

* api-change:``ds``: [``botocore``] This release adds support for describing and updating AWS Managed Microsoft AD settings
* api-change:``kafka``: [``botocore``] Documentation updates to use Az Id during cluster creation.
* api-change:``outposts``: [``botocore``] This release adds the AssetLocation structure to the ListAssets response. AssetLocation includes the RackElevation for an Asset.


1.24.12
=======

* api-change:``connect``: [``botocore``] This release updates these APIs: UpdateInstanceAttribute, DescribeInstanceAttribute and ListInstanceAttributes. You can use it to programmatically enable/disable High volume outbound communications using attribute type HIGH_VOLUME_OUTBOUND on the specified Amazon Connect instance.
* api-change:``connectcampaigns``: [``botocore``] Added Amazon Connect high volume outbound communications SDK.
* api-change:``dynamodb``: [``botocore``] Doc only update for DynamoDB service
* api-change:``dynamodbstreams``: [``botocore``] Update dynamodbstreams client to latest version


1.24.11
=======

* api-change:``redshift-data``: [``botocore``] This release adds a new --workgroup-name field to operations that connect to an endpoint. Customers can now execute queries against their serverless workgroups.
* api-change:``redshiftserverless``: [``botocore``] Add new API operations for Amazon Redshift Serverless, a new way of using Amazon Redshift without needing to manually manage provisioned clusters. The new operations let you interact with Redshift Serverless resources, such as create snapshots, list VPC endpoints, delete resource policies, and more.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``securityhub``: [``botocore``] Added Threats field for security findings. Added new resource details for ECS Container, ECS Task, RDS SecurityGroup, Kinesis Stream, EC2 TransitGateway, EFS AccessPoint, CloudFormation Stack, CloudWatch Alarm, VPC Peering Connection and WAF Rules


1.24.10
=======

* api-change:``finspace-data``: [``botocore``] This release adds a new set of APIs, GetPermissionGroup, DisassociateUserFromPermissionGroup, AssociateUserToPermissionGroup, ListPermissionGroupsByUser, ListUsersByPermissionGroup.
* api-change:``guardduty``: [``botocore``] Adds finding fields available from GuardDuty Console. Adds FreeTrial related operations. Deprecates the use of various APIs related to Master Accounts and Replace them with Administrator Accounts.
* api-change:``servicecatalog-appregistry``: [``botocore``] This release adds a new API ListAttributeGroupsForApplication that returns associated attribute groups of an application. In addition, the UpdateApplication and UpdateAttributeGroup APIs will not allow users to update the 'Name' attribute.
* api-change:``workspaces``: [``botocore``] Added new field "reason" to OperationNotSupportedException. Receiving this exception in the DeregisterWorkspaceDirectory API will now return a reason giving more context on the failure.


1.24.9
======

* api-change:``budgets``: [``botocore``] Add a budgets ThrottlingException. Update the CostFilters value pattern.
* api-change:``lookoutmetrics``: [``botocore``] Adding filters to Alert and adding new UpdateAlert API.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for rules that constrain Automatic-ABR rendition selection when generating ABR package ladders.


1.24.8
======

* api-change:``outposts``: [``botocore``] This release adds API operations AWS uses to install Outpost servers.


1.24.7
======

* api-change:``frauddetector``: [``botocore``] Documentation updates for Amazon Fraud Detector (AWSHawksNest)


1.24.6
======

* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for live transcription in AWS GovCloud (US) Regions.


1.24.5
======

* api-change:``dms``: [``botocore``] This release adds DMS Fleet Advisor APIs and exposes functionality for DMS Fleet Advisor. It adds functionality to create and modify fleet advisor instances, and to collect and analyze information about the local data infrastructure.
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``m2``: [``botocore``] AWS Mainframe Modernization service is a managed mainframe service and set of tools for planning, migrating, modernizing, and running mainframe workloads on AWS
* api-change:``neptune``: [``botocore``] This release adds support for Neptune to be configured as a global database, with a primary DB cluster in one region, and up to five secondary DB clusters in other regions.
* api-change:``redshift-serverless``: [``botocore``] Add new API operations for Amazon Redshift Serverless, a new way of using Amazon Redshift without needing to manually manage provisioned clusters. The new operations let you interact with Redshift Serverless resources, such as create snapshots, list VPC endpoints, delete resource policies, and more.
* api-change:``redshift``: [``botocore``] Adds new API GetClusterCredentialsWithIAM to return temporary credentials.


1.24.4
======

* api-change:``auditmanager``: [``botocore``] This release introduces 2 updates to the Audit Manager API. The roleType and roleArn attributes are now required when you use the CreateAssessment or UpdateAssessment operation. We also added a throttling exception to the RegisterAccount API operation.
* api-change:``ce``: [``botocore``] Added two new APIs to support cost allocation tags operations: ListCostAllocationTags, UpdateCostAllocationTagsStatus.


1.24.3
======

* api-change:``chime-sdk-messaging``: [``botocore``] This release adds support for searching channels by members via the SearchChannels API, removes required restrictions for Name and Mode in UpdateChannel API and enhances CreateChannel API by exposing member and moderator list as well as channel id as optional parameters.
* api-change:``connect``: [``botocore``] This release adds a new API, GetCurrentUserData, which returns real-time details about users' current activity.


1.24.2
======

* api-change:``codeartifact``: [``botocore``] Documentation updates for CodeArtifact
* api-change:``voice-id``: [``botocore``] Added a new attribute ServerSideEncryptionUpdateDetails to Domain and DomainSummary.
* api-change:``proton``: [``botocore``] Add new "Components" API to enable users to Create, Delete and Update AWS Proton components.
* api-change:``connect``: [``botocore``] This release adds the following features: 1) New APIs to manage (create, list, update) task template resources, 2) Updates to startTaskContact API to support task templates, and 3) new TransferContact API to programmatically transfer in-progress tasks via a contact flow.
* api-change:``application-insights``: [``botocore``] Provide Account Level onboarding support through CFN/CLI
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for GitHub. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-github.html


1.24.1
======

* api-change:``backup-gateway``: [``botocore``] Adds GetGateway and UpdateGatewaySoftwareNow API and adds hypervisor name to UpdateHypervisor API
* api-change:``forecast``: [``botocore``] Added Format field to Import and Export APIs in Amazon Forecast. Added TimeSeriesSelector to Create Forecast API.
* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for centrally controlling each participant's ability to send and receive audio, video and screen share within a WebRTC session.  Attendee capabilities can be specified when the attendee is created and updated during the session with the new BatchUpdateAttendeeCapabilitiesExcept API.
* api-change:``route53``: [``botocore``] Add new APIs to support Route 53 IP Based Routing


1.24.0
======

* api-change:``iotsitewise``: [``botocore``] This release adds the following new optional field to the IoT SiteWise asset resource: assetDescription.
* api-change:``lookoutmetrics``: [``botocore``] Adding backtest mode to detectors using the Cloudwatch data source.
* api-change:``transcribe``: [``botocore``] Amazon Transcribe now supports automatic language identification for multi-lingual audio in batch mode.
* feature:Python: Dropped support for Python 3.6
* feature:Python: [``botocore``] Dropped support for Python 3.6
* api-change:``cognito-idp``: [``botocore``] Amazon Cognito now supports IP Address propagation for all unauthenticated APIs (e.g. SignUp, ForgotPassword).
* api-change:``drs``: [``botocore``] Changed existing APIs and added new APIs to accommodate using multiple AWS accounts with AWS Elastic Disaster Recovery.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Notebook Instances now support Jupyter Lab 3.


1.23.10
=======

* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Notebook Instances now allows configuration of Instance Metadata Service version and Amazon SageMaker Studio now supports G5 instance types.
* api-change:``appflow``: [``botocore``] Adding the following features/changes: Parquet output that preserves typing from the source connector, Failed executions threshold before deactivation for scheduled flows, increasing max size of access and refresh token from 2048 to 4096
* api-change:``datasync``: [``botocore``] AWS DataSync now supports TLS encryption in transit, file system policies and access points for EFS locations.
* api-change:``emr-serverless``: [``botocore``] This release adds support for Amazon EMR Serverless, a serverless runtime environment that simplifies running analytics applications using the latest open source frameworks such as Apache Spark and Apache Hive.


1.23.9
======

* api-change:``lightsail``: [``botocore``] Amazon Lightsail now supports the ability to configure a Lightsail Container Service to pull images from Amazon ECR private repositories in your account.
* api-change:``emr-serverless``: [``botocore``] This release adds support for Amazon EMR Serverless, a serverless runtime environment that simplifies running analytics applications using the latest open source frameworks such as Apache Spark and Apache Hive.
* api-change:``ec2``: [``botocore``] C7g instances, powered by the latest generation AWS Graviton3 processors, provide the best price performance in Amazon EC2 for compute-intensive workloads.
* api-change:``forecast``: [``botocore``] Introduced a new field in Auto Predictor as Time Alignment Boundary. It helps in aligning the timestamps generated during Forecast exports


1.23.8
======

* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``fsx``: [``botocore``] This release adds root squash support to FSx for Lustre to restrict root level access from clients by mapping root users to a less-privileged user/group with limited permissions.
* api-change:``lookoutmetrics``: [``botocore``] Adding AthenaSourceConfig for MetricSet APIs to support Athena as a data source.
* api-change:``voice-id``: [``botocore``] VoiceID will now automatically expire Speakers if they haven't been accessed for Enrollment, Re-enrollment or Successful Auth for three years. The Speaker APIs now return a "LastAccessedAt" time for Speakers, and the EvaluateSession API returns "SPEAKER_EXPIRED" Auth Decision for EXPIRED Speakers.
* api-change:``cloudformation``: [``botocore``] Add a new parameter statusReason to DescribeStackSetOperation output for additional details
* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway
* api-change:``apprunner``: [``botocore``] Documentation-only update added for CodeConfiguration.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds support for manually selecting features from the input dataset using the CreateAutoMLJob API.


1.23.7
======

* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for rules that constrain Automatic-ABR rendition selection when generating ABR package ladders.
* api-change:``cognito-idp``: [``botocore``] Amazon Cognito now supports requiring attribute verification (ex. email and phone number) before update.
* api-change:``networkmanager``: [``botocore``] This release adds Multi Account API support for a TGW Global Network, to enable and disable AWSServiceAccess with AwsOrganizations for Network Manager service and dependency CloudFormation StackSets service.
* api-change:``ivschat``: [``botocore``] Doc-only update. For MessageReviewHandler structure, added timeout period in the description of the fallbackResult field
* api-change:``ec2``: [``botocore``] Stop Protection feature enables customers to protect their instances from accidental stop actions.


1.23.6
======

* api-change:``elasticache``: [``botocore``] Added support for encryption in transit for Memcached clusters. Customers can now launch Memcached cluster with encryption in transit enabled when using Memcached version 1.6.12 or later.
* api-change:``forecast``: [``botocore``] New APIs for Monitor that help you understand how your predictors perform over time.
* api-change:``personalize``: [``botocore``] Adding modelMetrics as part of DescribeRecommender API response for Personalize.


1.23.5
======

* api-change:``comprehend``: [``botocore``] Comprehend releases 14 new entity types for DetectPiiEntities and ContainsPiiEntities APIs.
* api-change:``logs``: [``botocore``] Doc-only update to publish the new valid values for log retention


1.23.4
======

* api-change:``gamesparks``: [``botocore``] This release adds an optional DeploymentResult field in the responses of GetStageDeploymentIntegrationTests and ListStageDeploymentIntegrationTests APIs.
* enhancement:StreamingBody: [``botocore``] Allow StreamingBody to be used as a context manager
* api-change:``lookoutmetrics``: [``botocore``] In this release we added SnsFormat to SNSConfiguration to support human readable alert.


1.23.3
======

* api-change:``greengrassv2``: [``botocore``] This release adds the new DeleteDeployment API operation that you can use to delete deployment resources. This release also adds support for discontinued AWS-provided components, so AWS can communicate when a component has any issues that you should consider before you deploy it.
* api-change:``quicksight``: [``botocore``] API UpdatePublicSharingSettings enables IAM admins to enable/disable account level setting for public access of dashboards. When enabled, owners/co-owners for dashboards can enable public access on their dashboards. These dashboards can only be accessed through share link or embedding.
* api-change:``appmesh``: [``botocore``] This release updates the existing Create and Update APIs for meshes and virtual nodes by adding a new IP preference field. This new IP preference field can be used to control the IP versions being used with the mesh and allows for IPv6 support within App Mesh.
* api-change:``batch``: [``botocore``] Documentation updates for AWS Batch.
* api-change:``iotevents-data``: [``botocore``] Introducing new API for deleting detectors: BatchDeleteDetector.
* api-change:``transfer``: [``botocore``] AWS Transfer Family now supports SetStat server configuration option, which provides the ability to ignore SetStat command issued by file transfer clients, enabling customers to upload files without any errors.


1.23.2
======

* api-change:``kms``: [``botocore``] Add HMAC best practice tip, annual rotation of AWS managed keys.
* api-change:``glue``: [``botocore``] This release adds a new optional parameter called codeGenNodeConfiguration to CRUD job APIs that allows users to manage visual jobs via APIs. The updated CreateJob and UpdateJob will create jobs that can be viewed in Glue Studio as a visual graph. GetJob can be used to get codeGenNodeConfiguration.


1.23.1
======

* api-change:``resiliencehub``: [``botocore``] In this release, we are introducing support for Amazon Elastic Container Service, Amazon Route 53, AWS Elastic Disaster Recovery, AWS Backup in addition to the existing supported Services.  This release also supports Terraform file input from S3 and scheduling daily assessments
* api-change:``servicecatalog``: [``botocore``] Updated the descriptions for the ListAcceptedPortfolioShares API description and the PortfolioShareType parameters.
* api-change:``discovery``: [``botocore``] Add Migration Evaluator Collector details to the GetDiscoverySummary API response
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``workspaces-web``: [``botocore``] Amazon WorkSpaces Web now supports Administrator timeout control
* api-change:``rekognition``: [``botocore``] Documentation updates for Amazon Rekognition.
* api-change:``cloudfront``: [``botocore``] Introduced a new error (TooLongCSPInResponseHeadersPolicy) that is returned when the value of the Content-Security-Policy header in a response headers policy exceeds the maximum allowed length.


1.23.0
======

* feature:Loaders: [``botocore``] Support for loading gzip compressed model files.
* api-change:``grafana``: [``botocore``] This release adds APIs for creating and deleting API keys in an Amazon Managed Grafana workspace.


1.22.13
=======

* api-change:``ivschat``: [``botocore``] Documentation-only updates for IVS Chat API Reference.
* api-change:``lambda``: [``botocore``] Lambda releases NodeJs 16 managed runtime to be available in all commercial regions.
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Jira. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-jira.html
* api-change:``transfer``: [``botocore``] AWS Transfer Family now accepts ECDSA keys for server host keys
* api-change:``iot``: [``botocore``] Documentation update for China region ListMetricValues for IoT
* api-change:``workspaces``: [``botocore``] Increased the character limit of the login message from 600 to 850 characters.
* api-change:``finspace-data``: [``botocore``] We've now deprecated CreateSnapshot permission for creating a data view, instead use CreateDataView permission.
* api-change:``lightsail``: [``botocore``] This release adds support to include inactive database bundles in the response of the GetRelationalDatabaseBundles request.
* api-change:``outposts``: [``botocore``] Documentation updates for AWS Outposts.
* api-change:``ec2``: [``botocore``] This release introduces a target type Gateway Load Balancer Endpoint for mirrored traffic. Customers can now specify GatewayLoadBalancerEndpoint option during the creation of a traffic mirror target.
* api-change:``ssm-incidents``: [``botocore``] Adding support for dynamic SSM Runbook parameter values. Updating validation pattern for engagements. Adding ConflictException to UpdateReplicationSet API contract.


1.22.12
=======

* api-change:``secretsmanager``: [``botocore``] Doc only update for Secrets Manager that fixes several customer-reported issues.
* api-change:``ec2``: [``botocore``] This release updates AWS PrivateLink APIs to support IPv6 for PrivateLink Services and Endpoints of type 'Interface'.


1.22.11
=======

* api-change:``migration-hub-refactor-spaces``: [``botocore``] AWS Migration Hub Refactor Spaces documentation only update to fix a formatting issue.
* api-change:``ec2``: [``botocore``] Added support for using NitroTPM and UEFI Secure Boot on EC2 instances.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``compute-optimizer``: [``botocore``] Documentation updates for Compute Optimizer
* api-change:``eks``: [``botocore``] Adds BOTTLEROCKET_ARM_64_NVIDIA and BOTTLEROCKET_x86_64_NVIDIA AMI types to EKS managed nodegroups


1.22.10
=======

* api-change:``evidently``: [``botocore``] Add detail message inside GetExperimentResults API response to indicate experiment result availability
* api-change:``ssm-contacts``: [``botocore``] Fixed an error in the DescribeEngagement example for AWS Incident Manager.
* api-change:``cloudcontrol``: [``botocore``] SDK release for Cloud Control API to include paginators for Python SDK.


1.22.9
======

* api-change:``rds``: [``botocore``] Various documentation improvements.
* api-change:``redshift``: [``botocore``] Introduces new field 'LoadSampleData' in CreateCluster operation. Customers can now specify 'LoadSampleData' option during creation of a cluster, which results in loading of sample data in the cluster that is created.
* api-change:``ec2``: [``botocore``] Add new state values for IPAMs, IPAM Scopes, and IPAM Pools.
* api-change:``mediapackage``: [``botocore``] This release adds Dvb Dash 2014 as an available profile option for Dash Origin Endpoints.
* api-change:``securityhub``: [``botocore``] Documentation updates for Security Hub API reference
* api-change:``location``: [``botocore``] Amazon Location Service now includes a MaxResults parameter for ListGeofences requests.


1.22.8
======

* api-change:``ec2``: [``botocore``] Amazon EC2 I4i instances are powered by 3rd generation Intel Xeon Scalable processors and feature up to 30 TB of local AWS Nitro SSD storage
* api-change:``kendra``: [``botocore``] AWS Kendra now supports hierarchical facets for a query. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/filtering.html
* api-change:``iot``: [``botocore``] AWS IoT Jobs now allows you to create up to 100,000 active continuous and snapshot jobs by using concurrency control.
* api-change:``datasync``: [``botocore``] AWS DataSync now supports a new ObjectTags Task API option that can be used to control whether Object Tags are transferred.


1.22.7
======

* api-change:``ssm``: [``botocore``] This release adds the TargetMaps parameter in SSM State Manager API.
* api-change:``backup``: [``botocore``] Adds support to 2 new filters about job complete time for 3 list jobs APIs in AWS Backup
* api-change:``lightsail``: [``botocore``] Documentation updates for Lightsail
* api-change:``iotsecuretunneling``: [``botocore``] This release introduces a new API RotateTunnelAccessToken that allow revoking the existing tokens and generate new tokens


1.22.6
======

* api-change:``ec2``: [``botocore``] Adds support for allocating Dedicated Hosts on AWS  Outposts. The AllocateHosts API now accepts an OutpostArn request  parameter, and the DescribeHosts API now includes an OutpostArn response parameter.
* api-change:``s3``: [``botocore``] Documentation only update for doc bug fixes for the S3 API docs.
* api-change:``kinesisvideo``: [``botocore``] Add support for multiple image feature related APIs for configuring image generation and notification of a video stream. Add "GET_IMAGES" to the list of supported API names for the GetDataEndpoint API.
* api-change:``sagemaker``: [``botocore``] SageMaker Autopilot adds new metrics for all candidate models generated by Autopilot experiments; RStudio on SageMaker now allows users to bring your own development environment in a custom image.
* api-change:``kinesis-video-archived-media``: [``botocore``] Add support for GetImages API  for retrieving images from a video stream


1.22.5
======

* api-change:``organizations``: [``botocore``] This release adds the INVALID_PAYMENT_INSTRUMENT as a fail reason and an error message.
* api-change:``synthetics``: [``botocore``] CloudWatch Synthetics has introduced a new feature to provide customers with an option to delete the underlying resources that Synthetics canary creates when the user chooses to delete the canary.
* api-change:``outposts``: [``botocore``] This release adds a new API called ListAssets to the Outposts SDK, which lists the hardware assets in an Outpost.


1.22.4
======

* api-change:``rds``: [``botocore``] Feature - Adds support for Internet Protocol Version 6 (IPv6) on RDS database instances.
* api-change:``codeguru-reviewer``: [``botocore``] Amazon CodeGuru Reviewer now supports suppressing recommendations from being generated on specific files and directories.
* api-change:``ssm``: [``botocore``] Update the StartChangeRequestExecution, adding TargetMaps to the Runbook parameter
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK nows supports creation of Dolby Vision profile 8.1, the ability to generate black frames of video, and introduces audio-only DASH and CMAF support.
* api-change:``wafv2``: [``botocore``] You can now inspect all request headers and all cookies. You can now specify how to handle oversize body contents in your rules that inspect the body.


1.22.3
======

* api-change:``auditmanager``: [``botocore``] This release adds documentation updates for Audit Manager. We provided examples of how to use the Custom_ prefix for the keywordValue attribute. We also provided more details about the DeleteAssessmentReport operation.
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall adds support for stateful threat signature AWS managed rule groups.
* api-change:``ec2``: [``botocore``] This release adds support to query the public key and creation date of EC2 Key Pairs. Additionally, the format (pem or ppk) of a key pair can be specified when creating a new key pair.
* api-change:``braket``: [``botocore``] This release enables Braket Hybrid Jobs with Embedded Simulators to have multiple instances.
* api-change:``guardduty``: [``botocore``] Documentation update for API description.
* api-change:``connect``: [``botocore``] This release introduces an API for changing the current agent status of a user in Connect.


1.22.2
======

* api-change:``rekognition``: [``botocore``] This release adds support to configure stream-processor resources for label detections on streaming-videos. UpateStreamProcessor API is also launched with this release, which could be used to update an existing stream-processor.
* api-change:``cloudtrail``: [``botocore``] Increases the retention period maximum to 2557 days. Deprecates unused fields of the ListEventDataStores API response. Updates documentation.
* api-change:``lookoutequipment``: [``botocore``] This release adds the following new features: 1) Introduces an option for automatic schema creation 2) Now allows for Ingestion of data containing most common errors and allows automatic data cleaning 3) Introduces new API ListSensorStatistics that gives further information about the ingested data
* api-change:``iotwireless``: [``botocore``] Add list support for event configurations, allow to get and update event configurations by resource type, support LoRaWAN events; Make NetworkAnalyzerConfiguration as a resource, add List, Create, Delete API support; Add FCntStart attribute support for ABP WirelessDevice.
* api-change:``amplify``: [``botocore``] Documentation only update to support the Amplify GitHub App feature launch
* api-change:``chime-sdk-media-pipelines``: [``botocore``] For Amazon Chime SDK meetings, the Amazon Chime Media Pipelines SDK allows builders to capture audio, video, and content share streams. You can also capture meeting events, live transcripts, and data messages. The pipelines save the artifacts to an Amazon S3 bucket that you designate.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds support for custom validation dataset and validation ratio through the CreateAutoMLJob and DescribeAutoMLJob APIs.


1.22.1
======

* api-change:``lightsail``: [``botocore``] This release adds support for Lightsail load balancer HTTP to HTTPS redirect and TLS policy configuration.
* api-change:``sagemaker``: [``botocore``] SageMaker Inference Recommender now accepts customer KMS key ID for encryption of endpoints and compilation outputs created during inference recommendation.
* api-change:``pricing``: [``botocore``] Documentation updates for Price List API
* api-change:``glue``: [``botocore``] This release adds documentation for the APIs to create, read, delete, list, and batch read of AWS Glue custom patterns, and for Lake Formation configuration settings in the AWS Glue crawler.
* api-change:``cloudfront``: [``botocore``] CloudFront now supports the Server-Timing header in HTTP responses sent from CloudFront. You can use this header to view metrics that help you gain insights about the behavior and performance of CloudFront. To use this header, enable it in a response headers policy.
* api-change:``ivschat``: [``botocore``] Adds new APIs for IVS Chat, a feature for building interactive chat experiences alongside an IVS broadcast.
* api-change:``network-firewall``: [``botocore``] AWS Network Firewall now enables customers to use a customer managed AWS KMS key for the encryption of their firewall resources.


1.22.0
======

* api-change:``gamelift``: [``botocore``] Documentation updates for Amazon GameLift.
* api-change:``mq``: [``botocore``] This release adds the CRITICAL_ACTION_REQUIRED broker state and the ActionRequired API property. CRITICAL_ACTION_REQUIRED informs you when your broker is degraded. ActionRequired provides you with a code which you can use to find instructions in the Developer Guide on how to resolve the issue.
* feature:IMDS: [``botocore``] Added resiliency mechanisms to IMDS Credential Fetcher
* api-change:``securityhub``: [``botocore``] Security Hub now lets you opt-out of auto-enabling the defaults standards (CIS and FSBP) in accounts that are auto-enabled with Security Hub via Security Hub's integration with AWS Organizations.
* api-change:``connect``: [``botocore``] This release adds SearchUsers API which can be used to search for users with a Connect Instance
* api-change:``rds-data``: [``botocore``] Support to receive SQL query results in the form of a simplified JSON string. This enables developers using the new JSON string format to more easily convert it to an object using popular JSON string parsing libraries.


1.21.46
=======

* api-change:``chime-sdk-meetings``: [``botocore``] Include additional exceptions types.
* api-change:``ec2``: [``botocore``] Adds support for waiters that automatically poll for a deleted NAT Gateway until it reaches the deleted state.


1.21.45
=======

* api-change:``wisdom``: [``botocore``] This release updates the GetRecommendations API to include a trigger event list for classifying and grouping recommendations.
* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``iottwinmaker``: [``botocore``] General availability (GA) for AWS IoT TwinMaker. For more information, see https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/Welcome.html
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``mediatailor``: [``botocore``] This release introduces tiered channels and adds support for live sources. Customers using a STANDARD channel can now create programs using live sources.
* api-change:``storagegateway``: [``botocore``] This release adds support for minimum of 5 character length virtual tape barcodes.
* api-change:``lookoutmetrics``: [``botocore``] Added DetectMetricSetConfig API for detecting configuration required for creating metric set from provided S3 data source.
* api-change:``iotsitewise``: [``botocore``] This release adds 3 new batch data query APIs : BatchGetAssetPropertyValue, BatchGetAssetPropertyValueHistory and BatchGetAssetPropertyAggregates
* api-change:``glue``: [``botocore``] This release adds APIs to create, read, delete, list, and batch read of Glue custom entity types


1.21.44
=======

* api-change:``macie2``: [``botocore``] Sensitive data findings in Amazon Macie now indicate how Macie found the sensitive data that produced a finding (originType).
* api-change:``rds``: [``botocore``] Added a new cluster-level attribute to set the capacity range for Aurora Serverless v2 instances.
* api-change:``mgn``: [``botocore``] Removed required annotation from input fields in Describe operations requests. Added quotaValue to ServiceQuotaExceededException
* api-change:``connect``: [``botocore``] This release adds APIs to search, claim, release, list, update, and describe phone numbers. You can also use them to associate and disassociate contact flows to phone numbers.


1.21.43
=======

* api-change:``textract``: [``botocore``] This release adds support for specifying and extracting information from documents using the Queries feature within Analyze Document API
* api-change:``worklink``: [``botocore``] Amazon WorkLink is no longer supported. This will be removed in a future version of the SDK.
* api-change:``ssm``: [``botocore``] Added offset support for specifying the number of days to wait after the date and time specified by a CRON expression when creating SSM association.
* api-change:``autoscaling``: [``botocore``] EC2 Auto Scaling now adds default instance warm-up times for all scaling activities, health check replacements, and other replacement events in the Auto Scaling instance lifecycle.
* api-change:``personalize``: [``botocore``] Adding StartRecommender and StopRecommender APIs for Personalize.
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Quip. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-quip.html
* api-change:``polly``: [``botocore``] Amazon Polly adds new Austrian German voice - Hannah. Hannah is available as Neural voice only.
* api-change:``transfer``: [``botocore``] This release contains corrected HomeDirectoryMappings examples for several API functions: CreateAccess, UpdateAccess, CreateUser, and UpdateUser,.
* api-change:``kms``: [``botocore``] Adds support for KMS keys and APIs that generate and verify HMAC codes
* api-change:``redshift``: [``botocore``] Introduces new fields for LogDestinationType and LogExports on EnableLogging requests and Enable/Disable/DescribeLogging responses. Customers can now select CloudWatch Logs as a destination for their Audit Logs.


1.21.42
=======

* api-change:``lightsail``: [``botocore``] This release adds support to describe the synchronization status of the account-level block public access feature for your Amazon Lightsail buckets.
* api-change:``rds``: [``botocore``] Removes Amazon RDS on VMware with the deletion of APIs related to Custom Availability Zones and Media installation
* api-change:``athena``: [``botocore``] This release adds subfields, ErrorMessage, Retryable, to the AthenaError response object in the GetQueryExecution API when a query fails.


1.21.41
=======

* api-change:``batch``: [``botocore``] Enables configuration updates for compute environments with BEST_FIT_PROGRESSIVE and SPOT_CAPACITY_OPTIMIZED allocation strategies.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``appstream``: [``botocore``] Includes updates for create and update fleet APIs to manage the session scripts locations for Elastic fleets.
* api-change:``glue``: [``botocore``] Auto Scaling for Glue version 3.0 and later jobs to dynamically scale compute resources. This SDK change provides customers with the auto-scaled DPU usage
* api-change:``appflow``: [``botocore``] Enables users to pass custom token URL parameters for Oauth2 authentication during create connector profile


1.21.40
=======

* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``fsx``: [``botocore``] This release adds support for deploying FSx for ONTAP file systems in a single Availability Zone.


1.21.39
=======

* api-change:``ec2``: [``botocore``] X2idn and X2iedn instances are powered by 3rd generation Intel Xeon Scalable processors with an all-core turbo frequency up to 3.5 GHzAmazon EC2. C6a instances are powered by 3rd generation AMD EPYC processors.
* api-change:``devops-guru``: [``botocore``] This release adds new APIs DeleteInsight to deletes the insight along with the associated anomalies, events and recommendations.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``iottwinmaker``: [``botocore``] This release adds the following new features: 1) ListEntities API now supports search using ExternalId. 2) BatchPutPropertyValue and GetPropertyValueHistory API now allows users to represent time in sub-second level precisions.


1.21.38
=======

* api-change:``amplifyuibuilder``: [``botocore``] In this release, we have added the ability to bind events to component level actions.
* api-change:``apprunner``: [``botocore``] This release adds tracing for App Runner services with X-Ray using AWS Distro for OpenTelemetry. New APIs: CreateObservabilityConfiguration, DescribeObservabilityConfiguration, ListObservabilityConfigurations, and DeleteObservabilityConfiguration. Updated APIs: CreateService and UpdateService.
* api-change:``workspaces``: [``botocore``] Added API support that allows customers to create GPU-enabled WorkSpaces using EC2 G4dn instances.


1.21.37
=======

* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for the pass-through of WebVTT styling to WebVTT outputs, pass-through of KLV metadata to supported formats, and improved filter support for processing 444/RGB content.
* api-change:``wafv2``: [``botocore``] Add a new CurrentDefaultVersion field to ListAvailableManagedRuleGroupVersions API response; add a new VersioningSupported boolean to each ManagedRuleGroup returned from ListAvailableManagedRuleGroups API response.
* api-change:``mediapackage-vod``: [``botocore``] This release adds ScteMarkersSource as an available field for Dash Packaging Configurations. When set to MANIFEST, MediaPackage will source the SCTE-35 markers from the manifest. When set to SEGMENTS, MediaPackage will source the SCTE-35 markers from the segments.


1.21.36
=======

* api-change:``apigateway``: [``botocore``] ApiGateway CLI command get-usage now includes usagePlanId, startDate, and endDate fields in the output to match documentation.
* api-change:``personalize``: [``botocore``] This release provides tagging support in AWS Personalize.
* api-change:``pi``: [``botocore``] Adds support for DocumentDB to the Performance Insights API.
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``docdb``: [``botocore``] Added support to enable/disable performance insights when creating or modifying db instances
* api-change:``sagemaker``: [``botocore``] Amazon Sagemaker Notebook Instances now supports G5 instance types


1.21.35
=======

* bugfix:Proxy: [``botocore``] Fix failure case for IP proxy addresses using TLS-in-TLS. `boto/botocore#2652 <https://github.com/boto/botocore/pull/2652>`__
* api-change:``config``: [``botocore``] Add resourceType enums for AWS::EMR::SecurityConfiguration and AWS::SageMaker::CodeRepository
* api-change:``panorama``: [``botocore``] Added Brand field to device listings.
* api-change:``lambda``: [``botocore``] This release adds new APIs for creating and managing Lambda Function URLs and adds a new FunctionUrlAuthType parameter to the AddPermission API. Customers can use Function URLs to create built-in HTTPS endpoints on their functions.
* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Box. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-box.html


1.21.34
=======

* api-change:``securityhub``: [``botocore``] Added additional ASFF details for RdsSecurityGroup AutoScalingGroup, ElbLoadBalancer, CodeBuildProject and RedshiftCluster.
* api-change:``fsx``: [``botocore``] Provide customers more visibility into file system status by adding new "Misconfigured Unavailable" status for Amazon FSx for Windows File Server.
* api-change:``s3control``: [``botocore``] Documentation-only update for doc bug fixes for the S3 Control API docs.
* api-change:``datasync``: [``botocore``] AWS DataSync now supports Amazon FSx for OpenZFS locations.


1.21.33
=======

* api-change:``iot``: [``botocore``] AWS IoT - AWS IoT Device Defender adds support to list metric datapoints collected for IoT devices through the ListMetricValues API
* api-change:``servicecatalog``: [``botocore``] This release adds ProvisioningArtifictOutputKeys to DescribeProvisioningParameters to reference the outputs of a Provisioned Product and deprecates ProvisioningArtifactOutputs.
* api-change:``sms``: [``botocore``] Revised product update notice for SMS console deprecation.
* api-change:``proton``: [``botocore``] SDK release to support tagging for AWS Proton Repository resource
* enhancement:AWSCRT: [``botocore``] Upgrade awscrt version to 0.13.8


1.21.32
=======

* api-change:``connect``: [``botocore``] This release updates these APIs: UpdateInstanceAttribute, DescribeInstanceAttribute and ListInstanceAttributes. You can use it to programmatically enable/disable multi-party conferencing using attribute type MULTI_PARTY_CONFERENCING on the specified Amazon Connect instance.


1.21.31
=======

* api-change:``cloudcontrol``: [``botocore``] SDK release for Cloud Control API in Amazon Web Services China (Beijing) Region, operated by Sinnet, and Amazon Web Services China (Ningxia) Region, operated by NWCD
* api-change:``pinpoint-sms-voice-v2``: [``botocore``] Amazon Pinpoint now offers a version 2.0 suite of SMS and voice APIs, providing increased control over sending and configuration. This release is a new SDK for sending SMS and voice messages called PinpointSMSVoiceV2.
* api-change:``workspaces``: [``botocore``] Added APIs that allow you to customize the logo, login message, and help links in the WorkSpaces client login page. To learn more, visit https://docs.aws.amazon.com/workspaces/latest/adminguide/customize-branding.html
* api-change:``route53-recovery-cluster``: [``botocore``] This release adds a new API "ListRoutingControls" to list routing control states using the highly reliable Route 53 ARC data plane endpoints.
* api-change:``databrew``: [``botocore``] This AWS Glue Databrew release adds feature to support ORC as an input format.
* api-change:``auditmanager``: [``botocore``] This release adds documentation updates for Audit Manager. The updates provide data deletion guidance when a customer deregisters Audit Manager or deregisters a delegated administrator.
* api-change:``grafana``: [``botocore``] This release adds tagging support to the Managed Grafana service. New APIs: TagResource, UntagResource and ListTagsForResource. Updates: add optional field tags to support tagging while calling CreateWorkspace.


1.21.30
=======

* api-change:``iot-data``: [``botocore``] Update the default AWS IoT Core Data Plane endpoint from VeriSign signed to ATS signed. If you have firewalls with strict egress rules, configure the rules to grant you access to data-ats.iot.[region].amazonaws.com or data-ats.iot.[region].amazonaws.com.cn.
* api-change:``ec2``: [``botocore``] This release simplifies the auto-recovery configuration process enabling customers to set the recovery behavior to disabled or default
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports the configuration of third-party policies that can use either the centralized or distributed deployment models.
* api-change:``fsx``: [``botocore``] This release adds support for modifying throughput capacity for FSx for ONTAP file systems.
* api-change:``iot``: [``botocore``] Doc only update for IoT that fixes customer-reported issues.


1.21.29
=======

* api-change:``organizations``: [``botocore``] This release provides the new CloseAccount API that enables principals in the management account to close any member account within an organization.


1.21.28
=======

* api-change:``medialive``: [``botocore``] This release adds support for selecting a maintenance window.
* api-change:``acm-pca``: [``botocore``] Updating service name entities


1.21.27
=======

* api-change:``ec2``: [``botocore``] This is release adds support for Amazon VPC Reachability Analyzer to analyze path through a Transit Gateway.
* api-change:``ssm``: [``botocore``] This Patch Manager release supports creating, updating, and deleting Patch Baselines for Rocky Linux OS.
* api-change:``batch``: [``botocore``] Bug Fix: Fixed a bug where shapes were marked as unboxed and were not serialized and sent over the wire, causing an API error from the service.


1.21.26
=======

* api-change:``lambda``: [``botocore``] Adds support for increased ephemeral storage (/tmp) up to 10GB for Lambda functions. Customers can now provision up to 10 GB of ephemeral storage per function instance, a 20x increase over the previous limit of 512 MB.
* api-change:``config``: [``botocore``] Added new APIs GetCustomRulePolicy and GetOrganizationCustomRulePolicy, and updated existing APIs PutConfigRule, DescribeConfigRule, DescribeConfigRuleEvaluationStatus, PutOrganizationConfigRule, DescribeConfigRule to support a new feature for building AWS Config rules with AWS CloudFormation Guard
* api-change:``transcribe``: [``botocore``] This release adds an additional parameter for subtitling with Amazon Transcribe batch jobs: outputStartIndex.


1.21.25
=======

* api-change:``redshift``: [``botocore``] This release adds a new [--encrypted | --no-encrypted] field in restore-from-cluster-snapshot API. Customers can now restore an unencrypted snapshot to a cluster encrypted with AWS Managed Key or their own KMS key.
* api-change:``ebs``: [``botocore``] Increased the maximum supported value for the Timeout parameter of the StartSnapshot API from 60 minutes to 4320 minutes.  Changed the HTTP error code for ConflictException from 503 to 409.
* api-change:``gamesparks``: [``botocore``] Released the preview of Amazon GameSparks, a fully managed AWS service that provides a multi-service backend for game developers.
* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``transfer``: [``botocore``] Documentation updates for AWS Transfer Family to describe how to remove an associated workflow from a server.
* api-change:``auditmanager``: [``botocore``] This release updates 1 API parameter, the SnsArn attribute. The character length and regex pattern for the SnsArn attribute have been updated, which enables you to deselect an SNS topic when using the UpdateSettings operation.
* api-change:``ssm``: [``botocore``] Update AddTagsToResource, ListTagsForResource, and RemoveTagsFromResource APIs to reflect the support for tagging Automation resources. Includes other minor documentation updates.


1.21.24
=======

* api-change:``location``: [``botocore``] Amazon Location Service now includes a MaxResults parameter for GetDevicePositionHistory requests.
* api-change:``polly``: [``botocore``] Amazon Polly adds new Catalan voice - Arlet. Arlet is available as Neural voice only.
* api-change:``lakeformation``: [``botocore``] The release fixes the incorrect permissions called out in the documentation - DESCRIBE_TAG, ASSOCIATE_TAG, DELETE_TAG, ALTER_TAG. This trebuchet release fixes the corresponding SDK and documentation.
* api-change:``ecs``: [``botocore``] Documentation only update to address tickets
* api-change:``ce``: [``botocore``] Added three new APIs to support tagging and resource-level authorization on Cost Explorer resources: TagResource, UntagResource, ListTagsForResource.  Added optional parameters to CreateCostCategoryDefinition, CreateAnomalySubscription and CreateAnomalyMonitor APIs to support Tag On Create.


1.21.23
=======

* api-change:``ram``: [``botocore``] Document improvements to the RAM API operations and parameter descriptions.
* api-change:``ecr``: [``botocore``] This release includes a fix in the DescribeImageScanFindings paginated output.
* api-change:``quicksight``: [``botocore``] AWS QuickSight Service Features - Expand public API support for group management.
* api-change:``chime-sdk-meetings``: [``botocore``] Add support for media replication to link multiple WebRTC media sessions together to reach larger and global audiences. Participants connected to a replica session can be granted access to join the primary session and can switch sessions with their existing WebRTC connection
* api-change:``mediaconnect``: [``botocore``] This release adds support for selecting a maintenance window.


1.21.22
=======

* enhancement:jmespath: [``botocore``] Add env markers to get working version of jmespath for python 3.6
* api-change:``glue``: [``botocore``] Added 9 new APIs for AWS Glue Interactive Sessions: ListSessions, StopSession, CreateSession, GetSession, DeleteSession, RunStatement, GetStatement, ListStatements, CancelStatement


1.21.21
=======

* enhancement:Dependency: [``botocore``] Added support for jmespath 1.0
* api-change:``amplifybackend``: [``botocore``] Adding the ability to customize Cognito verification messages for email and SMS in CreateBackendAuth and UpdateBackendAuth. Adding deprecation documentation for ForgotPassword in CreateBackendAuth and UpdateBackendAuth
* api-change:``acm-pca``: [``botocore``] AWS Certificate Manager (ACM) Private Certificate Authority (CA) now supports customizable certificate subject names and extensions.
* api-change:``ssm-incidents``: [``botocore``] Removed incorrect validation pattern for IncidentRecordSource.invokedBy
* enhancement:Dependency: Added support for jmespath 1.0
* api-change:``billingconductor``: [``botocore``] This is the initial SDK release for AWS Billing Conductor. The AWS Billing Conductor is a customizable billing service, allowing you to customize your billing data to match your desired business structure.
* api-change:``s3outposts``: [``botocore``] S3 on Outposts is releasing a new API, ListSharedEndpoints, that lists all endpoints associated with S3 on Outpost, that has been shared by Resource Access Manager (RAM).


1.21.20
=======

* api-change:``robomaker``: [``botocore``] This release deprecates ROS, Ubuntu and Gazbeo from RoboMaker Simulation Service Software Suites in favor of user-supplied containers and Relaxed Software Suites.
* api-change:``dataexchange``: [``botocore``] This feature enables data providers to use the RevokeRevision operation to revoke subscriber access to a given revision. Subscribers are unable to interact with assets within a revoked revision.
* api-change:``ec2``: [``botocore``] Adds the Cascade parameter to the DeleteIpam API. Customers can use this parameter to automatically delete their IPAM, including non-default scopes, pools, cidrs, and allocations. There mustn't be any pools provisioned in the default public scope to use this parameter.
* api-change:``cognito-idp``: [``botocore``] Updated EmailConfigurationType and SmsConfigurationType to reflect that you can now choose Amazon SES and Amazon SNS resources in the same Region.
* enhancement:AWSCRT: [``botocore``] Upgrade awscrt extra to 0.13.5
* api-change:``location``: [``botocore``] New HERE style "VectorHereExplore" and "VectorHereExploreTruck".
* api-change:``ecs``: [``botocore``] Documentation only update to address tickets
* api-change:``keyspaces``: [``botocore``] Fixing formatting issues in CLI and SDK documentation
* api-change:``rds``: [``botocore``] Various documentation improvements


1.21.19
=======

* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Slack. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html
* api-change:``timestream-query``: [``botocore``] Amazon Timestream Scheduled Queries now support Timestamp datatype in a multi-measure record.
* enhancement:Stubber: [``botocore``] Added support for modeled exception fields when adding errors to a client stub. Implements boto/boto3`#3178 <https://github.com/boto/botocore/issues/3178>`__.
* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``config``: [``botocore``] Add resourceType enums for AWS::ECR::PublicRepository and AWS::EC2::LaunchTemplate


1.21.18
=======

* api-change:``outposts``: [``botocore``] This release adds address filters for listSites
* api-change:``lambda``: [``botocore``] Adds PrincipalOrgID support to AddPermission API. Customers can use it to manage permissions to lambda functions at AWS Organizations level.
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager.
* api-change:``connect``: [``botocore``] This release adds support for enabling Rich Messaging when starting a new chat session via the StartChatContact API. Rich Messaging enables the following formatting options: bold, italics, hyperlinks, bulleted lists, and numbered lists.
* api-change:``chime``: [``botocore``] Chime VoiceConnector Logging APIs will now support MediaMetricLogs. Also CreateMeetingDialOut now returns AccessDeniedException.


1.21.17
=======

* api-change:``transcribe``: [``botocore``] Documentation fix for API `StartMedicalTranscriptionJobRequest`, now showing min sample rate as 16khz
* api-change:``transfer``: [``botocore``] Adding more descriptive error types for managed workflows
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version


1.21.16
=======

* api-change:``comprehend``: [``botocore``] Amazon Comprehend now supports extracting the sentiment associated with entities such as brands, products and services from text documents.


1.21.15
=======

* api-change:``eks``: [``botocore``] Introducing a new enum for NodeGroup error code: Ec2SubnetMissingIpv6Assignment
* api-change:``keyspaces``: [``botocore``] Adding link to CloudTrail section in Amazon Keyspaces Developer Guide
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for reading timecode from AVCHD sources and now provides the ability to segment WebVTT at the same interval as the video and audio in HLS packages.


1.21.14
=======

* api-change:``chime-sdk-meetings``: [``botocore``] Adds support for Transcribe language identification feature to the StartMeetingTranscription API.
* api-change:``ecs``: [``botocore``] Amazon ECS UpdateService API now supports additional parameters: loadBalancers, propagateTags, enableECSManagedTags, and serviceRegistries
* api-change:``migration-hub-refactor-spaces``: [``botocore``] AWS Migration Hub Refactor Spaces documentation update.


1.21.13
=======

* api-change:``synthetics``: [``botocore``] Allow custom handler function.
* api-change:``transfer``: [``botocore``] Add waiters for server online and offline.
* api-change:``devops-guru``: [``botocore``] Amazon DevOps Guru now integrates with Amazon CodeGuru Profiler. You can view CodeGuru Profiler recommendations for your AWS Lambda function in DevOps Guru. This feature is enabled by default for new customers as of 3/4/2022. Existing customers can enable this feature with UpdateEventSourcesConfig.
* api-change:``macie``: [``botocore``] Amazon Macie Classic (macie) has been discontinued and is no longer available. A new Amazon Macie (macie2) is now available with significant design improvements and additional features.
* api-change:``ec2``: [``botocore``] Documentation updates for Amazon EC2.
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``connect``: [``botocore``] This release updates the *InstanceStorageConfig APIs so they support a new ResourceType: REAL_TIME_CONTACT_ANALYSIS_SEGMENTS. Use this resource type to enable streaming for real-time contact analysis and to associate the Kinesis stream where real-time contact analysis segments will be published.


1.21.12
=======

* api-change:``greengrassv2``: [``botocore``] Doc only update that clarifies Create Deployment section.
* api-change:``fsx``: [``botocore``] This release adds support for data repository associations to use root ("/") as the file system path
* api-change:``kendra``: [``botocore``] Amazon Kendra now suggests spell corrections for a query. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/query-spell-check.html
* api-change:``appflow``: [``botocore``] Launching Amazon AppFlow Marketo as a destination connector SDK.
* api-change:``timestream-query``: [``botocore``] Documentation only update for SDK and CLI


1.21.11
=======

* api-change:``gamelift``: [``botocore``] Minor updates to address errors.
* api-change:``cloudtrail``: [``botocore``] Add bytesScanned field into responses of DescribeQuery and GetQueryResults.
* api-change:``athena``: [``botocore``] This release adds support for S3 Object Ownership by allowing the S3 bucket owner full control canned ACL to be set when Athena writes query results to S3 buckets.
* api-change:``keyspaces``: [``botocore``] This release adds support for data definition language (DDL) operations
* api-change:``ecr``: [``botocore``] This release adds support for tracking images lastRecordedPullTime.


1.21.10
=======

* api-change:``mediapackage``: [``botocore``] This release adds Hybridcast as an available profile option for Dash Origin Endpoints.
* api-change:``rds``: [``botocore``] Documentation updates for Multi-AZ DB clusters.
* api-change:``mgn``: [``botocore``] Add support for GP3 and IO2 volume types. Add bootMode to LaunchConfiguration object (and as a parameter to UpdateLaunchConfigurationRequest).
* api-change:``kafkaconnect``: [``botocore``] Adds operation for custom plugin deletion (DeleteCustomPlugin) and adds new StateDescription field to DescribeCustomPlugin and DescribeConnector responses to return errors from asynchronous resource creation.


1.21.9
======

* api-change:``finspace-data``: [``botocore``] Add new APIs for managing Users and Permission Groups.
* api-change:``amplify``: [``botocore``] Add repositoryCloneMethod field for hosting an Amplify app. This field shows what authorization method is used to clone the repo: SSH, TOKEN, or SIGV4.
* api-change:``fsx``: [``botocore``] This release adds support for the following FSx for OpenZFS features: snapshot lifecycle transition messages, force flag for deleting file systems with child resources, LZ4 data compression, custom record sizes, and unsetting volume quotas and reservations.
* api-change:``fis``: [``botocore``] This release adds logging support for AWS Fault Injection Simulator experiments. Experiment templates can now be configured to send experiment activity logs to Amazon CloudWatch Logs or to an S3 bucket.
* api-change:``route53-recovery-cluster``: [``botocore``] This release adds a new API option to enable overriding safety rules to allow routing control state updates.
* api-change:``amplifyuibuilder``: [``botocore``] We are adding the ability to configure workflows and actions for components.
* api-change:``athena``: [``botocore``] This release adds support for updating an existing named query.
* api-change:``ec2``: [``botocore``] This release adds support for new AMI property 'lastLaunchedTime'
* api-change:``servicecatalog-appregistry``: [``botocore``] AppRegistry is deprecating Application and Attribute-Group Name update feature. In this release, we are marking the name attributes for Update APIs as deprecated to give a heads up to our customers.


1.21.8
======

* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``panorama``: [``botocore``] Added NTP server configuration parameter to ProvisionDevice operation. Added alternate software fields to DescribeDevice response


1.21.7
======

* api-change:``route53``: [``botocore``] SDK doc update for Route 53 to update some parameters with new information.
* api-change:``databrew``: [``botocore``] This AWS Glue Databrew release adds feature to merge job outputs into a max number of files for S3 File output type.
* api-change:``transfer``: [``botocore``] Support automatic pagination when listing AWS Transfer Family resources.
* api-change:``s3control``: [``botocore``] Amazon S3 Batch Operations adds support for new integrity checking capabilities in Amazon S3.
* api-change:``s3``: [``botocore``] This release adds support for new integrity checking capabilities in Amazon S3. You can choose from four supported checksum algorithms for data integrity checking on your upload and download requests. In addition, AWS SDK can automatically calculate a checksum as it streams data into S3
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports the configuration of AWS Network Firewall policies with either centralized or distributed deployment models. This release also adds support for custom endpoint configuration, where you can choose which Availability Zones to create firewall endpoints in.
* api-change:``lightsail``: [``botocore``] This release adds support to delete and create Lightsail default key pairs that you can use with Lightsail instances.
* api-change:``autoscaling``: [``botocore``] You can now hibernate instances in a warm pool to stop instances without deleting their RAM contents. You can now also return instances to the warm pool on scale in, instead of always terminating capacity that you will need later.


1.21.6
======

* api-change:``transfer``: [``botocore``] The file input selection feature provides the ability to use either the originally uploaded file or the output file from the previous workflow step, enabling customers to make multiple copies of the original file while keeping the source file intact for file archival.
* api-change:``lambda``: [``botocore``] Lambda releases .NET 6 managed runtime to be available in all commercial regions.
* api-change:``textract``: [``botocore``] Added support for merged cells and column header for table response.


1.21.5
======

* api-change:``translate``: [``botocore``] This release enables customers to use translation settings for formality customization in their synchronous translation output.
* api-change:``wafv2``: [``botocore``] Updated descriptions for logging configuration.
* api-change:``apprunner``: [``botocore``] AWS App Runner adds a Java platform (Corretto 8, Corretto 11 runtimes) and a Node.js 14 runtime.


1.21.4
======

* api-change:``imagebuilder``: [``botocore``] This release adds support to enable faster launching for Windows AMIs created by EC2 Image Builder.
* api-change:``customer-profiles``: [``botocore``] This release introduces apis CreateIntegrationWorkflow, DeleteWorkflow, ListWorkflows, GetWorkflow and GetWorkflowSteps. These apis are used to manage and view integration workflows.
* api-change:``dynamodb``: [``botocore``] DynamoDB ExecuteStatement API now supports Limit as a request parameter to specify the maximum number of items to evaluate. If specified, the service will process up to the Limit and the results will include a LastEvaluatedKey value to continue the read in a subsequent operation.


1.21.3
======

* api-change:``transfer``: [``botocore``] Properties for Transfer Family used with SFTP, FTP, and FTPS protocols. Display Banners are bodies of text that can be displayed before and/or after a user authenticates onto a server using one of the previously mentioned protocols.
* api-change:``gamelift``: [``botocore``] Increase string list limit from 10 to 100.
* api-change:``budgets``: [``botocore``] This change introduces DescribeBudgetNotificationsForAccount API which returns budget notifications for the specified account


1.21.2
======

* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``redshift``: [``botocore``] SDK release for Cross region datasharing and cost-control for cross region datasharing
* api-change:``evidently``: [``botocore``] Add support for filtering list of experiments and launches by status
* api-change:``backup``: [``botocore``] AWS Backup add new S3_BACKUP_OBJECT_FAILED and S3_RESTORE_OBJECT_FAILED event types in BackupVaultNotifications events list.


1.21.1
======

* api-change:``ec2``: [``botocore``] Documentation updates for EC2.
* api-change:``budgets``: [``botocore``] Adds support for auto-adjusting budgets, a new budget method alongside fixed and planned. Auto-adjusting budgets introduces new metadata to configure a budget limit baseline using a historical lookback average or current period forecast.
* api-change:``ce``: [``botocore``] AWS Cost Anomaly Detection now supports SNS FIFO topic subscribers.
* api-change:``glue``: [``botocore``] Support for optimistic locking in UpdateTable
* api-change:``ssm``: [``botocore``] Assorted ticket fixes and updates for AWS Systems Manager.


1.21.0
======

* api-change:``appflow``: [``botocore``] Launching Amazon AppFlow SAP as a destination connector SDK.
* feature:Parser: [``botocore``] Adding support for parsing int/long types in rest-json response headers.
* api-change:``rds``: [``botocore``] Adds support for determining which Aurora PostgreSQL versions support Babelfish.
* api-change:``athena``: [``botocore``] This release adds a subfield, ErrorType, to the AthenaError response object in the GetQueryExecution API when a query fails.


1.20.54
=======

* api-change:``ssm``: [``botocore``] Documentation updates for AWS Systems Manager.


1.20.53
=======

* api-change:``cloudformation``: [``botocore``] This SDK release adds AWS CloudFormation Hooks HandlerErrorCodes
* api-change:``lookoutvision``: [``botocore``] This release makes CompilerOptions in Lookout for Vision's StartModelPackagingJob's Configuration object optional.
* api-change:``pinpoint``: [``botocore``] This SDK release adds a new paramater creation date for GetApp and GetApps Api call
* api-change:``sns``: [``botocore``] Customer requested typo fix in API documentation.
* api-change:``wafv2``: [``botocore``] Adds support for AWS WAF Fraud Control account takeover prevention (ATP), with configuration options for the new managed rule group AWSManagedRulesATPRuleSet and support for application integration SDKs for Android and iOS mobile apps.


1.20.52
=======

* api-change:``cloudformation``: [``botocore``] This SDK release is for the feature launch of AWS CloudFormation Hooks.


1.20.51
=======

* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Amazon FSx. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-fsx.html
* api-change:``apprunner``: [``botocore``] This release adds support for App Runner to route outbound network traffic of a service through an Amazon VPC. New API: CreateVpcConnector, DescribeVpcConnector, ListVpcConnectors, and DeleteVpcConnector. Updated API: CreateService, DescribeService, and UpdateService.
* api-change:``s3control``: [``botocore``] This release adds support for S3 Batch Replication. Batch Replication lets you replicate existing objects, already replicated objects to new destinations, and objects that previously failed to replicate. Customers will receive object-level visibility of progress and a detailed completion report.
* api-change:``sagemaker``: [``botocore``] Autopilot now generates an additional report with information on the performance of the best model, such as a Confusion matrix and  Area under the receiver operating characteristic (AUC-ROC). The path to the report can be found in CandidateArtifactLocations.


1.20.50
=======

* api-change:``auditmanager``: [``botocore``] This release updates 3 API parameters. UpdateAssessmentFrameworkControlSet now requires the controls attribute, and CreateAssessmentFrameworkControl requires the id attribute. Additionally, UpdateAssessmentFramework now has a minimum length constraint for the controlSets attribute.
* api-change:``synthetics``: [``botocore``] Adding names parameters to the Describe APIs.
* api-change:``ssm-incidents``: [``botocore``] Update RelatedItem enum to support SSM Automation
* api-change:``events``: [``botocore``] Update events client to latest version
* enhancement:Lambda Request Header: [``botocore``] Adding request header for Lambda recursion detection.


1.20.49
=======

* api-change:``athena``: [``botocore``] You can now optionally specify the account ID that you expect to be the owner of your query results output location bucket in Athena. If the account ID of the query results bucket owner does not match the specified account ID, attempts to output to the bucket will fail with an S3 permissions error.
* api-change:``rds``: [``botocore``] updates for RDS Custom for Oracle 12.1 support
* api-change:``lakeformation``: [``botocore``] Add support for calling Update Table Objects without a TransactionId.


1.20.48
=======

* api-change:``ec2``: [``botocore``] adds support for AMIs in Recycle Bin
* api-change:``robomaker``: [``botocore``] The release deprecates the use various APIs of RoboMaker Deployment Service in favor of AWS IoT GreenGrass v2.0.
* api-change:``meteringmarketplace``: [``botocore``] Add CustomerAWSAccountId to ResolveCustomer API response and increase UsageAllocation limit to 2500.
* api-change:``rbin``: [``botocore``] Add EC2 Image recycle bin support.


1.20.47
=======

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``personalize``: [``botocore``] Adding minRecommendationRequestsPerSecond attribute to recommender APIs.
* enhancement:Request headers: [``botocore``] Adding request headers with retry information.
* api-change:``appflow``: [``botocore``] Launching Amazon AppFlow Custom Connector SDK.
* api-change:``dynamodb``: [``botocore``] Documentation update for DynamoDB Java SDK.
* api-change:``iot``: [``botocore``] This release adds support for configuring AWS IoT logging level per client ID, source IP, or principal ID.
* api-change:``comprehend``: [``botocore``] Amazon Comprehend now supports sharing and importing custom trained models from one AWS account to another within the same region.
* api-change:``ce``: [``botocore``] Doc-only update for Cost Explorer API that adds INVOICING_ENTITY dimensions
* api-change:``fis``: [``botocore``] Added GetTargetResourceType and ListTargetResourceTypesAPI actions. These actions return additional details about resource types and parameters that can be targeted by FIS actions. Added a parameters field for the targets that can be specified in experiment templates.
* api-change:``es``: [``botocore``] Allows customers to get progress updates for blue/green deployments
* api-change:``glue``: [``botocore``] Launch Protobuf support for AWS Glue Schema Registry
* api-change:``elasticache``: [``botocore``] Documentation update for AWS ElastiCache


1.20.46
=======

* api-change:``appconfigdata``: [``botocore``] Documentation updates for AWS AppConfig Data.
* api-change:``athena``: [``botocore``] This release adds a field, AthenaError, to the GetQueryExecution response object when a query fails.
* api-change:``appconfig``: [``botocore``] Documentation updates for AWS AppConfig
* api-change:``cognito-idp``: [``botocore``] Doc updates for Cognito user pools API Reference.
* api-change:``secretsmanager``: [``botocore``] Feature are ready to release on Jan 28th
* api-change:``sagemaker``: [``botocore``] This release added a new NNA accelerator compilation support for Sagemaker Neo.


1.20.45
=======

* api-change:``ec2``: [``botocore``] X2ezn instances are powered by Intel Cascade Lake CPUs that deliver turbo all core frequency of up to 4.5 GHz and up to 100 Gbps of networking bandwidth
* api-change:``kafka``: [``botocore``] Amazon MSK has updated the CreateCluster and UpdateBrokerStorage API that allows you to specify volume throughput during cluster creation and broker volume updates.
* api-change:``connect``: [``botocore``] This release adds support for configuring a custom chat duration when starting a new chat session via the StartChatContact API. The default value for chat duration is 25 hours, minimum configurable value is 1 hour (60 minutes) and maximum configurable value is 7 days (10,080 minutes).
* api-change:``amplify``: [``botocore``] Doc only update to the description of basicauthcredentials to describe the required encoding and format.
* api-change:``opensearch``: [``botocore``] Allows customers to get progress updates for blue/green deployments


1.20.44
=======

* api-change:``frauddetector``: [``botocore``] Added new APIs for viewing past predictions and obtaining prediction metadata including prediction explanations: ListEventPredictions and GetEventPredictionMetadata
* api-change:``ebs``: [``botocore``] Documentation updates for Amazon EBS Direct APIs.
* api-change:``codeguru-reviewer``: [``botocore``] Added failure state and adjusted timeout in waiter
* api-change:``securityhub``: [``botocore``] Adding top level Sample boolean field
* api-change:``sagemaker``: [``botocore``] API changes relating to Fail steps in model building pipeline and add PipelineExecutionFailureReason in PipelineExecutionSummary.


1.20.43
=======

* api-change:``fsx``: [``botocore``] This release adds support for growing SSD storage capacity and growing/shrinking SSD IOPS for FSx for ONTAP file systems.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``connect``: [``botocore``] This release adds support for custom vocabularies to be used with Contact Lens. Custom vocabularies improve transcription accuracy for one or more specific words.
* api-change:``guardduty``: [``botocore``] Amazon GuardDuty expands threat detection coverage to protect Amazon Elastic Kubernetes Service (EKS) workloads.


1.20.42
=======

* api-change:``route53-recovery-readiness``: [``botocore``] Updated documentation for Route53 Recovery Readiness APIs.


1.20.41
=======

* enhancement:Exceptions: [``botocore``] ProxyConnectionError previously provided the full proxy URL. User info will now be appropriately masked if needed.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for 4K AV1 output resolutions & 10-bit AV1 color, the ability to ingest sidecar Dolby Vision XML metadata files, and the ability to flag WebVTT and IMSC tracks for accessibility in HLS.
* api-change:``transcribe``: [``botocore``] Add support for granular PIIEntityTypes when using Batch ContentRedaction.


1.20.40
=======

* api-change:``guardduty``: [``botocore``] Amazon GuardDuty findings now include remoteAccountDetails under AwsApiCallAction section if instance credential is exfiltrated.
* api-change:``connect``: [``botocore``] This release adds tagging support for UserHierarchyGroups resource.
* api-change:``mediatailor``: [``botocore``] This release adds support for multiple Segment Delivery Configurations. Users can provide a list of names and URLs when creating or editing a source location. When retrieving content, users can send a header to choose which URL should be used to serve content.
* api-change:``fis``: [``botocore``] Added action startTime and action endTime timestamp fields to the ExperimentAction object
* api-change:``ec2``: [``botocore``] C6i, M6i and R6i instances are powered by a third-generation Intel Xeon Scalable processor (Ice Lake) delivering all-core turbo frequency of 3.5 GHz


1.20.39
=======

* api-change:``macie2``: [``botocore``] This release of the Amazon Macie API introduces stricter validation of requests to create custom data identifiers.
* api-change:``ec2-instance-connect``: [``botocore``] Adds support for ED25519 keys. PushSSHPublicKey Availability Zone parameter is now optional. Adds EC2InstanceStateInvalidException for instances that are not running. This was previously a service exception, so this may require updating your code to handle this new exception.


1.20.38
=======

* api-change:``ivs``: [``botocore``] This release adds support for the new Thumbnail Configuration property for Recording Configurations. For more information see https://docs.aws.amazon.com/ivs/latest/userguide/record-to-s3.html
* api-change:``storagegateway``: [``botocore``] Documentation update for adding bandwidth throttling support for S3 File Gateways.
* api-change:``location``: [``botocore``] This release adds the CalculateRouteMatrix API which calculates routes for the provided departure and destination positions. The release also deprecates the use of pricing plan across all verticals.
* api-change:``cloudtrail``: [``botocore``] This release fixes a documentation bug in the description for the readOnly field selector in advanced event selectors. The description now clarifies that users omit the readOnly field selector to select both Read and Write management events.
* api-change:``ec2``: [``botocore``] Add support for AWS Client VPN client login banner and session timeout.


1.20.37
=======

* enhancement:Configuration: [``botocore``] Adding support for `defaults_mode` configuration. The `defaults_mode` will be used to determine how certain default configuration options are resolved in the SDK.


1.20.36
=======

* api-change:``config``: [``botocore``] Update ResourceType enum with values for CodeDeploy, EC2 and Kinesis resources
* api-change:``application-insights``: [``botocore``] Application Insights support for Active Directory and SharePoint
* api-change:``honeycode``: [``botocore``] Added read and write api support for multi-select picklist. And added errorcode field to DescribeTableDataImportJob API output, when import job fails.
* api-change:``ram``: [``botocore``] This release adds the ListPermissionVersions API which lists the versions for a given permission.
* api-change:``lookoutmetrics``: [``botocore``] This release adds a new DeactivateAnomalyDetector API operation.


1.20.35
=======

* api-change:``pinpoint``: [``botocore``] Adds JourneyChannelSettings to WriteJourneyRequest
* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio now supports validation for Launch Profiles. Launch Profiles now report static validation results after create/update to detect errors in network or active directory configuration.
* api-change:``glue``: [``botocore``] This SDK release adds support to pass run properties when starting a workflow run
* api-change:``ssm``: [``botocore``] AWS Systems Manager adds category support for DescribeDocument API
* api-change:``elasticache``: [``botocore``] AWS ElastiCache for Redis has added a new Engine Log LogType in LogDelivery feature. You can now publish the Engine Log from your Amazon ElastiCache for Redis clusters to Amazon CloudWatch Logs and Amazon Kinesis Data Firehose.


1.20.34
=======

* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``honeycode``: [``botocore``] Honeycode is releasing new APIs to allow user to create, delete and list tags on resources.
* api-change:``ec2``: [``botocore``] Hpc6a instances are powered by a third-generation AMD EPYC processors (Milan) delivering all-core turbo frequency of 3.4 GHz
* api-change:``fms``: [``botocore``] Shield Advanced policies for Amazon CloudFront resources now support automatic application layer DDoS mitigation. The max length for SecurityServicePolicyData ManagedServiceData is now 8192 characters, instead of 4096.
* api-change:``pi``: [``botocore``] This release adds three Performance Insights APIs. Use ListAvailableResourceMetrics to get available metrics, GetResourceMetadata to get feature metadata, and ListAvailableResourceDimensions to list available dimensions. The AdditionalMetrics field in DescribeDimensionKeys retrieves per-SQL metrics.


1.20.33
=======

* api-change:``finspace-data``: [``botocore``] Documentation updates for FinSpace.
* api-change:``rds``: [``botocore``] This release adds the db-proxy event type to support subscribing to RDS Proxy events.
* api-change:``ce``: [``botocore``] Doc only update for Cost Explorer API that fixes missing clarifications for MatchOptions definitions
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports advanced query language and query-less search.
* api-change:``workspaces``: [``botocore``] Introducing new APIs for Workspaces audio optimization with Amazon Connect: CreateConnectClientAddIn, DescribeConnectClientAddIns, UpdateConnectClientAddIn and DeleteConnectClientAddIn.
* api-change:``iotevents-data``: [``botocore``] This release provides documentation updates for Timer.timestamp in the IoT Events API Reference Guide.
* api-change:``ec2``: [``botocore``] EC2 Capacity Reservations now supports RHEL instance platforms (RHEL with SQL Server Standard, RHEL with SQL Server Enterprise, RHEL with SQL Server Web, RHEL with HA, RHEL with HA and SQL Server Standard, RHEL with HA and SQL Server Enterprise)


1.20.32
=======

* api-change:``ec2``: [``botocore``] New feature: Updated EC2 API to support faster launching for Windows images. Optimized images are pre-provisioned, using snapshots to launch instances up to 65% faster.
* api-change:``compute-optimizer``: [``botocore``] Adds support for new Compute Optimizer capability that makes it easier for customers to optimize their EC2 instances by leveraging multiple CPU architectures.
* api-change:``lookoutmetrics``: [``botocore``] This release adds FailureType in the response of DescribeAnomalyDetector.
* api-change:``databrew``: [``botocore``] This SDK release adds support for specifying a Bucket Owner for an S3 location.
* api-change:``transcribe``: [``botocore``] Documentation updates for Amazon Transcribe.


1.20.31
=======

* api-change:``medialive``: [``botocore``] This release adds support for selecting the Program Date Time (PDT) Clock source algorithm for HLS outputs.


1.20.30
=======

* api-change:``ec2``: [``botocore``] This release introduces On-Demand Capacity Reservation support for Cluster Placement Groups, adds Tags on instance Metadata, and includes documentation updates for Amazon EC2.
* api-change:``mediatailor``: [``botocore``] This release adds support for filler slate when updating MediaTailor channels that use the linear playback mode.
* api-change:``opensearch``: [``botocore``] Amazon OpenSearch Service adds support for Fine Grained Access Control for existing domains running Elasticsearch version 6.7 and above
* api-change:``iotwireless``: [``botocore``] Downlink Queue Management feature provides APIs for customers to manage the queued messages destined to device inside AWS IoT Core for LoRaWAN. Customer can view, delete or purge the queued message(s). It allows customer to preempt the queued messages and let more urgent messages go through.
* api-change:``es``: [``botocore``] Amazon OpenSearch Service adds support for Fine Grained Access Control for existing domains running Elasticsearch version 6.7 and above
* api-change:``mwaa``: [``botocore``] This release adds a "Source" field that provides the initiator of an update, such as due to an automated patch from AWS or due to modification via Console or API.
* api-change:``appsync``: [``botocore``] AppSync: AWS AppSync now supports configurable batching sizes for AWS Lambda resolvers, Direct AWS Lambda resolvers and pipeline functions


1.20.29
=======

* api-change:``cloudtrail``: [``botocore``] This release adds support for CloudTrail Lake, a new feature that lets you run SQL-based queries on events that you have aggregated into event data stores. New APIs have been added for creating and managing event data stores, and creating, running, and managing queries in CloudTrail Lake.
* api-change:``iot``: [``botocore``] This release adds an automatic retry mechanism for AWS IoT Jobs. You can now define a maximum number of retries for each Job rollout, along with the criteria to trigger the retry for FAILED/TIMED_OUT/ALL(both FAILED an TIMED_OUT) job.
* api-change:``ec2``: [``botocore``] This release adds a new API called ModifyVpcEndpointServicePayerResponsibility which allows VPC endpoint service owners to take payer responsibility of their VPC Endpoint connections.
* api-change:``snowball``: [``botocore``] Updating validation rules for interfaces used in the Snowball API to tighten security of service.
* api-change:``lakeformation``: [``botocore``] Add new APIs for 3rd Party Support for Lake Formation
* api-change:``appstream``: [``botocore``] Includes APIs for App Entitlement management regarding entitlement and entitled application association.
* api-change:``eks``: [``botocore``] Amazon EKS now supports running applications using IPv6 address space
* api-change:``quicksight``: [``botocore``] Multiple Doc-only updates for Amazon QuickSight.
* api-change:``ecs``: [``botocore``] Documentation update for ticket fixes.
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker now supports running training jobs on ml.g5 instance types.
* api-change:``glue``: [``botocore``] Add Delta Lake target support for Glue Crawler and 3rd Party Support for Lake Formation


1.20.28
=======

* api-change:``rekognition``: [``botocore``] This release introduces a new field IndexFacesModelVersion, which is the version of the face detect and storage model that was used when indexing the face vector.
* api-change:``s3``: [``botocore``] Minor doc-based updates based on feedback bugs received.
* enhancement:JSONFileCache: [``botocore``] Add support for __delitem__ in JSONFileCache
* api-change:``s3control``: [``botocore``] Documentation updates for the renaming of Glacier to Glacier Flexible Retrieval.


1.20.27
=======

* api-change:``sagemaker``: [``botocore``] The release allows users to pass pipeline definitions as Amazon S3 locations and control the pipeline execution concurrency using ParallelismConfiguration. It also adds support of EMR jobs as pipeline steps.
* api-change:``rds``: [``botocore``] Multiple doc-only updates for Relational Database Service (RDS)
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added strength levels to the Sharpness Filter and now permits OGG files to be specified as sidecar audio inputs.
* api-change:``greengrassv2``: [``botocore``] This release adds the API operations to manage the Greengrass role associated with your account and to manage the core device connectivity information. Greengrass V2 customers can now depend solely on Greengrass V2 SDK for all the API operations needed to manage their fleets.
* api-change:``detective``: [``botocore``] Added and updated API operations to support the Detective integration with AWS Organizations. New actions are used to manage the delegated administrator account and the integration configuration.


1.20.26
=======

* api-change:``nimble``: [``botocore``] Amazon Nimble Studio adds support for users to upload files during a streaming session using NICE DCV native client or browser.
* api-change:``chime-sdk-messaging``: [``botocore``] The Amazon Chime SDK now supports updating message attributes via channel flows
* api-change:``imagebuilder``: [``botocore``] Added a note to infrastructure configuration actions and data types concerning delivery of Image Builder event messages to encrypted SNS topics. The key that's used to encrypt the SNS topic must reside in the account that Image Builder runs under.
* api-change:``workmail``: [``botocore``] This release allows customers to change their email monitoring configuration in Amazon WorkMail.
* api-change:``transfer``: [``botocore``] Property for Transfer Family used with the FTPS protocol. TLS Session Resumption provides a mechanism to resume or share a negotiated secret key between the control and data connection for an FTPS session.
* api-change:``lookoutmetrics``: [``botocore``] This release adds support for Causal Relationships. Added new ListAnomalyGroupRelatedMetrics API operation and InterMetricImpactDetails API data type
* api-change:``mediaconnect``: [``botocore``] You can now use the Fujitsu-QoS protocol for your MediaConnect sources and outputs to transport content to and from Fujitsu devices.
* api-change:``qldb``: [``botocore``] Amazon QLDB now supports journal exports in JSON and Ion Binary formats. This release adds an optional OutputFormat parameter to the ExportJournalToS3 API.


1.20.25
=======

* api-change:``customer-profiles``: [``botocore``] This release adds an optional parameter, ObjectTypeNames to the PutIntegration API to support multiple object types per integration option. Besides, this release introduces Standard Order Objects which contain data from third party systems and each order object belongs to a specific profile.
* api-change:``sagemaker``: [``botocore``] This release adds a new ContentType field in AutoMLChannel for SageMaker CreateAutoMLJob InputDataConfig.
* api-change:``forecast``: [``botocore``] Adds ForecastDimensions field to the DescribeAutoPredictorResponse
* api-change:``securityhub``: [``botocore``] Added new resource details objects to ASFF, including resources for Firewall, and RuleGroup, FirewallPolicy Added additional details for AutoScalingGroup, LaunchConfiguration, and S3 buckets.
* api-change:``location``: [``botocore``] Making PricingPlan optional as part of create resource API.
* api-change:``redshift``: [``botocore``] This release adds API support for managed Redshift datashares. Customers can now interact with a Redshift datashare that is managed by a different service, such as AWS Data Exchange.
* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway
* api-change:``devops-guru``: [``botocore``] Adds Tags support to DescribeOrganizationResourceCollectionHealth
* api-change:``imagebuilder``: [``botocore``] This release adds support for importing and exporting VM Images as part of the Image Creation workflow via EC2 VM Import/Export.
* api-change:``datasync``: [``botocore``] AWS DataSync now supports FSx Lustre Locations.
* api-change:``finspace-data``: [``botocore``] Make dataset description optional and allow s3 export for dataviews


1.20.24
=======

* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager


1.20.23
=======

* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``network-firewall``: [``botocore``] This release adds support for managed rule groups.
* api-change:``route53-recovery-control-config``: [``botocore``] This release adds tagging supports to Route53 Recovery Control Configuration. New APIs: TagResource, UntagResource and ListTagsForResource. Updates: add optional field `tags` to support tagging while calling CreateCluster, CreateControlPanel and CreateSafetyRule.
* api-change:``ec2``: [``botocore``] Adds waiters support for internet gateways.
* api-change:``sms``: [``botocore``] This release adds SMS discontinuation information to the API and CLI references.
* api-change:``route53domains``: [``botocore``] Amazon Route 53 domain registration APIs now support filtering and sorting in the ListDomains API, deleting a domain by using the DeleteDomain API and getting domain pricing information by using the ListPrices API.
* api-change:``savingsplans``: [``botocore``] Adds the ability to specify Savings Plans hourly commitments using five digits after the decimal point.


1.20.22
=======

* api-change:``lookoutvision``: [``botocore``] This release adds new APIs for packaging an Amazon Lookout for Vision model as an AWS IoT Greengrass component.
* api-change:``sagemaker``: [``botocore``] This release added a new Ambarella device(amba_cv2) compilation support for Sagemaker Neo.
* api-change:``comprehendmedical``: [``botocore``] This release adds a new set of APIs (synchronous and batch) to support the SNOMED-CT ontology.
* api-change:``health``: [``botocore``] Documentation updates for AWS Health
* api-change:``logs``: [``botocore``] This release adds AWS Organizations support as condition key in destination policy for cross account Subscriptions in CloudWatch Logs.
* api-change:``outposts``: [``botocore``] This release adds the UpdateOutpost API.
* api-change:``support``: [``botocore``] Documentation updates for AWS Support.
* api-change:``iot``: [``botocore``] This release allows customer to enable caching of custom authorizer on HTTP protocol for clients that use persistent or Keep-Alive connection in order to reduce the number of Lambda invocations.


1.20.21
=======

* api-change:``location``: [``botocore``] This release adds support for Accuracy position filtering, position metadata and autocomplete for addresses and points of interest based on partial or misspelled free-form text.
* api-change:``appsync``: [``botocore``] AWS AppSync now supports custom domain names, allowing you to associate a domain name that you own with an AppSync API in your account.
* api-change:``route53``: [``botocore``] Add PriorRequestNotComplete exception to UpdateHostedZoneComment API


1.20.20
=======

* api-change:``rekognition``: [``botocore``] This release added new KnownGender types for Celebrity Recognition.


1.20.19
=======

* api-change:``ram``: [``botocore``] This release adds the ability to use the new ResourceRegionScope parameter on List operations that return lists of resources or resource types. This new parameter filters the results by letting you differentiate between global or regional resource types.
* api-change:``networkmanager``: [``botocore``] This release adds API support for AWS Cloud WAN.
* api-change:``amplifyuibuilder``: [``botocore``] This release introduces the actions and data types for the new Amplify UI Builder API. The Amplify UI Builder API provides a programmatic interface for creating and configuring user interface (UI) component libraries and themes for use in Amplify applications.


1.20.18
=======

* api-change:``sagemaker``: [``botocore``] This release enables - 1/ Inference endpoint configuration recommendations and ability to run custom load tests to meet performance needs. 2/ Deploy serverless inference endpoints. 3/ Query, filter and retrieve end-to-end ML lineage graph, and incorporate model quality/bias detection in ML workflow.
* api-change:``kendra``: [``botocore``] Experience Builder allows customers to build search applications without writing code. Analytics Dashboard provides quality and usability metrics for Kendra indexes. Custom Document Enrichment allows customers to build a custom ingestion pipeline to pre-process documents and generate metadata.
* api-change:``directconnect``: [``botocore``] Adds SiteLink support to private and transit virtual interfaces. SiteLink is a new Direct Connect feature that allows routing between Direct Connect points of presence.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``ec2``: [``botocore``] This release adds support for Amazon VPC IP Address Manager (IPAM), which enables you to plan, track, and monitor IP addresses for your workloads. This release also adds support for VPC Network Access Analyzer, which enables you to analyze network access to resources in your Virtual Private Clouds.
* api-change:``shield``: [``botocore``] This release adds API support for Automatic Application Layer DDoS Mitigation for AWS Shield Advanced. Customers can now enable automatic DDoS mitigation in count or block mode for layer 7 protected resources.
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``devops-guru``: [``botocore``] DevOps Guru now provides detailed, database-specific analyses of performance issues and recommends corrective actions for Amazon Aurora database instances with Performance Insights turned on. You can also use AWS tags to choose which resources to analyze and define your applications.
* api-change:``dynamodb``: [``botocore``] Add support for Table Classes and introduce the Standard Infrequent Access table class.


1.20.17
=======

* api-change:``s3``: [``botocore``] Introduce Amazon S3 Glacier Instant Retrieval storage class and a new setting in S3 Object Ownership to disable ACLs for bucket and the objects in it.
* api-change:``backup-gateway``: [``botocore``] Initial release of AWS Backup gateway which enables you to centralize and automate protection of on-premises VMware and VMware Cloud on AWS workloads using AWS Backup.
* api-change:``iot``: [``botocore``] Added the ability to enable/disable IoT Fleet Indexing for Device Defender and Named Shadow information, and search them through IoT Fleet Indexing APIs.
* api-change:``ec2``: [``botocore``] This release adds support for Is4gen and Im4gn instances. This release also adds a new subnet attribute, enableLniAtDeviceIndex, to support local network interfaces, which are logical networking components that connect an EC2 instance to your on-premises network.
* api-change:``outposts``: [``botocore``] This release adds the SupportedHardwareType parameter to CreateOutpost.
* api-change:``storagegateway``: [``botocore``] Added gateway type VTL_SNOW. Added new SNOWBALL HostEnvironment for gateways running on a Snowball device. Added new field HostEnvironmentId to serve as an identifier for the HostEnvironment on which the gateway is running.
* api-change:``kinesis``: [``botocore``] Amazon Kinesis Data Streams now supports on demand streams.
* api-change:``glue``: [``botocore``] Support for DataLake transactions
* api-change:``accessanalyzer``: [``botocore``] AWS IAM Access Analyzer now supports policy validation for resource policies attached to S3 buckets and access points. You can run additional policy checks by specifying the S3 resource type you want to attach to your resource policy.
* api-change:``lakeformation``: [``botocore``] This release adds support for row and cell-based access control in Lake Formation. It also adds support for Lake Formation Governed Tables, which support ACID transactions and automatic storage optimizations.
* api-change:``kafka``: [``botocore``] This release adds three new V2 APIs. CreateClusterV2 for creating both provisioned and serverless clusters. DescribeClusterV2 for getting information about provisioned and serverless clusters and ListClustersV2 for listing all clusters (both provisioned and serverless) in your account.
* api-change:``redshift-data``: [``botocore``] Data API now supports serverless queries.
* api-change:``snowball``: [``botocore``] Tapeball is to integrate tape gateway onto snowball, it enables customer to transfer local data on the tape to snowball,and then ingest the data into tape gateway on the cloud.
* api-change:``workspaces-web``: [``botocore``] This is the initial SDK release for Amazon WorkSpaces Web. Amazon WorkSpaces Web is a low-cost, fully managed WorkSpace built to deliver secure web-based workloads and software-as-a-service (SaaS) application access to users within existing web browsers.
* api-change:``iottwinmaker``: [``botocore``] AWS IoT TwinMaker makes it faster and easier to create, visualize and monitor digital twins of real-world systems like buildings, factories and industrial equipment to optimize operations. Learn more: https://docs.aws.amazon.com/iot-twinmaker/latest/apireference/Welcome.html (New Service) (Preview)
* api-change:``fsx``: [``botocore``] This release adds support for the FSx for OpenZFS file system type, FSx for Lustre file systems with the Persistent_2 deployment type, and FSx for Lustre file systems with Amazon S3 data repository associations and automatic export policies.


1.20.16
=======

* api-change:``s3``: [``botocore``] Amazon S3 Event Notifications adds Amazon EventBridge as a destination and supports additional event types. The PutBucketNotificationConfiguration API can now skip validation of Amazon SQS, Amazon SNS and AWS Lambda destinations.
* api-change:``wellarchitected``: [``botocore``] This update provides support for Well-Architected API users to use custom lens features.
* api-change:``rum``: [``botocore``] This is the first public release of CloudWatch RUM
* api-change:``rbin``: [``botocore``] This release adds support for Recycle Bin.
* api-change:``iotsitewise``: [``botocore``] AWS IoT SiteWise now supports retention configuration for the hot tier storage.
* api-change:``compute-optimizer``: [``botocore``] Adds support for the enhanced infrastructure metrics paid feature. Also adds support for two new sets of resource efficiency metrics, including savings opportunity metrics and performance improvement opportunity metrics.
* api-change:``ecr``: [``botocore``] This release adds supports for pull through cache rules and enhanced scanning.
* api-change:``evidently``: [``botocore``] Introducing Amazon CloudWatch Evidently. This is the first public release of Amazon CloudWatch Evidently.
* api-change:``inspector2``: [``botocore``] This release adds support for the new Amazon Inspector API. The new Amazon Inspector can automatically discover and scan Amazon EC2 instances and Amazon ECR container images for software vulnerabilities and unintended network exposure, and report centralized findings across multiple AWS accounts.
* api-change:``ssm``: [``botocore``] Added two new attributes to DescribeInstanceInformation called SourceId and SourceType along with new string filters SourceIds and SourceTypes to filter instance records.
* api-change:``ec2``: [``botocore``] This release adds support for G5g and M6a instances. This release also adds support for Amazon EBS Snapshots Archive, a feature that enables you to archive your EBS snapshots; and Recycle Bin, a feature that enables you to protect your EBS snapshots against accidental deletion.
* api-change:``dataexchange``: [``botocore``] This release enables providers and subscribers to use Data Set, Job, and Asset operations to work with API assets from Amazon API Gateway. In addition, this release enables subscribers to use the SendApiAsset operation to invoke a provider's Amazon API Gateway API that they are entitled to.


1.20.15
=======

* api-change:``migration-hub-refactor-spaces``: [``botocore``] This is the initial SDK release for AWS Migration Hub Refactor Spaces
* api-change:``textract``: [``botocore``] This release adds support for synchronously analyzing identity documents through a new API: AnalyzeID
* api-change:``personalize-runtime``: [``botocore``] This release adds inference support for Recommenders.
* api-change:``personalize``: [``botocore``] This release adds API support for Recommenders and BatchSegmentJobs.


1.20.14
=======

* api-change:``autoscaling``: [``botocore``] Documentation updates for Amazon EC2 Auto Scaling.
* api-change:``mgn``: [``botocore``] Application Migration Service now supports an additional replication method that does not require agent installation on each source server. This option is available for source servers running on VMware vCenter versions 6.7 and 7.0.
* api-change:``ec2``: [``botocore``] Documentation updates for EC2.
* api-change:``iotdeviceadvisor``: [``botocore``] Documentation update for Device Advisor GetEndpoint API
* api-change:``pinpoint``: [``botocore``] Added a One-Time Password (OTP) management feature. You can use the Amazon Pinpoint API to generate OTP codes and send them to your users as SMS messages. Your apps can then call the API to verify the OTP codes that your users input
* api-change:``outposts``: [``botocore``] This release adds new APIs for working with Outpost sites and orders.


1.20.13
=======

* api-change:``timestream-query``: [``botocore``] Releasing Amazon Timestream Scheduled Queries. It makes real-time analytics more performant and cost-effective for customers by calculating and storing frequently accessed aggregates, and other computations, typically used in operational dashboards, business reports, and other analytics applications
* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``proton``: [``botocore``] This release adds APIs for getting the outputs and provisioned stacks for Environments, Pipelines, and ServiceInstances.  You can now add tags to EnvironmentAccountConnections.  It also adds APIs for working with PR-based provisioning.  Also, it adds APIs for syncing templates with a git repository.
* api-change:``translate``: [``botocore``] This release enables customers to use translation settings to mask profane words and phrases in their translation output.
* api-change:``lambda``: [``botocore``] Remove Lambda function url apis
* api-change:``imagebuilder``: [``botocore``] This release adds support for sharing AMIs with Organizations within an EC2 Image Builder Distribution Configuration.
* api-change:``customer-profiles``: [``botocore``] This release introduces a new auto-merging feature for profile matching. The auto-merging configurations can be set via CreateDomain API or UpdateDomain API. You can use GetIdentityResolutionJob API and ListIdentityResolutionJobs API to fetch job status.
* api-change:``autoscaling``: [``botocore``] Customers can now configure predictive scaling policies to proactively scale EC2 Auto Scaling groups based on any CloudWatch metrics that more accurately represent the load on the group than the four predefined metrics. They can also use math expressions to further customize the metrics.
* api-change:``timestream-write``: [``botocore``] This release adds support for multi-measure records and magnetic store writes. Multi-measure records allow customers to store multiple measures in a single table row. Magnetic store writes enable customers to write late arrival data (data with timestamp in the past) directly into the magnetic store.
* api-change:``iotsitewise``: [``botocore``] AWS IoT SiteWise now accepts data streams that aren't associated with any asset properties. You can organize data by updating data stream associations.


1.20.12
=======

* api-change:``redshift``: [``botocore``] This release adds support for reserved node exchange with restore/resize
* api-change:``elasticache``: [``botocore``] Adding support for r6gd instances for Redis with data tiering. In a cluster with data tiering enabled, when available memory capacity is exhausted, the least recently used data is automatically tiered to solid state drives for cost-effective capacity scaling with minimal performance impact.
* api-change:``opensearch``: [``botocore``] This release adds an optional parameter dry-run for the UpdateDomainConfig API to perform basic validation checks, and detect the deployment type that will be required for the configuration change, without actually applying the change.
* api-change:``backup``: [``botocore``] This release adds new opt-in settings for advanced features for DynamoDB backups
* api-change:``iot``: [``botocore``] This release introduces a new feature, Managed Job Template, for AWS IoT Jobs Service. Customers can now use service provided managed job templates to easily create jobs for supported standard job actions.
* api-change:``iotwireless``: [``botocore``] Two new APIs, GetNetworkAnalyzerConfiguration and UpdateNetworkAnalyzerConfiguration, are added for the newly released Network Analyzer feature which enables customers to view real-time frame information and logs from LoRaWAN devices and gateways.
* api-change:``workspaces``: [``botocore``] Documentation updates for Amazon WorkSpaces
* api-change:``s3``: [``botocore``] Introduce two new Filters to S3 Lifecycle configurations - ObjectSizeGreaterThan and ObjectSizeLessThan. Introduce a new way to trigger actions on noncurrent versions by providing the number of newer noncurrent versions along with noncurrent days.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``macie2``: [``botocore``] Documentation updates for Amazon Macie
* api-change:``ec2``: [``botocore``] This release adds a new parameter ipv6Native to the allow creation of IPv6-only subnets using the CreateSubnet operation, and the operation ModifySubnetAttribute includes new parameters to modify subnet attributes to use resource-based naming and enable DNS resolutions for Private DNS name.
* api-change:``sqs``: [``botocore``] Amazon SQS adds a new queue attribute, SqsManagedSseEnabled, which enables server-side queue encryption using SQS owned encryption keys.
* api-change:``ecs``: [``botocore``] Documentation update for ARM support on Amazon ECS.
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``finspace-data``: [``botocore``] Update documentation for createChangeset API.
* api-change:``dynamodb``: [``botocore``] DynamoDB PartiQL now supports ReturnConsumedCapacity, which returns capacity units consumed by PartiQL APIs if the request specified returnConsumedCapacity parameter. PartiQL APIs include ExecuteStatement, BatchExecuteStatement, and ExecuteTransaction.
* api-change:``lambda``: [``botocore``] Release Lambda event source filtering for SQS, Kinesis Streams, and DynamoDB Streams.
* api-change:``iotdeviceadvisor``: [``botocore``] This release introduces a new feature for Device Advisor: ability to execute multiple test suites in parallel for given customer account. You can use GetEndpoint API to get the device-level test endpoint and call StartSuiteRun with "parallelRun=true" to run suites in parallel.
* api-change:``rds``: [``botocore``] Adds support for Multi-AZ DB clusters for RDS for MySQL and RDS for PostgreSQL.


1.20.11
=======

* api-change:``connect``: [``botocore``] This release adds support for UpdateContactFlowMetadata, DeleteContactFlow and module APIs. For details, see the Release Notes in the Amazon Connect Administrator Guide.
* api-change:``dms``: [``botocore``] Added new S3 endpoint settings to allow to convert the current UTC time into a specified time zone when a date partition folder is created. Using with 'DatePartitionedEnabled'.
* api-change:``es``: [``botocore``] This release adds an optional parameter dry-run for the UpdateElasticsearchDomainConfig API to perform basic validation checks, and detect the deployment type that will be required for the configuration change, without actually applying the change.
* api-change:``ssm``: [``botocore``] Adds new parameter to CreateActivation API . This parameter is for "internal use only".
* api-change:``chime-sdk-meetings``: [``botocore``] Added new APIs for enabling Echo Reduction with Voice Focus.
* api-change:``eks``: [``botocore``] Adding missing exceptions to RegisterCluster operation
* api-change:``quicksight``: [``botocore``] Add support for Exasol data source, 1 click enterprise embedding and email customization.
* api-change:``cloudformation``: [``botocore``] This release include SDK changes for the feature launch of Stack Import to Service Managed StackSet.
* api-change:``rds``: [``botocore``] Adds local backup support to Amazon RDS on AWS Outposts.
* api-change:``braket``: [``botocore``] This release adds support for Amazon Braket Hybrid Jobs.
* api-change:``s3control``: [``botocore``] Added Amazon CloudWatch publishing option for S3 Storage Lens metrics.
* api-change:``finspace-data``: [``botocore``] Add new APIs for managing Datasets, Changesets, and Dataviews.


1.20.10
=======

* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``cloudformation``: [``botocore``] The StackSets ManagedExecution feature will allow concurrency for non-conflicting StackSet operations and queuing the StackSet operations that conflict at a given time for later execution.
* api-change:``redshift``: [``botocore``] Added support of default IAM role for CreateCluster, RestoreFromClusterSnapshot and ModifyClusterIamRoles APIs
* api-change:``lambda``: [``botocore``] Add support for Lambda Function URLs. Customers can use Function URLs to create built-in HTTPS endpoints on their functions.
* api-change:``appstream``: [``botocore``] Includes APIs for managing resources for Elastic fleets: applications, app blocks, and application-fleet associations.
* api-change:``medialive``: [``botocore``] This release adds support for specifying a SCTE-35 PID on input. MediaLive now supports SCTE-35 PID selection on inputs containing one or more active SCTE-35 PIDs.
* api-change:``batch``: [``botocore``] Documentation updates for AWS Batch.
* api-change:``application-insights``: [``botocore``] Application Insights now supports monitoring for HANA


1.20.9
======

* api-change:``ivs``: [``botocore``] Add APIs for retrieving stream session information and support for filtering live streams by health.  For more information, see https://docs.aws.amazon.com/ivs/latest/userguide/stream-health.html
* api-change:``lambda``: [``botocore``] Added support for CLIENT_CERTIFICATE_TLS_AUTH and SERVER_ROOT_CA_CERTIFICATE as SourceAccessType for MSK and Kafka event source mappings.
* api-change:``chime``: [``botocore``] Adds new Transcribe API parameters to StartMeetingTranscription, including support for content identification and redaction (PII & PHI), partial results stabilization, and custom language models.
* api-change:``chime-sdk-meetings``: [``botocore``] Adds new Transcribe API parameters to StartMeetingTranscription, including support for content identification and redaction (PII & PHI), partial results stabilization, and custom language models.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``auditmanager``: [``botocore``] This release introduces a new feature for Audit Manager: Dashboard views. You can now view insights data for your active assessments, and quickly identify non-compliant evidence that needs to be remediated.
* api-change:``databrew``: [``botocore``] This SDK release adds the following new features: 1) PII detection in profile jobs, 2) Data quality rules, enabling validation of data quality in profile jobs, 3) SQL query-based datasets for Amazon Redshift and Snowflake data sources, and 4) Connecting DataBrew datasets with Amazon AppFlow flows.
* api-change:``redshift-data``: [``botocore``] Rolling back Data API serverless features until dependencies are live.
* api-change:``kafka``: [``botocore``] Amazon MSK has added a new API that allows you to update the connectivity settings for an existing cluster to enable public accessibility.
* api-change:``forecast``: [``botocore``] NEW CreateExplanability API that helps you understand how attributes such as price, promotion, etc. contributes to your forecasted values; NEW CreateAutoPredictor API that trains up to 40% more accurate forecasting model, saves up to 50% of retraining time, and provides model level explainability.
* api-change:``appconfig``: [``botocore``] Add Type to support feature flag configuration profiles


1.20.8
======

* api-change:``appconfigdata``: [``botocore``] AWS AppConfig Data is a new service that allows you to retrieve configuration deployed by AWS AppConfig. See the AppConfig user guide for more details on getting started. https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html
* api-change:``drs``: [``botocore``] Introducing AWS Elastic Disaster Recovery (AWS DRS), a new service that minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery.
* api-change:``apigateway``: [``botocore``] Documentation updates for Amazon API Gateway.
* api-change:``sns``: [``botocore``] Amazon SNS introduces the PublishBatch API, which enables customers to publish up to 10 messages per API request. The new API is valid for Standard and FIFO topics.
* api-change:``redshift-data``: [``botocore``] Data API now supports serverless requests.
* api-change:``amplifybackend``: [``botocore``] New APIs to support the Amplify Storage category. Add and manage file storage in your Amplify app backend.


1.20.7
======

* api-change:``location``: [``botocore``] This release adds the support for Relevance, Distance, Time Zone, Language and Interpolated Address for Geocoding and Reverse Geocoding.
* api-change:``cloudtrail``: [``botocore``] CloudTrail Insights now supports ApiErrorRateInsight, which enables customers to identify unusual activity in their AWS account based on API error codes and their rate.


1.20.6
======

* api-change:``migrationhubstrategy``: [``botocore``] AWS SDK for Migration Hub Strategy Recommendations. It includes APIs to start the portfolio assessment, import portfolio data for assessment, and to retrieve recommendations. For more information, see the AWS Migration Hub documentation at https://docs.aws.amazon.com/migrationhub/index.html
* api-change:``ec2``: [``botocore``] Adds a new VPC Subnet attribute "EnableDns64." When enabled on IPv6 Subnets, the Amazon-Provided DNS Resolver returns synthetic IPv6 addresses for IPv4-only destinations.
* api-change:``wafv2``: [``botocore``] Your options for logging web ACL traffic now include Amazon CloudWatch Logs log groups and Amazon S3 buckets.
* api-change:``dms``: [``botocore``] Add Settings in JSON format for the source GCP MySQL endpoint
* api-change:``ssm``: [``botocore``] Adds support for Session Reason and Max Session Duration for Systems Manager Session Manager.
* api-change:``appstream``: [``botocore``] This release includes support for images of AmazonLinux2 platform type.
* api-change:``eks``: [``botocore``] Adding Tags support to Cluster Registrations.
* api-change:``transfer``: [``botocore``] AWS Transfer Family now supports integrating a custom identity provider using AWS Lambda


1.20.5
======

* api-change:``ec2``: [``botocore``] C6i instances are powered by a third-generation Intel Xeon Scalable processor (Ice Lake) delivering all-core turbo frequency of 3.5 GHz. G5 instances feature up to 8 NVIDIA A10G Tensor Core GPUs and second generation AMD EPYC processors.
* api-change:``ssm``: [``botocore``] This Patch Manager release supports creating Patch Baselines for RaspberryPi OS (formerly Raspbian)
* api-change:``devops-guru``: [``botocore``] Add support for cross account APIs.
* api-change:``connect``: [``botocore``] This release adds APIs for creating and managing scheduled tasks. Additionally, adds APIs to describe and update a contact and list associated references.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added automatic modes for GOP configuration and added the ability to ingest screen recordings generated by Safari on MacOS 12 Monterey.


1.20.4
======

* api-change:``dynamodb``: [``botocore``] Updated Help section for "dynamodb update-contributor-insights" API
* api-change:``ec2``: [``botocore``] This release provides an additional route target for the VPC route table.
* api-change:``translate``: [``botocore``] This release enables customers to import Multi-Directional Custom Terminology and use Multi-Directional Custom Terminology in both real-time translation and asynchronous batch translation.


1.20.3
======

* api-change:``backup``: [``botocore``] AWS Backup SDK provides new options when scheduling backups: select supported services and resources that are assigned to a particular tag, linked to a combination of tags, or can be identified by a partial tag value, and exclude resources from their assignments.
* api-change:``ecs``: [``botocore``] This release adds support for container instance health.
* api-change:``resiliencehub``: [``botocore``] Initial release of AWS Resilience Hub, a managed service that enables you to define, validate, and track the resilience of your applications on AWS


1.20.2
======

* api-change:``batch``: [``botocore``] Adds support for scheduling policy APIs.
* api-change:``health``: [``botocore``] Documentation updates for AWS Health.
* api-change:``greengrassv2``: [``botocore``] This release adds support for Greengrass core devices running Windows. You can now specify name of a Windows user to run a component.


1.20.1
======

* bugfix:urllib3: [``botocore``] Fix NO_OP_TICKET import bug in older versions of urllib3


1.20.0
======

* feature:EndpointResolver: [``botocore``] Adding support for resolving modeled FIPS and Dualstack endpoints.
* feature:``six``: [``botocore``] Updated vendored version of ``six`` from 1.10.0 to 1.16.0
* api-change:``sagemaker``: [``botocore``] SageMaker CreateEndpoint and UpdateEndpoint APIs now support additional deployment configuration to manage traffic shifting options and automatic rollback monitoring. DescribeEndpoint now shows new in-progress deployment details with stage status.
* api-change:``chime-sdk-meetings``: [``botocore``] Updated format validation for ids and regions.
* api-change:``wafv2``: [``botocore``] You can now configure rules to run a CAPTCHA check against web requests and, as needed, send a CAPTCHA challenge to the client.
* api-change:``ec2``: [``botocore``] This release adds internal validation on the GatewayAssociationState field


1.19.12
=======

* api-change:``ec2``: [``botocore``] DescribeInstances now returns customer-owned IP addresses for instances running on an AWS Outpost.
* api-change:``translate``: [``botocore``] This release enable customers to use their own KMS keys to encrypt output files when they submit a batch transform job.
* api-change:``resourcegroupstaggingapi``: [``botocore``] Documentation updates and improvements.


1.19.11
=======

* api-change:``chime-sdk-meetings``: [``botocore``] The Amazon Chime SDK Meetings APIs allow software developers to create meetings and attendees for interactive audio, video, screen and content sharing in custom meeting applications which use the Amazon Chime SDK.
* api-change:``sagemaker``: [``botocore``] ListDevices and DescribeDevice now show Edge Manager agent version.
* api-change:``connect``: [``botocore``] This release adds CRUD operation support for Security profile resource in Amazon Connect
* api-change:``iotwireless``: [``botocore``] Adding APIs for the FUOTA (firmware update over the air) and multicast for LoRaWAN devices and APIs to support event notification opt-in feature for Sidewalk related events. A few existing APIs need to be modified for this new feature.
* api-change:``ec2``: [``botocore``] This release adds a new instance replacement strategy for EC2 Fleet, Spot Fleet. Now you can select an action to perform when your instance gets a rebalance notification. EC2 Fleet, Spot Fleet can launch a replacement then terminate the instance that received notification after a termination delay


1.19.10
=======

* api-change:``finspace``: [``botocore``] Adds superuser and data-bundle parameters to CreateEnvironment API
* api-change:``connectparticipant``: [``botocore``] This release adds a new boolean attribute - Connect Participant - to the CreateParticipantConnection API, which can be used to mark the participant as connected.
* api-change:``datasync``: [``botocore``] AWS DataSync now supports Hadoop Distributed File System (HDFS) Locations
* api-change:``macie2``: [``botocore``] This release adds support for specifying the severity of findings that a custom data identifier produces, based on the number of occurrences of text that matches the detection criteria.


1.19.9
======

* api-change:``cloudfront``: [``botocore``] CloudFront now supports response headers policies to add HTTP headers to the responses that CloudFront sends to viewers. You can use these policies to add CORS headers, control browser caching, and more, without modifying your origin or writing any code.
* api-change:``connect``: [``botocore``] Amazon Connect Chat now supports real-time message streaming.
* api-change:``nimble``: [``botocore``] Amazon Nimble Studio adds support for users to stop and start streaming sessions.


1.19.8
======

* api-change:``rekognition``: [``botocore``] This Amazon Rekognition Custom Labels release introduces the management of datasets with  projects
* api-change:``networkmanager``: [``botocore``] This release adds API support to aggregate resources, routes, and telemetry data across a Global Network.
* api-change:``lightsail``: [``botocore``] This release adds support to enable access logging for buckets in the Lightsail object storage service.
* api-change:``neptune``: [``botocore``] Adds support for major version upgrades to ModifyDbCluster API


1.19.7
======

* api-change:``transcribe``: [``botocore``] Transcribe and Transcribe Call Analytics now support automatic language identification along with custom vocabulary, vocabulary filter, custom language model and PII redaction.
* api-change:``application-insights``: [``botocore``] Added Monitoring support for SQL Server Failover Cluster Instance. Additionally, added a new API to allow one-click monitoring of containers resources.
* api-change:``rekognition``: [``botocore``] This release added new attributes to Rekognition Video GetCelebrityRecognition API operations.
* api-change:``connect``: [``botocore``] Amazon Connect Chat now supports real-time message streaming.
* api-change:``ec2``: [``botocore``] Support added for AMI sharing with organizations and organizational units in ModifyImageAttribute API


1.19.6
======

* api-change:``gamelift``: [``botocore``] Added support for Arm-based AWS Graviton2 instances, such as M6g, C6g, and R6g.
* api-change:``ecs``: [``botocore``] Amazon ECS now supports running Fargate tasks on Windows Operating Systems Families which includes Windows Server 2019 Core and Windows Server 2019 Full.
* api-change:``sagemaker``: [``botocore``] This release adds support for RStudio on SageMaker.
* api-change:``connectparticipant``: [``botocore``] This release adds a new boolean attribute - Connect Participant - to the CreateParticipantConnection API, which can be used to mark the participant as connected.
* api-change:``ec2``: [``botocore``] Added new read-only DenyAllIGWTraffic network interface attribute. Added support for DL1 24xlarge instances powered by Habana Gaudi Accelerators for deep learning model training workloads
* api-change:``ssm-incidents``: [``botocore``] Updating documentation, adding new field to ConflictException to indicate earliest retry timestamp for some operations, increase maximum length of nextToken fields


1.19.5
======

* api-change:``autoscaling``: [``botocore``] This release adds support for attribute-based instance type selection, a new EC2 Auto Scaling feature that lets customers express their instance requirements as a set of attributes, such as vCPU, memory, and storage.
* api-change:``ec2``: [``botocore``] This release adds: attribute-based instance type selection for EC2 Fleet, Spot Fleet, a feature that lets customers express instance requirements as attributes like vCPU, memory, and storage; and Spot placement score, a feature that helps customers identify an optimal location to run Spot workloads.
* enhancement:Session: Added `get_partition_for_region` to lookup partition for a given region_name
* api-change:``eks``: [``botocore``] EKS managed node groups now support BOTTLEROCKET_x86_64 and BOTTLEROCKET_ARM_64 AMI types.
* api-change:``sagemaker``: [``botocore``] This release allows customers to describe one or more versioned model packages through BatchDescribeModelPackage, update project via UpdateProject, modify and read customer metadata properties using Create, Update and Describe ModelPackage and enables cross account registration of model packages.
* enhancement:Session: [``botocore``] Added `get_partition_for_region` allowing partition lookup by region name.
* api-change:``textract``: [``botocore``] This release adds support for asynchronously analyzing invoice and receipt documents through two new APIs: StartExpenseAnalysis and GetExpenseAnalysis
* enchancement:``s3``: TransferConfig now supports the `max_bandwidth` argument.


1.19.4
======

* api-change:``emr-containers``: [``botocore``] This feature enables auto-generation of certificate  to secure the managed-endpoint and removes the need for customer provided certificate-arn during managed-endpoint setup.
* api-change:``chime-sdk-messaging``: [``botocore``] The Amazon Chime SDK now supports push notifications through Amazon Pinpoint
* api-change:``chime-sdk-identity``: [``botocore``] The Amazon Chime SDK now supports push notifications through Amazon Pinpoint


1.19.3
======

* api-change:``rds``: [``botocore``] This release adds support for Amazon RDS Custom, which is a new RDS management type that gives you full access to your database and operating system. For more information, see https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html
* api-change:``auditmanager``: [``botocore``] This release introduces a new feature for Audit Manager: Custom framework sharing. You can now share your custom frameworks with another AWS account, or replicate them into another AWS Region under your own account.
* api-change:``ec2``: [``botocore``] This release adds support to create a VPN Connection that is not attached to a Gateway at the time of creation. Use this to create VPNs associated with Core Networks, or modify your VPN and attach a gateway using the modify API after creation.
* api-change:``route53resolver``: [``botocore``] New API for ResolverConfig, which allows autodefined rules for reverse DNS resolution to be disabled for a VPC


1.19.2
======

* api-change:``quicksight``: [``botocore``] Added QSearchBar option for GenerateEmbedUrlForRegisteredUser ExperienceConfiguration to support Q search bar embedding
* api-change:``auditmanager``: [``botocore``] This release introduces character restrictions for ControlSet names. We updated regex patterns for the following attributes: ControlSet, CreateAssessmentFrameworkControlSet, and UpdateAssessmentFrameworkControlSet.
* api-change:``chime``: [``botocore``] Chime VoiceConnector and VoiceConnectorGroup APIs will now return an ARN.


1.19.1
======

* api-change:``connect``: [``botocore``] Released Amazon Connect hours of operation API for general availability (GA). This API also supports AWS CloudFormation. For more information, see Amazon Connect Resource Type Reference in the AWS CloudFormation User Guide.


1.19.0
======

* api-change:``appflow``: [``botocore``] Feature to add support for  JSON-L format for S3 as a source.
* api-change:``mediapackage-vod``: [``botocore``] MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added support for specifying caption time delta in milliseconds and the ability to apply color range legalization to source content other than AVC video.
* api-change:``mediapackage``: [``botocore``] When enabled, MediaPackage passes through digital video broadcasting (DVB) subtitles into the output.
* api-change:``panorama``: [``botocore``] General availability for AWS Panorama. AWS SDK for Panorama includes APIs to manage your devices and nodes, and deploy computer vision applications to the edge. For more information, see the AWS Panorama documentation at http://docs.aws.amazon.com/panorama
* feature:Serialization: [``botocore``] rest-json serialization defaults aligned across AWS SDKs
* api-change:``directconnect``: [``botocore``] This release adds 4 new APIS, which needs to be public able
* api-change:``securityhub``: [``botocore``] Added support for cross-Region finding aggregation, which replicates findings from linked Regions to a single aggregation Region. Added operations to view, enable, update, and delete the finding aggregation.


1.18.65
=======

* api-change:``dataexchange``: [``botocore``] This release adds support for our public preview of AWS Data Exchange for Amazon Redshift. This enables data providers to list products including AWS Data Exchange datashares for Amazon Redshift, giving subscribers read-only access to provider data in Amazon Redshift.
* api-change:``chime-sdk-messaging``: [``botocore``] The Amazon Chime SDK now allows developers to execute business logic on in-flight messages before they are delivered to members of a messaging channel with channel flows.


1.18.64
=======

* api-change:``quicksight``: [``botocore``] AWS QuickSight Service  Features    - Add IP Restriction UI and public APIs support.
* enchancement:AWSCRT: [``botocore``] Upgrade awscrt extra to 0.12.5
* api-change:``ivs``: [``botocore``] Bug fix: remove unsupported maxResults and nextToken pagination parameters from ListTagsForResource


1.18.63
=======

* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``glue``: [``botocore``] Enable S3 event base crawler API.


1.18.62
=======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``autoscaling``: [``botocore``] Amazon EC2 Auto Scaling now supports filtering describe Auto Scaling groups API using tags
* api-change:``sagemaker``: [``botocore``] This release updates the provisioning artifact ID to an optional parameter in CreateProject API. The provisioning artifact ID defaults to the latest provisioning artifact ID of the product if you don't provide one.
* api-change:``robomaker``: [``botocore``] Adding support to GPU simulation jobs as well as non-ROS simulation jobs.


1.18.61
=======

* api-change:``config``: [``botocore``] Adding Config support for AWS::OpenSearch::Domain
* api-change:``ec2``: [``botocore``] This release adds support for additional VPC Flow Logs delivery options to S3, such as Apache Parquet formatted files, Hourly partitions and Hive-compatible S3 prefixes
* api-change:``storagegateway``: [``botocore``] Adding support for Audit Logs on NFS shares and Force Closing Files on SMB shares.
* api-change:``workmail``: [``botocore``] This release adds APIs for adding, removing and retrieving details of mail domains
* api-change:``kinesisanalyticsv2``: [``botocore``] Support for Apache Flink 1.13 in Kinesis Data Analytics. Changed the required status of some Update properties to better fit the corresponding Create properties.


1.18.60
=======

* api-change:``cloudsearch``: [``botocore``] Adds an additional validation exception for Amazon CloudSearch configuration APIs for better error handling.
* api-change:``ecs``: [``botocore``] Documentation only update to address tickets.
* api-change:``mediatailor``: [``botocore``] MediaTailor now supports ad prefetching.
* api-change:``ec2``: [``botocore``] EncryptionSupport for InstanceStorageInfo added to DescribeInstanceTypes API


1.18.59
=======

* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* bugfix:Signing: [``botocore``] SigV4QueryAuth and CrtSigV4QueryAuth now properly respect AWSRequest.params while signing boto/botocore`#2521 <https://github.com/boto/botocore/issues/2521>`__
* api-change:``medialive``: [``botocore``] This release adds support for Transport Stream files as an input type to MediaLive encoders.
* api-change:``ec2``: [``botocore``] Documentation update for Amazon EC2.
* api-change:``frauddetector``: [``botocore``] New model type: Transaction Fraud Insights, which is optimized for online transaction fraud. Stored Events, which allows customers to send and store data directly within Amazon Fraud Detector. Batch Import, which allows customers to upload a CSV file of historic event data for processing and storage


1.18.58
=======

* api-change:``lexv2-runtime``: [``botocore``] Update lexv2-runtime client to latest version
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``secretsmanager``: [``botocore``] Documentation updates for Secrets Manager
* api-change:``securityhub``: [``botocore``] Added new resource details objects to ASFF, including resources for WAF rate-based rules, EC2 VPC endpoints, ECR repositories, EKS clusters, X-Ray encryption, and OpenSearch domains. Added additional details for CloudFront distributions, CodeBuild projects, ELB V2 load balancers, and S3 buckets.
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert has added the ability to set account policies which control access restrictions for HTTP, HTTPS, and S3 content sources.
* api-change:``ec2``: [``botocore``] This release removes a requirement for filters on SearchLocalGatewayRoutes operations.


1.18.57
=======

* api-change:``kendra``: [``botocore``] Amazon Kendra now supports indexing and querying documents in different languages.
* api-change:``grafana``: [``botocore``] Initial release of the SDK for Amazon Managed Grafana API.
* api-change:``firehose``: [``botocore``] Allow support for Amazon Opensearch Service(successor to Amazon Elasticsearch Service) as a Kinesis Data Firehose delivery destination.
* api-change:``backup``: [``botocore``] Launch of AWS Backup Vault Lock, which protects your backups from malicious and accidental actions, works with existing backup policies, and helps you meet compliance requirements.
* api-change:``schemas``: [``botocore``] Removing unused request/response objects.
* api-change:``chime``: [``botocore``] This release enables customers to configure Chime MediaCapturePipeline via API.


1.18.56
=======

* api-change:``sagemaker``: [``botocore``] This release adds a new TrainingInputMode FastFile for SageMaker Training APIs.
* api-change:``amplifybackend``: [``botocore``] Adding a new field 'AmplifyFeatureFlags' to the response of the GetBackend operation. It will return a stringified version of the cli.json file for the given Amplify project.
* api-change:``fsx``: [``botocore``] This release adds support for Lustre 2.12 to FSx for Lustre.
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports integration with AWS SSO


1.18.55
=======

* api-change:``workmail``: [``botocore``] This release allows customers to change their inbound DMARC settings in Amazon WorkMail.
* api-change:``location``: [``botocore``] Add support for PositionFiltering.
* api-change:``application-autoscaling``: [``botocore``] With this release, Application Auto Scaling adds support for Amazon Neptune. Customers can now automatically add or remove Read Replicas of their Neptune clusters to keep the average CPU Utilization at the target value specified by the customers.
* api-change:``ec2``: [``botocore``] Released Capacity Reservation Fleet, a feature of Amazon EC2 Capacity Reservations, which provides a way to manage reserved capacity across instance types. For more information: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html
* api-change:``glue``: [``botocore``] This release adds tag as an input of CreateConnection
* api-change:``backup``: [``botocore``] AWS Backup Audit Manager framework report.


1.18.54
=======

* api-change:``codebuild``: [``botocore``] CodeBuild now allows you to select how batch build statuses are sent to the source provider for a project.
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``kms``: [``botocore``] Added SDK examples for ConnectCustomKeyStore, CreateCustomKeyStore, CreateKey, DeleteCustomKeyStore, DescribeCustomKeyStores, DisconnectCustomKeyStore, GenerateDataKeyPair, GenerateDataKeyPairWithoutPlaintext, GetPublicKey, ReplicateKey, Sign, UpdateCustomKeyStore and Verify APIs


1.18.53
=======

* api-change:``synthetics``: [``botocore``] CloudWatch Synthetics now enables customers to choose a customer managed AWS KMS key or an Amazon S3-managed key instead of an AWS managed key (default) for the encryption of artifacts that the canary stores in Amazon S3. CloudWatch Synthetics also supports artifact S3 location updation now.
* api-change:``ssm``: [``botocore``] When "AutoApprovable" is true for a Change Template, then specifying --auto-approve (boolean) in Start-Change-Request-Execution will create a change request that bypasses approver review. (except for change calendar restrictions)
* api-change:``apprunner``: [``botocore``] This release contains several minor bug fixes.


1.18.52
=======

* api-change:``network-firewall``: [``botocore``] This release adds support for strict ordering for stateful rule groups. Using strict ordering, stateful rules are evaluated in the exact order in which you provide them.
* api-change:``dataexchange``: [``botocore``] This release enables subscribers to set up automatic exports of newly published revisions using the new EventAction API.
* api-change:``workmail``: [``botocore``] This release adds support for mobile device access overrides management in Amazon WorkMail.
* api-change:``account``: [``botocore``] This release of the Account Management API enables customers to manage the alternate contacts for their AWS accounts. For more information, see https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html
* api-change:``workspaces``: [``botocore``] Added CreateUpdatedWorkspaceImage API to update WorkSpace images with latest software and drivers. Updated DescribeWorkspaceImages API to display if there are updates available for WorkSpace images.
* api-change:``cloudcontrol``: [``botocore``] Initial release of the SDK for AWS Cloud Control API
* api-change:``macie2``: [``botocore``] Amazon S3 bucket metadata now indicates whether an error or a bucket's permissions settings prevented Amazon Macie from retrieving data about the bucket or the bucket's objects.


1.18.51
=======

* api-change:``lambda``: [``botocore``] Adds support for Lambda functions powered by AWS Graviton2 processors. Customers can now select the CPU architecture for their functions.
* api-change:``sesv2``: [``botocore``] This release includes the ability to use 2048 bits RSA key pairs for DKIM in SES, either with Easy DKIM or Bring Your Own DKIM.
* api-change:``amp``: [``botocore``] This release adds alert manager and rule group namespace APIs


1.18.50
=======

* api-change:``transfer``: [``botocore``] Added changes for managed workflows feature APIs.
* api-change:``imagebuilder``: [``botocore``] Fix description for AmiDistributionConfiguration Name property, which actually refers to the output AMI name. Also updated for consistent terminology to use "base" image, and another update to fix description text.


1.18.49
=======

* api-change:``appintegrations``: [``botocore``] The Amazon AppIntegrations service enables you to configure and reuse connections to external applications.
* api-change:``wisdom``: [``botocore``] Released Amazon Connect Wisdom, a feature of Amazon Connect, which provides real-time recommendations and search functionality in general availability (GA).  For more information, see https://docs.aws.amazon.com/wisdom/latest/APIReference/Welcome.html.
* api-change:``pinpoint``: [``botocore``] Added support for journey with contact center activity
* api-change:``voice-id``: [``botocore``] Released the Amazon Voice ID SDK, for usage with the Amazon Connect Voice ID feature released for Amazon Connect.
* api-change:``connect``: [``botocore``] This release updates a set of APIs: CreateIntegrationAssociation, ListIntegrationAssociations, CreateUseCase, and StartOutboundVoiceContact. You can use it to create integrations with Amazon Pinpoint for the Amazon Connect Campaigns use case, Amazon Connect Voice ID, and Amazon Connect Wisdom.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version


1.18.48
=======

* api-change:``license-manager``: [``botocore``] AWS License Manager now allows customers to get the LicenseArn in the Checkout API Response.
* api-change:``ec2``: [``botocore``] DescribeInstances now returns Platform Details, Usage Operation, and Usage Operation Update Time.


1.18.47
=======

* api-change:``mediaconvert``: [``botocore``] This release adds style and positioning support for caption or subtitle burn-in from rich text sources such as TTML. This release also introduces configurable image-based trick play track generation.
* api-change:``appsync``: [``botocore``] Documented the new OpenSearchServiceDataSourceConfig data type. Added deprecation notes to the ElasticsearchDataSourceConfig data type.
* api-change:``ssm``: [``botocore``] Added cutoff behavior support for preventing new task invocations from starting when the maintenance window cutoff time is reached.


1.18.46
=======

* api-change:``imagebuilder``: [``botocore``] This feature adds support for specifying GP3 volume throughput and configuring instance metadata options for instances launched by EC2 Image Builder.
* api-change:``wafv2``: [``botocore``] Added the regex match rule statement, for matching web requests against a single regular expression.
* api-change:``mediatailor``: [``botocore``] This release adds support to configure logs for playback configuration.
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``iam``: [``botocore``] Added changes to OIDC API about not using port numbers in the URL.
* api-change:``license-manager``: [``botocore``] AWS License Manager now allows customers to change their Windows Server or SQL license types from Bring-Your-Own-License (BYOL) to License Included or vice-versa (using the customer's media).
* api-change:``mediapackage-vod``: [``botocore``] MediaPackage VOD will now return the current processing statuses of an asset's endpoints. The status can be QUEUED, PROCESSING, PLAYABLE, or FAILED.


1.18.45
=======

* api-change:``comprehend``: [``botocore``] Amazon Comprehend now supports versioning of custom models, improved training with ONE_DOC_PER_FILE text documents for custom entity recognition, ability to provide specific test sets during training, and live migration to new model endpoints.
* api-change:``iot``: [``botocore``] This release adds support for verifying, viewing and filtering AWS IoT Device Defender detect violations with four verification states.
* api-change:``ecr``: [``botocore``] This release adds additional support for repository replication
* api-change:``ec2``: [``botocore``] This update adds support for downloading configuration templates using new APIs (GetVpnConnectionDeviceTypes and GetVpnConnectionDeviceSampleConfiguration) and Internet Key Exchange version 2 (IKEv2) parameters for many popular CGW devices.


1.18.44
=======

* api-change:``opensearch``: [``botocore``] This release adds an optional parameter in the ListDomainNames API to filter domains based on the engine type (OpenSearch/Elasticsearch).
* api-change:``es``: [``botocore``] This release adds an optional parameter in the ListDomainNames API to filter domains based on the engine type (OpenSearch/Elasticsearch).
* api-change:``dms``: [``botocore``] Optional flag force-planned-failover added to reboot-replication-instance API call. This flag can be used to test a planned failover scenario used during some maintenance operations.


1.18.43
=======

* api-change:``kafkaconnect``: [``botocore``] This is the initial SDK release for Amazon Managed Streaming for Apache Kafka Connect (MSK Connect).
* api-change:``macie2``: [``botocore``] This release adds support for specifying which managed data identifiers are used by a classification job, and retrieving a list of managed data identifiers that are available.
* api-change:``robomaker``: [``botocore``] Adding support to create container based Robot and Simulation applications by introducing an environment field
* api-change:``s3``: [``botocore``] Add support for access point arn filtering in S3 CW Request Metrics
* api-change:``transcribe``: [``botocore``] This release adds support for subtitling with Amazon Transcribe batch jobs.
* api-change:``sagemaker``: [``botocore``] Add API for users to retry a failed pipeline execution or resume a stopped one.
* api-change:``pinpoint``: [``botocore``] This SDK release adds a new feature for Pinpoint campaigns, in-app messaging.


1.18.42
=======

* api-change:``sagemaker``: [``botocore``] This release adds support for "Project Search"
* api-change:``ec2``: [``botocore``] This release adds support for vt1 3xlarge, 6xlarge and 24xlarge instances powered by Xilinx Alveo U30 Media Accelerators for video transcoding workloads
* api-change:``wafv2``: [``botocore``] This release adds support for including rate based rules in a rule group.
* api-change:``chime``: [``botocore``] Adds support for SipHeaders parameter for CreateSipMediaApplicationCall.
* api-change:``comprehend``: [``botocore``] Amazon Comprehend now allows you to train and run PDF and Word documents for custom entity recognition. With PDF and Word formats, you can extract information from documents containing headers, lists and tables.


1.18.41
=======

* api-change:``iot``: [``botocore``] AWS IoT Rules Engine adds OpenSearch action. The OpenSearch rule action lets you stream data from IoT sensors and applications to Amazon OpenSearch Service which is a successor to Amazon Elasticsearch Service.
* api-change:``ec2``: [``botocore``] Adds support for T3 instances on Amazon EC2 Dedicated Hosts.
* enhancement:Tagged Unions: [``botocore``] Introducing support for the `union` trait on structures in request and response objects.


1.18.40
=======

* api-change:``cloudformation``: [``botocore``] Doc only update for CloudFormation that fixes several customer-reported issues.
* api-change:``rds``: [``botocore``] This release adds support for providing a custom timeout value for finding a scaling point during autoscaling in Aurora Serverless v1.
* api-change:``ecr``: [``botocore``] This release updates terminology around KMS keys.
* api-change:``sagemaker``: [``botocore``] This release adds support for "Lifecycle Configurations" to SageMaker Studio
* api-change:``transcribe``: [``botocore``] This release adds an API option for startTranscriptionJob and startMedicalTranscriptionJob that allows the user to specify encryption context key value pairs for batch jobs.
* api-change:``quicksight``: [``botocore``] Add new data source type for Amazon OpenSearch (successor to Amazon ElasticSearch).


1.18.39
=======

* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``codeguru-reviewer``: [``botocore``] The Amazon CodeGuru Reviewer API now includes the RuleMetadata data object and a Severity attribute on a RecommendationSummary object. A RuleMetadata object contains information about a rule that generates a recommendation. Severity indicates how severe the issue associated with a recommendation is.
* api-change:``lookoutequipment``: [``botocore``] Added OffCondition parameter to CreateModel API


1.18.38
=======

* api-change:``opensearch``: [``botocore``] Updated Configuration APIs for Amazon OpenSearch Service (successor to Amazon Elasticsearch Service)
* api-change:``ram``: [``botocore``] A minor text-only update that fixes several customer issues.
* api-change:``kafka``: [``botocore``] Amazon MSK has added a new API that allows you to update the encrypting and authentication settings for an existing cluster.


1.18.37
=======

* api-change:``elasticache``: [``botocore``] Doc only update for ElastiCache
* api-change:``amp``: [``botocore``] This release adds tagging support for Amazon Managed Service for Prometheus workspace.
* api-change:``forecast``: [``botocore``] Predictor creation now supports selecting an accuracy metric to optimize in AutoML and hyperparameter optimization. This release adds additional accuracy metrics for predictors - AverageWeightedQuantileLoss, MAPE and MASE.
* api-change:``xray``: [``botocore``] Updated references to AWS KMS keys and customer managed keys to reflect current terminology.
* api-change:``ssm-contacts``: [``botocore``] Added SDK examples for SSM-Contacts.
* api-change:``mediapackage``: [``botocore``] SPEKE v2 support for live CMAF packaging type. SPEKE v2 is an upgrade to the existing SPEKE API to support multiple encryption keys, it supports live DASH currently.
* api-change:``eks``: [``botocore``] Adding RegisterCluster and DeregisterCluster operations, to support connecting external clusters to EKS.


1.18.36
=======

* api-change:``chime-sdk-identity``: [``botocore``] Documentation updates for Chime
* api-change:``chime-sdk-messaging``: [``botocore``] Documentation updates for Chime
* api-change:``outposts``: [``botocore``] This release adds a new API CreateOrder.
* api-change:``frauddetector``: [``botocore``] Enhanced GetEventPrediction API response to include risk scores from imported SageMaker models
* api-change:``codeguru-reviewer``: [``botocore``] Added support for CodeInconsistencies detectors


1.18.35
=======

* api-change:``acm-pca``: [``botocore``] Private Certificate Authority Service now allows customers to enable an online certificate status protocol (OCSP) responder service on their private certificate authorities. Customers can also optionally configure a custom CNAME for their OCSP responder.
* api-change:``s3control``: [``botocore``] S3 Multi-Region Access Points provide a single global endpoint to access a data set that spans multiple S3 buckets in different AWS Regions.
* api-change:``accessanalyzer``: [``botocore``] Updates service API, documentation, and paginators to support multi-region access points from Amazon S3.
* api-change:``schemas``: [``botocore``] This update include the support for Schema Discoverer to discover the events sent to the bus from another account. The feature will be enabled by default when discoverer is created or updated but can also be opt-in or opt-out  by specifying the value for crossAccount.
* api-change:``securityhub``: [``botocore``] New ASFF Resources: AwsAutoScalingLaunchConfiguration, AwsEc2VpnConnection, AwsEcrContainerImage. Added KeyRotationStatus to AwsKmsKey. Added AccessControlList, BucketLoggingConfiguration,BucketNotificationConfiguration and BucketNotificationConfiguration to AwsS3Bucket.
* enhancement:s3: [``botocore``] Added support for S3 Multi-Region Access Points
* api-change:``efs``: [``botocore``] Update efs client to latest version
* api-change:``transfer``: [``botocore``] AWS Transfer Family introduces Managed Workflows for creating, executing, monitoring, and standardizing post file transfer processing
* api-change:``ebs``: [``botocore``] Documentation updates for Amazon EBS direct APIs.
* api-change:``quicksight``: [``botocore``] This release adds support for referencing parent datasets as sources in a child dataset.
* api-change:``fsx``: [``botocore``] Announcing Amazon FSx for NetApp ONTAP, a new service that provides fully managed shared storage in the AWS Cloud with the data access and management capabilities of ONTAP.
* enhancement:Signers: [``botocore``] Added support for Sigv4a Signing Algorithm
* api-change:``lex-models``: [``botocore``] Lex now supports Korean (ko-KR) locale.


1.18.34
=======

* api-change:``ec2``: [``botocore``] Added LaunchTemplate support for the IMDS IPv6 endpoint
* api-change:``cloudtrail``: [``botocore``] Documentation updates for CloudTrail
* api-change:``mediatailor``: [``botocore``] This release adds support for wall clock programs in LINEAR channels.
* api-change:``config``: [``botocore``] Documentation updates for config
* api-change:``servicecatalog-appregistry``: [``botocore``] Introduction of GetAssociatedResource API and GetApplication response extension for Resource Groups support.


1.18.33
=======

* api-change:``iot``: [``botocore``] Added Create/Update/Delete/Describe/List APIs for a new IoT resource named FleetMetric. Added a new Fleet Indexing query API named GetBucketsAggregation. Added a new field named DisconnectedReason in Fleet Indexing query response. Updated their related documentations.
* api-change:``polly``: [``botocore``] Amazon Polly adds new South African English voice - Ayanda. Ayanda is available as Neural voice only.
* api-change:``compute-optimizer``: [``botocore``] Documentation updates for Compute Optimizer
* api-change:``sqs``: [``botocore``] Amazon SQS adds a new queue attribute, RedriveAllowPolicy, which includes the dead-letter queue redrive permission parameters. It defines which source queues can specify dead-letter queues as a JSON object.
* api-change:``memorydb``: [``botocore``] Documentation updates for MemoryDB


1.18.32
=======

* api-change:``codebuild``: [``botocore``] Documentation updates for CodeBuild
* api-change:``firehose``: [``botocore``] This release adds the Dynamic Partitioning feature to Kinesis Data Firehose service for S3 destinations.
* api-change:``kms``: [``botocore``] This release has changes to KMS nomenclature to remove the word master from both the "Customer master key" and "CMK" abbreviation and replace those naming conventions with "KMS key".
* api-change:``cloudformation``: [``botocore``] AWS CloudFormation allows you to iteratively develop your applications when failures are encountered without rolling back successfully provisioned resources. By specifying stack failure options, you can troubleshoot resources in a CREATE_FAILED or UPDATE_FAILED status.


1.18.31
=======

* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``ec2``: [``botocore``] This release adds the BootMode flag to the ImportImage API and showing the detected BootMode of an ImportImage task.


1.18.30
=======

* api-change:``transcribe``: [``botocore``] This release adds support for batch transcription in six new languages - Afrikaans, Danish, Mandarin Chinese (Taiwan), New Zealand English, South African English, and Thai.
* api-change:``rekognition``: [``botocore``] This release added new attributes to Rekognition RecognizeCelebities and GetCelebrityInfo API operations.
* api-change:``ec2``: [``botocore``] Support added for resizing VPC prefix lists
* api-change:``compute-optimizer``: [``botocore``] Adds support for 1) the AWS Graviton (AWS_ARM64) recommendation preference for Amazon EC2 instance and Auto Scaling group recommendations, and 2) the ability to get the enrollment statuses for all member accounts of an organization.


1.18.29
=======

* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports triggering resource cleanup workflow when account or resource goes out of policy scope for AWS WAF, Security group, AWS Network Firewall, and Amazon Route 53 Resolver DNS Firewall policies.
* api-change:``ec2``: [``botocore``] Support added for IMDS IPv6 endpoint
* api-change:``datasync``: [``botocore``] Added include filters to CreateTask and UpdateTask, and added exclude filters to StartTaskExecution, giving customers more granular control over how DataSync transfers files, folders, and objects.
* api-change:``events``: [``botocore``] AWS CWEvents adds an enum of EXTERNAL for EcsParameters LaunchType for PutTargets API


1.18.28
=======

* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added MBAFF encoding support for AVC video and the ability to pass encryption context from the job settings to S3.
* api-change:``polly``: [``botocore``] Amazon Polly adds new New Zealand English voice - Aria. Aria is available as Neural voice only.
* api-change:``transcribe``: [``botocore``] This release adds support for feature tagging with Amazon Transcribe batch jobs.
* api-change:``ssm``: [``botocore``] Updated Parameter Store property for logging improvements.
* api-change:``iot-data``: [``botocore``] Updated Publish with support for new Retain flag and added two new API operations: GetRetainedMessage, ListRetainedMessages.


1.18.27
=======

* api-change:``dms``: [``botocore``] Amazon AWS DMS service now support Redis target endpoint migration. Now S3 endpoint setting is capable to setup features which are used to be configurable only in extract connection attributes.
* api-change:``frauddetector``: [``botocore``] Updated an element of the DescribeModelVersion API response (LogitMetrics -> logOddsMetrics) for clarity. Added new exceptions to several APIs to protect against unlikely scenarios.
* api-change:``iotsitewise``: [``botocore``] Documentation updates for AWS IoT SiteWise
* api-change:``dlm``: [``botocore``] Added AMI deprecation support for Amazon Data Lifecycle Manager EBS-backed AMI policies.
* api-change:``glue``: [``botocore``] Add support for Custom Blueprints
* api-change:``apigateway``: [``botocore``] Adding some of the pending releases (1) Adding WAF Filter to GatewayResponseType enum (2) Ensuring consistent error model for all operations (3) Add missing BRE to GetVpcLink operation
* api-change:``backup``: [``botocore``] AWS Backup - Features: Evaluate your backup activity and generate audit reports.


1.18.26
=======

* api-change:``eks``: [``botocore``] Adds support for EKS add-ons "preserve" flag, which allows customers to maintain software on their EKS clusters after removing it from EKS add-ons management.
* api-change:``comprehend``: [``botocore``] Add tagging support for Comprehend async inference job.
* api-change:``robomaker``: [``botocore``] Documentation updates for RoboMaker
* api-change:``ec2``: [``botocore``] encryptionInTransitSupported added to DescribeInstanceTypes API


1.18.25
=======

* api-change:``ec2``: [``botocore``] The ImportImage API now supports the ability to create AMIs with AWS-managed licenses for Microsoft SQL Server for both Windows and Linux.
* api-change:``memorydb``: [``botocore``] AWS MemoryDB  SDK now supports all APIs for newly launched MemoryDB service.
* api-change:``application-autoscaling``: [``botocore``] This release extends Application Auto Scaling support for replication group of Amazon ElastiCache Redis clusters. Auto Scaling monitors and automatically expands node group count and number of replicas per node group when a critical usage threshold is met or according to customer-defined schedule.
* api-change:``appflow``: [``botocore``] This release adds support for SAPOData connector and extends Veeva connector for document extraction.


1.18.24
=======

* api-change:``codebuild``: [``botocore``] CodeBuild now allows you to make the build results for your build projects available to the public without requiring access to an AWS account.
* api-change:``route53``: [``botocore``] Documentation updates for route53
* api-change:``sagemaker-runtime``: [``botocore``] Update sagemaker-runtime client to latest version
* api-change:``route53resolver``: [``botocore``] Documentation updates for Route 53 Resolver
* api-change:``sagemaker``: [``botocore``] Amazon SageMaker now supports Asynchronous Inference endpoints. Adds PlatformIdentifier field that allows Notebook Instance creation with different platform selections. Increases the maximum number of containers in multi-container endpoints to 15. Adds more instance types to InstanceType field.


1.18.23
=======

* api-change:``cloud9``: [``botocore``] Added DryRun parameter to CreateEnvironmentEC2 API. Added ManagedCredentialsActions parameter to UpdateEnvironment API
* api-change:``ec2``: [``botocore``] This release adds support for EC2 ED25519 key pairs for authentication
* api-change:``clouddirectory``: [``botocore``] Documentation updates for clouddirectory
* api-change:``ce``: [``botocore``] This release is a new feature for Cost Categories: Split charge rules. Split charge rules enable you to allocate shared costs between your cost category values.
* api-change:``logs``: [``botocore``] Documentation-only update for CloudWatch Logs


1.18.22
=======

* api-change:``iotsitewise``: [``botocore``] AWS IoT SiteWise added query window for the interpolation interval. AWS IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval minus the window to the timestamp of each interval plus the window.
* api-change:``s3``: [``botocore``] Documentation updates for Amazon S3
* api-change:``codebuild``: [``botocore``] CodeBuild now allows you to select how batch build statuses are sent to the source provider for a project.
* api-change:``ds``: [``botocore``] This release adds support for describing client authentication settings.
* api-change:``config``: [``botocore``] Update ResourceType enum with values for Backup Plan, Selection, Vault, RecoveryPoint; ECS Cluster, Service, TaskDefinition; EFS AccessPoint, FileSystem; EKS Cluster; ECR Repository resources
* api-change:``license-manager``: [``botocore``] AWS License Manager now allows end users to call CheckoutLicense API using new CheckoutType PERPETUAL. Perpetual checkouts allow sellers to check out a quantity of entitlements to be drawn down for consumption.


1.18.21
=======

* api-change:``quicksight``: [``botocore``] Documentation updates for QuickSight.
* api-change:``emr``: [``botocore``] Update emr client to latest version
* api-change:``customer-profiles``: [``botocore``] This release introduces Standard Profile Objects, namely Asset and Case which contain values populated by data from third party systems and belong to a specific profile. This release adds an optional parameter, ObjectFilter to the ListProfileObjects API in order to search for these Standard Objects.
* api-change:``elasticache``: [``botocore``] This release adds ReplicationGroupCreateTime field to ReplicationGroup which indicates the UTC time when ElastiCache ReplicationGroup is created


1.18.20
=======

* api-change:``sagemaker``: [``botocore``] Amazon SageMaker Autopilot adds new metrics for all candidate models generated by Autopilot experiments.
* api-change:``apigatewayv2``: [``botocore``] Adding support for ACM imported or private CA certificates for mTLS enabled domain names
* api-change:``apigateway``: [``botocore``] Adding support for ACM imported or private CA certificates for mTLS enabled domain names
* api-change:``databrew``: [``botocore``] This SDK release adds support for the output of a recipe job results to Tableau Hyper format.
* api-change:``lambda``: [``botocore``] Lambda Python 3.9 runtime launch


1.18.19
=======

* api-change:``snow-device-management``: [``botocore``] AWS Snow Family customers can remotely monitor and operate their connected AWS Snowcone devices.
* api-change:``ecs``: [``botocore``] Documentation updates for ECS.
* api-change:``nimble``: [``botocore``] Add new attribute 'ownedBy' in Streaming Session APIs. 'ownedBy' represents the AWS SSO Identity Store User ID of the owner of the Streaming Session resource.
* api-change:``codebuild``: [``botocore``] CodeBuild now allows you to make the build results for your build projects available to the public without requiring access to an AWS account.
* api-change:``ebs``: [``botocore``] Documentation updates for Amazon EBS direct APIs.
* api-change:``route53``: [``botocore``] Documentation updates for route53


1.18.18
=======

* api-change:``chime``: [``botocore``] Add support for "auto" in Region field of StartMeetingTranscription API request.
* enchancement:Client: [``botocore``] Improve client performance by caching _alias_event_name on EventAliaser


1.18.17
=======

* api-change:``wafv2``: [``botocore``] This release adds APIs to support versioning feature of AWS WAF Managed rule groups
* api-change:``rekognition``: [``botocore``] This release adds support for four new types of segments (opening credits, content segments, slates, and studio logos), improved accuracy for credits and shot detection and new filters to control black frame detection.
* api-change:``ssm``: [``botocore``] Documentation updates for AWS Systems Manager.


1.18.16
=======

* api-change:``synthetics``: [``botocore``] Documentation updates for Visual Monitoring feature and other doc ticket fixes.
* api-change:``chime-sdk-identity``: [``botocore``] The Amazon Chime SDK Identity APIs allow software developers to create and manage unique instances of their messaging applications.
* api-change:``chime-sdk-messaging``: [``botocore``] The Amazon Chime SDK Messaging APIs allow software developers to send and receive messages in custom messaging applications.
* api-change:``connect``: [``botocore``] This release adds support for agent status and hours of operation. For details, see the Release Notes in the Amazon Connect Administrator Guide.
* api-change:``lightsail``: [``botocore``] This release adds support to track when a bucket access key was last used.
* api-change:``athena``: [``botocore``] Documentation updates for Athena.


1.18.15
=======

* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``autoscaling``: [``botocore``] EC2 Auto Scaling adds configuration checks and Launch Template validation to Instance Refresh.


1.18.14
=======

* api-change:``rds``: [``botocore``] This release adds AutomaticRestartTime to the DescribeDBInstances and DescribeDBClusters operations. AutomaticRestartTime indicates the time when a stopped DB instance or DB cluster is restarted automatically.
* api-change:``imagebuilder``: [``botocore``] Updated list actions to include a list of valid filters that can be used in the request.
* api-change:``transcribe``: [``botocore``] This release adds support for call analytics (batch) within Amazon Transcribe.
* api-change:``events``: [``botocore``] Update events client to latest version
* api-change:``ssm-incidents``: [``botocore``] Documentation updates for Incident Manager.


1.18.13
=======

* api-change:``redshift``: [``botocore``] API support for Redshift Data Sharing feature.
* api-change:``iotsitewise``: [``botocore``] My AWS Service (placeholder) - This release introduces custom Intervals and offset for tumbling window in metric for AWS IoT SiteWise.
* api-change:``glue``: [``botocore``] Add ConcurrentModificationException to create-table, delete-table, create-database, update-database, delete-database
* api-change:``mediaconvert``: [``botocore``] AWS Elemental MediaConvert SDK has added control over the passthrough of XDS captions metadata to outputs.
* api-change:``proton``: [``botocore``] Docs only add idempotent create apis


1.18.12
=======

* api-change:``ssm-contacts``: [``botocore``] Added new attribute in AcceptCode API. AcceptCodeValidation takes in two values - ENFORCE, IGNORE. ENFORCE forces validation of accept code and IGNORE ignores it which is also the default behavior; Corrected TagKeyList length from 200 to 50
* api-change:``greengrassv2``: [``botocore``] This release adds support for component system resource limits and idempotent Create operations. You can now specify the maximum amount of CPU and memory resources that each component can use.


1.18.11
=======

* api-change:``appsync``: [``botocore``] AWS AppSync now supports a new authorization mode allowing you to define your own authorization logic using an AWS Lambda function.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``secretsmanager``: [``botocore``] Add support for KmsKeyIds in the ListSecretVersionIds API response
* api-change:``sagemaker``: [``botocore``] API changes with respect to Lambda steps in model building pipelines. Adds several waiters to async Sagemaker Image APIs. Add more instance types to AppInstanceType field


1.18.10
=======

* api-change:``savingsplans``: [``botocore``] Documentation update for valid Savings Plans offering ID pattern
* api-change:``ec2``: [``botocore``] This release adds support for G4ad xlarge and 2xlarge instances powered by AMD Radeon Pro V520 GPUs and AMD 2nd Generation EPYC processors
* api-change:``chime``: [``botocore``] Adds support for live transcription of meetings with Amazon Transcribe and Amazon Transcribe Medical.  The new APIs, StartMeetingTranscription and StopMeetingTranscription, control the generation of user-attributed transcriptions sent to meeting clients via Amazon Chime SDK data messages.
* api-change:``iotsitewise``: [``botocore``] Added support for AWS IoT SiteWise Edge. You can now create an AWS IoT SiteWise gateway that runs on AWS IoT Greengrass V2. With the gateway,  you can collect local server and equipment data, process the data, and export the selected data from the edge to the AWS Cloud.
* api-change:``iot``: [``botocore``] Increase maximum credential duration of role alias to 12 hours.


1.18.9
======

* api-change:``sso-admin``: [``botocore``] Documentation updates for arn:aws:trebuchet:::service:v1:03a2216d-1cda-4696-9ece-1387cb6f6952
* api-change:``cloudformation``: [``botocore``] SDK update to support Importing existing Stacks to new/existing Self Managed StackSet - Stack Import feature.


1.18.8
======

* api-change:``route53``: [``botocore``] This release adds support for the RECOVERY_CONTROL health check type to be used in conjunction with Route53 Application Recovery Controller.
* api-change:``iotwireless``: [``botocore``] Add SidewalkManufacturingSn as an identifier to allow Customer to query WirelessDevice, in the response, AmazonId is added in the case that Sidewalk device is return.
* api-change:``route53-recovery-control-config``: [``botocore``] Amazon Route 53 Application Recovery Controller's routing control - Routing Control Configuration APIs help you create and delete clusters, control panels, routing controls and safety rules. State changes (On/Off) of routing controls are not part of configuration APIs.
* api-change:``route53-recovery-readiness``: [``botocore``] Amazon Route 53 Application Recovery Controller's readiness check capability continually monitors resource quotas, capacity, and network routing policies to ensure that the recovery environment is scaled and configured to take over when needed.
* api-change:``quicksight``: [``botocore``] Add support to use row-level security with tags when embedding dashboards for users not provisioned in QuickSight
* api-change:``iotanalytics``: [``botocore``] IoT Analytics now supports creating a dataset resource with IoT SiteWise MultiLayerStorage data stores, enabling customers to query industrial data within the service. This release includes adding JOIN functionality for customers to query multiple data sources in a dataset.
* api-change:``shield``: [``botocore``] Change name of DDoS Response Team (DRT) to Shield Response Team (SRT)
* api-change:``lexv2-models``: [``botocore``] Update lexv2-models client to latest version
* api-change:``redshift-data``: [``botocore``] Added structures to support new Data API operation BatchExecuteStatement, used to execute multiple SQL statements within a single transaction.
* api-change:``route53-recovery-cluster``: [``botocore``] Amazon Route 53 Application Recovery Controller's routing control - Routing Control Data Plane APIs help you update the state (On/Off) of the routing controls to reroute traffic across application replicas in a 100% available manner.
* api-change:``batch``: [``botocore``] Add support for ListJob filters


1.18.7
======

* api-change:``s3control``: [``botocore``] S3 Access Point aliases can be used anywhere you use S3 bucket names to access data in S3
* api-change:``textract``: [``botocore``] Adds support for AnalyzeExpense, a new API to extract relevant data such as contact information, items purchased, and vendor name, from almost any invoice or receipt without the need for any templates or configuration.
* api-change:``proton``: [``botocore``] Documentation-only update links
* api-change:``identitystore``: [``botocore``] Documentation updates for SSO API Ref.
* api-change:``cloudwatch``: [``botocore``] Update cloudwatch client to latest version
* api-change:``synthetics``: [``botocore``] CloudWatch Synthetics now supports visual testing in its canaries.


1.18.6
======

* api-change:``securityhub``: [``botocore``] Added product name, company name, and Region fields for security findings. Added details objects for RDS event subscriptions and AWS ECS services. Added fields to the details for AWS Elasticsearch domains.
* api-change:``imagebuilder``: [``botocore``] Update to documentation to reapply missing change to SSM uninstall switch default value and improve description.
* api-change:``s3outposts``: [``botocore``] Add on-premise access type support for endpoints


1.18.5
======

* api-change:``medialive``: [``botocore``] MediaLive now supports passing through style data on WebVTT caption outputs.
* api-change:``databrew``: [``botocore``] This SDK release adds two new features: 1) Output to Native JDBC destinations and 2) Adding configurations to profile jobs
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``s3control``: [``botocore``] Documentation updates for Amazon S3-control
* api-change:``ec2``: [``botocore``] This release allows customers to assign prefixes to their elastic network interface and to reserve IP blocks in their subnet CIDRs. These reserved blocks can be used to assign prefixes to elastic network interfaces or be excluded from auto-assignment.
* api-change:``qldb``: [``botocore``] Amazon QLDB now supports ledgers encrypted with customer managed KMS keys. Changes in CreateLedger, UpdateLedger and DescribeLedger APIs to support the changes.


1.18.4
======

* api-change:``kendra``: [``botocore``] Amazon Kendra now provides a data source connector for Amazon WorkDocs. For more information, see https://docs.aws.amazon.com/kendra/latest/dg/data-source-workdocs.html
* api-change:``proton``: [``botocore``] Documentation updates for AWS Proton
* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``rds``: [``botocore``] Adds the OriginalSnapshotCreateTime field to the DBSnapshot response object. This field timestamps the underlying data of a snapshot and doesn't change when the snapshot is copied.
* api-change:``elbv2``: [``botocore``] Update elbv2 client to latest version
* api-change:``lambda``: [``botocore``] New ResourceConflictException error code for PutFunctionEventInvokeConfig, UpdateFunctionEventInvokeConfig, and DeleteFunctionEventInvokeConfig operations.
* api-change:``codebuild``: [``botocore``] AWS CodeBuild now allows you to set the access permissions for build artifacts, project artifacts, and log files that are uploaded to an Amazon S3 bucket that is owned by another account.
* api-change:``personalize``: [``botocore``] My AWS Service (placeholder) - Making minProvisionedTPS an optional parameter when creating a campaign. If not provided, it defaults to 1.
* api-change:``emr``: [``botocore``] Update emr client to latest version


1.18.3
======

* api-change:``compute-optimizer``: [``botocore``] Documentation updates for Compute Optimizer
* api-change:``ec2``: [``botocore``] Added idempotency to the CreateVolume API using the ClientToken request parameter


1.18.2
======

* api-change:``imagebuilder``: [``botocore``] Documentation updates for reversal of default value for additional instance configuration SSM switch, plus improved descriptions for semantic versioning.
* api-change:``directconnect``: [``botocore``] Documentation updates for directconnect
* api-change:``health``: [``botocore``] In the Health API, the maximum number of entities for the EventFilter and EntityFilter data types has changed from 100 to 99. This change is related to an internal optimization of the AWS Health service.
* api-change:``robomaker``: [``botocore``] This release allows customers to create a new version of WorldTemplates with support for Doors.
* api-change:``location``: [``botocore``] Add five new API operations: UpdateGeofenceCollection, UpdateMap, UpdatePlaceIndex, UpdateRouteCalculator, UpdateTracker.
* api-change:``emr-containers``: [``botocore``] Updated DescribeManagedEndpoint and ListManagedEndpoints to return failureReason and stateDetails in API response.


1.18.1
======

* api-change:``appintegrations``: [``botocore``] Documentation update for AppIntegrations Service
* api-change:``chime``: [``botocore``] This SDK release adds Account Status as one of the attributes in Account API response
* api-change:``auditmanager``: [``botocore``] This release relaxes the S3 URL character restrictions in AWS Audit Manager. Regex patterns have been updated for the following attributes: s3RelativePath, destination, and s3ResourcePath. 'AWS' terms have also been replaced with entities to align with China Rebrand documentation efforts.


1.18.0
======

* api-change:``ec2``: [``botocore``] This feature enables customers  to specify weekly recurring time window(s) for scheduled events that reboot, stop or terminate EC2 instances.
* api-change:``cognito-idp``: [``botocore``] Documentation updates for cognito-idp
* api-change:``ecs``: [``botocore``] Documentation updates for support of awsvpc mode on Windows.
* api-change:``lex-models``: [``botocore``] Lex now supports the en-IN locale
* api-change:``iotsitewise``: [``botocore``] Update the default endpoint for the APIs used to manage asset models, assets, gateways, tags, and account configurations. If you have firewalls with strict egress rules, configure the rules to grant you access to api.iotsitewise.[region].amazonaws.com or api.iotsitewise.[cn-region].amazonaws.com.cn.
* feature:Python: Drop support for Python 2.7
* feature:Python: [``botocore``] Dropped support for Python 2.7


1.17.112
========

* api-change:``dms``: [``botocore``] Release of feature needed for ECA-Endpoint settings. This allows customer to delete a field in endpoint settings by using --exact-settings flag in modify-endpoint api. This also displays default values for certain required fields of endpoint settings in describe-endpoint-settings api.
* api-change:``glue``: [``botocore``] Add support for Event Driven Workflows
* api-change:``acm``: [``botocore``] Added support for RSA 3072 SSL certificate import
* api-change:``healthlake``: [``botocore``] General availability for Amazon HealthLake. StartFHIRImportJob and StartFHIRExportJob APIs now require AWS KMS parameter. For more information, see the Amazon HealthLake Documentation https://docs.aws.amazon.com/healthlake/index.html.
* api-change:``wellarchitected``: [``botocore``] This update provides support for Well-Architected API users to mark answer choices as not applicable.
* api-change:``lightsail``: [``botocore``] This release adds support for the Amazon Lightsail object storage service, which allows you to create buckets and store objects.


1.17.111
========

* api-change:``amplifybackend``: [``botocore``] Added Sign in with Apple OAuth provider.
* api-change:``redshift``: [``botocore``] Release new APIs to support new Redshift feature - Authentication Profile
* api-change:``ssm``: [``botocore``] Changes to OpsCenter APIs to support a new feature, operational insights.
* api-change:``lex-models``: [``botocore``] Customers can now migrate bots built with Lex V1 APIs to V2 APIs. This release adds APIs to initiate and manage the migration of a bot.
* api-change:``directconnect``: [``botocore``] This release adds a new filed named awsLogicalDeviceId that it displays the AWS Direct Connect endpoint which terminates a physical connection's BGP Sessions.
* api-change:``pricing``: [``botocore``] Documentation updates for api.pricing


1.17.110
========

* api-change:``eks``: [``botocore``] Documentation updates for Wesley to support the parallel node upgrade feature.
* api-change:``kendra``: [``botocore``] Amazon Kendra now supports Principal Store


1.17.109
========

* api-change:``sagemaker``: [``botocore``] Releasing new APIs related to Tuning steps in model building pipelines.
* api-change:``frauddetector``: [``botocore``] This release adds support for ML Explainability to display model variable importance value in Amazon Fraud Detector.
* api-change:``mediaconvert``: [``botocore``] MediaConvert now supports color, style and position information passthrough from 608 and Teletext to SRT and WebVTT subtitles. MediaConvert now also supports Automatic QVBR quality levels for QVBR RateControlMode.


1.17.108
========

* api-change:``eks``: [``botocore``] Added waiters for EKS FargateProfiles.
* api-change:``outposts``: [``botocore``] Added property filters for listOutposts
* api-change:``fms``: [``botocore``] AWS Firewall Manager now supports route table monitoring, and provides remediation action recommendations to security administrators for AWS Network Firewall policies with misconfigured routes.
* api-change:``mediatailor``: [``botocore``] Add ListAlerts for Channel, Program, Source Location, and VOD Source to return alerts for resources.
* api-change:``devops-guru``: [``botocore``] Add AnomalyReportedTimeRange field to include open and close time of anomalies.
* api-change:``ssm-contacts``: [``botocore``] Updated description for CreateContactChannel contactId.


1.17.107
========

* api-change:``iam``: [``botocore``] Documentation updates for AWS Identity and Access Management (IAM).
* api-change:``sts``: [``botocore``] Documentation updates for AWS Security Token Service.
* api-change:``mq``: [``botocore``] adds support for modifying the maintenance window for brokers.
* api-change:``cloudfront``: [``botocore``] Amazon CloudFront now provides two new APIs, ListConflictingAliases and AssociateAlias, that help locate and move Alternate Domain Names (CNAMEs) if you encounter the CNAMEAlreadyExists error code.
* api-change:``chime``: [``botocore``] Releasing new APIs for AWS Chime MediaCapturePipeline
* api-change:``iotsitewise``: [``botocore``] This release add storage configuration APIs for AWS IoT SiteWise.
* api-change:``storagegateway``: [``botocore``] Adding support for oplocks for SMB file shares,  S3 Access Point and S3 Private Link for all file shares and IP address support for file system associations
* api-change:``ec2``: [``botocore``] This release adds resource ids and tagging support for VPC security group rules.


1.17.106
========

* api-change:``lambda``: [``botocore``] Added support for AmazonMQRabbitMQ as an event source. Added support for VIRTUAL_HOST as SourceAccessType for streams event source mappings.
* api-change:``imagebuilder``: [``botocore``] Adds support for specifying parameters to customize components for recipes. Expands configuration of the Amazon EC2 instances that are used for building and testing images, including the ability to specify commands to run on launch, and more control over installation and removal of the SSM agent.
* api-change:``mgn``: [``botocore``] Bug fix: Remove not supported EBS encryption type "NONE"
* api-change:``eks``: [``botocore``] Adding new error code UnsupportedAddonModification for Addons in EKS
* api-change:``macie2``: [``botocore``] Sensitive data findings in Amazon Macie now include enhanced location data for JSON and JSON Lines files
* api-change:``sns``: [``botocore``] Documentation updates for Amazon SNS.


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

