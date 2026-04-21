#!/usr/bin/env python3
"""Complete vault audit: formatação, structure, readability."""

import os
import re
from pathlib import Path
from collections import defaultdict

VAULT_DIR = Path(__file__).parent

def analyze_file(filepath):
    """Analyze single file comprehensively."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        issues = []
        warnings = []
        score = 100  # Start at 100, deduct for issues

        # 1. Properties check
        properties_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        if not properties_match:
            issues.append("❌ No Properties found")
            score -= 30
        else:
            yaml_content = properties_match.group(1)
            properties = {}
            for line in yaml_content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    properties[key.strip()] = value.strip()

            required = ['name', 'description', 'type', 'status', 'foco']
            missing = [p for p in required if p not in properties]
            if missing:
                issues.append(f"⚠️ Missing properties: {missing}")
                score -= 10 * len(missing)

        # 2. Structure check (4 mandatory sections)
        body = content.split('---\n')[-1] if properties_match else content
        required_sections = ['🎯 Por Que Isto Importa', '⚡ Quick Checklist', '📖 Conteúdo Principal', '🔗 Relacionados']
        found_sections = [s for s in required_sections if s in body]
        missing_sections = [s for s in required_sections if s not in body]

        if missing_sections:
            issues.append(f"⚠️ Missing sections: {missing_sections}")
            score -= 15 * len(missing_sections)

        # 3. Spacing/formatting check
        lines = body.split('\n')

        # Check for proper heading spacing
        heading_issues = 0
        for i, line in enumerate(lines):
            if line.startswith('##'):
                # Should have blank line before (except first)
                if i > 0 and lines[i-1].strip() != '':
                    heading_issues += 1
                # Should have blank line after
                if i < len(lines) - 1 and lines[i+1].strip() != '':
                    heading_issues += 1

        if heading_issues > 3:
            warnings.append(f"⚠️ Poor spacing around headings ({heading_issues} issues)")
            score -= 5

        # 4. Content density check
        non_empty_lines = [l for l in lines if l.strip()]
        avg_line_length = sum(len(l) for l in non_empty_lines) / len(non_empty_lines) if non_empty_lines else 0

        if avg_line_length > 100:
            warnings.append(f"⚠️ Lines too long (avg {avg_line_length:.0f} chars) - hard to read")
            score -= 5

        # 5. Wikilink check
        wikilinks = re.findall(r'\[\[([^\]]+)\]\]', body)
        if wikilinks:
            # Check for case issues (should be CamelCase or uppercase)
            bad_wikilinks = [w for w in wikilinks if w != w.replace(' ', '-') or (w != w.upper() and '-' not in w)]
            if bad_wikilinks:
                warnings.append(f"⚠️ Potential wikilink issues: {bad_wikilinks[:3]}")
                score -= 3

        # 6. Readability estimate (subjective)
        # Check if has proper structure
        has_bullets = '- ' in body
        has_checklist = '[ ]' in body
        has_code = '```' in body

        if not (has_bullets or has_checklist or has_code):
            warnings.append("⚠️ Very text-dense, no visual structure (bullets/checklist/code)")
            score -= 5

        return {
            'filepath': filepath.relative_to(VAULT_DIR),
            'issues': issues,
            'warnings': warnings,
            'score': max(0, score),
            'properties_found': properties_match is not None,
            'sections_found': len(found_sections),
            'sections_missing': missing_sections,
            'content_length': len(body),
            'has_structure': has_bullets or has_checklist or has_code,
        }

    except Exception as e:
        return {
            'filepath': filepath.relative_to(VAULT_DIR),
            'issues': [f"❌ Error reading file: {e}"],
            'warnings': [],
            'score': 0,
            'properties_found': False,
            'sections_found': 0,
        }

def main():
    results = []
    print("🔍 Auditing vault completeness & readability...\n")

    for root, dirs, files in os.walk(VAULT_DIR):
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.claude']]

        for file in files:
            if file.endswith('.md'):
                filepath = Path(root) / file
                result = analyze_file(filepath)
                results.append(result)

    # Sort by score
    results.sort(key=lambda x: x['score'])

    # Print summary
    scores = [r['score'] for r in results]
    avg_score = sum(scores) / len(scores) if scores else 0

    print("=" * 80)
    print(f"📊 VAULT AUDIT SUMMARY")
    print("=" * 80)
    print(f"Total files: {len(results)}")
    print(f"Average format score: {avg_score:.0f}/100")
    print(f"Files with issues: {len([r for r in results if r['issues']])}")
    print(f"Files with warnings: {len([r for r in results if r['warnings']])}")
    print()

    # Print critical issues
    critical = [r for r in results if r['score'] < 50]
    if critical:
        print("🔴 CRITICAL (score < 50):")
        for r in critical[:10]:
            print(f"  {r['filepath']} [{r['score']}/100]")
            for issue in r['issues'][:2]:
                print(f"    {issue}")
        print()

    # Print warning issues
    warnings_only = [r for r in results if r['score'] >= 50 and r['score'] < 80 and r['warnings']]
    if warnings_only:
        print("🟡 WARNINGS (score 50-80):")
        for r in warnings_only[:10]:
            print(f"  {r['filepath']} [{r['score']}/100]")
            for warning in r['warnings'][:1]:
                print(f"    {warning}")
        print()

    # Print good files
    good = [r for r in results if r['score'] >= 80]
    print(f"🟢 GOOD (score >= 80): {len(good)}/{len(results)}")

    # Breakdown by issue type
    print("\n" + "=" * 80)
    print("📈 ISSUE BREAKDOWN")
    print("=" * 80)

    issue_counts = defaultdict(int)
    for r in results:
        for issue in r['issues']:
            if 'No Properties' in issue:
                issue_counts['No Properties'] += 1
            elif 'Missing properties' in issue:
                issue_counts['Incomplete Properties'] += 1
            elif 'Missing sections' in issue:
                issue_counts['Missing Sections'] += 1
        for warning in r['warnings']:
            if 'spacing' in warning.lower():
                issue_counts['Poor Spacing'] += 1
            elif 'Lines too long' in warning:
                issue_counts['Lines Too Long'] += 1
            elif 'wikilink' in warning.lower():
                issue_counts['Wikilink Issues'] += 1
            elif 'text-dense' in warning.lower():
                issue_counts['Text-Dense'] += 1

    for issue_type, count in sorted(issue_counts.items(), key=lambda x: -x[1]):
        print(f"  {issue_type}: {count}")

    print("\n" + "=" * 80)
    print("✅ NEXT STEPS")
    print("=" * 80)
    print("1. Fix CRITICAL issues (No Properties, Missing Sections)")
    print("2. Fix WARNINGS (spacing, readability)")
    print("3. Implement agent parsers for standardized reading")
    print("4. Test with agent workflow")

if __name__ == '__main__':
    main()
