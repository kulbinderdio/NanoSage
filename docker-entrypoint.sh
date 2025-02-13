#!/bin/bash
set -e

# Create results directory if it doesn't exist
mkdir -p /app/results

# Set proper permissions
chmod -R 755 /app/results

# Execute the main command
exec "$@"
