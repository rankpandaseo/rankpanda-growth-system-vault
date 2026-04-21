---
name: sop-3-clustering-collection-mapping
description: Group keywords by intent type and map to Shopify collections to
create navigable store structure
type: sop
status: active
foco: seo
tags: [clustering, collections, shopify-structure, keyword-mapping]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[SOP-1-STORE-CONTEXT-SETUP-v2]],
[[FASE-2-EXECUTION]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# SOP 3 — Clustering + Collection Mapping **Resumo:** Agrupar keywords por tipo de intenção/conteúdo e mapear para Shopify collections — criar estrutura navegável e implementável. --- ## 🎯 Por Que Isto Importa **Impacto direto em SEO:**

**Resumo:** SOP 3 — Clustering + Collection Mapping **Resumo:** Agrupar keywords
por tipo de intenção/conteúdo e mapear para Shopify collections — criar
estrutura navegável e implementável. --- ## 🎯 Por Que Isto Importa **Impacto
direto em SEO:**

---

## 🎯 Por Que Isto Importa

[Adiciona contexto: impacto direto no projeto, porquê isto importa]
- Ponto 1
- Ponto 2
- Ponto 3

---

## ⚡ Quick Checklist

- ← [[SOP-2-KEYWORD-RESEARCH-V2]] — **Input Obrigatório:** Keywords finalizadas em keywords.json (com scoring, SERP data, revenue potential). Clustering depende 100% deste output. --- ## ⚡ Quick Checklist - [ ] keywords.json (SOP 2 output) carregado
- [ ] Cluster types definidos (7 tipos: categoria, feature, marca, preço, informacional, localização, long-tail)
- [ ] Claude clustering executado (agrupa keywords em ~20-30 clusters semânticos)
- [ ] Collection structure esboçado (main + sub-collections)
- [ ] Primary keywords atribuído a cada cluster
- [ ] Child keywords + variações mapeadas
- [ ] collection_map.json gerado
- [ ] shopify_collection_structure.md criado
- [ ] Validação: 0 canibalizações, cada keyword em 1 cluster apenas
- [ ] Ready for --- ## 🔑 Key Principles 1. **One Keyword, One Home:** Cada keyword mapeia para EXATAMENTE uma collection/página. Evita cannibalização.
- [ ] SOP 2 output (`keywords.json`) disponível
- [ ] Store context (industria, categories, AOV, CR) validado
- [ ] Timeline e fases (FASE 1, 2, 3) alinhadas com cliente ### Execução
- [ ] Claude clustering executado
- [ ] Validação de coesão de clusters (manual review)
- [ ] Collection mapping decidido
- [ ] Meta titles e descriptions redigidas
- [ ] Blog content strategy definida ### Validação
- [ ] 100% de keywords clustered
- [ ] Nenhum keyword em 2 clusters (exclusividade)
- [ ] Cada cluster tem ≥ 3 keywords (coesão)
- [ ] Collections viáveis (≥ 3 produtos esperados por collection)
- [ ] Blog strategy definida (≥ 3 posts informativos) ### Output Final
- [ ] `collection_map.json` salvo
- [ ] `shopify_collection_structure.md` pronto para implementação Shopify
- [ ] Handed off para SOP 4 (On-Page Optimization) --- ## Próximas Etapas 1. **SOP 4:** On-Page Optimization (aplicar keywords em product titles, meta descriptions, H1, body)

---

## 📖 Conteúdo Principal

2. **Semantic Clustering:** Agrupa não por string matching, mas por intenção de
utilizador (ex: "vibrador recargável" + "vibrador impermeável" = mesmo cluster
FEATURE, público = pessoas que querem conveniência).
3. **Shopify-Native:** Clusters transformam-se em collections reais. Não teórico
— implementável 1:1 em Shopify.
4. **Collection Hierarchy:** Main collection (CATEGORIA) pode ter
sub-collections (FEATURE + PREÇO). Estrutura navigável.
5. **Reverse Map:** Qual é a "landing page" ideal para "vibrador clítoris"?
Collection "Vibradores Clítoris" ou artigo "Guia de Vibradores Clítoris"? --- ##
📖 Cluster Types (Taxonomia) Cada keyword encaixa em UM dos seguintes cluster
types: ### 1. CATEGORIA (Category)
**Definição:** Keywords que definem categorias principais de produtos.
**Exemplo:** "vibrador clítoris", "vibrador ponto G", "masturbadores",
"vibradores premium"
**Características:**
**Definição:** Keywords focadas em atributos específicos.
**Exemplo:** "vibrador recargável", "vibrador impermeável", "vibrador
silencioso", "vibrador wireless"
**Características:**
**Definição:** Keywords de marca própria ou concorrentes.
**Exemplo:** "BrandX vibrador", "vibrador similar a BrandX", "alternativa a
BrandX"
**Características:**
**Definição:** Keywords orientadas por preço/budget.
**Exemplo:** "vibrador barato", "vibrador premium", "vibrador até €50"
**Características:**
**Definição:** Keywords com intent educacional/informacional.
**Exemplo:** "como usar vibrador", "melhores vibradores 2026", "vibrador
recomendado", "guia de vibradores"
**Características:**
**Definição:** Keywords com componente geográfico.
**Exemplo:** "vibrador em Lisboa", "comprar vibrador Porto", "loja vibradores
Portugal"
**Características:**
**Definição:** Keywords muito específicas ou conversacionais.
**Exemplo:** "qual é o melhor vibrador para iniciantes", "vibrador clítoris é
seguro", "vibrador com mais modos"
**Características:**
Tu és especialista em clustering de keywords para ecommerce de vibradores. Aqui
estão {N} keywords com metadados (volume, difficulty, semantic variations,
categoria recomendada): [keywords.json content] Tarefa: Agrupar keywords em
clusters. Para CADA keyword, determina:
1. **Cluster Type** (categoria, feature, marca, preço, informacional,
localização, long-tail)
2. **Cluster Name** (nome semântico do grupo)
3. **Primary Keyword** (a mais importante do cluster)
4. **Child Keywords** (variações + long-tail relacionadas)
5. **Collection Recommendation** (qual collection Shopify) Critérios de
clustering:
{ "clusters": [ { "cluster_id": "c_001", "cluster_type": "categoria",
"cluster_name": "Vibradores para Clítoris", "primary_keyword": "vibrador
clítoris", "search_volume_primary": 800, "child_keywords": [ { "keyword":
"vibrador clitoriano", "type": "semantic_variation", "volume": NULL }, {
"keyword": "vibrador clítoris recargável", "type": "long_tail_child", "volume":
120 }, { "keyword": "melhor vibrador clítoris", "type": "long_tail_child",
"volume": 80 } ], "estimated_monthly_revenue": 45, "effort_category":
"easy_quick_win", "priority_phase": "FASE 1", "recommended_collection":
"Vibradores Clítoris", "recommended_page_type": "categoria + filtro",
"content_strategy": "Category page com sub-filtros (recargável, material,
marca)" }, ... ]
}
``` ### Etapa 2: Validation & Deduplication
|-------------|------------------|---------|
| CATEGORIA | Collection principal | Collection: "Vibradores Clítoris" |
| FEATURE | Sub-collection OU filtro | Sub: "Recargáveis", "Impermeáveis", "Silenciosos" |
| MARCA | Página especial OU descartado | Página: "Marcas de Confiança" (se estratégia inclui) |
| PREÇO | Filtro automático em todas | Tag/Metafield: price_range |
| INFORMACIONAL | Blog/Knowledge Base | Blog posts que linkam para produtos |
| LOCALIZAÇÃO | Descartado (pilot é online only) | — |
| LONG-TAIL | Parte de cluster categoria | Incluso em categoria + FAQ | --- ## Output Structure ### Output 1: `collection_map.json` ```json
{ "project": "pilot-vibradores", "date": "2026-04-20", "store_context": { "industry": "Adult Wellness", "primary_market": "PT", "total_categories": 5 }, "clustering_summary": { "total_keywords": 380, "total_clusters": 28, "clusters_by_type": { "categoria": 5, "feature": 8, "marca": 2, "preço": 2, "informacional": 7, "long_tail": 4 }, "keywords_coverage": 0.98 }, "shopify_collections": [ { "collection_id": "col_001", "collection_name": "Vibradores para Clítoris", "collection_handle": "vibradores-clitoris", "collection_type": "categoria", "parent_cluster": "c_001", "primary_keyword": "vibrador clítoris", "related_keywords": [ "vibrador clitoriano", "vibrador externo", "vibrador clítoris recargável", "vibrador clítoris impermeável", "melhor vibrador clítoris" ], "meta_title": "Vibradores para Clítoris | Premium | Recargáveis | Seguro", "meta_description": "Vibradores especializados para estimulação clitoriana. Silicone premium, recargáveis, impermeáveis. Entrega discreta Portugal.", "description": "Vibradores especializados para a estimulação e prazer clitoriano. Todos os nossos vibradores para clítoris são feitos em silicone de qualidade, com recarga USB, e incluem garantia. Descobre as melhores opções para beginners até experientes.", "estimated_products": 8, "estimated_monthly_revenue": 45, "effort_category": "easy_quick_win", "priority_phase": "FASE 1", "sub_filters": [ { "filter_name": "Tipo", "options": ["Externo", "Estimulador", "Com Vibração"] }, { "filter_name": "Características", "options": ["Recargável", "Impermeável", "Silencioso"] }, { "filter_name": "Preço", "options": ["Até €25", "€25-€50", "€50-€100", "+€100"] } ], "content_recommendations": [ "Blog post: 'Guia de Vibradores para Clítoris — Como Escolher'", "Blog post: 'Melhores Vibradores Clítoris 2026'", "FAQ: 'É seguro usar vibrador? Dicas e cuidados'" ], "related_blog_clusters": ["c_info_001", "c_info_002"] }, { "collection_id": "col_002", "collection_name": "Vibradores Ponto G", "collection_handle": "vibradores-ponto-g", "collection_type": "categoria", "primary_keyword": "vibrador ponto G", "related_keywords": ["vibrador ponto G", "vibrador curvo", "vibrador profundo"], "meta_title": "Vibradores Ponto G | Curvados | Premium | Portugal", "meta_description": "Vibradores curvados para estimulação interna do ponto G. Silicone premium, recargáveis. Descobre os melhores.", "description": "Vibradores especialmente curvados e projetados para a estimulação interna, focado no ponto G. Design ergonómico, materiais seguros, recarga USB.", "estimated_products": 6, "estimated_monthly_revenue": 32, "effort_category": "easy_quick_win", "priority_phase": "FASE 1" }, { "collection_id": "col_003", "collection_name": "Premium & Luxury", "collection_handle": "premium-luxury", "collection_type": "categoria", "primary_keyword": "vibrador premium", "related_keywords": ["vibrador premium", "vibrador de qualidade", "vibrador de luxo", "vibrador silicone premium"], "meta_title": "Vibradores Premium & Luxury | Silicone de Qualidade | Portugal", "meta_description": "Vibradores premium de gama alta em silicone de qualidade superior. Design sofisticado, desempenho avançado.", "estimated_products": 4, "estimated_monthly_revenue": 28, "effort_category": "médio", "priority_phase": "FASE 2" }, { "collection_id": "col_004", "collection_name": "Acessórios & Características", "collection_handle": "acessorios-caracteristicas", "collection_type": "feature", "primary_keyword": "vibrador recargável", "related_keywords": [ "vibrador recargável", "vibrador impermeável", "vibrador silencioso", "vibrador wireless", "carregador vibrador" ], "meta_title": "Acessórios & Características | Recargáveis | Impermeáveis", "description": "Acessórios e produtos com características específicas. Recargáveis USB, impermeáveis, silenciosos, e mais.", "estimated_products": 12, "estimated_monthly_revenue": 55, "effort_category": "easy_quick_win", "priority_phase": "FASE 1", "sub_filters": [ { "filter_name": "Características", "options": ["Recargável", "Impermeável", "Silencioso", "Wireless", "Aquecimento"] } ] }, { "collection_id": "col_blog", "collection_name": "Blog & Guias", "collection_type": "informacional", "primary_keywords": [ "como usar vibrador", "melhores vibradores 2026", "guia vibradores", "é seguro vibrador" ], "content_strategy": "Blog posts informativos que eventualmente linkam para produtos", "estimated_posts": 8, "estimated_organic_sessions": 200, "content_items": [ { "title": "Guia Completo: Como Usar Vibrador de Forma Segura", "primary_keyword": "como usar vibrador", "secondary_keywords": ["técnicas vibrador", "segurança vibrador"], "estimated_word_count": 2000, "internal_links_to": ["col_001", "col_002", "col_004"] }, { "title": "Melhores Vibradores 2026 — Análise Completa", "primary_keyword": "melhores vibradores 2026", "secondary_keywords": ["vibrador recomendado", "melhor vibrador"], "estimated_word_count": 2500, "internal_links_to": ["col_001", "col_002", "col_003", "col_004"] }, { "title": "Vibradores: Respostas às Perguntas Mais Comuns", "primary_keyword": "FAQ vibradores", "faq_items": [ "É seguro usar vibrador?", "Posso usar vibrador na gravidez?", "Como limpar e manter um vibrador?", "Quanto tempo dura a bateria?", "É normal isso não funcionar primeiro dia?" ], "estimated_word_count": 1500, "internal_links_to": ["col_001", "col_002", "col_004"] } ] } ], "shopify_structure_summary": { "total_collections": 5, "product_collections": 4, "blog_collections": 1, "estimated_total_products": 30, "estimated_total_blog_posts": 8, "estimated_total_revenue_potential": 182, "implementation_timeline": { "phase_1_easy_wins": "DIAS 3-5 (antes de loja live)", "phase_2_medium": "DIAS 6-20 (após loja live, FASE 1)", "phase_3_hard": "DIAS 21-45 (FASE 2-3, com autoridade)" } }
}
``` ### Output 2: `shopify_collection_structure.md` (Para Implementação) ```markdown
**Handle:** `vibradores-clitoris`
**Meta Title:** Vibradores para Clítoris | Premium | Recargáveis | Seguro
**Meta Description:** Vibradores especializados para estimulação clitoriana.
Silicone premium, recargáveis, impermeáveis. Entrega discreta Portugal.
**Collection Description:**
Vibradores especializados para a estimulação e prazer clitoriano. Todos os
nossos vibradores para clítoris são feitos em silicone de qualidade, com recarga
USB, e incluem garantia. Descobre as melhores opções para beginners até
experientes. **Produtos Esperados:** 8
**Keywords Alvo:**
**Handle:** `vibradores-ponto-g`
**Meta Title:** Vibradores Ponto G | Curvados | Premium | Portugal
**Meta Description:** Vibradores curvados para estimulação interna do ponto G.
Silicone premium, recargáveis. Descobre os melhores. **Produtos Esperados:** 6
**Keywords Alvo:**
**Handle:** `premium-luxury`
**Meta Title:** Vibradores Premium & Luxury | Silicone de Qualidade | Portugal **Produtos Esperados:** 4
**Keywords Alvo:**
**Handle:** `acessorios-caracteristicas`
**Meta Title:** Acessórios & Características | Recargáveis | Impermeáveis **Produtos Esperados:** 12
**Keywords Alvo:**
**URL:** `/blog/como-usar-vibrador-segura`
**Primary Keyword:** "como usar vibrador"
**Word Count Target:** 2000
**Internal Links To:** col_001, col_002, col_004 **Sections:**
**URL:** `/blog/melhores-vibradores-2026`
**Primary Keyword:** "melhores vibradores 2026"
**Word Count Target:** 2500
**Internal Links To:** col_001, col_002, col_003, col_004 **Sections:**
**URL:** `/faq` (ou `/blog/faq-vibradores`)
**Primary Keyword:** "FAQ vibradores"
**Word Count Target:** 1500 **FAQ Items:**
1. É seguro usar vibrador?
2. Posso usar vibrador na gravidez?
3. Como limpar e manter um vibrador?
4. Quanto tempo dura a bateria?
5. É normal não funcionar no primeiro dia?
6. Qual é o melhor vibrador para iniciantes?
7. Existem efeitos secundários?
8. Como sou discreto na compra? --- ## Métricas de Sucesso (FASE 1-3) | Métrica | Baseline | Target FASE 1 | Target FASE 2 | Target FASE 3 |
|---------|----------|---------------|---------------|---------------|
| Collections Indexadas (GSC) | 0 | 5 | 5 | 5 |
| Blog Posts Live | 0 | 3 | 5 | 8 |
| Keywords em TOP 30 | 0 | 5-10 | 20-30 | 40-50 |
| Keywords em TOP 10 | 0 | 0-2 | 3-5 | 5-10 |
| Organic Sessions/Mês | 0 | 10-50 | 100-200 | 500+ |
| Revenue Potential (EUR/Mês) | €0 | €50-100 | €200-300 | €500+ | ``` ### Output 3: `cluster_validation.json` (Audit interno) ```json
{ "validation_checklist": { "no_duplicate_keywords": true,
"all_keywords_clustered": true, "cluster_cohesion_score": 0.92,
"collection_viability": { "col_001": { "name": "Vibradores Clítoris",
"keyword_count": 12, "revenue_potential": 45, "viability": "high" } },
"gaps_identified": [ "Localização (géo) ignorada — site é online only", "Marca:
apenas 2 clusters — adicionar se estratégia de comparação", "Long-tail:
considerar agrupar mais em cada categoria" ], "recommendations": [ "Proceder com
5 collections (4 produto + 1 blog)", "Priorizar col_001 e col_004 em FASE 1
(quick wins)", "Blog antes de ter ranking (FASE 0, para estabelecer autoridade
de conteúdo)" ] }
}
``` --- ## Validação & Checklists ### Pré-execução
2. **SOP 5:** Internal Linking Strategy (breadcrumbs, related products, blog
links)
3. **Shopify App Implementation:** Integra SOP 1-5 em UI interativa --- ## 🔗
Relacionados **Dependências & Fluxo Sequencial:**

---

## 🔗 Relacionados

- [[Related-Doc-1]] — descrição
- [[Related-Doc-2]] — descrição

---
