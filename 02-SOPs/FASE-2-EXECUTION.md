# SOP FASE 2 — Execução Cirúrgica (Semana 2-4)

## 🎯 Objetivo

Corrigir essencial para indexação, visibilidade e estrutura semântica. Implementação paralela em 3 streams: KW Research, Collections, Products.

---

## CAMADA 1 — AUDITORIA (Weak Points Detection)

### Checklist de Execução

**KW Research (Semana 2):**
- [ ] Cliente aprovou 5-10 coleções principais
- [ ] Tom de voz validado
- [ ] Objetivos de volume/posição estabelecidos
- [ ] SE Ranking API respondendo
- [ ] GSC data acessível

**Collection Optimization (Semana 2-3):**
- [ ] 5-10 coleções identificadas para otimizar
- [ ] Draft review process definido
- [ ] Shopify metafields configurados
- [ ] Client approval gate estruturado

**Product Optimization (Semana 2-4):**
- [ ] Batches de 20-50 produtos definidas
- [ ] Product sampling process (5-10 para client review)
- [ ] Bulk API permissions validadas
- [ ] QA process definido

**Technical Setup (Semana 2-3):**
- [ ] Metafields dinâmicos criados
- [ ] Schema.org templates prontos
- [ ] Liquid templates testadas (se necessário)
- [ ] IndexNow ativado
- [ ] GA4 refinement completo

### Gaps Identificados

_Se algum gap aparecer durante execução:_

**Gap:** [descrição]
- **Blocker?** [sim/não]
- **Solução:** [o que fazer]
- **Impact na timeline:** [dias]

---

## CAMADA 2 — FORMATIVO (How-To / Teaching Module)

### Porque Execução Precisa Ser Bem Estruturada

Execução sem estrutura = caos:
- Conflitos entre streams (ambos tentando escrever products)
- Client review delays (drafts não prontos no tempo)
- QA failures (coisas publicadas com erros)
- Metrics ruins (schema mal implementado)
- Retrabalho

**Princípio:** Parallelização com guardrails. Cada stream independente, com approval gates claros.

### Como Fazer KW Research (Semana 2)

**Inputs necessários:**
1. Coleções aprovadas (handle + nome)
2. Tom de voz cliente
3. Objetivos (volume, position, tipo de intent)

**Workflow:**
1. **Para cada coleção:**
   - SE Ranking: extrair keywords com volume + difficulty
   - GSC: keywords actuais que já rankeiam (aproveitamos)
   - Análise: agrupar por intent (commercial, informational)
   - Claude: gerar keywords adicionais baseado em análise

2. **Estruturar briefing:**
   - Top 3 primary keywords (main target)
   - 5-10 secondary keywords (supporting)
   - Long-tail variations
   - Search volumes + difficulty scores

3. **Client approval:**
   - Enviar form com keywords propostas
   - Cliente aprova ou pede ajustes
   - Guardar em vault + database

**Output:** `[loja]/kw-research.md` no vault com tudo documentado

### Como Fazer Collection Optimization (Semana 2-3)

**Para cada coleção:**

1. **Generate drafts (Claude):**
   - Title: 50-60 chars, keyword-rich, conversão-oriented
   - Meta description: 120-155 chars, CTA implicit
   - Introduction: 2-3 parágrafos, natural language, keywords
   - Schema: ProductCollection + BreadcrumbList (JSON-LD)

2. **Draft review com cliente:**
   - Enviar form com drafts
   - Cliente comenta/aprova (turnaround: 2-3 dias)
   - Guardar versão aprovada

3. **Publicar no Shopify:**
   - Usar Shopify metafields (não inline content)
   - Template Liquid lê metafields
   - Publicar em batch

4. **Indexation push:**
   - GSC: submit for indexing
   - IndexNow: notify
   - Monitor impressões/clicks por 2 semanas

**Output:** Collections publicadas + spreadsheet de status

### Como Fazer Product Optimization (Semana 2-4)

**Workflow em batches:**

1. **Preparar batch (20-50 produtos):**
   - Selecionar por coleção
   - Validar que têm imagens, descrição, etc

2. **Gerar drafts (Claude):**
   - Title: 70-80 chars, keyword-rich
   - Introduction/Summary: 100-150 chars
   - Title tag (metafield): 55-60 chars
   - Meta description (metafield): 120-155 chars
   - Schema: Product + Offer (JSON-LD)

3. **Client sampling review:**
   - Escolher 5-10 produtos representativos
   - Cliente aprova amostra (ou pede ajustes)
   - Aplicar feedback a resto do batch

4. **Bulk apply via Shopify API:**
   - Usar bulk operations API
   - Aplicar em 1-2 horas
   - Validar que aplicou corretamente

5. **Monitor indexation:**
   - GSC: check que produtos aparecem
   - IndexNow: push updates

**Output:** X produtos publicados + tracking spreadsheet

### Como Sincronizar Streams Paralelamente

**Timeline:**
```
Semana 2:
  [KW Research]     Draft → Client Review
  [Collections]     Draft → Client Review
  [Tech Setup]      Metafields, Schema, IndexNow

Semana 3:
  [KW Research]     Final (client approved)
  [Collections]     Publish → GSC Submit → Monitor
  [Products Batch1] Draft → Client Review
  [Tech Setup]      Finalizar, testes

Semana 4:
  [Collections]     Monitor indexation
  [Products B1-B3]  Publish → GSC Submit → Monitor
  [Reporting]       Prepare metrics, learnings
```

**Coordenação via ClickUp:**
- Cada stream tem sua própria folder
- Dependencies marcadas
- Daily standup review

---

## CAMADA 3 — TEMPLATE ClickUp (Operational Tasks)

### ClickUp Space Structure (FASE 2)

**Project:** `[Loja] — 45D Sprint → FASE 2 Execution`

**Folders:**

1. **KW RESEARCH**
   - [ ] Coleções target confirmadas
   - [ ] KW research draft done
   - [ ] Client review sent
   - [ ] Client approved
   - [ ] Learnings documented

2. **COLLECTION OPTIMIZATION**
   - [ ] Drafts generated for each collection
   - [ ] Client review sent
   - [ ] Client approved
   - [ ] Published to Shopify
   - [ ] GSC submission done
   - [ ] Monitoring started

3. **PRODUCT OPTIMIZATION (Batch 1-N)**
   - [ ] Batch scope defined (products, collection)
   - [ ] Drafts generated
   - [ ] Client sampling review sent
   - [ ] Client approved
   - [ ] Bulk applied
   - [ ] QA validation
   - [ ] GSC submission done

4. **TECHNICAL SETUP**
   - [ ] Metafields created + tested
   - [ ] Schema.org templates validated
   - [ ] Liquid templates updated (if needed)
   - [ ] IndexNow activated + tested
   - [ ] GA4 refinement done
   - [ ] Robots.txt checked

5. **COMMUNICATION & MONITORING**
   - [ ] Weekly update (Loom/email)
   - [ ] Client checkpoint calls
   - [ ] Metrics tracking

### Tarefas Específicas (KW Research)

#### Task 1 — Generate KW Research
- **Assignee:** [RankPanda SEO]
- **Due:** Day 3-4
- **Description:** Use SE Ranking + GSC + Claude to generate keywords per collection. Document in Vault.
- **Dependencies:** Client approved collections (FASE 1)

#### Task 2 — Structure KW Briefing
- **Assignee:** [RankPanda SEO]
- **Due:** Day 5
- **Description:** Create approval form with top keywords, search volumes, difficulty scores.
- **Dependencies:** Task 1

#### Task 3 — KW Client Review
- **Assignee:** [RankPanda owner]
- **Due:** Day 5-7
- **Description:** Send form to client. Manage feedback. Document approvals.
- **Dependencies:** Task 2

#### Task 4 — Finalize & Document
- **Assignee:** [RankPanda SEO]
- **Due:** Day 8
- **Description:** Incorporate client feedback. Store approved keywords. Move to PHASE 2 execution.
- **Dependencies:** Task 3

### Tarefas Específicas (Collections)

#### Task 1 — Generate Collection Drafts
- **Assignee:** [RankPanda content]
- **Due:** Day 3-4
- **Description:** Use Claude to generate title, meta desc, intro, schema for each collection.
- **Dependencies:** KW research finalized

#### Task 2 — Structure Collection Review
- **Assignee:** [RankPanda content]
- **Due:** Day 5
- **Description:** Create approval form with drafts (title, intro, meta desc visible).
- **Dependencies:** Task 1

#### Task 3 — Collection Client Review
- **Assignee:** [RankPanda owner]
- **Due:** Day 5-7
- **Description:** Send form to client. Manage feedback/approvals.
- **Dependencies:** Task 2

#### Task 4 — Publish to Shopify
- **Assignee:** [RankPanda tech]
- **Due:** Day 8-9
- **Description:** Apply approved content to Shopify (metafields). Bulk operations API.
- **Dependencies:** Task 3

#### Task 5 — GSC Submission & Indexation
- **Assignee:** [RankPanda tech]
- **Due:** Day 9-10
- **Description:** Submit collections to GSC. Activate IndexNow. Start monitoring.
- **Dependencies:** Task 4

#### Task 6 — Monitor Indexation (2 weeks)
- **Assignee:** [RankPanda analytics]
- **Due:** Ongoing until Day 18
- **Description:** Weekly check GSC impressions/clicks. Document learnings.
- **Dependencies:** Task 5

### Tarefas Específicas (Products - Batch Pattern)

#### Task 1 — Define Batch Scope
- **Assignee:** [RankPanda owner]
- **Due:** Day 4
- **Description:** Choose 20-50 products from approved collection. Create list.
- **Dependencies:** Collections approved

#### Task 2 — Generate Product Drafts
- **Assignee:** [RankPanda content]
- **Due:** Day 5-6
- **Description:** Use Claude to generate title, intro, tags, desc for each product. Bulk output.
- **Dependencies:** Task 1

#### Task 3 — Sampling Review
- **Assignee:** [RankPanda owner]
- **Due:** Day 6-7
- **Description:** Select 5-10 products. Send to client for sampling approval.
- **Dependencies:** Task 2

#### Task 4 — Client Sampling Review
- **Assignee:** [RankPanda owner]
- **Due:** Day 7-9
- **Description:** Gather client feedback on sample. Iterate.
- **Dependencies:** Task 3

#### Task 5 — Bulk Apply
- **Assignee:** [RankPanda tech]
- **Due:** Day 9-10
- **Description:** Apply approved products via Shopify bulk operations API.
- **Dependencies:** Task 4

#### Task 6 — QA Validation
- **Assignee:** [RankPanda tech]
- **Due:** Day 10-11
- **Description:** Spot-check 5-10 products on live site. Verify schema, content appears.
- **Dependencies:** Task 5

#### Task 7 — Indexation Push
- **Assignee:** [RankPanda tech]
- **Due:** Day 11
- **Description:** GSC submission. IndexNow activation. Start monitoring.
- **Dependencies:** Task 6

#### Task 8 — Monitor Indexation
- **Assignee:** [RankPanda analytics]
- **Due:** Ongoing
- **Description:** Weekly check indexation status. Document.
- **Dependencies:** Task 7

### Weekly Communication Task

#### Task — Weekly Update (Every Friday)
- **Assignee:** [RankPanda owner]
- **Due:** Fridays Day 7, 14, 21
- **Description:** Record Loom with progress: collections live, products optimized, metrics so far. Send to client.
- **Dependencies:** Ongoing work

---

## ✅ Entregáveis Fase 2

1. ✅ KW research completo + approved by client
2. ✅ 5-10 collections optimized + published + indexed
3. ✅ 50-100+ products optimized + published + indexed
4. ✅ Technical setup completo (schema, metafields, IndexNow)
5. ✅ Weekly communication com cliente
6. ✅ Vault updated com learnings + pepitas de ouro

---

**Versão:** 1.0  
**Última Atualização:** [data]  
**Owner:** [nome]
