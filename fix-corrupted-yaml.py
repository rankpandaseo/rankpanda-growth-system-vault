#!/usr/bin/env python3
"""Fix corrupted YAML frontmatter where closing --- got merged with markdown."""

import re
from pathlib import Path

def fix_corrupted_file(filepath: Path) -> bool:
    """Fix a file with corrupted YAML frontmatter."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if YAML closing tag is merged with markdown (--- followed by # or space)
        if not re.search(r'^--- [^ ]', content, re.MULTILINE):
            return False  # Not corrupted

        # Extract the valid YAML block
        # Pattern: starts with ---, find content until we hit --- [something]
        yaml_match = re.match(r'^---\n(.*?)\n---\s+\S+', content, re.DOTALL)

        if not yaml_match:
            # Fallback: try to extract piece by piece
            lines = content.split('\n')
            yaml_lines = []
            body_start_idx = 0

            for i, line in enumerate(lines):
                if i == 0 and line == '---':
                    continue
                if line.startswith('---'):
                    # This is where YAML ends
                    body_start_idx = i + 1
                    break
                yaml_lines.append(line)

            if not yaml_lines:
                return False

            # Clean up yaml_lines
            yaml_text = '\n'.join(yaml_lines)

            # Remove any markdown content merged into YAML
            yaml_text = re.sub(r' ##.*$', '', yaml_text, flags=re.MULTILINE)
            yaml_text = re.sub(r' ```.*$', '', yaml_text, flags=re.MULTILINE)

            # Rejoin with the body
            body = '\n'.join(lines[body_start_idx:])

            # Reconstruct file
            fixed_content = f"---\n{yaml_text}\n---\n\n{body}"
        else:
            yaml_block = yaml_match.group(1)
            # Get everything after the corrupted closing tag
            after_match = re.search(r'^--- [^ ](.*)', content, re.MULTILINE | re.DOTALL)
            body_content = after_match.group(1) if after_match else ''

            # Clean up yaml_block
            yaml_block = re.sub(r' ##.*$', '', yaml_block, flags=re.MULTILINE)
            yaml_block = re.sub(r' ```.*$', '', yaml_block, flags=re.MULTILINE)

            # Reconstruct
            fixed_content = f"---\n{yaml_block}\n---\n\n{body_content}"

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed_content)

        return True
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main():
    vault_root = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')

    corrupted_files = [
        'todo.md',
        '03-Automações/AUTOMATION-CLAUDE-SCHEDULED-TASKS.md',
        '05-Curso-45D/M01-Fundamentos/COURSE-M01-1.3-Papeis-E-Responsabilidades.md',
        '00-Memory/sessions/REFERENCE-SESSION-2026-04-18.md'
    ]

    print("\n🔧 FIXING CORRUPTED YAML FRONTMATTER")
    print("─" * 70)

    fixed = 0
    for filepath_str in corrupted_files:
        filepath = vault_root / filepath_str
        if filepath.exists():
            print(f"\n  Checking: {filepath_str}")
            if fix_corrupted_file(filepath):
                print(f"  ✅ Fixed!")
                fixed += 1
            else:
                print(f"  ⚠️  Not corrupted or skipped")
        else:
            print(f"  ⚠️  File not found: {filepath_str}")

    print(f"\n✅ Fixed {fixed} files")

if __name__ == '__main__':
    main()
