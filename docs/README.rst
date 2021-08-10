Boto3 Documentation
~~~~~~~~~~~~~~~~~~~
Documentation for boto3 can be found `here <https://boto3.amazonaws.com/v1/documentation/api/latest/index.html>`_.

Generating Documentation
~~~~~~~~~~~~~~~~~~~~~~~~
Note: `Botocore's <https://github.com/boto/botocore>`_ requirement-docs.txt must be installed prior to attempting the following steps.

Sphinx is used for documentation. You can generate HTML locally with the
following:

.. code-block:: sh

    $ pip install -r requirements-docs.txt
    $ cd docs
    $ make html
