FROM python:3.12-slim

WORKDIR /br.com.onggabriel.backend.www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /br.com.onggabriel.backend.www/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /br.com.onggabriel.backend.www/
