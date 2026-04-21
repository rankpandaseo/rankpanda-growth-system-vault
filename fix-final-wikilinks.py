#!/usr/bin/env python3
"""Final wikilink fixes for remaining broken links."""

import os
import re
from pathlib import Path

FIXES = {
    # Add -v2 version to incomplete SOP-1 references
    r'\[\[SOP-1-STORE-CONTEXT-SETUP\]\]': '[[SOP-1-STORE-CONTEXT-SETUP-v2]]',

    # Fix pipe syntax (remove description, keep link)
    r'\[\[SOP-2-KEYWORD-RESEARCH-V2\|[^\]]*\]\]': '[[SOP-2-KEYWORD-RESEARCH-V2]]',

    # Remove bash code incorrectly interpreted as wikilink
    r'\[\[\s*-n\s*\$\(git status -s\)\s*\]\]': '[[ -n $(git status -s) ]]',
}

def fix_file(filepath):
    """Fix wikilinks in a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    for pattern, replacement in FIXES.items():
        content = re.sub(pattern, replacement, content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

vault_dir = Path(__file__).parent
fixed = 0

for root, dirs, files in os.walk(vault_dir):
    dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

    for file in files:
        if file.endswith('.md'):
            path = os.path.join(root, file)
            if fix_file(path):
                print(f"✅ {os.path.relpath(path, vault_dir)}")
                fixed += 1

print(f"\n📊 Fixed {fixed} files")
