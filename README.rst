===============================
Boto3 - The AWS SDK for Python
===============================

|Version| |Gitter|

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for
Python, which allows Python developers to write software that makes use
of services like Amazon S3 and Amazon EC2. You can find the latest, most
up to date, documentation at our `doc site`_, including a list of
services that are supported.

On 01/15/2021 deprecation for Python 2.7 was announced and support will be dropped
on 07/15/2021. To avoid disruption, customers using Boto3 on Python 2.7 may
need to upgrade their version of Python or pin the version of Boto3. For
more information, see this `blog post <https://aws.amazon.com/blogs/developer/announcing-end-of-support-for-python-2-7-in-aws-sdk-for-python-and-aws-cli-v1/>`__.


.. _boto: https://docs.pythonboto.org/
.. _`doc site`: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
.. |Gitter| image:: https://badges.gitter.im/boto/boto3.svg
   :target: https://gitter.im/boto/boto3
   :alt: Gitter
.. |Downloads| image:: http://img.shields.io/pypi/dm/boto3.svg?style=flat
    :target: https://pypi.python.org/pypi/boto3/
    :alt: Downloads
.. |Version| image:: http://img.shields.io/pypi/v/boto3.svg?style=flat
    :target: https://pypi.python.org/pypi/boto3/
    :alt: Version
.. |License| image:: http://img.shields.io/pypi/l/boto3.svg?style=flat
    :target: https://github.com/boto/boto3/blob/develop/LICENSE
    :alt: License

Getting Started
---------------
Assuming that you have Python and ``virtualenv`` installed, set up your environment and install the required dependencies like this or you can install the library using ``pip``:

.. code-block:: sh

    $ git clone https://github.com/boto/boto3.git
    $ cd boto3
    $ virtualenv venv
    ...
    $ . venv/bin/activate
    $ python -m pip install -r requirements.txt
    $ python -m pip install -e .

.. code-block:: sh

    $ python -m pip install boto3

    
Using Boto3
~~~~~~~~~~~~~~
After installing boto3 

Next, set up credentials (in e.g. ``~/.aws/credentials``):

.. code-block:: ini

    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET

Then, set up a default region (in e.g. ``~/.aws/config``):

.. code-block:: ini

   [default]
   region=us-east-1
    
Other credentials configuration method can be found `here <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>`__

Then, from a Python interpreter:

.. code-block:: python

    >>> import boto3
    >>> s3 = boto3.resource('s3')
    >>> for bucket in s3.buckets.all():
            print(bucket.name)

Running Tests
~~~~~~~~~~~~~
You can run tests in all supported Python versions using ``tox``. By default,
it will run all of the unit and functional tests, but you can also specify your own
``nosetests`` options. Note that this requires that you have all supported
versions of Python installed, otherwise you must pass ``-e`` or run the
``nosetests`` command directly:

.. code-block:: sh

    $ tox
    $ tox -- unit/test_session.py
    $ tox -e py26,py33 -- integration/

You can also run individual tests with your default Python version:

.. code-block:: sh

    $ nosetests tests/unit


Getting Help
------------

We use GitHub issues for tracking bugs and feature requests and have limited
bandwidth to address them. Please use these community resources for getting
help:

* Ask a question on `Stack Overflow <https://stackoverflow.com/>`__ and tag it with `boto3 <https://stackoverflow.com/questions/tagged/boto3>`__
* Come join the AWS Python community chat on `gitter <https://gitter.im/boto/boto3>`__
* Open a support ticket with `AWS Support <https://console.aws.amazon.com/support/home#/>`__
* If it turns out that you may have found a bug, please `open an issue <https://github.com/boto/boto3/issues/new>`__


Contributing
------------

We value feedback and contributions from our community. Whether it's a bug report, new feature, correction, or additional documentation, we welcome your issues and pull requests. Please read through this `CONTRIBUTING <https://github.com/boto/boto3/blob/develop/CONTRIBUTING.rst>`__ document before submitting any issues or pull requests to ensure we have all the necessary information to effectively respond to your contribution.


Maintenance and Support for SDK Major Versions
----------------------------------------------

Boto3 was made generally available on 06/22/2015 and is currently in the full support phase of the availability life cycle.

For information about maintenance and support for SDK major versions and their underlying dependencies, see the following in the AWS SDKs and Tools Shared Configuration and Credentials Reference Guide:

* `AWS SDKs and Tools Maintenance Policy <https://docs.aws.amazon.com/credref/latest/refdocs/maint-policy.html>`__
* `AWS SDKs and Tools Version Support Matrix <https://docs.aws.amazon.com/credref/latest/refdocs/version-support-matrix.html>`__


More Resources
--------------

* `NOTICE <https://github.com/boto/boto3/blob/develop/NOTICE>`__
* `Changelog <https://github.com/boto/boto3/blob/develop/CHANGELOG.rst>`__
* `License <https://github.com/boto/boto3/blob/develop/LICENSE>`__

