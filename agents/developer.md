# Instruções de Desenvolvimento - Monitoramento de Pontes

## Contexto do Projeto
Este repositório contém o MVP do sistema de monitoramento inteligente para 15 pontes críticas, desenvolvido para a Engenharia Avançada S.A.

## Diretrizes do Código
- **Linguagem:** Python 3.12 utilizando o framework FastAPI.
- **Arquitetura:** Os schemas de dados de entrada dos sensores e saída do diagnóstico devem usar estritamente o Pydantic em `app/models.py`.
- **IA:** O motor de análise em `app/ai_engine.py` utiliza a técnica de Few-Shot Prompting para simulação local/homologação de custo zero.
- **Latência:** Toda lógica deve ser otimizada para garantir a resposta em menos de 5 minutos.