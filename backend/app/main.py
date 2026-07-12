"""Vizo Glass — Backend FastAPI app for local LLM inference
CEO e criador: David Adriano Ferrari dos Santos

This app provides HTTP endpoints to run a local GGML-based LLM via llama-cpp-python.
It also contains placeholders for STT (Whisper) and TTS (Coqui/pyttsx3) integrations.

IMPORTANT:
- This repository does NOT include model weights. Place your GGML model file at backend/models/ggml-model.bin
- Running large models locally requires significant RAM/VRAM. See backend/README.md for hardware guidance.
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import os
import asyncio

try:
    from llama_cpp import Llama
except Exception as e:
    Llama = None
    print("Warning: llama-cpp-python not available. Install it to enable local LLM inference.", e)

MODEL_PATH = os.getenv("LLM_MODEL_PATH", "backend/models/ggml-model.bin")

app = FastAPI(title="Vizo Glass LLM Local Backend")
llm = None

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.2


@app.on_event("startup")
async def startup_event():
    global llm
    if Llama is None:
        print("llama-cpp-python is not installed; model loading is disabled.")
        return
    if not os.path.exists(MODEL_PATH):
        print(f"Model file not found at {MODEL_PATH}. Please place your GGML model at that path.")
        return
    # Load the model (blocking); consider async offload for heavy models
    try:
        print("Loading model from", MODEL_PATH)
        llm = Llama(model_path=MODEL_PATH)
        print("Model loaded")
    except Exception as e:
        print("Failed to load model:", e)


@app.get("/api/health")
async def health():
    return {"status": "ok", "llm_loaded": llm is not None}


@app.post("/api/generate")
async def generate(req: ChatRequest):
    """Generate a response from the local LLM using llama-cpp-python.
    The request contains a list of messages (role: system/user/assistant). We'll concatenate for a single prompt.
    """
    if llm is None:
        raise HTTPException(status_code=503, detail="LLM not loaded on server")

    # Simple prompt construction — for more advanced chat protocol, implement conversation state and system messages handling.
    prompt = "\n".join([f"{m.role}: {m.content}" for m in req.messages])

    try:
        resp = llm.create(prompt=prompt, max_tokens=req.max_tokens, temperature=req.temperature)
        # resp is a dict from llama-cpp-python
        text = resp.get("choices", [{}])[0].get("text", "")
        return {"text": text, "meta": resp}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Placeholder endpoints for STT/TTS — these should be implemented using local Whisper/Coqui or other engines.
@app.post("/api/stt")
async def stt_upload():
    # Accept an audio file (multipart/form-data) and return transcript
    raise HTTPException(status_code=501, detail="STT endpoint not implemented in this scaffold. See backend/README.md")


@app.post("/api/tts")
async def tts_generate():
    # Accept text and return audio bytes or URL to generated file
    raise HTTPException(status_code=501, detail="TTS endpoint not implemented in this scaffold. See backend/README.md")
