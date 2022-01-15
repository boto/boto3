.. _guide_security:

Security
========

Cloud security at Amazon Web Services (AWS) is the highest priority. As an AWS
customer, you benefit from a data center and network architecture that is built to meet the
requirements of the most security-sensitive organizations. Security is a shared responsibility
between AWS and you. The `Shared Responsibility Model <https://aws.amazon.com/compliance/shared-responsibility-model/>`_
describes this as Security of the Cloud and Security in the Cloud.

**Security of the Cloud** – AWS is responsible for
protecting the infrastructure that runs all of the services offered in the AWS Cloud and
providing you with services that you can use securely. Our security responsibility is the
highest priority at AWS, and the effectiveness of our security is regularly tested and
verified by third-party auditors as part of the `AWS Compliance Programs <https://aws.amazon.com/compliance/programs/>`_.

**Security in the Cloud** – Your responsibility is
determined by the AWS service you are using, and other factors including the sensitivity of
your data, your organization’s requirements, and applicable laws and regulations.

Boto3 follows the `shared responsibility model <https://aws.amazon.com/compliance/shared-responsibility-model>`_
through the specific AWS services it supports. For AWS service security information, see the
`AWS service security documentation page <https://aws.amazon.com/security/?id=docs_gateway#aws-security>`_
and `AWS services that are in scope of AWS compliance efforts by compliance program <https://aws.amazon.com/compliance/services-in-scope/>`_.

.. _data_protection_intro:

Data protection
---------------

The AWS `shared responsibility model <https://aws.amazon.com/compliance/shared-responsibility-model>`_
applies to data protection in AWS SDK for Python (Boto3). As described in this model,
AWS is responsible for protecting the global infrastructure that runs all of the AWS
Cloud. You are responsible for maintaining control over your content that is hosted on
this infrastructure. This content includes the security configuration and management
tasks for the AWS services that you use. For more information about data privacy, see
the `Data Privacy FAQ <https://aws.amazon.com/compliance/data-privacy-faq>`_.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with
AWS Identity and Access Management (IAM), so that each user is given only the permissions necessary to fulfill their job duties. We also recommend that
you secure your data in the following ways:

* Use multi-factor authentication (MFA) with each account.
* Use SSL/TLS to communicate with AWS resources. To use minimum TLS version of 1.2, see `Enforcing TLS 1.2`_
* Set up API and user activity logging with AWS CloudTrail.
* Use AWS encryption solutions, along with all default security controls within AWS services.
* Use advanced managed security services such as Amazon Macie, which assists in discovering and securing personal data that
  is stored in Amazon S3.

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into
free-form fields such as a **Name** field. This includes when you work with Boto3 or other AWS services
using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into Boto3 or other services might get picked up
for inclusion in diagnostic logs. When you provide a URL to an external server, don't include credentials information in the URL
to validate your request to that server.

.. _identity_and_access_management_intro:

Identity and access management
------------------------------

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access to AWS resources.
IAM administrators control who can be *authenticated* (signed in) and *authorized* (have permissions) to use AWS resources. IAM is an AWS service that you can use with no additional charge.

To use Boto3 to access AWS, you need an AWS account and AWS credentials. To increase the security of your
AWS account, we recommend that you use an *IAM user* to provide access credentials instead of using your AWS
account credentials.

For details about working with IAM, see `IAM <https://aws.amazon.com/iam/>`_.

For an overview of IAM users and why they are important for the security of your account,
see `AWS Security Credentials <https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`_
in the `Amazon Web Services General Reference <https://docs.aws.amazon.com/general/latest/gr/>`_.

.. _compliance_validation_intro:

Compliance validation
---------------------

The security and compliance of AWS services is assessed by third-party auditors as part
of multiple AWS compliance programs. These include SOC, PCI, FedRAMP, HIPAA, and others.
AWS provides a frequently updated list of AWS services in scope of specific compliance programs at
`AWS Services in Scope by Compliance Program <https://aws.amazon.com/compliance/services-in-scope/>`_.

Third-party audit reports are available for you to download using AWS Artifact. For more information, see
`Downloading Reports in AWS Artifact <https://docs.aws.amazon.com/artifact/latest/ug/downloading-documents.html>`_.

For more information about AWS compliance programs, see `AWS Compliance Programs <https://aws.amazon.com/compliance/programs/>`_.

Your compliance responsibility when using Boto3 to access an AWS service is determined by the sensitivity of your data, your organization’s compliance objectives,
and applicable laws and regulations. If your use of an AWS service is subject to compliance with standards such as HIPAA, PCI, or FedRAMP, AWS provides resources to help:

* `Security and Compliance Quick Start Guides <https://aws.amazon.com/quickstart/?quickstart-all.sort-by=item.additionalFields.updateDate&quickstart-all.sort-order=desc&awsf.quickstart-homepage-filter=categories%23security-identity-compliance>`_ –
  Deployment guides that discuss architectural considerations and provide steps for deploying security-focused and compliance-focused baseline environments on AWS.
* `Architecting for HIPAA Security and Compliance Whitepaper <https://d0.awsstatic.com/whitepapers/compliance/AWS_HIPAA_Compliance_Whitepaper.pdf>`_ –
  A whitepaper that describes how companies can use AWS to create HIPAA-compliant applications.
* `AWS Compliance Resources <https://aws.amazon.com/compliance/resources/>`_ – A collection of workbooks and guides that might apply to your industry and location.
* `AWS Config <https://aws.amazon.com/config/>`_ – A service that assesses how well your resource configurations comply with
  internal practices, industry guidelines, and regulations.
* `AWS Security Hub <https://aws.amazon.com/security-hub>`_ – A comprehensive view of your security state within AWS that helps
  you check your compliance with security industry standards and best practices.

.. _resilience_intro:

Resilience
----------

The AWS global infrastructure is built around AWS Regions and Availability Zones.

AWS Regions provide multiple physically separated and isolated Availability Zones, which are connected with low-latency, high-throughput, and highly redundant networking.

With Availability Zones, you can design and operate applications and databases that automatically fail over between Availability Zones without interruption.
Availability Zones are more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For more information about AWS Regions and Availability Zones, see `AWS Global Infrastructure <https://aws.amazon.com/about-aws/global-infrastructure/>`_.

.. _infrastructure_security_intro:

Infrastructure security
-----------------------

For information about AWS security processes, see the `AWS: Overview of Security Processes <https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf>`_ whitepaper.

.. _enforcing_tls_12_intro:

Enforcing TLS 1.2
------------------

To ensure the AWS SDK for Python uses no TLS version earlier than TLS 1.2, you might need to recompile OpenSSL to enforce this minimum and then recompile Python to use the recompiled OpenSSL.

Determining supported protocols
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

First, create a self-signed certificate to use for the test server and the SDK using OpenSSL::

    openssl req -subj '/CN=localhost' -x509 -newkey rsa:4096 -nodes -keyout key.pem -out cert.pem -days 365

Then spin up a test server using OpenSSL::

    openssl s_server -key key.pem -cert cert.pem -www

In a new terminal window, create a virtual environment and install the SDK::

    python3 -m venv test-env
    source test-env/bin/activate
    pip install botocore


Create a new Python script called ``check.py`` that will use the SDK’s underlying HTTP library::

    import urllib3
    URL = 'https://localhost:4433/'

    http = urllib3.PoolManager(
        ca_certs='cert.pem',
        cert_reqs='CERT_REQUIRED',
    )
    r = http.request('GET', URL)
    print(r.data.decode('utf-8'))

Run the script::

    python check.py 

This will give details about the connection made. Search for ``Protocol :`` in the output. If the output is ``TLSv1.2`` or later, the SDK will default to TLS v1.2 and later. If it's earlier, you need to recompile OpenSSL and then recompile Python.

However, even if your installation of Python defaults to TLS v1.2 or later, it's still possible for Python to renegotiate to a version earlier than TLS v1.2 if the server doesn't support TLS v1.2+. To check that Python will not automatically renegotiate to these earlier versions, restart the test server with the following::

    openssl s_server -key key.pem -cert cert.pem -no_tls1_3 -no_tls1_2 -www

.. note::

    If you are using an older version of OpenSSL, you might not have the ``-no_tls_3`` flag available. 
    In this case, just remove the flag because the version of OpenSSL you are using doesn't support TLS v1.3.

Rerun the Python script::

    python check.py

If your installation of Python correctly does not renegotiate for versions earlier than TLS 1.2, you should receive an SSL error::

    urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='localhost', port=4433): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: UNSUPPORTED_PROTOCOL] unsupported protocol (_ssl.c:1108)')))

If you are able to make a connection, you need to recompile OpenSSL and Python to disable negotiation of protocols earlier than TLS v1.2.

Compile OpenSSL and Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~

To ensure the SDK or CLI doesn't not negotiate for anything earlier than TLS 1.2, you need to recompile OpenSSL and Python. First copy the following content to create a script and run it::


    #!/usr/bin/env bash
    set -e

    OPENSSL_VERSION="1.1.1d"
    OPENSSL_PREFIX="/opt/openssl-with-min-tls1_2"
    PYTHON_VERSION="3.8.1"
    PYTHON_PREFIX="/opt/python-with-min-tls1_2"


    curl -O "https://www.openssl.org/source/openssl-$OPENSSL_VERSION.tar.gz"
    tar -xzf "openssl-$OPENSSL_VERSION.tar.gz"
    cd openssl-$OPENSSL_VERSION
    ./config --prefix=$OPENSSL_PREFIX no-ssl3 no-tls1 no-tls1_1 no-shared
    make > /dev/null
    sudo make install_sw > /dev/null


    cd /tmp
    curl -O "https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz"
    tar -xzf "Python-$PYTHON_VERSION.tgz"
    cd Python-$PYTHON_VERSION
    ./configure --prefix=$PYTHON_PREFIX --with-openssl=$OPENSSL_PREFIX --disable-shared > /dev/null
    make > /dev/null
    sudo make install > /dev/null


This will compile a version of Python that has a statically linked OpenSSL that will not automatically negotiate anything earlier than TLS 1.2. This will also install OpenSSL in the directory: ``/opt/openssl-with-min-tls1_2`` and install Python in the directory: ``/opt/python-with-min-tls1_2``. 

After you run this script, you should be able to use this newly installed version of Python::

    /opt/python-with-min-tls1_2/bin/python3 --version

This should print out::

    Python 3.8.1

To confirm this new version of Python does not negotiate a version earlier than TLS 1.2, rerun the steps from `Determining Supported Protocols`_ using the newly installed Python version (that is, ``/opt/python-with-min-tls1_2/bin/python3``).
