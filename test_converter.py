#!/usr/bin/env python3
"""
Test suite for Markdown to BBCode Converter
Copyright (C) 2025 - Licensed under GPL v3
"""

import unittest
import sys
import os

# Add the current directory to the path so we can import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from md_to_bbcode import MarkdownToBBCodeConverter


class TestMarkdownToBBCodeConverter(unittest.TestCase):
    """Test cases for the Markdown to BBCode converter."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.converter = MarkdownToBBCodeConverter()
    
    def test_headers(self):
        """Test header conversion."""
        test_cases = [
            ("# Header 1", "[size=6][b]Header 1[/b][/size]"),
            ("## Header 2", "[size=5][b]Header 2[/b][/size]"),
            ("### Header 3", "[size=4][b]Header 3[/b][/size]"),
            ("#### Header 4", "[size=3][b]Header 4[/b][/size]"),
            ("##### Header 5", "[size=2][b]Header 5[/b][/size]"),
            ("###### Header 6", "[size=1][b]Header 6[/b][/size]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_bold_formatting(self):
        """Test bold text formatting."""
        test_cases = [
            ("**bold**", "[b]bold[/b]"),
            ("__bold__", "[b]bold[/b]"),
            ("This is **bold** text", "This is [b]bold[/b] text"),
            ("Multiple **bold** and **more bold**", "Multiple [b]bold[/b] and [b]more bold[/b]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_italic_formatting(self):
        """Test italic text formatting."""
        test_cases = [
            ("*italic*", "[i]italic[/i]"),
            ("_italic_", "[i]italic[/i]"),
            ("This is *italic* text", "This is [i]italic[/i] text"),
            ("Multiple *italic* and *more italic*", "Multiple [i]italic[/i] and [i]more italic[/i]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_bold_italic_combination(self):
        """Test bold and italic combination."""
        test_cases = [
            ("***bold italic***", "[b][i]bold italic[/i][/b]"),
            ("___bold italic___", "[b][i]bold italic[/i][/b]"),
            ("**bold** and *italic*", "[b]bold[/b] and [i]italic[/i]"),
            ("***combo*** with **bold** and *italic*", "[b][i]combo[/i][/b] with [b]bold[/b] and [i]italic[/i]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_strikethrough(self):
        """Test strikethrough formatting."""
        test_cases = [
            ("~~strikethrough~~", "[s]strikethrough[/s]"),
            ("This is ~~deleted~~ text", "This is [s]deleted[/s] text"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_inline_code(self):
        """Test inline code formatting."""
        test_cases = [
            ("`code`", "[code]code[/code]"),
            ("Use `print()` function", "Use [code]print()[/code] function"),
            ("Multiple `code` and `more code`", "Multiple [code]code[/code] and [code]more code[/code]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_code_blocks(self):
        """Test code block formatting."""
        test_cases = [
            ("```\ncode block\n```", "[code]code block[/code]"),
            ("```python\ndef hello():\n    print('Hello')\n```", "[code]def hello():\n    print('Hello')[/code]"),
            ("```javascript\nconsole.log('test');\n```", "[code]console.log('test');[/code]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_links(self):
        """Test link formatting."""
        test_cases = [
            ("[Google](https://google.com)", "[url=https://google.com]Google[/url]"),
            ("[Link text](https://example.com)", "[url=https://example.com]Link text[/url]"),
            ("Visit [GitHub](https://github.com) for code", "Visit [url=https://github.com]GitHub[/url] for code"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_images(self):
        """Test image formatting."""
        test_cases = [
            ("![Alt text](image.jpg)", "[img]image.jpg[/img]"),
            ("![Logo](https://example.com/logo.png)", "[img]https://example.com/logo.png[/img]"),
            ("![](image.gif)", "[img]image.gif[/img]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_unordered_lists(self):
        """Test unordered list formatting."""
        test_cases = [
            ("* Item 1", "[*] Item 1"),
            ("- Item 1", "[*] Item 1"),
            ("+ Item 1", "[*] Item 1"),
            ("* Item with **bold**", "[*] Item with [b]bold[/b]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_ordered_lists(self):
        """Test ordered list formatting."""
        test_cases = [
            ("1. First item\n2. Second item", "[list=1]\n[*] First item\n[*] Second item\n[/list]"),
            ("1. Item one\n2. Item two\n3. Item three", "[list=1]\n[*] Item one\n[*] Item two\n[*] Item three\n[/list]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_quotes(self):
        """Test blockquote formatting."""
        test_cases = [
            ("> This is a quote", "[quote]This is a quote[/quote]"),
            ("> Quote with **bold**", "[quote]Quote with [b]bold[/b][/quote]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_horizontal_rules(self):
        """Test horizontal rule formatting."""
        test_cases = [
            ("---", "[hr]"),
            ("***", "[hr]"),
            ("___", "[hr]"),
            ("----", "[hr]"),
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)
    
    def test_complex_document(self):
        """Test a complex document with multiple elements."""
        markdown = """# Main Title

This is a **complex** document with *various* formatting.

## Code Example

Here's some `inline code` and a code block:

```python
def hello():
    return "Hello, World!"
```

## Lists and Links

* Visit [Google](https://google.com)
* Check out **bold** text
* Some *italic* formatting

### Quotes

> This is an important quote
> with multiple lines

---

That's all!"""
        
        result = self.converter.convert(markdown)
        
        # Check that key elements are present
        self.assertIn("[size=6][b]Main Title[/b][/size]", result)
        self.assertIn("[b]complex[/b]", result)
        self.assertIn("[i]various[/i]", result)
        self.assertIn("[size=5][b]Code Example[/b][/size]", result)
        self.assertIn("[code]inline code[/code]", result)
        self.assertIn("[code]def hello():\n    return \"Hello, World!\"[/code]", result)
        self.assertIn("[url=https://google.com]Google[/url]", result)
        self.assertIn("[quote]This is an important quote", result)
        self.assertIn("with multiple lines[/quote]", result)
        self.assertIn("[hr]", result)
    
    def test_edge_cases(self):
        """Test edge cases and potential problematic inputs."""
        test_cases = [
            ("", ""),  # Empty string
            ("Plain text", "Plain text"),  # No formatting
            ("**", "**"),  # Incomplete bold
            ("*", "*"),  # Single asterisk
            ("`", "`"),  # Single backtick
            ("# ", "#"),  # Header with just space (should not match, space gets stripped)
        ]
        
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)


class TestCLIIntegration(unittest.TestCase):
    """Test CLI integration and file I/O."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_input_file = "test_input.md"
        self.test_output_file = "test_output.bbcode"
    
    def tearDown(self):
        """Clean up test files."""
        for file in [self.test_input_file, self.test_output_file]:
            if os.path.exists(file):
                os.remove(file)
    
    def test_file_conversion(self):
        """Test file-based conversion."""
        # Create a test input file
        test_content = "# Test\n\nThis is **bold** text."
        with open(self.test_input_file, 'w') as f:
            f.write(test_content)
        
        # Import and use the converter
        from md_to_bbcode import MarkdownToBBCodeConverter
        converter = MarkdownToBBCodeConverter()
        
        # Read, convert, and write
        with open(self.test_input_file, 'r') as f:
            markdown_content = f.read()
        
        bbcode_content = converter.convert(markdown_content)
        
        with open(self.test_output_file, 'w') as f:
            f.write(bbcode_content)
        
        # Verify output
        with open(self.test_output_file, 'r') as f:
            result = f.read()
        
        expected = "[size=6][b]Test[/b][/size]\n\nThis is [b]bold[/b] text."
        self.assertEqual(result, expected)


def run_tests():
    """Run all tests and return the results."""
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Add all test cases
    suite.addTest(unittest.makeSuite(TestMarkdownToBBCodeConverter))
    suite.addTest(unittest.makeSuite(TestCLIIntegration))
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    print("=" * 60)
    print("Markdown to BBCode Converter - Test Suite")
    print("=" * 60)
    
    success = run_tests()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests passed!")
        sys.exit(0)
    else:
        print("❌ Some tests failed!")
        sys.exit(1)
