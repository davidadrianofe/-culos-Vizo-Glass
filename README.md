# Vizo Glass — Óculos Inteligente LLM (Local)

Projeto MVP para óculos inteligente com LLM local.

CEO e criador: David Adriano Ferrari dos Santos

Este repositório contém um scaffold para rodar um assistente local (LLM) que roda em hardware local, sem depender de APIs externas. O backend usa "llama-cpp-python" para carregar modelos GGML localmente. O STT pode ser feito com Whisper local (faster-whisper/whisper.cpp) e TTS com pyttsx3 ou Coqui.

Aviso importante
- Este repositório NÃO inclui pesos de modelos (arquivos .bin GGML). Você deve obter os pesos do modelo compatível (por exemplo, um modelo convertido para formato GGML) por meios legais e colocá-los em `backend/models/`.
- Rodar modelos grandes requer hardware significativo (RAM/VRAM). Leia o README abaixo para recomendações.

Estrutura inicial
- backend/: FastAPI + integração com llama-cpp-python (LLM local), STT e TTS.
- client/: scripts de referência para rodar no óculos (Raspberry Pi/PC).

Como começar (resumo rápido)
1. Instale dependências no backend: `pip install -r backend/requirements.txt`.
2. Coloque o arquivo do modelo GGML em `backend/models/ggml-model.bin`.
3. Rode o backend: `uvicorn backend.app.main:app --host 0.0.0.0 --port 8080`.
4. No cliente, ajuste `BACKEND_URL` em `client/config.py` e rode `python client/capture_and_send.py`.

Licença: MIT (arquivo LICENSE está incluído)
