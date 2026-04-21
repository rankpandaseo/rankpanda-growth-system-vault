#!/usr/bin/env python3
"""Wikilink Resolution Graph — Maps wikilink names to filepaths dynamically."""

import re
from pathlib import Path
from typing import Dict, List, Optional, Set
from dataclasses import dataclass

@dataclass
class WikilinkResolution:
    """Result of resolving a wikilink."""
    wikilink_name: str
    filepath: Optional[Path]
    found: bool
    alternatives: List[Path]

class WikilinkResolver:
    """Resolve wikilinks to actual file paths with caching."""

    def __init__(self, vault_root: str):
        """Initialize resolver with vault root directory."""
        self.vault_root = Path(vault_root)
        self.graph: Dict[str, Path] = {}  # name → filepath mapping
        self.reverse_graph: Dict[str, List[str]] = {}  # filepath → [wikilinks]
        self.built = False

    def build_graph(self, force_rebuild: bool = False) -> None:
        """Build wikilink resolution graph from all vault documents."""
        if self.built and not force_rebuild:
            return

        self.graph.clear()
        self.reverse_graph.clear()

        # Index all markdown files
        for md_file in self.vault_root.rglob('*.md'):
            # Skip system directories
            if any(part.startswith('.') for part in md_file.parts):
                continue

            # Use multiple indexing strategies
            self._index_file(md_file)

        self.built = True

    def _index_file(self, filepath: Path) -> None:
        """Index a file for wikilink resolution."""
        filename_no_ext = filepath.stem

        # Strategy 1: Exact filename match (lowercase)
        key = filename_no_ext.lower().replace(' ', '-')
        if key not in self.graph:
            self.graph[key] = filepath

        # Strategy 2: CamelCase conversion
        # e.g., "SOP-StorageContextSetup" → "storage-context-setup"
        camel_match = re.findall(r'([A-Z][a-z]+|[A-Z]+(?=[A-Z][a-z]|\d|\W|$)|\d+)', filename_no_ext)
        if camel_match:
            camel_key = '-'.join(camel_match).lower()
            if camel_key not in self.graph and camel_key != key:
                self.graph[camel_key] = filepath

        # Strategy 3: Type-prefix removal (e.g., "SOP-" prefix)
        # "SOP-MyDoc" → "my-doc"
        type_patterns = ['sop-', 'fase-', 'conceito-', 'template-', 'course-', 'reference-', 'automation-']
        for pattern in type_patterns:
            if filename_no_ext.lower().startswith(pattern):
                bare_name = filename_no_ext[len(pattern):].lower().replace(' ', '-')
                if bare_name not in self.graph:
                    self.graph[bare_name] = filepath
                break

    def resolve(self, wikilink_name: str) -> WikilinkResolution:
        """Resolve a single wikilink name to filepath."""
        if not self.built:
            self.build_graph()

        wikilink_key = wikilink_name.lower().replace(' ', '-')

        # Direct match
        if wikilink_key in self.graph:
            return WikilinkResolution(
                wikilink_name=wikilink_name,
                filepath=self.graph[wikilink_key],
                found=True,
                alternatives=[]
            )

        # Fuzzy match (partial name)
        alternatives = []
        for key, filepath in self.graph.items():
            if wikilink_key in key or key in wikilink_key:
                alternatives.append(filepath)

        return WikilinkResolution(
            wikilink_name=wikilink_name,
            filepath=None,
            found=False,
            alternatives=alternatives[:3]  # Top 3 alternatives
        )

    def resolve_batch(self, wikilink_names: List[str]) -> Dict[str, WikilinkResolution]:
        """Resolve multiple wikilinks."""
        return {name: self.resolve(name) for name in wikilink_names}

    def get_bidirectional_links(self, filepath: Path) -> Dict[str, List[str]]:
        """Get incoming and outgoing links for a document."""
        from vault_parser import VaultDocumentParser

        try:
            doc = VaultDocumentParser(str(filepath))
            outgoing = doc.wikilinks()

            # Find incoming links (which documents reference this file)
            incoming = []
            target_name = filepath.stem.lower()

            for other_file in self.vault_root.rglob('*.md'):
                if other_file == filepath or any(part.startswith('.') for part in other_file.parts):
                    continue

                try:
                    other_doc = VaultDocumentParser(str(other_file))
                    if any(target_name in wl.lower() for wl in other_doc.wikilinks()):
                        incoming.append(other_file.stem)
                except:
                    pass

            return {
                'incoming': incoming,
                'outgoing': outgoing
            }
        except:
            return {'incoming': [], 'outgoing': []}

    def detect_broken_links(self) -> Dict[str, List[str]]:
        """Detect broken wikilinks in all vault documents."""
        from vault_parser import VaultParser

        if not self.built:
            self.build_graph()

        vault = VaultParser(str(self.vault_root))
        vault.load_all()

        broken_links = {}

        for doc_name, doc in vault.documents.items():
            unresolved = []
            for wikilink in doc.wikilinks():
                resolution = self.resolve(wikilink)
                if not resolution.found:
                    unresolved.append(wikilink)

            if unresolved:
                broken_links[doc_name] = unresolved

        return broken_links

    def suggest_wikilinks(self, text: str, limit: int = 5) -> List[str]:
        """Suggest wikilinks based on text content."""
        if not self.built:
            self.build_graph()

        suggestions = []
        words = re.findall(r'\b[A-Za-z]{4,}\b', text.lower())
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        # Find matching documents
        for word, freq in sorted(word_freq.items(), key=lambda x: -x[1]):
            resolution = self.resolve(word)
            if resolution.found:
                suggestions.append(resolution.filepath.stem)
                if len(suggestions) >= limit:
                    break

            # Also add alternatives if main doc not found
            for alt_path in resolution.alternatives:
                if len(suggestions) < limit:
                    suggestions.append(alt_path.stem)

        return suggestions[:limit]

    def audit_wikilinks(self) -> Dict:
        """Audit entire vault for wikilink health."""
        if not self.built:
            self.build_graph()

        from vault_parser import VaultParser

        vault = VaultParser(str(self.vault_root))
        vault.load_all()

        total_docs = len(vault.documents)
        broken = self.detect_broken_links()
        broken_count = len(broken)
        total_broken_links = sum(len(links) for links in broken.values())

        orphaned = []
        for doc in vault.documents.values():
            if not doc.wikilinks() and doc.name() not in ['00-readme', 'todo']:
                orphaned.append(doc.name())

        return {
            'total_documents': total_docs,
            'documents_with_broken_links': broken_count,
            'total_broken_links': total_broken_links,
            'orphaned_documents': len(orphaned),
            'graph_size': len(self.graph),
            'broken_links': broken,
            'orphaned': orphaned,
            'health_score': (1 - (total_broken_links / max(1, total_docs * 5))) * 100
        }

    def __len__(self) -> int:
        """Return size of wikilink graph."""
        if not self.built:
            self.build_graph()
        return len(self.graph)

    def __getitem__(self, wikilink_name: str) -> Optional[Path]:
        """Get filepath for wikilink name."""
        resolution = self.resolve(wikilink_name)
        return resolution.filepath if resolution.found else None


if __name__ == '__main__':
    import sys
    import json

    resolver = WikilinkResolver('.')
    resolver.build_graph()

    print(f"📊 Wikilink Resolution Graph")
    print(f"─" * 60)
    print(f"Graph size: {len(resolver)} wikilinks indexed\n")

    if len(sys.argv) > 1:
        wikilink = sys.argv[1]
        resolution = resolver.resolve(wikilink)
        print(f"Resolving: {wikilink}")
        print(f"  Found: {resolution.found}")
        if resolution.filepath:
            print(f"  Path: {resolution.filepath}")
        if resolution.alternatives:
            print(f"  Alternatives: {[str(p) for p in resolution.alternatives]}")
    else:
        # Audit
        audit = resolver.audit_wikilinks()
        print(f"Audit Results:")
        print(f"  Total documents: {audit['total_documents']}")
        print(f"  Docs with broken links: {audit['documents_with_broken_links']}")
        print(f"  Total broken links: {audit['total_broken_links']}")
        print(f"  Orphaned documents: {audit['orphaned_documents']}")
        print(f"  Health score: {audit['health_score']:.1f}%")

        if audit['broken_links']:
            print(f"\n⚠️  Broken Links:")
            for doc, links in list(audit['broken_links'].items())[:5]:
                print(f"  - {doc}: {links}")
