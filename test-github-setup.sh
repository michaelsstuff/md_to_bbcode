#!/bin/bash

# Test script to verify GitHub repository setup
# This script should be run after pushing to GitHub

set -e

echo "🔍 Testing GitHub repository setup..."

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository"
    exit 1
fi

# Check if we have a remote origin
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "❌ No remote origin configured"
    exit 1
fi

ORIGIN_URL=$(git remote get-url origin)
echo "✅ Remote origin: $ORIGIN_URL"

# Check if we're on main branch
CURRENT_BRANCH=$(git branch --show-current)
if [ "$CURRENT_BRANCH" != "main" ]; then
    echo "⚠️  Currently on branch: $CURRENT_BRANCH (should be 'main')"
else
    echo "✅ On main branch"
fi

# Check if we have the required files
echo ""
echo "📋 Checking required files..."

required_files=(
    ".github/workflows/ci-cd.yml"
    ".github/workflows/pr-test.yml"
    "package.json"
    "package-lock.json"
    ".releaserc.json"
    "CONTRIBUTING.md"
    "README.md"
    "LICENSE"
)

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ $file (missing)"
        exit 1
    fi
done

echo ""
echo "🐳 Checking Docker setup..."

# Check if Docker is available
if ! command -v docker &> /dev/null; then
    echo "⚠️  Docker not found (install for local testing)"
else
    echo "✅ Docker available"
    
    # Try to build the image
    if docker build -t md-to-bbcode:test . > /dev/null 2>&1; then
        echo "✅ Docker image builds successfully"
        
        # Test the image
        if echo "# Test" | docker run --rm -i md-to-bbcode:test > /dev/null 2>&1; then
            echo "✅ Docker image works correctly"
        else
            echo "❌ Docker image failed to run"
            exit 1
        fi
    else
        echo "❌ Docker image build failed"
        exit 1
    fi
fi

echo ""
echo "🧪 Running tests..."

# Run Python tests
if python test_converter.py > /dev/null 2>&1; then
    echo "✅ Python tests pass"
else
    echo "❌ Python tests failed"
    exit 1
fi

echo ""
echo "📦 Checking Node.js setup..."

# Check if Node.js is available
if ! command -v npm &> /dev/null; then
    echo "⚠️  npm not found (needed for semantic-release)"
else
    echo "✅ npm available"
    
    # Check if dependencies are installed
    if [ -d "node_modules" ]; then
        echo "✅ Node.js dependencies installed"
    else
        echo "🔄 Installing Node.js dependencies..."
        npm ci
        echo "✅ Node.js dependencies installed"
    fi
fi

echo ""
echo "🎯 Next steps:"
echo "1. Push to GitHub: git push origin main"
echo "2. Check GitHub Actions: https://github.com/YOUR_USERNAME/md_to_bbcode/actions"
echo "3. Configure repository secrets:"
echo "   - DOCKER_USERNAME: Your Docker Hub username"
echo "   - DOCKER_PASSWORD: Your Docker Hub password/token"
echo "4. Make a commit with 'feat: initial release' to trigger first release"

echo ""
echo "🎉 Setup verification complete!"
