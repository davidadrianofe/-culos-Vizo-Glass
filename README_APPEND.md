# Root README — appended with hardware recommendation for glasses

Hardware recomendation (para óculos com processamento local avançado):
- Edge backpack com mini-PC + GPU NVIDIA (e.g., RTX 4070/4080) para permitir execução de modelos 13B/70B em quantização e offload.
- Alternativa mais leve e embutida: NVIDIA Jetson AGX Orin (32GB) para modelos quantizados 7B e workloads de visão/robotica.

Eu já adicionei o scaffold inicial no branch feature/llm-local-mvp com backend, client e instruções. Próximo passo: implementar STT/TTS locais, optimizações de quantização e scripts de conversão/benchmark.

CEO e criador: David Adriano Ferrari dos Santos
