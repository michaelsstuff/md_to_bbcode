# Use Python 3.11 slim image as base
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY md_to_bbcode.py .

# Make the script executable
RUN chmod +x md_to_bbcode.py

# Create a non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Set the default command
ENTRYPOINT ["python", "md_to_bbcode.py"]
CMD ["--help"]
