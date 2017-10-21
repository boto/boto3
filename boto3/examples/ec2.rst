Add an EC2 security group rule referencing another security group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following example shows how to add an EC2 security group rule allowing access from another security group.

.. code-block:: python

    import boto3
    from botocore.exceptions import ClientError

    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

    try:
        response = ec2.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                             Description='DESCRIPTION',
                                             VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))

        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                 'FromPort': 80,
                 'ToPort': 80,
                 'UserIdGroupPairs': [{'GroupId': 'OTHER_SECURITY_GROUP_ID'}]},
                {'IpProtocol': 'tcp',
                 'FromPort': 22,
                 'ToPort': 22,
                 'UserIdGroupPairs': [{'GroupId': 'OTHER_SECURITY_GROUP_ID'}]}
            ])
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(e)
