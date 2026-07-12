# Backend README — instructions and hardware guidance

Este diretório contém o backend do Vizo Glass MVP para execução local de um LLM (sem depender de APIs externas).

Importante:
- Este repositório NÃO inclui pesos do modelo. Coloque um arquivo GGML (por exemplo `ggml-model.bin`) em `backend/models/`.
- Para óculos com computação embarcada é comum usar um dispositivo de "compute" na mochila/bolsa — modelos grandes (13B/70B) costumam exigir GPU.

Recomendações de hardware para diferentes tamanhos de modelo:
- 7B quantizado (q4_K_M ou q4_0): pode rodar em CPU moderno (Intel i7/i9 recentes) ou Jetson AGX com RAM suficiente; é a escolha mais fria para dispositivos menores.
- 13B: recomenda-se GPU com ao menos 16 GB VRAM (ex.: NVIDIA RTX 3060 Ti 16GB, RTX 4070 12GB pode ser insuficiente dependendo da quantizaç��o) ou uso de offload.
- 70B: normalmente requer múltiplas GPUs ou servidores com >= 40 GB VRAM por GPU e ferramentas de offload — não realista para execução totalmente embarcada.

Hardware sugerido para um óculos com capacidade local avançada (trade-off entre peso e potência):
- Setup "edge backpack": mini-PC com GPU NVIDIA (ex.: NVIDIA RTX 4060/4070/4080) em mochila/bolsa, conectado ao óculos via Wi-Fi local de baixa latência.
- Alternativa embarcada: NVIDIA Jetson AGX Orin (32GB) — capaz de rodar modelos menores/quantizados localmente.

Instalação rápida (desenvolvimento):
1. Crie um virtualenv: python -m venv .venv && source .venv/bin/activate
2. pip install -r backend/requirements.txt
3. Coloque seu modelo GGML em backend/models/ggml-model.bin
4. export LLM_MODEL_PATH=backend/models/ggml-model.bin
5. uvicorn backend.app.main:app --host 0.0.0.0 --port 8080

STT/TTS:
- Para STT local: recomendo faster-whisper (GPU) ou whisper.cpp (CPU). See links in README root for conversion instructions.
- Para TTS local: Coqui TTS (neural) ou pyttsx3 (simples, menos natural).

Segurança e legal:
- Obtenha modelos apenas de fontes com licença compatível.
- Não commitaremos nem distribuiremos pesos proprietários.
