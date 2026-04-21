#!/usr/bin/env python3
"""Auditoria ESTRUTURADA — pastas, ficheiros, padrões de problemas."""

import re
from pathlib import Path
from collections import defaultdict

def analyze_file(filepath):
    """Analyze single file for all issues."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = {
        'fake_wikilinks': len(re.findall(r'\[\[Related-Doc-\d+\]\]', content)),
        'placeholder_context': bool(re.search(r'\[Adiciona contexto', content)),
        'placeholder_items': len(re.findall(r'- \[ \] Item \d+', content)),
        'placeholder_ponto': len(re.findall(r'- Ponto \d+$', content, re.MULTILINE)),
        'empty_por_que': False,
        'malformed_yaml_wikilinks': False,
        'duplicate_lines': 0,
    }
    
    # Check "Por Que" section
    if '## 🎯 Por Que Isto Importa' in content:
        match = re.search(r'## 🎯 Por Que Isto Importa\n\n(.+?)(?=\n---|\n##|$)', content, re.DOTALL)
        if match:
            text = match.group(1).strip()
            if len(text) < 50 or '[Adiciona contexto' in text:
                issues['empty_por_que'] = True
    
    # Check YAML wikilinks
    if content.startswith('---'):
        parts = content.split('---\n', 2)
        if len(parts) >= 2:
            yaml = parts[1]
            if 'wikilinks:' in yaml:
                wl = re.search(r'wikilinks:\s*(.+?)(?=\n[a-z]+:|$)', yaml, re.DOTALL)
                if wl and '\n' in wl.group(1) and not wl.group(1).strip().startswith('['):
                    issues['malformed_yaml_wikilinks'] = True
    
    # Check duplicates
    lines = content.split('\n')
    for i in range(len(lines)-1):
        if lines[i] and lines[i] == lines[i+1] and len(lines[i]) > 20:
            issues['duplicate_lines'] += 1
    
    return issues

def main():
    vault = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')
    
    # Organize by folder
    by_folder = defaultdict(list)
    all_files = {}
    
    for md_file in sorted(vault.rglob('*.md')):
        if any(part.startswith('.') for part in md_file.parts):
            continue
        
        folder = md_file.parent.name
        rel_path = str(md_file.relative_to(vault))
        filename = md_file.name
        
        try:
            issues = analyze_file(md_file)
            by_folder[folder].append({
                'path': rel_path,
                'name': filename,
                'issues': issues,
                'total_issues': sum(1 for v in issues.values() if v and isinstance(v, (int, bool)) and v)
            })
            all_files[rel_path] = issues
        except Exception as e:
            print(f"Error: {rel_path} — {e}")
    
    # Report
    print("\n" + "="*120)
    print("📊 AUDITORIA ESTRUTURADA — VAULT")
    print("="*120)
    
    total_files = len(all_files)
    files_with_issues = sum(1 for f in all_files.values() if any(f.values()))
    
    print(f"\n📁 Estrutura: {len(by_folder)} pastas")
    print(f"📄 Total ficheiros: {total_files}")
    print(f"🔴 Ficheiros com problemas: {files_with_issues} ({files_with_issues*100//total_files}%)")
    
    print("\n" + "="*120)
    print("PASTA A PASTA")
    print("="*120)
    
    for folder in sorted(by_folder.keys()):
        files = by_folder[folder]
        problematic = sum(1 for f in files if f['total_issues'] > 0)
        
        print(f"\n📁 {folder}/ ({len(files)} ficheiros, {problematic} com problemas)")
        print("─" * 120)
        
        for file_info in files:
            issues = file_info['issues']
            if file_info['total_issues'] > 0:
                issue_list = []
                if issues['fake_wikilinks']:
                    issue_list.append(f"{issues['fake_wikilinks']}×fake-wikilinks")
                if issues['placeholder_context']:
                    issue_list.append("placeholder-context")
                if issues['placeholder_items']:
                    issue_list.append(f"{issues['placeholder_items']}×placeholder-items")
                if issues['placeholder_ponto']:
                    issue_list.append(f"{issues['placeholder_ponto']}×placeholder-ponto")
                if issues['empty_por_que']:
                    issue_list.append("empty-por-que")
                if issues['malformed_yaml_wikilinks']:
                    issue_list.append("malformed-yaml")
                if issues['duplicate_lines']:
                    issue_list.append(f"{issues['duplicate_lines']}×duplicates")
                
                print(f"  ❌ {file_info['name']}")
                print(f"     └─ {', '.join(issue_list)}")
    
    # Summary by issue type
    print("\n" + "="*120)
    print("RESUMO POR TIPO DE PROBLEMA")
    print("="*120)
    
    issue_counts = defaultdict(int)
    for issues in all_files.values():
        if issues['fake_wikilinks']:
            issue_counts['fake-wikilinks'] += issues['fake_wikilinks']
        if issues['placeholder_context']:
            issue_counts['placeholder-context'] += 1
        if issues['placeholder_items']:
            issue_counts['placeholder-items'] += issues['placeholder_items']
        if issues['placeholder_ponto']:
            issue_counts['placeholder-ponto'] += issues['placeholder_ponto']
        if issues['empty_por_que']:
            issue_counts['empty-por-que'] += 1
        if issues['malformed_yaml_wikilinks']:
            issue_counts['malformed-yaml'] += 1
        if issues['duplicate_lines']:
            issue_counts['duplicate-lines'] += issues['duplicate_lines']
    
    for issue_type in sorted(issue_counts.keys()):
        count = issue_counts[issue_type]
        print(f"  🔴 {issue_type}: {count}")
    
    print("\n" + "="*120)
    print(f"Estado: {files_with_issues} ficheiros precisam de repair")
    print("="*120 + "\n")

if __name__ == '__main__':
    main()
