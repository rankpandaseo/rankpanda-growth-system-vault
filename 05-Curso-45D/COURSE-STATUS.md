---
name: course-status
description: Course status tracker - progress on 45D Sprint Framework course completion
type: course
status: active
foco: course
tags: [course, status, progress, tracking]
wikilinks: [[COURSE-00-STRUCTURE]], [[COURSE-PEPITAS-DE-OURO]]
---

# COURSE — Status: 45D Sprint System Course Progress

**Resumo:** Tracking document para progresso do curso. Status de cada módulo (M01-M10), lições completas vs. em progresso, pepitas capturadas. Atualizado semanalmente durante execução de sprints.

---

## 🎯 Por Que Isto Importa

- **Transparência de progresso:** Cliente/team vê exatamente qual é % do curso completo (4/61 lições = 7%). Sem isto, "quando fica o curso pronto?" fica nebuloso.
- **Dependency tracking:** M01 (Fundamentos) DEVE estar 100% antes de M02-M10 fazerem sentido. Status doc mostra blocking dependencies.
- **Pepita-to-lesson conversion:** Cada pepita aprovada = 1 lição. Status doc mostra quantas pepitas ainda faltam ser convertidas em lições.

---

## ⚡ Quick Checklist

- [ ] Todos os módulos M01-M10 têm README (estrutura skeleton)
- [ ] M01 — 4 lições completas (100%)
- [ ] M02-M10 — 57 lições planned, 0 written (skeleton phase)
- [ ] Pepitas M01 capturadas (10 aprovadas)
- [ ] Roadmap para M02-M10 writing (triggered by sprints)
- [ ] Quality checklist por lição (metadata, duração, conteúdo, exemplos)
- [ ] Status doc atualizado semanalmente (% progresso)

---

## 📖 Conteúdo Principal

### Overall Course Status

```
📚 COURSE COMPLETION OVERVIEW

Total Planned:
  • Modules: 10
  • Lessons: 61
  • Duration: 570+ minutes (9.5+ hours)
  
Current State (2026-04-21):
  • Modules Complete: 1 (M01)
  • Lessons Complete: 4 (M01 only)
  • Completion: 7% (4 of 61 lessons)
  • Total Duration Available: 80 minutes (M01 only)

Roadmap Status:
  • Foundation (M01): ✅ 100% Complete
  • Specialty Modules (M02-M10): 🔄 Skeleton Phase (README only)
  • Pepitas System: ✅ Approved & Active
  • Live Deployment: ⏳ Week 5 (estimated)
```

---

### Module-by-Module Breakdown

#### ✅ M01 — Fundamentos: O que é 45D Sprint? (100% Complete)

```
Module Duration: 80 minutes (4 lessons)
Status: ✅ ALL LESSONS COMPLETE
Pepitas Extracted: 10 approved
Quality Review: ✅ Passed
```

| # | Título | Duration | Status | Pepitas |
|---|--------|----------|--------|---------|
| 1.1 | O que é 45D Sprint (e por que funciona) | 20 min | ✅ Complete | #1, #2 |
| 1.2 | As 4 Fases em Detalhe (Kickoff, Diagnostic, Execution, Validation) | 25 min | ✅ Complete | #3, #4 |
| 1.3 | Papéis e Responsabilidades (RankPanda team + cliente) | 15 min | ✅ Complete | #5 |
| 1.4 | Por que isto vence agências tradicionais | 20 min | ✅ Complete | #6-#10 |

---

#### 🔄 M02 — Memória e Contexto: Como Claude Sempre Sabe (0% — Skeleton Phase)

```
Module Duration: 60 minutes (4 lessons planned)
Current Status: 🔄 README ONLY
Estimated Start: Week 2 (post M01 validation)
Trigger: Pilot sprint execution → capture real memory patterns
Expected Pepitas: 10 planned
```

| # | Título | Duration | Status | Notes |
|---|--------|----------|--------|-------|
| 2.1 | O Problema: Cada Sessão Começa do Zero | 12 min | ⏳ Planned | Capture from pilot sprint session transitions |
| 2.2 | A Solução: MEMORY.md e Vault de Contexto | 18 min | ⏳ Planned | Use pilot sprint memory captures as examples |
| 2.3 | Padrões de Memória: Quatro Tipos Que Importam | 15 min | ⏳ Planned | From real memory usage in FASE-1, FASE-2 |
| 2.4 | Evitando Alucinações com Contexto Estruturado | 15 min | ⏳ Planned | Real failures/recovery from pilot |

---

#### 🔄 M03 — Integrações: Qual Ferramenta Usar Quando (0% — Skeleton Phase)

```
Module Duration: 60 minutes (4 lessons planned)
Current Status: 🔄 README ONLY
Estimated Start: Week 2 (with M02)
Trigger: Pilot sprint API integrations + decisions
Expected Pepitas: 10 planned (#21-#30)
```

---

#### 🔄 M04–M10 Modules (0% Each — Skeleton Phase)

```
| Module | Duration | Lessons | Status | Pepitas |
|--------|----------|---------|--------|---------|
| M04 — Gestão de Equipa | 55 min | 4 | 🔄 Skeleton | #24-#26 |
| M05 — Automações e Agents | 55 min | 4 | 🔄 Skeleton | #27-#29 |
| M06 — Vault e Sync | 50 min | 4 | 🔄 Skeleton | #30-#32 |
| M07 — Reporting | 50 min | 4 | 🔄 Skeleton | #33-#35 |
| M08 — Qualidade | 45 min | 4 | 🔄 Skeleton | #36-#38 |
| M09 — Scaling | 54 min | 4 | 🔄 Skeleton | #39-#41 |
| M10 — Infraestrutura | 47 min | 4 | 🔄 Skeleton | #42-#44 |

Total Remaining: 356 minutes (57 lessons)
Estimated Completion Timeline: 8-10 weeks (with concurrent pepita capture)
```

---

### Pepitas System Status

```
📚 PEPITAS TO LESSONS PIPELINE

Pepitas Captured by Module:
  M01: 10 ✅ Approved → Lessons drafted
  M02: 0 ⏳ Planned (start Week 2)
  M03-M10: 0 ⏳ Planned (start Week 2-3)

Total Pipeline:
  Approved & In Lessons: 10 (M01)
  In Draft: 0
  Pending Capture: 28 (M02-M10)

Conversion Rate (Pepita → Lesson):
  Current: 10/10 captured pepitas → 4 lessons (100% drafted)
  Target: 38 pepitas → 61 lessons (100% complete by Week 5)

Quality Gate:
  ✅ All pepitas must be based on real execution (not theory)
  ✅ All pepitas must be actionable (not vague observations)
  ✅ All pepitas must be surprising or non-obvious
  ✅ All pepitas must be reusable across multiple sprints
```

---

### Writing Roadmap

```
📅 LESSON WRITING TIMELINE

Week 1 (Apr 21-27):
  ✅ M01 lesson refinement + quality review
  🔄 M02-M04 skeleton planning + pepita prep
  🔄 Pilot sprint FASE-0 kickoff

Week 2-3 (Apr 28-May 10):
  🔄 M02-M04 lesson writing (12 lessons)
  🔄 Pilot sprint FASE-1 execution → pepita capture
  🔄 M02-M04 pepitas approved (goal: 10)

Week 3-4 (May 5-17):
  🔄 M05-M07 lesson writing (12 lessons)
  🔄 Pilot sprint FASE-1 → FASE-2 transition
  🔄 M05-M07 pepitas captured

Week 4+ (May 18 onwards):
  🔄 M08-M10 lesson writing (12 lessons)
  🔄 Pilot sprint FASE-3 validation
  🔄 Final pepitas compilation

Week 5+ (End-May onwards):
  ✅ All 61 lessons drafted
  ✅ Quality review complete
  ✅ Course live in Obsidian vault
  ⏳ Continuous pepita capture on all future sprints
```

---

### Quality Gates Per Lesson

```
✅ LESSON QUALITY CHECKLIST (Template):

Every lesson in COURSE includes:

Metadata:
  ✅ Level (Beginner / Intermediate / Advanced)
  ✅ Duration (est. mins + actual)
  ✅ Prerequisites (which lessons to take first)
  ✅ Status (Draft / Review / Live)

Content:
  ✅ Learning objectives (3-5 bullet points)
  ✅ Real example (from actual sprint execution, not theory)
  ✅ Step-by-step breakdown
  ✅ Common mistakes (anti-patterns)
  ✅ Actionable takeaway

Validation:
  ✅ Reviewed by pilot sprint team
  ✅ Tested in real context (not just written)
  ✅ Linked to relevant SOPs/FASEs
  ✅ Cross-referenced with pepitas

Completion Criteria:
  ✅ 100% metadata filled
  ✅ Example is real (not hypothetical)
  ✅ Someone could learn & apply this in 1-2 hours
  ✅ Q&A section ready (common questions)
```

---

### Notes & Principles

```
📋 PHILOSOPHY (Non-Negotiable):

1. NOT theoretical course
   ├─ Every lesson comes from real sprint execution
   ├─ Pepitas drive lesson creation (not the reverse)
   └─ If something didn't happen in a sprint, don't teach it

2. Grows continuously
   ├─ Each sprint = 3-5 new pepitas
   ├─ Each pepita = 1 new lesson (eventually)
   └─ Course gets better, not older

3. Stays in sync with operations
   ├─ M01 complete because 45D framework is proven (10 sprints)
   ├─ M02-M10 start after first paid sprint execution
   └─ No lessons written before real execution proves the pattern

4. Replicability is the goal
   ├─ Purpose: teach 100+ people to execute 45D identically
   ├─ Not to get individual people "trained up"
   └─ Success = someone takes this course and runs successful sprint
```

---

## 🔗 Relacionados

- [[COURSE-00-STRUCTURE]] — Master curriculum index
- [[COURSE-PEPITAS-DE-OURO]] — Pepitas that feed lesson creation
- [[TEMPLATE-PEPITA-CAPTURE]] — How to submit new pepitas for lesson conversion

---
