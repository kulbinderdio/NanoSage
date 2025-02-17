FROM python:3.8-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create results directory with proper permissions
RUN mkdir -p /app/results && chmod 777 /app/results

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download the model
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Copy application code
COPY . .

# Add entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose port for API
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 8000

# Environment variable for Ollama host
ENV OLLAMA_HOST=http://host.docker.internal:11434

# Run the API server
CMD ["python", "api.py"]
