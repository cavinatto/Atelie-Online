FROM python:3.11-slim

WORKDIR /app

# dependências do sistema para psycopg2
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# expõe porta
EXPOSE 5000

CMD ["python", "entrypoint.py"]
