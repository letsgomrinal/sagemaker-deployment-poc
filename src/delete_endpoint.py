from sagemaker.predictor import Predictor
from src.config import endpoint_name

predictor = Predictor(endpoint_name)
predictor.delete_endpoint()
print("🧹 Endpoint deleted.")
