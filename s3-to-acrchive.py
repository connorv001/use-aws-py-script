import boto3
s3 = boto3.client('s3')
bucket_names = ['bucket1', 'bucket2', 'bucket3']
for bucket_name in bucket_names:
    s3.create_bucket_lifecycle_configuration(Bucket=bucket_name,
        LifecycleConfiguration={
            'Rules': [{
                'Status': 'Enabled',
                'Transitions': [{
                    'Days': 30,
                    'StorageClass': 'GLACIER'
                }]
            }]
        }
    )
    print(f'Bucket {bucket_name} has been moved to Glacier.')
