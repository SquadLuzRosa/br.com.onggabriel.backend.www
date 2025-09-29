FROM python:3.12-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY --from=builder /wheels /wheels

RUN pip install --no-cache /wheels/*

COPY . .

EXPOSE 8000

CMD ["gunicorn", "app.wsgi:application", "--bind", "0.0.0.0:8000"]
    

