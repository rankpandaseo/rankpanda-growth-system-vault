#!/usr/bin/env python3
"""Audit entire vault for placeholder content and insufficient content."""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def extract_content_section(filepath: Path) -> Tuple[str, int]:
    """Extract content section from file and return (content, length)."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by frontmatter
        if not content.startswith('---'):
            return "", 0

        # Find end of frontmatter
        parts = content.split('---\n', 2)
        if len(parts) < 3:
            return "", 0

        body = parts[2]

        # Look for Conteúdo Principal section
        content_match = re.search(r'## 📖 Conteúdo Principal\n\n(.*?)(?=\n---|\n## |\Z)', body, re.DOTALL)
        if content_match:
            text = content_match.group(1).strip()
            return text, len(text)

        # Fallback: look for any main content area
        # Remove headers and checklist
        lines = body.split('\n')
        content_lines = []
        skip_section = False

        for line in lines:
            if line.startswith('##') or line.startswith('---'):
                skip_section = True
                continue
            if skip_section and line.startswith('## '):
                skip_section = False
            if not skip_section and line.strip():
                content_lines.append(line)

        text = '\n'.join(content_lines).strip()
        return text, len(text)

    except Exception as e:
        return "", 0

def is_placeholder(text: str) -> bool:
    """Check if text is placeholder."""
    placeholders = [
        '[Escreve conteúdo aqui]',
        '[...]',
        '[Conteúdo aqui]',
        '[content]',
        'Escreve conteúdo',
        'TODO:',
        'FIXME:',
    ]

    text_lower = text.lower()
    return any(p.lower() in text_lower for p in placeholders)

def audit_vault():
    """Audit entire vault for placeholder content."""
    vault_root = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')

    results = {
        'total_files': 0,
        'files_with_placeholders': [],
        'files_with_short_content': [],
        'by_type': {},
        'issues_summary': {}
    }

    # Find all markdown files
    md_files = sorted(vault_root.rglob('*.md'))

    for md_file in md_files:
        # Skip system files
        if any(part.startswith('.') for part in md_file.parts):
            continue

        results['total_files'] += 1

        # Extract content
        content_text, content_len = extract_content_section(md_file)
        filename = md_file.name
        rel_path = md_file.relative_to(vault_root)

        # Get file type from YAML
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                yaml_block = f.read().split('---\n')[1]
                type_match = re.search(r'type: (\w+)', yaml_block)
                file_type = type_match.group(1) if type_match else 'unknown'
        except:
            file_type = 'unknown'

        # Track by type
        if file_type not in results['by_type']:
            results['by_type'][file_type] = {'total': 0, 'with_issues': 0}
        results['by_type'][file_type]['total'] += 1

        # Check for issues
        has_placeholder = is_placeholder(content_text)
        is_short = content_len < 50 and content_len > 0
        is_empty = content_len == 0

        if has_placeholder:
            results['files_with_placeholders'].append({
                'file': str(rel_path),
                'type': file_type,
                'length': content_len,
                'preview': content_text[:80] if content_text else "[Empty]"
            })
            results['by_type'][file_type]['with_issues'] += 1

        if is_short or is_empty:
            results['files_with_short_content'].append({
                'file': str(rel_path),
                'type': file_type,
                'length': content_len,
                'status': 'empty' if is_empty else 'too_short',
                'preview': content_text[:80] if content_text else "[Empty]"
            })
            if not has_placeholder:  # Don't double count
                results['by_type'][file_type]['with_issues'] += 1

    return results

def main():
    print("\n" + "=" * 70)
    print("🔍 VAULT CONTENT AUDIT — Placeholder & Insufficient Content")
    print("=" * 70)

    audit = audit_vault()

    print(f"\n📊 SUMMARY")
    print(f"─" * 70)
    print(f"Total files scanned: {audit['total_files']}")
    print(f"Files with placeholder content: {len(audit['files_with_placeholders'])}")
    print(f"Files with short/empty content: {len(audit['files_with_short_content'])}")

    print(f"\n📈 BY FILE TYPE:")
    print(f"─" * 70)
    for ftype, stats in sorted(audit['by_type'].items()):
        pct = (stats['with_issues'] / stats['total'] * 100) if stats['total'] > 0 else 0
        print(f"  {ftype:12} — {stats['total']:2} files, {stats['with_issues']:2} with issues ({pct:5.1f}%)")

    # Show placeholders
    if audit['files_with_placeholders']:
        print(f"\n⚠️  FILES WITH PLACEHOLDER TEXT ({len(audit['files_with_placeholders'])}):")
        print(f"─" * 70)
        for issue in sorted(audit['files_with_placeholders'], key=lambda x: x['file']):
            print(f"\n  {issue['file']}")
            print(f"    Type: {issue['type']}")
            print(f"    Length: {issue['length']} chars")
            print(f"    Preview: {issue['preview'][:60]}...")

    # Show short content
    if audit['files_with_short_content']:
        print(f"\n⚠️  FILES WITH SHORT/EMPTY CONTENT ({len(audit['files_with_short_content'])}):")
        print(f"─" * 70)
        for issue in sorted(audit['files_with_short_content'], key=lambda x: x['file']):
            status_emoji = "❌" if issue['status'] == 'empty' else "⚠️"
            print(f"\n  {status_emoji} {issue['file']}")
            print(f"    Type: {issue['type']}")
            print(f"    Length: {issue['length']} chars")
            if issue['length'] > 0:
                print(f"    Preview: {issue['preview'][:60]}...")
            else:
                print(f"    Status: [EMPTY]")

if __name__ == '__main__':
    main()
