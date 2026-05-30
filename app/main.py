# app/main.py
from fastapi import FastAPI, HTTPException
import uvicorn

# Imports corrigidos para evitar o erro interno de inicialização
from models import LoteDadosPonte, DiagnosticoPonte
from ai_engine import analisar_dados_com_chatgpt

app = FastAPI(
    title="Sistema de Análise Estrutural Inteligente",
    description="API para monitoramento de pontes em tempo real utilizando IA"
)

@app.get("/")
def read_root():
    return {"status": "operacional", "sistema": "Engenharia Avançada S.A."}

@app.post("/api/v1/monitoramento/analisar", response_model=DiagnosticoPonte)
async def receber_dados_tempo_real(dados: LoteDadosPonte):
    try:
        if not dados.pacote_leituras:
             raise HTTPException(status_code=400, detail="O lote não contém leituras de sensores.")
             
        # Pegamos a primeira leitura enviada para analisar
        leitura_alvo = dados.pacote_leituras[0]
        
        # Chama o simulador gratuito do ai_engine.py
        resposta_ia = analisar_dados_com_chatgpt(
            dados_sensor=leitura_alvo.valores,
            tipo_sensor=leitura_alvo.tipo
        )
        
        return DiagnosticoPonte(
            ponte_id=dados.ponte_id,
            status_structure=resposta_ia.get("status", "ERRO"), # Garante compatibilidade
            status_estrutura=resposta_ia.get("status", "ERRO"),
            anomalia_detectada=resposta_ia.get("anomalia", False),
            ia_analise_detalhada=resposta_ia.get("motivo", "Falha ao analisar.")
        )
        
    except Exception as e:
        # Se der erro, printa o motivo real no terminal do servidor para sabermos o que foi
        print(f"[ERRO NO SERVIDOR]: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)