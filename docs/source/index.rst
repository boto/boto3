.. Boto3 documentation master file, created by
   sphinx-quickstart on Wed Sep  3 11:11:30 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Boto 3 Documentation
====================
Boto is the Amazon Web Services (AWS) SDK for Python, which allows Python
developers to write software that makes use of Amazon services like S3 and
EC2. Boto provides an easy to use, object-oriented API as well as low-level
direct service access.

.. danger::

   Boto 3 is *highly experimental* and **should not** be used in production
   yet. Consider yourself warned!

Installation
------------
Install the latest Boto 3 release via :command:`pip`::

    pip install boto3

You may also install a specific version::

    pip install boto3==1.0.0

The latest development version can always be found on
`GitHub <https://github.com/boto/boto3>`_.

Tutorials
---------

.. toctree::
   :maxdepth: 2

   tutorial/sqs

Design Documentation
--------------------

.. toctree::
   :maxdepth: 2

   design/architecture
   design/resources

API References
--------------

Services
~~~~~~~~

* Coming soon

Core
~~~~

.. toctree::
   :maxdepth: 2
   :glob:

   reference/core/*

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
