===============
Upgrading Notes
===============

1.4.0
=====

* Logic from the ``s3transfer`` package was ported into ``boto3.s3.transfer``
  module. In upgrading to this new version of ``boto3``, code that relies on
  the public classes and interfaces of ``boto3.s3.transfer``, such as
   ``S3Transfer`` and ``TransferConfig``, should not be affected. However,
  code that relies on the internal classes and functionality of the
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
