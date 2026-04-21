---
name: fase-2-execution
description: Execute keyword research, collection optimization, and product optimization in parallel with client approval gates
type: fase
status: active
foco: execução
tags: [execution, keyword-research, collections, products, parallelization]
wikilinks: [[[FASE-1-DIAGNOSTIC]], [[SOP-2-KEYWORD-RESEARCH-V2]], [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-3-VALIDATION]], [[pilot-vibradores]]]
---

# SOP FASE 2 — Execução Cirúrgica (Semana 2-4)

**Resumo:** Implementar keyword research, otimizar collections e produtos em paralelo (3 streams independentes) com approval gates estruturados e sincronização via ClickUp.

---

## 🎯 Por Que Isto Importa

**Impacto na velocidade e qualidade da implementação:**
- **Parallelização com guardrails:** 3 streams (KW, Collections, Products) rodam em paralelo, reduzindo 21 dias para 14-18. Sem guardrails = caos, conflitos, retrabalho.
- **Approval gates:** Cliente aprova amostra (5-10 produtos) antes de aplicarmos 50+. Uma vez aprovado o padrão, aplicamos em bulk com segurança.
- **Technical foundation:** Schema, metafields, IndexNow ativados em paralelo = quando publicamos (dia 9), Google já está pronto a indexar.
- **Weekly communication:** Cliente vê progresso (Loom videos, relatórios). Mantém confiança, permite feedback rápido.

**Sem FASE 2 bem estruturada:** Fazemos tudo sequencial, publicamos tudo ao mesmo tempo, descobrimos problemas em mass, 5 dias perdidos em refactoring.

---

## 📋 Pré-requisitos

Antes de começar FASE-2:
- ← [[FASE-1-DIAGNOSTIC]] — **Input Obrigatório:** Diagnóstico completo (gaps identificados, oportunidades priorizadas)
- ← [[SOP-2-KEYWORD-RESEARCH-V2]] — **Input:** Keywords aprovadas por cliente
- ← [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — **Input:** Clusters e mapping de collections definidos

---

## ⚡ Quick Checklist

- [ ] KW research draft completo (SE Ranking + GSC + Claude)
- [ ] KW briefing form aprovado por cliente
- [ ] Collection drafts gerados (title, meta desc, intro, schema)
- [ ] Collection approval form aprovado por cliente
- [ ] Product batches definidos (20-50 produtos por batch)
- [ ] Product sample (5-10) aprovado por cliente
- [ ] Metafields Shopify criados e testados
- [ ] Schema.org templates validados (ProductCollection, Product, BreadcrumbList)
- [ ] Liquid templates atualizados (se necessário)
- [ ] IndexNow ativado e testado
- [ ] Todas as colecções e produtos publicados no Shopify
- [ ] GSC submissions completos
- [ ] Monitorização iniciada (impressões, clicks, indexação)
- [ ] Ready for [[FASE-3-VALIDATION]]

---

## 🔑 Key Principles

1. **Parallelization with Clarity:** Cada stream é independente, mas dependencies claras em ClickUp. Ninguém fica bloqueado.
2. **Approval Sampling:** Não pedimos approval em 100 produtos. Aprovamos padrão em 5-10. Depois aplicamos.
3. **Bulk over Manual:** Shopify API bulk operations (não manual edits). 50 produtos aplicados em 1-2h, não 20h.
4. **Weekly Beats:** Cliente vê progresso toda a sexta. Zero surpresas. Feedback loop rápido.
5. **Technical Parallel:** Setup técnico não é blocker. Enquanto fazemos KW, configuramos schema/metafields.

---

## Operacional: AUDITORIA (Weak Points Detection)

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

## Como Fazer KW Research (Semana 2)

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

## Execução: ClickUp Space + Tarefas

### ClickUp Space Structure (FASE 2)

**Project:** `[Loja] — 45D Sprint → FASE 2 Execution`

**Using Templates:** See `/04-Templates/` for approval-gate-keywords.md, approval-gate-collections.md, approval-gate-products.md, and weekly-update-template.md

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

## Validação & Entregáveis

- ✅ KW research completo + approved by client
- ✅ 5-10 collections optimized + published + indexed
- ✅ 50-100+ products optimized + published + indexed
- ✅ Technical setup completo (schema, metafields, IndexNow)
- ✅ Weekly communication com cliente (Loom videos, relatórios)
- ✅ Vault updated com learnings + pepitas de ouro

---

## 🔗 Relacionados

**Dependências & Fluxo Sequencial:**
- [[FASE-1-DIAGNOSTIC]] ← **Input:** Diagnóstico orienta priorização de FASE 2
- [[SOP-2-KEYWORD-RESEARCH-V2]] ← **Input:** Keywords aprovadas
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] ← **Input:** Mapping de collections
- [[FASE-3-VALIDATION]] → **Próximo:** Validação de rankings, tráfego, conversão

**Conceitos Transversais (Hubs):**
- [[CONCEITO-Keyword-Research]] ↔ **Implementação:** Keywords research metodologia
- [[CONCEITO-Shopify-Collections]] ↔ **Implementação:** Estrutura + metafields + schema de collections
- [[CONCEITO-Client-Approval]] ↔ **Governança:** Approval gates para keywords, collections, products
- [[API-REGISTRY]] ↔ **Integração:** Shopify API bulk operations + GSC submissions

**Exemplos & Referência:**
- [[pilot-vibradores]] → **Caso Real:** Execução ao vivo com 3 streams paralelos

---

**Versão:** 2.0  
**Data:** 2026-04-21  
**Status:** ATIVO  
**Próximo:** [[FASE-3-VALIDATION]] (após indexação)
