# FROM python

# # 
# WORKDIR /code

# # 
# COPY ./requirements.txt /code/requirements.txt

# # 
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# # 
# COPY ./app /code/app

# # 
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Dockerfile

# Usa a mesma imagem base (Python)
FROM python:3.11.2-slim-buster

# Define o diretório de trabalho
WORKDIR /code

# Copia o arquivo de requisitos para instalar dependências
COPY ./requirements.txt /code/requirements.txt

# Instala as dependências
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia o diretório do aplicativo
COPY ./app /code/app

# Verifica se a variável de ambiente ENVIRONMENT é definida como TEST
# Se não, executa o aplicativo
CMD ["sh", "-c", "if [ \"$ENVIRONMENT\" != \"TEST\" ]; then uvicorn app.main:app --host 0.0.0.0 --port 80 --reload; fi"]
