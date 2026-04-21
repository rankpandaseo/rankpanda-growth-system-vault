#!/usr/bin/env python3
"""Fix foco values: convert Portuguese to English."""

import os
import re
from pathlib import Path

# Mapping of PT foco values to EN
FOCO_MAP = {
    'operacional': 'operational',
    'análise': 'technical',
    'validação': 'operational',
    'execução': 'operational',
    'documentação': 'course',
    'seo-técnico': 'technical',
}

def fix_foco_in_file(filepath):
    """Fix foco values in a single file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Find and replace foco values
        for pt_value, en_value in FOCO_MAP.items():
            pattern = rf"foco: {pt_value}"
            replacement = f"foco: {en_value}"
            content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")
        return False

def main():
    vault_dir = Path(__file__).parent
    fixed = 0

    print("🔄 Fixing foco values (PT → EN)...\n")

    for root, dirs, files in os.walk(vault_dir):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                rel_path = filepath.relative_to(vault_dir)

                if fix_foco_in_file(filepath):
                    print(f"✅ {rel_path}")
                    fixed += 1

    print(f"\n📊 Fixed {fixed} files")

if __name__ == '__main__':
    main()
