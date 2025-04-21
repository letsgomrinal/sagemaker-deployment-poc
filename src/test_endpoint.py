import numpy as np
from sagemaker.predictor import Predictor
from src.config import endpoint_name

predictor = Predictor(endpoint_name)

sample = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = predictor.predict(sample)
print("Prediction:", prediction)
