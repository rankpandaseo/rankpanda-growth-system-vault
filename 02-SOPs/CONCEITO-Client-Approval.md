---
name: conceito-client-approval
description: Central hub for client approval workflows, sampling patterns, feedback loops, and decision gates across 45D sprint
type: conceito
status: active
foco: operational
tags: [client-approval, sampling, feedback-loop, decision-gate, governance]
wikilinks: [[[SOP-2-KEYWORD-RESEARCH-V2]], [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-2-EXECUTION]], [[pilot-vibradores]]]
---

# CONCEITO — Client Approval (Hub Agregador)

**Resumo:** Central hub para toda a estratégia de aprovação de cliente no 45D Sprint. Agrupa sampling patterns, feedback loops, decision gates e governance workflows que ocorrem em múltiplas FASEs.

---

## 🎯 Propósito deste Hub

Este documento é um **aggregator** para todo o conhecimento de client approval transversal. Quando perguntas:
- "Como estruturamos approval de keywords?"
- "Qual é o padrão de sampling (não pedimos approval em 100 items)?"
- "Como é o feedback loop com cliente?"
- "Quando cliente diz 'não', como iteramos?"

→ Este hub centraliza padrões, timelines e escalation paths.

---

## 📚 Estrutura Conceptual

### 1. **Fundações — Por Que Sampling, Não Full Approval?**

**Problema sem Sampling:**
- Pedimos cliente aprovar 100 keywords = 1 semana esperando resposta
- Pedimos cliente aprovar 50 collections = cliente sobrecarregado, approva sem ler
- Pedimos cliente aprovar 200 products = impossível revisar qualidade

**Solução: Approval by Pattern (Sampling):**
- Selecionar 5-10 items REPRESENTATIVOS
- Cliente aprova pattern (não cada item)
- Uma vez pattern aprovado: aplicar em bulk a resto (20-200 items)
- Resultado: 3 dias de feedback instead of 1 semana

**Benefício para Cliente:**
- Menos overhead (5 items vs 100)
- Mais qualidade (pode ler cuidadosamente)
- Mais confiança (vê que padrão é bom antes de aplicar em massa)

**Benefício para RankPanda:**
- Velocidade: não bloqueados esperando approval
- Clarity: cliente vê exatamente o que espera
- Replicabilidade: padrão aprovado = zero surprises em bulk apply

---

### 2. **Workflow Padrão — 3 Gates**

**Gate 1 — Draft Approval (Amostra pequena)**

```
Dia 1-2: RankPanda gera 5-10 drafts
           ↓
Dia 3-4: Envia form ao cliente (Google Form ou similar)
           ↓
Dia 5-6: Cliente comenta/aprova (48h turnaround)
           ↓
Dia 7:   RankPanda incorpora feedback
```

**Form Obrigatório:**
- Visual preview (title, meta desc, intro visíveis)
- Comment field (cliente escreve feedback)
- Approve/Reject toggle
- Optional: revisão sugerida (cliente propõe alternativa)

**Output:**
- Cliente approva pattern OR pede revisão (iteração 1-2x)
- RankPanda documenta decisão (guardar form screenshot no vault)

---

**Gate 2 — Feedback Incorporation (Iteração)**

Se cliente pede ajustes:
```
Dia 7:   RankPanda lê feedback
           ↓
Dia 8-9: Gera nova versão (aplica feedback, mantém padrão)
           ↓
Dia 10:  Envia revisão ao cliente
           ↓
Dia 11:  Cliente aprova OR pede novo ajuste
```

**Limite de Iterações:** Máximo 2 rounds. Se cliente ainda não aprova:
- Escalate to RankPanda owner + cliente sync call
- Clarify: o que exatamente precisa de mudança?
- Agree on direction (compromisso)

---

**Gate 3 — Pattern Lock-In (Bulk Apply)**

Uma vez aprovado (amostra 5-10 items):
```
Dia 12:  RankPanda aprova pattern como "locked-in"
           ↓
Dia 13-14: Bulk apply a resto (20-200 items)
           ↓
Dia 15:  QA validation (spot-check 5-10 items on live site)
           ↓
Dia 16:  Confirma com cliente: "Tudo live, verificar site"
```

**Não existe 3ª approval de bulk aplicado.** Cliente já aprovou padrão.
- Se encontra problema em QA → fix antes de publicar
- Se encontra problema após publicar → rápido fix (1-2 horas)

---

### 3. **Sampling Patterns — Como Escolher Amostra?**

**Critério de Representatividade:**

**Keywords (5-10 amostras):**
- 2-3 HIGH volume (principal targets)
- 2-3 MEDIUM volume (supporting)
- 2-3 LONG-TAIL (niche variations)
- Mix de intent types (transactional, informational)

**Collections (5-10 amostras):**
- 2-3 HIGH priority (maior tráfego potencial)
- 2-3 MEDIUM complexity (typical case)
- 1-2 Edge cases (muito niche, ou muito genérico)
- Mix de tamanho (10 products vs 100 products)

**Products (5-10 amostras):**
- 2-3 HIGH value (caro, popular)
- 2-3 MEDIUM value (típico)
- 2-3 LOW value (cheap, niche)
- Mix de categoria (diferentes collections)

**Regra de Ouro:** Se cliente aprova padrão em amostra representativa, assume-se que 90% do bulk apply será aceitável.

---

### 4. **Feedback Loop — Como Gerir Objecções**

**Scenario 1 — Cliente aprova padrão (mais comum)**
```
Cliente: "Gosto desta abordagem. Aplicar a todos."
RankPanda: Procede com bulk apply (3 dias)
Timeline: Sem iteração, sprint fica on-track
```

**Scenario 2 — Cliente pede ajuste minor (comum)**
```
Cliente: "Ótimo, mas pode ser mais casual no tone?"
RankPanda: Gera nova versão com tone casual
Cliente: "Perfeito, aplicar a todos."
Timeline: 1 iteração, sprint fica 2 dias mais lento
```

**Scenario 3 — Cliente rejeita padrão (raro, mas possível)**
```
Cliente: "Isto não encaixa. Nada que propuseram."
RankPanda: Escalate call (síncrono)
  - Clarify: o que cliente quer ver?
  - Propor 2-3 alternativas diferentes
  - Testar uma no amostra
Cliente: Aprova alternativa
RankPanda: Continua com novo padrão
Timeline: 3-4 dias de atraso
```

**Escalation Path (Se iteração 2 não converge):**
1. RankPanda SEO lead calls cliente (síncrono)
2. Demonstra 2-3 alternativas diferentes
3. Cliente escolhe direção preferida
4. Gera nova amostra (1 item apenas, quick validation)
5. Procede com bulk apply (pattern locked)

---

### 5. **Communication Format — Forms & Validation**

**Approval Form Template (Google Form / Typeform):**
```
Title: "Aprovação de [Keywords / Collections / Products] — [Loja Name]"

Section 1 — Preview
[Visual preview of 5-10 items with formatting clearly visible]

Section 2 — Feedback
- "Qual é o seu feedback geral?" [Long text]
- "Há algo que gostaria de mudar?" [Multiple choice]
  ◯ Tone of voice
  ◯ Keywords focus
  ◯ Structure/format
  ◯ Length
  ◯ Other: [specify]

Section 3 — Decision
- "Aprova este padrão para aplicar em bulk?" 
  ◯ Yes, apply to all
  ◯ Make changes, then apply
  ◯ Reject, start over

Section 4 — Optional Suggestions
- "Se desejar, pode sugerir uma versão alternativa aqui" [Long text]

Timeline: "Favor responder até [DATE]. Confirme que recebeu."
```

**Alternative: Async Review (Loom Video)**
- RankPanda grava Loom (5 min): "Aqui está amostra. Isto é o padrão que vamos aplicar. O que acha?"
- Cliente responde via email ou form
- Mais barato que call síncrono, melhor que form unidireccional

**Best Practice:** Usar AMBOS:
1. Form para feedback estruturado
2. Loom video + call síncrono para objecções (scenario 3 acima)

---

## 🔄 Fluxo Cross-Phase

```
FASE-1 — DIAGNOSTIC (não há approval cliente ainda)
└─ RankPanda identifica 3-5 oportunidades
   └─ Prepara estratégia (sem commitment cliente)

FASE-2 — EXECUTION (múltiplos approval gates)
├─ SOP-2: Keywords approval
│  ├─ RankPanda: gera 50 keywords
│  ├─ Sampling: apresenta 5-10 ao cliente
│  ├─ Cliente: aprova padrão
│  └─ RankPanda: locks-in keywords.json
│
├─ SOP-3: Collections approval  
│  ├─ RankPanda: gera 10-20 collections
│  ├─ Sampling: apresenta 5-10 drafts ao cliente
│  ├─ Cliente: aprova padrão (tone, structure, keywords)
│  └─ RankPanda: bulk applies metafields
│
└─ Products approval
   ├─ RankPanda: gera 50-100 product titles/descriptions
   ├─ Sampling: apresenta 5-10 ao cliente
   ├─ Cliente: aprova padrão (keywords, tone, length)
   └─ RankPanda: bulk applies via Shopify API

FASE-3 — VALIDATION (cliente vê prova de impacto)
└─ RankPanda: apresenta before/after metrics
   └─ Cliente: decide continuidade (90D roadmap)
```

---

## 💡 Padrões Replicáveis

### Pattern 1 — Quick Approval (3 dias)

**Setup:** Cliente com high trust, low complexity
- Keywords: all similar volume/intent
- Collections: straightforward categories
- Products: consistent quality/positioning

**Workflow:**
1. Draft 5 items (any from batch)
2. Send form (async)
3. Cliente aprova em 24h (típico)
4. Bulk apply (2 days)
5. Total: 3 dias

---

### Pattern 2 — Iterative Approval (7 dias)

**Setup:** Cliente com concerns, wants fine-tuning
- Keywords: different intent mixes (precisa feedback on one)
- Collections: different tones (cliente wants consistency check)
- Products: varies by category (cliente wants approval per category)

**Workflow:**
1. Draft 5-8 items (cover variety)
2. Send form (async)
3. Cliente comenta (48h)
4. RankPanda revisa (1 dia)
5. Send revised amostra
6. Cliente aprova (24h)
7. Bulk apply (2 dias)
8. Total: 7 dias

---

### Pattern 3 — Escalated Approval (10+ dias)

**Setup:** Cliente com strong preferences, needs alignment
- Keywords: cliente acha que keywords estão errados
- Collections: cliente quer muito diferente approach
- Products: cliente rejeita tone completamente

**Workflow:**
1. Draft amostra
2. Cliente rejeita (sends feedback)
3. RankPanda lead calls cliente (30 min síncrono)
4. Align on direction (one specific approach)
5. Re-draft amostra (novo padrão)
6. Cliente aprova (24h)
7. Bulk apply (2 dias)
8. Total: 10+ dias

---

## 🛠️ Integração com Governance

**Documentação de Aprovações:**
- Guardar form screenshot no vault (`/vault/01-Clientes/[cliente]/approvals/`)
- Filename: `approval-keywords-[date].png` ou `approval-collections-[date].json`
- Reference em ClickUp task (attach screenshot)

**Audit Trail:**
- Cada approval forms parte do contrato (prova de cliente sign-off)
- Se dispute futuro: "Veja, cliente aprovou exatamente isto no [date]"

**Escalation Log:**
- Se houve iteração 2+: document why
- Serve como learning (para próximo cliente similar)
- Pepita de ouro: "Cliente [X] prefers casual tone. Remember para próxima vez."

---

## 📊 Métricas de Sucesso

**Por Gate:**
- **Approval Speed:** Quantas horas até cliente responder? (Target: <48h)
- **Iterations:** Quantos rounds de feedback? (Target: 1-2)
- **Satisfaction:** Cliente aprova final padrão? (Target: 95%+)

**Aggregate:**
- **Timeline Adherence:** Approval gates on-track? (Target: 100%)
- **Rework:** % de items que precisaram revisão pós-approval (Target: <5%)
- **Client NPS:** Aprovação smooth → confiança → NPS ↑

---

## 🔗 Relacionados

**SOPs que usam approval gates:**
- [[SOP-2-KEYWORD-RESEARCH-V2]] ← "Client approval" is sequential gate
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] ← Clustering aprovado por cliente
- [[FASE-2-EXECUTION]] → Múltiplos approval gates (KW, collections, products)

**Templates & Recursos:**
- `/vault/04-Templates/approval-gate-keywords.md` — Keyword approval form
- `/vault/04-Templates/approval-gate-collections.md` — Collection approval form
- `/vault/04-Templates/approval-gate-products.md` — Product approval form

**Casos Reais:**
- [[pilot-vibradores]] → Exemplo end-to-end de approval workflow real

---

**Versão:** 1.0  
**Data:** 2026-04-21  
**Status:** ACTIVE  
**Próximo:** Integração bidirecional com SOP-2, SOP-3, FASE-2
