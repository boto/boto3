.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-boto3-kms-examples-encrypt-decrypt-file:

**************************
Encrypt and decrypt a file
**************************

The example program uses AWS KMS keys to encrypt and decrypt a file.

A master key, also called a Customer Master Key or CMK, is created and used to generate a data key. 
The data key is then used to encrypt a disk file. The encrypted data key is stored within 
the encrypted file. To decrypt the file, the data key is decrypted and then used to decrypt 
the rest of the file. This manner of using master and data keys is called envelope encryption.

To encrypt and decrypt data, the example uses the well-known Python ``cryptography`` package. 
This package is not part of the Python standard library and must be installed separately, for
example, with the ``pip`` command.

::

    pip install cryptography

Each section describes a single function from the example's `entire
source file <https://github.com/awsdocs/aws-doc-sdk-examples/tree/master/python/example_code/kms/encrypt_decrypt_file.py>`_.


Retrieve an existing master key
===============================

Master keys are created, managed, and stored within AWS KMS. A KMS master key is also referred to 
as a customer master key or CMK. An AWS storage cost is incurred for each CMK, therefore, one CMK is 
often used to manage multiple data keys.

The example ``retrieve_cmk`` function searches for an existing CMK. A key description is specified 
when a CMK is created, and this description is used to identify and retrieve the desired key. If 
many CMKs exist, they are processed in batches until either the desired key is found or all keys are
examined.

If the example function finds the desired CMK, it returns both the CMK's ID and its ARN (Amazon 
Resource Name). Either of these identifiers can be used to reference the CMK in subsequent calls 
to AWS KMS methods.

.. code-block:: python

    def retrieve_cmk(desc):
        """Retrieve an existing KMS CMK based on its description

        :param desc: Description of CMK specified when the CMK was created
        :return Tuple(KeyId, KeyArn) where:
            KeyId: CMK ID
            KeyArn: Amazon Resource Name of CMK
        :return Tuple(None, None) if a CMK with the specified description was
        not found
        """

        # Retrieve a list of existing CMKs
        # If more than 100 keys exist, retrieve and process them in batches
        kms_client = boto3.client('kms')
        try:
            response = kms_client.list_keys()
        except ClientError as e:
            logging.error(e)
            return None, None

        done = False
        while not done:
            for cmk in response['Keys']:
                # Get info about the key, including its description
                try:
                    key_info = kms_client.describe_key(KeyId=cmk['KeyArn'])
                except ClientError as e:
                    logging.error(e)
                    return None, None

                # Is this the key we're looking for?
                if key_info['KeyMetadata']['Description'] == desc:
                    return cmk['KeyId'], cmk['KeyArn']

            # Are there more keys to retrieve?
            if not response['Truncated']:
                # No, the CMK was not found
                logging.debug('A CMK with the specified description was not found')
                done = True
            else:
                # Yes, retrieve another batch
                try:
                    response = kms_client.list_keys(Marker=response['NextMarker'])
                except ClientError as e:
                    logging.error(e)
                    return None, None

        # All existing CMKs were checked and the desired key was not found
        return None, None


Create a customer master key
============================

If the example does not find an existing CMK, it creates a new one and returns its ID and ARN.

.. code-block:: python

    def create_cmk(desc='Customer Master Key'):
        """Create a KMS Customer Master Key

        The created CMK is a Customer-managed key stored in AWS KMS.

        :param desc: key description
        :return Tuple(KeyId, KeyArn) where:
            KeyId: AWS globally-unique string ID
            KeyArn: Amazon Resource Name of the CMK
        :return Tuple(None, None) if error
        """

        # Create CMK
        kms_client = boto3.client('kms')
        try:
            response = kms_client.create_key(Description=desc)
        except ClientError as e:
            logging.error(e)
            return None, None

        # Return the key ID and ARN
        return response['KeyMetadata']['KeyId'], response['KeyMetadata']['Arn']


Create a data key
=================

To encrypt a file, the example ``create_data_key`` function creates a data key. The data key is 
customer managed and does not incur an AWS storage cost. The example creates a data key for 
each file it encrypts, but it's possible to use a single data key to encrypt multiple files.

The example function returns the data key in both its plaintext and encrypted forms. The 
plaintext form is used to encrypt the data. The encrypted form will be stored with the encrypted 
file. The data key is associated with a CMK which is capable of decrypting the encrypted data key 
when necessary.


.. code-block:: python

    def create_data_key(cmk_id, key_spec='AES_256'):
        """Generate a data key to use when encrypting and decrypting data

        :param cmk_id: KMS CMK ID or ARN under which to generate and encrypt the
        data key.
        :param key_spec: Length of the data encryption key. Supported values:
            'AES_128': Generate a 128-bit symmetric key
            'AES_256': Generate a 256-bit symmetric key
        :return Tuple(EncryptedDataKey, PlaintextDataKey) where:
            EncryptedDataKey: Encrypted CiphertextBlob data key as binary string
            PlaintextDataKey: Plaintext base64-encoded data key as binary string
        :return Tuple(None, None) if error
        """

        # Create data key
        kms_client = boto3.client('kms')
        try:
            response = kms_client.generate_data_key(KeyId=cmk_id, KeySpec=key_spec)
        except ClientError as e:
            logging.error(e)
            return None, None

        # Return the encrypted and plaintext data key
        return response['CiphertextBlob'], base64.b64encode(response['Plaintext'])


Encrypt a file
==============

The ``encrypt_file`` function creates a data key and uses it to encrypt the contents of a disk file.

The encryption operation is performed by a ``Fernet`` object created by the Python ``cryptography`` 
package.

The encrypted form of the data key is saved within the encrypted file and will be used in the future 
to decrypt the file. The encrypted file can be decrypted by any program with the credentials to 
decrypt the encrypted data key.

.. code-block:: python

    def encrypt_file(filename, cmk_id):
        """Encrypt a file using an AWS KMS CMK

        A data key is generated and associated with the CMK.
        The encrypted data key is saved with the encrypted file. This enables the
        file to be decrypted at any time in the future and by any program that
        has the credentials to decrypt the data key.
        The encrypted file is saved to <filename>.encrypted
        Limitation: The contents of filename must fit in memory.

        :param filename: File to encrypt
        :param cmk_id: AWS KMS CMK ID or ARN
        :return: True if file was encrypted. Otherwise, False.
        """

        # Read the entire file into memory
        try:
            with open(filename, 'rb') as file:
                file_contents = file.read()
        except IOError as e:
            logging.error(e)
            return False

        # Generate a data key associated with the CMK
        # The data key is used to encrypt the file. Each file can use its own
        # data key or data keys can be shared among files.
        # Specify either the CMK ID or ARN
        data_key_encrypted, data_key_plaintext = create_data_key(cmk_id)
        if data_key_encrypted is None:
            return False
        logging.info('Created new AWS KMS data key')

        # Encrypt the file
        f = Fernet(data_key_plaintext)
        file_contents_encrypted = f.encrypt(file_contents)

        # Write the encrypted data key and encrypted file contents together
        try:
            with open(filename + '.encrypted', 'wb') as file_encrypted:
                file_encrypted.write(len(data_key_encrypted).to_bytes(NUM_BYTES_FOR_LEN,
                                                                      byteorder='big'))
                file_encrypted.write(data_key_encrypted)
                file_encrypted.write(file_contents_encrypted)
        except IOError as e:
            logging.error(e)
            return False

        # For the highest security, the data_key_plaintext value should be wiped
        # from memory. Unfortunately, this is not possible in Python. However,
        # storing the value in a local variable makes it available for garbage
        # collection.
        return True


Decrypt a data key
==================

To decrypt an encrypted file, the encrypted data key used to perform the encryption must first
be decrypted. This operation is performed by the example ``decrypt_data_key`` function which returns
the plaintext form of the key.

.. code-block:: python

    def decrypt_data_key(data_key_encrypted):
        """Decrypt an encrypted data key

        :param data_key_encrypted: Encrypted ciphertext data key.
        :return Plaintext base64-encoded binary data key as binary string
        :return None if error
        """

        # Decrypt the data key
        kms_client = boto3.client('kms')
        try:
            response = kms_client.decrypt(CiphertextBlob=data_key_encrypted)
        except ClientError as e:
            logging.error(e)
            return None

        # Return plaintext base64-encoded binary data key
        return base64.b64encode((response['Plaintext']))


Decrypt a file
==============

The example ``decrypt_file`` function first extracts the encrypted data key from the encrypted file. It 
then decrypts the key to get its plaintext form and uses that to decrypt the file contents.

The decryption operation is performed by a ``Fernet`` object created by the Python ``cryptography`` 
package.

.. code-block:: python

    def decrypt_file(filename):
        """Decrypt a file encrypted by encrypt_file()

        The encrypted file is read from <filename>.encrypted
        The decrypted file is written to <filename>.decrypted

        :param filename: File to decrypt
        :return: True if file was decrypted. Otherwise, False.
        """

        # Read the encrypted file into memory
        try:
            with open(filename + '.encrypted', 'rb') as file:
                file_contents = file.read()
        except IOError as e:
            logging.error(e)
            return False

        # The first NUM_BYTES_FOR_LEN bytes contain the integer length of the
        # encrypted data key.
        # Add NUM_BYTES_FOR_LEN to get index of end of encrypted data key/start
        # of encrypted data.
        data_key_encrypted_len = int.from_bytes(file_contents[:NUM_BYTES_FOR_LEN],
                                                byteorder='big') \
                                 + NUM_BYTES_FOR_LEN
        data_key_encrypted = file_contents[NUM_BYTES_FOR_LEN:data_key_encrypted_len]

        # Decrypt the data key before using it
        data_key_plaintext = decrypt_data_key(data_key_encrypted)
        if data_key_plaintext is None:
            return False

        # Decrypt the rest of the file
        f = Fernet(data_key_plaintext)
        file_contents_decrypted = f.decrypt(file_contents[data_key_encrypted_len:])

        # Write the decrypted file contents
        try:
            with open(filename + '.decrypted', 'wb') as file_decrypted:
                file_decrypted.write(file_contents_decrypted)
        except IOError as e:
            logging.error(e)
            return False

        # The same security issue described at the end of encrypt_file() exists
        # here, too, i.e., the wish to wipe the data_key_plaintext value from
        # memory.
        return True
