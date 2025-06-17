#!/usr/bin/env python3
"""
Markdown to BBCode Converter
A utility to convert Markdown formatted text to BBCode format.

Copyright (C) 2025

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import re
import sys
from typing import Dict, List, Tuple
import click

# Import version
try:
    from version import __version__
except ImportError:
    __version__ = "unknown"


class MarkdownToBBCodeConverter:
    """Converts Markdown syntax to BBCode syntax."""
    
    def __init__(self):
        # Define conversion patterns (order matters for some patterns)
        self.patterns = [
            # Headers (require non-empty content)
            (r'^# (.+)$', r'[size=6][b]\1[/b][/size]'),
            (r'^## (.+)$', r'[size=5][b]\1[/b][/size]'),
            (r'^### (.+)$', r'[size=4][b]\1[/b][/size]'),
            (r'^#### (.+)$', r'[size=3][b]\1[/b][/size]'),
            (r'^##### (.+)$', r'[size=2][b]\1[/b][/size]'),
            (r'^###### (.+)$', r'[size=1][b]\1[/b][/size]'),
            
            # Code blocks and inline code (before other formatting)
            (r'```(\w+)?\n(.*?)\n```', r'[code]\2[/code]'),  # Code blocks with language
            (r'```\n(.*?)\n```', r'[code]\1[/code]'),        # Code blocks without language
            (r'`([^`]+)`', r'[code]\1[/code]'),              # Inline code
            
            # Images (must come before links to avoid conflicts)
            (r'!\[([^\]]*)\]\(([^)]+)\)', r'[img]\2[/img]'),
            
            # Links
            (r'\[([^\]]+)\]\(([^)]+)\)', r'[url=\2]\1[/url]'),
            
            # Lists (unordered)
            (r'^[\*\-\+] (.+)$', r'[*] \1'),
            
            # Quotes
            (r'^> (.+)$', r'[quote]\1[/quote]'),
            
            # Horizontal rule
            (r'^---+$', r'[hr]'),
            (r'^\*\*\*+$', r'[hr]'),
            (r'^___+$', r'[hr]'),
        ]
    
    def process_inline_formatting(self, text: str) -> str:
        """Process inline formatting (bold, italic) more carefully to avoid nesting."""
        
        # Handle triple asterisks/underscores (bold+italic) first
        text = re.sub(r'\*\*\*(.+?)\*\*\*', r'[b][i]\1[/i][/b]', text)
        text = re.sub(r'___(.+?)___', r'[b][i]\1[/i][/b]', text)
        
        # Handle double asterisks/underscores (bold)
        text = re.sub(r'\*\*(.+?)\*\*', r'[b]\1[/b]', text)
        text = re.sub(r'__(.+?)__', r'[b]\1[/b]', text)
        
        # Handle single asterisks/underscores (italic) - avoid conflicts with bold
        text = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'[i]\1[/i]', text)
        text = re.sub(r'(?<!_)_([^_]+?)_(?!_)', r'[i]\1[/i]', text)
        
        # Handle strikethrough
        text = re.sub(r'~~(.+?)~~', r'[s]\1[/s]', text)
        
        return text
    
    def convert_line(self, line: str) -> str:
        """Convert a single line from Markdown to BBCode."""
        result = line
        
        # Process formatting patterns in specific order to avoid conflicts
        for pattern, replacement in self.patterns:
            if pattern.startswith('^'):
                # Line-specific patterns (headers, quotes, lists, etc.)
                result = re.sub(pattern, replacement, result, flags=re.MULTILINE)
            else:
                # Inline patterns
                result = re.sub(pattern, replacement, result)
        
        # Apply inline formatting separately for better control
        result = self.process_inline_formatting(result)
        
        return result
    
    def convert_text(self, markdown_text: str) -> str:
        """Convert entire Markdown text to BBCode."""
        lines = markdown_text.split('\n')
        converted_lines = []
        in_code_block = False
        code_block_content = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Handle multi-line code blocks
            if line.strip().startswith('```'):
                if not in_code_block:
                    # Start of code block
                    in_code_block = True
                    code_block_content = []
                    language = line.strip()[3:].strip()
                else:
                    # End of code block
                    in_code_block = False
                    code_content = '\n'.join(code_block_content)
                    converted_lines.append(f'[code]{code_content}[/code]')
                    code_block_content = []
                i += 1
                continue
            
            if in_code_block:
                code_block_content.append(line)
            else:
                converted_line = self.convert_line(line)
                converted_lines.append(converted_line)
            
            i += 1
        
        # Handle unclosed code block
        if in_code_block and code_block_content:
            code_content = '\n'.join(code_block_content)
            converted_lines.append(f'[code]{code_content}[/code]')
        
        return '\n'.join(converted_lines)
    
    def convert_ordered_lists(self, text: str) -> str:
        """Convert ordered lists to BBCode format."""
        lines = text.split('\n')
        result_lines = []
        in_list = False
        
        for line in lines:
            # Check if line is an ordered list item
            if re.match(r'^\d+\.\s+(.+)$', line):
                if not in_list:
                    result_lines.append('[list=1]')
                    in_list = True
                match = re.match(r'^\d+\.\s+(.+)$', line)
                result_lines.append(f'[*] {match.group(1)}')
            else:
                if in_list:
                    result_lines.append('[/list]')
                    in_list = False
                result_lines.append(line)
        
        # Close list if still open
        if in_list:
            result_lines.append('[/list]')
        
        return '\n'.join(result_lines)
    
    def post_process(self, text: str) -> str:
        """Apply post-processing fixes."""
        # Handle ordered lists
        text = self.convert_ordered_lists(text)
        
        # Fix multiple consecutive quote blocks
        text = re.sub(r'\[/quote\]\n\[quote\]', '\n', text)
        
        # Fix empty headers (edge case)
        text = re.sub(r'\[size=\d+\]\[b\]\[/b\]\[/size\]', '', text)
        
        # Clean up extra whitespace
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
    
    def convert(self, markdown_text: str) -> str:
        """Main conversion method."""
        bbcode_text = self.convert_text(markdown_text)
        bbcode_text = self.post_process(bbcode_text)
        return bbcode_text


@click.command()
@click.option('--input', '-i', type=click.File('r'), default=None,
              help='Input Markdown file (default: stdin)')
@click.option('--output', '-o', type=click.File('w'), default=sys.stdout,
              help='Output BBCode file (default: stdout)')
@click.option('--file', '-f', type=click.Path(exists=True),
              help='Input file path (alternative to --input)')
@click.version_option(version=__version__, prog_name='md-to-bbcode')
def main(input, output, file):
    """Convert Markdown text to BBCode format."""
    
    converter = MarkdownToBBCodeConverter()
    
    try:
        if file:
            with open(file, 'r', encoding='utf-8') as f:
                markdown_content = f.read()
        elif input:
            markdown_content = input.read()
        else:
            # Default to stdin if no input specified
            markdown_content = sys.stdin.read()
        
        bbcode_content = converter.convert(markdown_content)
        output.write(bbcode_content)
        
        if output != sys.stdout:
            click.echo(f"✅ Conversion completed successfully!", err=True)
        
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    main()
