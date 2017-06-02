#!/usr/bin/env python

import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    inst_names = [tag['Value'] for tag in instance.tags if tag['Key'] == 'Name']
    print(inst_names)
