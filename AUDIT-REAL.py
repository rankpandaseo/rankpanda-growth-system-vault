#!/usr/bin/env python3
"""Auditoria REAL — placeholders, malformed YAML, duplicates."""

import re
from pathlib import Path

def audit_quality(filepath):
    """Audit real quality, not just structure."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 1. Check for placeholders in critical sections
    placeholders = [
        r'\[Adiciona contexto[^\]]*\]',
        r'- \[ \] Item [0-9]',
        r'\[\[Related-Doc-[0-9]\]\]',
        r'descrição\|$',  # Generic descrição on its own line
        r'\[content here\]',
        r'\[main content\]',
        r'- Ponto [0-9]$',  # Generic "Ponto 1/2/3"
    ]
    
    for placeholder in placeholders:
        if re.search(placeholder, content, re.MULTILINE):
            issues.append(f"placeholder: {placeholder}")
    
    # 2. Check YAML section structure
    if content.startswith('---'):
        parts = content.split('---\n', 2)
        if len(parts) >= 2:
            yaml_block = parts[1]
            # Check if wikilinks spans multiple lines (malformed)
            if 'wikilinks:' in yaml_block:
                wikilinks_match = re.search(r'wikilinks:\s*(.+?)(?=\n[a-z]+:|$)', yaml_block, re.DOTALL)
                if wikilinks_match:
                    wl_value = wikilinks_match.group(1)
                    if '\n' in wl_value and not wl_value.strip().startswith('['):
                        issues.append("yaml_wikilinks_multiline")
    
    # 3. Check for duplicated text
    lines = content.split('\n')
    for i in range(len(lines)-1):
        if lines[i] and lines[i] == lines[i+1] and len(lines[i]) > 20:
            issues.append(f"duplicate_line: {lines[i][:50]}")
    
    # 4. Check section content quality
    if '## 🎯 Por Que Isto Importa' in content:
        match = re.search(r'## 🎯 Por Que Isto Importa\n\n(.+?)(?=\n---|\n##|$)', content, re.DOTALL)
        if match:
            text = match.group(1).strip()
            if '[Adiciona contexto' in text or len(text) < 50:
                issues.append("por_que_placeholder_or_short")
    
    # 5. Check for "Relacionados" with fake links
    if '## 🔗 Relacionados' in content:
        match = re.search(r'## 🔗 Relacionados\n\n(.+?)$', content, re.DOTALL)
        if match:
            related_text = match.group(1).strip()
            fake_links = re.findall(r'\[\[Related-Doc-\d+\]\]', related_text)
            if fake_links:
                issues.append(f"fake_wikilinks: {len(fake_links)} Related-Doc placeholders")
    
    return issues

def main():
    vault = Path('/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault')
    
    files_with_issues = {}
    for md_file in sorted(vault.rglob('*.md')):
        if any(part.startswith('.') for part in md_file.parts):
            continue
        
        try:
            issues = audit_quality(md_file)
            if issues:
                rel_path = str(md_file.relative_to(vault))
                files_with_issues[rel_path] = issues
        except Exception as e:
            pass
    
    print("\n" + "="*100)
    print("⚠️  AUDITORIA REAL — Ficheiros com Problemas DE QUALIDADE")
    print("="*100)
    
    if not files_with_issues:
        print("\n✅ Nenhum problema encontrado")
    else:
        print(f"\n🔴 {len(files_with_issues)} ficheiros com problemas:\n")
        for filepath in sorted(files_with_issues.keys()):
            issues = files_with_issues[filepath]
            print(f"  ❌ {filepath}")
            for issue in issues:
                print(f"     - {issue}")
    
    print("\n" + "="*100)
    print(f"Total de ficheiros com problemas: {len(files_with_issues)}")
    print("="*100)

if __name__ == '__main__':
    main()
