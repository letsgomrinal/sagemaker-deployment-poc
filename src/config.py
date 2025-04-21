bucket_name = "test-sagemaker-deployment-poc-bucket" 
key = "model/model.tar.gz"
instance_type="ml.t2.medium"
instance_count=1
endpoint_name="rf-iris-endpoint-v2"
aws_account_id="enter account id here!"
role_name="sagemaker-model-deployment"
aws_arn=f'arn:aws:iam::{aws_account_id}:role/{role_name}'
