#!/usr/bin/env python3
"""
Filename Validator for RankPanda Vault

Ensures all markdown files follow the naming pattern:
[TYPE]-[NAME]-[VERSION/CONTEXT].md in CamelCase

Types: SOP, FASE, CONCEITO, TEMPLATE, REFERENCE, AUTOMATION, COURSE, SKILL

Detects:
- Lowercase letters (breaks wikilinks)
- Spaces in filenames
- Inconsistent naming pattern
- Missing TYPE prefix
"""

import os
import re
import sys
from pathlib import Path

# Define allowed patterns
PATTERN = re.compile(r'^([A-Z][A-Za-z0-9]*-)+[A-Za-z0-9\-\.]+\.md$')
ALLOWED_TYPES = ['SOP', 'FASE', 'CONCEITO', 'TEMPLATE', 'REFERENCE', 'AUTOMATION', 'COURSE', 'SKILL', 'API']

def validate_filename(filepath):
    """Check if filename follows pattern and conventions."""
    filename = os.path.basename(filepath)

    # Special cases that are OK
    if filename in ['00-README.md', 'todo.md', 'interlinking-validator.py']:
        return True, None

    errors = []

    # Check for spaces
    if ' ' in filename:
        errors.append("Contains spaces (should use hyphens)")

    # Check for lowercase letters (except in version tags like -v2)
    if re.search(r'[a-z]+', filename.split('.')[0]):
        # Allow lowercase in the middle but not at the start of segments
        parts = filename.split('-')
        for part in parts:
            if part and part[0].islower() and not re.match(r'^v\d+$', part):
                errors.append(f"Lowercase in '{part}' (should be CamelCase)")
                break

    # Check for TYPE prefix
    first_part = filename.split('-')[0]
    if first_part not in ALLOWED_TYPES and not first_part.startswith(('CONCEITO', 'pilot')):
        if first_part not in ['00', 'README', 'WIKILINK']:
            errors.append(f"Missing TYPE prefix (got '{first_part}', allowed: {', '.join(ALLOWED_TYPES)})")

    # Check pattern
    if not PATTERN.match(filename) and filename not in ['WIKILINK-STRATEGY.md', 'API-REGISTRY.md']:
        errors.append("Doesn't match pattern [TYPE]-[NAME]-[VERSION].md")

    return len(errors) == 0, errors

def suggest_name(filepath):
    """Suggest a conforming filename."""
    filename = os.path.basename(filepath)

    # Special cases
    if filename == '00-README.md':
        return 'REFERENCE-README.md'
    if filename == 'todo.md':
        return 'REFERENCE-TODO.md'
    if filename == 'WIKILINK-STRATEGY.md':
        return 'REFERENCE-WIKILINK-STRATEGY.md'

    # Extract parts
    parts = filename.replace('.md', '').split('-')

    # Capitalize all parts except 'v' versions
    clean_parts = []
    for part in parts:
        if re.match(r'^v\d+$', part):
            clean_parts.append(part)
        elif part:
            clean_parts.append(part.capitalize())

    # Ensure TYPE prefix
    if clean_parts[0] not in ALLOWED_TYPES and not clean_parts[0].startswith('CONCEITO'):
        type_map = {
            'template': 'TEMPLATE',
            'approval': 'TEMPLATE',
            'report': 'TEMPLATE',
            'briefing': 'TEMPLATE',
            'update': 'TEMPLATE',
            'pepita': 'TEMPLATE',
            'kw': 'REFERENCE',
            'keyword': 'REFERENCE',
            'sop': 'SOP',
            'fase': 'FASE',
        }
        guessed_type = type_map.get(clean_parts[0].lower(), 'TEMPLATE')
        clean_parts.insert(0, guessed_type)

    return '-'.join(clean_parts) + '.md'

def main():
    vault_dir = Path(__file__).parent

    print("🔍 Filename Validator — RankPanda Vault\n")
    print(f"Scanning: {vault_dir}\n")

    conforming = []
    non_conforming = []

    # Scan all markdown files
    for root, dirs, files in os.walk(vault_dir):
        # Skip certain directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md') or file.endswith('.py'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, vault_dir)

                # Skip this validator script and external files
                if 'validator.py' in file or 'scripts' in root:
                    continue

                is_valid, errors = validate_filename(rel_path)

                if is_valid:
                    conforming.append(rel_path)
                else:
                    suggested = suggest_name(file)
                    non_conforming.append({
                        'file': rel_path,
                        'errors': errors,
                        'suggested': suggested
                    })

    # Report results
    print(f"✅ Conforming: {len(conforming)}")
    for f in sorted(conforming)[:5]:
        print(f"   {f}")
    if len(conforming) > 5:
        print(f"   ... and {len(conforming) - 5} more")

    print(f"\n❌ Non-conforming: {len(non_conforming)}")
    if non_conforming:
        for item in sorted(non_conforming, key=lambda x: x['file']):
            print(f"\n   File: {item['file']}")
            print(f"   Issues: {', '.join(item['errors'])}")
            print(f"   Suggest: {item['suggested']}")

    print(f"\n📊 Summary: {len(conforming)}/{len(conforming) + len(non_conforming)} conforming")

    return 0 if len(non_conforming) == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
