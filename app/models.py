"""
JSON que servirá para evitar gargalo no processamento de big data, dessa forma garantindo que a latência maxima de 5 minutos será respeitada.
{
  "timestamp_envio": "2026-05-25T18:40:00Z",
  "ponte_id": 12,
  "leituras": [
    {
      "sensor_id": "ACEL-001",
      "tipo": "acelerometro",
      "valores": [0.012, 0.015, 0.011]
    },
    {
      "sensor_id": "EXT-045",
      "tipo": "extensometro",
      "valores": [152.4]
    }
  ]
} 

O que temos aqui em cima é como os arquivos .JSON serão carregados e lidos, dessa forma acelerando e evitando que eles fiquem cheios
"""
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class LeituraSensor(BaseModel):
    sensor_id: str = Field(..., example="ACEL-001")
    tipo: str = Field(..., example="acelerometro") 
    valores: List[float] = Field(..., description="Lista de métricas coletadas no intervalo de tempo")
    # Classe para guardar a leitura dos sensores

class LoteDadosPonte(BaseModel):
    timestamp_envio: datetime
    ponte_id: int = Field(..., ge=1, le=15) # Restrito às 15 pontes do projeto 
    pacote_leituras: List[LeituraSensor]