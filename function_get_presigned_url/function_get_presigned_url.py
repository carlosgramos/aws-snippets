import json
import boto3

print('Loading function')

s3_client = boto3.client('s3')

bucket = '#bucket_name'
prefix = '#prefix_name'
delimiter = '/'

response = s3_client.list_objects_v2(
            Bucket=bucket,
            Prefix=prefix,
            Delimiter=delimiter,
            MaxKeys=10
        )

presigned_urls = []

for object in response['Contents']:
    key_segments = object['Key'].split('/')
    if len(key_segments) <= 2:
        url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': key_segments[1]})
        presigned_urls.append(url)

print(presigned_urls)
