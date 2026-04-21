#!/bin/bash
# Fix wikilink case sensitivity in vault markdown files

cd /Users/rankpanda/Shopify\ RankPanda\ APP\ -\ Oficial\ 2026/vault

echo "🔧 Fixing wikilink case sensitivity..."
echo ""

# Fix lowercase wikilinks to match actual filenames
# SOP files
find 02-SOPs -name "*.md" -exec sed -i '' \
  -e 's/\[\[\[\[sop-1-store-context-setup\]\]/[[SOP-1-STORE-CONTEXT-SETUP-v2]]/g' \
  -e 's/\[\[\[\[sop-2-keyword-research\]\]/[[SOP-2-KEYWORD-RESEARCH-V2]]/g' \
  -e 's/\[\[\[\[sop-2-keyword-research-v2\]\]/[[SOP-2-KEYWORD-RESEARCH-V2]]/g' \
  -e 's/\[\[\[\[sop-3-clustering-collection-mapping\]\]/[[SOP-3-CLUSTERING-COLLECTION-MAPPING]]/g' \
  -e 's/\[\[\[\[fase-0-kickoff\]\]/[[FASE-0-KICKOFF]]/g' \
  -e 's/\[\[\[\[fase-1-diagnostic\]\]/[[FASE-1-DIAGNOSTIC]]/g' \
  -e 's/\[\[\[\[fase-2-execution\]\]/[[FASE-2-EXECUTION]]/g' \
  -e 's/\[\[\[\[fase-3-validation\]\]/[[FASE-3-VALIDATION]]/g' \
  {} \;

# Fix double-bracket lowercase wikilinks
find 02-SOPs -name "*.md" -exec sed -i '' \
  -e 's/\[\[sop-1-store-context-setup\]\]/[[SOP-1-STORE-CONTEXT-SETUP-v2]]/g' \
  -e 's/\[\[sop-2-keyword-research\]\]/[[SOP-2-KEYWORD-RESEARCH-V2]]/g' \
  -e 's/\[\[sop-2-keyword-research-v2\]\]/[[SOP-2-KEYWORD-RESEARCH-V2]]/g' \
  -e 's/\[\[sop-3-clustering-collection-mapping\]\]/[[SOP-3-CLUSTERING-COLLECTION-MAPPING]]/g' \
  -e 's/\[\[fase-0-kickoff\]\]/[[FASE-0-KICKOFF]]/g' \
  -e 's/\[\[fase-1-diagnostic\]\]/[[FASE-1-DIAGNOSTIC]]/g' \
  -e 's/\[\[fase-2-execution\]\]/[[FASE-2-EXECUTION]]/g' \
  -e 's/\[\[fase-3-validation\]\]/[[FASE-3-VALIDATION]]/g' \
  -e 's/\[\[conceito-keyword-research\]\]/[[CONCEITO-Keyword-Research]]/g' \
  -e 's/\[\[conceito-shopify-collections\]\]/[[CONCEITO-Shopify-Collections]]/g' \
  -e 's/\[\[conceito-client-approval\]\]/[[CONCEITO-Client-Approval]]/g' \
  -e 's/\[\[api-registry\]\]/[[API-REGISTRY]]/g' \
  {} \;

echo "✅ Wikilink fixes applied"
echo ""

# Also check and report any remaining potential issues
echo "📊 Checking for remaining issues..."
echo ""

broken=$(grep -r "\[\[[^]]*-[a-z]" 02-SOPs/*.md | grep -v "FASE\|SOP\|CONCEITO\|API" | wc -l)
echo "Lowercase wikilinks remaining: $broken"

echo ""
echo "✅ Done!"
