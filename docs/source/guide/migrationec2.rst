.. _guide_migration_ec2:

Amazon EC2
==========
Boto 2.x contains a number of customizations to make working with Amazon EC2 instances, storage and networks easy. Boto 3 exposes these same objects through its resources interface in a unified and consistent way.

Creating the Connection
-----------------------
Boto 3 has both low-level clients and higher-level resources. For Amazon EC2, the higher-level resources are the most similar to Boto 2.x's ``ec2`` and ``vpc`` modules::

    # Boto 2.x
    import boto
    ec2_connection = boto.connect_ec2()
    vpc_connection = boto.connect_vpc()

    # Boto 3
    import boto3
    ec2 = boto3.resource('ec2')

Launching New Instances
-----------------------
Launching new instances requires an image ID and the number of instances to launch. It can also take several optional parameters, such as the instance type and security group::

    # Boto 2.x
    ec2_connection.run_instances('<ami-image-id>')

    # Boto 3
    ec2.create_instances(ImageId='<ami-image-id>', MinCount=1, MaxCount=5)

Stopping & Terminating Instances
--------------------------------
Stopping and terminating multiple instances given a list of instance IDs uses Boto 3 collection filtering::

    ids = ['instance-id-1', 'instance-id-2', ...]

    # Boto 2.x
    ec2_connection.stop_instances(instance_ids=ids)
    ec2_connection.terminate_instances(instance_ids=ids)

    # Boto 3
    ec2.instances.filter(InstanceIds=ids).stop()
    ec2.instances.filter(InstanceIds=ids).terminate()

Checking What Instances Are Running
-----------------------------------
Boto 3 collections come in handy when listing all your running instances as well. Every collection exposes a ``filter`` method that allows you to pass additional parameters to the underlying service API operation. The EC2 instances collection takes a parameter called ``Filters`` which is a list of names and values, for example::

    # Boto 2.x
    reservations = ec2_connection.get_all_reservations(
        filters={'instance-state-name': 'running'})
    for reservation in reservations:
        for instance in reservation.instances:
            print(instance.instance_id, instance.instance_type)

    # Boto 3
    # Use the filter() method of the instances collection to retrieve
    # all running EC2 instances.
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id, instance.instance_type)

Checking Health Status Of Instances
-----------------------------------
It is possible to get scheduled maintenance information for your running instances. At the time of this writing Boto 3 does not have a status resource, so you must drop down to the low-level client via ``ec2.meta.client``::

    # Boto 2.x
    for status in ec2_connection.get_all_instance_statuses():
        print(status)

    # Boto 3
    for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
        print(status)

Working with EBS Snapshots
--------------------------
Snapshots provide a way to create a copy of an EBS volume, as well as make new volumes from the snapshot which can be attached to an instance::

    # Boto 2.x
    snapshot = ec2_connection.create_snapshot('volume-id', 'Description')
    volume = snapshot.create_volume('us-west-2')
    ec2_connection.attach_volume(volume.id, 'instance-id', '/dev/sdy')
    ec2_connection.delete_snapshot(snapshot.id)

    # Boto 3
    snapshot = ec2.create_snapshot(VolumeId='volume-id', Description='description')
    volume = ec2.create_volume(SnapshotId=snapshot.id, AvailabilityZone='us-west-2a')
    ec2.Instance('instance-id').attach_volume(VolumeId=volume.id, Device='/dev/sdy')
    snapshot.delete()

Creating a VPC, Subnet, and Gateway
-----------------------------------
Creating VPC resources in Boto 3 is very similar to Boto 2.x::

    # Boto 2.x
    vpc = vpc_connection.create_vpc('10.0.0.0/24')
    subnet = vpc_connection.create_subnet(vpc.id, '10.0.0.0/25')
    gateway = vpc_connection.create_internet_gateway()

    # Boto 3
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/24')
    subnet = vpc.create_subnet(CidrBlock='10.0.0.0/25')
    gateway = ec2.create_internet_gateway()

Attaching and Detaching an Elastic IP and Gateway
-------------------------------------------------
Elastic IPs and gateways provide a way for instances inside of a VPC to communicate with the outside world::

    # Boto 2.x
    ec2_connection.attach_internet_gateway(gateway.id, vpc.id)
    ec2_connection.detach_internet_gateway(gateway.id, vpc.id)

    from boto.ec2.address import Address
    address = Address()
    address.allocation_id = 'eipalloc-35cf685d'
    address.associate('i-71b2f60b')
    address.disassociate()

    # Boto 3
    gateway.attach_to_vpc(VpcId=vpc.id)
    gateway.detach_from_vpc(VpcId=vpc.id)

    address = ec2.VpcAddress('eipalloc-35cf685d')
    address.associate('i-71b2f60b')
    address.association.delete()
