import boto3

s3 = boto3.resource('s3')

bucket = "bucket"
key = "key"

obj = s3.Object(bucket, key)
obj.get()['Body'].read().decode('utf-8')
