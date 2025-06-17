# Contributing to Markdown to BBCode Converter

Thank you for your interest in contributing to this project! This guide will help you understand our development workflow and contribution standards.

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Git
- Docker (optional, for container testing)

### Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/michaelsstuff/md_to_bbcode.git
   cd md_to_bbcode
   ```

3. **Set up virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run tests** to ensure everything works:
   ```bash
   python test_converter.py
   ```

## Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes
- Write code following existing patterns
- Add tests for new functionality
- Update documentation if needed
- Ensure all tests pass locally

### 3. Test Your Changes
```bash
# Run the test suite
python test_converter.py

# Test CLI functionality
python md_to_bbcode.py --version
echo "# Test **bold**" | python md_to_bbcode.py

# Test with sample file
python md_to_bbcode.py -f sample.md
```

### 4. Docker Testing (Optional)
```bash
# Build and test Docker image
docker build -t md-to-bbcode-test .
echo "# Docker Test" | docker run --rm -i md-to-bbcode-test
```

## Commit Message Guidelines

This project uses **Conventional Commits** for automated versioning and changelog generation. Please follow this format:

### Commit Message Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Commit Types

| Type | Description | Version Impact | Examples |
|------|-------------|----------------|----------|
| `feat` | New feature | Minor release (0.1.0 → 0.2.0) | `feat: add table support` |
| `fix` | Bug fix | Patch release (0.1.0 → 0.1.1) | `fix: resolve header parsing` |
| `perf` | Performance improvement | Patch release | `perf: optimize regex patterns` |
| `docs` | Documentation changes | Patch release | `docs: update API examples` |
| `refactor` | Code refactoring | Patch release | `refactor: simplify converter logic` |
| `test` | Adding/updating tests | No release | `test: add edge case tests` |
| `build` | Build system changes | Patch release | `build: update Docker base image` |
| `ci` | CI configuration changes | No release | `ci: improve test coverage` |
| `chore` | Maintenance tasks | No release | `chore: update dependencies` |
| `style` | Code style changes | No release | `style: format with black` |
| `revert` | Reverting changes | Patch release | `revert: undo feature X` |

### Breaking Changes
For breaking changes that require a major version bump, use one of these formats:

```bash
# Option 1: Add ! after type
feat!: redesign conversion API

# Option 2: Add BREAKING CHANGE in footer
feat: add new converter options

BREAKING CHANGE: The old convert() method signature has changed
```

### Commit Examples

#### ✅ Good Commits
```bash
feat: add strikethrough text support
fix: correct nested list indentation
docs: add usage examples to README
test: add tests for edge cases
perf: improve regex performance for large files
refactor(parser): simplify header detection logic
```

#### ❌ Avoid These
```bash
update stuff           # Too vague
fixed bug             # Not descriptive
WIP                   # Work in progress commits
Added new feature     # Use imperative mood
```

### Scopes (Optional)
Use scopes to specify the area of change:

- `parser` - Markdown parsing logic
- `converter` - BBCode conversion logic
- `cli` - Command-line interface
- `docker` - Docker-related changes
- `test` - Test files

Examples:
```bash
feat(parser): add support for nested quotes
fix(cli): handle empty input gracefully
docs(docker): update container usage examples
```

## Code Guidelines

### Python Style
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Add docstrings for classes and public methods
- Keep functions focused and small

### Testing
- Add tests for all new features
- Include edge cases and error conditions
- Maintain existing test coverage
- Test both Python API and CLI interface

### Documentation
- Update README.md for user-facing changes
- Add docstrings for new functions/methods
- Include usage examples when appropriate
- Update type hints where applicable

## What We're Looking For

### 🐛 Bug Fixes
- Fix parsing edge cases
- Resolve CLI issues
- Improve error handling
- Performance optimizations

### ✨ New Features
- Additional Markdown syntax support
- New BBCode format options
- Enhanced CLI functionality
- Docker improvements

### 📚 Documentation
- Usage examples
- API documentation
- Installation guides
- Tutorial content

### 🧪 Testing
- Additional test cases
- Integration tests
- Performance benchmarks
- Edge case coverage

## Release Process

### Automatic Releases
This project uses semantic-release for automated versioning:

1. **You commit** with conventional format
2. **CI tests** your changes
3. **Semantic-release** analyzes commits and determines version
4. **Automatic release** created with changelog
5. **Docker images** published to registry

### Version Bumping Examples
Given current version `1.2.3`:

- `fix: resolve bug` → `1.2.4` (patch)
- `feat: add feature` → `1.3.0` (minor)
- `feat!: breaking change` → `2.0.0` (major)

No manual version management needed!

## Pull Request Process

### Before Submitting
- [ ] Tests pass locally
- [ ] Code follows style guidelines
- [ ] Commit messages follow conventional format
- [ ] Documentation updated if needed
- [ ] Self-review completed

### PR Description Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature causing existing functionality to change)
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Manual testing completed
- [ ] Docker testing performed (if applicable)

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have performed a self-review
- [ ] I have commented my code where necessary
- [ ] My changes generate no new warnings
- [ ] Tests pass locally
```

## Getting Help

### Questions?
- Check existing issues and discussions
- Review the README.md and documentation
- Look at existing code for patterns
- Ask questions in pull request comments

### Found a Bug?
1. Check if it's already reported
2. Create a minimal reproduction case
3. Include system information (Python version, OS)
4. Provide sample input and expected output

### Feature Requests?
1. Describe the use case
2. Explain the expected behavior
3. Consider implementation complexity
4. Discuss alternatives considered

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Assume good intentions
- Keep discussions on-topic

## Development Reference

### Project Structure
```
md_to_bbcode/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml          # Main CI/CD pipeline with semantic-release
│       └── pr-test.yml        # Pull request testing
├── Dockerfile                 # Docker container configuration
├── .dockerignore              # Docker build exclusions
├── .gitignore                 # Git ignore patterns
├── .releaserc.json            # semantic-release configuration
├── package.json               # Node.js dependencies for semantic-release
├── package-lock.json          # Locked Node.js dependencies
├── requirements.txt           # Python dependencies
├── version.py                 # Version file (managed by semantic-release)
├── md_to_bbcode.py           # Main converter script
├── test_converter.py         # Comprehensive test suite
├── sample.md                 # Sample Markdown file
├── build.sh                  # Build and run script
├── run_tests.sh              # Test runner script
├── CHANGELOG.md              # Auto-generated changelog
├── LICENSE                   # GPL v3 license
├── CONTRIBUTING.md           # This file
└── README.md                 # User documentation
```

### Advanced Testing

#### Local Test Suite
```bash
# Set up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run comprehensive tests
python test_converter.py

# Run with verbose output
python -m pytest test_converter.py -v
```

#### Docker Testing
```bash
# Build and test container
docker build -t md-to-bbcode-dev .
./run_tests.sh

# Complete build, test, and demo
./build.sh
```

#### Test Coverage
The test suite covers:
- All header levels (H1-H6)
- Bold and italic formatting (both syntaxes)
- Code blocks (inline and fenced)
- Links and images
- Ordered and unordered lists
- Blockquotes (single and multi-line)
- Horizontal rules
- Edge cases and error conditions
- Nested formatting combinations

### CI/CD Pipeline Details

#### Automated Versioning & Releases
- **Conventional Commits**: Commit messages determine version bumps
- **Semantic Versioning**: Automatic major.minor.patch versioning
- **Automated Changelog**: Generated from commit messages
- **Git Tags**: Automatically created for each release
- **GitHub Releases**: Created with release notes and assets

#### Testing Pipeline
- **Multi-Python Support**: Tests run on Python 3.8, 3.9, 3.10, 3.11, and 3.12
- **Pull Request Testing**: Every PR is automatically tested before merge
- **Docker Testing**: Container functionality is verified in CI

#### Release & Deployment
- **Conditional Deployment**: Docker images are **only** published when semantic-release creates a new version
- **Multi-Architecture**: Images built for both AMD64 and ARM64 architectures
- **Security Scanning**: Images are scanned for vulnerabilities using Trivy
- **Versioned Images**: Each release creates tagged Docker images (e.g., `v1.2.3`, `1.2`, `1`, `latest`)

#### Release Workflow
1. **Develop** → Make changes with conventional commits
2. **Push to main** → Triggers automated testing
3. **Semantic Release** → Analyzes commits, creates version, tag, and GitHub release
4. **Docker Build** → Only triggers if a new release was created
5. **Security Scan** → Scans the published image

### GitHub Repository Setup

To enable automated Docker image publishing, configure these repository secrets:
- `DOCKER_USERNAME`: Your Docker Hub username  
- `DOCKER_PASSWORD`: Your Docker Hub password or access token

The CI/CD pipeline will automatically:
- Test all changes on multiple Python versions
- Build and test Docker images
- Run semantic-release for version management
- Publish Docker images only on successful releases
- Scan published images for security vulnerabilities

## Recognition

Contributors are recognized in:
- Git commit history
- GitHub contributors page
- Release notes (for significant contributions)

Thank you for contributing to make this project better! 🚀
