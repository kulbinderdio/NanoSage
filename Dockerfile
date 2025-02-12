FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for API
EXPOSE 8000

# Environment variable for Ollama host
ENV OLLAMA_HOST=http://host.docker.internal:11434

# Run the API server
CMD ["python", "api.py"]
