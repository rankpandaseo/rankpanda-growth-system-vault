---
name: conceito-client-approval
description: Central hub for client approval workflows, sampling patterns,
feedback loops, and decision gates across 45D sprint
type: conceito
status: active
foco: operational
tags: [client-approval, sampling, feedback-loop, decision-gate, governance]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]],
[[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-2-EXECUTION]],
[[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# CONCEITO — Client Approval (Hub Agregador)

**Resumo:** Central hub para toda a estratégia de aprovação de cliente no 45D Sprint. Agrupa sampling patterns, feedback loops, decision gates e governance workflows que ocorrem em múltiplas FASEs.

---

## 🎯 Por Que Isto Importa

- **Sampling não é aprovação de 100%:** Aprovamos amostra de 5-10 items de 100. Cliente valida padrão, não cada detalhe. Isto acelera 10x: 2 dias em vez de 20.
- **2-round max, depois lock-in:** Iteração 1, feedback; Iteração 2, final. Terceira ronda? Não existe. RankPanda locks-in padrão e bulk-applies. Impacto: sprint fica on-track, não negociação infinita.
- **Escalation path clara:** Se cliente rejeita padrão, síncrono call (30 min), alinha direção, re-testa uma amostra, procede. Impacto: evita impasse, resolve em 3-4 dias.

---

## ⚡ Quick Checklist

- [ ] Approval form template (Google Form) preparado
- [ ] Amostra de 5-10 items pronta (representativa do padrão)
- [ ] Feedback form enviado ao cliente
- [ ] Turnaround esperado: 48h (cliente comenta)
- [ ] Iteração 1: feedback incorporado, new amostra enviada
- [ ] Iteração 2: cliente aprova ou rejeita padrão
- [ ] Se rejeição: escalation call (30 min) para alinhar direção
- [ ] Padrão locked-in → bulk apply autorizado

---

## 📖 Conteúdo Principal

Dia 1-2: RankPanda gera 5-10 drafts ↓
Dia 3-4: Envia form ao cliente (Google Form ou similar) ↓
Dia 5-6: Cliente comenta/aprova (48h turnaround) ↓
Dia 7: RankPanda incorpora feedback
``` **Form Obrigatório:**
```
Dia 7: RankPanda lê feedback ↓
Dia 8-9: Gera nova versão (aplica feedback, mantém padrão) ↓
Dia 10: Envia revisão ao cliente ↓
Dia 11: Cliente aprova OR pede novo ajuste
``` **Limite de Iterações:** Máximo 2 rounds. Se cliente ainda não aprova:
```
Dia 12: RankPanda aprova pattern como "locked-in" ↓
Dia 13-14: Bulk apply a resto (20-200 items) ↓
Dia 15: QA validation (spot-check 5-10 items on live site) ↓
Dia 16: Confirma com cliente: "Tudo live, verificar site"
``` **Não existe 3ª approval de bulk aplicado.** Cliente já aprovou padrão.
```
Cliente: "Gosto desta abordagem. Aplicar a todos."
RankPanda: Procede com bulk apply (3 dias)
Timeline: Sem iteração, sprint fica on-track
``` **Scenario 2 — Cliente pede ajuste minor (comum)**
```
Cliente: "Ótimo, mas pode ser mais casual no tone?"
RankPanda: Gera nova versão com tone casual
Cliente: "Perfeito, aplicar a todos."
Timeline: 1 iteração, sprint fica 2 dias mais lento
``` **Scenario 3 — Cliente rejeita padrão (raro, mas possível)**
```
Cliente: "Isto não encaixa. Nada que propuseram."
RankPanda: Escalate call (síncrono) - Clarify: o que cliente quer ver? - Propor
2-3 alternativas diferentes - Testar uma no amostra
Cliente: Aprova alternativa
RankPanda: Continua com novo padrão
Timeline: 3-4 dias de atraso
``` **Escalation Path (Se iteração 2 não converge):**
1. RankPanda SEO lead calls cliente (síncrono)
2. Demonstra 2-3 alternativas diferentes
3. Cliente escolhe direção preferida
4. Gera nova amostra (1 item apenas, quick validation)
5. Procede com bulk apply (pattern locked) --- ### 5. **Communication Format —
Forms & Validation** **Approval Form Template (Google Form / Typeform):**
```
Title: "Aprovação de [Keywords / Collections / Products] — [Loja Name]" Section
1 — Preview
[Visual preview of 5-10 items with formatting clearly visible] Section 2 —
Feedback
``` **Alternative: Async Review (Loom Video)**
1. Form para feedback estruturado
2. Loom video + call síncrono para objecções (scenario 3 acima) --- ## 🔄 Fluxo
Cross-Phase ```
FASE-1 — DIAGNOSTIC (não há approval cliente ainda)
└─ RankPanda identifica 3-5 oportunidades └─ Prepara estratégia (sem commitment
cliente) FASE-2 — EXECUTION (múltiplos approval gates)
├─ SOP-2: Keywords approval
│ ├─ RankPanda: gera 50 keywords
│ ├─ Sampling: apresenta 5-10 ao cliente
│ ├─ Cliente: aprova padrão
│ └─ RankPanda: locks-in keywords.json
│
├─ SOP-3: Collections approval │ ├─ RankPanda: gera 10-20 collections
│ ├─ Sampling: apresenta 5-10 drafts ao cliente
│ ├─ Cliente: aprova padrão (tone, structure, keywords)
│ └─ RankPanda: bulk applies metafields
│
└─ Products approval ├─ RankPanda: gera 50-100 product titles/descriptions ├─
Sampling: apresenta 5-10 ao cliente ├─ Cliente: aprova padrão (keywords, tone,
length) └─ RankPanda: bulk applies via Shopify API FASE-3 — VALIDATION (cliente
vê prova de impacto)
└─ RankPanda: apresenta before/after metrics └─ Cliente: decide continuidade
(90D roadmap)
``` --- ## 💡 Padrões Replicáveis ### Pattern 1 — Quick Approval (3 dias) **Setup:** Cliente com high trust, low complexity
1. Draft 5 items (any from batch)
2. Send form (async)
3. Cliente aprova em 24h (típico)
4. Bulk apply (2 days)
5. Total: 3 dias --- ### Pattern 2 — Iterative Approval (7 dias) **Setup:**
Cliente com concerns, wants fine-tuning
1. Draft 5-8 items (cover variety)
2. Send form (async)
3. Cliente comenta (48h)
4. RankPanda revisa (1 dia)
5. Send revised amostra
6. Cliente aprova (24h)
7. Bulk apply (2 dias)
8. Total: 7 dias --- ### Pattern 3 — Escalated Approval (10+ dias) **Setup:**
Cliente com strong preferences, needs alignment
1. Draft amostra
2. Cliente rejeita (sends feedback)
3. RankPanda lead calls cliente (30 min síncrono)
4. Align on direction (one specific approach)
5. Re-draft amostra (novo padrão)
6. Cliente aprova (24h)
7. Bulk apply (2 dias)
8. Total: 10+ dias --- ## 🛠️ Integração com Governance **Documentação de
Aprovações:**

---

## 🔗 Relacionados

- [[SOP-2-KEYWORD-RESEARCH-V2]] — Keyword approval é gate 1 em FASE-2
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Collection approval é gate 2 em FASE-2
- [[FASE-2-EXECUTION]] — Product approval é gate 3 (com sampling)

---
