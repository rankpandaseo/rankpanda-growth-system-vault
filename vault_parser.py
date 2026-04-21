#!/usr/bin/env python3
"""VaultDocumentParser — Agent-friendly vault document reading interface."""

import re
from pathlib import Path
from typing import List, Dict, Optional, Tuple

class VaultDocumentParser:
    """Parse and extract data from standardized vault documents."""

    def __init__(self, filepath: str):
        """Initialize parser with a vault document path."""
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"Document not found: {filepath}")

        with open(self.filepath, 'r', encoding='utf-8') as f:
            self._raw_content = f.read()

        # Extract frontmatter and body
        self.properties, self.body = self._extract_frontmatter_and_body()
        self.title = self._extract_title()

    def _extract_frontmatter_and_body(self) -> Tuple[Dict, str]:
        """Extract Properties YAML and body content."""
        match = re.match(r'^---\n(.*?)\n---\n', self._raw_content, re.DOTALL)
        if not match:
            return {}, self._raw_content

        yaml_content = match.group(1)
        body = self._raw_content[match.end():]

        # Parse YAML properties
        properties = {}
        for line in yaml_content.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                properties[key.strip()] = value.strip()

        return properties, body.strip()

    def _extract_title(self) -> str:
        """Extract H1 title from body."""
        match = re.search(r'^# (.+?)$', self.body, re.MULTILINE)
        return match.group(1) if match else "Untitled"

    def _extract_section(self, section_name: str) -> str:
        """Extract content between section heading and next heading or end."""
        pattern = rf'^## {re.escape(section_name)}\n\n(.*?)(?=\n---\n|$)'
        match = re.search(pattern, self.body, re.DOTALL | re.MULTILINE)
        if not match:
            return ""
        return match.group(1).strip()

    def _extract_checklist_items(self, text: str) -> List[str]:
        """Extract checkbox items from text."""
        items = []
        for match in re.finditer(r'- \[ \] (.+?)(?:\n|$)', text):
            items.append(match.group(1).strip())
        return items

    def _extract_bullets(self, text: str) -> List[str]:
        """Extract bullet points from text."""
        bullets = []
        for match in re.finditer(r'^- (.+?)$', text, re.MULTILINE):
            bullets.append(match.group(1).strip())
        return bullets

    # ===== PROPERTIES ACCESSORS =====

    def name(self) -> str:
        """Return document name (kebab-case ID)."""
        return self.properties.get('name', 'unnamed')

    def description(self) -> str:
        """Return document description."""
        return self.properties.get('description', '')

    def type(self) -> str:
        """Return document type (sop, fase, template, course, reference, automation, etc)."""
        return self.properties.get('type', 'reference')

    def status(self) -> str:
        """Return document status (draft, ready, active)."""
        return self.properties.get('status', 'draft')

    def foco(self) -> str:
        """Return document focus area (seo, technical, operational, course)."""
        return self.properties.get('foco', 'operational')

    def tags(self) -> List[str]:
        """Return document tags."""
        tags_str = self.properties.get('tags', '[]')
        # Parse YAML list format: [tag1, tag2, tag3]
        tags_str = tags_str.strip('[]')
        if not tags_str:
            return []
        return [t.strip() for t in tags_str.split(',')]

    def wikilinks_property(self) -> List[str]:
        """Return wikilinks from Properties."""
        links_str = self.properties.get('wikilinks', '[]')
        links_str = links_str.strip('[]')
        if not links_str:
            return []
        # Extract from [[link1]], [[link2]] format
        return re.findall(r'\[\[([^\]]+)\]\]', links_str)

    # ===== SECTION ACCESSORS =====

    def why(self) -> str:
        """Extract 'Por Que Isto Importa' section."""
        return self._extract_section('🎯 Por Que Isto Importa')

    def checklist(self) -> List[str]:
        """Extract checklist items from 'Quick Checklist' section."""
        section = self._extract_section('⚡ Quick Checklist')
        return self._extract_checklist_items(section)

    def content(self) -> str:
        """Extract main content from 'Conteúdo Principal' section."""
        return self._extract_section('📖 Conteúdo Principal')

    def related(self) -> List[Tuple[str, str]]:
        """Extract related documents and descriptions.

        Returns: List of (wikilink, description) tuples
        """
        section = self._extract_section('🔗 Relacionados')
        related_docs = []

        for match in re.finditer(r'\[\[([^\]]+)\]\]\s*—\s*(.+?)(?:\n|$)', section):
            wikilink = match.group(1).strip()
            description = match.group(2).strip()
            related_docs.append((wikilink, description))

        return related_docs

    # ===== WIKILINK ACCESSORS =====

    def wikilinks(self) -> List[str]:
        """Extract all wikilinks from body content."""
        return re.findall(r'\[\[([^\]]+)\]\]', self.body)

    def wikilinks_all(self) -> List[str]:
        """Extract all wikilinks (Properties + body)."""
        props_links = self.wikilinks_property()
        body_links = self.wikilinks()
        # Remove duplicates while preserving order
        seen = set()
        result = []
        for link in props_links + body_links:
            if link not in seen:
                seen.add(link)
                result.append(link)
        return result

    def resolve_wikilinks(self, vault_root: Optional[Path] = None) -> Dict[str, Optional[Path]]:
        """Resolve wikilinks to actual file paths.

        Args:
            vault_root: Root directory of vault. If None, uses parent of this file.

        Returns:
            Dict mapping wikilink name → filepath (or None if not found)
        """
        if vault_root is None:
            vault_root = self.filepath.parent

        resolved = {}
        for wikilink in self.wikilinks_all():
            # Search for file matching wikilink name (case-insensitive)
            found = None
            for md_file in vault_root.rglob('*.md'):
                # Check if filename (without extension) matches wikilink
                filename_without_ext = md_file.stem.lower()
                wikilink_lower = wikilink.lower().replace(' ', '-')

                if filename_without_ext == wikilink_lower:
                    found = md_file
                    break

                # Also try exact name match
                if wikilink in md_file.name:
                    found = md_file
                    break

            resolved[wikilink] = found

        return resolved

    # ===== UTILITY METHODS =====

    def summary(self) -> Dict:
        """Return complete document summary."""
        return {
            'filepath': str(self.filepath),
            'name': self.name(),
            'title': self.title,
            'description': self.description(),
            'type': self.type(),
            'status': self.status(),
            'foco': self.foco(),
            'tags': self.tags(),
            'sections': {
                'why': len(self.why()) > 0,
                'checklist': len(self.checklist()) > 0,
                'content': len(self.content()) > 0,
                'related': len(self.related()) > 0,
            },
            'checklist_items': len(self.checklist()),
            'wikilinks': len(self.wikilinks()),
        }

    def is_complete(self) -> bool:
        """Check if document has all required sections and properties."""
        required_properties = ['name', 'description', 'type', 'status', 'foco']
        has_all_props = all(prop in self.properties for prop in required_properties)

        has_all_sections = all([
            len(self.why()) > 0,
            len(self.checklist()) > 0,
            len(self.content()) > 0,
            len(self.related()) > 0,
        ])

        return has_all_props and has_all_sections

    def __str__(self) -> str:
        """Return string representation."""
        return f"VaultDoc({self.name()} | {self.type()} | {self.status()})"

    def __repr__(self) -> str:
        """Return detailed representation."""
        return f"VaultDocumentParser('{self.filepath}')"


# ===== VAULT COLLECTION PARSER =====

class VaultParser:
    """Parse entire vault and provide collection-level operations."""

    def __init__(self, vault_root: str):
        """Initialize vault parser with root directory."""
        self.vault_root = Path(vault_root)
        self.documents = {}

    def load_all(self):
        """Load and parse all markdown documents in vault."""
        for md_file in self.vault_root.rglob('*.md'):
            # Skip generated files and system directories
            if any(part.startswith('.') for part in md_file.parts):
                continue

            try:
                doc = VaultDocumentParser(str(md_file))
                self.documents[doc.name()] = doc
            except Exception as e:
                print(f"⚠️ Error parsing {md_file}: {e}")

    def get(self, name: str) -> Optional[VaultDocumentParser]:
        """Get document by name."""
        return self.documents.get(name)

    def find_by_type(self, doc_type: str) -> List[VaultDocumentParser]:
        """Find all documents of a specific type."""
        return [doc for doc in self.documents.values() if doc.type() == doc_type]

    def find_by_foco(self, foco: str) -> List[VaultDocumentParser]:
        """Find all documents with specific foco."""
        return [doc for doc in self.documents.values() if doc.foco() == foco]

    def find_by_tag(self, tag: str) -> List[VaultDocumentParser]:
        """Find all documents with specific tag."""
        return [doc for doc in self.documents.values() if tag in doc.tags()]

    def audit_completeness(self) -> Dict:
        """Audit vault for completeness and compliance."""
        complete = [doc for doc in self.documents.values() if doc.is_complete()]
        incomplete = [doc for doc in self.documents.values() if not doc.is_complete()]

        return {
            'total_documents': len(self.documents),
            'complete': len(complete),
            'incomplete': len(incomplete),
            'compliance_score': (len(complete) / len(self.documents) * 100) if self.documents else 0,
            'incomplete_files': [doc.name() for doc in incomplete],
        }

    def __len__(self) -> int:
        """Return number of documents loaded."""
        return len(self.documents)


if __name__ == '__main__':
    # Example usage
    import sys

    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            doc = VaultDocumentParser(filepath)
            print(f"✅ Parsed: {doc}")
            print(f"\nSummary:")
            import json
            print(json.dumps(doc.summary(), indent=2, default=str))
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        print("Usage: python3 vault_parser.py <filepath>")
        print("\nExample:")
        print("  python3 vault_parser.py /path/to/vault/02-SOPs/SOP-1-STORE-CONTEXT-SETUP-v2.md")
