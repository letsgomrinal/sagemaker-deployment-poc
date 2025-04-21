import os
import joblib
import json
import numpy as np

def model_fn(model_dir):
    model_path = os.path.join(model_dir, "model.pkl")
    return joblib.load(model_path)

def input_fn(request_body, request_content_type):
    if request_content_type == "application/json":
        try:
            parsed = json.loads(request_body)
            return np.array(parsed)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON input: {e}")
    else:
        raise ValueError(f"Unsupported content type: {request_content_type}")

def predict_fn(input_data, model):
    try:
        return model.predict(input_data)
    except Exception as e:
        raise RuntimeError(f"Prediction failed: {e}")

def output_fn(prediction, content_type):
    if content_type == "application/json":
        return json.dumps(prediction.tolist())
    else:
        raise ValueError(f"Unsupported response content type: {content_type}")
