# Memory Index — RankPanda Growth System

Persistent context that enables Claude to maintain project awareness and become increasingly proactive.

---

## 📋 Structure

```
00-Memory/
├── context/          ← Business rules, decisions, team info
├── projects/         ← Client-specific state (grows with sprints)
├── feedback/         ← Inviolable rules that guide decisions
└── integrations/     ← Resource indices and maps
```

---

## 🔗 Quick Links

### Context (How We Work)
- `context/decisions.md` — Inviolable architectural decisions (APIs diretas, 45D Sprint, Vault como fonte, Auto-scaffold)
- `context/people.md` — Squad members, responsibilities, communication cadence, authority matrix
- `context/lessons.md` — Critical learnings that can't repeat (Shopify rate limiting, GSC data lag, GA4 tracking, ClickUp dependencies)

### Projects (What We're Building)
- `projects/pilot-vibradores.md` — Sprint 001: Vibradores dropshipping pilot

### Feedback (Rules That Don't Change)
- `feedback/foundation-priority.md` — Build foundation before features
- `feedback/minimalism.md` — Use ClickUp + Discord, not complex dashboards

### Integrations (Where Things Live)
- `integrations/external-systems.md` — ClickUp, Discord, Shopify, GSC, GA4, SE Ranking API endpoints
- `integrations/vault-map.md` — Where files live in the vault

### Automations (Scripts in /03-Automações/)
- `onboarding-scaffold.py` — Processes kickoff-briefing-form.md → creates memory/projects/[cliente].md + pending.md
- `metrics-aggregator.py` — Daily metric collection orchestrator (calls all API clients)
- `api_clients.py` — Base classes for GSC, GA4, Shopify, SE Ranking clients (credentials from GitHub vault)

---

## 🔄 Update Cadence

- **Weekly:** Context updates with new learnings
- **Per Sprint:** Project files updated with phase progress
- **End of Sprint:** Feedback and decision updates
- **Monthly:** Comprehensive retrospective

---

## 🎯 Purpose

This memory system enables:
1. **Continuity** — Each session starts with full project context
2. **Proactivity** — Claude anticipates problems and proposes solutions
3. **Learning** — Org learnings persist across projects
4. **Scaling** — New sprints reference what worked before

---

**Version:** 1.0  
**Updated:** 2026-04-18  
**Owner:** RankPanda AI System
