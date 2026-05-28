# 1. Cria a pasta principal e entra nela
mkdir projeto-monitoramento-pontes
cd projeto-monitoramento-pontes

# 2. Inicializa o repositório Git e o Ambiente Virtual do Python
git init
python3 -m venv venv

# 3. Cria as pastas estruturais exigidas e específicas do app [cite: 58, 59, 77, 81, 87]
mkdir -p .github/workflows .agents docs app

# 4. Cria os arquivos base do projeto e do servidor FastAPI
touch .gitignore README.md requirements.txt app/__init__.py app/main.py app/database.py app/models.py app/ai_engine.py