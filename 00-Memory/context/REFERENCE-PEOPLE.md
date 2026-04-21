# People — Squad, Dinâmicas, Alertas Mapeamento de pessoas, responsabilidades, e padrões de comunicação. Atualiza-se conforme dinâmicas evoluem. --- ## 👤 Core Team ### Rui (Founder/PM) **Papel:** Fundador RankPanda, PM de Shopify SEO sprints **Responsabilidades:** Strategic direction, client relationships, architectural decisions, course content **Timezone:** Europe/Lisbon (WET/WEST) **Preferências:**
- PT-PT sempre (não EN)
- Conciso, sem filler, "bloco a bloco"
- APIs diretas, sem MCP complexity
- Focus on automation e performance
- Weekly review de estado atual **Alertas:**
- Se sprint entra em risco (>5% desvio de timeline), escala para Rui imediatamente
- Decisões INVIOLÁVEL devem ser aprovadas por Rui antes de deviation
- Client blockers (acesso técnico, form não preenchido) → notify Rui, não espera --- ### Claude (Operations AI/PM Assistant) **Papel:** Operacionalize 45D Sprint, manage daily execution, monitor metrics **Responsabilidades:** - INÍCIO: Load 8 memory files cada sessão
- TO-DO: Register immediate tasks in ClickUp
- PERIÓDICO: Update metrics hourly (GSC, GA4, Shopify)
- FECHO: Save all context at end of session
- PEPITAS: Capture insights, lessons, discoveries
- Coordinar com technical squad
- Client comms (via Discord, ClickUp comments) **Preferências:**
- Always PT-PT in written comms
- Async-first (Discord, ClickUp, not Slack meetings)
- Direct APIs only (Shopify, GSC, GA4, SE Ranking, ClickUp, Gmail, Calendar, Drive, Leexi)
- Flag blockers immediately, propose solutions **Alertas:**
- Se API integration falha 2x consecutivas, notify Rui + document in lessons.md
- Se cliente não responde a approval gate >2 dias, escalate
- Se metrics mostram regression >10%, pause work + diagnóstico --- ## 🔄 Client Squad (Per Sprint) Template para cada cliente (e.g., pilot-vibradores): ### [Cliente] — Sprint 001 **Client:** [nome] / [contact email] **Owner (Rui):** Responsável por relação **Owner (Technical):** [nome], responsável por Shopify/técnico **Communication:** Discord channel #[client-nome] **Dinâmicas:**
- Approval gates: Cliente responde via Discord/email
- Weekly sync: [Dia/hora], quem participa
- Escalation: Quem contacta se há blockers **Alertas:**
- Slow approval: >3 dias sem feedback = follow-up automático via ClickUp comment + email
- Technical blockers: API auth, Shopify metafields, GSC access = Rui involved imediatamente --- ## 📊 Communication Cadence **Daily:**
- Morning (09:00 PT): Review overnight metrics (GSC, GA4)
- Evening (18:00 PT): Update cliente progress in Discord (3-line format: Done / In Progress / Blocked) **Weekly:**
- Monday: Sprint planning, assignments
- Wednesday: Mid-week check-in (any blockers?)
- Friday: Weekly update (metrics + next week priorities) **Per Phase:**
- FASE 0: Daily kickoff updates
- FASE 1: 3x weekly progress (Seg/Qua/Sex)
- FASE 2: Daily (parallelization needs tight comms)
- FASE 3: 2x weekly (ramp down) --- ## 🎯 Decision Authority | Decisão | Authority | Escalate If |
|---------|-----------|------------|
| Task reassignment | Claude | >1 day impact |
| Timeline slip <2 dias | Claude | >2 dias slip |
| Technical pivot | Claude + Technical | Affects deliverables |
| Client scope change | Rui | Always (ROI impact) |
| Architecture decision | Rui | Always (INVIOLÁVEL gate) | --- **Versão:** 1.0 **Criado:** 2026-04-18 **Próxima revisão:** Após client #1 completo
