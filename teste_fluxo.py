# teste_fluxo.py
import urllib.request
import json
import random

url = "http://127.0.0.1:8000/api/v1/monitoramento/analisar"

# CASO DE TESTE 1: Ponte em Estado Estável (Dados normais)
payload_estavel = {
    "timestamp_envio": "2026-05-28T14:30:00Z",
    "ponte_id": random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    "pacote_leituras": [
        {"sensor_id": "ACEL-001", "tipo": "acelerometro", "valores": [random.random()*10, random.random()*10, random.random()*10]}
    ]
}

# CASO DE TESTE 2: Ponte em Estado Crítico (Pico de vibração / Anomalia)
payload_critico = {
    "timestamp_envio": "2026-05-28T14:32:00Z",
    "ponte_id": random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]),
    "pacote_leituras": [
        {"sensor_id": "ACEL-089", "tipo": "acelerometro", "valores": [random.random()*10, random.random()*10, random.random()*10]}
    ]
}

def enviar_requisicao(payload, titulo):
    print(f"\n--- TESTANDO: {titulo} ---")
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode('utf-8')
            print("Resposta do Servidor (Formato JSON esperado):")
            print(json.dumps(json.loads(res_body), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Erro ao conectar com a API: {e}")

if __name__ == "__main__":
    print("Iniciando Validação da Prova de Lógica do Sistema...")
    enviar_requisicao(payload_estavel, "Cenário 1 - Operação Normal (NBR 8681)")
    enviar_requisicao(payload_critico, "Cenário 2 - Alerta de Fadiga Estrutural (NBR 6118)")