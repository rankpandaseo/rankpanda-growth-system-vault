---
name: conceito-shopify-collections
description: Central hub for Shopify collection optimization patterns, metafields, schema, API workflows, and best practices
type: conceito
status: active
foco: technical
tags: [shopify, collections, metafields, schema-org, api, technical-seo]
wikilinks: [[[sop-3-clustering-collection-mapping]], [[fase-2-execution]], [[sop-1-store-context-setup]], [[pilot-vibradores]]]
---

# CONCEITO — Shopify Collections (Hub Agregador)

**Resumo:** Central hub para toda a implementação técnica de collections em Shopify. Agrupa metafields, schema patterns, API workflows, bulk operations e best practices transversais.

---

## 🎯 Propósito deste Hub

Este documento é um **aggregator** para todo o conhecimento de Shopify collections implementation. Quando perguntas:
- "Qual é a estrutura de metafields para collection SEO?"
- "Como implementamos schema.org ProductCollection?"
- "Qual é o fluxo de bulk operations em Shopify?"
- "Como validamos que collection foi publicada corretamente?"

→ Este hub centraliza padrões, workflows e checklists.

---

## 📚 Estrutura Conceptual

### 1. **Fundações — Shopify Collections Anatomy**

**O que é uma Collection em Shopify:**
- Container de products (manual, rule-based, ou hybrid)
- Tem próprio template + metafields (não herda de products)
- Indexável no Google (com canonical, sem blockers)
- Ponteiro semântico (category, tema, atributo)

**Estrutura URL:**
```
mystore.com/collections/[handle]
mystore.com/collections/vibrador-em-silicone
```

**SEO Elements:**
- Title tag (60 chars, keyword-rich) — em metafield
- Meta description (120-155 chars, CTA) — em metafield
- Breadcrumb schema — JSON-LD em template
- Product schema aggregation — Markup de products dentro
- H1 (natural, 1 per page) — em Liquid template

**Referência:** [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Estrutura de collections definida

---

### 2. **Metafields — Data Layer**

**Metafields Obrigatórios para SEO:**

```json
{
  "seo_title": "Vibradores em Silicone | Premium Quality",
  "seo_meta_description": "Vibradores silicone de alta qualidade. Entrega rápida, garantia, discreto.",
  "seo_h1": "Descobrir Vibradores em Silicone de Primeira Qualidade",
  "collection_intro": "Bem-vindo à nossa coleção de vibradores em silicone. Selecionados pelos critérios de qualidade...",
  "collection_cta": "Explorar coleção | Adicionar ao carrinho",
  "keywords_target": "vibrador silicone, vibrador à prova de água, vibrador discreto",
  "indexing_enabled": true
}
```

**Integração com Liquid Template:**
```liquid
<title>{{ collection.metafields.custom.seo_title }}</title>
<meta name="description" content="{{ collection.metafields.custom.seo_meta_description }}">
<h1>{{ collection.metafields.custom.seo_h1 }}</h1>
{{ collection.metafields.custom.collection_intro }}
```

**Workflow de Criação:**
1. Claude gera drafts (title, meta desc, intro, H1)
2. Cliente aprova amostra (5-10 collections)
3. Shopify Admin: criar metafield definitions (1x per store)
4. Bulk API: aplicar valores a todas as collections

**Referência:** [[FASE-2-EXECUTION]] — "Como Fazer Collection Optimization"

---

### 3. **Schema.org — Semantic Markup**

**Schema Patterns por Collection:**

**ProductCollection (Main):**
```json
{
  "@context": "https://schema.org",
  "@type": "ProductCollection",
  "name": "Vibradores em Silicone",
  "description": "Coleção premium de vibradores silicone de alta qualidade",
  "url": "https://mystore.com/collections/vibrador-em-silicone",
  "image": "https://cdn.com/collection-image.jpg",
  "numberOfItems": 42,
  "itemListElement": [
    {
      "@type": "Product",
      "name": "Product 1",
      "url": "...",
      ...
    }
  ]
}
```

**BreadcrumbList (Navigation):**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Home",
      "item": "https://mystore.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Products",
      "item": "https://mystore.com/collections"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Vibradores em Silicone",
      "item": "https://mystore.com/collections/vibrador-em-silicone"
    }
  ]
}
```

**Validação:**
- Use Google Rich Results Test
- Verify JSON-LD is structured data
- Check for errors (missing required fields)

**Implementação:**
- ProductCollection gerada por Claude
- JSON-LD injectado via metafield + Liquid render
- Validado antes de publish

**Referência:** [[FASE-2-EXECUTION]] — Schema validation checklist

---

### 4. **Shopify API — Bulk Operations**

**Workflow de Bulk Apply (Collections):**

```graphql
mutation {
  bulkOperationRunMutation(
    mutation: """
      mutation {
        collectionUpdate(input: {
          id: "gid://shopify/Collection/${{ ID }}",
          metafields: [
            {
              namespace: "custom",
              key: "seo_title",
              value: "${{ SEO_TITLE }}",
              type: "single_line_text_field"
            },
            {
              namespace: "custom",
              key: "seo_meta_description",
              value: "${{ SEO_META_DESC }}",
              type: "multi_line_text_field"
            }
          ]
        }) {
          collection {
            id
            title
          }
          userErrors { field message }
        }
      }
    """
  ) {
    bulkOperation {
      id
      status
    }
  }
}
```

**Execution Timeline:**
1. Prepare CSV: collection_id, seo_title, seo_meta_description, seo_h1, intro
2. Generate GraphQL mutation (per collection)
3. Submit bulk operation
4. Monitor status (typically 5-30 min for 50-100 collections)
5. Verify success (check userErrors)

**Error Handling:**
- Metafield definition missing → Create via Admin API first
- Invalid value type → Re-format (text, number, JSON)
- Rate limit → Queue and retry with delay

**Referência:** [[FASE-2-EXECUTION]] — Task "Publish to Shopify" (Collections)

---

### 5. **QA & Validation Pattern**

**Pre-Publish Checklist:**
- ✅ Metafield definitions created in Shopify
- ✅ Drafts approved by client (5-10 sample collections)
- ✅ JSON-LD schema validated (Rich Results Test)
- ✅ Liquid template renders metafields (local preview)
- ✅ No canonical issues (pointing to self)
- ✅ robots.txt allows crawling

**Post-Publish Validation:**
1. Pick 5-10 published collections
2. Visit in browser: verify title tag, meta desc, H1, intro visible
3. View page source: confirm JSON-LD present + valid
4. GSC: submit for indexing (bulk)
5. IndexNow: notify Google of updates
6. Monitor GSC: track indexation status (24-72h)

**Long-term Monitoring:**
- Weekly GSC check: indexed collections growing
- Monthly GA4 check: collection pages getting traffic
- Quarterly: position tracking (main keywords per collection)

**Referência:** [[FASE-2-EXECUTION]] — QA & Indexation tasks

---

## 🔄 Fluxo Cross-Phase

```
SOP-3 — CLUSTERING & MAPPING
├─ Define which products → which collection
├─ Keyword mapping per collection
└─ Output: collection structure document

FASE-2 — COLLECTION OPTIMIZATION
├─ Generate drafts (Claude): title, meta desc, intro, schema
├─ Client approval sampling (5-10 collections)
├─ Metafields create + bulk apply (Shopify API)
├─ JSON-LD validation + template integration
└─ Publish to Shopify

FASE-2 — INDEXATION
├─ GSC: submit collections for indexing
├─ IndexNow: notify Google
└─ Monitor indexation weekly

FASE-3 — VALIDATION
├─ Measure: collections indexed? Appearing in SERP?
├─ Track: impressions, clicks, position per collection
└─ Analyze: which collections driving most value?
```

---

## 💡 Padrões Replicáveis

### Pattern 1 — Simple Collection (1 day)

**Setup:**
- 1 primary keyword + 2-3 secondary variations
- 20-50 products
- Simple intro paragraph (1-2 sentences)

**Workflow:**
1. Claude: generate title, meta desc, intro, schema
2. Client: approve (1-2 hours turnaround)
3. Metafields: create + apply (30 min)
4. Publish: live immediately

**Result:** Collection rankeando para primary keyword em 2-4 weeks

### Pattern 2 — Clustered Collection (2-3 days)

**Setup:**
- Primary keyword + 5-10 semantic variations
- 50-200 products (rule-based filtering)
- Rich intro (3-5 paras, natural language, no stuffing)
- Sub-filters (size, color, material by product attributes)

**Workflow:**
1. Cluster keywords by intent (Claude analysis)
2. Generate intro per cluster (different angle per sub-collection)
3. Client approval (sampling + feedback)
4. Bulk metafields apply (2 collections at once)
5. JSON-LD aggregation (schema reflects product count accurately)

**Result:** Dominate keyword family (pos 1-10 for 60%+ of cluster variations)

### Pattern 3 — Dynamic Collections (1 week integration)

**Setup:**
- Rule-based collections (automatic product assignment)
- Metafields updated dynamically (inventory-driven titles)
- Auto-refresh product count in schema

**Workflow:**
1. Define collection rules in Shopify (e.g., tag=silicone AND price>$20)
2. Generate base metafields (title template with variable placeholders)
3. Liquid template renders dynamic values (product count, price range)
4. Schema updates automatically as products added/removed

**Result:** Collections stay fresh, SEO signals remain strong as inventory changes

---

## 🛠️ Integração Technical Stack

| Layer | Component | Integration |
|---|---|---|
| **Content** | Metafields (seo_title, seo_meta_description, etc) | Shopify Admin + Bulk API |
| **Template** | Liquid template (renders metafields + schema) | Shopify Theme Editor |
| **Schema** | JSON-LD ProductCollection + BreadcrumbList | Render via metafield in Liquid |
| **API** | GraphQL Bulk Operations | Python/Node mutation calls |
| **Indexing** | GSC + IndexNow | API submissions post-publish |

---

## 📊 Métricas de Sucesso

**Por Collection:**
- Baseline: Position, impressions, clicks (week 1)
- Target: Top 10 for primary keyword (week 4)
- Success: +50% impressions, +25% clicks (week 5 vs week 1)

**Aggregate (All Collections):**
- Collections indexed: Track % of total published
- Collection traffic: % of organic traffic from collections
- Revenue contribution: Sessions × CR × AOV from collection traffic

---

## 🔗 Relacionados

**Documentação que depende deste conceito:**
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] → Define structure de collections + keyword mapping
- [[SOP-1-STORE-CONTEXT-SETUP]] ← Collection context feeds store understanding
- [[FASE-2-EXECUTION]] → Implementação completa de collections (drafts, approval, publish)
- [[FASE-3-VALIDATION]] → Medição de impacto (collections indexed, traffic, conversions)

**Casos Reais:**
- [[pilot-vibradores]] → Implementação end-to-end de collection optimization

**Recursos:**
- `/vault/04-Templates/approval-gate-collections.md` — Template de aprovação
- `/vault/05-Curso-45D/pepitas-de-ouro.md` — Learnings de collections optimization

---

**Versão:** 1.0  
**Data:** 2026-04-21  
**Status:** ACTIVE  
**Próximo:** Integração bidirecional com SOP-3 e FASE-2
