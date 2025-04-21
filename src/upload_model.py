import tarfile
import boto3
from botocore.exceptions import ClientError
from src.config import bucket_name, key


# Compress the model directory
with tarfile.open("model/model.tar.gz", "w:gz") as tar:
    tar.add("model", arcname=".")

s3 = boto3.client("s3")
# Check if bucket exists
try:
    s3.head_bucket(Bucket=bucket_name)
except ClientError:
    print(f"❌ Bucket '{bucket_name}' does not exist.")
    exit(1)
    
# Upload to S3
s3.upload_file("model.tar.gz", bucket_name, key)
print(f"✅ Uploaded model to s3://{bucket_name}/{key}")
