---
name: automation-claude-scheduled-tasks
description: Claude Scheduled Tasks Configuration. Automated tasks that keep memory system, course generator, and todo tracking running 24/7.
type: automation
status: active
foco: operational
tags: [automation, script, scheduled-tasks]
wikilinks: []
---

# Automation — Claude Scheduled Tasks

**Resumo:** Configuration for automated tasks that run on schedule to keep the RankPanda system running 24/7, including memory updates, course generation, and todo tracking.

---

## 🎯 Por Que Isto Importa

- **Persistence:** Memory system stays current without manual sync
- **Automation:** New pepitas and learnings automatically feed the course
- **Scalability:** Todo tracking and updates happen on schedule, not ad-hoc
- **Proactivity:** System learns and improves autonomously
- **Reliability:** Critical workflows run reliably on schedule

---

## ⚡ Quick Checklist

- [ ] Task 1: Memory Context Update (Monday 9:00 AM)
- [ ] Task 2: Pepitas of Oro Collection (Weekly)
- [ ] Task 3: Course Module Synthesis (Every 2 weeks)
- [ ] Verify cron expressions are valid
- [ ] Test each task in dry-run mode

---

## 📖 Conteúdo Principal

### Task 1 — Weekly Memory Context Update

**Purpose:** Update memory files with current project status and new learnings  
**Schedule:** Every Monday 9:00 AM (cron: `0 9 * * 1`)  
**Scope:**
- Read `memoria/sessions/estado-atual.md`
- Summarize key decisions made last week
- Update `memoria/context/decisions.md` if new rules emerged
- Update `memoria/context/lessons.md` if failures occurred
- Commit to Git

### Task 2 — Weekly Pepitas Collection

**Purpose:** Aggregate new learnings and insights into course material  
**Schedule:** Every Friday (cron: `0 9 * * 5`)  
**Scope:**
- Scan `/vault/05-Curso-45D/pepitas-de-ouro.md`
- Organize by category (KW research, collections, products, technical, client)
- Max 10 pepitas per week
- Format each pepita with: Context, Learning, How to Apply

### Task 3 — Course Module Synthesis

**Purpose:** Auto-generate course lessons from pepitas and SOP experience  
**Schedule:** Every 2 weeks Monday 10:00 AM (cron: `0 10 */2 * 1`)  
**Scope:**
1. Review pepitas related to current module topic
2. Review relevant SOPs from `/vault/02-SOPs/`
3. Generate new lesson outlines for incomplete modules
4. Format: `### Lição X.Y — [Title]` with Duration, Prerequisites, Content

---

## 🔗 Relacionados

- [[SOP-VAULT-FORMAT-SPECIFICATION]] — Document standards
- [[pepitas-de-ouro]] — Course material source
- [[estado-atual]] — Current session state
