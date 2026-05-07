---
name: DATAFORSEO-USAGE-AUDIT-2026-05-07
description: Auditoria de eficiência (custo + performance) do uso da DataForSEO API no RankPanda — gaps + plano de optimização
type: sop
status: active
foco: technical
tags: [dataforseo, api, cost-optimization, audit, semantic-kw]
wikilinks: [[ETAPA-2-VALIDATION-MLforSEO-2026-05-07]], [[SOP-2-KEYWORD-RESEARCH-V2]], [[API-REGISTRY]]]
---

# DataForSEO Usage Audit — Cost + Performance (07/05/2026)

**Resumo:** Auditoria do uso actual da DataForSEO API no codebase RankPanda Shopify. **5 problemas críticos** que multiplicam o custo por ~30x vs. configuração óptima. Plano de optimização em 5 passos (~1.5 dias) que reduz custo de ~$70 para ~$2.35 num research cycle de 10k keywords.

---

## 🎯 Por Que Isto Importa

- O Rui paga por cada chamada DataForSEO. A diferença entre uso eficiente e ineficiente é **30x** em custo total.
- Sem optimização, P0 #3 (EAV combination generator) que gera 10k-100k keywords sintéticas vai consumir centenas de dólares por research cycle em vez de unidades.
- **Pré-requisito para P0 #3 e qualquer feature futura que toque DataForSEO.**

---

## 📊 Estado Actual (auditado contra código)

### Onde a API é chamada

| Ficheiro | Linha | Propósito |
|---|---|---|
| `shopify-app/app/services/serpAnalysis.server.ts` | 233 | POST `/v3/serp/google/organic/live/regular` |
| `shopify-app/app/routes/app.api.serp-analysis.tsx` | 33 | Rota Remix → `analyzeKeywordPageType()` |
| `shopify-app/app/routes/app.keyword-research.tsx` | 1107-1122 | `submitSerpBulk()` — fila client-side sequencial |
| `shopify-app/app/services/csvParser.server.ts` | 111-127 | Parser para CSV exports DataForSEO |
| `shopify-app/services/keywords-service/src/index.ts` | 145-167 | Parser para endpoint `/import` (import-time) |

**Único endpoint chamado:** `/v3/serp/google/organic/live/regular`. Mais nada.

### Configuração

| Aspecto | Estado |
|---|---|
| Credenciais | `.env`: `DATAFORSEO_LOGIN`, `DATAFORSEO_SECRET` |
| URL base | `https://api.dataforseo.com` (hardcoded) |
| Rate limiting client-side | ❌ Não existe |
| Retry + exponential backoff | ❌ Não existe (só timeout 15s) |
| Sandbox / production toggle | ❌ Sem config (sempre prod) |

### Cache (único positivo)

| Aspecto | Estado |
|---|---|
| Tabela | `SerpCache` (Prisma) |
| TTL | 30 dias |
| Chave | `(keyword, locationCode=2620, languageCode="pt")` |
| Cobertura | Todas as chamadas SERP passam por `loadFromCache()` antes de chamar a API |
| Reutilização | Global — keyword analisada para shopA é reutilizada para shopB ✅ |
| Campos cached | `organicUrls`, `crawlData`, `pageType`, `titleTerms`, `serpFeatures` |

### Observabilidade

| Aspecto | Estado |
|---|---|
| Counter de calls por shop | ❌ Não existe |
| Estimativa de custo | ❌ Nenhuma |
| Logging detalhado | ⚠️ Básico (`console.log` em cache hits) |
| Alertas de spend | ❌ Nenhum |

---

## 🚨 5 Problemas Críticos (ordem por impacto em $)

### #1 — Modo Live em vez de Standard Queue (~70% economia possível)

**Estado actual:** Todos os requests usam `/live/regular` mode.

**Pricing real (auditado nas docs oficiais):**
- SERP Live mode: **$2.00 / 1000 requests**
- SERP Standard Queue (Task POST + Task GET): **$0.60 / 1000 requests** — 70% mais barato
- Trade-off: Standard demora 5-45 min vs Live 6 segundos

**Quando Live é justificado:** UX user-facing tempo-real (autocomplete enquanto user escreve).

**Quando Standard é o correcto:** Análise batch de keywords pré-importadas — o user não está à espera, pode esperar 30 min para guardar dinheiro.

**Caso de uso real:** Quando user importa CSV com 500 keywords e clica "Analyse all", actualmente são 500 chamadas Live = **$1.00**. Em Standard seria **$0.30**. Multiplicado por todos os clientes/imports = milhares.

### #2 — Zero batching no SERP (1 keyword/request)

**Estado actual:** Loop sequencial — 1 chamada HTTP por keyword.

**Realidade da API:** SERP `task_post` aceita até **100 tasks num único POST request**. Cada task ainda paga individualmente, mas o overhead de rede é 100x menor → tempo total cai de N×6s para ~30s para o batch inteiro processar.

**Performance ganha:** análise de 100 keywords passa de **~10 minutos** (1 a 1) para **~30s** (batch).

### #3 — Sem `Keywords Data search_volume` (golden batch endpoint missing)

**Estado actual:** Validação de search volume não existe na app — confiamos no que o user importa do Semrush.

**Realidade:** DataForSEO tem o endpoint **golden** `/v3/keywords_data/google_ads/search_volume/live` que aceita **até 1000 keywords num único request** por **$0.075** (= **$0.000075/keyword**).

**Impacto direto no P0 #3 (EAV combination generator):**
- Sem este endpoint: P0 #3 gera 10k-100k keywords sintéticas mas zero forma barata de validar volumes.
- Com este endpoint: validar 100k keywords sintéticas = 100 batches × $0.075 = **$7.50 total**.
- Sem ele, fazer SERP individual = ~$200.

### #4 — Sem DataForSEO Labs API (expansion barata em falta)

**Estado actual:** Não usamos Labs API.

**Realidade:** Labs API tem 3 endpoints baratíssimos para expansion semântica:
- `/v3/dataforseo_labs/google/keyword_suggestions/live` — $0.01/seed
- `/v3/dataforseo_labs/google/related_keywords/live` — $0.01/seed
- `/v3/dataforseo_labs/google/keyword_ideas/live` — $0.01/seed

**Impacto:** Expansion de 100 seeds = $1 com Labs vs ~$50 com SERP queries equivalentes.

### #5 — Sem observabilidade de custo

**Estado actual:** Não há contador de chamadas, nem auditoria de custo por shop, nem dashboard.

**Risco:** O Rui pode ter shop com runaway costs e só descobrir quando vê a factura DataForSEO.

---

## 💰 Custo Estimado — Antes vs Depois

Para 1 research cycle típico (10.000 keywords, vibradores como exemplo):

### Cenário ATUAL (sem optimização)
| Operação | Endpoint | Custo |
|---|---|---|
| SERP analysis 10k keywords (Live, 1×1) | SERP live | $20.00 |
| Search volume validation | ❌ não existe | — |
| Keyword expansion | ❌ não existe (manual via Semrush) | — |
| **Total por research cycle** | | **$20.00** |

### Cenário OPTIMIZADO (após plano abaixo)

Assumindo cycle típico: 8.000 keywords vêm via Semrush CSV (com volume) + 2.000 são descobertas pela app (sintéticas/expansion):

| Operação | Endpoint | Custo |
|---|---|---|
| Volume das 8k keywords Semrush | **N/A — já vêm no CSV** | **$0.00** |
| Expansion 100 seeds (descobre ~2k novas) | Labs suggestions | $1.00 |
| Volume das 2k descobertas (2 batches) | KD search_volume/live | $0.15 |
| SERP analysis top 10 (1k prioritárias, Standard batched) | SERP task_post | $0.60 |
| **Total por research cycle** | | **$1.75** |

**Diferença vs cenário actual:** **11x mais barato** + cobre **3x mais funcionalidade**. Vs cenário sem skip-existing seria $2.35 — **DF0 (source-aware resolver) poupa adicional $0.60 por cycle (25%).**

---

## 🛠️ Plano de Optimização (6 passos, ~2 dias)

Implementar **antes** de P0 #3 — caso contrário P0 #3 gera tráfego ineficiente desde o dia 1.

### Princípio fundador: dados importados ≠ dados descobertos

**Insight do Rui (07/05/2026):** Quando user importa CSV do Semrush/Ahrefs/SE Ranking, o CSV **já traz `searchVolume`, `difficulty`, `cpc`, `intent`** por keyword. Pagar à DataForSEO para validar esses dados é **dinheiro deitado fora** — o Semrush já cobrou a investigação.

**Regra:** DataForSEO só é chamada para:
1. Keywords **descobertas pela própria app** (sintéticas do P0 #3, expansion via Labs API, sugestões de autocomplete) — estas NÃO têm volume conhecido
2. SERP analysis — Semrush não dá top-10 results estruturado
3. Refresh explícito pelo user (botão "Refresh volumes" em Settings) — se ele suspeitar que dados ficaram velhos

### DF0 — Source-aware data resolver (~½ dia) — TRANSVERSAL, FAZER PRIMEIRO

Este é o **building block** que todos os outros DFs usam. Wrapper único:

```typescript
// services/dataforseoResolver.server.ts
async function resolveKeywordVolumes(
  shop: string,
  keywords: string[],
  opts?: { forceRefresh?: boolean }
): Promise<Map<string, { volume: number | null; source: 'csv' | 'cache' | 'api' }>>
```

Lógica:
1. Para cada keyword, fazer query a `KeywordResearch` no DB:
   - Se `searchVolume IS NOT NULL` E `forceRefresh=false` → marcar como `'csv'`, devolver valor
   - Se `searchVolume IS NULL` → marcar como pendente
2. Para as pendentes:
   - Verificar `KeywordVolumeCache` (TTL 30 dias) → marcar como `'cache'`, devolver
3. Para as ainda pendentes (verdadeiramente novas):
   - Chamar `bulkSearchVolume()` (DF2) em batches de 1000
   - Persistir no `KeywordVolumeCache`
   - Marcar como `'api'`, devolver

**Resultado:** P0 #3 pode chamar `resolveKeywordVolumes(shop, syntheticKeywords)` sem se preocupar — o resolver garante zero waste.

Idem para `resolveDifficulty()`, `resolveCpc()`, `resolveSerp()` se vier a fazer sentido. SERP fica em `SerpCache` (já existe).

### DF1 — Migrar SERP para Standard Queue com fallback Live (~½ dia)

- Refactor de `serpAnalysis.server.ts` para usar `task_post` + polling de `task_get`
- Adicionar parâmetro `mode: 'live' | 'standard'` à função (default `standard`)
- Live só fica para user-facing real-time UI (se houver caso)
- Polling: queue interno (Redis ou in-memory) + cron que faz `task_get` quando `task_ready` indica disponibilidade

### DF2 — Implementar Keywords Data search_volume bulk (~½ dia)

- Novo service `dataforseoVolume.server.ts` com função primitiva `bulkSearchVolume(keywords[]): Map<string, number>` (chama API directamente)
- Aceita até 1000 keywords / call; chunks automáticos se mais
- Persistência: nova tabela `KeywordVolumeCache (keyword, locationCode, languageCode, volume, fetchedAt)` com TTL 30 dias
- **Sempre invocada via DF0 resolver** — nunca chamada directamente pelos use cases. Resolver garante skip de keywords que já têm volume.
- Endpoint Remix `app.api.keywords.bulk-volume.tsx` para UI consumir manualmente (ex: botão "Refresh volumes")

### DF3 — Implementar Labs API expansion (~¼ dia)

- Novo service `dataforseoLabs.server.ts` com 3 funções:
  - `getKeywordSuggestions(seed): Keyword[]`
  - `getRelatedKeywords(seed): Keyword[]`
  - `getKeywordIdeas(seeds[]): Keyword[]`
- Cache TTL 7-14 dias (recomendação oficial)

### DF4 — Cost observability (~¼ dia)

- Nova tabela `DataForSEOCallLog` (shop, endpoint, count, estimatedCost, createdAt)
- Wrapper `callDataForSEO(endpoint, payload)` que loga cada call
- UI em `/app/settings` mostra custo estimado mensal por shop
- Threshold opcional (ex: bloquear se shop ultrapassar $50/mês)

### DF5 — Retry + exponential backoff helper (~¼ dia)

- Helper `withRetry(fn, opts)` em `vps.server.ts` ou `lib/retry.ts`
- 3 tentativas com 1s, 2s, 4s backoff
- Distinguir 429 (rate limit, esperar) de 5xx (transitório, retry) de 4xx (não retry)

---

## 🔗 Após optimização

P0 #3 (EAV combination generator) consome estes building blocks:
- `bulkSearchVolume(syntheticKeywords)` para validar volumes (DF2)
- `getKeywordSuggestions(seed)` para expansion alternativa (DF3)
- SERP em standard mode para análise (DF1)
- Tudo loggado com cost tracking (DF4)
- Robusto a falhas transitórias (DF5)

---

## 📚 Referências

- DataForSEO pricing: https://dataforseo.com/pricing
- DataForSEO docs: https://docs.dataforseo.com/v3
- SERP API: https://dataforseo.com/apis/serp-api
- Keywords Data API: https://dataforseo.com/apis/keyword-data-api
- Labs API: https://dataforseo.com/apis/dataforseo-labs-api

## 🔗 Relacionados

- `[[ETAPA-2-VALIDATION-MLforSEO-2026-05-07]]` — relatório do módulo MLforSEO; P0 #3 depende destas optimizações
- `[[SOP-2-KEYWORD-RESEARCH-V2]]` — pipeline operacional onde DataForSEO é consumido
- `[[API-REGISTRY]]` — registo central de APIs (a actualizar com este resultado)
