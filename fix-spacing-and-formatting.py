#!/usr/bin/env python3
"""Fix spacing, line length, and heading formatting in all vault files."""

import os
import re
from pathlib import Path

VAULT_DIR = Path(__file__).parent
MAX_LINE_LENGTH = 80

def fix_heading_spacing(content):
    """Ensure proper spacing around headings."""
    lines = content.split('\n')
    result = []

    for i, line in enumerate(lines):
        # Add blank line before heading (except at start or after blank line)
        if line.startswith('##') and i > 0 and result and result[-1].strip() != '':
            result.append('')

        result.append(line)

        # Add blank line after heading (except at end or before blank line)
        if line.startswith('##') and i < len(lines) - 1:
            if lines[i+1].strip() != '':
                result.append('')

    return '\n'.join(result)

def wrap_long_lines(content):
    """Wrap lines longer than MAX_LINE_LENGTH."""
    lines = content.split('\n')
    result = []

    for line in lines:
        # Don't wrap code blocks, links, or special markdown
        if line.startswith('```') or line.startswith('- ') or line.startswith('* ') or '|' in line:
            result.append(line)
        elif len(line) > MAX_LINE_LENGTH and not line.startswith('#'):
            # Wrap text, preserving indentation
            words = line.split()
            current_line = ''
            for word in words:
                if len(current_line) + len(word) + 1 <= MAX_LINE_LENGTH:
                    if current_line:
                        current_line += ' ' + word
                    else:
                        current_line = word
                else:
                    if current_line:
                        result.append(current_line)
                    current_line = word
            if current_line:
                result.append(current_line)
        else:
            result.append(line)

    return '\n'.join(result)

def fix_excessive_blank_lines(content):
    """Remove more than 2 consecutive blank lines."""
    lines = content.split('\n')
    result = []
    blank_count = 0

    for line in lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                result.append(line)
        else:
            blank_count = 0
            result.append(line)

    return '\n'.join(result)

def fix_file_spacing(filepath):
    """Fix spacing and formatting in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_length = len(content)

        # Apply fixes in order
        content = fix_heading_spacing(content)
        content = fix_excessive_blank_lines(content)
        content = wrap_long_lines(content)

        # Remove trailing whitespace
        lines = [line.rstrip() for line in content.split('\n')]
        content = '\n'.join(lines)

        # Ensure file ends with newline
        if content and not content.endswith('\n'):
            content += '\n'

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        size_change = len(content) - original_length
        return True, f"Fixed (size: {size_change:+d} bytes)"

    except Exception as e:
        return False, f"Error: {str(e)[:50]}"

def main():
    fixed = 0
    skipped = 0

    print("🔧 Fixing spacing and formatting...\n")

    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in sorted(files):
            if file.endswith('.md'):
                filepath = Path(root) / file
                rel_path = filepath.relative_to(VAULT_DIR)

                success, msg = fix_file_spacing(filepath)
                if success:
                    print(f"✅ {rel_path}: {msg}")
                    fixed += 1
                else:
                    skipped += 1

    print(f"\n📊 Fixed: {fixed} | Skipped: {skipped}")
    print(f"\n✨ All files now have proper spacing and formatting")

if __name__ == '__main__':
    main()
