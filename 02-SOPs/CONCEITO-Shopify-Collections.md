---
name: conceito-shopify-collections
description: Central hub for Shopify collection optimization patterns,
metafields, schema, API workflows, and best practices
type: conceito
status: active
foco: technical
tags: [shopify, collections, metafields, schema-org, api, technical-seo]
wikilinks: [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-2-EXECUTION]],
[[SOP-1-STORE-CONTEXT-SETUP-v2]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# CONCEITO — Shopify Collections (Hub Agregador) **Resumo:** Central hub para toda a implementação técnica de collections em Shopify. Agrupa metafields, schema patterns, API workflows, bulk operations e best practices transversais. --- ## 🎯 Propósito deste Hub Este documento é um **aggregator** para todo o conhecimento de Shopify collections implementation. Quando perguntas:

**Resumo:** CONCEITO — Shopify Collections (Hub Agregador) **Resumo:** Central
hub para toda a implementação técnica de collections em Shopify. Agrupa
metafields, schema patterns, API workflows, bulk operations e best practices
transversais. --- ## 🎯 Propósito deste Hub Este documento é um **aggregator**
para todo o conhecimento de Shopify collections implementation. Quando
perguntas:

---

## 🎯 Por Que Isto Importa

[Adiciona contexto: impacto direto no projeto, porquê isto importa]
- Ponto 1
- Ponto 2
- Ponto 3

---

## ⚡ Quick Checklist

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

---

## 📖 Conteúdo Principal

```
mystore.com/collections/[handle]
mystore.com/collections/vibrador-em-silicone
``` **SEO Elements:**
{ "seo_title": "Vibradores em Silicone | Premium Quality", "seo_meta_description": "Vibradores silicone de alta qualidade. Entrega rápida, garantia, discreto.", "seo_h1": "Descobrir Vibradores em Silicone de Primeira Qualidade", "collection_intro": "Bem-vindo à nossa coleção de vibradores em silicone. Selecionados pelos critérios de qualidade...", "collection_cta": "Explorar coleção | Adicionar ao carrinho", "keywords_target": "vibrador silicone, vibrador à prova de água, vibrador discreto", "indexing_enabled": true
}
``` **Integração com Liquid Template:**
```liquid
<title>{{ collection.metafields.custom.seo_title }}</title>
<meta name="description" content="{{
collection.metafields.custom.seo_meta_description }}">
<h1>{{ collection.metafields.custom.seo_h1 }}</h1>
{{ collection.metafields.custom.collection_intro }}
``` **Workflow de Criação:**
1. Claude gera drafts (title, meta desc, intro, H1)
2. Cliente aprova amostra (5-10 collections)
3. Shopify Admin: criar metafield definitions (1x per store)
4. Bulk API: aplicar valores a todas as collections **Referência:**
[[FASE-2-EXECUTION]] — "Como Fazer Collection Optimization" --- ### 3.
**Schema.org — Semantic Markup** **Schema Patterns por Collection:**
**ProductCollection (Main):**
```json
{ "@context": "https://schema.org", "@type": "ProductCollection", "name":
"Vibradores em Silicone", "description": "Coleção premium de vibradores silicone
de alta qualidade", "url":
"https://mystore.com/collections/vibrador-em-silicone", "image":
"https://cdn.com/collection-image.jpg", "numberOfItems": 42, "itemListElement":
[ { "@type": "Product", "name": "Product 1", "url": "...", ... } ]
}
``` **BreadcrumbList (Navigation):**
```json
{ "@context": "https://schema.org", "@type": "BreadcrumbList",
"itemListElement": [ { "@type": "ListItem", "position": 1, "name": "Home",
"item": "https://mystore.com" }, { "@type": "ListItem", "position": 2, "name":
"Products", "item": "https://mystore.com/collections" }, { "@type": "ListItem",
"position": 3, "name": "Vibradores em Silicone", "item":
"https://mystore.com/collections/vibrador-em-silicone" } ]
}
``` **Validação:**
mutation { bulkOperationRunMutation( mutation: """ mutation {
collectionUpdate(input: { id: "gid://shopify/Collection/${{ ID }}", metafields:
[ { namespace: "custom", key: "seo_title", value: "${{ SEO_TITLE }}", type:
"single_line_text_field" }, { namespace: "custom", key: "seo_meta_description",
value: "${{ SEO_META_DESC }}", type: "multi_line_text_field" } ] }) { collection
{ id title } userErrors { field message } } } """ ) { bulkOperation { id status
} }
}
``` **Execution Timeline:**
1. Prepare CSV: collection_id, seo_title, seo_meta_description, seo_h1, intro
2. Generate GraphQL mutation (per collection)
3. Submit bulk operation
4. Monitor status (typically 5-30 min for 50-100 collections)
5. Verify success (check userErrors) **Error Handling:**
1. Pick 5-10 published collections
2. Visit in browser: verify title tag, meta desc, H1, intro visible
3. View page source: confirm JSON-LD present + valid
4. GSC: submit for indexing (bulk)
5. IndexNow: notify Google of updates
6. Monitor GSC: track indexation status (24-72h) **Long-term Monitoring:**
SOP-3 — CLUSTERING & MAPPING
├─ Define which products → which collection
├─ Keyword mapping per collection
└─ Output: collection structure document FASE-2 — COLLECTION OPTIMIZATION
├─ Generate drafts (Claude): title, meta desc, intro, schema
├─ Client approval sampling (5-10 collections)
├─ Metafields create + bulk apply (Shopify API)
├─ JSON-LD validation + template integration
└─ Publish to Shopify FASE-2 — INDEXATION
├─ GSC: submit collections for indexing
├─ IndexNow: notify Google
└─ Monitor indexation weekly FASE-3 — VALIDATION
├─ Measure: collections indexed? Appearing in SERP?
├─ Track: impressions, clicks, position per collection
└─ Analyze: which collections driving most value?
``` --- ## 💡 Padrões Replicáveis ### Pattern 1 — Simple Collection (1 day) **Setup:**
1. Claude: generate title, meta desc, intro, schema
2. Client: approve (1-2 hours turnaround)
3. Metafields: create + apply (30 min)
4. Publish: live immediately **Result:** Collection rankeando para primary
keyword em 2-4 weeks ### Pattern 2 — Clustered Collection (2-3 days) **Setup:**
1. Cluster keywords by intent (Claude analysis)
2. Generate intro per cluster (different angle per sub-collection)
3. Client approval (sampling + feedback)
4. Bulk metafields apply (2 collections at once)
5. JSON-LD aggregation (schema reflects product count accurately) **Result:**
Dominate keyword family (pos 1-10 for 60%+ of cluster variations) ### Pattern 3
— Dynamic Collections (1 week integration) **Setup:**
1. Define collection rules in Shopify (e.g., tag=silicone AND price>$20)
2. Generate base metafields (title template with variable placeholders)
3. Liquid template renders dynamic values (product count, price range)
4. Schema updates automatically as products added/removed **Result:** Collections stay fresh, SEO signals remain strong as inventory changes --- ## 🛠️ Integração Technical Stack | Layer | Component | Integration |
|---|---|---|
| **Content** | Metafields (seo_title, seo_meta_description, etc) | Shopify Admin + Bulk API |
| **Template** | Liquid template (renders metafields + schema) | Shopify Theme Editor |
| **Schema** | JSON-LD ProductCollection + BreadcrumbList | Render via metafield in Liquid |
| **API** | GraphQL Bulk Operations | Python/Node mutation calls |
| **Indexing** | GSC + IndexNow | API submissions post-publish | --- ## 📊 Métricas de Sucesso **Por Collection:**

---

## 🔗 Relacionados

- [[Related-Doc-1]] — descrição
- [[Related-Doc-2]] — descrição

---
