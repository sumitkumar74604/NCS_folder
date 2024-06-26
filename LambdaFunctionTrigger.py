## python 3.8 

import boto3
from uuid import uuid4

def lambda_handler(event, context):
    # Initialize boto3 clients and resources
    s3 = boto3.client("s3")
    dynamodb = boto3.resource('dynamodb')
    
    # Retrieve DynamoDB table
    dynamoTable = dynamodb.Table('LambdaFunctionTriggerDatabaseTable')
    
    # Process each record in the event
    for record in event['Records']:
        # Extract information from the S3 event record
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        size = record['s3']['object'].get('size', -1)
        event_name = record['eventName']
        event_time = record['eventTime']
        
        # Generate a unique identifier for the item
        unique_id = str(uuid4())
        
        # Put item into DynamoDB table
        dynamoTable.put_item(
            Item={
                'unique': unique_id,
                'Bucket': bucket_name,
                'Object': object_key,
                'Size': size,
                'Event': event_name,
                'EventTime': event_time
            }
        )

# Just copy and paste this code into your Lambda function, and it should work with the corrected values for the S3 bucket name and DynamoDB table name.
#------------------------------------------------------------------------------------------------------------------
# auto start or stop istance using labda function
# python 3.9
import boto3
import time
from uuid import uuid4

region = 'ap-southeast-1'
instances = ['i-047d64a597e5ff39c']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    while True:
        # Start instances
        start_instances()
        print('Starting your instances:', instances)
        
        # Delay for 60 seconds
        time.sleep(60)
        
        # Stop instances
        stop_instances()
        print('Stopping your instances:', instances)

def start_instances():
    ec2.start_instances(InstanceIds=instances)

def stop_instances():
    ec2.stop_instances(InstanceIds=instances)
