# Markdown to BBCode Converter

[![CI/CD Pipeline](https://github.com/michaelsstuff/md_to_bbcode/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/michaelsstuff/md_to_bbcode/actions/workflows/ci-cd.yml)
[![semantic-release: conventionalcommits](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
[![Docker Hub](https://img.shields.io/docker/pulls/halandar/md-to-bbcode)](https://hub.docker.com/r/halandar/md-to-bbcode)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python tool that converts Markdown formatted text to BBCode format. Perfect for migrating content from Markdown-based systems to forums, bulletin boards, or any platform that uses BBCode markup.

## Features

- **Comprehensive Format Support**: Headers, bold, italic, strikethrough, code blocks, links, images, lists, quotes, and horizontal rules
- **Flexible I/O**: Command-line interface with stdin/stdout or file-based input/output
- **Dockerized**: Containerized for consistent deployment and easy integration
- **Open Source**: GPL v3 licensed for free use and modification

## Supported Conversions

| Markdown | BBCode | Notes |
|----------|--------|-------|
| `# Header 1` | `[size=6][b]Header 1[/b][/size]` | H1-H6 supported |
| `## Header 2` | `[size=5][b]Header 2[/b][/size]` | Progressive sizing |
| `**bold**` / `__bold__` | `[b]bold[/b]` | Both syntaxes |
| `*italic*` / `_italic_` | `[i]italic[/i]` | Both syntaxes |
| `***bold italic***` | `[b][i]bold italic[/i][/b]` | Nested formatting |
| `~~strikethrough~~` | `[s]strikethrough[/s]` | Complete support |
| `` `inline code` `` | `[code]inline code[/code]` | Inline code |
| `[link text](url)` | `[url=url]link text[/url]` | Full link support |
| `![alt text](image.jpg)` | `[img]image.jpg[/img]` | Image embedding |
| `- list item` / `* item` | `[*] list item` | Unordered lists |
| `1. ordered item` | `[list=1][*] ordered item[/list]` | Ordered lists |
| `> blockquote` | `[quote]blockquote[/quote]` | Multi-line quotes |
| `---` / `***` | `[hr]` | Horizontal rules |

## Quick Start

### Using Docker (Recommended)

1. **Build the image:**
```bash
docker build -t md-to-bbcode .
```

2. **Convert a file:**
```bash
docker run --rm -v $(pwd):/data md-to-bbcode -f /data/input.md -o /data/output.bbcode
```

3. **Convert from stdin:**
```bash
echo "# Hello **World**" | docker run --rm -i md-to-bbcode
```

### Using Python Locally

1. **Set up virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run the converter:**
```bash
python md_to_bbcode.py -f input.md -o output.bbcode
```

## Usage Options

### Command Line Arguments
- `-f, --file`: Input Markdown file path
- `-o, --output`: Output BBCode file path (default: stdout)
- `-h, --help`: Show help message and exit

### Input/Output Methods
- **File to File**: `python md_to_bbcode.py -f input.md -o output.bbcode`
- **File to Stdout**: `python md_to_bbcode.py -f input.md`
- **Stdin to File**: `cat input.md | python md_to_bbcode.py -o output.bbcode`
- **Stdin to Stdout**: `echo "# Title" | python md_to_bbcode.py`

## Docker Usage Examples

### Basic Conversion
```bash
# Convert sample.md to BBCode
docker run --rm -v $(pwd):/data md-to-bbcode -f /data/sample.md
```

### Batch Processing
```bash
# Convert multiple files
for file in *.md; do
    docker run --rm -v $(pwd):/data md-to-bbcode -f "/data/$file" -o "/data/${file%.md}.bbcode"
done
```

### Pipeline Integration
```bash
# Use in a pipeline
cat input.md | docker run --rm -i md-to-bbcode | grep -E '^\[.*\]' > filtered_output.bbcode
```

## Example Conversion

### Input (Markdown)
```markdown
# Sample Document

This is a **sample document** with *italic text* and `inline code`.

## Code Block
```python
def hello():
    print("Hello, World!")
```

### Links and Lists
- [Google](https://google.com)
- [GitHub](https://github.com)

1. First item
2. Second item

> This is a blockquote
> with multiple lines

---
```

### Output (BBCode)
```bbcode
[size=6][b]Sample Document[/b][/size]

This is a [b]sample document[/b] with [i]italic text[/i] and [code]inline code[/code].

[size=5][b]Code Block[/b][/size]
[code]def hello():
    print("Hello, World!")[/code]

[size=4][b]Links and Lists[/b][/size]
[*] [url=https://google.com]Google[/url]
[*] [url=https://github.com]GitHub[/url]

[list=1][*] First item
[*] Second item[/list]

[quote]This is a blockquote
with multiple lines[/quote]

[hr]
```

## Project Structure

```
md_to_bbcode/
├── .github/
│   └── workflows/
│       ├── ci-cd.yml          # Main CI/CD pipeline with semantic-release
│       └── pr-test.yml        # Pull request testing
├── node_modules/              # Node.js dependencies (gitignored)
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
├── test-release.sh           # Local semantic-release testing
├── CHANGELOG.md              # Auto-generated changelog (created by semantic-release)
├── LICENSE                   # GPL v3 license
├── CONTRIBUTING.md           # Contribution guidelines and commit standards
└── README.md                 # This file
```

## Development and Testing

### Run Tests Locally
```bash
# Set up environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run tests
python -m pytest test_converter.py -v
# or
python test_converter.py
```

### Run Tests in Docker
```bash
# Build and run test suite
./run_tests.sh
```

### Build and Test Everything
```bash
# Complete build, test, and demo
./build.sh
```

### Test Coverage
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

## CI/CD Pipeline

This project uses **semantic-release** for automated versioning and GitHub Actions for CI/CD:

### Automated Versioning & Releases
- **Conventional Commits**: Commit messages determine version bumps
- **Semantic Versioning**: Automatic major.minor.patch versioning
- **Automated Changelog**: Generated from commit messages
- **Git Tags**: Automatically created for each release
- **GitHub Releases**: Created with release notes and assets

### Testing Pipeline
- **Multi-Python Support**: Tests run on Python 3.8, 3.9, 3.10, 3.11, and 3.12
- **Pull Request Testing**: Every PR is automatically tested before merge
- **Docker Testing**: Container functionality is verified in CI

### Release & Deployment
- **Conditional Deployment**: Docker images are **only** published when semantic-release creates a new version
- **Multi-Architecture**: Images built for both AMD64 and ARM64 architectures
- **Security Scanning**: Images are scanned for vulnerabilities using Trivy
- **Versioned Images**: Each release creates tagged Docker images (e.g., `v1.2.3`, `1.2`, `1`, `latest`)

### Commit Format
Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): description

feat: add new feature          → Minor version bump (1.0.0 → 1.1.0)
fix: resolve parsing bug       → Patch version bump (1.1.0 → 1.1.1)
feat!: breaking API change     → Major version bump (1.1.1 → 2.0.0)
docs: update readme           → Patch version bump (2.0.0 → 2.0.1)
test: add unit tests          → No version bump
```

See [CONVENTIONAL_COMMITS.md](CONVENTIONAL_COMMITS.md) for detailed guidelines.

### Docker Hub Repository
Published images are available at: `your-dockerhub-username/md-to-bbcode`

```bash
# Pull the latest version
docker pull your-dockerhub-username/md-to-bbcode:latest

# Pull a specific version
docker pull your-dockerhub-username/md-to-bbcode:v1.2.3
```

### Release Workflow
1. **Develop** → Make changes with conventional commits
2. **Push to main** → Triggers automated testing
3. **Semantic Release** → Analyzes commits, creates version, tag, and GitHub release
4. **Docker Build** → Only triggers if a new release was created
5. **Security Scan** → Scans the published image

## Dependencies

- **Python 3.8+**: Core runtime
- **click**: Command-line interface framework
- **markdown**: Markdown parsing (used for validation)

## Docker Image

The Docker image is built on Alpine Linux for minimal size and includes:
- Python 3.11 runtime
- All required dependencies
- Non-root user execution
- Optimized for production use

## License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to:
- Use the software for any purpose
- Study and modify the source code
- Distribute copies of the software
- Distribute modified versions

Under the condition that any distributed work is also licensed under GPL-3.0.

See the [LICENSE](LICENSE) file for full details.

## Contributing

Contributions are welcome! This project uses **semantic-release** for automated versioning.

### Quick Start
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Set up virtual environment: `python3 -m venv venv && source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run tests: `python test_converter.py`
6. **Use conventional commits**: See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines
7. Push to your branch and create a Pull Request

### Commit Message Format
This project uses [Conventional Commits](https://www.conventionalcommits.org/) for automated releases:

```bash
feat: add support for tables           # Minor version bump
fix: resolve header parsing bug        # Patch version bump  
docs: update installation guide        # Patch version bump
test: add integration tests           # No version bump
feat!: redesign conversion API         # Major version bump (breaking change)
```

### Release Process
- **Automated**: Releases are created automatically based on commit messages
- **Semantic Versioning**: Version numbers follow semver (major.minor.patch)
- **Changelog**: Generated automatically from commit messages
- **Docker Images**: Published automatically for each release

For complete guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Support

For issues, questions, or contributions:
- Open an issue on GitHub
- Review the test suite for usage examples
- Check the sample.md file for supported syntax

---

**Made with ❤️ for the open source community**
