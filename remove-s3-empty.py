import boto3

# Initialize a session using DigitalOcean Spaces.
session = boto3.Session()

# Connect to S3
client = session.client('s3')

# List all buckets
response = client.list_buckets()

# Iterate through all the buckets
for bucket in response['Buckets']:
    if not bucket['Name'].startswith('aws-logs'):
        # Get the contents of the bucket
        contents = client.list_objects(Bucket=bucket['Name'])
        if 'Contents' not in contents:
            print(f'Bucket {bucket["Name"]} is empty. Deleting...')
            client.delete_bucket(Bucket=bucket['Name'])
            print(f'Bucket {bucket["Name"]} deleted.')
        else:
            print(f'Bucket {bucket["Name"]} is not empty.')
