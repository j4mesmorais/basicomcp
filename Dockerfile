# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY mcp_server.py .
# 5. Exponha a porta (uvicorn rodará na 80)
EXPOSE 80
CMD ["uvicorn", "mcp_server:app", "--host", "0.0.0.0", "--port", "80"]
