#!/usr/bin/env python3
"""Convert vault markdown files to Obsidian Properties native format.

Converts YAML frontmatter to Obsidian Properties (same syntax, but natively parsed).
Validates structure, ensures all required properties present.
"""

import os
import re
from pathlib import Path

VALID_TYPES = ['sop', 'fase', 'conceito', 'template', 'reference', 'automation', 'course', 'skill', 'api']
VALID_STATUS = ['draft', 'ready', 'active']
VALID_FOCO = ['seo', 'technical', 'operational', 'course']

def parse_frontmatter(content):
    """Extract YAML frontmatter from content."""
    match = re.match(r'^---\n(.*?)\n---\s*(.*)$', content, re.DOTALL)
    if not match:
        return None, content

    yaml_content = match.group(1)
    body = match.group(2).lstrip()

    # Parse YAML properties
    properties = {}
    for line in yaml_content.split('\n'):
        if not line.strip() or line.startswith('#'):
            continue

        if ':' in line:
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()

            # Handle arrays (tags, wikilinks)
            if value.startswith('[') and value.endswith(']'):
                # Keep as array notation
                properties[key] = value
            else:
                properties[key] = value

    return properties, body

def validate_properties(properties, filepath):
    """Validate that required properties exist and are valid."""
    required = ['name', 'description', 'type', 'status', 'foco']
    missing = [p for p in required if p not in properties]

    if missing:
        print(f"⚠️  {filepath.relative_to(filepath.parent.parent.parent)}: Missing properties: {missing}")
        return False

    # Validate values
    if properties.get('type') not in VALID_TYPES:
        print(f"⚠️  {filepath.relative_to(filepath.parent.parent.parent)}: Invalid type: {properties.get('type')}")
        return False

    if properties.get('status') not in VALID_STATUS:
        print(f"⚠️  {filepath.relative_to(filepath.parent.parent.parent)}: Invalid status: {properties.get('status')}")
        return False

    if properties.get('foco') not in VALID_FOCO:
        print(f"⚠️  {filepath.relative_to(filepath.parent.parent.parent)}: Invalid foco: {properties.get('foco')}")
        return False

    return True

def build_properties_frontmatter(properties):
    """Build frontmatter with properties in correct order."""
    order = ['name', 'description', 'type', 'status', 'foco', 'tags', 'wikilinks']

    lines = ['---']
    for key in order:
        if key in properties:
            value = properties[key]
            lines.append(f"{key}: {value}")

    # Add any extra properties not in standard order
    for key, value in properties.items():
        if key not in order:
            lines.append(f"{key}: {value}")

    lines.append('---')
    return '\n'.join(lines)

def convert_file(filepath):
    """Convert single file to Obsidian Properties format."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        properties, body = parse_frontmatter(content)

        if properties is None:
            # No frontmatter found, skip
            return False

        if not validate_properties(properties, filepath):
            return False

        # Build new frontmatter
        new_frontmatter = build_properties_frontmatter(properties)
        new_content = f"{new_frontmatter}\n{body}"

        # Only write if changed
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True

        return False

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    vault_dir = Path(__file__).parent
    converted = 0
    skipped = 0

    print("🔄 Converting vault to Obsidian Properties format...\n")

    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                rel_path = filepath.relative_to(vault_dir)

                if convert_file(filepath):
                    print(f"✅ {rel_path}")
                    converted += 1
                else:
                    skipped += 1

    print(f"\n📊 Converted: {converted} | Skipped: {skipped}")
    print("\n✨ Vault is now using Obsidian Properties format")

if __name__ == '__main__':
    main()
