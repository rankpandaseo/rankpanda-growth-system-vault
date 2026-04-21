#!/usr/bin/env python3
"""Create a new vault document with correct YAML frontmatter and structure."""

import sys
import argparse
from pathlib import Path
from vault_parser import VaultParser

VALID_TYPES = ['sop', 'fase', 'conceito', 'template', 'reference', 'automation', 'course', 'skill', 'api']
VALID_STATUS = ['draft', 'ready', 'active']
VALID_FOCO = ['seo', 'technical', 'operational', 'course']

TEMPLATE = '''---
name: {filename}
description: {description}
type: {type}
status: draft
foco: {foco}
tags: []
wikilinks: []
---

# {title}

**Resumo:** {description}

---

## 🎯 Por Que Isto Importa

[Adiciona contexto: impacto direto no projeto, porquê isto importa]

---

## ⚡ Quick Checklist

- [ ] Passo 1
- [ ] Passo 2
- [ ] Passo 3

---

## 📖 Conteúdo Principal

[Escreve conteúdo aqui]

---

## 🔗 Relacionados

- [[related-doc-1]] — descrição
- [[related-doc-2]] — descrição
'''

def kebab_to_camel(text):
    """Convert kebab-case to CamelCase."""
    parts = text.split('-')
    return ''.join(word.capitalize() for word in parts)

def find_related_documents(vault, doc_type, foco, limit=3):
    """Find related documents by type and foco for wikilinks suggestions."""
    candidates = []

    # Find documents of same type or complementary types
    type_relations = {
        'sop': ['fase', 'conceito', 'template'],
        'fase': ['sop', 'conceito'],
        'conceito': ['sop', 'fase', 'reference'],
        'template': ['sop', 'automation'],
        'reference': ['sop', 'conceito'],
        'automation': ['template', 'reference'],
        'course': ['sop', 'fase'],
    }

    related_types = type_relations.get(doc_type, ['sop', 'reference'])

    # Find documents with same foco or operational
    for related_type in related_types:
        docs = vault.find_by_type(related_type)
        for doc in docs:
            if doc.foco() == foco or doc.foco() == 'operational':
                candidates.append(doc)

    # Sort by type priority and return top N
    candidates = candidates[:limit]
    return [(doc.name(), doc.title) for doc in candidates]

def validate_created_document(filepath):
    """Validate newly created document."""
    from vault_parser import VaultDocumentParser

    try:
        doc = VaultDocumentParser(str(filepath))
        if doc.is_complete():
            return True, "✅ Document is complete and valid"
        else:
            missing = []
            if not doc.why():
                missing.append("'Por Que Isto Importa' section")
            if not doc.checklist():
                missing.append("'Quick Checklist' items")
            if not doc.content():
                missing.append("'Conteúdo Principal' section")
            if not doc.related():
                missing.append("'Relacionados' links")
            return False, f"⚠️ Document incomplete. Missing: {', '.join(missing)}"
    except Exception as e:
        return False, f"❌ Validation error: {e}"

def create_document(doc_type, name, description, foco, vault_root, validate=True, auto_suggest=False):
    """Create a new document with correct filename and frontmatter."""

    if doc_type not in VALID_TYPES:
        print(f"❌ Invalid type. Choose from: {', '.join(VALID_TYPES)}")
        sys.exit(1)

    if foco not in VALID_FOCO:
        print(f"❌ Invalid foco. Choose from: {', '.join(VALID_FOCO)}")
        sys.exit(1)

    # Convert name to filename format
    filename_slug = name.lower().replace(' ', '-')
    filename = f"{doc_type.upper()}-{kebab_to_camel(filename_slug)}.md"
    title = name

    # Determine directory based on type
    type_dirs = {
        'sop': '02-SOPs',
        'fase': '02-SOPs',
        'conceito': '02-SOPs',
        'template': '04-Templates',
        'reference': '00-Memory',
        'automation': '03-Automações',
        'course': '05-Curso-45D',
        'skill': '04-Templates',
        'api': '04-Templates',
    }

    target_dir = Path(vault_root) / type_dirs[doc_type]
    target_file = target_dir / filename

    if target_file.exists():
        print(f"❌ File already exists: {target_file}")
        sys.exit(1)

    # Generate wikilinks suggestions if requested
    wikilinks = '[]'
    if auto_suggest:
        try:
            vault = VaultParser(str(Path(vault_root)))
            vault.load_all()
            related = find_related_documents(vault, doc_type, foco, limit=3)
            if related:
                wikilink_list = ', '.join([f'[[{doc[0]}]]' for doc in related])
                wikilinks = f'[{wikilink_list}]'
        except Exception as e:
            print(f"⚠️ Could not auto-suggest wikilinks: {e}")

    # Generate content with wikilinks
    template_content = TEMPLATE.replace('wikilinks: []', f'wikilinks: {wikilinks}')
    content = template_content.format(
        filename=filename_slug,
        description=description,
        type=doc_type,
        foco=foco,
        title=title
    )

    # Write file
    target_file.parent.mkdir(parents=True, exist_ok=True)
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Created: {target_file.relative_to(target_dir.parent.parent.parent)}")

    # Validate if requested
    if validate:
        success, msg = validate_created_document(target_file)
        print(f"{msg}")
        if not success:
            print(f"📝 Complete the missing sections before committing")
    else:
        print(f"📝 Edit and commit when ready")

def main():
    parser = argparse.ArgumentParser(description='Create a new vault document')
    parser.add_argument('--type', required=True, help=f'Document type: {", ".join(VALID_TYPES)}')
    parser.add_argument('--name', required=True, help='Document name (e.g., "Store Context Setup")')
    parser.add_argument('--description', required=True, help='One-line description (80 chars max)')
    parser.add_argument('--foco', required=True, help=f'Focus area: {", ".join(VALID_FOCO)}')
    parser.add_argument('--vault-root', default='/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault', help='Vault root directory')
    parser.add_argument('--validate', action='store_true', default=True, help='Validate document on creation (default: True)')
    parser.add_argument('--no-validate', dest='validate', action='store_false', help='Skip validation')
    parser.add_argument('--auto-suggest', action='store_true', help='Auto-suggest related wikilinks')

    args = parser.parse_args()

    create_document(args.type, args.name, args.description, args.foco, args.vault_root,
                    validate=args.validate, auto_suggest=args.auto_suggest)

if __name__ == '__main__':
    main()
