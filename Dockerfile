# Use Python 3.11 slim image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set default environment variables
ENV LOG_INTERVAL_MIN=0.5
ENV LOG_INTERVAL_MAX=3.5
ENV LOG_FORMAT_JSON=false
ENV LOG_LEVEL=INFO
ENV CONFIG_FILE=logs_config.json

# Command to run the application
CMD ["python", "app.py"] 