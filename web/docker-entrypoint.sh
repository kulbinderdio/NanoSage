#!/bin/bash
set -e

# Create necessary directories if they don't exist
mkdir -p /app/results
mkdir -p /app/templates

# Set proper permissions
chmod -R 755 /app/results
chmod -R 755 /app/templates

# Execute the main command
exec "$@"
