FROM python:3.14-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:0.9.7 /uv /uvx /bin/

ADD . /app

WORKDIR /app

RUN uv sync --locked

EXPOSE 8000
