# Markdown to BBCode Converter

[![CI/CD Pipeline](https://github.com/michaelsstuff/md_to_bbcode/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/michaelsstuff/md_to_bbcode/actions/workflows/ci-cd.yml)
[![semantic-release: conventionalcommits](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)
[![Docker Hub](https://img.shields.io/docker/pulls/michaelsstuff/md-to-bbcode)](https://hub.docker.com/r/michaelsstuff/md-to-bbcode)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A robust Python tool that converts Markdown formatted text to BBCode format. Perfect for migrating content from Markdown-based systems to forums, bulletin boards, or any platform that uses BBCode markup.

## Features

- **Comprehensive Format Support**: Headers, bold, italic, strikethrough, code blocks, links, images, lists, quotes, and horizontal rules
- **Flexible I/O**: Command-line interface with stdin/stdout or file-based input/output
- **Dockerized**: Containerized for consistent deployment and easy integration
- **Production Ready**: Comprehensive testing, automated releases, and semantic versioning
- **Open Source**: GPL v3 licensed for free use and modification

## Quick Start

### Using Docker (Recommended)

**Pull from Docker Hub:**
```bash
docker pull michaelsstuff/md-to-bbcode:latest
```

**Convert a file:**
```bash
docker run --rm -v $(pwd):/data michaelsstuff/md-to-bbcode -f /data/input.md -o /data/output.bbcode
```

**Convert from stdin:**
```bash
echo "# Hello **World**" | docker run --rm -i michaelsstuff/md-to-bbcode
```

### Using Python Locally

1. **Clone and set up:**
```bash
git clone https://github.com/michaelsstuff/md_to_bbcode.git
cd md_to_bbcode
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run the converter:**
```bash
python md_to_bbcode.py -f input.md -o output.bbcode
```

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

## Usage Options

### Command Line Arguments
- `-f, --file`: Input Markdown file path
- `-o, --output`: Output BBCode file path (default: stdout)
- `-v, --version`: Show version information
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
docker run --rm -v $(pwd):/data michaelsstuff/md-to-bbcode -f /data/sample.md
```

### Batch Processing
```bash
# Convert multiple files
for file in *.md; do
    docker run --rm -v $(pwd):/data michaelsstuff/md-to-bbcode -f "/data/$file" -o "/data/${file%.md}.bbcode"
done
```

### Pipeline Integration
```bash
# Use in a pipeline
cat input.md | docker run --rm -i michaelsstuff/md-to-bbcode | grep -E '^\[.*\]' > filtered_output.bbcode
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

## Installation & Dependencies

### Python Requirements
- **Python 3.8+**: Core runtime
- **click**: Command-line interface framework
- **markdown**: Markdown parsing (used for validation)

### Docker Image
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

Contributions are welcome! This project uses automated versioning and semantic releases.

**Quick contribution steps:**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test them
4. Use conventional commit messages (see [CONTRIBUTING.md](CONTRIBUTING.md))
5. Push to your branch and create a Pull Request

For detailed development setup, testing procedures, and contribution guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

## Support

For issues, questions, or contributions:
- **Issues**: [GitHub Issues](https://github.com/michaelsstuff/md_to_bbcode/issues)
- **Documentation**: Check the [sample.md](sample.md) file for supported syntax examples
- **Testing**: Review the [test suite](test_converter.py) for comprehensive usage examples

---

**Made with ❤️ for the open source community**
