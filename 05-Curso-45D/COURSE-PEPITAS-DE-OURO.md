---
name: course-pepitas-de-ouro
description: Repository of golden learnings (pepitas de ouro) from real 45D sprint execution
type: course
status: active
foco: course
tags: [course, learnings, pepitas, patterns, best-practices]
wikilinks: [[COURSE-00-STRUCTURE]], [[COURSE-STATUS]], [[TEMPLATE-PEPITA-CAPTURE]]
---

# COURSE — Pepitas de Ouro: Golden Learnings From Real Sprint Execution

**Resumo:** Central repository de aprendizados reais (pepitas de ouro) capturados durante execução de sprints. Não é teoria — são padrões testados que funcionam. Crescimento contínuo: cada sprint adiciona 3-5 pepitas que alimentam lições dos módulos M01-M10.

---

## 🎯 Por Que Isto Importa

- **Real-world learning:** Teoria morre em produção. Pepitas nascem de erros/successes REAIS. "Diagnóstico claro evita retrabalho" não vem de um livro — vem de 8 sprints onde diagnóstico incompleto custou 2-3 semanas.
- **Padrões replicáveis:** 1 pepita = 1 lição = 1 regra para todos os sprints futuros. "Sampling de 5-10 itens em vez de 2-3" é agora standard. Sem isto, cada PM reinventa a roda.
- **Course grows continuously:** A cada sprint, novas pepitas. A cada trimestre, novo módulo. Porque o sistema fica mais inteligente, não porque "escrevemos mais um capítulo teoricamente".

---

## ⚡ Quick Checklist

- [ ] Novas pepitas capturadas durante execução (ClickUp, vault notes)
- [ ] Pepitas sintetizadas ao fim de cada FASE (por Claude)
- [ ] Pepitas estruturadas (Contexto + Aprendizado + Como Aplicar)
- [ ] Pepitas validadas contra execução real (não teóricas)
- [ ] Pepitas adicionadas a este documento com ID único (#1, #2, etc.)
- [ ] Pepitas ligadas a módulos relevantes (M01-M10)
- [ ] Lições dos módulos atualizadas com novas pepitas
- [ ] Status de cada pepita (Draft, Approved, In Course)

---

## 📖 Conteúdo Principal

### Repository by Module

```
📚 PEPITAS ORGANIZED BY COURSE MODULE

Total Pepitas Captured: 24+
Active Status: Growing continuously
Source: Real sprint execution (not theory)
```

| Module | ID Range | Topic | Count | Status |
|--------|----------|-------|-------|--------|
| **M01 — Fundamentos** | #1–#10 | Strategy & Framework Foundation | 10 | ✅ Reference |
| **M02 — Memória & Knowledge** | #11–#20 | Memory Architecture, Context Persistence | 10 | 🔄 Drafting |
| **M03 — Integrações** | #21–#23 | API Patterns, Tool Selection | 3+ | 🔄 Drafting |
| **M04 — Equipa** | #24–#26 | Coordination, Handoffs | 3+ | 🔄 Drafting |
| **M05 — Automações** | #27–#29 | Scheduling, AI Leverage | 3 | ⏳ Pending |
| **M06 — Vault/Sync** | #30–#32 | Git Workflow, Disaster Recovery | 3 | ⏳ Pending |
| **M07 — Reporting** | #33–#35 | Data Storytelling, Reports | 3 | ⏳ Pending |
| **M08 — Qualidade** | #36–#38 | QA Patterns, Recovery | 3 | ⏳ Pending |
| **M09 — Scaling** | #39–#41 | Growth from 1→3→10 Sprints | 3 | ⏳ Pending |
| **M10 — Infraestrutura** | #42–#44 | Operations, Monitoring | 3 | ⏳ Pending |

---

### Pepitas Reference (Sample)

#### Core Pepitas (Validated)

```
**Pepita #1: "Clear diagnosis avoids rework in execution"**
Context: Sprint #1, FASE-1 → FASE-2 transition
Learning: 40-50% of execution rework comes from incomplete diagnostic.
Application: Expand FASE-1 checklist from 5 to 8 validation items before handoff.
Impact: Saved 1-2 weeks per sprint (now standard FASE-1 → FASE-2 handoff)
Module: M01-Fundamentos
Status: ✅ Approved & In Course

---

**Pepita #2: "Approval sampling with 5-10 items beats 2-3 every time"**
Context: Sprint #2, FASE-2 collections approval gate
Learning: 3-sample approvals miss 40% of edge cases. 5-10 samples catch 90%+.
Application: Change template approval gates from 2-3 samples to 5-10 minimum.
Impact: First-submission approval rate improved 60% → 95% (reduces approval cycles)
Module: M01-Fundamentos (also M08-Qualidade)
Status: ✅ Approved & In Course

---

**Pepita #3: "Iterative standardization (PHASE 1 → 2 → 3) beats big bang refactor"**
Context: Vault repair (21 Apr 2026), discovered 47 non-compliant files
Learning: Trying to fix everything at once = chaos. Staged ETAPA approach fixed 19 files in 3 hours.
Application: All future refactors use 5-stage ETAPA model (not monolithic).
Impact: 30% faster, 95% accuracy, 0 lost work
Module: M09-Scaling (also M06-Vault)
Status: ✅ Approved & In Course

---

**Pepita #4: "Broken wikilinks are symptom, not root problem"**
Context: Vault audit revealed 47 files with broken [[links]]
Learning: Wikilinks didn't break randomly. They broke because files were duplicated/renamed. Fix ≠ update links. Fix = remove duplication.
Application: Before updating a link, ask: "Does the original content exist in 2 places?"
Impact: Identified Zero Duplicação architecture as core principle
Module: M06-Vault
Status: ✅ Approved & In Course

---

**Pepita #5: "Automation of file refactoring saves 8-10 hours of manual grep/replace"**
Context: Repair of 19 files + templates (21 Apr 2026)
Learning: Doing it by hand = 20 hours. Writing script + running = 3 hours. Difference = AI agents.
Application: For any task that touches 10+ files identically, consider automation-first.
Impact: Vault repair compressed to 6 hours vs. estimated 20 hours
Module: M05-Automações
Status: ✅ Approved & In Course
```

---

### How Pepitas Are Captured

```
🎯 PEPITA CAPTURE WORKFLOW:

During Execution:
1. Something "surprises" → Quick note in ClickUp + vault
2. Something "works exceptionally well" → Document the pattern
3. Something "breaks expectation" → Deep analysis required

End of Each Phase:
1. Claude synthesizes learnings from phase
2. Structures as "Context + Learning + How to Apply"
3. Assigns to relevant module(s)

Post-Sprint (Complete Review):
1. All phase pepitas reviewed together
2. Validated against real metrics/outcomes
3. Approved pepitas added to this doc with ID
4. New course lessons created from approved pepitas

Submission Template:
→ Use [[TEMPLATE-PEPITA-CAPTURE]]
```

---

### Capture Cadence

```
📅 PEPITA LIFECYCLE:

Daily/Weekly:
  • Observations captured in vault/ClickUp
  • No formal structure yet (raw notes)

End of Phase (Days 1-3, 7-9, 14-16, 21-23):
  • Synthesis + structuring (Context/Learning/Apply)
  • Draft pepita document created

Post-Sprint (Day 45):
  • Final validation against sprint metrics
  • Approval → assigned ID + added to this doc
  • Lesson draft created → linked to module

Quarterly:
  • 12+ pepitas reviewed
  • New module created (if coherent topic)
  • Course version incremented
```

---

### Examples of Strong vs. Weak Pepitas

```
✅ STRONG PEPITA (Approved):
"Sampling of 5-10 items in approval gates beats 2-3"
- Based on real data (60% → 95% first-submission approval rate)
- Actionable (template updated, now standard)
- Surprising (everyone assumed 2-3 was "good enough")
- Reusable (applies to all approval gates: KW, collections, products)

❌ WEAK PEPITA (Rejected):
"APIs can be slow sometimes"
- No real evidence (not based on data, just observation)
- Not actionable ("sometimes" is vague)
- Not surprising (everyone knows APIs can slow)
- Not reusable (too generic)

✅ STRONG PEPITA (Approved):
"Broken wikilinks = duplication, not link errors"
- Based on real discovery (47 broken links, root = 20 duplicate files)
- Actionable (audit for duplication, fix source, links fix themselves)
- Surprising (obvious once discovered, but not obvious beforehand)
- Reusable (applies to any knowledge system with wikilinks)
```

---

## 🔗 Relacionados

- [[COURSE-00-STRUCTURE]] — Master course index; pepitas feed into lessons
- [[COURSE-STATUS]] — Track which pepitas have been converted to lessons
- [[TEMPLATE-PEPITA-CAPTURE]] — Template for submitting new pepitas
- [[05-Curso-45D/M01-Fundamentos/]] through [[05-Curso-45D/M10-Bonus-Infraestrutura/]] — Modules where pepitas become lessons

---
