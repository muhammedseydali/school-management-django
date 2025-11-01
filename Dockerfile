FROM python:3.12-slim

COPY . /app
WORKDIR /app


RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Ensure entrypoint is clean and executable
RUN apt-get update && apt-get install -y dos2unix && \
    dos2unix /app/entrypoint.sh && chmod +x /app/entrypoint.sh && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
