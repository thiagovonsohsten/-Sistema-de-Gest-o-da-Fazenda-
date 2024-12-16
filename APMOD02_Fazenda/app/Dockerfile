# Utilizando uma imagem base do Python
FROM python:3.10-slim

# Configurações do diretório da aplicação
WORKDIR /app

# Instalação das dependências
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiando o código da aplicação
COPY . .

# Comando para iniciar a aplicação
CMD ["python", "main.py"]
