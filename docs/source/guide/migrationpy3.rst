.. _guide_migration_py3:

Migrating from Python 2.7 to Python 3
=====================================
Python 2.7 was deprecated by the `Python Software Foundation <https://www.python.org/psf-landing/>`_ back on January 1, 2020 following a multi-year process of phasing it out. Because of this, AWS has deprecated support for Python 2.7, so versions of Boto3 and the AWS CLI v1 released after the deprecation date will no longer work with Python 2.7.

.. note::

    Since the AWS CLI v2 bundles its own copy of Python, this transition only impacts users of the CLI v1.

Timeline
--------
Going forward, all projects using the AWS SDK for Python need to transition to using Python 3, with Python 3.6 becoming the minimum by the end of the transition. The deprecation dates for the affected versions of Python are:

==================     ===================
Python version         Deprecation date
==================     ===================
Python 2.7             July 14, 2021
Python 3.4 and 3.5     February 1, 2021
==================     ===================

As shown in the table, Python 2.7 projects must transition to Python 3.6 by July 14, 2021, while Python 3.4 and 3.5 projects need to be updated to Python 3.6 by February 1, 2021.

Impact on the AWS CLI
---------------------
The AWS Command Line Interface is built using the Python SDK, so it's affected by this transition. AWS CLI v2 isn't affected by this transition, since it bundles its own copy of Python 3. However, if you still use the AWS CLI v1, you need to decide whether to :ref:`upgrade to Python 3 <quickstart_install_python>` or to `transition to the AWS CLI v2 <https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html>`_.

Updating your project to use Python 3
-------------------------------------
Before you begin to update your project and environment, make sure you’ve installed or updated to Python 3.6 or later as described in :ref:`upgrade to Python 3 <quickstart_install_python>`. You can get Python from the `PSF web site <https://www.python.org/downloads>`_ or using your local package manager.

Update the CLI
~~~~~~~~~~~~~~
Updating the CLI to the latest version isn't difficult:

1. To begin, uninstall your existing copy of the AWS CLI using the following command::

    $ python -m pip uninstall awscli

2. Next, use Python 3 to reinstall the AWS CLI. Here, we're using the :command:`python3` command to ensure that Python 3 is used rather than Python 2::

    $ python3 -m pip install awscli

3. If you wish, you may verify that the newly installed copy of the AWS CLI tool, :command:`aws`, is using the correct version of Python. The :command:`aws --version` command reports the :command:`aws` tool's version number, followed by the version of Python it's running under, then the operating system version and the computer's processor family. As long as the Python version is at least 3.6, you're ready to go::

    $ aws --version
    aws-cli/1.18.191 Python/3.6.6 Darwin/19.6.0 botocore/1.19.31

Update Boto3 and Botocore
~~~~~~~~~~~~~~~~~~~~~~~~~
Now that you're sure you have Python 3 installed, you can proceed to upgrade Boto3 and Botocore. You can do this globally, or within your virtual environment if you use one for your project.

1. Begin by uninstalling the currently installed copies of Boto3 and Botocore::

    $ python -m pip uninstall boto3 botocore

2. Then install the new version of Boto3. This will also install Botocore, which it requires::

    $ python3 -m pip install boto3

3. You can optionally verify that the freshly installed copy of the :command:`aws` tool is using the correct version of Python. One way to do that is to run a snippet of code that uses Boto3 and outputs the Python and Boto3 versions, such as the following::

    $ python3 -c "import boto3, sys; print(f'{sys.version} \nBoto3: {boto3.__version__}')"
    3.8.6 (default, Jan  7 2021, 17:11:21)
    [GCC 7.3.1 20180712 (Red Hat 7.3.1-11)]
    Boto3: 1.16.15

If you're unable to upgrade to Python 3
---------------------------------------
It may be possible that you're unable to upgrade to Python 3. If you have a large project that's heavily dependent on syntax or features that no longer work as desired in Python 3, for example, you may need to keep using Python 2.7. It's also possible that you need to postpone the Python transition while you finish updates to your code.

Under these circumstances, you should be prepared for the deprecation date, in order to not be inconvenienced when the time arrives. If you've kept all software up-to-date, you shouldn't need to do anything. If you're using a version of the AWS CLI v1 and/or Boto3 that requires Python 2, you can keep using the version you have after the deprecation date. You should, however, update to the most recent version of the AWS SDK for Python 2 that you can.

.. note::

    Keep in mind that Python 2.7-based versions of Boto3 and the AWS CLI v1 will not receive support for new AWS capabilities after the scheduled deprecation dates.

Upgrade a pip-based install
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is particularly true if you installed the AWS CLI and/or Boto3 using `pip`, since `pip` 10.0 and later will automatically prevent you from installing upgrades to the CLI or Boto3 that wouldn't be compatible with the version of Python you're using.

Since the bundled installer only performs global installs, any virtual environment based projects will likely be using the CLI installed using `pip`.

Windows MSI Installer
~~~~~~~~~~~~~~~~~~~~~
If you installed the AWS CLI v1 using the Windows MSI Installer for Python 3 [`32 bit <https://s3.amazonaws.com/aws-cli/AWSCLI32PY3.msi>`_] [`64 bit <https://s3.amazonaws.com/aws-cli/AWSCLI64PY3.msi>`_], you're not impacted by this transition, since these installers stay up-to-date with each release.

If you're still using the AWS CLI v1 as installed using the Windows MSI Installer for *Python 2*, be aware that after the deprecation date, we will no longer offer these Python 2-based installers, so you may wish to download and save copies now if you believe you need them [`32 bit <https://s3.amazonaws.com/aws-cli/AWSCLI32.msi>`_] [`64 bit <https://s3.amazonaws.com/aws-cli/AWSCLI64.msi>`_].

You can download these installers using the links below.

**For Python 3**

* `Windows MSI Installer for Python 3 (32 bit) <https://s3.amazonaws.com/aws-cli/AWSCLI32PY3.msi>`_
* `Windows MSI Installer for Python 3 (64 bit) <https://s3.amazonaws.com/aws-cli/AWSCLI64PY3.msi>`_

**For Python 2**

* `Windows MSI Installer for Python 2 (32 bit) <https://s3.amazonaws.com/aws-cli/AWSCLI32.msi>`_
* `Windows MSI Installer for Python 2 (64 bit) <https://s3.amazonaws.com/aws-cli/AWSCLI64.msi>`_

Upgrade with the AWS CLI bundled installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you used the AWS CLI bundled installer when you previously installed the AWS CLI v1, and the installed copy of the CLI package doesn't support the Python 2.7 runtime, you need to upgrade to a version that does. You can do this by downloading the installer using the URL `https://s3.amazonaws.com/aws-cli/awscli-bundle-{VERSION}.zip`, where "{VERSION}" is the AWS CLI version you wish to install. For example, you could choose version 1.18.200 using the following command::

    curl https://s3.amazonaws.com/aws-cli/awscli-bundle-1.18.200.zip -o awscli-bundle.zip

Once you've downloaded the bundle, proceed with *step 2* of the bundle-based installation instructions for your platform:

* `Linux <https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html#install-linux-bundled>`_
* `macOS <https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html#install-macosos-bundled-sudo>`_
