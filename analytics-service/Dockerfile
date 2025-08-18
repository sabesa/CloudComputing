FROM python:3.10-slim

WORKDIR /app

# Install PostgreSQL client tools for pg_isready
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python wait-for-postgres.py && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

