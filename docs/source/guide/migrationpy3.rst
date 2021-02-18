.. _guide_migration_py3:

Migrating to Python 3
=====================

Python 2.7 was deprecated by the `Python Software Foundation <https://www.python.org/psf-landing/>`_
on January 1, 2020 following a multi-year process of phasing it out. Because of this, AWS has
deprecated support for Python 2.7, which means that releases of Boto3 issued after the deprecation
date will no longer work on Python 2.7.

This affects both modules that comprise the AWS SDK for Python: Botocore (the underlying low-level
module) and Boto3 (which implements the API functionality and higher-level features).

Timeline
--------
Going forward, all projects using Boto3 need to transition to Python 3.6 or later. Boto3 and
Botocore support for Python 3.4 and 3.5 has already ended, and support for Python 2.7 will end effective July 15, 2021.

Updating your project to use Python 3
-------------------------------------

Before you begin to update your project and environment, make sure you’ve installed or updated to
Python 3.6 or later as described in :ref:`upgrade to Python 3 <quickstart_install_python>`. You can
get Python from the `PSF web site <https://www.python.org/downloads>`_ or using your local package
manager.

After you have installed Python 3, you can upgrade the SDK. To do so, you need to update the Boto3
Python package. You can do this globally or within your virtual environment if you use one for your
project.

To update the AWS SDK for Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Uninstall the currently installed copies of Boto3 and Botocore::

    $ python -m pip uninstall boto3 botocore

2. Install the new version of Boto3. This will also install Botocore, which it requires::

    $ python3 -m pip install boto3

3. (Optional) Verify that the SDK is using the correct version of Python::

    $ python3 -c "import boto3, sys; print(f'{sys.version} \nboto3: {boto3.__version__}')"
    3.8.6 (default, Jan  7 2021, 17:11:21)
    [GCC 7.3.1 20180712 (Red Hat 7.3.1-11)]
    boto3: 1.16.15

If you're unable to upgrade to Python 3
---------------------------------------

It may be that you're unable to upgrade to Python 3, for example if you have a large project that's
heavily dependent on syntax or features that no longer work as desired in Python 3. It's also
possible that you need to postpone the Python transition while you finish updates to your code.

Under these circumstances, you should plan on pinning your project's install of Boto3 to the last
release that supports the Python version you use, then not updating Boto3 further. You can then keep
using an existing installation of Boto3 on Python 2, even after its deprecation date, with the
understanding that deprecated versions of Boto3 will not receive further feature or security
updates.

pip-based installations
~~~~~~~~~~~~~~~~~~~~~~~

If you installed Boto3 using :command:`pip` 10.0 or later, you'll automatically stop receiving Boto3
updates after the last Python 2 compatible version of the SDK is installed. If you're using an older
version of :command:`pip`, you need to pin your Boto3 install to no later than version 1.17.

Other installation methods
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you installed Boto3 and Botocore from source or by any other method, be sure to download and
install a version released prior to the Python 2.7 deprecation date.
