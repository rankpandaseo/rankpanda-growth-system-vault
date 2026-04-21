#!/usr/bin/env python3
"""Detailed vault audit — ficheiro a ficheiro, com checklist completo."""

import re
from pathlib import Path
from typing import Dict, List, Tuple

def audit_file(filepath: Path) -> Dict:
    """Audit individual file comprehensively."""
    result = {
        'file': str(filepath.relative_to(Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault'))),
        'checks': {}
    }

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Check YAML frontmatter
        yaml_valid = False
        yaml_block = ""
        if content.startswith('---'):
            parts = content.split('---\n', 2)
            if len(parts) >= 3:
                yaml_valid = True
                yaml_block = parts[1]
        result['checks']['yaml_valid'] = yaml_valid

        # 2. Check required YAML fields
        required_yaml = ['name', 'description', 'type', 'status', 'foco', 'tags', 'wikilinks']
        yaml_fields = {}
        for field in required_yaml:
            match = re.search(rf'^{field}:\s*(.+)$', yaml_block, re.MULTILINE)
            yaml_fields[field] = match is not None
        result['checks']['yaml_fields'] = yaml_fields

        # 3. Check 4 mandatory sections
        body = content.split('---\n', 2)[2] if yaml_valid else content
        sections = {
            'por_que': '## 🎯 Por Que Isto Importa' in body,
            'checklist': '## ⚡ Quick Checklist' in body,
            'conteudo': '## 📖 Conteúdo Principal' in body,
            'relacionados': '## 🔗 Relacionados' in body,
        }
        result['checks']['sections'] = sections

        # 4. Check section content
        content_checks = {}
        if sections['por_que']:
            match = re.search(r'## 🎯 Por Que Isto Importa\n\n(.*?)(?=\n---|\n## |\Z)', body, re.DOTALL)
            text = match.group(1).strip() if match else ""
            content_checks['por_que'] = {'has_content': len(text) > 20, 'length': len(text)}

        if sections['checklist']:
            match = re.search(r'## ⚡ Quick Checklist\n\n(.*?)(?=\n---|\n## |\Z)', body, re.DOTALL)
            text = match.group(1).strip() if match else ""
            content_checks['checklist'] = {'has_content': len(text) > 5, 'length': len(text)}

        if sections['conteudo']:
            match = re.search(r'## 📖 Conteúdo Principal\n\n(.*?)(?=\n---|\n## |\Z)', body, re.DOTALL)
            text = match.group(1).strip() if match else ""
            is_placeholder = text in ['[Conteúdo principal aqui]', '[main content here]', '[content here]', ''] or len(text) < 30
            content_checks['conteudo'] = {'has_content': len(text) > 50, 'is_placeholder': is_placeholder, 'length': len(text)}

        if sections['relacionados']:
            match = re.search(r'## 🔗 Relacionados\n\n(.*?)(?=\n---|\Z)', body, re.DOTALL)
            text = match.group(1).strip() if match else ""
            wikilinks = len(re.findall(r'\[\[', text))
            content_checks['relacionados'] = {'has_wikilinks': wikilinks > 0, 'count': wikilinks}

        result['checks']['section_content'] = content_checks

        # 5. Check overall completeness
        all_fields_ok = all(yaml_fields.values())
        all_sections_ok = all(sections.values())
        result['checks']['completeness'] = {
            'all_yaml_fields': all_fields_ok,
            'all_sections': all_sections_ok,
            'is_complete': all_fields_ok and all_sections_ok and content_checks.get('conteudo', {}).get('has_content', False)
        }

        result['status'] = 'OK' if result['checks']['completeness']['is_complete'] else 'ISSUE'

    except Exception as e:
        result['status'] = 'ERROR'
        result['error'] = str(e)

    return result

def main():
    vault_root = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')

    # Get all markdown files organized by folder
    files_by_folder = {}
    for md_file in sorted(vault_root.rglob('*.md')):
        if any(part.startswith('.') for part in md_file.parts):
            continue

        folder = md_file.parent.name
        if folder not in files_by_folder:
            files_by_folder[folder] = []
        files_by_folder[folder].append(md_file)

    # Audit all files
    all_results = {}
    for folder in sorted(files_by_folder.keys()):
        all_results[folder] = []
        for filepath in sorted(files_by_folder[folder]):
            result = audit_file(filepath)
            all_results[folder].append(result)

    # Print detailed report
    print("\n" + "=" * 100)
    print("📋 DETAILED VAULT AUDIT — FICHEIRO A FICHEIRO")
    print("=" * 100)

    total_files = 0
    total_ok = 0
    total_issues = 0

    for folder in sorted(all_results.keys()):
        print(f"\n📁 {folder}/")
        print("─" * 100)

        for result in all_results[folder]:
            total_files += 1
            filename = result['file'].split('/')[-1]

            if result['status'] == 'ERROR':
                print(f"  ❌ {filename}")
                print(f"     ERROR: {result.get('error', 'Unknown')}")
                total_issues += 1
            elif result['status'] == 'OK':
                print(f"  ✅ {filename}")
                total_ok += 1
            else:
                print(f"  ⚠️  {filename}")
                total_issues += 1

                # Detail what's missing
                checks = result['checks']
                if not checks.get('yaml_valid'):
                    print(f"     ❌ YAML frontmatter invalid")
                else:
                    missing_fields = [k for k, v in checks.get('yaml_fields', {}).items() if not v]
                    if missing_fields:
                        print(f"     ❌ Missing YAML fields: {', '.join(missing_fields)}")

                missing_sections = [k for k, v in checks.get('sections', {}).items() if not v]
                if missing_sections:
                    section_names = {
                        'por_que': 'Por Que Isto Importa',
                        'checklist': 'Quick Checklist',
                        'conteudo': 'Conteúdo Principal',
                        'relacionados': 'Relacionados'
                    }
                    print(f"     ❌ Missing sections: {', '.join([section_names.get(s, s) for s in missing_sections])}")

                section_content = checks.get('section_content', {})
                if section_content.get('conteudo', {}).get('is_placeholder'):
                    print(f"     ⚠️  Conteúdo Principal: only placeholder text ({section_content['conteudo']['length']} chars)")

    # Summary
    print("\n" + "=" * 100)
    print("📊 SUMMARY")
    print("=" * 100)
    print(f"\nTotal files: {total_files}")
    print(f"  ✅ OK: {total_ok}")
    print(f"  ⚠️  Issues: {total_issues}")
    print(f"  Compliance: {(total_ok/total_files*100):.1f}%")

    if total_issues == 0:
        print(f"\n🎉 VAULT IS 100% COMPLIANT!")
    else:
        print(f"\n⚠️  {total_issues} ficheiros need attention")

if __name__ == '__main__':
    main()
