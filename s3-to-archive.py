import boto3

# Set up a client for S3
s3 = boto3.client('s3')

# List of S3 bucket names to move to Glacier
bucket_names = ['bucket1', 'bucket2', 'bucke3']
# Iterate through the list of bucket names
for bucket_name in bucket_names:
    # Set the storage class of all objects in the bucket to Glacier
    s3.put_bucket_lifecycle_configuration(Bucket=bucket_name,
        LifecycleConfiguration={
            'Rules': [{
                'Status': 'Enabled',
                'Filter': {'Prefix':'string'},
                'Transitions': [{
                    'Days': 30,
                    'StorageClass': 'GLACIER'
                }],
                'Expiration': {
                    'Days': 300
                }
            }]
        }
    )
    print(f'Bucket {bucket_name} has been moved to Glacier and objects are set to expire after 300 days.')
