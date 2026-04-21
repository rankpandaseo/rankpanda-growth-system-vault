#!/usr/bin/env python3
"""
Interlinking Validator — Analyze vault wikilinks for bidirectional correctness
"""

import os
import re
from collections import defaultdict
from pathlib import Path

def extract_wikilinks(content):
    """Extract all [[...]] wikilinks from markdown content"""
    pattern = r'\[\[([^\]]+)\]\]'
    return re.findall(pattern, content)

def read_vault_structure(vault_path):
    """Read all markdown files and extract wikilinks"""

    wikilink_graph = defaultdict(list)  # source -> [targets]
    reverse_graph = defaultdict(list)   # target -> [sources]
    all_files = {}  # filename -> full_path

    # Scan all markdown files
    for root, dirs, files in os.walk(vault_path):
        # Skip .git, .obsidian, etc
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                # Store by filename without extension
                filename = file.replace('.md', '')
                all_files[filename] = full_path

                # Read content
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract wikilinks
                links = extract_wikilinks(content)
                wikilink_graph[filename] = links

                # Build reverse graph
                for target in links:
                    reverse_graph[target].append(filename)

    return wikilink_graph, reverse_graph, all_files

def validate_interlinking(vault_path):
    """Run full validation"""

    print("\n🔍 INTERLINKING VALIDATOR — RankPanda Vault\n")
    print("=" * 70)

    wikilink_graph, reverse_graph, all_files = read_vault_structure(vault_path)

    errors = []
    warnings = []

    # 1. Check for broken wikilinks
    print("\n✅ CHECKING BROKEN WIKILINKS")
    print("-" * 70)

    broken = []
    for source, targets in wikilink_graph.items():
        for target in targets:
            if target not in all_files:
                broken.append((source, target))
                errors.append(f"BROKEN: [[{source}]] references non-existent [[{target}]]")

    if broken:
        print(f"❌ Found {len(broken)} broken wikilinks:")
        for source, target in broken:
            print(f"   - [[{source}]] → [[{target}]] (not found)")
    else:
        print("✅ All wikilinks point to existing files")

    # 2. Check for one-way links (not bidirectional)
    print("\n✅ CHECKING BIDIRECTIONALITY")
    print("-" * 70)

    one_way = []
    for source, targets in wikilink_graph.items():
        for target in targets:
            # Check if target links back to source
            target_links = wikilink_graph.get(target, [])
            if source not in target_links:
                # Check if it's an expected one-way (template, reference)
                # For now, just log it
                one_way.append((source, target))

    if one_way:
        print(f"⚠️  Found {len(one_way)} one-way links (may be intentional):")
        for source, target in one_way[:10]:  # Show first 10
            print(f"   - [[{source}]] → [[{target}]] (no backlink)")
        if len(one_way) > 10:
            print(f"   ... and {len(one_way) - 10} more")
    else:
        print("✅ All links are bidirectional")

    # 3. Check for orphaned files (no inlinks, no outlinks)
    print("\n✅ CHECKING FOR ORPHANED FILES")
    print("-" * 70)

    orphaned = []
    for filename in all_files.keys():
        has_inlinks = len(reverse_graph.get(filename, [])) > 0
        has_outlinks = len(wikilink_graph.get(filename, [])) > 0

        if not has_inlinks and not has_outlinks:
            orphaned.append(filename)

    if orphaned:
        print(f"⚠️  Found {len(orphaned)} potentially orphaned files:")
        for f in orphaned:
            print(f"   - {f}")
    else:
        print("✅ No orphaned files found")

    # 4. Graph statistics
    print("\n📊 GRAPH STATISTICS")
    print("-" * 70)

    total_files = len(all_files)
    total_links = sum(len(targets) for targets in wikilink_graph.values())
    avg_links = total_links / total_files if total_files > 0 else 0

    # Files with most inlinks
    top_inlinks = sorted(
        [(f, len(sources)) for f, sources in reverse_graph.items()],
        key=lambda x: x[1],
        reverse=True
    )[:5]

    # Files with most outlinks
    top_outlinks = sorted(
        [(f, len(targets)) for f, targets in wikilink_graph.items()],
        key=lambda x: x[1],
        reverse=True
    )[:5]

    print(f"Total files: {total_files}")
    print(f"Total links: {total_links}")
    print(f"Average links per file: {avg_links:.1f}")

    print(f"\n🔝 Most referenced files (inlinks):")
    for f, count in top_inlinks:
        print(f"   - {f}: {count} references")

    print(f"\n🔗 Most linking files (outlinks):")
    for f, count in top_outlinks:
        print(f"   - {f}: {count} links")

    # 5. Summary
    print("\n" + "=" * 70)
    print("📋 VALIDATION SUMMARY")
    print("=" * 70)

    if errors:
        print(f"❌ {len(errors)} ERRORS found")
        print(f"⚠️  {len(warnings)} WARNINGS")
        print(f"📊 {total_files} files analyzed, {total_links} links")
        return False
    elif warnings or orphaned or one_way:
        print(f"✅ No critical errors")
        print(f"⚠️  {len(warnings) + len(orphaned) + len(one_way)} warnings (review above)")
        print(f"📊 {total_files} files analyzed, {total_links} links")
        return True
    else:
        print(f"✅ VALIDATION PASSED")
        print(f"📊 {total_files} files, {total_links} links, all bidirectional")
        return True

if __name__ == '__main__':
    vault_path = '/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault'
    success = validate_interlinking(vault_path)
    exit(0 if success else 1)
