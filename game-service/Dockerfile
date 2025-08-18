FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run FastAPI server
CMD ["sh", "-c", "python wait-for-postgres.py && uvicorn main:app --host 0.0.0.0 --port 8000"]
