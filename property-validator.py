#!/usr/bin/env python3
"""Property Validation Rules — Custom validation per document type."""

from dataclasses import dataclass
from typing import List, Dict, Optional
from vault_parser import VaultDocumentParser, VaultParser

@dataclass
class ValidationRule:
    """A single validation rule for a document."""
    name: str
    required: bool
    description: str
    check: callable  # Function that takes doc and returns (passed: bool, message: str)

class PropertyValidator:
    """Validates documents against type-specific rules."""

    def __init__(self):
        """Initialize validator with default rules per type."""
        self.rules = self._build_rules()

    def _build_rules(self) -> Dict[str, List[ValidationRule]]:
        """Build validation rules for each document type."""
        return {
            'sop': [
                ValidationRule(
                    'has_checklist',
                    required=True,
                    description='SOP must have actionable checklist',
                    check=lambda doc: (len(doc.checklist()) > 0,
                                      f"Checklist has {len(doc.checklist())} items")
                ),
                ValidationRule(
                    'has_prerequisites',
                    required=True,
                    description='SOP must document prerequisites',
                    check=lambda doc: (len(doc.content()) > 50,
                                      f"Content has {len(doc.content())} chars (need >50)")
                ),
                ValidationRule(
                    'proper_status',
                    required=True,
                    description='SOP status must be draft, ready, or active',
                    check=lambda doc: (doc.status() in ['draft', 'ready', 'active'],
                                      f"Status: {doc.status()}")
                ),
                ValidationRule(
                    'has_why_section',
                    required=True,
                    description='SOP must explain why it matters',
                    check=lambda doc: (len(doc.why()) > 0,
                                      f"Why section: {len(doc.why())} chars")
                ),
            ],
            'fase': [
                ValidationRule(
                    'has_checklist',
                    required=True,
                    description='FASE must have clear checklist',
                    check=lambda doc: (len(doc.checklist()) > 0,
                                      f"Checklist: {len(doc.checklist())} items")
                ),
                ValidationRule(
                    'linked_to_sops',
                    required=False,
                    description='FASE should reference SOPs',
                    check=lambda doc: (len([w for w in doc.wikilinks() if 'sop' in w.lower()]) > 0,
                                      f"SOPs linked: {len([w for w in doc.wikilinks() if 'sop' in w.lower()])}")
                ),
                ValidationRule(
                    'has_related',
                    required=True,
                    description='FASE must have related documents',
                    check=lambda doc: (len(doc.related()) > 0,
                                      f"Related docs: {len(doc.related())}")
                ),
            ],
            'template': [
                ValidationRule(
                    'is_draft',
                    required=True,
                    description='Template should be in draft status',
                    check=lambda doc: (doc.status() == 'draft',
                                      f"Status: {doc.status()}")
                ),
                ValidationRule(
                    'has_placeholders',
                    required=True,
                    description='Template must have fill-in placeholders',
                    check=lambda doc: ('[' in doc.content() or '{{' in doc.content(),
                                      "Contains placeholders or brackets")
                ),
            ],
            'conceito': [
                ValidationRule(
                    'links_to_sops',
                    required=True,
                    description='Conceito must explain related SOPs',
                    check=lambda doc: (len([w for w in doc.wikilinks() if 'sop' in w.lower()]) > 0,
                                      f"SOPs linked: {len([w for w in doc.wikilinks() if 'sop' in w.lower()])}")
                ),
                ValidationRule(
                    'has_why_section',
                    required=True,
                    description='Conceito must explain importance',
                    check=lambda doc: (len(doc.why()) > 50,
                                      f"Why section: {len(doc.why())} chars")
                ),
            ],
            'reference': [
                ValidationRule(
                    'has_content',
                    required=True,
                    description='Reference must have substantive content',
                    check=lambda doc: (len(doc.content()) > 50,
                                      f"Content: {len(doc.content())} chars")
                ),
            ],
            'course': [
                ValidationRule(
                    'has_learning_objectives',
                    required=True,
                    description='Course must explain what you learn',
                    check=lambda doc: (len(doc.why()) > 0,
                                      f"Learning objectives: {len(doc.why())} chars")
                ),
                ValidationRule(
                    'has_content',
                    required=True,
                    description='Course must have educational content',
                    check=lambda doc: (len(doc.content()) > 100,
                                      f"Content: {len(doc.content())} chars")
                ),
            ],
        }

    def validate_document(self, doc: VaultDocumentParser) -> Dict:
        """Validate a document against its type-specific rules."""
        doc_type = doc.type()
        rules = self.rules.get(doc_type, [])

        results = {
            'name': doc.name(),
            'type': doc_type,
            'passed': 0,
            'failed': 0,
            'warnings': 0,
            'details': []
        }

        for rule in rules:
            try:
                passed, message = rule.check(doc)
                status = 'PASS' if passed else 'FAIL'

                if passed:
                    results['passed'] += 1
                else:
                    if rule.required:
                        results['failed'] += 1
                    else:
                        results['warnings'] += 1

                results['details'].append({
                    'rule': rule.name,
                    'required': rule.required,
                    'passed': passed,
                    'message': message,
                    'description': rule.description
                })
            except Exception as e:
                results['failed'] += 1
                results['details'].append({
                    'rule': rule.name,
                    'required': rule.required,
                    'passed': False,
                    'message': f'Error: {e}',
                    'description': rule.description
                })

        return results

    def validate_vault(self) -> Dict:
        """Validate entire vault."""
        vault = VaultParser('.')
        vault.load_all()

        total_docs = len(vault.documents)
        results = {
            'total_documents': total_docs,
            'compliant': 0,
            'non_compliant': 0,
            'issues': [],
            'by_type': {}
        }

        for doc_name, doc in vault.documents.items():
            validation = self.validate_document(doc)

            if validation['failed'] == 0:
                results['compliant'] += 1
            else:
                results['non_compliant'] += 1

            # Group by type
            doc_type = doc.type()
            if doc_type not in results['by_type']:
                results['by_type'][doc_type] = {'total': 0, 'compliant': 0}

            results['by_type'][doc_type]['total'] += 1
            if validation['failed'] == 0:
                results['by_type'][doc_type]['compliant'] += 1

            # Collect failures
            if validation['failed'] > 0:
                results['issues'].append({
                    'document': doc_name,
                    'type': doc_type,
                    'failures': [d for d in validation['details'] if not d['passed'] and d['required']]
                })

        results['compliance_score'] = (results['compliant'] / total_docs * 100) if total_docs > 0 else 0

        return results


if __name__ == '__main__':
    import sys
    import json

    validator = PropertyValidator()

    if len(sys.argv) > 1:
        # Validate specific document
        try:
            doc = VaultDocumentParser(sys.argv[1])
            result = validator.validate_document(doc)
            print(f"\n📋 Validation Report: {result['name']}")
            print(f"─" * 60)
            print(f"Type: {result['type']}")
            print(f"Passed: {result['passed']} | Failed: {result['failed']} | Warnings: {result['warnings']}\n")

            for detail in result['details']:
                status = '✅' if detail['passed'] else ('❌' if detail['required'] else '⚠️')
                print(f"{status} {detail['rule']}")
                print(f"   {detail['description']}")
                print(f"   {detail['message']}\n")
        except Exception as e:
            print(f"❌ Error: {e}")
    else:
        # Audit entire vault
        audit = validator.validate_vault()
        print(f"\n📊 Vault Validation Audit")
        print(f"─" * 60)
        print(f"Total documents: {audit['total_documents']}")
        print(f"Compliant: {audit['compliant']}")
        print(f"Non-compliant: {audit['non_compliant']}")
        print(f"Compliance score: {audit['compliance_score']:.1f}%\n")

        print(f"By Type:")
        for doc_type, stats in sorted(audit['by_type'].items()):
            pct = (stats['compliant'] / stats['total'] * 100) if stats['total'] > 0 else 0
            print(f"  {doc_type}: {stats['compliant']}/{stats['total']} ({pct:.0f}%)")

        if audit['issues']:
            print(f"\n⚠️  Issues Found ({len(audit['issues'])}):")
            for issue in audit['issues'][:5]:
                print(f"\n  {issue['document']} ({issue['type']})")
                for failure in issue['failures'][:2]:
                    print(f"    - {failure['rule']}: {failure['message']}")
