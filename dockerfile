
# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /projeto_erp_new

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o script Python para o contêiner
COPY main.py .

# Execute o script quando o contêiner iniciar
CMD ["streamlit",'run', "main.py"]

