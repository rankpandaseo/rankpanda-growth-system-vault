---
name: sop-2-keyword-research-v2
description: API-first pipeline to transform Semrush CSV into enriched keyword
list with SERP data, content analysis, and revenue potential
type: sop
status: active
foco: seo
tags: [keyword-research, semrush, dataforseo, api-first]
wikilinks: [[SOP-1-STORE-CONTEXT-SETUP-v2]],
[[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-1-DIAGNOSTIC]],
[[FASE-2-EXECUTION]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# SOP 2 — Keyword Research v2 (API-First Pipeline) **Resumo:** Transformar Semrush CSV em keyword list limpa, enriquecida com SERP data, content analysis, semantic variations, e revenue potential — pronta para clustering (SOP 3). --- ## 🎯 Por Que Isto Importa **Impacto direto em SEO:**

**Resumo:** SOP 2 — Keyword Research v2 (API-First Pipeline) **Resumo:**
Transformar Semrush CSV em keyword list limpa, enriquecida com SERP data,
content analysis, semantic variations, e revenue potential — pronta para
clustering (SOP 3). --- ## 🎯 Por Que Isto Importa **Impacto direto em SEO:**

---

## 🎯 Por Que Isto Importa

[Adiciona contexto: impacto direto no projeto, porquê isto importa]
- Ponto 1
- Ponto 2
- Ponto 3

---

## ⚡ Quick Checklist

- ← [[FASE-1-DIAGNOSTIC]] — **Insights Competitivos:** Análise competitiva de keywords que competitors rankeiam (opcional, mas melhora priorização) --- ## ⚡ Quick Checklist - [ ] SOP 1 (Store Context) preenchido completamente
- [ ] Semrush CSVs exportados (keywords + SERP data)
- [ ] Credenciais DataForSEO ativas
- [ ] Credenciais Crawl4AI ativas (ou alternativa scraping)
- [ ] Claude relevance gate executado (threshold: >60% relevante)
- [ ] DataForSEO SERP fetch completo (apenas keywords filtradas)
- [ ] Content analysis top 3 páginas por keyword
- [ ] Revenue potential + effort scoring calculado
- [ ] Outputs gerados: keywords.json + keywords.csv + clusters_for_sop3.json
- [ ] Validações passed (>200 keywords, relevance gate <40% rejeição, effort distributed)
- [ ] Ready for [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] --- ## 🔑 Key Principles 1. **API-First:** Semrush → Claude relevance gate → DataForSEO → Crawl4AI → claude semantic analysis. Cada etapa filtra ou enriquece.
- [ ] SOP 1 (Store Context) preenchido
- [ ] Semrush CSVs exportados (keywords + SERP)
- [ ] Credenciais DataForSEO ativas
- [ ] Credenciais Crawl4AI ativas (ou alternativa de scraping) ### Execução
- [ ] Parse Semrush CSVs
- [ ] Claude relevance gate executado
- [ ] DataForSEO SERP fetch (apenas keywords filtradas)
- [ ] Crawl4AI content analysis (top 3 páginas)
- [ ] Claude semantic extraction
- [ ] Revenue potential + effort scoring
- [ ] Output JSON/CSV gerados ### Validação
- [ ] Total de keywords output ≥ 200 (mínimo para viabilidade)
- [ ] Relevance gate rejeitou < 20% (se > 40%, rever store context)
- [ ] Revenue potential total > 0 (lógica funcionou)
- [ ] Effort scores distribuídos entre FASE 1, 2, 3
- [ ] Semantic variations encontradas para 80%+ keywords ### Output Final
- [ ] `keywords.json` salvo em `/vault/01-Clientes/[cliente]/`
- [ ] `keywords.csv` importado em ClickUp como task list
- [ ] `clusters_for_sop3.json` pronto para SOP 3 --- ## PARTE H — API Checklist | API | Endpoint | Frequência | Custo | Alternativa |

---

## 📖 Conteúdo Principal

2. **Cost Control:** Claude gate ANTES de DataForSEO (evita chamar API para
keywords irrelevantes). Estimativa total: €5-10, não €50-100.
3. **Revenue-Focused:** Cada keyword tem revenue_potential calculado (SV × CTR ×
CR × AOV). Priorização baseada em impacto, não em volume.
4. **Semantic Expansion:** Não paramos em "vibrador clítoris". Encontramos
variações (vibrador clitoriano, externo) + long-tail (com recargável,
silencioso, premium).
5. **SERP Context:** Entendemos o SERP (ecommerce rankings? featured snippet?
PAA?). Isto molda on-page strategy em SOP 4. --- ## 📖 Processo Completo --- ###
Etapa 1: Input Structure (Semrush CSV) ### CSV 1: Keyword Base
```
keyword,search_volume,keyword_difficulty,intent,trend,cpc_usd
vibradores,2000,45,comercial,estável,0.85
vibrador clítoris,800,35,comercial,crescente,0.65
vibrador recargável,600,30,comercial,estável,0.45
melhores vibradores,500,28,info+comercial,estável,NULL
vibrador silencioso,400,25,comercial,estável,0.35
...
``` **Campos esperados:**
```
keyword,rank_1_domain,rank_1_url,rank_1_dr,rank_2_domain,rank_2_url,rank_2_dr,rank_3_domain,rank_3_url,rank_3_dr
vibradores,example1.com,/vibradores,65,example2.com,/best-vibrators,60,example3.com,/vibrators,55
vibrador
clítoris,specialized.com,/clitoris-vibrators,45,example1.com,/category/clit,65,guide.com,/guide,40
...
``` **Notas:**
Ler da SOP 1:
**Prompt para Claude:** ```
Tu es um especialista em keyword relevance para ecommerce. Contexto da loja:
{ "keywords": [ { "keyword": "vibrador clítoris", "relevance": "RELEVANTE",
"reason": "Alinha perfeitamente com categoria 'Vibradores Clítoris', intent
comercial forte, AOV esperado €30-50" }, ... ], "summary": { "total_input": N,
"relevante": X, "marginal": Y, "irrelevante": Z, "recomendacao": "Proceder com X
keywords relevantes + Y marginais (total N) para DataForSEO" }
}
``` **Output esperado:** JSON com classificação + reasoning ### Etapa 3: Filter Decision
Para CADA keyword relevante, chamar DataForSEO SERP API: ```bash
curl -X POST https://api.dataforseo.com/v3/serp/google/organic/live/advanced \
-H "Content-Type: application/json" \ -d '{ "keyword": "vibrador clítoris",
"location_code": 554, # Portugal "language_code": "pt", "depth": 20 # Top 20
results }'
``` **Resposta esperada:**
```json
{ "keyword": "vibrador clítoris", "serp_results": [ { "rank": 1, "url":
"https://example.com/product", "title": "Vibrador Clítoris...", "snippet":
"...", "domain": "example.com", "type": "organic", "rating": 4.5,
"review_count": 123 }, ... ], "serp_features": ["shopping_results",
"featured_snippet", "people_also_ask"], "search_volume": 800, "cpc": 0.65
}
``` ### Etapa 2: Extract Key Metrics
```
gap_score = (avg_dr_top_3 - our_dr_estimate) + (keyword_difficulty / 2)
``` --- ### Etapa 4: Content Analysis (Crawl4AI) Scrapear top 3 pages no SERP para entender: intent real, structure, semantic keywords, schema. ### Etapa 1: Crawl Top 3
Para CADA keyword, fetch HTML das 3 páginas top-ranking: ```python
from crawl4ai import AsyncWebCrawler async def fetch_page(url): async with
AsyncWebCrawler() as crawler: result = await crawler.arun(url) return { "url":
url, "html": result.html, "markdown": result.markdown, "metadata":
result.metadata }
``` ### Etapa 2: Extract Key Elements
Para cada página:
**Prompt para Claude:** ```
Aqui está a página top-ranking para "vibrador clítoris": [HTML/Markdown da
página] Extrai:
1. **Semantic Keywords** (variações da keyword principal encontradas na página)
- Título: "vibrador clitoriano", "vibrador externo", etc. - H2/H3: variações
semânticas - Corpo: long-tail variations 2. **Category Signals** (que tipo de
página é) - Produto? Categoria? Guia? Artigo informacional? Comparação? 3.
**Content Structure** - Tem seção de preços? Avaliações? FAQ? Comparação? 4.
**Entity Relationships** - Marcas mencionadas - Características (material,
impermeável, recargável, etc.) - Públicos-alvo implícitos Retorna JSON:
{ "semantic_keywords": ["vibrador clitoriano", "vibrador externo", ...],
"page_type": "produto", "has_pricing": true, "has_reviews": true,
"key_features_mentioned": ["silicone", "recargável", "impermeável"],
"competitor_brand": "BrandX", "content_depth_score": 0.85 # 0-1, baseado em
estrutura
}
``` --- ### Etapa 5: Enrichment & Scoring ### Etapa 1: Revenue Potential Calculation Para cada keyword: ```
revenue_potential = search_volume × ctr × conversion_rate × aov Onde:
revenue_potential = 800 × 0.03 (CTR baixo, loja nova) × 0.02 (2% CR benchmark) ×
€35 (AOV) = €16.8 / mês em potencial (após ranking) Nota: Isto é POTENCIAL, não
realidade. Serve para priorizar keywords de maior impacto.
``` ### Etapa 2: Effort Score (Prioritização) ```
effort_score = (keyword_difficulty × 0.4) + (gap_score × 0.3) +
(search_volume_inverse × 0.3) Onde:
``` ### Etapa 3: Semantic Variations & Long-Tail Expansion **Prompt para Claude:** ```
Baseado na keyword "vibrador clítoris" e nas variações semânticas encontradas:
Gera variações que podem rankear + long-tail keywords relacionadas: 1.
**Variações Semânticas (même intent)** - "vibrador clitoriano" - "vibrador para
clítoris" - "vibrador externo" 2. **Long-Tail Expandidas (mesmo público, mais
específico)** - "vibrador clítoris recargável" - "vibrador clítoris impermeável"
- "vibrador clítoris silencioso" - "vibrador clítoris premium" 3.
**Conversational/Voice** - "qual é o melhor vibrador para clítoris" - "vibrador
clítoris é seguro" Retorna JSON:
{ "primary_keyword": "vibrador clítoris", "semantic_variations": [...],
"long_tail_expansions": [...], "conversational_queries": [...],
"recommended_for_sop3_clustering": [...]
}
``` --- ### Etapa 6: Output Structure ### Output 1: `keywords.json` (Estruturado, para código) ```json
{ "project": "pilot-vibradores", "date": "2026-04-20", "store_context": {
"industry": "Adult Wellness", "primary_market": "PT", "categories": ["Vibradores
Clítoris", "Vibradores Ponto G", "Premium", "Acessórios"], "aov_eur": 35,
"conversion_rate_benchmark": 0.02 }, "summary": { "total_keywords_input": 450,
"after_claude_gate": 380, "with_serp_data": 380, "with_content_analysis": 380,
"estimated_monthly_revenue_potential": 8500, "quick_wins_count": 45,
"medium_term_count": 120, "long_term_count": 215 }, "keywords": [ { "id":
"kw_001", "keyword": "vibrador clítoris", "search_volume": 800,
"keyword_difficulty": 35, "intent": "comercial", "trend": "crescente",
"cpc_usd": 0.65, "relevance_score": "RELEVANTE", "relevance_reason": "Alinha com
categoria principal", "serp_data": { "rank_1_domain": "example1.com",
"rank_1_url": "https://example1.com/vibrador-clitoris", "rank_1_dr": 60,
"rank_2_domain": "example2.com", "rank_2_dr": 55, "rank_3_domain":
"example3.com", "rank_3_dr": 50, "avg_dr_top_3": 55, "gap_score": 45,
"serp_features": ["shopping_results", "ratings"], "has_ecommerce_ranking": true
}, "content_analysis": { "page_types_top_3": ["produto", "produto",
"categoria"], "semantic_keywords": ["vibrador clitoriano", "vibrador externo",
"vibrador rápido"], "key_features": ["silicone", "recargável", "impermeável",
"múltiplos modos"], "content_depth_avg": 0.78 }, "revenue_potential": {
"ctr_estimated": 0.025, "monthly_revenue_potential_eur": 14, "calculation": "800
× 0.025 × 0.02 × €35 = €14/mês" }, "effort_score": 28, "effort_category":
"easy_quick_win", "priority_phase": "FASE 1", "semantic_variations": [ "vibrador
clitoriano", "vibrador para clítoris", "vibrador externo" ],
"long_tail_suggestions": [ "vibrador clítoris recargável", "vibrador clítoris
impermeável", "vibrador clítoris silencioso", "melhor vibrador clítoris" ],
"recommended_collection": "Vibradores Clítoris", "recommended_page_type":
"produto + categoria", "notes": "Oportunidade forte, volume alto, dificuldade
média — ataque em FASE 1" }, ... ]
}
``` ### Output 2: `keywords.csv` (Flat, para ClickUp) ```csv
keyword,search_volume,difficulty,intent,effort_score,effort_category,priority_phase,revenue_potential_eur,recommended_collection,serp_difficulty,notes
vibrador clítoris,800,35,comercial,28,easy_quick_win,FASE 1,14,"Vibradores
Clítoris",55,"Alto volume, dificuldade média — quick win"
vibrador recargável,600,30,comercial,22,easy_quick_win,FASE
1,10.5,"Acessórios",48,"Feature-specific, fácil de rankear"
...
``` ### Output 3: `clusters_for_sop3.json` (Input para SOP 3) ```json
{ "ready_for_clustering": [ { "keyword": "vibrador clítoris", "cluster_type":
"category", "candidate_collections": ["Vibradores Clítoris"],
"semantic_variations": ["vibrador clitoriano", "vibrador externo"],
"long_tail_children": [ "vibrador clítoris recargável", "vibrador clítoris
impermeável", "melhor vibrador clítoris" ] }, ... ]
}
``` --- ### Validação & Checklists ### Pré-execução
|-----|----------|-----------|-------|------------|
| Semrush | CSV Export | 1x | FREE (export manual) | N/A |
| Claude | /messages (relevance gate) | 1x | ~$0.01-0.05 | Sem alternativa prática |
| DataForSEO | /serp/google/organic | 1x per keyword | $0.01-0.02 per call | Alternativa: Semrush SERP data se já tem |
| Crawl4AI | HTTP fetch | 1x per top-3 URL | FREE (self-hosted) | Puppeteer, Playwright |
| Claude | /messages (semantic analysis) | 1x | ~$0.05-0.10 | Sem alternativa | **Estimativa de custo (pilot-vibradores, 380 keywords):**
2. **SOP 4:** On-Page Optimization (aplica keywords em title, meta description,
H1, corpo)
3. **Implementação Shopify App:** Integra SOP 1 + SOP 2 + SOP 3 em formulário
interativo --- --- ## 🔗 Relacionados **Dependências & Fluxo Sequencial:**

---

## 🔗 Relacionados

- [[Related-Doc-1]] — descrição
- [[Related-Doc-2]] — descrição

---
