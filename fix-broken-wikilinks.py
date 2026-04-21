#!/usr/bin/env python3
"""
Fix broken wikilinks in vault files.

Handles:
- Abbreviated references (SOP-1 → SOP-1-STORE-CONTEXT-SETUP-v2)
- Template references (Template-* → TEMPLATE-*)
- Typos ([[[  → [[)
- Nonexistent files (remove or replace)
"""

import os
import re
from pathlib import Path

# Mapping of broken/abbreviated wikilinks to correct filenames
WIKILINK_FIXES = {
    # Abbreviated SOP references
    r'\[\[SOP-1\]\](?!-)': '[[SOP-1-STORE-CONTEXT-SETUP-v2]]',
    r'\[\[SOP-2\]\](?!-)': '[[SOP-2-KEYWORD-RESEARCH-V2]]',
    r'\[\[SOP-3\]\](?!-)': '[[SOP-3-CLUSTERING-COLLECTION-MAPPING]]',

    # Template references (old pattern)
    r'\[\[Template-KW-Research\]\]': '[[TEMPLATE-APPROVAL-GATE-KEYWORDS]]',
    r'\[\[Template-KW-Approval\]\]': '[[TEMPLATE-APPROVAL-GATE-KEYWORDS]]',
    r'\[\[Template-Collection-Review\]\]': '[[TEMPLATE-APPROVAL-GATE-COLLECTIONS]]',
    r'\[\[Template-Weekly-Update\]\]': '[[TEMPLATE-WEEKLY-UPDATE]]',
    r'\[\[Template-Pepita-Capture\]\]': '[[TEMPLATE-PEPITA-CAPTURE]]',

    # Fix typos (triple brackets)
    r'\[\[\[([^\]]+)\]\]': r'[[\1]]',

    # Nonexistent files (remove from WIKILINK-STRATEGY)
    r'\[\[SOP-4\]\]': '',
    r'\[\[GSC-Monitoring\]\]': '',
    r'\[\[Discord-Setup\]\]': '',
    r'\[\[sop-4-on-page-optimization\]\]': '',
    r'\[\[CLAUDE\.md\]\]': '',
}

def fix_wikilinks_in_file(filepath):
    """Update wikilinks in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Apply fixes
    for pattern, replacement in WIKILINK_FIXES.items():
        content = re.sub(pattern, replacement, content)

    # Clean up double spaces from removed links
    content = re.sub(r'\s{2,}', ' ', content)

    # Write back if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    vault_dir = Path(__file__).parent
    fixed_count = 0

    print("🔧 Fixing broken wikilinks...\n")

    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, vault_dir)

                if fix_wikilinks_in_file(filepath):
                    print(f"✅ {rel_path}")
                    fixed_count += 1

    print(f"\n📊 Fixed {fixed_count} files with broken wikilink corrections")

if __name__ == '__main__':
    main()
