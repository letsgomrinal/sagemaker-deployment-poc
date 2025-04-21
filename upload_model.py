import tarfile
import boto3
from config import bucket_name, key


# Compress the model directory
with tarfile.open("model.tar.gz", "w:gz") as tar:
    tar.add("model", arcname=".")

# Upload to S3
s3 = boto3.client("s3")
s3.upload_file("model.tar.gz", bucket_name, key)
print(f"✅ Uploaded model to s3://{bucket_name}/{key}")
