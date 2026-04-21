---
name: fase-2-execution
description: Execute keyword research, collection optimization, and product
optimization in parallel with client approval gates
type: fase
status: active
foco: operational
tags: [execution, keyword-research, collections, products, parallelization]
wikilinks: [[FASE-1-DIAGNOSTIC]], [[SOP-2-KEYWORD-RESEARCH-V2]],
[[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-3-VALIDATION]],
[[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# SOP FASE 2 — Execução Cirúrgica (Semana 2-4)

**Resumo:** Implementar keyword research, otimizar collections e produtos em paralelo (3 streams independentes) com approval gates estruturados e sincronização via ClickUp.

---

## 🎯 Por Que Isto Importa

- **Parallelização real:** 3 streams (keywords, collections, products) correm em simultâneo. Sem isto, tudo corre sequencial (3x mais lento).
- **Approval gates estruturados:** Antes de cada grande passo (coleções, product descriptions), cliente aprova. Evita retrabalho.
- **Sincronização via ClickUp:** Todos na mesma página. Não há "eu pensava que fazíamos X".

---

## ⚡ Quick Checklist

- ← [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — **Input:** Clusters e mapping de collections definidos --- ## ⚡ Quick Checklist - [ ] KW research draft completo (SE Ranking + GSC + Claude)
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
- [ ] Ready for [[FASE-3-VALIDATION]] --- ## 🔑 Key Principles 1. **Parallelization with Clarity:** Cada stream é independente, mas dependencies claras em ClickUp. Ninguém fica bloqueado.
- [ ] Cliente aprovou 5-10 coleções principais
- [ ] Tom de voz validado
- [ ] Objetivos de volume/posição estabelecidos
- [ ] SE Ranking API respondendo
- [ ] GSC data acessível **Collection Optimization (Semana 2-3):**
- [ ] 5-10 coleções identificadas para otimizar
- [ ] Draft review process definido
- [ ] Shopify metafields configurados
- [ ] Client approval gate estruturado **Product Optimization (Semana 2-4):**
- [ ] Batches de 20-50 produtos definidas
- [ ] Product sampling process (5-10 para client review)
- [ ] Bulk API permissions validadas
- [ ] QA process definido **Technical Setup (Semana 2-3):**
- [ ] Metafields dinâmicos criados
- [ ] Schema.org templates prontos
- [ ] Liquid templates testadas (se necessário)
- [ ] IndexNow ativado
- [ ] GA4 refinement completo ### Gaps Identificados _Se algum gap aparecer durante execução:_ **Gap:** [description]
- Daily standup review --- ## Execução: ClickUp Space + Tarefas ### ClickUp Space Structure (FASE 2) **Project:** `[Loja] — 45D Sprint → FASE 2 Execution` **Using Templates:** See `/04-Templates/` for approval-gate-keywords.md, approval-gate-collections.md, approval-gate-products.md, and weekly-update-template.md **Folders:** 1. **KW RESEARCH** - [ ] Coleções target confirmadas - [ ] KW research draft done - [ ] Client review sent - [ ] Client approved - [ ] Learnings documented 2. **COLLECTION OPTIMIZATION** - [ ] Drafts generated for each collection - [ ] Client review sent - [ ] Client approved - [ ] Published to Shopify - [ ] GSC submission done - [ ] Monitoring started 3. **PRODUCT OPTIMIZATION (Batch 1-N)** - [ ] Batch scope defined (products, collection) - [ ] Drafts generated - [ ] Client sampling review sent - [ ] Client approved - [ ] Bulk applied - [ ] QA validation - [ ] GSC submission done 4. **TECHNICAL SETUP** - [ ] Metafields created + tested - [ ] Schema.org templates validated - [ ] Liquid templates updated (if needed) - [ ] IndexNow activated + tested - [ ] GA4 refinement done - [ ] Robots.txt checked 5. **COMMUNICATION & MONITORING** - [ ] Weekly update (Loom/email) - [ ] Client checkpoint calls - [ ] Metrics tracking ### Tarefas Específicas (KW Research) #### Task 1 — Generate KW Research

---

## 📖 Conteúdo Principal

2. **Approval Sampling:** Não pedimos approval em 100 produtos. Aprovamos padrão
em 5-10. Depois aplicamos.
3. **Bulk over Manual:** Shopify API bulk operations (não manual edits). 50
produtos aplicados em 1-2h, não 20h.
4. **Weekly Beats:** Cliente vê progresso toda a sexta. Zero surpresas. Feedback
loop rápido.
5. **Technical Parallel:** Setup técnico não é blocker. Enquanto fazemos KW,
configuramos schema/metafields. --- ## Operacional: AUDITORIA (Weak Points
Detection) ### Checklist de Execução **KW Research (Semana 2):**
1. Coleções aprovadas (handle + nome)
2. Tom de voz cliente
3. Objetivos (volume, position, tipo de intent) **Workflow:**
1. **Para cada coleção:** - SE Ranking: extrair keywords com volume + difficulty
- GSC: keywords actuais que já rankeiam (aproveitamos) - Análise: agrupar por
intent (commercial, informational) - Claude: gerar keywords adicionais baseado
em análise 2. **Estruturar briefing:** - Top 3 primary keywords (main target) -
5-10 secondary keywords (supporting) - Long-tail variations - Search volumes +
difficulty scores 3. **Client approval:** - Enviar form com keywords propostas -
Cliente aprova ou pede ajustes - Guardar em vault + database **Output:**
`[loja]/kw-research.md` no vault com tudo documentado ### Como Fazer Collection
Optimization (Semana 2-3) **Para cada coleção:** 1. **Generate drafts
(Claude):** - Title: 50-60 chars, keyword-rich, conversão-oriented - Meta
description: 120-155 chars, CTA implicit - Introduction: 2-3 parágrafos, natural
language, keywords - Schema: ProductCollection + BreadcrumbList (JSON-LD) 2.
**Draft review com cliente:** - Enviar form com drafts - Cliente comenta/aprova
(turnaround: 2-3 dias) - Guardar versão aprovada 3. **Publicar no Shopify:** -
Usar Shopify metafields (não inline content) - Template Liquid lê metafields -
Publicar em batch 4. **Indexation push:** - GSC: submit for indexing - IndexNow:
notify - Monitor impressões/clicks por 2 semanas **Output:** Collections
publicadas + spreadsheet de status ### Como Fazer Product Optimization (Semana
2-4) **Workflow em batches:** 1. **Preparar batch (20-50 produtos):** -
Selecionar por coleção - Validar que têm imagens, descrição, etc 2. **Gerar
drafts (Claude):** - Title: 70-80 chars, keyword-rich - Introduction/Summary:
100-150 chars - Title tag (metafield): 55-60 chars - Meta description
(metafield): 120-155 chars - Schema: Product + Offer (JSON-LD) 3. **Client
sampling review:** - Escolher 5-10 produtos representativos - Cliente aprova
amostra (ou pede ajustes) - Aplicar feedback a resto do batch 4. **Bulk apply
via Shopify API:** - Usar bulk operations API - Aplicar em 1-2 horas - Validar
que aplicou corretamente 5. **Monitor indexation:** - GSC: check que produtos
aparecem - IndexNow: push updates **Output:** X produtos publicados + tracking
spreadsheet ### Como Sincronizar Streams Paralelamente **Timeline:**
```
Semana 2: [KW Research] Draft → Client Review [Collections] Draft → Client
Review [Tech Setup] Metafields, Schema, IndexNow Semana 3: [KW Research] Final
(client approved) [Collections] Publish → GSC Submit → Monitor [Products Batch1]
Draft → Client Review [Tech Setup] Finalizar, testes Semana 4: [Collections]
Monitor indexation [Products B1-B3] Publish → GSC Submit → Monitor [Reporting]
Prepare metrics, learnings
``` **Coordenação via ClickUp:**

---

## 🔗 Relacionados

- [[FASE-1-DIAGNOSTIC]] — Pré-requisito: diagnóstico concluído + oportunidades identificadas
- [[SOP-2-KEYWORD-RESEARCH-V2]] — Stream 1: keyword research em paralelo
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Stream 2: collection optimization
- [[FASE-3-VALIDATION]] — Próxima fase: validação + go-live

---
