# Model manager helpers for Vizo Glass backend
# CEO e criador: David Adriano Ferrari dos Santos

import os

try:
    from llama_cpp import Llama
except Exception:
    Llama = None

MODEL_ENV = "LLM_MODEL_PATH"


def load_local_model(path: str = None):
    """Load a local GGML model via llama-cpp-python. Returns a Llama instance or raises.
    """
    if Llama is None:
        raise RuntimeError("llama-cpp-python not installed")
    if path is None:
        path = os.getenv(MODEL_ENV, "backend/models/ggml-model.bin")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found at {path}")
    return Llama(model_path=path)
