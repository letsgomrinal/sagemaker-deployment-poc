# sagemaker-deployment-poc

# Install `uv`

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

# Initiate Project

```
uv venv
source .venv/bin/activate
uv init
uv pip install sagemaker boto3 joblib scikit-learn
```

# Setup  `aws cli`

```
aws configure
```

# To check buckets 

```
 aws s3 ls
```

# Create an S3 bucket:

```
aws s3api create-bucket \
  --bucket test-sagemaker-deployment-poc-bucket \
  --region us-east-1
