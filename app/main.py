from fastapi import FastAPI, HTTPException
from app.models import LoteDadosPonte, DiagnosticoPonte
from app.ai_engine import analisar_dados_com_chatgpt

# 1. Inicialização do Aplicativo
app = FastAPI(
    title="Sistema de Análise Estrutural Inteligente",
    description="API para monitoramento de pontes em tempo real utilizando IA (OpenAI API)"
)

# 2. Rota de Diagnóstico (Healthcheck)
@app.get("/")
def read_root():
    return {"status": "operacional", "sistema": "Engenharia Avançada S.A."}

# 3. Rota Principal de Ingestão e Análise via Inteligência Artificial
@app.post("/api/v1/monitoramento/analisar", response_model=DiagnosticoPonte)
async def receber_dados_tempo_real(dados: LoteDadosPonte):
    """
    Recebe o lote de dados da ponte (simulando buffer Kafka/Redis)
    e repassa para análise preditiva da Inteligência Artificial.
    """
    try:
        # Extraímos a primeira leitura do lote para simplificar a simulação no mock
        if not dados.pacote_leituras:
             raise HTTPException(status_code=400, detail="O lote não contém leituras de sensores.")
             
        leitura_alvo = dados.pacote_leituras[0]
        
        # O Motor de IA (ChatGPT) entra em ação usando Few-Shot Prompting
        resposta_ia = analisar_dados_com_chatgpt(
            dados_sensor=leitura_alvo.valores,
            tipo_sensor=leitura_alvo.tipo
        )
        
        # Retorna o Diagnóstico formatado rigorosamente para a resposta da API
        return DiagnosticoPonte(
            ponte_id=dados.ponte_id,
            status_estrutura=resposta_ia.get("status", "ERRO"),
            anomalia_detectada=resposta_ia.get("anomalia", False),
            ia_analise_detalhada=resposta_ia.get("motivo", "Falha ao analisar motivo com a IA.")
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno no processamento: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    # Executa o servidor localmente na porta 8000
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)