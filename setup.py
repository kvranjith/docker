#!/usr/bin/python 
import boto3
import uuid
random = str(uuid.uuid4())
client = boto3.client('ec2',region_name='us-east-2')
response = client.describe_instances()
for ins in response['Reservations']:
    for vol in ins['Instances']:
        test = vol['InstanceId'],vol['State']['Name']
        print test
        print random