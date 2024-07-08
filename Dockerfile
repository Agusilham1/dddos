# Gunakan image dasar Python
FROM python:3.9-slim

# Set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Copy requirements.txt ke working directory
COPY requirements.txt /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy semua file di direktori lokal ke working directory di container
COPY . /app/

# Jalankan script
CMD ["python", "run.py"]
