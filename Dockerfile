FROM python:3.12-slim

WORKDIR /br.com.onggabriel.backend.www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update

COPY requirements.txt /br.com.onggabriel.backend.www/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /br.com.onggabriel.backend.www/
