#!/bin/bash
# Test runner script for Docker environment
# Copyright (C) 2025 - Licensed under GPL v3

set -e

IMAGE_NAME="md-to-bbcode-test"
CONTAINER_NAME="md-to-bbcode-test-runner"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info "Building test image..."

# Create a test Dockerfile
cat > Dockerfile.test << 'EOF'
# Use the same base as our main image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY md_to_bbcode.py .
COPY test_converter.py .

# Run tests by default
CMD ["python", "test_converter.py"]
EOF

# Build test image
if docker build -f Dockerfile.test -t "$IMAGE_NAME" . > /dev/null 2>&1; then
    print_status "Test image built successfully"
else
    print_error "Failed to build test image"
    exit 1
fi

print_info "Running test suite..."

# Run the tests
if docker run --rm "$IMAGE_NAME"; then
    print_status "All tests completed successfully!"
    
    # Clean up test files
    print_info "Cleaning up..."
    docker rmi "$IMAGE_NAME" > /dev/null 2>&1 || true
    rm -f Dockerfile.test
    
    echo
    echo -e "${GREEN}🎉 Test suite passed! The converter is working correctly.${NC}"
else
    print_error "Tests failed!"
    
    # Clean up test files
    docker rmi "$IMAGE_NAME" > /dev/null 2>&1 || true
    rm -f Dockerfile.test
    
    exit 1
fi
