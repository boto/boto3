.. _guide_security:
.. include:: _security-includes.txt

Security
========

Cloud security at |AWSlong| (|AWS|) is the highest priority. As an |AWS|
customer, you benefit from a data center and network architecture that is built to meet the
requirements of the most security-sensitive organizations. Security is a shared responsibility
between |AWS| and you. The `Shared Responsibility Model <https://aws.amazon.com/compliance/shared-responsibility-model/>`_
describes this as Security of the Cloud and Security in the Cloud.

**Security of the Cloud** – AWS is responsible for
protecting the infrastructure that runs all of the services offered in the |AWS| Cloud and
providing you with services that you can use securely. Our security responsibility is the
highest priority at |AWS|, and the effectiveness of our security is regularly tested and
verified by third-party auditors as part of the `AWS Compliance Programs <https://aws.amazon.com/compliance/programs/>`_.

**Security in the Cloud** – Your responsibility is
determined by the |AWS| service you are using, and other factors including the sensitivity of
your data, your organization’s requirements, and applicable laws and regulations.

|SERVICENAMESENTENCECASE| follows the `shared responsibility model <https://aws.amazon.com/compliance/shared-responsibility-model>`_
through the specific |AWS| services it supports. For |AWS| service security information, see the
`AWS service security documentation page <https://aws.amazon.com/security/?id=docs_gateway#aws-security>`_
and `AWS services that are in scope of AWS compliance efforts by compliance program <https://aws.amazon.com/compliance/services-in-scope/>`_.

.. _data_protection_intro:

Data Protection
---------------

For data protection purposes, we recommend that you protect |AWS| account credentials and set up individual user accounts with
|IAMlong| (|IAM|), so that each user is given only the permissions necessary to fulfill their job duties. We also recommend that
you secure your data in the following ways:

* Use multi-factor authentication (MFA) with each account.
* Use SSL/TLS to communicate with |AWS| resources.
* Set up API and user activity logging with |CTlong|.
* Use |AWS| encryption solutions, along with all default security controls within |AWS| services.
* Use advanced managed security services such as |MCElong|, which assists in discovering and securing personal data that
  is stored in |S3|.

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into
free-form fields such as a **Name** field. This includes when you work with |SERVICENAME| or other |AWS| services
using the console, API, |CLI|, or |AWS| SDKs. Any data that you enter into |SERVICENAME| or other services might get picked up
for inclusion in diagnostic logs. When you provide a URL to an external server, don't include credentials information in the URL
to validate your request to that server.

For more information about data protection, see the
`AWS Shared Responsibility Model and GDPR <https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/>`_
blog post on the *AWS Security Blog*.

.. _identity_and_access_management_intro:

Identity and Access Management
------------------------------

|IAMlong| (|IAM|) is an |AWS| service that helps an administrator securely control access to |AWS| resources.
|IAM| administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use |AWS| resources. |IAM| is an |AWS| service that you can use with no additional charge.

To use |SERVICENAME| to access |AWS|, you need an |AWS| account and |AWS| credentials. To increase the security of your
|AWS| account, we recommend that you use an *IAM user* to provide access credentials instead of using your |AWS|
account credentials.

For details about working with |IAM|, see |IAM|_.

For an overview of |IAM| users and why they are important for the security of your account,
see `AWS Security Credentials <https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`_
in the |AWS-gr|_.

.. _compliance_validation_intro:

Compliance Validation
---------------------

The security and compliance of |AWS| services is assessed by third-party auditors as part
of multiple |AWS| compliance programs. These include SOC, PCI, FedRAMP, HIPAA, and others.
|AWS| provides a frequently updated list of |AWS| services in scope of specific compliance programs at
`AWS Services in Scope by Compliance Program <https://aws.amazon.com/compliance/services-in-scope/>`_.

Third-party audit reports are available for you to download using |ARTlong|. For more information, see
`Downloading Reports in AWS Artifact <https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html>`_.

For more information about |AWS| compliance programs, see `AWS Compliance Programs <https://aws.amazon.com/compliance/programs/>`_.

Your compliance responsibility when using |SERVICENAME| to access an |AWS| service is determined by the sensitivity of your data, your organization’s compliance objectives,
and applicable laws and regulations. If your use of an |AWS| service is subject to compliance with standards such as HIPAA, PCI, or FedRAMP, |AWS| provides resources to help:

* `Security and Compliance Quick Start Guides <https://aws.amazon.com/quickstart/?quickstart-all.sort-by=item.additionalFields.updateDate&quickstart-all.sort-order=desc&awsf.quickstart-homepage-filter=categories%23security-identity-compliance>`_ –
  Deployment guides that discuss architectural considerations and provide steps for deploying security-focused and compliance-focused baseline environments on |AWS|.
* `Architecting for HIPAA Security and Compliance Whitepaper <https://d0.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf>`_ –
  A whitepaper that describes how companies can use |AWS| to create HIPAA-compliant applications.
* `AWS Compliance Resources <https://aws.amazon.com/compliance/resources/>`_ – A collection of workbooks and guides that might apply to your industry and location.
* `AWS Config <https://aws.amazon.com/config/>`_ – A service that assesses how well your resource configurations comply with
  internal practices, industry guidelines, and regulations.
* `AWS Security Hub <https://aws.amazon.com/security-hub>`_ – A comprehensive view of your security state within |AWS| that helps
  you check your compliance with security industry standards and best practices.

.. _resilience_intro:

Resilience
----------

The |AWS| global infrastructure is built around |AWS| Regions and Availability Zones.

|AWS| Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking.

With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption.
Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about |AWS| Regions and Availability Zones, see `AWS Global Infrastructure <https://aws.amazon.com/about-aws/global-infrastructure/>`_.

.. _infrastructure_security_intro:

Infrastructure Security
-----------------------

For information about |AWS| security processes, see the `AWS: Overview of Security Processes <https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf>`_ whitepaper.