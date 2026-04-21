#!/usr/bin/env python3
"""Audit vault content quality — identifies which files need actual content work."""

import re
from pathlib import Path
from typing import Dict, List

def extract_content_section(filepath: Path) -> tuple:
    """Extract main content section and context."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if not content.startswith('---'):
            return "", 0, "unknown"

        parts = content.split('---\n', 2)
        if len(parts) < 3:
            return "", 0, "unknown"

        # Get file type from YAML
        yaml_block = parts[1]
        type_match = re.search(r'type: (\w+)', yaml_block)
        file_type = type_match.group(1) if type_match else 'unknown'

        body = parts[2]

        # Extract Conteúdo Principal section
        content_match = re.search(
            r'## 📖 Conteúdo Principal\n\n(.*?)(?=\n---|\n## |\Z)',
            body,
            re.DOTALL
        )

        if content_match:
            text = content_match.group(1).strip()
            return text, len(text), file_type

        return "", 0, file_type

    except Exception as e:
        return "", 0, "error"

def categorize_issue(filepath_name: str, content: str, length: int, file_type: str) -> Dict:
    """Categorize the nature of the content issue."""

    # Pure placeholders: [something]
    if re.match(r'^\[.+\]$', content.strip()):
        return {
            'severity': 'CRITICAL',
            'category': 'empty_placeholder',
            'reason': 'Only placeholder text, no actual content'
        }

    # Documentation/example files (these are meta-documents showing HOW to fill placeholders)
    if 'VAULT' in filepath_name.upper() or 'ROADMAP' in filepath_name.upper():
        if content and len(content) > 100:
            return {
                'severity': 'OK',
                'category': 'documentation',
                'reason': 'This is a documentation file explaining structure — content is fine'
            }
        elif '[⬅️' in content or '...]:' in content:
            return {
                'severity': 'OK',
                'category': 'documentation',
                'reason': 'This is a documentation file showing examples — acceptable'
            }

    # Reference/Memory files that are legitimately short indices
    if file_type == 'reference' and 'reference' in filepath_name.lower():
        if length < 50:
            return {
                'severity': 'WARN',
                'category': 'short_index',
                'reason': 'Reference/index file — acceptable if it\'s a summary index'
            }

    # Actual content files with insufficient content
    if length < 50 and length > 0:
        return {
            'severity': 'HIGH',
            'category': 'insufficient_content',
            'reason': f'Content is too short ({length} chars, need >50 for operational docs)'
        }

    if length == 0:
        return {
            'severity': 'CRITICAL',
            'category': 'missing_content',
            'reason': 'No content section found'
        }

    return {
        'severity': 'OK',
        'category': 'complete',
        'reason': 'Content looks adequate'
    }

def main():
    vault_root = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')

    critical = []  # Blocking issues
    high = []      # Should fix soon
    warn = []      # Monitor
    ok = []        # No action needed

    # Scan all markdown files
    for md_file in sorted(vault_root.rglob('*.md')):
        if any(part.startswith('.') for part in md_file.parts):
            continue

        rel_path = str(md_file.relative_to(vault_root))
        content, length, file_type = extract_content_section(md_file)

        issue = categorize_issue(md_file.name, content, length, file_type)

        record = {
            'file': rel_path,
            'type': file_type,
            'length': length,
            'issue': issue
        }

        if issue['severity'] == 'CRITICAL':
            critical.append(record)
        elif issue['severity'] == 'HIGH':
            high.append(record)
        elif issue['severity'] == 'WARN':
            warn.append(record)
        else:
            ok.append(record)

    # Print report
    print("\n" + "=" * 80)
    print("📊 VAULT CONTENT QUALITY AUDIT")
    print("=" * 80)

    total = len(critical) + len(high) + len(warn) + len(ok)
    print(f"\nTotal files scanned: {total}")
    print(f"  🔴 CRITICAL (blocking): {len(critical)}")
    print(f"  🔶 HIGH (should fix): {len(high)}")
    print(f"  🟡 WARN (monitor): {len(warn)}")
    print(f"  🟢 OK: {len(ok)}")

    if critical:
        print(f"\n🔴 CRITICAL FILES ({len(critical)}) — MUST FIX:")
        print("─" * 80)
        for rec in critical:
            print(f"\n  {rec['file']}")
            print(f"    Type: {rec['type']}")
            print(f"    Content length: {rec['length']} chars")
            print(f"    Issue: {rec['issue']['reason']}")

    if high:
        print(f"\n🔶 HIGH PRIORITY ({len(high)}) — SHOULD FIX SOON:")
        print("─" * 80)
        for rec in high:
            print(f"\n  {rec['file']}")
            print(f"    Type: {rec['type']}")
            print(f"    Content length: {rec['length']} chars")
            print(f"    Issue: {rec['issue']['reason']}")

    if warn:
        print(f"\n🟡 WARNINGS ({len(warn)}) — REVIEW:")
        print("─" * 80)
        for rec in warn:
            print(f"\n  {rec['file']}")
            print(f"    Type: {rec['type']}")
            print(f"    Content length: {rec['length']} chars")
            print(f"    Issue: {rec['issue']['reason']}")

    # Summary
    print(f"\n" + "=" * 80)
    print("📋 SUMMARY & ACTION PLAN")
    print("=" * 80)

    if critical:
        print(f"\n✅ ACTION (Priority P0 — Blocking):")
        print(f"   Edit these {len(critical)} critical files and add substantive content:")
        for rec in critical:
            print(f"   - {rec['file']}")
        print(f"\n   Why: Agents cannot read empty documents. This is blocking.")

    if high:
        print(f"\n✅ ACTION (Priority P1 — Should Fix):")
        print(f"   Review and expand these {len(high)} files to have >50 chars of content:")
        for rec in high:
            print(f"   - {rec['file']} ({rec['length']} chars)")
        print(f"\n   Why: These documents are incomplete per SOP standards.")

    if warn:
        print(f"\n✅ ACTION (Priority P2 — Monitor):")
        print(f"   These {len(warn)} files are acceptable but keep an eye on them:")
        for rec in warn:
            print(f"   - {rec['file']}")

    print(f"\n🎯 NEXT STEP:")
    if critical or high:
        print(f"   Open each file and fill in the 'Conteúdo Principal' section with real content.")
        print(f"   Minimum: >50 characters of substantive text (not placeholder).")
    else:
        print(f"   ✅ Vault content is in good shape! All files have adequate content.")

if __name__ == '__main__':
    main()
