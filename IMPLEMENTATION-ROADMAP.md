---
name: implementation-roadmap
description: Plano de implementação sequencial para vault standardization (curto/médio/longo prazo)
type: reference
status: active
foco: operational
tags: [vault, roadmap, agents, implementation]
wikilinks: [[SOP-VAULT-FORMAT-SPECIFICATION]], [[audit-vault-complete]]
---

# Vault Standardization — Implementation Roadmap

**Status:** 🚀 Ready to Execute
**Priority:** P0 (blocker for agent integration)
**Last Audit:** 2026-04-21, 24/100 avg score

---

## 📊 Current State (Audit Results)

| Métrica | Valor | Status |
|---------|-------|--------|
| Total files | 53 | ✓ |
| Files with Properties | 14/53 | 🔴 26% |
| Files with 4 sections | 0/53 | 🔴 0% |
| Files with good spacing | 51/53 | 🟡 96% |
| Average readability score | 24/100 | 🔴 CRITICAL |
| **BLOCKER:** Agents can read vault? | ❌ No | 🔴 Cannot proceed |

**Key Finding:** Vault is not agent-readable right now. Must fix before agents touch it.

---

## ⏱️ CURTO PRAZO (Today - 2026-04-21, ~3-4 hours)

**Goal:** Make vault agent-readable. Fix structural issues.

### Phase 1A: Add Properties to 39 Missing Files (~1.5h)

**Script:** `add-missing-properties.py`

Ficheiros afectados:
- All 5 `TEMPLATE-*.md` files → Properties with type=template
- All 10 `COURSE-*.md` files (M01-M10) → Properties with type=course
- `AUTOMATION-CLAUDE-SCHEDULED-TASKS.md` → type=automation
- `COURSE-PEPITAS-DE-OURO.md` → type=course
- `00-Memory/context/*.md` files (3 files) → type=reference
- Others (8 files) → type=reference

**Action:**
```bash
python3 add-missing-properties.py
```

**Output:** All 39 files get Properties frontmatter added.

**Validation:** `audit-vault-complete.py` should report 53/53 with Properties.

---

### Phase 1B: Add 4 Mandatory Sections to All Files (~2h)

**Script:** `add-missing-sections.py`

Current state: 0/53 files have the 4 sections.

**The 4 Sections:**
```markdown
## 🎯 Por Que Isto Importa
[bullet points explaining impact]

## ⚡ Quick Checklist
[action items OR summary]

## 📖 Conteúdo Principal
[main content here]

## 🔗 Relacionados
[wikilinks to related docs]
```

**How script works:**
1. Extract existing content (ignore current structure)
2. Categorize by content type (SOP → has checklist, CONCEITO → has overview, etc)
3. Rebuild with 4 mandatory sections
4. Preserve all original content
5. Write back to file

**Action:**
```bash
python3 add-missing-sections.py --auto-categorize
```

**Output:** All 53 files now have consistent 4-section structure.

---

### Phase 1C: Fix Spacing/Readability (~30m)

**Script:** `fix-spacing-and-formatting.py`

Issues to fix:
- 11 files with lines > 100 chars → wrap to 80 chars
- 2 files with poor heading spacing → add blank lines before/after `##`
- Remove excessive blank lines (>2 consecutive)

**Action:**
```bash
python3 fix-spacing-and-formatting.py
```

**Output:** All files have proper spacing, readable in terminal.

---

### Phase 1 Validation (~15m)

```bash
# Re-run audit
python3 audit-vault-complete.py

# Expected output:
# - Average score: 70+/100
# - All 53 files have Properties
# - All 53 files have 4 sections
# - Spacing issues: 0
```

**Commit:** "refactor: Vault structural standardization (Phase 1)"

---

## 📅 MÉDIO PRAZO (Next 3-5 days, ~6-8 hours)

**Goal:** Enable agent reading + document creation. Build parser infrastructure.

### Phase 2A: Agent Reading Parser (~3h)

**Code:** Python library `vault_parser.py`

**What it does:**
```python
from vault_parser import VaultDocumentParser

# Agent can now read documents easily
doc = VaultDocumentParser('02-SOPs/SOP-1-STORE-CONTEXT-SETUP-v2.md')

# Extract properties
doc.name()  # → 'sop-store-context-setup'
doc.type()  # → 'sop'
doc.foco()  # → 'seo'
doc.tags()  # → ['onboarding', 'baseline']

# Extract sections
doc.why()  # → "Por Que Isto Importa" content
doc.checklist()  # → "Quick Checklist" items
doc.content()  # → "Conteúdo Principal" text
doc.related()  # → wikilinks in "Relacionados"

# Wikilink resolution
doc.wikilinks()  # → [['SOP-2-KEYWORD-RESEARCH-V2'], ...]
doc.resolve_wikilinks()  # → [Path('02-SOPs/SOP-2-KEYWORD-RESEARCH-V2.md'), ...]
```

**Implementation:**
- Class `VaultDocumentParser` with methods for each section
- Wikilink resolver (map name → filepath)
- Properties extractor
- Content parser (bullets, checklist items, code blocks)

**Testing:** Unit tests for each method. Test with 5-10 real documents.

---

### Phase 2B: Dynamic Document Creation (~2h)

**Expand:** `create-vault-document.py` with agent template support

**Current:** Agents can create with `--type sop --name "..."` etc.

**New features:**
- Pre-populate sections with AI suggestions
- Validate on creation (not on commit)
- Generate wikilinks suggestions
- Auto-populate "related" section

```bash
# Agent creates document
python3 create-vault-document.py \
  --type sop \
  --name "My New SOP" \
  --description "Description" \
  --foco seo \
  --auto-suggest-related  # ← New: suggests related docs

# Output: ready-to-edit file with smart defaults
```

---

### Phase 2C: Agent Integration Test (~1.5h)

**Test workflow:**
1. Agent reads SOP-1 using `VaultDocumentParser`
2. Agent extracts checklist
3. Agent follows checklist to create data
4. Agent creates new document using script
5. Validate new document is readable

**Success criteria:**
- Agent completes full workflow
- New document is valid (audit score > 80)
- No manual intervention needed

---

### Phase 2 Validation

```bash
# Run agent integration test
python3 test-agent-integration.py

# Expected: ✅ Agent can read → create → validate successfully
```

**Commit:** "feat: Agent parser + dynamic creation (Phase 2)"

---

## 🚀 LONGO PRAZO (2+ weeks, optional enhancements)

**Goal:** Advanced features for production use at scale.

### Phase 3A: Obsidian Plugin (~4-6h)

**What it does:**
- Real-time validation in Obsidian editor
- Properties sidebar shows type, status, foco
- Warns if section missing or properties incomplete
- Database views (filter by type, status, foco)

**Why later:** Agents don't need this. Humans do. Implement after agents working.

---

### Phase 3B: Wikilink Resolution Graph (~4h)

**What it does:**
- System that maps all wikilinks dynamically
- Agent can resolve `[[SOP-1]]` → actual filepath
- Update graph when files added/renamed
- Detect broken links automatically

**Implementation:**
- Hash map (name → filepath)
- Updated on every vault file change
- Exposed as Python API for agents

---

### Phase 3C: Property Validation Rules (~3h)

**What it does:**
- Custom validation rules per document type
- FASE must have: Objetivo, Duração, Deliverables
- SOP must have: Checklist, Pré-requisitos
- CONCEITO must have: Related SOPs

**Implementation:**
- Rules engine as YAML
- Validator checks against rules
- Agents get clear feedback on what's missing

---

## 📋 TODOS & Scripts Needed

### Curto Prazo (URGENT):
- [ ] Create `add-missing-properties.py` (1h)
- [ ] Create `add-missing-sections.py` (1.5h)
- [ ] Create `fix-spacing-and-formatting.py` (0.5h)
- [ ] Run audit after each phase
- [ ] Commit Phase 1 (1h total)

### Médio Prazo (next week):
- [ ] Create `vault_parser.py` + tests (3h)
- [ ] Expand `create-vault-document.py` (2h)
- [ ] Integration test workflow (1.5h)
- [ ] Commit Phase 2

### Longo Prazo (optional):
- [ ] Obsidian plugin (Phase 3A)
- [ ] Wikilink graph (Phase 3B)
- [ ] Property rules (Phase 3C)

---

## 🎯 Success Criteria

| Phase | Metric | Target | Current |
|-------|--------|--------|---------|
| **Phase 1** | Average audit score | 70+/100 | 24/100 |
| **Phase 1** | Files with Properties | 100% | 26% |
| **Phase 1** | Files with 4 sections | 100% | 0% |
| **Phase 2** | Agent can read document | ✅ Yes | ❌ No |
| **Phase 2** | Agent can create document | ✅ Yes | ⚠️ Partial |
| **Phase 3** | Real-time validation | ✅ Yes | N/A |

---

## 📝 Notes for Implementation

**Important:**
- Phase 1 is **BLOCKING** — cannot proceed to agents until vault is readable
- Phase 2 is **ESSENTIAL** — agents need parser + creation before live use
- Phase 3 is **OPTIONAL** — nice-to-have for human workflow, not needed for agents

**Risk:** If Phase 1 fails, agents cannot read vault. Must be 100% successful.

**Dependencies:** Phase 2 depends on Phase 1. Phase 3 is independent.

---

## 🔗 Related

- [[SOP-VAULT-FORMAT-SPECIFICATION]] — The spec we're implementing
- [[SOP-VAULT-NEW-DOCUMENT]] — How to create documents
- [[audit-vault-complete]] — Audit script
