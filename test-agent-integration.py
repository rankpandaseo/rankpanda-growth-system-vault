#!/usr/bin/env python3
"""Integration test: Agent reads SOP → extracts checklist → creates document → validates."""

import subprocess
import sys
from pathlib import Path
from vault_parser import VaultDocumentParser, VaultParser

def step1_read_document(filepath):
    """Step 1: Agent reads a SOP document."""
    print("\n📖 STEP 1: Agent reads document")
    print(f"─" * 60)

    try:
        doc = VaultDocumentParser(filepath)
        print(f"✅ Loaded: {doc.name()} ({doc.type()})")
        print(f"   Title: {doc.title}")
        print(f"   Status: {doc.status()}")
        print(f"   Complete: {doc.is_complete()}")
        return doc
    except Exception as e:
        print(f"❌ Failed to read: {e}")
        return None

def step2_extract_checklist(doc):
    """Step 2: Agent extracts checklist from SOP."""
    print("\n✅ STEP 2: Agent extracts checklist")
    print(f"─" * 60)

    checklist = doc.checklist()
    if not checklist:
        print("⚠️  No checklist items found")
        return checklist

    print(f"✅ Found {len(checklist)} checklist items:")
    for i, item in enumerate(checklist[:5], 1):
        print(f"   {i}. {item}")

    if len(checklist) > 5:
        print(f"   ... and {len(checklist) - 5} more")

    return checklist

def step3_understand_context(doc):
    """Step 3: Agent extracts context from document."""
    print("\n📚 STEP 3: Agent understands document context")
    print(f"─" * 60)

    print(f"✅ Why this matters:")
    why = doc.why()
    if why:
        print(f"   {why[:100]}..." if len(why) > 100 else f"   {why}")

    print(f"\n✅ Related documents:")
    related = doc.related()
    for wikilink, desc in related[:3]:
        print(f"   - {wikilink}: {desc}")

    print(f"\n✅ Key sections extracted:")
    print(f"   - Content: {len(doc.content())} chars")
    print(f"   - Wikilinks: {len(doc.wikilinks())}")

    return {
        'why': why,
        'related': related,
        'wikilinks': doc.wikilinks()
    }

def step4_create_related_document():
    """Step 4: Agent creates a new related document."""
    print("\n📝 STEP 4: Agent creates new related document")
    print(f"─" * 60)

    cmd = [
        'python3',
        'create-vault-document.py',
        '--type', 'reference',
        '--name', 'Integration Test Reference',
        '--description', 'Auto-created document during Phase 2C integration test',
        '--foco', 'operational',
        '--auto-suggest'
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"✅ Created document")
        # Extract filename from output
        for line in result.stdout.split('\n'):
            if 'Created:' in line:
                print(f"   {line.strip()}")
        return True
    else:
        print(f"❌ Failed to create: {result.stderr}")
        return False

def step5_validate_new_document():
    """Step 5: Agent validates the newly created document."""
    print("\n✔️ STEP 5: Agent validates new document")
    print(f"─" * 60)

    # Find the most recently created reference document
    vault = VaultParser('.')
    vault.load_all()

    # Get all reference documents, sorted by creation time
    refs = vault.find_by_type('reference')
    if not refs:
        print("⚠️  No reference documents found")
        return False

    # Get the one matching "integration-test-reference"
    test_doc = None
    for doc in refs:
        if 'integration-test-reference' in doc.name():
            test_doc = doc
            break

    if not test_doc:
        print("⚠️  Integration test document not found")
        return False

    print(f"✅ Found: {test_doc.name()}")
    print(f"   Complete: {test_doc.is_complete()}")
    print(f"   Type: {test_doc.type()}")
    print(f"   Status: {test_doc.status()}")
    print(f"   Wikilinks: {test_doc.wikilinks()}")

    return test_doc.is_complete()

def main():
    print("\n" + "=" * 60)
    print("🧪 AGENT INTEGRATION TEST — Phase 2C")
    print("=" * 60)
    print("Testing: Read → Extract → Create → Validate workflow")

    # Use a known SOP for testing
    test_sop = "02-SOPs/FASE-0-KICKOFF.md"

    if not Path(test_sop).exists():
        print(f"❌ Test SOP not found: {test_sop}")
        return False

    # Step 1: Read
    doc = step1_read_document(test_sop)
    if not doc:
        return False

    # Step 2: Extract checklist
    checklist = step2_extract_checklist(doc)

    # Step 3: Understand context
    context = step3_understand_context(doc)

    # Step 4: Create new document
    created = step4_create_related_document()
    if not created:
        print("❌ Integration test failed at document creation")
        return False

    # Step 5: Validate new document
    valid = step5_validate_new_document()

    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    if valid:
        print("✅ PASSED — Agent workflow complete!")
        print("   1. ✅ Read document successfully")
        print("   2. ✅ Extracted checklist items")
        print("   3. ✅ Understood context (why + related)")
        print("   4. ✅ Created new document")
        print("   5. ✅ Validated new document")
        print("\n🎉 Phase 2C integration test SUCCESSFUL")
        return True
    else:
        print("❌ FAILED — Document validation failed")
        return False

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
