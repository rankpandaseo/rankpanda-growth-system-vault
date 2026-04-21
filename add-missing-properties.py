#!/usr/bin/env python3
"""Add missing Properties to files that don't have them."""

import os
import re
from pathlib import Path

VAULT_DIR = Path(__file__).parent

# Mapping of file patterns to properties
PROPERTIES_MAP = {
    # Templates
    'TEMPLATE-': {
        'type': 'template',
        'status': 'draft',
        'foco': 'operational',
        'tags': '[template, reusable]',
    },
    # Course modules
    'COURSE-M': {
        'type': 'course',
        'status': 'active',
        'foco': 'course',
        'tags': '[course, learning]',
    },
    # Course metadata
    'COURSE-': {
        'type': 'course',
        'status': 'active',
        'foco': 'course',
        'tags': '[course, reference]',
    },
    # Automations
    'AUTOMATION-': {
        'type': 'automation',
        'status': 'active',
        'foco': 'operational',
        'tags': '[automation, script]',
    },
    # Pepitas
    'COURSE-PEPITAS': {
        'type': 'course',
        'status': 'active',
        'foco': 'course',
        'tags': '[pepitas, learning]',
    },
    # References
    'REFERENCE-': {
        'type': 'reference',
        'status': 'active',
        'foco': 'operational',
        'tags': '[reference, index]',
    },
}

def guess_properties(filepath, filename):
    """Guess properties based on filename and content."""
    # Try patterns
    for pattern, props in PROPERTIES_MAP.items():
        if pattern in filename:
            return props

    # Default to reference if nothing matches
    return {
        'type': 'reference',
        'status': 'draft',
        'foco': 'operational',
        'tags': '[reference]',
    }

def extract_title_from_content(content):
    """Extract title from markdown content."""
    lines = content.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return None

def generate_name_from_filename(filename):
    """Convert filename to name property (kebab-case)."""
    # Remove .md extension
    name = filename.replace('.md', '')
    # Convert to lowercase
    name = name.lower()
    return name

def add_properties_to_file(filepath):
    """Add Properties frontmatter to file if missing."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already has Properties
        if content.startswith('---\n'):
            return False, "Already has Properties"

        # Generate properties
        filename = filepath.name
        name = generate_name_from_filename(filename)
        title = extract_title_from_content(content)
        description = title if title else filename

        # Guess type based on filename
        guessed = guess_properties(filepath, filename)

        # Build Properties
        properties = f"""---
name: {name}
description: {description}
type: {guessed['type']}
status: {guessed['status']}
foco: {guessed['foco']}
tags: {guessed['tags']}
wikilinks: []
---

{content}"""

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(properties)

        return True, f"Added properties (type={guessed['type']})"

    except Exception as e:
        return False, f"Error: {e}"

def main():
    added = 0
    skipped = 0

    print("🔄 Adding missing Properties...\n")

    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in sorted(files):
            if file.endswith('.md'):
                filepath = Path(root) / file
                rel_path = filepath.relative_to(VAULT_DIR)

                success, msg = add_properties_to_file(filepath)
                if success:
                    print(f"✅ {rel_path}: {msg}")
                    added += 1
                else:
                    skipped += 1

    print(f"\n📊 Added: {added} | Skipped: {skipped}")
    print(f"\n✨ All files now have Properties frontmatter")

if __name__ == '__main__':
    main()
