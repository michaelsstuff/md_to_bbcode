#!/bin/bash

# Markdown to BBCode Converter - Build and Run Script

set -e

IMAGE_NAME="md-to-bbcode"
CONTAINER_NAME="md-to-bbcode-converter"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🐳 Markdown to BBCode Converter${NC}"
echo "=================================="

# Function to print colored output
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Build the Docker image
build_image() {
    print_info "Building Docker image: $IMAGE_NAME"
    if docker build -t "$IMAGE_NAME" .; then
        print_status "Docker image built successfully"
    else
        print_error "Failed to build Docker image"
        exit 1
    fi
}

# Run a test conversion
test_conversion() {
    print_info "Testing conversion with sample.md"
    
    if [ ! -f "sample.md" ]; then
        print_warning "sample.md not found, skipping test"
        return
    fi
    
    echo -e "\n${YELLOW}--- Original Markdown ---${NC}"
    head -20 sample.md
    echo -e "\n${YELLOW}--- Converted BBCode ---${NC}"
    
    if docker run --rm -v "$(pwd):/data" "$IMAGE_NAME" -f /data/sample.md | head -20; then
        print_status "Test conversion completed"
    else
        print_error "Test conversion failed"
    fi
}

# Show usage examples
show_usage() {
    echo -e "\n${BLUE}📖 Usage Examples:${NC}"
    echo "=================="
    echo
    echo "1. Convert a file:"
    echo "   docker run --rm -v \$(pwd):/data $IMAGE_NAME -f /data/input.md > output.bbcode"
    echo
    echo "2. Convert from stdin:"
    echo "   echo '# Hello **World**' | docker run --rm -i $IMAGE_NAME"
    echo
    echo "3. Convert and save to file:"
    echo "   docker run --rm -v \$(pwd):/data $IMAGE_NAME -f /data/input.md -o /data/output.bbcode"
    echo
    echo "4. Show help:"
    echo "   docker run --rm $IMAGE_NAME --help"
    echo
    echo "5. Interactive mode:"
    echo "   docker run --rm -it -v \$(pwd):/data $IMAGE_NAME"
}

# Main execution
main() {
    case "${1:-build}" in
        "build")
            build_image
            test_conversion
            show_usage
            ;;
        "test")
            test_conversion
            ;;
        "clean")
            print_info "Cleaning up Docker image"
            docker rmi "$IMAGE_NAME" 2>/dev/null || print_warning "Image not found"
            print_status "Cleanup completed"
            ;;
        "help"|"--help"|"-h")
            echo "Usage: $0 [build|test|clean|help]"
            echo
            echo "Commands:"
            echo "  build  - Build Docker image and run test (default)"
            echo "  test   - Run test conversion only"
            echo "  clean  - Remove Docker image"
            echo "  help   - Show this help"
            ;;
        *)
            print_error "Unknown command: $1"
            echo "Use '$0 help' for usage information"
            exit 1
            ;;
    esac
}

main "$@"
