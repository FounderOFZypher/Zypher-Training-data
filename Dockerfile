FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md LICENSE ./
COPY runtime ./runtime
COPY brain ./brain
COPY config ./config

RUN pip install --no-cache-dir -e .

ENV COLTEX_HOST=0.0.0.0
ENV COLTEX_PORT=8080
ENV COLTEX_DEPLOYMENT_PROFILE=lan
ENV COLTEX_OPEN_BROWSER=false

EXPOSE 8080

VOLUME ["/app/workspaces", "/app/data"]

CMD ["coltex", "serve", "--no-browser"]
