.. _guide_migration_py3:

Migrating from Python 2.7 to Python 3
=====================================
Python 2.7 was deprecated back on January 1, 2020 following a multi-year process of phasing it out. Because of this, AWS has deprecated support for Python 2.7, and support for Python 2.7 will be removed from all SDKs before the end of 2021. This includes the AWS SDK for Python and the AWS Command Line Interface (CLI).

This transition also requires transitioning from Boto 2.x to Boto3. See :ref:`Install or upgrade Python <quickstart_install_python>` for details.

.. note::

    Since the AWS CLI v2 bundles its own copy of Python, this transition only impacts users of the version 1 CLI.

Timeline
--------
Going forward, all projects using the AWS SDK for Python need to transition to using Python 3, with Python 3.6 becoming the minimum by the end of the transition. The deprecation dates the affected versions of Python are:

============== ===================
Python version Date of deprecation
============== ===================
Python 2.7     June 1, 2021
Python 3.4     February 1, 2021
Python 3.5     February 1, 2021
============== ===================

As shown in the table, you must transition to Python 3.6 by June 1, 2021, while Python 3.4 and 3.5 projects need to be updated to Python 3.7 by February 1, 2021.

Impact on the AWS CLI
---------------------
The AWS Command Line Interface is built using the Python SDK, so it's affected by this transition. AWS CLI v2 isn't affected by this transition, since it bundles its own copy of Python 3. However, if you still use the AWS CLI v1, you need to decide whether to :ref:`upgrade to Python 3 <quickstart_install_python>` or to `transition to the version 2 CLI <https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html>`_.

Updating your project to use Python 3
-------------------------------------
If your project is currently based on Python 2, you need to begin by ensuring that you're using the latest version of the CLI. If you need to continue to use the version 1 CLI, you may do so, as long as you `update to the newest version of the v1 CLI <https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html>`_.

.. note::

    Before you get started make, sure you’ve updated Python as described in  from the `PSF <https://www.python.org/downloads>`_ or your local package manager.

Update the CLI
~~~~~~~~~~~~~~
First, upgrade to the latest version of the AWS CLI v1.

1. To begin, uninstall your existing copy of the AWS CLI using the following command::

    $ python -m pip uninstall awscli

2. Next, use Python 3 to reinstall the AWS CLI. Here, we're using the :command:`python3` command to ensure that Python 3 is used rather than Python 2::

    $ python3 -m pip install awscli

3. If you wish, you may verify that the newly installed copy of the AWS CLI tool, :command:`aws`, is using the correct version of Python. The :command:`aws --version` command reports the :command:`aws` tool's version number, followed by the version of Python it's running under, then the operating system version and the computer's processor family. As long as the Python version is at least 3.6, you're ready to go::

    $ aws --version
    aws-cli/2.0.61 *Python/3.7.4* Darwin/19.6.0 exe/x86_64

Update Boto3 and Botocore
~~~~~~~~~~~~~~~~~~~~~~~~~
Now that you're sure you have Python 3 installed and you've updated the CLI (if needed), you can proceed to upgrade Boto3 and Botocore. You can do this globally, or within your virtual environment if you use one for your project.

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

Under these circumstances, you should be prepared for the deprecation date, in order to not be inconvenienced when the time arrives. If you've kept all software up-to-date, you shouldn't need to do anything. If you're using the a version of the AWS CLI v1 and/or Boto3 that requires Python 2, the version you have will keep working as long as you're on Python 2.

.. note::

    Keep in mind that Python 2.7-based versions of Boto3 and the AWS CLI v1 will not receive support for new AWS capabilities after the scheduled deprecation dates. Its also worth noting that by 2023, all operating systems on which Python can be installed will have ended support for Python 2.7. This means you'll probably have to complete the Python 3 transition eventually.

Upgrade a pip-based install
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is particularly true if you installed the AWS CLI and/or Boto3 using `pip`, since `pip` 10.0 and later will automatically prevent you from installing upgrades to the CLI or Boto3 that wouldn't be compatible with the version of Python you're using.

Since the bundled installer only performs global installs, any virtual environment based projects will likely be using the CLI installed using `pip`.

Upgrade with the AWS CLI bundled installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you used the AWS CLI bundled installer when you previously installed the AWS CLI v1, and the installed copy of the CLI package doesn't support the Python 2.7 runtime, you need to upgrade to a version that does. You can do this by downloading the installer using the URL `https://s3.amazonaws.com/aws-cli/awscli-bundle-{VERSION}.zip`, where "{VERSION}" is the AWS CLI version you wish to install. For example, you could choose version 1.18.50 using the following command::

    curl https://s3.amazonaws.com/aws-cli/awscli-bundle-1.18.50.zip -o awscli-bundle.zip

Once you've downloaded the bundle, proceed with *step 2* of the bundle-based installation instructions for your platform:

* `Linux <https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html#install-linux-bundled>`_
* `macOS <https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html#install-macosos-bundled-sudo>`_
* `Windows <https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html#msi-on-windows>`_
