#!/bin/bash
# Local semantic-release testing script
# Copyright (C) 2025 - Licensed under GPL v3

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    print_error "Node.js is not installed. Please install Node.js to use semantic-release."
    print_info "Visit: https://nodejs.org/"
    exit 1
fi

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    print_error "npm is not installed. Please install npm."
    exit 1
fi

print_info "Node.js version: $(node --version)"
print_info "npm version: $(npm --version)"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
    print_info "Installing semantic-release dependencies..."
    npm install
    print_success "Dependencies installed"
else
    print_info "Dependencies already installed"
fi

# Show current version
CURRENT_VERSION=$(python -c "from version import __version__; print(__version__)" 2>/dev/null || echo "unknown")
print_info "Current version: $CURRENT_VERSION"

# Check what semantic-release would do (dry run)
print_info "Running semantic-release in dry-run mode..."
print_warning "This will show what would happen without making actual changes"

# Set environment variables for dry run
export CI=true
export GITHUB_ACTIONS=true
export GITHUB_REF=refs/heads/main
export GITHUB_REPOSITORY=YOUR_USERNAME/md_to_bbcode

# Run semantic-release in dry-run mode
if npx semantic-release --dry-run; then
    print_success "Semantic-release dry-run completed successfully"
    print_info "Check the output above to see what would happen on the next release"
else
    print_error "Semantic-release dry-run failed"
    print_info "This might be normal if there are no releasable commits since the last release"
fi

print_info "To create a test commit for releasing:"
print_info "  git commit -m 'feat: add new feature' --allow-empty"
print_info "  git commit -m 'fix: resolve issue' --allow-empty"
print_info "  git commit -m 'feat!: breaking change' --allow-empty"

print_warning "Remember: actual releases only happen on pushes to the main branch in GitHub Actions"
