FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Create results directory with proper permissions
RUN mkdir -p /app/results && chmod 777 /app/results

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Add entrypoint script
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose port for web interface
ENTRYPOINT ["docker-entrypoint.sh"]
EXPOSE 5000

# Run the web server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "300", "--workers", "4", "--threads", "2", "app:app"]
