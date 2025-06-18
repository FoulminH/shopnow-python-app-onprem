FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD ["sh", "-c", "exec gunicorn -b :${PORT:-8080} main:app"]
