FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# --- ESTÁGIO 2: Final (A Sala de Estar) ---
# Começamos com um novo ambiente limpo para a imagem final.
FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copia os pacotes pré-compilados do estágio builder.
COPY --from=builder /wheels /wheels

# Instala os pacotes.
RUN pip install --no-cache /wheels/*

# Copia o código-fonte da aplicação.
COPY . .

# Expõe a porta que a aplicação vai usar.
EXPOSE 8000

# Define o comando padrão para iniciar a aplicação.
CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
    

