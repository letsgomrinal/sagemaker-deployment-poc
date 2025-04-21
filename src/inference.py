import os
import joblib
import json
import numpy as np

def model_fn(model_dir):
    return joblib.load(os.path.join(model_dir, "model.pkl"))

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        return np.array(json.loads(request_body))
    raise ValueError("Unsupported content type")

def predict_fn(input_data, model):
    return model.predict(input_data)

def output_fn(prediction, content_type):
    return json.dumps(prediction.tolist())
