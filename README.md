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