# Arquitetura de Dados do Sistema

## Fluxo de Ingestão (50GB/dia)
1. **Sensores (Campo):** Acelerômetros, Extensômetros e Inclinômetros geram leituras brutas a cada 1 segundo.
2. **Gateway:** Agrupa as leituras por ponte e envia via HTTPS para a rota `/api/v1/monitoramento/analisar` do FastAPI.
3. **Buffer (Simulado):** Os dados passam pelo processamento assíncrono para downsampling (médias de intervalo) a fim de mitigar gargalos.
4. **Análise Preditiva:** O motor de IA avalia as métricas em conformidade com as normas NBR 6118 e NBR 8681.
5. **Armazenamento Split:** - Hot Storage: Banco de séries temporais para dados operacionais (< 30 dias).
   - Cold Storage: Data Lake (formatos compactados .parquet) para treinamento futuro de IA.