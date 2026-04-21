---
name: template-pepita-capture
description: Pepita Capture template for documenting golden insights discovered during sprint execution
type: template
status: active
foco: operational
tags: [template, pepita, learning, course, documentation]
wikilinks: [[05-Curso-45D/pepitas-de-ouro]], [[FASE-0-KICKOFF]], [[FASE-1-DIAGNOSTIC]], [[FASE-2-EXECUTION]], [[FASE-3-VALIDATION]]
---

# TEMPLATE — Pepita Capture: Learning Documentation

**Resumo:** Formulário para capturar "pepitas de ouro" (golden nuggets of insight) que emergem durante a execução do sprint. Usado semanalmente para documentar padrões, descobertas, e insights que alimentam o course.

---

## 🎯 Por Que Isto Importa

- **Captura real-time learning:** Sem este form, insights morrem. Com ele, cada sprint gera 3-5 pepitas que ficam no course para sempre (e evitam erros futuros).
- **Transforma execução em educação:** A diferença entre "fazemos a work" vs "documentamos a work" é 50% do valor de escala. Pepitas = multiplicadores de valor.
- **Mantém 45D System evolutivo:** Cada sprint melhora o playbook anterior. Erros descobertos em FASE-2 viram regras em FASE-2-v2. Padrões replicáveis viram best practices.

---

## ⚡ Quick Checklist

- [ ] Pepita descoberta durante sprint (erro, padrão, insight)
- [ ] Form preenchido enquanto memória está fresca (dentro de 24h da descoberta)
- [ ] Context, Learning, Application tudo documentado com exemplos
- [ ] Classification checklist completo (Type, Domain se applicable)
- [ ] Quality Checklist passado (real evidence, actionable, reusable)
- [ ] Pepita ID atribuído (após review)
- [ ] Adicionado a pepitas-de-ouro.md
- [ ] Referência em módulos do course relevantes

---

## 📖 Conteúdo Principal

### Form Header

```
🏆 PEPITA DE OURO — LEARNING CAPTURE FORM

Sprint: _________________ 
Phase: FASE _____ (0/1/2/3)
Week: _____ of sprint
Date Discovered: _______________

Captured By: _________________________ | Role: _______________________
```

---

### Section 1: Pepita Title & Context

#### The Title

```
**Pepita Title** (5-10 words max — clear, actionable statement):

"_________________________________________________________________"

Example titles:
- "Metafield schema changes broke bulk API if no fallback"
- "Product sampling of 10 items caught 80% of client feedback"
- "Collection pages rank better when description <160 chars"
```

#### The Trigger (Where did this come from?)

```
**Trigger/Discovery:** Where did this learning emerge? What situation revealed it?

_________________________________________________________________
_________________________________________________________________

Example:
"During FASE-2 bulk apply, 47 products failed with GraphQL error. 
Discovered: missing metafield fallback logic. Cost: 4 hours debugging. 
Lesson: add schema validation before bulk operations."
```

#### Date & Source

```
**When Discovered:** _______________________

**Source/Project:** [Client Name] Sprint [#] FASE ___

**Situation Context:** What was the team doing when this emerged?

_________________________________________________________________
_________________________________________________________________
```

---

### Section 2: The Learning & Impact

#### Core Learning (What pattern emerged?)

```
**The Learning (O Aprendizado):**

What did we learn? What pattern or principle emerged?

_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

Example:
"Client approval gates with only 3 samples miss 40% of edge cases.
Next time: 5-10 samples + more diverse category mix = higher approval 
quality on first submission."
```

#### Why It Matters

```
**Why It Matters:**

Impact on project? How does this improve future execution?

_________________________________________________________________
_________________________________________________________________

Example:
"Saves 1-2 weeks of revision cycles. Increases client confidence. 
Directly impacts FASE-2 timeline."
```

#### Impact Metrics (if applicable)

```
**Metrics/Evidence:**

What data proves this learning? (time saved, errors caught, quality improved, etc.)

_________________________________________________________________
_________________________________________________________________

Examples:
- "Saved 4 hours debugging" 
- "Prevented 47 API failures"
- "Increased first-submission approval rate from 60% → 95%"
- "Client feedback time reduced 48h → 24h"
```

---

### Section 3: How to Apply

#### Direct Application (Action Steps)

```
**Direct Application (Como Aplicar):**

How should the next sprint use this learning? Step-by-step.

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

Example:
1. Before FASE-2 bulk apply, run schema validation script
2. Test on 5% sample first, monitor for errors
3. If zero errors, proceed with 95% remaining batch
```

#### Best Practice Going Forward

```
**Best Practice (Regra):**

What's the rule/principle for next time?

_________________________________________________________________
_________________________________________________________________

Example:
"Always validate metafield schema before bulk operations.
Never apply to 100% of items without 5-10 item test first."
```

#### Where to Document

```
**Storage Location:**

This learning should live in:
[ ] SOP (which one?) _______________________
[ ] FASE (which one?) _______________________
[ ] Template (which one?) _______________________
[ ] Course Module (which one?) _______________________
[ ] Pepitas Main File (always yes)
```

---

### Section 4: Classification & Quality

#### Pepita Type

```
🏷️ CLASSIFICATION:

**Type (select 1):**

[ ] 45D System Pepita — Learning about the process/framework itself
    Example: "Approval gates work better with 5-10 samples"

[ ] Shopify SEO Pepita — Domain-specific learning about SEO on Shopify
    Example: "Collection pages rank better with schema.org"

[ ] Technical Pepita — Code, API, infrastructure learning
    Example: "GraphQL mutations need fallback logic"

[ ] Team/Operations Pepita — How we work, internal process
    Example: "Weekly learnings sync increased knowledge sharing 50%"

[ ] Client Communication Pepita — Relationship, feedback, expectations
    Example: "Sampling form with visual mockups gets 2x faster approvals"
```

#### Domain (if Shopify/SEO-specific)

```
**Domain (if applicable — select all that apply):**

[ ] Technical SEO (crawlability, indexation, robots.txt, sitemap)
[ ] Content/Metadata (titles, descriptions, keyword placement)
[ ] Collection Structure (hierarchy, taxonomy, clustering)
[ ] Product Optimization (product pages, metafields, bulk updates)
[ ] Shopify API/Metafields (GraphQL, REST, schema validation)
[ ] Indexation Patterns (what gets indexed, what doesn't, why)
[ ] Schema/Structured Data (schema.org, JSON-LD, implementation)
[ ] Client Workflow (approval gates, sampling, communication)
[ ] Other: _______________________________
```

#### Quality Checklist

```
✅ QUALITY CHECKLIST:

This pepita is...

[ ] Based on REAL EVIDENCE (not theory or guessing)
    — Can you point to specific proof? Metrics? Error logs?

[ ] ACTIONABLE (can be applied to next sprint)
    — Does someone know exactly what to do with this?

[ ] SURPRISING or NON-OBVIOUS
    — Would someone learn something new from this? Or is it "obvious"?

[ ] REUSABLE across multiple clients/sprints
    — Does this pattern apply to most stores? Or just this one edge case?

[ ] CLEARLY DOCUMENTED
    — Is context clear enough that someone reads this in 3 months and understands?

[ ] HIGH IMPACT on sprint outcomes
    — Does this improve quality, speed, or ROI significantly?

**Rating:**

[ ] 🟢 Essential — Must include in course. Critical learning.
[ ] 🟡 Important — Should include. High value.
[ ] 🔵 Nice-to-have — Maybe later. Interesting but not urgent.
```

---

### Section 5: Approval & Storage

#### Final Approval

```
✅ APPROVAL:

**RankPanda Review:** [ ] Approved [ ] Needs More Work [ ] Rejected

**Feedback/Notes:**
_________________________________________________________________
_________________________________________________________________

**Reviewed By:** _________________________ | **Date:** _______________
```

#### Pepita ID & Storage

```
📝 STORAGE & REFERENCE:

**Pepita ID (assigned by course system):** #_____

**Added to `pepitas-de-ouro.md`:** [ ] Yes [ ] Pending [ ] No

**Modules Where Included:**
- Module: M_____ (____________________)
- Module: M_____ (____________________)

**SOPs Where Referenced:**
- SOP: [[FASE-___-___________]]
- SOP: [[SOP-___-___________]]

**Templates Updated:**
- [[TEMPLATE-___________]]

**Status:** [ ] Active (in use) [ ] Draft (in review) [ ] Archived
```

---

### Examples of Strong Pepitas

```
📚 REFERENCE EXAMPLES:

**Example 1 — 45D System Pepita:**
Title: "Approval gate sampling of 5-10 items catches 80% of revision needs"
Learning: Client feedback quality improves with sample size 5-10 vs. 2-3.
Application: All future approval gates use 5-10 samples minimum.
Impact: Saves 1-2 weeks of revision per sprint.

**Example 2 — Shopify SEO Pepita:**
Title: "Collection pages with schema.org ProductCollection rank 15-30% higher"
Learning: Explicit schema improves CTR for branded collection searches.
Application: Add schema.org:ProductCollection to all collection pages via Liquid.
Impact: +X organic sessions on collection pages.

**Example 3 — Technical Pepita:**
Title: "GraphQL bulk mutations need fallback logic for missing metafields"
Learning: If a metafield is missing, bulk mutation fails silently without errors.
Application: Validate all metafield data before bulk API calls.
Impact: Prevented 4-hour debugging session. Zero silent failures now.

**Example 4 — Client Communication Pepita:**
Title: "Approval forms with visual mockups get 100% faster approval than text-only"
Learning: Clients can't visualize changes from text. Mockups = instant clarity.
Application: Always include before/after screenshots or mockups in approval forms.
Impact: Approval turnaround 48h → 24h.
```

---

## 🔗 Relacionados

- [[05-Curso-45D/pepitas-de-ouro]] — Main file where all pepitas are stored
- [[FASE-0-KICKOFF]], [[FASE-1-DIAGNOSTIC]], [[FASE-2-EXECUTION]], [[FASE-3-VALIDATION]] — Phases where pepitas are discovered
- [[CONCEITO-Client-Approval]] — Client communication patterns generate pepitas frequently

---
