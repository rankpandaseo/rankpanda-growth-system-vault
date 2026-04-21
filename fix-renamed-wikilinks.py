#!/usr/bin/env python3
"""
Fix wikilinks after filename refactoring.

Maps old wikilinks to new filenames and updates all .md files.
"""

import os
import re
from pathlib import Path

# Mapping of old wikilink names to new filenames
WIKILINK_MAPPING = {
    # Memory files
    'MEMORY': 'REFERENCE-MEMORY-INDEX',
    'decisions': 'REFERENCE-DECISIONS',
    'lessons': 'REFERENCE-LESSONS',
    'people': 'REFERENCE-PEOPLE',
    'pilot-vibradores': 'PILOT-VIBRADORES-00-MASTER-PLAN',
    'estado-atual': 'REFERENCE-ESTADO-ATUAL',

    # Template files
    'pepita-capture-template': 'TEMPLATE-PEPITA-CAPTURE',
    'approval-gate-collections': 'TEMPLATE-APPROVAL-GATE-COLLECTIONS',
    'before-after-report-template': 'TEMPLATE-BEFORE-AFTER-REPORT',
    'kickoff-briefing-form': 'TEMPLATE-KICKOFF-BRIEFING-FORM',
    'approval-gate-keywords': 'TEMPLATE-APPROVAL-GATE-KEYWORDS',
    'weekly-update-template': 'TEMPLATE-WEEKLY-UPDATE',
    'approval-gate-products': 'TEMPLATE-APPROVAL-GATE-PRODUCTS',

    # Pilot project files
    'keyword-research': 'PILOT-VIBRADORES-01-KEYWORD-RESEARCH',
    'loja-setup-7d': 'PILOT-VIBRADORES-02-LOJA-SETUP-7D',
    'MASTER-PLAN': 'PILOT-VIBRADORES-00-MASTER-PLAN',
}

def fix_wikilinks_in_file(filepath):
    """Update all wikilinks in a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace wikilinks
    for old, new in WIKILINK_MAPPING.items():
        # Case-insensitive pattern that captures the exact format
        pattern = r'\[\[' + re.escape(old) + r'\]\]'
        replacement = f'[[{new}]]'
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    # Write back if changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    vault_dir = Path(__file__).parent
    fixed_count = 0

    print("🔧 Fixing renamed wikilinks...\n")

    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                rel_path = os.path.relpath(filepath, vault_dir)

                if fix_wikilinks_in_file(filepath):
                    print(f"✅ {rel_path}")
                    fixed_count += 1

    print(f"\n📊 Fixed {fixed_count} files with wikilink updates")

if __name__ == '__main__':
    main()
