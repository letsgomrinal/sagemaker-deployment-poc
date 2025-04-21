import sagemaker
import boto3
from sagemaker.sklearn.model import SKLearnModel
from sagemaker import get_execution_role
from src.config import bucket_name, key, instance_type, instance_count, endpoint_name, role_name



iam = boto3.client("iam")
response = iam.get_role(RoleName=role_name)
role = response["Role"]["Arn"]

# role = get_execution_role()  -> works in SageMaker Studio

session = sagemaker.Session()
model = SKLearnModel(
    model_data=f"s3://{bucket_name}/{key}",
    role=role,
    entry_point="inference.py",
    framework_version="0.23-1",
    py_version="py3",
    sagemaker_session=session
)

predictor = model.deploy(
    instance_type=instance_type,
    initial_instance_count=instance_count,
    endpoint_name=endpoint_name
)

print(f"✅ Deployed at {endpoint_name}")
