# Sistema Inteligente de Monitoramento Estrutural - Engenharia Avançada S.A.

## Sobre o Projeto
Este projeto é um Mínimo Produto Viável (MVP) desenvolvido para o governo estadual, visando o monitoramento contínuo e inteligente de 15 pontes críticas da região metropolitana. O sistema substitui as inspeções manuais trimestrais por uma API de processamento em tempo real que recebe dados de sensores (acelerômetros, extensômetros, etc.) e utiliza Inteligência Artificial para emitir diagnósticos estruturais.

A análise automatizada é estritamente embasada nas normas técnicas:
- **NBR 6118:** Projeto de estruturas de concreto (Limites de fadiga).
- **NBR 8681:** Ações e segurança nas estruturas.

## Tecnologias Utilizadas
- **Linguagem:** Python 3.12+
- **Framework Web:** FastAPI (Alta performance e processamento assíncrono)
- **Validação de Dados:** Pydantic V2
- **Integração Contínua (CI):** GitHub Actions
- **IA e Integração:** Engenharia de Prompt (Zero/Few-Shot, Chain-of-Thought) e arquitetura MCP para integração BIM (ISO 16739).

##  Como o Código Funciona
1. **Ingestão:** Os sensores de campo enviam lotes de leituras em formato JSON para a rota `/api/v1/monitoramento/analisar`.
2. **Validação:** A camada de modelos (Pydantic) garante que apenas dados válidos sejam processados (ex: rejeita dados de pontes fora do escopo de 1 a 15).
3. **Análise de IA:** O motor de inferência calcula a média de vibração e aplica regras de engenharia. Se o limite de 5.0 for ultrapassado, o sistema classifica o status da ponte como **CRÍTICO**.
4. **Resposta:** A API devolve um diagnóstico detalhado estruturado que pode ser integrado a softwares CAD/BIM e dashboards.

---

## 💻 Instruções de Instalação e Execução

### 1. Preparação do Ambiente
Abra o seu terminal e execute os comandos abaixo para criar a estrutura do projeto e o ambiente virtual:

```bash

mkdir projeto-monitoramento-pontes
cd projeto-monitoramento-pontes

git init
python3 -m venv venv

source venv/bin/activate

mkdir -p .github/workflows .agents docs app