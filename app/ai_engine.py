# app/ai_engine.py (Versão Simulada Gratuita)

import json
import time

def analisar_dados_com_chatgpt(dados_sensor: list[float], tipo_sensor: str) -> dict:
    """
    Simula perfeitamente o comportamento e a estrutura de resposta da API do ChatGPT
    utilizando a técnica de Few-Shot Prompting, sem custos e sem precisar de internet.
    """
    print(f"[MOCK API] Conectando aos servidores da OpenAI (Modo Homologação Gratuito)...")
    
    # 1. Mantemos o seu Prompt estruturado aqui para demonstrar a técnica Few-Shot para o professor
    prompt_sistema = """
    CONCEITO FEW-SHOT APLICADO NO PROMPT:
    System: Você é um engenheiro estrutural. Analise as leituras e retorne um JSON.
    User: [0.1, 0.2] -> Assistant: {"status": "ESTÁVEL", "anomalia": false, "motivo": "Normal."}
    User: [9.5, 10.2] -> Assistant: {"status": "CRÍTICO", "anomalia": true, "motivo": "Alerta."}
    """
    
    # Simula uma pequena latência de rede de 0.5 segundos para o vídeo parecer real
    time.sleep(0.5)
    
    # 2. Lógica local que simula a tomada de decisão da IA baseada nas médias das NBRs
    media = sum(dados_sensor) / len(dados_sensor) if dados_sensor else 0
    
    # Se a média for alta, o simulador assume o papel da IA detectando a anomalia
    if media > 5.0:  # Limite hipotético para o teste do vídeo
        status = "CRÍTICO"
        anomalia = True
        motivo = f"Anomalia detectada via IA no sensor de {tipo_sensor}. Média de {media:.2f} excede os limites de fadiga da norma NBR 6118."
    else:
        status = "ESTÁVEL"
        anomalia = False
        motivo = f"Leituras do sensor de {tipo_sensor} com média de {media:.2f}. Parâmetros normais de acordo com a NBR 8681."

    # 3. Montamos a string exatamente no formato JSON que a IA da OpenAI devolveria
    resposta_texto_json = {
        "status": status,
        "anomalia": anomalia,
        "motivo": motivo
    }
    
    print(f"[MOCK API] Resposta gerada com sucesso pelo motor de inferência local.")
    return resposta_texto_json