# 1. Começamos com uma imagem base do Python.
FROM python:3.12-slim-bookworm

# 2. Define o diretório de trabalho dentro do contêiner.
WORKDIR /app

# 3. Variáveis de ambiente para o Python, recomendadas pelo Django.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 4. Copia apenas o arquivo de dependências primeiro.
#    Isso otimiza o cache do Docker para builds futuros.
COPY requirements.txt .

# 5. Instala as dependências do projeto.
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# 6. Copia todo o resto do código do seu projeto para dentro do contêiner.
COPY . .

# 7. Informa ao Docker que a aplicação dentro deste contêiner usará a porta 8000.
EXPOSE 8000

# 8. Define o comando padrão para iniciar a aplicação.
#    ATENÇÃO: Altere "app.wsgi:application" se a pasta do seu projeto Django
#    que contém o arquivo wsgi.py tiver um nome diferente.
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]

