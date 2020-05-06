===============
Upgrading notes
===============

Notes to refer to when upgrading ``boto3`` versions.

1.9.0
-----

What changed
~~~~~~~~~~~~

The boto3 event system was changed to emit events based on the service id
rather than the endpoint prefix or service name.

Why was the change made
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This was done to handle several issues that were becoming increasingly
problematic:

* Services changing their endpoint prefix would cause some registered events to
  no longer fire (but not all).
* New services that launch using an endpoint that another service is using
  won't be able to be uniquely selected. There are a number of cases of this
  already.
* Services whose client name and endpoint prefix differed would require two
  different strings if you want to register against all events.

How do I know if I'm impacted
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any users relying on registering an event against one service impacting other
services are impacted. You can consult the following table to see if you are
impacted. If you are registering an event using one of the event parts in the
leftmost column with the intention of impacting an unintended target service
in the rightmost column, then you are impacted and will need to update.

+----------------------+-------------------------+---------------------------------------------------+
| Event Part           | Intended Target Service | Unintended Target Services                        |
+----------------------+-------------------------+---------------------------------------------------+
| rds                  | rds                     | neptune                                           |
+----------------------+-------------------------+---------------------------------------------------+
| autoscaling          | autoscaling             | application-autoscaling, autoscaling-plans        |
+----------------------+-------------------------+---------------------------------------------------+
| kinesisvideo         | kinesisvideo            | kinesis-video-media, kinesis-video-archived-media |
+----------------------+-------------------------+---------------------------------------------------+
| elasticloadbalancing | elb                     | elbv2                                             |
+----------------------+-------------------------+---------------------------------------------------+

For example, if you are registering an event against
``before-call.elasticloadbalancing`` expecting it to run when making calls with
an ``elbv2`` client, you will be impacted.

If you are registering an event against one of the services in the Unintended
Targets column, you may be impacted if you were relying on those events not
firing.

If you are registering events using ``*`` in the service place, or are
registering against any service not in this table, you will not need a code
change. In many cases the actual event name will have changed, but for services
without shared endpoints we do the work of translating the event name at
registration and emission time. In future versions of boto3 we will remove
this translation, so you may wish to update your code anyway.

How do I update my code
~~~~~~~~~~~~~~~~~~~~~~~

You will need to look at the events you are registering against and determine
which services you wish to impact with your handler. If you only wish to
impact the intended target service (as defined in the above table), then you
don't need to change the event. If you wish to impact another service in
addition to the intended target service, you will need to register a new event
using that service's event name. Similarly, if you wish to impact another
service instead you will simply need to change the event you are registered
against.

To get the new event name, consult this table:

+------------------------------+----------------------+------------------------------+
| Service                      | Old Event Name       | New Event Name               |
+------------------------------+----------------------+------------------------------+
| application-autoscaling      | autoscaling          | application-auto-scaling     |
+------------------------------+----------------------+------------------------------+
| autoscaling-plans            | autoscaling          | auto-scaling-plans           |
+------------------------------+----------------------+------------------------------+
| elbv2                        | elasticloadbalancing | elastic-load-balancing       |
+------------------------------+----------------------+------------------------------+
| kinesis-video-archived-media | kinesisvideo         | kinesis-video-archived-media |
+------------------------------+----------------------+------------------------------+
| kinesis-video-media          | kinesisvideo         | kinesis-video-media          |
+------------------------------+----------------------+------------------------------+
| neptune                      | rds                  | neptune                      |
+------------------------------+----------------------+------------------------------+

Additionally, you can get the new event name in code like so::

    import boto3

    client = boto3.client('elbv2')
    service_event_name = client.meta.service_model.service_id.hyphenize()

Armed with the service event name, simply replace the old service name in the
handler with the new service event name. If you were registering an event
against ``before-call.autoscaling`` intending to impact ``autoscaling-plans``
for example, you would instead register against
``before-call.auto-scaling-plans``.

If you are registering an event against one of the services in the Unintended
Targets column, you will now see those events getting fired where previously
they were not. While this is enabling that expected behavior, this still
represents a change in actual behavior. You should not need to update your
code, but you should test to ensure that you are seeing the behavior you want.


1.4.2
-----

* The ``use_threads`` option was added to
  :py:class:`boto3.s3.transfer.TransferConfig`.
  Starting in version ``1.4.0``, all managed S3 transfer methods became
  threaded instead of possibly being threaded. If it is not desired to use
  threads for managed S3 transfers, set ``use_threads`` to ``False``.


1.4.0
-----

* Logic from the `s3transfer <https://github.com/boto/s3transfer>`_ package
  was ported into the ``boto3.s3.transfer`` module. In upgrading to this
  new version of ``boto3``, code that relies on the public classes and
  interfaces of ``boto3.s3.transfer``, such as
  :py:class:`boto3.s3.transfer.S3Transfer` and
  :py:class:`boto3.s3.transfer.TransferConfig`, should not be affected.
  However, code that relies on the internal classes and functionality of the
  ``boto3.s3.transfer`` module may be affected in upgrading:

  * Removed internal classes such as ``MultipartUploader``,
    ``MultipartDownloader``, ``ReadFileChunk``, etc. All of the managed
    transfer logic now lives inside of ``s3transfer`` and as a result these
    internal classes are no longer used and is essentially dead code.

  * Custom implementations of ``OSUtils`` may see the
    ``open_file_chunk_reader`` method no longer being called when uploads
    occur. If this was for the purpose of being able to provide file-like
    objects for transfers, use the newly added ``upload_fileobj``
    and ``download_fileobj`` methods that support both nonmultipart and
    multipart transfers.

  * By default, all managed transfer methods are now threaded. In prior
    versions, threads were only created if a non multipart upload or download
    was initiated. To run the managed transfer methods with no threads
    (i.e. all of the transfer logic happens in the main thread), set
    ``use_threads`` to ``False`` when providing a ``TransferConfig`` object.
    The ``use_threads`` option is only available in ``boto3`` versions higher
    than ``1.4.1``.
