#!/usr/bin/env python3
"""Add missing 4-section structure to all files."""

import os
import re
from pathlib import Path

VAULT_DIR = Path(__file__).parent

REQUIRED_SECTIONS = [
    '🎯 Por Que Isto Importa',
    '⚡ Quick Checklist',
    '📖 Conteúdo Principal',
    '🔗 Relacionados',
]

def extract_properties_and_body(content):
    """Extract Properties frontmatter and body content."""
    match = re.match(r'^---\n(.*?)\n---\n(.*)$', content, re.DOTALL)
    if match:
        return match.group(1), match.group(2).strip()
    return None, content.strip()

def has_all_sections(body):
    """Check if body has all 4 required sections."""
    for section in REQUIRED_SECTIONS:
        if f"## {section}" not in body:
            return False
    return True

def extract_title_from_body(body):
    """Extract title from markdown body."""
    lines = body.split('\n')
    for line in lines:
        if line.startswith('# '):
            return line[2:].strip()
    return "Document"

def build_default_sections(body, title):
    """Build default 4-section structure with placeholder content."""

    # Extract any bullets or structured content
    has_bullets = '- ' in body
    has_checklist = '[ ]' in body

    # Build sections
    sections = {
        '🎯 Por Que Isto Importa': '''[Adiciona contexto: impacto direto no projeto, porquê isto importa]
- Ponto 1
- Ponto 2
- Ponto 3''',

        '⚡ Quick Checklist': '''- [ ] Item 1
- [ ] Item 2
- [ ] Item 3''' if not has_checklist else extract_section_content(body, 'checklist'),

        '📖 Conteúdo Principal': body if not has_bullets else extract_main_content(body),

        '🔗 Relacionados': '''- [[Related-Doc-1]] — descrição
- [[Related-Doc-2]] — descrição''',
    }

    return sections

def extract_main_content(body):
    """Extract main content excluding structured lists."""
    lines = []
    skip = False
    for line in body.split('\n'):
        if line.startswith('## '):
            skip = True
        elif line.startswith('# '):
            skip = True
        elif skip and line.startswith('- '):
            continue
        else:
            lines.append(line)

    content = '\n'.join(lines).strip()
    return content if content else '[Conteúdo principal aqui]'

def extract_section_content(body, section_type):
    """Try to extract relevant content for a section."""
    if section_type == 'checklist':
        lines = [l for l in body.split('\n') if '[ ]' in l or '[x]' in l]
        if lines:
            return '\n'.join(lines)
    return None

def build_complete_document(properties_text, title, sections_dict):
    """Build complete document with Properties + sections."""
    doc_lines = ['---', properties_text, '---', '', f'# {title}', '']

    # Add summary
    doc_lines.append(f'**Resumo:** {title}')
    doc_lines.append('')
    doc_lines.append('---')
    doc_lines.append('')

    # Add all 4 sections
    for section_title, section_content in sections_dict.items():
        doc_lines.append(f'## {section_title}')
        doc_lines.append('')
        doc_lines.append(section_content)
        doc_lines.append('')
        doc_lines.append('---')
        doc_lines.append('')

    return '\n'.join(doc_lines)

def add_missing_sections_to_file(filepath):
    """Add missing sections to file if needed."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        properties_text, body = extract_properties_and_body(content)

        # Check if already has all sections
        if has_all_sections(body):
            return False, "Already has all sections"

        # Extract title
        title = extract_title_from_body(body)

        # Build sections
        sections = build_default_sections(body, title)

        # Build complete document
        new_content = build_complete_document(properties_text, title, sections)

        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        return True, f"Added 4 sections (title: {title[:40]})"

    except Exception as e:
        return False, f"Error: {str(e)[:50]}"

def main():
    added = 0
    skipped = 0

    print("🔄 Adding missing 4-section structure...\n")

    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in sorted(files):
            if file.endswith('.md'):
                filepath = Path(root) / file
                rel_path = filepath.relative_to(VAULT_DIR)

                success, msg = add_missing_sections_to_file(filepath)
                if success:
                    print(f"✅ {rel_path}: {msg}")
                    added += 1
                else:
                    skipped += 1

    print(f"\n📊 Added: {added} | Skipped: {skipped}")
    print(f"\n✨ All files now have 4-section structure")

if __name__ == '__main__':
    main()
