FROM python:3.14-slim-bookworm

# Copy UV
COPY --from=ghcr.io/astral-sh/uv:0.9.7 /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-install-project

# Copy application code
COPY . .

# Sync project itself
RUN uv sync --frozen

EXPOSE 8000
