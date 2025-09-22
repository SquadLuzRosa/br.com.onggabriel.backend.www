FROM python:3.12-slim-bookworm AS builder

WORKDIR /br.com.onggabriel.backend.www

RUN apt-get update && \
apt-get install -y --no-install-recommends gcc && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && \
pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt


<<<<<<< HEAD
FROM python:3-12-slim-bookworm
=======
FROM python:3.12-slim-bookworm
>>>>>>> 9f977acd9113e8d2f77f5d909a0dfac7ec30ea89

WORKDIR /br.com.onggabriel.backend.www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup --system django && adduser --system --ingroup django django

COPY --from=builder /wheels /wheels

RUN pip install --no-cache /wheels/*

COPY . .

RUN chown -R django:django /br.com.onggabriel.backend.www

USER django

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

EXPOSE 8000


