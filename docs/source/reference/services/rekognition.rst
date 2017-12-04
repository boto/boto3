

***********
Rekognition
***********

.. contents:: Table of Contents
   :depth: 2


======
Client
======



.. py:class:: Rekognition.Client

  A low-level client representing Amazon Rekognition::

    
    import boto3
    
    client = boto3.client('rekognition')

  
  These are the available methods:
  
  *   :py:meth:`~Rekognition.Client.can_paginate`

  
  *   :py:meth:`~Rekognition.Client.compare_faces`

  
  *   :py:meth:`~Rekognition.Client.create_collection`

  
  *   :py:meth:`~Rekognition.Client.create_stream_processor`

  
  *   :py:meth:`~Rekognition.Client.delete_collection`

  
  *   :py:meth:`~Rekognition.Client.delete_faces`

  
  *   :py:meth:`~Rekognition.Client.delete_stream_processor`

  
  *   :py:meth:`~Rekognition.Client.describe_stream_processor`

  
  *   :py:meth:`~Rekognition.Client.detect_faces`

  
  *   :py:meth:`~Rekognition.Client.detect_labels`

  
  *   :py:meth:`~Rekognition.Client.detect_moderation_labels`

  
  *   :py:meth:`~Rekognition.Client.detect_text`

  
  *   :py:meth:`~Rekognition.Client.generate_presigned_url`

  
  *   :py:meth:`~Rekognition.Client.get_celebrity_info`

  
  *   :py:meth:`~Rekognition.Client.get_celebrity_recognition`

  
  *   :py:meth:`~Rekognition.Client.get_content_moderation`

  
  *   :py:meth:`~Rekognition.Client.get_face_detection`

  
  *   :py:meth:`~Rekognition.Client.get_face_search`

  
  *   :py:meth:`~Rekognition.Client.get_label_detection`

  
  *   :py:meth:`~Rekognition.Client.get_paginator`

  
  *   :py:meth:`~Rekognition.Client.get_person_tracking`

  
  *   :py:meth:`~Rekognition.Client.get_waiter`

  
  *   :py:meth:`~Rekognition.Client.index_faces`

  
  *   :py:meth:`~Rekognition.Client.list_collections`

  
  *   :py:meth:`~Rekognition.Client.list_faces`

  
  *   :py:meth:`~Rekognition.Client.list_stream_processors`

  
  *   :py:meth:`~Rekognition.Client.recognize_celebrities`

  
  *   :py:meth:`~Rekognition.Client.search_faces`

  
  *   :py:meth:`~Rekognition.Client.search_faces_by_image`

  
  *   :py:meth:`~Rekognition.Client.start_celebrity_recognition`

  
  *   :py:meth:`~Rekognition.Client.start_content_moderation`

  
  *   :py:meth:`~Rekognition.Client.start_face_detection`

  
  *   :py:meth:`~Rekognition.Client.start_face_search`

  
  *   :py:meth:`~Rekognition.Client.start_label_detection`

  
  *   :py:meth:`~Rekognition.Client.start_person_tracking`

  
  *   :py:meth:`~Rekognition.Client.start_stream_processor`

  
  *   :py:meth:`~Rekognition.Client.stop_stream_processor`

  

  .. py:method:: can_paginate(operation_name)

        
    Check if an operation can be paginated.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :return: ``True`` if the operation can be paginated,
        ``False`` otherwise.


  .. py:method:: compare_faces(**kwargs)

    

    Compares a face in the *source* input image with each of the 100 largest faces detected in the *target* input image. 

     

    .. note::

       

      If the source image contains multiple faces, the service detects the largest face and compares it with each face detected in the target image. 

       

     

    You pass the input and target images either as base64-encoded image bytes or as a references to images in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    In response, the operation returns an array of face matches ordered by similarity score in descending order. For each face match, the response provides a bounding box of the face, facial landmarks, pose details (pitch, role, and yaw), quality (brightness and sharpness), and confidence value (indicating the level of confidence that the bounding box contains a face). The response also provides a similarity score, which indicates how closely the faces match. 

     

    .. note::

       

      By default, only faces with a similarity score of greater than or equal to 80% are returned in the response. You can change this value by specifying the ``SimilarityThreshold`` parameter.

       

     

     ``CompareFaces`` also returns an array of faces that don't match the source image. For each face, it returns a bounding box, confidence value, landmarks, pose details, and quality. The response also returns information about the face in the source image, including the bounding box of the face and confidence value.

     

    If the image doesn't contain Exif metadata, ``CompareFaces`` returns orientation information for the source and target images. Use these values to display the images with the correct image orientation.

     

    If no faces are detected in the source or target images, ``CompareFaces`` returns an ``InvalidParameterException`` error. 

     

    .. note::

       

      This is a stateless API operation. That is, data returned by this operation doesn't persist.

       

     

    For an example, see  faces-compare-images .

     

    This operation requires permissions to perform the ``rekognition:CompareFaces`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CompareFaces>`_    


    **Request Syntax** 
    ::

      response = client.compare_faces(
          SourceImage={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          TargetImage={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          SimilarityThreshold=...
      )
    :type SourceImage: dict
    :param SourceImage: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type TargetImage: dict
    :param TargetImage: **[REQUIRED]** 

      The target image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type SimilarityThreshold: float
    :param SimilarityThreshold: 

      The minimum level of confidence in the face matches that a match must meet to be included in the ``FaceMatches`` array.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SourceImageFace': {
                'BoundingBox': {
                    'Width': ...,
                    'Height': ...,
                    'Left': ...,
                    'Top': ...
                },
                'Confidence': ...
            },
            'FaceMatches': [
                {
                    'Similarity': ...,
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...,
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        }
                    }
                },
            ],
            'UnmatchedFaces': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...,
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    }
                },
            ],
            'SourceImageOrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
            'TargetImageOrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SourceImageFace** *(dict) --* 

          The face in the source image that was used for comparison.

          
          

          - **BoundingBox** *(dict) --* 

            Bounding box of the face.

            
            

            - **Width** *(float) --* 

              Width of the bounding box as a ratio of the overall image width.

              
            

            - **Height** *(float) --* 

              Height of the bounding box as a ratio of the overall image height.

              
            

            - **Left** *(float) --* 

              Left coordinate of the bounding box as a ratio of overall image width.

              
            

            - **Top** *(float) --* 

              Top coordinate of the bounding box as a ratio of overall image height.

              
        
          

          - **Confidence** *(float) --* 

            Confidence level that the selected bounding box contains a face.

            
      
        

        - **FaceMatches** *(list) --* 

          An array of faces in the target image that match the source image face. Each ``CompareFacesMatch`` object provides the bounding box, the confidence level that the bounding box contains a face, and the similarity score for the face in the bounding box and the face in the source image.

          
          

          - *(dict) --* 

            Provides information about a face in a target image that matches the source image face analysed by ``CompareFaces`` . The ``Face`` property contains the bounding box of the face in the target image. The ``Similarity`` property is the confidence that the source image face matches the face in the bounding box.

            
            

            - **Similarity** *(float) --* 

              Level of confidence that the faces match.

              
            

            - **Face** *(dict) --* 

              Provides face metadata (bounding box and confidence that the bounding box actually contains a face).

              
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Confidence** *(float) --* 

                Level of confidence that what the bounding box contains is a face.

                
              

              - **Landmarks** *(list) --* 

                An array of facial landmarks.

                
                

                - *(dict) --* 

                  Indicates the location of the landmark on the face.

                  
                  

                  - **Type** *(string) --* 

                    Type of the landmark.

                    
                  

                  - **X** *(float) --* 

                    x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                    
                  

                  - **Y** *(float) --* 

                    y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    
              
            
              

              - **Pose** *(dict) --* 

                Indicates the pose of the face as determined by its pitch, roll, and yaw.

                
                

                - **Roll** *(float) --* 

                  Value representing the face rotation on the roll axis.

                  
                

                - **Yaw** *(float) --* 

                  Value representing the face rotation on the yaw axis.

                  
                

                - **Pitch** *(float) --* 

                  Value representing the face rotation on the pitch axis.

                  
            
              

              - **Quality** *(dict) --* 

                Identifies face image brightness and sharpness. 

                
                

                - **Brightness** *(float) --* 

                  Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                  
                

                - **Sharpness** *(float) --* 

                  Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                  
            
          
        
      
        

        - **UnmatchedFaces** *(list) --* 

          An array of faces in the target image that did not match the source image face.

          
          

          - *(dict) --* 

            Provides face metadata for target image faces that are analysed by ``CompareFaces`` and ``RecognizeCelebrities`` .

            
            

            - **BoundingBox** *(dict) --* 

              Bounding box of the face.

              
              

              - **Width** *(float) --* 

                Width of the bounding box as a ratio of the overall image width.

                
              

              - **Height** *(float) --* 

                Height of the bounding box as a ratio of the overall image height.

                
              

              - **Left** *(float) --* 

                Left coordinate of the bounding box as a ratio of overall image width.

                
              

              - **Top** *(float) --* 

                Top coordinate of the bounding box as a ratio of overall image height.

                
          
            

            - **Confidence** *(float) --* 

              Level of confidence that what the bounding box contains is a face.

              
            

            - **Landmarks** *(list) --* 

              An array of facial landmarks.

              
              

              - *(dict) --* 

                Indicates the location of the landmark on the face.

                
                

                - **Type** *(string) --* 

                  Type of the landmark.

                  
                

                - **X** *(float) --* 

                  x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                  
                

                - **Y** *(float) --* 

                  y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  
            
          
            

            - **Pose** *(dict) --* 

              Indicates the pose of the face as determined by its pitch, roll, and yaw.

              
              

              - **Roll** *(float) --* 

                Value representing the face rotation on the roll axis.

                
              

              - **Yaw** *(float) --* 

                Value representing the face rotation on the yaw axis.

                
              

              - **Pitch** *(float) --* 

                Value representing the face rotation on the pitch axis.

                
          
            

            - **Quality** *(dict) --* 

              Identifies face image brightness and sharpness. 

              
              

              - **Brightness** *(float) --* 

                Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                
              

              - **Sharpness** *(float) --* 

                Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                
          
        
      
        

        - **SourceImageOrientationCorrection** *(string) --* 

          The orientation of the source image (counterclockwise direction). If your application displays the source image, you can use this value to correct image orientation. The bounding box coordinates returned in ``SourceImageFace`` represent the location of the face before the image orientation is corrected. 

           

          .. note::

             

            If the source image is in .jpeg format, it might contain exchangeable image (Exif) metadata that includes the image's orientation. If the Exif metadata for the source image populates the orientation field, the value of ``OrientationCorrection`` is null and the ``SourceImageFace`` bounding box coordinates represent the location of the face after Exif metadata is used to correct the orientation. Images in .png format don't contain Exif metadata.

             

          
        

        - **TargetImageOrientationCorrection** *(string) --* 

          The orientation of the target image (in counterclockwise direction). If your application displays the target image, you can use this value to correct the orientation of the image. The bounding box coordinates returned in ``FaceMatches`` and ``UnmatchedFaces`` represent face locations before the image orientation is corrected. 

           

          .. note::

             

            If the target image is in .jpg format, it might contain Exif metadata that includes the orientation of the image. If the Exif metadata for the target image populates the orientation field, the value of ``OrientationCorrection`` is null and the bounding box coordinates in ``FaceMatches`` and ``UnmatchedFaces`` represent the location of the face after Exif metadata is used to correct the orientation. Images in .png format don't contain Exif metadata.

             

          
    

    **Examples** 

    This operation compares the largest face detected in the source image with each face detected in the target image.
    ::

      response = client.compare_faces(
          SimilarityThreshold=90,
          SourceImage={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'mysourceimage',
              },
          },
          TargetImage={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'mytargetimage',
              },
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FaceMatches': [
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.33481481671333313,
                          'Left': 0.31888890266418457,
                          'Top': 0.4933333396911621,
                          'Width': 0.25,
                      },
                      'Confidence': 99.9991226196289,
                  },
                  'Similarity': 100,
              },
          ],
          'SourceImageFace': {
              'BoundingBox': {
                  'Height': 0.33481481671333313,
                  'Left': 0.31888890266418457,
                  'Top': 0.4933333396911621,
                  'Width': 0.25,
              },
              'Confidence': 99.9991226196289,
          },
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_collection(**kwargs)

    

    Creates a collection in an AWS Region. You can add faces to the collection using the operation. 

     

    For example, you might create collections, one for each of your application users. A user can then index faces using the ``IndexFaces`` operation and persist results in a specific collection. Then, a user can search the collection for faces in the user-specific container. 

     

    .. note::

       

      Collection names are case-sensitive.

       

     

    This operation requires permissions to perform the ``rekognition:CreateCollection`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateCollection>`_    


    **Request Syntax** 
    ::

      response = client.create_collection(
          CollectionId='string'
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID for the collection that you are creating.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StatusCode': 123,
            'CollectionArn': 'string',
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StatusCode** *(integer) --* 

          HTTP status code indicating the result of the operation.

          
        

        - **CollectionArn** *(string) --* 

          Amazon Resource Name (ARN) of the collection. You can use this to manage permissions on your resources. 

          
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the collection you are creating.

          
    

    **Examples** 

    This operation creates a Rekognition collection for storing image data.
    ::

      response = client.create_collection(
          CollectionId='myphotos',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CollectionArn': 'aws:rekognition:us-west-2:123456789012:collection/myphotos',
          'StatusCode': 200,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: create_stream_processor(**kwargs)

    

    Creates an Amazon Rekognition stream processor that you can use to detect and recognize faces in a streaming video.

     

    Rekognition Video is a consumer of live video from Amazon Kinesis Video Streams. Rekognition Video sends analysis results to Amazon Kinesis Data Streams.

     

    You provide as input a Kinesis video stream (``Input`` ) and a Kinesis data stream (``Output`` ) stream. You also specify the face recognition criteria in ``Settings`` . For example, the collection containing faces that you want to recognize. Use ``Name`` to assign an identifier for the stream processor. You use ``Name`` to manage the stream processor. For example, you can start processing the source video by calling with the ``Name`` field. 

     

    After you have finished analyzing a streaming video, use to stop processing. You can delete the stream processor by calling .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateStreamProcessor>`_    


    **Request Syntax** 
    ::

      response = client.create_stream_processor(
          Input={
              'KinesisVideoStream': {
                  'Arn': 'string'
              }
          },
          Output={
              'KinesisDataStream': {
                  'Arn': 'string'
              }
          },
          Name='string',
          Settings={
              'FaceSearch': {
                  'CollectionId': 'string',
                  'FaceMatchThreshold': ...
              }
          },
          RoleArn='string'
      )
    :type Input: dict
    :param Input: **[REQUIRED]** 

      Kinesis video stream stream that provides the source streaming video. If you are using the AWS CLI, the parameter name is ``StreamProcessorInput`` .

      

    
      - **KinesisVideoStream** *(dict) --* 

        The Kinesis video stream input stream for the source streaming video.

        

      
        - **Arn** *(string) --* 

          ARN of the Kinesis video stream stream that streams the source video.

          

        
      
    
    :type Output: dict
    :param Output: **[REQUIRED]** 

      Kinesis data stream stream to which Rekognition Video puts the analysis results. If you are using the AWS CLI, the parameter name is ``StreamProcessorOutput`` .

      

    
      - **KinesisDataStream** *(dict) --* 

        The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.

        

      
        - **Arn** *(string) --* 

          ARN of the output Amazon Kinesis Data Streams stream.

          

        
      
    
    :type Name: string
    :param Name: **[REQUIRED]** 

      An identifier you assign to the stream processor. You can use ``Name`` to manage the stream processor. For example, you can get the current status of the stream processor by calling . ``Name`` is idempotent. 

      

    
    :type Settings: dict
    :param Settings: **[REQUIRED]** 

      Face recognition input parameters to be used by the stream processor. Includes the collection to use for face recognition and the face attributes to detect.

      

    
      - **FaceSearch** *(dict) --* 

        Face search settings to use on a streaming video. 

        

      
        - **CollectionId** *(string) --* 

          The ID of a collection that contains faces that you want to search for.

          

        
        - **FaceMatchThreshold** *(float) --* 

          Minimum face match confidence score that must be met to return a result for a recognized face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.

          

        
      
    
    :type RoleArn: string
    :param RoleArn: **[REQUIRED]** 

      ARN of the IAM role that allows access to the stream processor.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StreamProcessorArn': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StreamProcessorArn** *(string) --* 

          ARN for the newly create stream processor.

          
    

  .. py:method:: delete_collection(**kwargs)

    

    Deletes the specified collection. Note that this operation removes all faces in the collection. For an example, see  delete-collection-procedure .

     

    This operation requires permissions to perform the ``rekognition:DeleteCollection`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteCollection>`_    


    **Request Syntax** 
    ::

      response = client.delete_collection(
          CollectionId='string'
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'StatusCode': 123
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **StatusCode** *(integer) --* 

          HTTP status code that indicates the result of the operation.

          
    

    **Examples** 

    This operation deletes a Rekognition collection.
    ::

      response = client.delete_collection(
          CollectionId='myphotos',
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'StatusCode': 200,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_faces(**kwargs)

    

    Deletes faces from a collection. You specify a collection ID and an array of face IDs to remove from the collection.

     

    This operation requires permissions to perform the ``rekognition:DeleteFaces`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteFaces>`_    


    **Request Syntax** 
    ::

      response = client.delete_faces(
          CollectionId='string',
          FaceIds=[
              'string',
          ]
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      Collection from which to remove the specific faces.

      

    
    :type FaceIds: list
    :param FaceIds: **[REQUIRED]** 

      An array of face IDs to delete.

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'DeletedFaces': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **DeletedFaces** *(list) --* 

          An array of strings (face IDs) of the faces that were deleted.

          
          

          - *(string) --* 
      
    

    **Examples** 

    This operation deletes one or more faces from a Rekognition collection.
    ::

      response = client.delete_faces(
          CollectionId='myphotos',
          FaceIds=[
              'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
          ],
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'DeletedFaces': [
              'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: delete_stream_processor(**kwargs)

    

    Deletes the stream processor identified by ``Name`` . You assign the value for ``Name`` when you create the stream processor with . You might not be able to use the same name for a stream processor for a few seconds after calling ``DeleteStreamProcessor`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DeleteStreamProcessor>`_    


    **Request Syntax** 
    ::

      response = client.delete_stream_processor(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the stream processor you want to delete.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: describe_stream_processor(**kwargs)

    

    Provides information about a stream processor created by . You can get information about the input and output streams, the input parameters for the face recognition being performed, and the current status of the stream processor.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DescribeStreamProcessor>`_    


    **Request Syntax** 
    ::

      response = client.describe_stream_processor(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      Name of the stream processor for which you want information.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Name': 'string',
            'StreamProcessorArn': 'string',
            'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING',
            'StatusMessage': 'string',
            'CreationTimestamp': datetime(2015, 1, 1),
            'LastUpdateTimestamp': datetime(2015, 1, 1),
            'Input': {
                'KinesisVideoStream': {
                    'Arn': 'string'
                }
            },
            'Output': {
                'KinesisDataStream': {
                    'Arn': 'string'
                }
            },
            'RoleArn': 'string',
            'Settings': {
                'FaceSearch': {
                    'CollectionId': 'string',
                    'FaceMatchThreshold': ...
                }
            }
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Name** *(string) --* 

          Name of the stream processor. 

          
        

        - **StreamProcessorArn** *(string) --* 

          ARN of the stream processor.

          
        

        - **Status** *(string) --* 

          Current status of the stream processor.

          
        

        - **StatusMessage** *(string) --* 

          Detailed status message about the stream processor.

          
        

        - **CreationTimestamp** *(datetime) --* 

          Date and time the stream processor was created

          
        

        - **LastUpdateTimestamp** *(datetime) --* 

          The time, in Unix format, the stream processor was last updated. For example, when the stream processor moves from a running state to a failed state, or when the user starts or stops the stream processor.

          
        

        - **Input** *(dict) --* 

          Kinesis video stream that provides the source streaming video.

          
          

          - **KinesisVideoStream** *(dict) --* 

            The Kinesis video stream input stream for the source streaming video.

            
            

            - **Arn** *(string) --* 

              ARN of the Kinesis video stream stream that streams the source video.

              
        
      
        

        - **Output** *(dict) --* 

          Kinesis data stream to which Rekognition Video puts the analysis results.

          
          

          - **KinesisDataStream** *(dict) --* 

            The Amazon Kinesis Data Streams stream to which the Amazon Rekognition stream processor streams the analysis results.

            
            

            - **Arn** *(string) --* 

              ARN of the output Amazon Kinesis Data Streams stream.

              
        
      
        

        - **RoleArn** *(string) --* 

          ARN of the IAM role that allows access to the stream processor.

          
        

        - **Settings** *(dict) --* 

          Face recognition input parameters that are being used by the stream processor. Includes the collection to use for face recognition and the face attributes to detect.

          
          

          - **FaceSearch** *(dict) --* 

            Face search settings to use on a streaming video. 

            
            

            - **CollectionId** *(string) --* 

              The ID of a collection that contains faces that you want to search for.

              
            

            - **FaceMatchThreshold** *(float) --* 

              Minimum face match confidence score that must be met to return a result for a recognized face. Default is 70. 0 is the lowest confidence. 100 is the highest confidence.

              
        
      
    

  .. py:method:: detect_faces(**kwargs)

    

    Detects faces within an image that is provided as input.

     

     ``DetectFaces`` detects the 100 largest faces in the image. For each face detected, the operation returns face details including a bounding box of the face, a confidence value (that the bounding box contains a face), and a fixed set of attributes such as facial landmarks (for example, coordinates of eye and mouth), gender, presence of beard, sunglasses, etc. 

     

    The face-detection algorithm is most effective on frontal faces. For non-frontal or obscured faces, the algorithm may not detect the faces or might detect faces with lower confidence. 

     

    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    .. note::

       

      This is a stateless API operation. That is, the operation does not persist any data.

       

     

    For an example, see  procedure-detecting-faces-in-images .

     

    This operation requires permissions to perform the ``rekognition:DetectFaces`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectFaces>`_    


    **Request Syntax** 
    ::

      response = client.detect_faces(
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          Attributes=[
              'DEFAULT'|'ALL',
          ]
      )
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type Attributes: list
    :param Attributes: 

      An array of facial attributes you want to be returned. This can be the default list of attributes or all attributes. If you don't specify a value for ``Attributes`` or if you specify ``["DEFAULT"]`` , the API returns the following subset of facial attributes: ``BoundingBox`` , ``Confidence`` , ``Pose`` , ``Quality`` and ``Landmarks`` . If you provide ``["ALL"]`` , all facial attributes are returned but the operation will take longer to complete.

       

      If you provide both, ``["ALL", "DEFAULT"]`` , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes). 

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FaceDetails': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'AgeRange': {
                        'Low': 123,
                        'High': 123
                    },
                    'Smile': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Eyeglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Sunglasses': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Gender': {
                        'Value': 'Male'|'Female',
                        'Confidence': ...
                    },
                    'Beard': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Mustache': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'EyesOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'MouthOpen': {
                        'Value': True|False,
                        'Confidence': ...
                    },
                    'Emotions': [
                        {
                            'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                            'Confidence': ...
                        },
                    ],
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    },
                    'Confidence': ...
                },
            ],
            'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FaceDetails** *(list) --* 

          Details of each face found in the image. 

          
          

          - *(dict) --* 

            Structure containing attributes of the face that the algorithm detected.

            
            

            - **BoundingBox** *(dict) --* 

              Bounding box of the face.

              
              

              - **Width** *(float) --* 

                Width of the bounding box as a ratio of the overall image width.

                
              

              - **Height** *(float) --* 

                Height of the bounding box as a ratio of the overall image height.

                
              

              - **Left** *(float) --* 

                Left coordinate of the bounding box as a ratio of overall image width.

                
              

              - **Top** *(float) --* 

                Top coordinate of the bounding box as a ratio of overall image height.

                
          
            

            - **AgeRange** *(dict) --* 

              The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

              
              

              - **Low** *(integer) --* 

                The lowest estimated age.

                
              

              - **High** *(integer) --* 

                The highest estimated age.

                
          
            

            - **Smile** *(dict) --* 

              Indicates whether or not the face is smiling, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the face is smiling or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Eyeglasses** *(dict) --* 

              Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the face is wearing eye glasses or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Sunglasses** *(dict) --* 

              Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the face is wearing sunglasses or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Gender** *(dict) --* 

              Gender of the face and the confidence level in the determination.

              
              

              - **Value** *(string) --* 

                Gender of the face.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Beard** *(dict) --* 

              Indicates whether or not the face has a beard, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the face has beard or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Mustache** *(dict) --* 

              Indicates whether or not the face has a mustache, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the face has mustache or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **EyesOpen** *(dict) --* 

              Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the eyes on the face are open.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **MouthOpen** *(dict) --* 

              Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

              
              

              - **Value** *(boolean) --* 

                Boolean value that indicates whether the mouth on the face is open or not.

                
              

              - **Confidence** *(float) --* 

                Level of confidence in the determination.

                
          
            

            - **Emotions** *(list) --* 

              The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

              
              

              - *(dict) --* 

                The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                
                

                - **Type** *(string) --* 

                  Type of emotion detected.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
          
            

            - **Landmarks** *(list) --* 

              Indicates the location of landmarks on the face.

              
              

              - *(dict) --* 

                Indicates the location of the landmark on the face.

                
                

                - **Type** *(string) --* 

                  Type of the landmark.

                  
                

                - **X** *(float) --* 

                  x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                  
                

                - **Y** *(float) --* 

                  y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  
            
          
            

            - **Pose** *(dict) --* 

              Indicates the pose of the face as determined by its pitch, roll, and yaw.

              
              

              - **Roll** *(float) --* 

                Value representing the face rotation on the roll axis.

                
              

              - **Yaw** *(float) --* 

                Value representing the face rotation on the yaw axis.

                
              

              - **Pitch** *(float) --* 

                Value representing the face rotation on the pitch axis.

                
          
            

            - **Quality** *(dict) --* 

              Identifies image brightness and sharpness.

              
              

              - **Brightness** *(float) --* 

                Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                
              

              - **Sharpness** *(float) --* 

                Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                
          
            

            - **Confidence** *(float) --* 

              Confidence level that the bounding box contains a face (and not a different object such as a tree).

              
        
      
        

        - **OrientationCorrection** *(string) --* 

          The orientation of the input image (counter-clockwise direction). If your application displays the image, you can use this value to correct image orientation. The bounding box coordinates returned in ``FaceDetails`` represent face locations before the image orientation is corrected. 

           

          .. note::

             

            If the input image is in .jpeg format, it might contain exchangeable image (Exif) metadata that includes the image's orientation. If so, and the Exif metadata for the input image populates the orientation field, the value of ``OrientationCorrection`` is null and the ``FaceDetails`` bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.

             

          
    

    **Examples** 

    This operation detects faces in an image stored in an AWS S3 bucket.
    ::

      response = client.detect_faces(
          Image={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'myphoto',
              },
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FaceDetails': [
              {
                  'BoundingBox': {
                      'Height': 0.18000000715255737,
                      'Left': 0.5555555820465088,
                      'Top': 0.33666667342185974,
                      'Width': 0.23999999463558197,
                  },
                  'Confidence': 100,
                  'Landmarks': [
                      {
                          'Type': 'EYE_LEFT',
                          'X': 0.6394737362861633,
                          'Y': 0.40819624066352844,
                      },
                      {
                          'Type': 'EYE_RIGHT',
                          'X': 0.7266660928726196,
                          'Y': 0.41039225459098816,
                      },
                      {
                          'Type': 'NOSE_LEFT',
                          'X': 0.6912462115287781,
                          'Y': 0.44240960478782654,
                      },
                      {
                          'Type': 'MOUTH_DOWN',
                          'X': 0.6306198239326477,
                          'Y': 0.46700039505958557,
                      },
                      {
                          'Type': 'MOUTH_UP',
                          'X': 0.7215608954429626,
                          'Y': 0.47114261984825134,
                      },
                  ],
                  'Pose': {
                      'Pitch': 4.050806522369385,
                      'Roll': 0.9950747489929199,
                      'Yaw': 13.693790435791016,
                  },
                  'Quality': {
                      'Brightness': 37.60169982910156,
                      'Sharpness': 80,
                  },
              },
          ],
          'OrientationCorrection': 'ROTATE_0',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: detect_labels(**kwargs)

    

    Detects instances of real-world entities within an image (JPEG or PNG) provided as input. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; and concepts like landscape, evening, and nature. For an example, see  images-s3 .

     

    .. note::

       

       ``DetectLabels`` does not support the detection of activities. However, activity detection is supported for label detection in videos. For more information, see .

       

     

    You pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    For each object, scene, and concept the API returns one or more labels. Each label provides the object name, and the level of confidence that the image contains the object. For example, suppose the input image has a lighthouse, the sea, and a rock. The response will include all three labels, one for each object. 

     

     ``{Name: lighthouse, Confidence: 98.4629}``  

     

     ``{Name: rock,Confidence: 79.2097}``  

     

     ``{Name: sea,Confidence: 75.061}``  

     

    In the preceding example, the operation returns one label for each of the three objects. The operation can also return multiple labels for the same object in the image. For example, if the input image shows a flower (for example, a tulip), the operation might return the following three labels. 

     

     ``{Name: flower,Confidence: 99.0562}``  

     

     ``{Name: plant,Confidence: 99.0562}``  

     

     ``{Name: tulip,Confidence: 99.0562}``  

     

    In this example, the detection algorithm more precisely identifies the flower as a tulip.

     

    In response, the API returns an array of labels. In addition, the response also includes the orientation correction. Optionally, you can specify ``MinConfidence`` to control the confidence threshold for the labels returned. The default is 50%. You can also add the ``MaxLabels`` parameter to limit the number of labels returned. 

     

    .. note::

       

      If the object detected is a person, the operation doesn't provide the same facial details that the  DetectFaces operation provides.

       

     

    This is a stateless API operation. That is, the operation does not persist any data.

     

    This operation requires permissions to perform the ``rekognition:DetectLabels`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectLabels>`_    


    **Request Syntax** 
    ::

      response = client.detect_labels(
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          MaxLabels=123,
          MinConfidence=...
      )
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type MaxLabels: integer
    :param MaxLabels: 

      Maximum number of labels you want the service to return in the response. The service returns the specified number of highest confidence labels. 

      

    
    :type MinConfidence: float
    :param MinConfidence: 

      Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with confidence lower than this specified value.

       

      If ``MinConfidence`` is not specified, the operation returns labels with a confidence values greater than or equal to 50 percent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Labels': [
                {
                    'Name': 'string',
                    'Confidence': ...
                },
            ],
            'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Labels** *(list) --* 

          An array of labels for the real-world objects detected. 

          
          

          - *(dict) --* 

            Structure containing details about the detected label, including name, and level of confidence.

            
            

            - **Name** *(string) --* 

              The name (label) of the object.

              
            

            - **Confidence** *(float) --* 

              Level of confidence.

              
        
      
        

        - **OrientationCorrection** *(string) --* 

          The orientation of the input image (counter-clockwise direction). If your application displays the image, you can use this value to correct the orientation. If Amazon Rekognition detects that the input image was rotated (for example, by 90 degrees), it first corrects the orientation before detecting the labels. 

           

          .. note::

             

            If the input image Exif metadata populates the orientation field, Amazon Rekognition does not perform orientation correction and the value of OrientationCorrection will be null.

             

          
    

    **Examples** 

    This operation detects labels in the supplied image
    ::

      response = client.detect_labels(
          Image={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'myphoto',
              },
          },
          MaxLabels=123,
          MinConfidence=70,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Labels': [
              {
                  'Confidence': 99.25072479248047,
                  'Name': 'People',
              },
              {
                  'Confidence': 99.25074005126953,
                  'Name': 'Person',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: detect_moderation_labels(**kwargs)

    

    Detects explicit or suggestive adult content in a specified JPEG or PNG format image. Use ``DetectModerationLabels`` to moderate images depending on your requirements. For example, you might want to filter images that contain nudity, but not images containing suggestive content.

     

    To filter images, use the labels returned by ``DetectModerationLabels`` to determine which types of content are appropriate. For information about moderation labels, see  moderation .

     

    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectModerationLabels>`_    


    **Request Syntax** 
    ::

      response = client.detect_moderation_labels(
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          MinConfidence=...
      )
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type MinConfidence: float
    :param MinConfidence: 

      Specifies the minimum confidence level for the labels to return. Amazon Rekognition doesn't return any labels with a confidence level lower than this specified value.

       

      If you don't specify ``MinConfidence`` , the operation returns labels with confidence values greater than or equal to 50 percent.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'ModerationLabels': [
                {
                    'Confidence': ...,
                    'Name': 'string',
                    'ParentName': 'string'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **ModerationLabels** *(list) --* 

          Array of detected Moderation labels and the time, in millseconds from the start of the video, they were detected.

          
          

          - *(dict) --* 

            Provides information about a single type of moderated content found in an image or video. Each type of moderated content has a label within a hierarchical taxonomy. For more information, see  moderation .

            
            

            - **Confidence** *(float) --* 

              Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.

               

              If you don't specify the ``MinConfidence`` parameter in the call to ``DetectModerationLabels`` , the operation returns labels with a confidence value greater than or equal to 50 percent.

              
            

            - **Name** *(string) --* 

              The label name for the type of content detected in the image.

              
            

            - **ParentName** *(string) --* 

              The name for the parent label. Labels at the top-level of the hierarchy have the parent label ``""`` .

              
        
      
    

  .. py:method:: detect_text(**kwargs)

    

    Detects text in the input image and converts it into machine-readable text.

     

    Pass the input image as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the AWS CLI to call Amazon Rekognition operations, you must pass it as a reference to an image in an Amazon S3 bucket. For the AWS CLI, passing image bytes is not supported. The image must be either a .png or .jpeg formatted file. 

     

    The ``DetectText`` operation returns text in an array of elements, ``TextDetections`` . Each ``TextDetection`` element provides information about a single word or line of text that was detected in the image. 

     

    A word is one or more ISO basic latin script characters that are not separated by spaces. ``DetectText`` can detect up to 50 words in an image.

     

    A line is a string of equally spaced words. A line isn't necessarily a complete sentence. For example, a driver's license number is detected as a line. A line ends when there is no aligned text after it. Also, a line ends when there is a large gap between words, relative to the length of the words. This means, depending on the gap between words, Amazon Rekognition may detect multiple lines in text aligned in the same direction. Periods don't represent the end of a line. If a sentence spans multiple lines, the ``DetectText`` operation returns multiple lines.

     

    To determine whether a ``TextDetection`` element is a line of text or a word, use the ``TextDetection`` object ``Type`` field. 

     

    To be detected, text must be within +/- 30 degrees orientation of the horizontal axis.

     

    For more information, see  text-detection .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/DetectText>`_    


    **Request Syntax** 
    ::

      response = client.detect_text(
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          }
      )
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Rekognition operations, you can't pass image bytes. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'TextDetections': [
                {
                    'DetectedText': 'string',
                    'Type': 'LINE'|'WORD',
                    'Id': 123,
                    'ParentId': 123,
                    'Confidence': ...,
                    'Geometry': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Polygon': [
                            {
                                'X': ...,
                                'Y': ...
                            },
                        ]
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **TextDetections** *(list) --* 

          An array of text that was detected in the input image.

          
          

          - *(dict) --* 

            Information about a word or line of text detected by .

             

            The ``DetectedText`` field contains the text that Amazon Rekognition detected in the image. 

             

            Every word and line has an identifier (``Id`` ). Each word belongs to a line and has a parent identifier (``ParentId`` ) that identifies the line of text in which the word appears. The word ``Id`` is also an index for the word within a line of words. 

             

            For more information, see  text-detection .

            
            

            - **DetectedText** *(string) --* 

              The word or line of text recognized by Amazon Rekognition. 

              
            

            - **Type** *(string) --* 

              The type of text that was detected.

              
            

            - **Id** *(integer) --* 

              The identifier for the detected text. The identifier is only unique for a single call to ``DetectText`` . 

              
            

            - **ParentId** *(integer) --* 

              The Parent identifier for the detected text identified by the value of ``ID`` . If the type of detected text is ``LINE`` , the value of ``ParentId`` is ``Null`` . 

              
            

            - **Confidence** *(float) --* 

              The confidence that Amazon Rekognition has in the accuracy of the detected text and the accuracy of the geometry points around the detected text.

              
            

            - **Geometry** *(dict) --* 

              The location of the detected text on the image. Includes an axis aligned coarse bounding box surrounding the text and a finer grain polygon for more accurate spatial information.

              
              

              - **BoundingBox** *(dict) --* 

                An axis-aligned coarse representation of the detected text's location on the image.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Polygon** *(list) --* 

                Within the bounding box, a fine-grained polygon around the detected text.

                
                

                - *(dict) --* 

                  The X and Y coordinates of a point on an image. The X and Y values returned are ratios of the overall image size. For example, if the input image is 700x200 and the operation returns X=0.5 and Y=0.25, then the point is at the (350,50) pixel coordinate on the image.

                   

                  An array of ``Point`` objects, ``Polygon`` , is returned by . ``Polygon`` represents a fine-grained polygon around detected text. For more information, see . 

                  
                  

                  - **X** *(float) --* 

                    The value of the X coordinate for a point on a ``Polygon`` .

                    
                  

                  - **Y** *(float) --* 

                    The value of the Y coordinate for a point on a ``Polygon`` .

                    
              
            
          
        
      
    

  .. py:method:: generate_presigned_url(ClientMethod, Params=None, ExpiresIn=3600, HttpMethod=None)

        
    Generate a presigned url given a client, its method, and arguments
    
    :type ClientMethod: string
    :param ClientMethod: The client method to presign for
    
    :type Params: dict
    :param Params: The parameters normally passed to
        ``ClientMethod``.
    
    :type ExpiresIn: int
    :param ExpiresIn: The number of seconds the presigned url is valid
        for. By default it expires in an hour (3600 seconds)
    
    :type HttpMethod: string
    :param HttpMethod: The http method to use on the generated url. By
        default, the http method is whatever is used in the method's model.
    
    :returns: The presigned url


  .. py:method:: get_celebrity_info(**kwargs)

    

    Gets the name and additional information about a celebrity based on his or her Rekognition ID. The additional information is returned as an array of URLs. If there is no additional information about the celebrity, this list is empty. For more information, see  get-celebrity-info-procedure .

     

    This operation requires permissions to perform the ``rekognition:GetCelebrityInfo`` action. 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetCelebrityInfo>`_    


    **Request Syntax** 
    ::

      response = client.get_celebrity_info(
          Id='string'
      )
    :type Id: string
    :param Id: **[REQUIRED]** 

      The ID for the celebrity. You get the celebrity ID from a call to the operation, which recognizes celebrities in an image. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Urls': [
                'string',
            ],
            'Name': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Urls** *(list) --* 

          An array of URLs pointing to additional celebrity information. 

          
          

          - *(string) --* 
      
        

        - **Name** *(string) --* 

          The name of the celebrity.

          
    

  .. py:method:: get_celebrity_recognition(**kwargs)

    

    Gets the celebrity recognition results for a Rekognition Video analysis started by .

     

    Celebrity recognition in a video is an asynchronous operation. Analysis is started by a call to which returns a job identifier (``JobId`` ). When the celebrity recognition operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartCelebrityRecognition`` . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetCelebrityDetection`` and pass the job identifier (``JobId`` ) from the initial call to ``StartCelebrityDetection`` . For more information, see  video .

     

     ``GetCelebrityRecognition`` returns detected celebrities and the time(s) they are detected in an array (``Celebrities`` ) of objects. Each ``CelebrityRecognition`` contains information about the celebrity in a object and the time, ``Timestamp`` , the celebrity was detected. 

     

    By default, the ``Celebrities`` array is sorted by time (milliseconds from the start of the video). You can also sort the array by celebrity by specifying the value ``ID`` in the ``SortBy`` input parameter.

     

    The ``CelebrityDetail`` object includes the celebrity identifer and additional information urls. If you don't store the additional information urls, you can get them later by calling with the celebrity identifer.

     

    No information is returned for faces not recognized as celebrities.

     

    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetCelebrityDetection`` and populate the ``NextToken`` request parameter with the token value returned from the previous call to ``GetCelebrityRecognition`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetCelebrityRecognition>`_    


    **Request Syntax** 
    ::

      response = client.get_celebrity_recognition(
          JobId='string',
          MaxResults=123,
          NextToken='string',
          SortBy='ID'|'TIMESTAMP'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      Job identifier for the required celebrity recognition analysis. You can get the job identifer from a call to ``StartCelebrityRecognition`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of celebrities you want Rekognition Video to return in the response. The default is 1000.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there is more recognized celebrities to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of celebrities. 

      

    
    :type SortBy: string
    :param SortBy: 

      Sort to use for celebrities returned in ``Celebrities`` field. Specify ``ID`` to sort by the celebrity identifier, specify ``TIMESTAMP`` to sort by the time the celebrity was recognized.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'NextToken': 'string',
            'Celebrities': [
                {
                    'Timestamp': 123,
                    'Celebrity': {
                        'Urls': [
                            'string',
                        ],
                        'Name': 'string',
                        'Id': 'string',
                        'Confidence': ...,
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the celebrity recognition job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Rekognition Video analyzed. ``Videometadata`` is returned in every page of paginated responses from a Rekognition Video operation.

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of celebrities.

          
        

        - **Celebrities** *(list) --* 

          Array of celebrities recognized in the video.

          
          

          - *(dict) --* 

            Information about a detected celebrity and the time the celebrity was detected in a stored video. For more information, see .

            
            

            - **Timestamp** *(integer) --* 

              The time, in milliseconds from the start of the video, that the celebrity was recognized.

              
            

            - **Celebrity** *(dict) --* 

              Information about a recognized celebrity.

              
              

              - **Urls** *(list) --* 

                An array of URLs pointing to additional celebrity information. 

                
                

                - *(string) --* 
            
              

              - **Name** *(string) --* 

                The name of the celebrity.

                
              

              - **Id** *(string) --* 

                The unique identifier for the celebrity. 

                
              

              - **Confidence** *(float) --* 

                The confidence, in percentage, that Amazon Rekognition has that the recognized face is the celebrity. 

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box around the body of a celebrity.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Face** *(dict) --* 

                Face details for the recognized celebrity.

                
                

                - **BoundingBox** *(dict) --* 

                  Bounding box of the face.

                  
                  

                  - **Width** *(float) --* 

                    Width of the bounding box as a ratio of the overall image width.

                    
                  

                  - **Height** *(float) --* 

                    Height of the bounding box as a ratio of the overall image height.

                    
                  

                  - **Left** *(float) --* 

                    Left coordinate of the bounding box as a ratio of overall image width.

                    
                  

                  - **Top** *(float) --* 

                    Top coordinate of the bounding box as a ratio of overall image height.

                    
              
                

                - **AgeRange** *(dict) --* 

                  The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

                  
                  

                  - **Low** *(integer) --* 

                    The lowest estimated age.

                    
                  

                  - **High** *(integer) --* 

                    The highest estimated age.

                    
              
                

                - **Smile** *(dict) --* 

                  Indicates whether or not the face is smiling, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is smiling or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Eyeglasses** *(dict) --* 

                  Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing eye glasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Sunglasses** *(dict) --* 

                  Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing sunglasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Gender** *(dict) --* 

                  Gender of the face and the confidence level in the determination.

                  
                  

                  - **Value** *(string) --* 

                    Gender of the face.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Beard** *(dict) --* 

                  Indicates whether or not the face has a beard, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has beard or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Mustache** *(dict) --* 

                  Indicates whether or not the face has a mustache, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has mustache or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **EyesOpen** *(dict) --* 

                  Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the eyes on the face are open.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **MouthOpen** *(dict) --* 

                  Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the mouth on the face is open or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Emotions** *(list) --* 

                  The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

                  
                  

                  - *(dict) --* 

                    The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                    
                    

                    - **Type** *(string) --* 

                      Type of emotion detected.

                      
                    

                    - **Confidence** *(float) --* 

                      Level of confidence in the determination.

                      
                
              
                

                - **Landmarks** *(list) --* 

                  Indicates the location of landmarks on the face.

                  
                  

                  - *(dict) --* 

                    Indicates the location of the landmark on the face.

                    
                    

                    - **Type** *(string) --* 

                      Type of the landmark.

                      
                    

                    - **X** *(float) --* 

                      x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                      
                    

                    - **Y** *(float) --* 

                      y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                      
                
              
                

                - **Pose** *(dict) --* 

                  Indicates the pose of the face as determined by its pitch, roll, and yaw.

                  
                  

                  - **Roll** *(float) --* 

                    Value representing the face rotation on the roll axis.

                    
                  

                  - **Yaw** *(float) --* 

                    Value representing the face rotation on the yaw axis.

                    
                  

                  - **Pitch** *(float) --* 

                    Value representing the face rotation on the pitch axis.

                    
              
                

                - **Quality** *(dict) --* 

                  Identifies image brightness and sharpness.

                  
                  

                  - **Brightness** *(float) --* 

                    Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                    
                  

                  - **Sharpness** *(float) --* 

                    Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                    
              
                

                - **Confidence** *(float) --* 

                  Confidence level that the bounding box contains a face (and not a different object such as a tree).

                  
            
          
        
      
    

  .. py:method:: get_content_moderation(**kwargs)

    

    Gets the content moderation analysis results for a Rekognition Video analysis started by .

     

    Content moderation analysis of a video is an asynchronous operation. You start analysis by calling . which returns a job identifier (``JobId`` ). When analysis finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartContentModeration`` . To get the results of the content moderation analysis, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetCelebrityDetection`` and pass the job identifier (``JobId`` ) from the initial call to ``StartCelebrityDetection`` . For more information, see  video . 

     

     ``GetContentModeration`` returns detected content moderation labels, and the time they are detected, in an array, ``ModerationLabels`` , of objects. 

     

    By default, the moderated labels are returned sorted by time, in milliseconds from the start of the video. You can also sort them by moderated label by specifying ``NAME`` for the ``SortBy`` input parameter. 

     

    Since video analysis can return a large number of results, use the ``MaxResults`` parameter to limit the number of labels returned in a single call to ``GetContentModeration`` . If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetContentModeration`` and populate the ``NextToken`` request parameter with the value of ``NextToken`` returned from the previous call to ``GetContentModeration`` .

     

    For more information, see  moderation .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetContentModeration>`_    


    **Request Syntax** 
    ::

      response = client.get_content_moderation(
          JobId='string',
          MaxResults=123,
          NextToken='string',
          SortBy='NAME'|'TIMESTAMP'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The identifier for the content moderation job. Use ``JobId`` to identify the job in a subsequent call to ``GetContentModeration`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of content moderation labels to return. The default is 1000.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of content moderation labels.

      

    
    :type SortBy: string
    :param SortBy: 

      Sort to use for elements in the ``ModerationLabelDetections`` array. Use ``TIMESTAMP`` to sort array elements by the time labels are detected. Use ``NAME`` to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by ``TIMESTAMP`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'ModerationLabels': [
                {
                    'Timestamp': 123,
                    'ModerationLabel': {
                        'Confidence': ...,
                        'Name': 'string',
                        'ParentName': 'string'
                    }
                },
            ],
            'NextToken': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the content moderation job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in every page of paginated responses from ``GetContentModeration`` . 

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **ModerationLabels** *(list) --* 

          The detected moderation labels and the time(s) they were detected.

          
          

          - *(dict) --* 

            Information about a moderation label detection in a stored video.

            
            

            - **Timestamp** *(integer) --* 

              Time, in milliseconds from the beginning of the video, that the moderation label was detected.

              
            

            - **ModerationLabel** *(dict) --* 

              The moderation label detected by in the stored video.

              
              

              - **Confidence** *(float) --* 

                Specifies the confidence that Amazon Rekognition has that the label has been correctly identified.

                 

                If you don't specify the ``MinConfidence`` parameter in the call to ``DetectModerationLabels`` , the operation returns labels with a confidence value greater than or equal to 50 percent.

                
              

              - **Name** *(string) --* 

                The label name for the type of content detected in the image.

                
              

              - **ParentName** *(string) --* 

                The name for the parent label. Labels at the top-level of the hierarchy have the parent label ``""`` .

                
          
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of moderation labels. 

          
    

  .. py:method:: get_face_detection(**kwargs)

    

    Gets face detection results for a Rekognition Video analysis started by .

     

    Face detection with Rekognition Video is an asynchronous operation. You start face detection by calling which returns a job identifier (``JobId`` ). When the face detection operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartFaceDetection`` . To get the results of the face detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartFaceDetection`` .

     

     ``GetFaceDetection`` returns an array of detected faces (``Faces`` ) sorted by the time the faces were detected. 

     

    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetFaceDetection`` and populate the ``NextToken`` request parameter with the token value returned from the previous call to ``GetFaceDetection`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetFaceDetection>`_    


    **Request Syntax** 
    ::

      response = client.get_face_detection(
          JobId='string',
          MaxResults=123,
          NextToken='string'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      Unique identifier for the face detection job. The ``JobId`` is returned from ``StartFaceDetection`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of detected faces to return. The default is 1000.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there are more faces to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'NextToken': 'string',
            'Faces': [
                {
                    'Timestamp': 123,
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the face detection job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Rekognition Video analyzed. ``Videometadata`` is returned in every page of paginated responses from a Amazon Rekognition video operation.

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces. 

          
        

        - **Faces** *(list) --* 

          An array of faces detected in the video. Each element contains a detected face's details and the time, in milliseconds from the start of the video, the face was detected. 

          
          

          - *(dict) --* 

            Information about a face detected in a video analysis request and the time the face was detected in the video. 

            
            

            - **Timestamp** *(integer) --* 

              Time, in milliseconds from the start of the video, that the face was detected.

              
            

            - **Face** *(dict) --* 

              The face properties for the detected face.

              
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **AgeRange** *(dict) --* 

                The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

                
                

                - **Low** *(integer) --* 

                  The lowest estimated age.

                  
                

                - **High** *(integer) --* 

                  The highest estimated age.

                  
            
              

              - **Smile** *(dict) --* 

                Indicates whether or not the face is smiling, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is smiling or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Eyeglasses** *(dict) --* 

                Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is wearing eye glasses or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Sunglasses** *(dict) --* 

                Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is wearing sunglasses or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Gender** *(dict) --* 

                Gender of the face and the confidence level in the determination.

                
                

                - **Value** *(string) --* 

                  Gender of the face.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Beard** *(dict) --* 

                Indicates whether or not the face has a beard, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face has beard or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Mustache** *(dict) --* 

                Indicates whether or not the face has a mustache, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face has mustache or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **EyesOpen** *(dict) --* 

                Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the eyes on the face are open.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **MouthOpen** *(dict) --* 

                Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the mouth on the face is open or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Emotions** *(list) --* 

                The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

                
                

                - *(dict) --* 

                  The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                  
                  

                  - **Type** *(string) --* 

                    Type of emotion detected.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
            
              

              - **Landmarks** *(list) --* 

                Indicates the location of landmarks on the face.

                
                

                - *(dict) --* 

                  Indicates the location of the landmark on the face.

                  
                  

                  - **Type** *(string) --* 

                    Type of the landmark.

                    
                  

                  - **X** *(float) --* 

                    x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                    
                  

                  - **Y** *(float) --* 

                    y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    
              
            
              

              - **Pose** *(dict) --* 

                Indicates the pose of the face as determined by its pitch, roll, and yaw.

                
                

                - **Roll** *(float) --* 

                  Value representing the face rotation on the roll axis.

                  
                

                - **Yaw** *(float) --* 

                  Value representing the face rotation on the yaw axis.

                  
                

                - **Pitch** *(float) --* 

                  Value representing the face rotation on the pitch axis.

                  
            
              

              - **Quality** *(dict) --* 

                Identifies image brightness and sharpness.

                
                

                - **Brightness** *(float) --* 

                  Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                  
                

                - **Sharpness** *(float) --* 

                  Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                  
            
              

              - **Confidence** *(float) --* 

                Confidence level that the bounding box contains a face (and not a different object such as a tree).

                
          
        
      
    

  .. py:method:: get_face_search(**kwargs)

    

    Gets the face search results for Rekognition Video face search started by . The search returns faces in a collection that match the faces of persons detected in a video. It also includes the time(s) that faces are matched in the video.

     

    Face search in a video is an asynchronous operation. You start face search by calling to which returns a job identifier (``JobId`` ). When the search operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartFaceSearch`` . To get the search results, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call ``GetFaceSearch`` and pass the job identifier (``JobId`` ) from the initial call to ``StartFaceSearch`` . For more information, see  collections .

     

    The search results are retured in an array, ``Persons`` , of objects. Each``PersonMatch`` element contains details about the matching faces in the input collection, person information for the matched person, and the time the person was matched in the video.

     

    By default, the ``Persons`` array is sorted by the time, in milliseconds from the start of the video, persons are matched. You can also sort by persons by specifying ``INDEX`` for the ``SORTBY`` input parameter.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetFaceSearch>`_    


    **Request Syntax** 
    ::

      response = client.get_face_search(
          JobId='string',
          MaxResults=123,
          NextToken='string',
          SortBy='INDEX'|'TIMESTAMP'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The job identifer for the search request. You get the job identifier from an initial call to ``StartFaceSearch`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of search results you want Rekognition Video to return in the response. The default is 1000.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there is more search results to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of search results. 

      

    
    :type SortBy: string
    :param SortBy: 

      Sort to use for grouping faces in the response. Use ``TIMESTAMP`` to group faces by the time that they are recognized. Use ``INDEX`` to sort by recognized faces. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'NextToken': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'Persons': [
                {
                    'Timestamp': 123,
                    'Person': {
                        'Index': 123,
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    },
                    'FaceMatches': [
                        {
                            'Similarity': ...,
                            'Face': {
                                'FaceId': 'string',
                                'BoundingBox': {
                                    'Width': ...,
                                    'Height': ...,
                                    'Left': ...,
                                    'Top': ...
                                },
                                'ImageId': 'string',
                                'ExternalImageId': 'string',
                                'Confidence': ...
                            }
                        },
                    ]
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the face search job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of search results. 

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Amazon Rekognition analyzed. ``Videometadata`` is returned in every page of paginated responses from a Rekognition Video operation. 

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **Persons** *(list) --* 

          An array of persons, , in the video whose face(s) match the face(s) in an Amazon Rekognition collection. It also includes time information for when persons are matched in the video. You specify the input collection in an initial call to ``StartFaceSearch`` . Each ``Persons`` element includes a time the person was matched, face match details (``FaceMatches`` ) for matching faces in the collection, and person information (``Person`` ) for the matched person. 

          
          

          - *(dict) --* 

            Information about a person whose face matches a face(s) in a Amazon Rekognition collection. Includes information about the faces in the Amazon Rekognition collection (,information about the person ( PersonDetail ) and the timestamp for when the person was detected in a video. An array of ``PersonMatch`` objects is returned by . 

            
            

            - **Timestamp** *(integer) --* 

              The time, in milliseconds from the beginning of the video, that the person was matched in the video.

              
            

            - **Person** *(dict) --* 

              Information about the matched person.

              
              

              - **Index** *(integer) --* 

                Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box around the detected person.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Face** *(dict) --* 

                Face details for the detected person.

                
                

                - **BoundingBox** *(dict) --* 

                  Bounding box of the face.

                  
                  

                  - **Width** *(float) --* 

                    Width of the bounding box as a ratio of the overall image width.

                    
                  

                  - **Height** *(float) --* 

                    Height of the bounding box as a ratio of the overall image height.

                    
                  

                  - **Left** *(float) --* 

                    Left coordinate of the bounding box as a ratio of overall image width.

                    
                  

                  - **Top** *(float) --* 

                    Top coordinate of the bounding box as a ratio of overall image height.

                    
              
                

                - **AgeRange** *(dict) --* 

                  The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

                  
                  

                  - **Low** *(integer) --* 

                    The lowest estimated age.

                    
                  

                  - **High** *(integer) --* 

                    The highest estimated age.

                    
              
                

                - **Smile** *(dict) --* 

                  Indicates whether or not the face is smiling, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is smiling or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Eyeglasses** *(dict) --* 

                  Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing eye glasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Sunglasses** *(dict) --* 

                  Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing sunglasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Gender** *(dict) --* 

                  Gender of the face and the confidence level in the determination.

                  
                  

                  - **Value** *(string) --* 

                    Gender of the face.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Beard** *(dict) --* 

                  Indicates whether or not the face has a beard, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has beard or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Mustache** *(dict) --* 

                  Indicates whether or not the face has a mustache, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has mustache or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **EyesOpen** *(dict) --* 

                  Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the eyes on the face are open.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **MouthOpen** *(dict) --* 

                  Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the mouth on the face is open or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Emotions** *(list) --* 

                  The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

                  
                  

                  - *(dict) --* 

                    The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                    
                    

                    - **Type** *(string) --* 

                      Type of emotion detected.

                      
                    

                    - **Confidence** *(float) --* 

                      Level of confidence in the determination.

                      
                
              
                

                - **Landmarks** *(list) --* 

                  Indicates the location of landmarks on the face.

                  
                  

                  - *(dict) --* 

                    Indicates the location of the landmark on the face.

                    
                    

                    - **Type** *(string) --* 

                      Type of the landmark.

                      
                    

                    - **X** *(float) --* 

                      x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                      
                    

                    - **Y** *(float) --* 

                      y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                      
                
              
                

                - **Pose** *(dict) --* 

                  Indicates the pose of the face as determined by its pitch, roll, and yaw.

                  
                  

                  - **Roll** *(float) --* 

                    Value representing the face rotation on the roll axis.

                    
                  

                  - **Yaw** *(float) --* 

                    Value representing the face rotation on the yaw axis.

                    
                  

                  - **Pitch** *(float) --* 

                    Value representing the face rotation on the pitch axis.

                    
              
                

                - **Quality** *(dict) --* 

                  Identifies image brightness and sharpness.

                  
                  

                  - **Brightness** *(float) --* 

                    Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                    
                  

                  - **Sharpness** *(float) --* 

                    Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                    
              
                

                - **Confidence** *(float) --* 

                  Confidence level that the bounding box contains a face (and not a different object such as a tree).

                  
            
          
            

            - **FaceMatches** *(list) --* 

              Information about the faces in the input collection that match the face of a person in the video.

              
              

              - *(dict) --* 

                Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

                
                

                - **Similarity** *(float) --* 

                  Confidence in the match of this face with the input face.

                  
                

                - **Face** *(dict) --* 

                  Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

                  
                  

                  - **FaceId** *(string) --* 

                    Unique identifier that Amazon Rekognition assigns to the face.

                    
                  

                  - **BoundingBox** *(dict) --* 

                    Bounding box of the face.

                    
                    

                    - **Width** *(float) --* 

                      Width of the bounding box as a ratio of the overall image width.

                      
                    

                    - **Height** *(float) --* 

                      Height of the bounding box as a ratio of the overall image height.

                      
                    

                    - **Left** *(float) --* 

                      Left coordinate of the bounding box as a ratio of overall image width.

                      
                    

                    - **Top** *(float) --* 

                      Top coordinate of the bounding box as a ratio of overall image height.

                      
                
                  

                  - **ImageId** *(string) --* 

                    Unique identifier that Amazon Rekognition assigns to the input image.

                    
                  

                  - **ExternalImageId** *(string) --* 

                    Identifier that you assign to all the faces in the input image.

                    
                  

                  - **Confidence** *(float) --* 

                    Confidence level that the bounding box contains a face (and not a different object such as a tree).

                    
              
            
          
        
      
    

  .. py:method:: get_label_detection(**kwargs)

    

    Gets the label detection results of a Rekognition Video analysis started by . 

     

    The label detection operation is started by a call to which returns a job identifier (``JobId`` ). When the label detection operation finishes, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartlabelDetection`` . To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartLabelDetection`` .

     

     ``GetLabelDetection`` returns an array of detected labels (``Labels`` ) sorted by the time the labels were detected. You can also sort by the label name by specifying ``NAME`` for the ``SortBy`` input parameter.

     

    The labels returned include the label name, the percentage confidence in the accuracy of the detected label, and the time the label was detected in the video.

     

    Use MaxResults parameter to limit the number of labels returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetlabelDetection`` and populate the ``NextToken`` request parameter with the token value returned from the previous call to ``GetLabelDetection`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetLabelDetection>`_    


    **Request Syntax** 
    ::

      response = client.get_label_detection(
          JobId='string',
          MaxResults=123,
          NextToken='string',
          SortBy='NAME'|'TIMESTAMP'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      Job identifier for the label detection operation for which you want results returned. You get the job identifer from an initial call to ``StartlabelDetection`` .

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of labels you want Amazon Rekognition to return in the response. The default is 1000.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there are more labels to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of labels. 

      

    
    :type SortBy: string
    :param SortBy: 

      Sort to use for elements in the ``Labels`` array. Use ``TIMESTAMP`` to sort array elements by the time labels are detected. Use ``NAME`` to alphabetically group elements for a label together. Within each label group, the array element are sorted by detection confidence. The default sort is by ``TIMESTAMP`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'NextToken': 'string',
            'Labels': [
                {
                    'Timestamp': 123,
                    'Label': {
                        'Name': 'string',
                        'Confidence': ...
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the label detection job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Rekognition Video analyzed. ``Videometadata`` is returned in every page of paginated responses from a Amazon Rekognition video operation.

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of labels.

          
        

        - **Labels** *(list) --* 

          An array of labels detected in the video. Each element contains the detected label and the time, in milliseconds from the start of the video, that the label was detected. 

          
          

          - *(dict) --* 

            Information about a label detected in a video analysis request and the time the label was detected in the video. 

            
            

            - **Timestamp** *(integer) --* 

              Time, in milliseconds from the start of the video, that the label was detected.

              
            

            - **Label** *(dict) --* 

              Details about the detected label.

              
              

              - **Name** *(string) --* 

                The name (label) of the object.

                
              

              - **Confidence** *(float) --* 

                Level of confidence.

                
          
        
      
    

  .. py:method:: get_paginator(operation_name)

        
    Create a paginator for an operation.
    
    :type operation_name: string
    :param operation_name: The operation name.  This is the same name
        as the method name on the client.  For example, if the
        method name is ``create_foo``, and you'd normally invoke the
        operation as ``client.create_foo(**kwargs)``, if the
        ``create_foo`` operation can be paginated, you can use the
        call ``client.get_paginator("create_foo")``.
    
    :raise OperationNotPageableError: Raised if the operation is not
        pageable.  You can use the ``client.can_paginate`` method to
        check if an operation is pageable.
    
    :rtype: L{botocore.paginate.Paginator}
    :return: A paginator object.


  .. py:method:: get_person_tracking(**kwargs)

    

    Gets the person tracking results of a Rekognition Video analysis started by .

     

    The person detection operation is started by a call to ``StartPersonTracking`` which returns a job identifier (``JobId`` ). When the person detection operation finishes, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic registered in the initial call to ``StartPersonTracking`` .

     

    To get the results of the person tracking operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartPersonTracking`` .

     

     ``GetPersonTracking`` returns an array, ``Persons`` , of tracked persons and the time(s) they were tracked in the video. 

     

    By default, the array is sorted by the time(s) a person is tracked in the video. You can sort by tracked persons by specifying ``INDEX`` for the ``SortBy`` input parameter.

     

    Use the ``MaxResults`` parameter to limit the number of items returned. If there are more results than specified in ``MaxResults`` , the value of ``NextToken`` in the operation response contains a pagination token for getting the next set of results. To get the next page of results, call ``GetPersonTracking`` and populate the ``NextToken`` request parameter with the token value returned from the previous call to ``GetPersonTracking`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/GetPersonTracking>`_    


    **Request Syntax** 
    ::

      response = client.get_person_tracking(
          JobId='string',
          MaxResults=123,
          NextToken='string',
          SortBy='INDEX'|'TIMESTAMP'
      )
    :type JobId: string
    :param JobId: **[REQUIRED]** 

      The identifier for a job that tracks persons in a video. You get the ``JobId`` from a call to ``StartPersonTracking`` . 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of tracked persons to return. The default is 1000. 

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there are more persons to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of persons. 

      

    
    :type SortBy: string
    :param SortBy: 

      Sort to use for elements in the ``Persons`` array. Use ``TIMESTAMP`` to sort array elements by the time persons are detected. Use ``INDEX`` to sort by the tracked persons. If you sort by ``INDEX`` , the array elements for each person are sorted by detection confidence. The default sort is by ``TIMESTAMP`` .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobStatus': 'IN_PROGRESS'|'SUCCEEDED'|'FAILED',
            'StatusMessage': 'string',
            'VideoMetadata': {
                'Codec': 'string',
                'DurationMillis': 123,
                'Format': 'string',
                'FrameRate': ...,
                'FrameHeight': 123,
                'FrameWidth': 123
            },
            'NextToken': 'string',
            'Persons': [
                {
                    'Timestamp': 123,
                    'Person': {
                        'Index': 123,
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Face': {
                            'BoundingBox': {
                                'Width': ...,
                                'Height': ...,
                                'Left': ...,
                                'Top': ...
                            },
                            'AgeRange': {
                                'Low': 123,
                                'High': 123
                            },
                            'Smile': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Eyeglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Sunglasses': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Gender': {
                                'Value': 'Male'|'Female',
                                'Confidence': ...
                            },
                            'Beard': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Mustache': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'EyesOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'MouthOpen': {
                                'Value': True|False,
                                'Confidence': ...
                            },
                            'Emotions': [
                                {
                                    'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                    'Confidence': ...
                                },
                            ],
                            'Landmarks': [
                                {
                                    'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                    'X': ...,
                                    'Y': ...
                                },
                            ],
                            'Pose': {
                                'Roll': ...,
                                'Yaw': ...,
                                'Pitch': ...
                            },
                            'Quality': {
                                'Brightness': ...,
                                'Sharpness': ...
                            },
                            'Confidence': ...
                        }
                    }
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobStatus** *(string) --* 

          The current status of the person tracking job.

          
        

        - **StatusMessage** *(string) --* 

          If the job fails, ``StatusMessage`` provides a descriptive error message.

          
        

        - **VideoMetadata** *(dict) --* 

          Information about a video that Rekognition Video analyzed. ``Videometadata`` is returned in every page of paginated responses from a Rekognition Video operation.

          
          

          - **Codec** *(string) --* 

            Type of compression used in the analyzed video. 

            
          

          - **DurationMillis** *(integer) --* 

            Length of the video in milliseconds.

            
          

          - **Format** *(string) --* 

            Format of the analyzed video. Possible values are MP4, MOV and AVI. 

            
          

          - **FrameRate** *(float) --* 

            Number of frames per second in the video.

            
          

          - **FrameHeight** *(integer) --* 

            Vertical pixel dimension of the video.

            
          

          - **FrameWidth** *(integer) --* 

            Horizontal pixel dimension of the video.

            
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of persons. 

          
        

        - **Persons** *(list) --* 

          An array of the persons detected in the video and the times they are tracked throughout the video. An array element will exist for each time the person is tracked. 

          
          

          - *(dict) --* 

            Details and tracking information for a single time a person is tracked in a video. Amazon Rekognition operations that track persons return an array of ``PersonDetection`` objects with elements for each time a person is tracked in a video. For more information, see . 

            
            

            - **Timestamp** *(integer) --* 

              The time, in milliseconds from the start of the video, that the person was tracked.

              
            

            - **Person** *(dict) --* 

              Details about a person tracked in a video.

              
              

              - **Index** *(integer) --* 

                Identifier for the person detected person within a video. Use to keep track of the person throughout the video. The identifier is not stored by Amazon Rekognition.

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box around the detected person.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Face** *(dict) --* 

                Face details for the detected person.

                
                

                - **BoundingBox** *(dict) --* 

                  Bounding box of the face.

                  
                  

                  - **Width** *(float) --* 

                    Width of the bounding box as a ratio of the overall image width.

                    
                  

                  - **Height** *(float) --* 

                    Height of the bounding box as a ratio of the overall image height.

                    
                  

                  - **Left** *(float) --* 

                    Left coordinate of the bounding box as a ratio of overall image width.

                    
                  

                  - **Top** *(float) --* 

                    Top coordinate of the bounding box as a ratio of overall image height.

                    
              
                

                - **AgeRange** *(dict) --* 

                  The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

                  
                  

                  - **Low** *(integer) --* 

                    The lowest estimated age.

                    
                  

                  - **High** *(integer) --* 

                    The highest estimated age.

                    
              
                

                - **Smile** *(dict) --* 

                  Indicates whether or not the face is smiling, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is smiling or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Eyeglasses** *(dict) --* 

                  Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing eye glasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Sunglasses** *(dict) --* 

                  Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face is wearing sunglasses or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Gender** *(dict) --* 

                  Gender of the face and the confidence level in the determination.

                  
                  

                  - **Value** *(string) --* 

                    Gender of the face.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Beard** *(dict) --* 

                  Indicates whether or not the face has a beard, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has beard or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Mustache** *(dict) --* 

                  Indicates whether or not the face has a mustache, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the face has mustache or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **EyesOpen** *(dict) --* 

                  Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the eyes on the face are open.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **MouthOpen** *(dict) --* 

                  Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

                  
                  

                  - **Value** *(boolean) --* 

                    Boolean value that indicates whether the mouth on the face is open or not.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
                

                - **Emotions** *(list) --* 

                  The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

                  
                  

                  - *(dict) --* 

                    The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                    
                    

                    - **Type** *(string) --* 

                      Type of emotion detected.

                      
                    

                    - **Confidence** *(float) --* 

                      Level of confidence in the determination.

                      
                
              
                

                - **Landmarks** *(list) --* 

                  Indicates the location of landmarks on the face.

                  
                  

                  - *(dict) --* 

                    Indicates the location of the landmark on the face.

                    
                    

                    - **Type** *(string) --* 

                      Type of the landmark.

                      
                    

                    - **X** *(float) --* 

                      x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                      
                    

                    - **Y** *(float) --* 

                      y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                      
                
              
                

                - **Pose** *(dict) --* 

                  Indicates the pose of the face as determined by its pitch, roll, and yaw.

                  
                  

                  - **Roll** *(float) --* 

                    Value representing the face rotation on the roll axis.

                    
                  

                  - **Yaw** *(float) --* 

                    Value representing the face rotation on the yaw axis.

                    
                  

                  - **Pitch** *(float) --* 

                    Value representing the face rotation on the pitch axis.

                    
              
                

                - **Quality** *(dict) --* 

                  Identifies image brightness and sharpness.

                  
                  

                  - **Brightness** *(float) --* 

                    Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                    
                  

                  - **Sharpness** *(float) --* 

                    Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                    
              
                

                - **Confidence** *(float) --* 

                  Confidence level that the bounding box contains a face (and not a different object such as a tree).

                  
            
          
        
      
    

  .. py:method:: get_waiter(waiter_name)

        


  .. py:method:: index_faces(**kwargs)

    

    Detects faces in the input image and adds them to the specified collection. 

     

    Amazon Rekognition does not save the actual faces detected. Instead, the underlying detection algorithm first detects the faces in the input image, and for each face extracts facial features into a feature vector, and stores it in the back-end database. Amazon Rekognition uses feature vectors when performing face match and search operations using the and operations.

     

    If you are using version 1.0 of the face detection model, ``IndexFaces`` indexes the 15 largest faces in the input image. Later versions of the face detection model index the 100 largest faces in the input image. To determine which version of the model you are using, check the the value of ``FaceModelVersion`` in the response from ``IndexFaces`` . For more information, see  face-detection-model .

     

    If you provide the optional ``ExternalImageID`` for the input image you provided, Amazon Rekognition associates this ID with all faces that it detects. When you call the operation, the response returns the external ID. You can use this external image ID to create a client-side index to associate the faces with each image. You can then use the index to find all faces in an image. 

     

    In response, the operation returns an array of metadata for all detected faces. This includes, the bounding box of the detected face, confidence value (indicating the bounding box contains a face), a face ID assigned by the service for each face that is detected and stored, and an image ID assigned by the service for the input image. If you request all facial attributes (using the ``detectionAttributes`` parameter, Amazon Rekognition returns detailed facial attributes such as facial landmarks (for example, location of eye and mount) and other facial attributes such gender. If you provide the same image, specify the same collection, and use the same external ID in the ``IndexFaces`` operation, Amazon Rekognition doesn't save duplicate face metadata. 

     

    The input image is passed either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    This operation requires permissions to perform the ``rekognition:IndexFaces`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/IndexFaces>`_    


    **Request Syntax** 
    ::

      response = client.index_faces(
          CollectionId='string',
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ExternalImageId='string',
          DetectionAttributes=[
              'DEFAULT'|'ALL',
          ]
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      The ID of an existing collection to which you want to add the faces that are detected in the input images.

      

    
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ExternalImageId: string
    :param ExternalImageId: 

      ID you want to assign to all the faces detected in the image.

      

    
    :type DetectionAttributes: list
    :param DetectionAttributes: 

      An array of facial attributes that you want to be returned. This can be the default list of attributes or all attributes. If you don't specify a value for ``Attributes`` or if you specify ``["DEFAULT"]`` , the API returns the following subset of facial attributes: ``BoundingBox`` , ``Confidence`` , ``Pose`` , ``Quality`` and ``Landmarks`` . If you provide ``["ALL"]`` , all facial attributes are returned but the operation will take longer to complete.

       

      If you provide both, ``["ALL", "DEFAULT"]`` , the service uses a logical AND operator to determine which attributes to return (in this case, all attributes). 

      

    
      - *(string) --* 

      
  
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'FaceRecords': [
                {
                    'Face': {
                        'FaceId': 'string',
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'ImageId': 'string',
                        'ExternalImageId': 'string',
                        'Confidence': ...
                    },
                    'FaceDetail': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'AgeRange': {
                            'Low': 123,
                            'High': 123
                        },
                        'Smile': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Eyeglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Sunglasses': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Gender': {
                            'Value': 'Male'|'Female',
                            'Confidence': ...
                        },
                        'Beard': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Mustache': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'EyesOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'MouthOpen': {
                            'Value': True|False,
                            'Confidence': ...
                        },
                        'Emotions': [
                            {
                                'Type': 'HAPPY'|'SAD'|'ANGRY'|'CONFUSED'|'DISGUSTED'|'SURPRISED'|'CALM'|'UNKNOWN',
                                'Confidence': ...
                            },
                        ],
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        },
                        'Confidence': ...
                    }
                },
            ],
            'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270',
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **FaceRecords** *(list) --* 

          An array of faces detected and added to the collection. For more information, see  collections-index-faces . 

          
          

          - *(dict) --* 

            Object containing both the face metadata (stored in the back-end database) and facial attributes that are detected but aren't stored in the database.

            
            

            - **Face** *(dict) --* 

              Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned. 

              
              

              - **FaceId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the face.

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **ImageId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the input image.

                
              

              - **ExternalImageId** *(string) --* 

                Identifier that you assign to all the faces in the input image.

                
              

              - **Confidence** *(float) --* 

                Confidence level that the bounding box contains a face (and not a different object such as a tree).

                
          
            

            - **FaceDetail** *(dict) --* 

              Structure containing attributes of the face that the algorithm detected.

              
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **AgeRange** *(dict) --* 

                The estimated age range, in years, for the face. Low represents the lowest estimated age and High represents the highest estimated age.

                
                

                - **Low** *(integer) --* 

                  The lowest estimated age.

                  
                

                - **High** *(integer) --* 

                  The highest estimated age.

                  
            
              

              - **Smile** *(dict) --* 

                Indicates whether or not the face is smiling, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is smiling or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Eyeglasses** *(dict) --* 

                Indicates whether or not the face is wearing eye glasses, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is wearing eye glasses or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Sunglasses** *(dict) --* 

                Indicates whether or not the face is wearing sunglasses, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face is wearing sunglasses or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Gender** *(dict) --* 

                Gender of the face and the confidence level in the determination.

                
                

                - **Value** *(string) --* 

                  Gender of the face.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Beard** *(dict) --* 

                Indicates whether or not the face has a beard, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face has beard or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Mustache** *(dict) --* 

                Indicates whether or not the face has a mustache, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the face has mustache or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **EyesOpen** *(dict) --* 

                Indicates whether or not the eyes on the face are open, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the eyes on the face are open.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **MouthOpen** *(dict) --* 

                Indicates whether or not the mouth on the face is open, and the confidence level in the determination.

                
                

                - **Value** *(boolean) --* 

                  Boolean value that indicates whether the mouth on the face is open or not.

                  
                

                - **Confidence** *(float) --* 

                  Level of confidence in the determination.

                  
            
              

              - **Emotions** *(list) --* 

                The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY. 

                
                

                - *(dict) --* 

                  The emotions detected on the face, and the confidence level in the determination. For example, HAPPY, SAD, and ANGRY.

                  
                  

                  - **Type** *(string) --* 

                    Type of emotion detected.

                    
                  

                  - **Confidence** *(float) --* 

                    Level of confidence in the determination.

                    
              
            
              

              - **Landmarks** *(list) --* 

                Indicates the location of landmarks on the face.

                
                

                - *(dict) --* 

                  Indicates the location of the landmark on the face.

                  
                  

                  - **Type** *(string) --* 

                    Type of the landmark.

                    
                  

                  - **X** *(float) --* 

                    x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                    
                  

                  - **Y** *(float) --* 

                    y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    
              
            
              

              - **Pose** *(dict) --* 

                Indicates the pose of the face as determined by its pitch, roll, and yaw.

                
                

                - **Roll** *(float) --* 

                  Value representing the face rotation on the roll axis.

                  
                

                - **Yaw** *(float) --* 

                  Value representing the face rotation on the yaw axis.

                  
                

                - **Pitch** *(float) --* 

                  Value representing the face rotation on the pitch axis.

                  
            
              

              - **Quality** *(dict) --* 

                Identifies image brightness and sharpness.

                
                

                - **Brightness** *(float) --* 

                  Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                  
                

                - **Sharpness** *(float) --* 

                  Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                  
            
              

              - **Confidence** *(float) --* 

                Confidence level that the bounding box contains a face (and not a different object such as a tree).

                
          
        
      
        

        - **OrientationCorrection** *(string) --* 

          The orientation of the input image (counterclockwise direction). If your application displays the image, you can use this value to correct image orientation. The bounding box coordinates returned in ``FaceRecords`` represent face locations before the image orientation is corrected. 

           

          .. note::

             

            If the input image is in jpeg format, it might contain exchangeable image (Exif) metadata. If so, and the Exif metadata populates the orientation field, the value of ``OrientationCorrection`` is null and the bounding box coordinates in ``FaceRecords`` represent face locations after Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata.

             

          
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the input collection (``CollectionId`` ).

          
    

    **Examples** 

    This operation detects faces in an image and adds them to the specified Rekognition collection.
    ::

      response = client.index_faces(
          CollectionId='myphotos',
          DetectionAttributes=[
          ],
          ExternalImageId='myphotoid',
          Image={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'myphoto',
              },
          },
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FaceRecords': [
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.33481481671333313,
                          'Left': 0.31888890266418457,
                          'Top': 0.4933333396911621,
                          'Width': 0.25,
                      },
                      'Confidence': 99.9991226196289,
                      'FaceId': 'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
                      'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
                  },
                  'FaceDetail': {
                      'BoundingBox': {
                          'Height': 0.33481481671333313,
                          'Left': 0.31888890266418457,
                          'Top': 0.4933333396911621,
                          'Width': 0.25,
                      },
                      'Confidence': 99.9991226196289,
                      'Landmarks': [
                          {
                              'Type': 'EYE_LEFT',
                              'X': 0.3976764678955078,
                              'Y': 0.6248345971107483,
                          },
                          {
                              'Type': 'EYE_RIGHT',
                              'X': 0.4810936450958252,
                              'Y': 0.6317117214202881,
                          },
                          {
                              'Type': 'NOSE_LEFT',
                              'X': 0.41986238956451416,
                              'Y': 0.7111940383911133,
                          },
                          {
                              'Type': 'MOUTH_DOWN',
                              'X': 0.40525302290916443,
                              'Y': 0.7497701048851013,
                          },
                          {
                              'Type': 'MOUTH_UP',
                              'X': 0.4753248989582062,
                              'Y': 0.7558549642562866,
                          },
                      ],
                      'Pose': {
                          'Pitch': -9.713645935058594,
                          'Roll': 4.707281112670898,
                          'Yaw': -24.438663482666016,
                      },
                      'Quality': {
                          'Brightness': 29.23358917236328,
                          'Sharpness': 80,
                      },
                  },
              },
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.32592591643333435,
                          'Left': 0.5144444704055786,
                          'Top': 0.15111111104488373,
                          'Width': 0.24444444477558136,
                      },
                      'Confidence': 99.99950408935547,
                      'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
                      'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
                  },
                  'FaceDetail': {
                      'BoundingBox': {
                          'Height': 0.32592591643333435,
                          'Left': 0.5144444704055786,
                          'Top': 0.15111111104488373,
                          'Width': 0.24444444477558136,
                      },
                      'Confidence': 99.99950408935547,
                      'Landmarks': [
                          {
                              'Type': 'EYE_LEFT',
                              'X': 0.6006892323493958,
                              'Y': 0.290842205286026,
                          },
                          {
                              'Type': 'EYE_RIGHT',
                              'X': 0.6808141469955444,
                              'Y': 0.29609042406082153,
                          },
                          {
                              'Type': 'NOSE_LEFT',
                              'X': 0.6395332217216492,
                              'Y': 0.3522595763206482,
                          },
                          {
                              'Type': 'MOUTH_DOWN',
                              'X': 0.5892083048820496,
                              'Y': 0.38689887523651123,
                          },
                          {
                              'Type': 'MOUTH_UP',
                              'X': 0.674560010433197,
                              'Y': 0.394125759601593,
                          },
                      ],
                      'Pose': {
                          'Pitch': -4.683138370513916,
                          'Roll': 2.1029529571533203,
                          'Yaw': 6.716655254364014,
                      },
                      'Quality': {
                          'Brightness': 34.951698303222656,
                          'Sharpness': 160,
                      },
                  },
              },
          ],
          'OrientationCorrection': 'ROTATE_0',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_collections(**kwargs)

    

    Returns list of collection IDs in your account. If the result is truncated, the response also provides a ``NextToken`` that you can use in the subsequent request to fetch the next set of collection IDs.

     

    For an example, see  list-collection-procedure .

     

    This operation requires permissions to perform the ``rekognition:ListCollections`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListCollections>`_    


    **Request Syntax** 
    ::

      response = client.list_collections(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      Pagination token from the previous response.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of collection IDs to return. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CollectionIds': [
                'string',
            ],
            'NextToken': 'string',
            'FaceModelVersions': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CollectionIds** *(list) --* 

          An array of collection IDs.

          
          

          - *(string) --* 
      
        

        - **NextToken** *(string) --* 

          If the result is truncated, the response provides a ``NextToken`` that you can use in the subsequent request to fetch the next set of collection IDs.

          
        

        - **FaceModelVersions** *(list) --* 

          Version numbers of the face detection models associated with the collections in the array ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the version number for the face detection model used by the collection in ``CollectionId[2]`` .

          
          

          - *(string) --* 
      
    

    **Examples** 

    This operation returns a list of Rekognition collections.
    ::

      response = client.list_collections(
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'CollectionIds': [
              'myphotos',
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_faces(**kwargs)

    

    Returns metadata for faces in the specified collection. This metadata includes information such as the bounding box coordinates, the confidence (that the bounding box contains a face), and face ID. For an example, see  list-faces-in-collection-procedure . 

     

    This operation requires permissions to perform the ``rekognition:ListFaces`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListFaces>`_    


    **Request Syntax** 
    ::

      response = client.list_faces(
          CollectionId='string',
          NextToken='string',
          MaxResults=123
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection from which to list the faces.

      

    
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there is more data to retrieve), Amazon Rekognition returns a pagination token in the response. You can use this pagination token to retrieve the next set of faces.

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of faces to return.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Faces': [
                {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                },
            ],
            'NextToken': 'string',
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Faces** *(list) --* 

          An array of ``Face`` objects. 

          
          

          - *(dict) --* 

            Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned. 

            
            

            - **FaceId** *(string) --* 

              Unique identifier that Amazon Rekognition assigns to the face.

              
            

            - **BoundingBox** *(dict) --* 

              Bounding box of the face.

              
              

              - **Width** *(float) --* 

                Width of the bounding box as a ratio of the overall image width.

                
              

              - **Height** *(float) --* 

                Height of the bounding box as a ratio of the overall image height.

                
              

              - **Left** *(float) --* 

                Left coordinate of the bounding box as a ratio of overall image width.

                
              

              - **Top** *(float) --* 

                Top coordinate of the bounding box as a ratio of overall image height.

                
          
            

            - **ImageId** *(string) --* 

              Unique identifier that Amazon Rekognition assigns to the input image.

              
            

            - **ExternalImageId** *(string) --* 

              Identifier that you assign to all the faces in the input image.

              
            

            - **Confidence** *(float) --* 

              Confidence level that the bounding box contains a face (and not a different object such as a tree).

              
        
      
        

        - **NextToken** *(string) --* 

          If the response is truncated, Amazon Rekognition returns this token that you can use in the subsequent request to retrieve the next set of faces.

          
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the input collection (``CollectionId`` ).

          
    

    **Examples** 

    This operation lists the faces in a Rekognition collection.
    ::

      response = client.list_faces(
          CollectionId='myphotos',
          MaxResults=20,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'Faces': [
              {
                  'BoundingBox': {
                      'Height': 0.18000000715255737,
                      'Left': 0.5555559992790222,
                      'Top': 0.336667001247406,
                      'Width': 0.23999999463558197,
                  },
                  'Confidence': 100,
                  'FaceId': '1c62e8b5-69a7-5b7d-b3cd-db4338a8a7e7',
                  'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
              },
              {
                  'BoundingBox': {
                      'Height': 0.16555599868297577,
                      'Left': 0.30963000655174255,
                      'Top': 0.7066670060157776,
                      'Width': 0.22074100375175476,
                  },
                  'Confidence': 100,
                  'FaceId': '29a75abe-397b-5101-ba4f-706783b2246c',
                  'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
              },
              {
                  'BoundingBox': {
                      'Height': 0.3234420120716095,
                      'Left': 0.3233329951763153,
                      'Top': 0.5,
                      'Width': 0.24222199618816376,
                  },
                  'Confidence': 99.99829864501953,
                  'FaceId': '38271d79-7bc2-5efb-b752-398a8d575b85',
                  'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
              },
              {
                  'BoundingBox': {
                      'Height': 0.03555560111999512,
                      'Left': 0.37388700246810913,
                      'Top': 0.2477779984474182,
                      'Width': 0.04747769981622696,
                  },
                  'Confidence': 99.99210357666016,
                  'FaceId': '3b01bef0-c883-5654-ba42-d5ad28b720b3',
                  'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
              },
              {
                  'BoundingBox': {
                      'Height': 0.05333330109715462,
                      'Left': 0.2937690019607544,
                      'Top': 0.35666701197624207,
                      'Width': 0.07121659815311432,
                  },
                  'Confidence': 99.99919891357422,
                  'FaceId': '4839a608-49d0-566c-8301-509d71b534d1',
                  'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
              },
              {
                  'BoundingBox': {
                      'Height': 0.3249259889125824,
                      'Left': 0.5155559778213501,
                      'Top': 0.1513350009918213,
                      'Width': 0.24333299696445465,
                  },
                  'Confidence': 99.99949645996094,
                  'FaceId': '70008e50-75e4-55d0-8e80-363fb73b3a14',
                  'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
              },
              {
                  'BoundingBox': {
                      'Height': 0.03777780011296272,
                      'Left': 0.7002969980239868,
                      'Top': 0.18777799606323242,
                      'Width': 0.05044509842991829,
                  },
                  'Confidence': 99.92639923095703,
                  'FaceId': '7f5f88ed-d684-5a88-b0df-01e4a521552b',
                  'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
              },
              {
                  'BoundingBox': {
                      'Height': 0.05555560067296028,
                      'Left': 0.13946600258350372,
                      'Top': 0.46333301067352295,
                      'Width': 0.07270029932260513,
                  },
                  'Confidence': 99.99469757080078,
                  'FaceId': '895b4e2c-81de-5902-a4bd-d1792bda00b2',
                  'ImageId': '812d9f04-86f9-54fc-9275-8d0dcbcb6784',
              },
              {
                  'BoundingBox': {
                      'Height': 0.3259260058403015,
                      'Left': 0.5144439935684204,
                      'Top': 0.15111100673675537,
                      'Width': 0.24444399774074554,
                  },
                  'Confidence': 99.99949645996094,
                  'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
                  'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
              },
              {
                  'BoundingBox': {
                      'Height': 0.18888899683952332,
                      'Left': 0.3783380091190338,
                      'Top': 0.2355560064315796,
                      'Width': 0.25222599506378174,
                  },
                  'Confidence': 99.9999008178711,
                  'FaceId': '908544ad-edc3-59df-8faf-6a87cc256cf5',
                  'ImageId': '3c731605-d772-541a-a5e7-0375dbc68a07',
              },
              {
                  'BoundingBox': {
                      'Height': 0.33481499552726746,
                      'Left': 0.31888899207115173,
                      'Top': 0.49333301186561584,
                      'Width': 0.25,
                  },
                  'Confidence': 99.99909973144531,
                  'FaceId': 'ff43d742-0c13-5d16-a3e8-03d3f58e980b',
                  'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
              },
          ],
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: list_stream_processors(**kwargs)

    

    Gets a list of stream processors that you have created with . 

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListStreamProcessors>`_    


    **Request Syntax** 
    ::

      response = client.list_stream_processors(
          NextToken='string',
          MaxResults=123
      )
    :type NextToken: string
    :param NextToken: 

      If the previous response was incomplete (because there are more stream processors to retrieve), Rekognition Video returns a pagination token in the response. You can use this pagination token to retrieve the next set of stream processors. 

      

    
    :type MaxResults: integer
    :param MaxResults: 

      Maximum number of stream processors you want Rekognition Video to return in the response. The default is 1000. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'NextToken': 'string',
            'StreamProcessors': [
                {
                    'Name': 'string',
                    'Status': 'STOPPED'|'STARTING'|'RUNNING'|'FAILED'|'STOPPING'
                },
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **NextToken** *(string) --* 

          If the response is truncated, Rekognition Video returns this token that you can use in the subsequent request to retrieve the next set of stream processors. 

          
        

        - **StreamProcessors** *(list) --* 

          List of stream processors that you have created.

          
          

          - *(dict) --* 

            An object that recognizes faces in a streaming video. An Amazon Rekognition stream processor is created by a call to . The request parameters for ``CreateStreamProcessor`` describe the Kinesis video stream source for the streaming video, face recognition parameters, and where to stream the analysis resullts. 

            
            

            - **Name** *(string) --* 

              Name of the Amazon Rekognition stream processor. 

              
            

            - **Status** *(string) --* 

              Current status of the Amazon Rekognition stream processor.

              
        
      
    

  .. py:method:: recognize_celebrities(**kwargs)

    

    Returns an array of celebrities recognized in the input image. For more information, see  celebrities . 

     

     ``RecognizeCelebrities`` returns the 100 largest faces in the image. It lists recognized celebrities in the ``CelebrityFaces`` array and unrecognized faces in the ``UnrecognizedFaces`` array. ``RecognizeCelebrities`` doesn't return celebrities whose faces are not amongst the largest 100 faces in the image.

     

    For each celebrity recognized, the ``RecognizeCelebrities`` returns a ``Celebrity`` object. The ``Celebrity`` object contains the celebrity name, ID, URL links to additional information, match confidence, and a ``ComparedFace`` object that you can use to locate the celebrity's face on the image.

     

    Rekognition does not retain information about which images a celebrity has been recognized in. Your application must store this information and use the ``Celebrity`` ID property as a unique identifier for the celebrity. If you don't store the celebrity name or additional information URLs returned by ``RecognizeCelebrities`` , you will need the ID to identify the celebrity in a call to the operation.

     

    You pass the imput image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    For an example, see  celebrities-procedure-image .

     

    This operation requires permissions to perform the ``rekognition:RecognizeCelebrities`` operation.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/RecognizeCelebrities>`_    


    **Request Syntax** 
    ::

      response = client.recognize_celebrities(
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          }
      )
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CelebrityFaces': [
                {
                    'Urls': [
                        'string',
                    ],
                    'Name': 'string',
                    'Id': 'string',
                    'Face': {
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'Confidence': ...,
                        'Landmarks': [
                            {
                                'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                                'X': ...,
                                'Y': ...
                            },
                        ],
                        'Pose': {
                            'Roll': ...,
                            'Yaw': ...,
                            'Pitch': ...
                        },
                        'Quality': {
                            'Brightness': ...,
                            'Sharpness': ...
                        }
                    },
                    'MatchConfidence': ...
                },
            ],
            'UnrecognizedFaces': [
                {
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'Confidence': ...,
                    'Landmarks': [
                        {
                            'Type': 'eyeLeft'|'eyeRight'|'nose'|'mouthLeft'|'mouthRight'|'leftEyeBrowLeft'|'leftEyeBrowRight'|'leftEyeBrowUp'|'rightEyeBrowLeft'|'rightEyeBrowRight'|'rightEyeBrowUp'|'leftEyeLeft'|'leftEyeRight'|'leftEyeUp'|'leftEyeDown'|'rightEyeLeft'|'rightEyeRight'|'rightEyeUp'|'rightEyeDown'|'noseLeft'|'noseRight'|'mouthUp'|'mouthDown'|'leftPupil'|'rightPupil',
                            'X': ...,
                            'Y': ...
                        },
                    ],
                    'Pose': {
                        'Roll': ...,
                        'Yaw': ...,
                        'Pitch': ...
                    },
                    'Quality': {
                        'Brightness': ...,
                        'Sharpness': ...
                    }
                },
            ],
            'OrientationCorrection': 'ROTATE_0'|'ROTATE_90'|'ROTATE_180'|'ROTATE_270'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CelebrityFaces** *(list) --* 

          Details about each celebrity found in the image. Amazon Rekognition can detect a maximum of 15 celebrities in an image.

          
          

          - *(dict) --* 

            Provides information about a celebrity recognized by the operation.

            
            

            - **Urls** *(list) --* 

              An array of URLs pointing to additional information about the celebrity. If there is no additional information about the celebrity, this list is empty.

              
              

              - *(string) --* 
          
            

            - **Name** *(string) --* 

              The name of the celebrity.

              
            

            - **Id** *(string) --* 

              A unique identifier for the celebrity. 

              
            

            - **Face** *(dict) --* 

              Provides information about the celebrity's face, such as its location on the image.

              
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **Confidence** *(float) --* 

                Level of confidence that what the bounding box contains is a face.

                
              

              - **Landmarks** *(list) --* 

                An array of facial landmarks.

                
                

                - *(dict) --* 

                  Indicates the location of the landmark on the face.

                  
                  

                  - **Type** *(string) --* 

                    Type of the landmark.

                    
                  

                  - **X** *(float) --* 

                    x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                    
                  

                  - **Y** *(float) --* 

                    y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                    
              
            
              

              - **Pose** *(dict) --* 

                Indicates the pose of the face as determined by its pitch, roll, and yaw.

                
                

                - **Roll** *(float) --* 

                  Value representing the face rotation on the roll axis.

                  
                

                - **Yaw** *(float) --* 

                  Value representing the face rotation on the yaw axis.

                  
                

                - **Pitch** *(float) --* 

                  Value representing the face rotation on the pitch axis.

                  
            
              

              - **Quality** *(dict) --* 

                Identifies face image brightness and sharpness. 

                
                

                - **Brightness** *(float) --* 

                  Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                  
                

                - **Sharpness** *(float) --* 

                  Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                  
            
          
            

            - **MatchConfidence** *(float) --* 

              The confidence, in percentage, that Rekognition has that the recognized face is the celebrity.

              
        
      
        

        - **UnrecognizedFaces** *(list) --* 

          Details about each unrecognized face in the image.

          
          

          - *(dict) --* 

            Provides face metadata for target image faces that are analysed by ``CompareFaces`` and ``RecognizeCelebrities`` .

            
            

            - **BoundingBox** *(dict) --* 

              Bounding box of the face.

              
              

              - **Width** *(float) --* 

                Width of the bounding box as a ratio of the overall image width.

                
              

              - **Height** *(float) --* 

                Height of the bounding box as a ratio of the overall image height.

                
              

              - **Left** *(float) --* 

                Left coordinate of the bounding box as a ratio of overall image width.

                
              

              - **Top** *(float) --* 

                Top coordinate of the bounding box as a ratio of overall image height.

                
          
            

            - **Confidence** *(float) --* 

              Level of confidence that what the bounding box contains is a face.

              
            

            - **Landmarks** *(list) --* 

              An array of facial landmarks.

              
              

              - *(dict) --* 

                Indicates the location of the landmark on the face.

                
                

                - **Type** *(string) --* 

                  Type of the landmark.

                  
                

                - **X** *(float) --* 

                  x-coordinate from the top left of the landmark expressed as the ratio of the width of the image. For example, if the images is 700x200 and the x-coordinate of the landmark is at 350 pixels, this value is 0.5. 

                  
                

                - **Y** *(float) --* 

                  y-coordinate from the top left of the landmark expressed as the ratio of the height of the image. For example, if the images is 700x200 and the y-coordinate of the landmark is at 100 pixels, this value is 0.5.

                  
            
          
            

            - **Pose** *(dict) --* 

              Indicates the pose of the face as determined by its pitch, roll, and yaw.

              
              

              - **Roll** *(float) --* 

                Value representing the face rotation on the roll axis.

                
              

              - **Yaw** *(float) --* 

                Value representing the face rotation on the yaw axis.

                
              

              - **Pitch** *(float) --* 

                Value representing the face rotation on the pitch axis.

                
          
            

            - **Quality** *(dict) --* 

              Identifies face image brightness and sharpness. 

              
              

              - **Brightness** *(float) --* 

                Value representing brightness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a brighter face image.

                
              

              - **Sharpness** *(float) --* 

                Value representing sharpness of the face. The service returns a value between 0 and 100 (inclusive). A higher value indicates a sharper face image.

                
          
        
      
        

        - **OrientationCorrection** *(string) --* 

          The orientation of the input image (counterclockwise direction). If your application displays the image, you can use this value to correct the orientation. The bounding box coordinates returned in ``CelebrityFaces`` and ``UnrecognizedFaces`` represent face locations before the image orientation is corrected. 

           

          .. note::

             

            If the input image is in .jpeg format, it might contain exchangeable image (Exif) metadata that includes the image's orientation. If so, and the Exif metadata for the input image populates the orientation field, the value of ``OrientationCorrection`` is null and the ``CelebrityFaces`` and ``UnrecognizedFaces`` bounding box coordinates represent face locations after Exif metadata is used to correct the image orientation. Images in .png format don't contain Exif metadata. 

             

          
    

  .. py:method:: search_faces(**kwargs)

    

    For a given input face ID, searches for matching faces in the collection the face belongs to. You get a face ID when you add a face to the collection using the  IndexFaces operation. The operation compares the features of the input face with faces in the specified collection. 

     

    .. note::

       

      You can also search faces without indexing faces by using the ``SearchFacesByImage`` operation.

       

     

    The operation response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match that is found. Along with the metadata, the response also includes a ``confidence`` value for each face match, indicating the confidence that the specific face matches the input face. 

     

    For an example, see  search-face-with-id-procedure .

     

    This operation requires permissions to perform the ``rekognition:SearchFaces`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchFaces>`_    


    **Request Syntax** 
    ::

      response = client.search_faces(
          CollectionId='string',
          FaceId='string',
          MaxFaces=123,
          FaceMatchThreshold=...
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection the face belongs to.

      

    
    :type FaceId: string
    :param FaceId: **[REQUIRED]** 

      ID of a face to find matches for in the collection.

      

    
    :type MaxFaces: integer
    :param MaxFaces: 

      Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

      

    
    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: 

      Optional value specifying the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SearchedFaceId': 'string',
            'FaceMatches': [
                {
                    'Similarity': ...,
                    'Face': {
                        'FaceId': 'string',
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'ImageId': 'string',
                        'ExternalImageId': 'string',
                        'Confidence': ...
                    }
                },
            ],
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SearchedFaceId** *(string) --* 

          ID of the face that was searched for matches in a collection.

          
        

        - **FaceMatches** *(list) --* 

          An array of faces that matched the input face, along with the confidence in the match.

          
          

          - *(dict) --* 

            Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

            
            

            - **Similarity** *(float) --* 

              Confidence in the match of this face with the input face.

              
            

            - **Face** *(dict) --* 

              Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

              
              

              - **FaceId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the face.

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **ImageId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the input image.

                
              

              - **ExternalImageId** *(string) --* 

                Identifier that you assign to all the faces in the input image.

                
              

              - **Confidence** *(float) --* 

                Confidence level that the bounding box contains a face (and not a different object such as a tree).

                
          
        
      
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the input collection (``CollectionId`` ).

          
    

    **Examples** 

    This operation searches for matching faces in the collection the supplied face belongs to.
    ::

      response = client.search_faces(
          CollectionId='myphotos',
          FaceId='70008e50-75e4-55d0-8e80-363fb73b3a14',
          FaceMatchThreshold=90,
          MaxFaces=10,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FaceMatches': [
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.3259260058403015,
                          'Left': 0.5144439935684204,
                          'Top': 0.15111100673675537,
                          'Width': 0.24444399774074554,
                      },
                      'Confidence': 99.99949645996094,
                      'FaceId': '8be04dba-4e58-520d-850e-9eae4af70eb2',
                      'ImageId': '465f4e93-763e-51d0-b030-b9667a2d94b1',
                  },
                  'Similarity': 99.97222137451172,
              },
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.16555599868297577,
                          'Left': 0.30963000655174255,
                          'Top': 0.7066670060157776,
                          'Width': 0.22074100375175476,
                      },
                      'Confidence': 100,
                      'FaceId': '29a75abe-397b-5101-ba4f-706783b2246c',
                      'ImageId': '147fdf82-7a71-52cf-819b-e786c7b9746e',
                  },
                  'Similarity': 97.04154968261719,
              },
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.18888899683952332,
                          'Left': 0.3783380091190338,
                          'Top': 0.2355560064315796,
                          'Width': 0.25222599506378174,
                      },
                      'Confidence': 99.9999008178711,
                      'FaceId': '908544ad-edc3-59df-8faf-6a87cc256cf5',
                      'ImageId': '3c731605-d772-541a-a5e7-0375dbc68a07',
                  },
                  'Similarity': 95.94520568847656,
              },
          ],
          'SearchedFaceId': '70008e50-75e4-55d0-8e80-363fb73b3a14',
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: search_faces_by_image(**kwargs)

    

    For a given input image, first detects the largest face in the image, and then searches the specified collection for matching faces. The operation compares the features of the input face with faces in the specified collection. 

     

    .. note::

       

      To search for all faces in an input image, you might first call the operation, and then use the face IDs returned in subsequent calls to the operation. 

       

      You can also call the ``DetectFaces`` operation and use the bounding boxes in the response to make face crops, which then you can pass in to the ``SearchFacesByImage`` operation. 

       

     

    You pass the input image either as base64-encoded image bytes or as a reference to an image in an Amazon S3 bucket. If you use the Amazon CLI to call Amazon Rekognition operations, passing image bytes is not supported. The image must be either a PNG or JPEG formatted file. 

     

    The response returns an array of faces that match, ordered by similarity score with the highest similarity first. More specifically, it is an array of metadata for each face match found. Along with the metadata, the response also includes a ``similarity`` indicating how similar the face is to the input face. In the response, the operation also returns the bounding box (and a confidence level that the bounding box contains a face) of the face that Amazon Rekognition used for the input image. 

     

    For an example, see  search-face-with-image-procedure .

     

    This operation requires permissions to perform the ``rekognition:SearchFacesByImage`` action.

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/SearchFacesByImage>`_    


    **Request Syntax** 
    ::

      response = client.search_faces_by_image(
          CollectionId='string',
          Image={
              'Bytes': b'bytes',
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          MaxFaces=123,
          FaceMatchThreshold=...
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection to search.

      

    
    :type Image: dict
    :param Image: **[REQUIRED]** 

      The input image as base64-encoded bytes or an S3 object. If you use the AWS CLI to call Amazon Rekognition operations, passing base64-encoded image bytes is not supported. 

      

    
      - **Bytes** *(bytes) --* 

        Blob of image bytes up to 5 MBs.

        

      
      - **S3Object** *(dict) --* 

        Identifies an S3 object as the image source.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type MaxFaces: integer
    :param MaxFaces: 

      Maximum number of faces to return. The operation returns the maximum number of faces with the highest confidence in the match.

      

    
    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: 

      (Optional) Specifies the minimum confidence in the face match to return. For example, don't return any matches where confidence in matches is less than 70%.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'SearchedFaceBoundingBox': {
                'Width': ...,
                'Height': ...,
                'Left': ...,
                'Top': ...
            },
            'SearchedFaceConfidence': ...,
            'FaceMatches': [
                {
                    'Similarity': ...,
                    'Face': {
                        'FaceId': 'string',
                        'BoundingBox': {
                            'Width': ...,
                            'Height': ...,
                            'Left': ...,
                            'Top': ...
                        },
                        'ImageId': 'string',
                        'ExternalImageId': 'string',
                        'Confidence': ...
                    }
                },
            ],
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **SearchedFaceBoundingBox** *(dict) --* 

          The bounding box around the face in the input image that Amazon Rekognition used for the search.

          
          

          - **Width** *(float) --* 

            Width of the bounding box as a ratio of the overall image width.

            
          

          - **Height** *(float) --* 

            Height of the bounding box as a ratio of the overall image height.

            
          

          - **Left** *(float) --* 

            Left coordinate of the bounding box as a ratio of overall image width.

            
          

          - **Top** *(float) --* 

            Top coordinate of the bounding box as a ratio of overall image height.

            
      
        

        - **SearchedFaceConfidence** *(float) --* 

          The level of confidence that the ``searchedFaceBoundingBox`` , contains a face.

          
        

        - **FaceMatches** *(list) --* 

          An array of faces that match the input face, along with the confidence in the match.

          
          

          - *(dict) --* 

            Provides face metadata. In addition, it also provides the confidence in the match of this face with the input face.

            
            

            - **Similarity** *(float) --* 

              Confidence in the match of this face with the input face.

              
            

            - **Face** *(dict) --* 

              Describes the face properties such as the bounding box, face ID, image ID of the source image, and external image ID that you assigned.

              
              

              - **FaceId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the face.

                
              

              - **BoundingBox** *(dict) --* 

                Bounding box of the face.

                
                

                - **Width** *(float) --* 

                  Width of the bounding box as a ratio of the overall image width.

                  
                

                - **Height** *(float) --* 

                  Height of the bounding box as a ratio of the overall image height.

                  
                

                - **Left** *(float) --* 

                  Left coordinate of the bounding box as a ratio of overall image width.

                  
                

                - **Top** *(float) --* 

                  Top coordinate of the bounding box as a ratio of overall image height.

                  
            
              

              - **ImageId** *(string) --* 

                Unique identifier that Amazon Rekognition assigns to the input image.

                
              

              - **ExternalImageId** *(string) --* 

                Identifier that you assign to all the faces in the input image.

                
              

              - **Confidence** *(float) --* 

                Confidence level that the bounding box contains a face (and not a different object such as a tree).

                
          
        
      
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the input collection (``CollectionId`` ).

          
    

    **Examples** 

    This operation searches for faces in a Rekognition collection that match the largest face in an S3 bucket stored image.
    ::

      response = client.search_faces_by_image(
          CollectionId='myphotos',
          FaceMatchThreshold=95,
          Image={
              'S3Object': {
                  'Bucket': 'mybucket',
                  'Name': 'myphoto',
              },
          },
          MaxFaces=5,
      )
      
      print(response)

    
    Expected Output:
    ::

      {
          'FaceMatches': [
              {
                  'Face': {
                      'BoundingBox': {
                          'Height': 0.3234420120716095,
                          'Left': 0.3233329951763153,
                          'Top': 0.5,
                          'Width': 0.24222199618816376,
                      },
                      'Confidence': 99.99829864501953,
                      'FaceId': '38271d79-7bc2-5efb-b752-398a8d575b85',
                      'ImageId': 'd5631190-d039-54e4-b267-abd22c8647c5',
                  },
                  'Similarity': 99.97036743164062,
              },
          ],
          'SearchedFaceBoundingBox': {
              'Height': 0.33481481671333313,
              'Left': 0.31888890266418457,
              'Top': 0.4933333396911621,
              'Width': 0.25,
          },
          'SearchedFaceConfidence': 99.9991226196289,
          'ResponseMetadata': {
              '...': '...',
          },
      }

    

  .. py:method:: start_celebrity_recognition(**kwargs)

    

    Starts asynchronous recognition of celebrities in a stored video.

     

    Rekognition Video can detect celebrities in a video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartCelebrityRecognition`` returns a job identifier (``JobId`` ) which you use to get the results of the analysis. When celebrity recognition analysis is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` . To get the results of the celebrity recognition analysis, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartCelebrityRecognition`` . For more information, see  celebrities .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartCelebrityRecognition>`_    


    **Request Syntax** 
    ::

      response = client.start_celebrity_recognition(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ClientRequestToken='string',
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video in which you want to recognize celebrities. The video must be stored in an Amazon S3 bucket.

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartCelebrityRecognition`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The Amazon SNS topic ARN that you want Rekognition Video to publish the completion status of the celebrity recognition analysis to.

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the celebrity recognition analysis job. Use ``JobId`` to identify the job in a subsequent call to ``GetCelebrityRecognition`` .

          
    

  .. py:method:: start_content_moderation(**kwargs)

    

    Starts asynchronous detection of explicit or suggestive adult content in a stored video.

     

    Rekognition Video can moderate content in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartContentModeration`` returns a job identifier (``JobId`` ) which you use to get the results of the analysis. When content moderation analysis is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` .

     

    To get the results of the content moderation analysis, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartContentModeration`` . For more information, see  moderation .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartContentModeration>`_    


    **Request Syntax** 
    ::

      response = client.start_content_moderation(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          MinConfidence=...,
          ClientRequestToken='string',
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video in which you want to moderate content. The video must be stored in an Amazon S3 bucket.

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type MinConfidence: float
    :param MinConfidence: 

      Specifies the minimum confidence that Amazon Rekognition must have in order to return a moderated content label. Confidence represents how certain Amazon Rekognition is that the moderated content is correctly identified. 0 is the lowest confidence. 100 is the highest confidence. Amazon Rekognition doesn't return any moderated content labels with a confidence level lower than this specified value.

      

    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartContentModeration`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The Amazon SNS topic ARN that you want Rekognition Video to publish the completion status of the content moderation analysis to.

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the content moderation analysis job. Use ``JobId`` to identify the job in a subsequent call to ``GetContentModeration`` .

          
    

  .. py:method:: start_face_detection(**kwargs)

    

    Starts asynchronous detection of faces in a stored video.

     

    Rekognition Video can detect faces in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartFaceDetection`` returns a job identifier (``JobId`` ) that you use to get the results of the operation. When face detection is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` . To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartFaceDetection`` . For more information, see  faces-video .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartFaceDetection>`_    


    **Request Syntax** 
    ::

      response = client.start_face_detection(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ClientRequestToken='string',
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          FaceAttributes='DEFAULT'|'ALL',
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video in which you want to detect faces. The video must be stored in an Amazon S3 bucket.

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartFaceDetection`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The ARN of the Amazon SNS topic to which you want Rekognition Video to publish the completion status of the face detection operation.

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type FaceAttributes: string
    :param FaceAttributes: 

      The face attributes you want returned.

       

       ``DEFAULT`` - The following subset of facial attributes are returned: BoundingBox, Confidence, Pose, Quality and Landmarks. 

       

       ``ALL`` - All facial attributes are returned.

      

    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the face detection job. Use ``JobId`` to identify the job in a subsequent call to ``GetFaceDetection`` .

          
    

  .. py:method:: start_face_search(**kwargs)

    

    Starts the asynchronous search for faces in a collection that match the faces of persons detected in a stored video.

     

    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartFaceSearch`` returns a job identifier (``JobId`` ) which you use to get the search results once the search has completed. When searching is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` . To get the search results, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartFaceSearch`` . For more information, see  collections-search-person .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartFaceSearch>`_    


    **Request Syntax** 
    ::

      response = client.start_face_search(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ClientRequestToken='string',
          FaceMatchThreshold=...,
          CollectionId='string',
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video you want to search. The video must be stored in an Amazon S3 bucket. 

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartFaceSearch`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type FaceMatchThreshold: float
    :param FaceMatchThreshold: 

      The minimum confidence in the person match to return. For example, don't return any matches where confidence in matches is less than 70%. 

      

    
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection that contains the faces you want to search for.

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The ARN of the Amazon SNS topic to which you want Rekognition Video to publish the completion status of the search. 

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the search job. Use ``JobId`` to identify the job in a subsequent call to ``GetFaceSearch`` . 

          
    

  .. py:method:: start_label_detection(**kwargs)

    

    Starts asynchronous detection of labels in a stored video.

     

    Rekognition Video can detect labels in a video. Labels are instances of real-world entities. This includes objects like flower, tree, and table; events like wedding, graduation, and birthday party; concepts like landscape, evening, and nature; and activities like a person getting out of a car or a person skiing.

     

    The video must be stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartLabelDetection`` returns a job identifier (``JobId`` ) which you use to get the results of the operation. When label detection is finished, Rekognition Video publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` .

     

    To get the results of the label detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartLabelDetection`` .

     

    

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartLabelDetection>`_    


    **Request Syntax** 
    ::

      response = client.start_label_detection(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ClientRequestToken='string',
          MinConfidence=...,
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video in which you want to detect labels. The video must be stored in an Amazon S3 bucket.

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartLabelDetection`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type MinConfidence: float
    :param MinConfidence: 

      Specifies the minimum confidence that Rekognition Video must have in order to return a detected label. Confidence represents how certain Amazon Rekognition is that a label is correctly identified.0 is the lowest confidence. 100 is the highest confidence. Rekognition Video doesn't return any labels with a confidence level lower than this specified value.

       

      If you don't specify ``MinConfidence`` , the operation returns labels with confidence values greater than or equal to 50 percent.

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The Amazon SNS topic ARN you want Rekognition Video to publish the completion status of the label detection operation to. 

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the label detection job. Use ``JobId`` to identify the job in a subsequent call to ``GetLabelDetection`` . 

          
    

  .. py:method:: start_person_tracking(**kwargs)

    

    Starts the asynchronous tracking of persons in a stored video.

     

    Rekognition Video can track persons in a video stored in an Amazon S3 bucket. Use  Video to specify the bucket name and the filename of the video. ``StartPersonTracking`` returns a job identifier (``JobId`` ) which you use to get the results of the operation. When label detection is finished, Amazon Rekognition publishes a completion status to the Amazon Simple Notification Service topic that you specify in ``NotificationChannel`` . 

     

    To get the results of the person detection operation, first check that the status value published to the Amazon SNS topic is ``SUCCEEDED`` . If so, call and pass the job identifier (``JobId`` ) from the initial call to ``StartPersonTracking`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartPersonTracking>`_    


    **Request Syntax** 
    ::

      response = client.start_person_tracking(
          Video={
              'S3Object': {
                  'Bucket': 'string',
                  'Name': 'string',
                  'Version': 'string'
              }
          },
          ClientRequestToken='string',
          NotificationChannel={
              'SNSTopicArn': 'string',
              'RoleArn': 'string'
          },
          JobTag='string'
      )
    :type Video: dict
    :param Video: **[REQUIRED]** 

      The video in which you want to detect people. The video must be stored in an Amazon S3 bucket.

      

    
      - **S3Object** *(dict) --* 

        The Amazon S3 bucket name and file name for the video.

        

      
        - **Bucket** *(string) --* 

          Name of the S3 bucket.

          

        
        - **Name** *(string) --* 

          S3 object key name.

          

        
        - **Version** *(string) --* 

          If the bucket is versioning enabled, you can specify the object version. 

          

        
      
    
    :type ClientRequestToken: string
    :param ClientRequestToken: 

      Idempotent token used to identify the start request. If you use the same token with multiple ``StartPersonTracking`` requests, the same ``JobId`` is returned. Use ``ClientRequestToken`` to prevent the same job from being accidently started more than once. 

      

    
    :type NotificationChannel: dict
    :param NotificationChannel: 

      The Amazon SNS topic ARN you want Rekognition Video to publish the completion status of the people detection operation to.

      

    
      - **SNSTopicArn** *(string) --* **[REQUIRED]** 

        The Amazon SNS topic to which Amazon Rekognition to posts the completion status.

        

      
      - **RoleArn** *(string) --* **[REQUIRED]** 

        The ARN of an IAM role that gives Amazon Rekognition publishing permissions to the Amazon SNS topic. 

        

      
    
    :type JobTag: string
    :param JobTag: 

      Unique identifier you specify to identify the job in the completion status published to the Amazon Simple Notification Service topic. 

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'JobId': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **JobId** *(string) --* 

          The identifier for the person detection job. Use ``JobId`` to identify the job in a subsequent call to ``GetPersonTracking`` .

          
    

  .. py:method:: start_stream_processor(**kwargs)

    

    Starts processing a stream processor. You create a stream processor by calling . To tell ``StartStreamProcessor`` which stream processor to start, use the value of the ``Name`` field specified in the call to ``CreateStreamProcessor`` .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StartStreamProcessor>`_    


    **Request Syntax** 
    ::

      response = client.start_stream_processor(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of the stream processor to start processing.

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

  .. py:method:: stop_stream_processor(**kwargs)

    

    Stops a running stream processor that was created by .

    

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/StopStreamProcessor>`_    


    **Request Syntax** 
    ::

      response = client.stop_stream_processor(
          Name='string'
      )
    :type Name: string
    :param Name: **[REQUIRED]** 

      The name of a stream processor created by .

      

    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {}
        
      **Response Structure** 

      

      - *(dict) --* 
    

==========
Paginators
==========


The available paginators are:

* :py:class:`Rekognition.Paginator.ListCollections`


* :py:class:`Rekognition.Paginator.ListFaces`



.. py:class:: Rekognition.Paginator.ListCollections

  ::

    
    paginator = client.get_paginator('list_collections')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Rekognition.Client.list_collections`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListCollections>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'CollectionIds': [
                'string',
            ],
            'FaceModelVersions': [
                'string',
            ]
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **CollectionIds** *(list) --* 

          An array of collection IDs.

          
          

          - *(string) --* 
      
        

        - **FaceModelVersions** *(list) --* 

          Version numbers of the face detection models associated with the collections in the array ``CollectionIds`` . For example, the value of ``FaceModelVersions[2]`` is the version number for the face detection model used by the collection in ``CollectionId[2]`` .

          
          

          - *(string) --* 
      
    

.. py:class:: Rekognition.Paginator.ListFaces

  ::

    
    paginator = client.get_paginator('list_faces')

  
  

  .. py:method:: paginate(**kwargs)

    Creates an iterator that will paginate through responses from :py:meth:`Rekognition.Client.list_faces`.

    See also: `AWS API Documentation <https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/ListFaces>`_    


    **Request Syntax** 
    ::

      response_iterator = paginator.paginate(
          CollectionId='string',
          PaginationConfig={
              'MaxItems': 123,
              'PageSize': 123,
              'StartingToken': 'string'
          }
      )
    :type CollectionId: string
    :param CollectionId: **[REQUIRED]** 

      ID of the collection from which to list the faces.

      

    
    :type PaginationConfig: dict
    :param PaginationConfig: 

      A dictionary that provides parameters to control pagination.

      

    
      - **MaxItems** *(integer) --* 

        The total number of items to return. If the total number of items available is more than the value specified in max-items then a ``NextToken`` will be provided in the output that you can use to resume pagination.

        

      
      - **PageSize** *(integer) --* 

        The size of each page.

        

        

        

      
      - **StartingToken** *(string) --* 

        A token to specify where to start paginating. This is the ``NextToken`` from a previous response.

        

      
    
    
    :rtype: dict
    :returns: 
      
      **Response Syntax** 

      
      ::

        {
            'Faces': [
                {
                    'FaceId': 'string',
                    'BoundingBox': {
                        'Width': ...,
                        'Height': ...,
                        'Left': ...,
                        'Top': ...
                    },
                    'ImageId': 'string',
                    'ExternalImageId': 'string',
                    'Confidence': ...
                },
            ],
            'FaceModelVersion': 'string'
        }
      **Response Structure** 

      

      - *(dict) --* 
        

        - **Faces** *(list) --* 

          An array of ``Face`` objects. 

          
          

          - *(dict) --* 

            Describes the face properties such as the bounding box, face ID, image ID of the input image, and external image ID that you assigned. 

            
            

            - **FaceId** *(string) --* 

              Unique identifier that Amazon Rekognition assigns to the face.

              
            

            - **BoundingBox** *(dict) --* 

              Bounding box of the face.

              
              

              - **Width** *(float) --* 

                Width of the bounding box as a ratio of the overall image width.

                
              

              - **Height** *(float) --* 

                Height of the bounding box as a ratio of the overall image height.

                
              

              - **Left** *(float) --* 

                Left coordinate of the bounding box as a ratio of overall image width.

                
              

              - **Top** *(float) --* 

                Top coordinate of the bounding box as a ratio of overall image height.

                
          
            

            - **ImageId** *(string) --* 

              Unique identifier that Amazon Rekognition assigns to the input image.

              
            

            - **ExternalImageId** *(string) --* 

              Identifier that you assign to all the faces in the input image.

              
            

            - **Confidence** *(float) --* 

              Confidence level that the bounding box contains a face (and not a different object such as a tree).

              
        
      
        

        - **FaceModelVersion** *(string) --* 

          Version number of the face detection model associated with the input collection (``CollectionId`` ).

          
    