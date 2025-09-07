# syntax=docker/dockerfile:1.7-labs
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1     PYTHONUNBUFFERED=1     PIP_NO_CACHE_DIR=1

# System deps (add git if needed)
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential  && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Leverage Docker layer caching: copy only project metadata first
COPY pyproject.toml README.md /app/
# Install build backend and dev tools early for caching
RUN python -m pip install --upgrade pip setuptools wheel

# Create a virtualenv to keep site-packages tidy (optional)
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install project in editable mode with dev extras
# Copy minimal src layout first to satisfy deps if any
COPY src/ /app/src/
RUN pip install -e .[dev]

# Then bring in the rest of the workspace (tests, examples, etc.)
COPY . /app

# Default command drops into shell; override with `docker compose run ...`
CMD ["/bin/bash"]
