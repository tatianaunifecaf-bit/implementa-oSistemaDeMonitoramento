# app/models.py
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class LeituraSensor(BaseModel):
    sensor_id: str = Field(..., description="ID do sensor")
    tipo: str = Field(..., description="Tipo do sensor (ex: acelerometro)")
    valores: List[float] = Field(..., description="Lista de leituras numéricas")

class LoteDadosPonte(BaseModel):
    timestamp_envio: str = Field(..., description="Timestamp do envio")
    ponte_id: int = Field(..., description="ID da ponte (1 a 15)", ge=1, le=15)
    pacote_leituras: List[LeituraSensor] = Field(..., description="Lista de leituras")

class DiagnosticoPonte(BaseModel):
    ponte_id: int
    status_estrutura: str
    anomalia_detectada: bool
    ia_analise_detalhada: str