.. _guide_migration_py3:

Migrating from Python 2.7 to Python 3
=====================================
Python 2.7 was deprecated by the `Python Software Foundation <https://www.python.org/psf-landing/>`_ back on January 1, 2020 following a multi-year process of phasing it out. Because of this, AWS has deprecated support for Python 2.7, so versions of boto3 and botocore released after the deprecation date will no longer work with Python 2.7.

Timeline
--------
Going forward, all projects using the AWS SDK for Python need to transition to using Python 3, with Python 3.6 becoming the minimum by the end of the transition. The deprecation dates for the affected versions of Python are:

==================     ===================
Python version         Deprecation date
==================     ===================
Python 2.7             July 15, 2021
Python 3.4 and 3.5     February 1, 2021
==================     ===================

As shown in the table, Python 2.7 projects must transition to Python 3.6 by July 15, 2021, while Python 3.4 and 3.5 projects need to be updated to Python 3.6 by February 1, 2021.

Updating your project to use Python 3
-------------------------------------
Before you begin to update your project and environment, make sure you’ve installed or updated to Python 3.6 or later as described in :ref:`upgrade to Python 3 <quickstart_install_python>`. You can get Python from the `PSF web site <https://www.python.org/downloads>`_ or using your local package manager.

Update boto3 and botocore
~~~~~~~~~~~~~~~~~~~~~~~~~
Once you're sure you have Python 3 installed, you can proceed to upgrade boto3 and botocore. You can do this globally, or within your virtual environment if you use one for your project.

1. Begin by uninstalling the currently installed copies of boto3 and botocore::

    $ python -m pip uninstall boto3 botocore

2. Then install the new version of boto3. This will also install botocore, which it requires::

    $ python3 -m pip install boto3

3. You can optionally verify that the freshly installed copy of Boto3 is using the correct version of Python. One way to do that is to run a snippet of code that uses boto3 and outputs the Python and boto3 versions, such as the following::

    $ python3 -c "import boto3, sys; print(f'{sys.version} \nboto3: {boto3.__version__}')"
    3.8.6 (default, Jan  7 2021, 17:11:21)
    [GCC 7.3.1 20180712 (Red Hat 7.3.1-11)]
    boto3: 1.16.15

If you're unable to upgrade to Python 3
---------------------------------------
It may be possible that you're unable to upgrade to Python 3. If you have a large project that's heavily dependent on syntax or features that no longer work as desired in Python 3, for example, you may need to keep using Python 2.7. It's also possible that you need to postpone the Python transition while you finish updates to your code.

Under these circumstances, you should be prepared for the deprecation date in order to not be inconvenienced when the time arrives. If you've kept all software up-to-date, you shouldn't need to do anything. If you're using an existing installation of boto3 on Python 2, you can keep using it even after the deprecation date. That version of boto3, however, will not receive further feature or security updates, so you should consider migrating to Python 3 as soon as possible.

pip-based installations
~~~~~~~~~~~~~~~~~~~~~~~
If you installed boto3 using :command:`pip` 10.0 or later, you'll automatically stop receiving boto3 updates after the last Python 2 compatible version of boto3 is installed. If you're using an older version of :command:`pip`, you need to pin your boto3 install to no later than version 1.17.

Other installation methods
~~~~~~~~~~~~~~~~~~~~~~~~~~
If install boto3 from source or using any other approach, be sure you download and install a version released prior to the Python 2.7 deprecation date.
