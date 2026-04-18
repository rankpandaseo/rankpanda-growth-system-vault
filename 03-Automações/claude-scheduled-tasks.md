# Claude Scheduled Tasks Configuration

Automated tasks that keep memory system, course generator, and todo tracking running 24/7.

---

## Task 1 — Weekly Memory Context Update

**Purpose:** Update memory files with current project status, new learnings.

**Schedule:** Every Monday 9:00 AM (cron: `0 9 * * 1`)

**Prompt:**

```
Review the past week's vault changes (check git log).
Update memory files:
1. Update project_45d_framework.md with any new patterns discovered
2. Update feedback_foundation_priority.md if priorities shifted
3. Check if new integrations were added; update reference_external_systems.md
4. Note any new decisions in memory files (create new if needed)

Files to update: /memory/*.md
Check git log in vault for changes in past 7 days.
Commit changes to memory/ folder.
```

---

## Task 2 — Pepitas de Ouro Capture

**Purpose:** Synthesize learnings from vault updates into golden insights.

**Schedule:** Every Friday 5:00 PM (cron: `0 17 * * 5`)

**Prompt:**

```
Check vault folder: 02-SOPs/ and any sprint memory folders (/memory/projects/).
Look for:
- "Learnings:" comments
- "Surprise discovery:" notes
- "Next time:" suggestions
- "Time saver:" shortcuts

Compile these into pepita format:
---
## Pepita: [descriptive title]
**Context:** [when/where this happened]
**Learning:** [the insight]
**How to apply:** [actionable next time]
---

Add to: /vault/05-Curso-PM-com-IA/pepitas-de-ouro.md
Max 10 pepitas per week.
Organize by category (KW research, collections, products, technical, client, etc).
```

---

## Task 3 — Course Module Synthesis

**Purpose:** Auto-generate course lessons from accumulated pepitas and SOP experience.

**Schedule:** Every 2 weeks Monday 10:00 AM (cron: `0 10 */2 * 1`)

**Prompt:**

```
Review pepitas-de-ouro.md and recent SOP executions.
Check which course modules need new lessons based on learnings.

For next module with incomplete lessons:
1. Read pepitas related to that module's topic
2. Read relevant SOP docs (02-SOPs/)
3. Generate 1-2 new lesson outlines

Format:
### Lição X.Y — [Title]
**Duration:** [estimated minutes]
**Prerequisites:** [previous lessons]
**Learning outcomes:** 
- [ ] Outcome 1
- [ ] Outcome 2
**Content:**
[lesson outline]
**Practical exercise:**
[what to do to practice this]

Add to: /vault/05-Curso-PM-com-IA/M0X/

Update MODULE_STATUS in 00-STRUCTURE.md
```

---

## Task 4 — Sprint Status Tracking

**Purpose:** Monitor active sprints, update todo.md, notify on blockers.

**Schedule:** Every weekday 8:00 AM (cron: `0 8 * * 1-5`)

**Prompt:**

```
For any active sprint (check /memory/projects/ folders):
1. Read ClickUp space status (if we have API access)
2. Check Vault for phase-specific notes
3. Identify blockers or risks
4. Update todo.md:
   - Mark completed tasks
   - Note any blockers
   - Update timeline if needed

Send Discord notification:
- Sprint name
- Current phase
- This week's priorities
- Any blockers

Format:
**[Loja Name] Sprint Status**
Phase: FASE X (Y% complete)
This week: [key activities]
Blockers: [if any]
Metrics: [current state vs baseline]
```

---

## Task 5 — Github Repo Health Check

**Purpose:** Ensure vault sync and code repos are healthy.

**Schedule:** Every day 6:00 AM (cron: `0 6 * * *`)

**Prompt:**

```
Check:
1. rankpanda-growth-system repo: latest commit time, branch status
2. rankpanda-growth-system-vault repo: latest commit time, branch status
3. Any unmerged branches older than 7 days?
4. Any failing CI/CD pipelines?

Report to Discord:
- Repo status (green/yellow/red)
- Latest commits
- Any stale branches

If critical: send alert to geral@rankpanda.pt
```

---

## Task 6 — Anthropic Updates Integration

**Purpose:** Weekly fetch of latest Claude/API updates, integrate into course.

**Schedule:** Every Friday 11:00 AM (cron: `0 11 * * 5`)

**Prompt:**

```
Check Anthropic's GitHub releases and blog:
1. anthropics/claude-code releases
2. anthropics/anthropic-sdk releases
3. Claude API changelog

Look for:
- New features we should know about
- Breaking changes we should prepare for
- Best practices updates

Create pepita if finding is surprising/relevant:
## Pepita: [Anthropic Update]
**Source:** [link to release]
**What changed:** [summary]
**How we use it:** [impact on our system]
**Action:** [if any needed]

If major update: create meeting task in ClickUp "Review Anthropic update: [feature]"
```

---

## Task 7 — Monthly Review & Roadmap Update

**Purpose:** Look back on month, update strategy, plan next month.

**Schedule:** First Monday of month, 9:00 AM (cron: `0 9 1 * *`)

**Prompt:**

```
Monthly retrospective:
1. Sprints completed: [count and names]
2. Learnings captured: [count]
3. Course modules updated: [count]
4. Automations added: [count]

Update todo.md:
- Move completed items to ✅
- Add new priorities for next month
- Adjust timeline if needed
- Update blocking dependencies

Create monthly summary for memory:
File: memory/monthly-summaries/YYYY-MM.md
Include:
- Sprints executed
- Key learnings
- Automations built
- Metrics (sprints per week, course growth, etc)
- What's next for next month

Send to Discord: Monthly progress report
```

---

## Setup Instructions

### 1. Create Scheduled Tasks in Claude Code

Using Claude Code's memory system at:
```
/Users/rankpanda/.claude/projects/-Users-rankpanda-Shopify-RankPanda-APP---Oficial-2026/
```

Each task becomes a `.md` file in the `.claude/scheduled-tasks/` directory.

### 2. Example Task File

Create: `.claude/scheduled-tasks/weekly-memory-update.md`

```markdown
---
name: Weekly Memory Context Update
description: Update memory files with project status and learnings
type: scheduled-task
schedule: "0 9 * * 1"  # Every Monday 9 AM
recurring: true
durable: true
---

[Task prompt content here]
```

### 3. Environment Variables

Add to `.env`:

```
CLAUDE_SCHEDULED_TASKS_ENABLED=true
VAULT_PATH=/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault
MEMORY_PATH=/Users/rankpanda/.claude/projects/-Users-rankpanda-Shopify-RankPanda-APP---Oficial-2026/memory
GITHUB_VAULT_REPO=rankpandaseo/rankpanda-growth-system-vault
GITHUB_GROWTH_REPO=rankpandaseo/rankpanda-growth-system
DISCORD_WEBHOOK_UPDATES=https://discord.com/api/webhooks/...
```

---

## Manual Execution

If needed, trigger tasks manually:

```bash
# Check scheduled tasks
claude code tasks list

# Run specific task
claude code tasks run weekly-memory-update

# View task history
claude code tasks history
```

---

## Monitoring

**Discord channel for task status:**

Each task should report:
- ✅ Task completed
- ⚠️ Task with warnings (e.g., no changes found)
- ❌ Task failed (investigation needed)

**Example messages:**

```
✅ Weekly Memory Update
Updated: project_45d_framework.md, reference_external_systems.md
Lines changed: 47
Committed: 2 files to memory/

⚠️ Pepitas Capture
No new learnings found this week. Review ongoing sprints?

❌ GitHub Repo Health
rankpanda-growth-system: Latest commit 5 days old
Action: Check if development stalled or pushing directly to main
```

---

## Debugging Failed Tasks

If a task fails:

1. **Check logs:** Discord notification will have error details
2. **Review prompt:** Make sure task prompt is clear and executable
3. **Test manually:** Run task prompt in Claude Code directly
4. **Update:** Fix and re-deploy task

---

**Version:** 1.0  
**Status:** Ready for Implementation  
**Owner:** RankPanda AI System
