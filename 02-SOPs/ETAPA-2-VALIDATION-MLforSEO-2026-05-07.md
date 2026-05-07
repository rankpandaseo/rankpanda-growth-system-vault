---
name: ETAPA-2-VALIDATION-MLforSEO-2026-05-07
description: Análise comparativa entre módulo "Fundamentals of Semantic KW Research" (MLforSEO/Lazarina Stoy) e implementação real da ETAPA 2 — alinhamentos, gaps, recomendações
type: sop
status: active
foco: seo
tags: [etapa-2, semantic-kw, eav, mlforseo, validation, gap-analysis]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[CONCEITO-Keyword-Research]], [[../../SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS]], [[../../SEMANTIC-KW-PIPELINE-DESIGN]], [[../../ETAPA2_DOCUMENTATION_INDEX]]
---

# ETAPA 2 — Validation Report vs MLforSEO Module 1 (Fundamentals of Semantic KW Research)

**Resumo:** Análise comparativa em 3 eixos (transcripts MLforSEO ↔ docs do vault ↔ código real) para a ETAPA 2 (Semantic Keyword Extraction). Identifica o que está alinhado, trade-offs explícitos, e 9 gaps priorizados (P0-P2) com recomendação de execução em 5-6 dias.

**Data:** 2026-05-07
**Origem:** Sessão de validação ETAPA 2 com Rui

---

## 🎯 Por Que Isto Importa

- **Alinhar a app com state-of-the-art** — o módulo da Lazarina Stoy é referência reconhecida em semantic SEO. Saber onde divergimos com fundamento e onde divergimos por omissão é diferente.
- **Defender a entrega ao cliente** — quando vendemos "semantic KW research", o método tem de cobrir o que o mercado conhece como tal.
- **Prioritizar o roadmap** — em vez de implementar tudo, sabemos quais 3 P0 desbloqueiam o output principal do método EAV (combination generation).

---

## 📚 Material Auditado

### Lado MLforSEO (4 aulas que constituem o "Module 1")

Os transcripts integrais estão arquivados em `[[SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS]]` (raiz do projecto):

| Aula | Tópico | Linhas em `SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS.md` |
|---|---|---|
| 1 | Entities, Entity Attributes, Entity Attribute Variables (EAV Model) | ~130-310 |
| 2 | Practical/Lab — Query Entity Extraction with Google NLP + ML analysis | ~317+ |
| 3 | Search Query Sequences and Query Path | (capítulo seguinte) |
| 4 | Practical/Lab — Working with Google's Autocomplete API | (capítulo seguinte) |

### Lado vault — docs relevantes existentes

- `[[../../SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS]]` — 17 lições integrais do curso da MLforSEO (2.489 linhas)
- `[[../../SEMANTIC-KW-PIPELINE-DESIGN]]` — Design de ETAPA 1-9 (897 linhas) — desenhada como heurística, **divergente da implementação real (Claude)**
- `[[../../SEMANTIC-KW-COURSE-ANALYSIS-FOR-PHASE1]]` — Análise lesson-by-lesson mapeada a Phase 1 (719 linhas)
- `[[../../SEMANTIC-KW-STATE-OF-THE-ART-AUDIT]]` — Audit vs concorrentes
- `[[../../WEEK-1-DEEP-DIVE-AULAS-1-3]]` — Cronograma + schemas
- `[[../../WEEK-1-MONDAY-EAV-ANALYSIS]]` — Análise EAV manual (11 entities, 19 features, 4 personas)
- `[[../../WEEK-1-TUESDAY-INTENT-PERSONA-ANALYSIS]]` — Intent rules PT-PT + persona×intent matrix
- `[[../../ETAPA2_DOCUMENTATION_INDEX]]` — Índice de documentação ETAPA 2
- `[[../../ETAPA2_IMPROVEMENT_SUMMARY]]` — Reescrita do prompt com businessContext
- `[[../../ETAPA2_COMPLETION_REPORT]]`
- `[[../../ETAPA2_NEXT_STEPS]]`
- `[[SOP-2-KEYWORD-RESEARCH-V2]]` — Pipeline operacional API-first
- `[[CONCEITO-Keyword-Research]]` — Conceito generic

### Lado código — implementação real da ETAPA 2

- `shopify-app/services/keywords-service/src/etapa2-services/claude-eav-extractor.ts` (~290 linhas) — extracção via Claude CLI
- `shopify-app/services/keywords-service/src/etapa2-services/eav-types.ts:6-30` — JSON schema do output
- `shopify-app/services/keywords-service/src/pipelines/etapa2-eav-extraction.ts:17-106` — pipeline batch
- `shopify-app/services/keywords-service/src/consumers/categorization-consumer.ts:8` — RabbitMQ consumer
- `shopify-app/services/keywords-service/src/index.ts:934-965` — endpoint `/etapa2/status`
- `shopify-app/app/routes/app.api.keywords.etapa2-status.tsx` — proxy Remix
- `shopify-app/app/components/keywords/ETAPA2ProgressModal.tsx` — UI

---

## ✅ Alinhamentos Confirmados

| Conceito MLforSEO | Implementação |
|---|---|
| Entity → Attribute → Variable (Aula 1) | `eav-types.ts:6-30` produz `entities[]`, `attributes[{category, value}]` por keyword |
| EAV via ML supervisionado (Aula 2) | Claude CLI substitui Google NLP API (decisão arquitectónica — ver trade-off abaixo) |
| Intent classification (referida brevemente nas aulas) | **Mais rigorosa que o módulo** — 4 classes (info/commercial/transactional/navigational) + confidence scores + regras explícitas no prompt |
| Persona awareness (Aula 1, "buyer personas") | `eav-types.ts:21` — Claude detecta persona por keyword (mulher/homem/casal/etc.) |
| Localização linguística (multi-idioma) | ETAPA 1 detecta PT/EN/ES/FR; prompt agnóstico de nicho com locale dinâmico |
| Business context calibration | **Vai além do módulo** — passa contexto da loja ao Claude para melhorar accuracy |

---

## 🔄 Trade-off Explícito: Claude vs Google NLP API

A Aula 2 prescreve Google NLP API. A app usa Claude CLI. **A troca é defensável** mas tem custos:

| Aspecto | Google NLP (Aula) | Claude (nosso) |
|---|---|---|
| Custo (8-10k KW) | ~$78/dia | Mais barato com plano Max |
| Entity types | Tipologia fixa Google | Tipologia aberta — flexível mas inconsistente |
| Salience score numérico | ✅ Devolvido por API | ❌ Não pedimos no prompt |
| Sentiment + magnitude | ✅ Devolvido por API | ❌ Não pedimos no prompt |
| Mentions / variations | ✅ Standardizado | ❌ Não pedimos |
| Knowledge Graph metadata | ✅ Automático | ❌ Não — Claude não tem KG live |
| Multi-tarefa num só pass | ❌ Várias chamadas | ✅ Tudo num só pass |
| Customização do prompt | ❌ Hardcoded | ✅ Prompt + businessContext + productTerms |

**Veredicto:** swap legítimo. Perda crítica é o **Knowledge Graph metadata** — recuperável com chamada extra à Google KG API (P1 #4 abaixo).

---

## 🚨 Gaps Priorizados

### P0 — Critical (bloqueiam capacidades core do módulo)

#### P0 #1 — Custom prominence metric
- **Ensina (Aula 2):** salience da API só é fiável em texto longo. Para queries curtas, calcular manualmente: para cada entidade, `nº keywords onde aparece` + `soma de search volume`.
- **App actual:** salience NÃO é capturada. Métrica agregada NÃO existe.
- **Impacto:** sem isto, não conseguimos identificar **as entidades que realmente importam** no keyword universe (vs as que aparecem por acaso).
- **Implementação:** query SQL agregada sobre `KeywordResearch.rawData->>'eav'`. ~50 linhas.

#### P0 #2 — Co-occurring n-grams por entidade
- **Ensina (Aula 2 / passo 2 + Aula 3 / approach 3):** para cada entidade, top-N bigrams/trigrams co-ocorrentes nas keywords onde aparece. Detecta padrões ("how to fix X", "best Y for Z").
- **App actual:** NÃO existe.
- **Impacto:** patterns são a **base para gerar EAV combinations programáticas**. Sem patterns detectados, qualquer geração é cega.
- **Implementação:** SQL/JS sem ML pesada. ~80 linhas.

#### P0 #3 — EAV combination generator
- **Ensina (Aula 1 / final):** dado entity + attribute + variables, gerar todas as combinações (ex: 1 × 356 raças × 8 food types × 8 needs ≈ 26k variações) e validar contra search volume + SERP analysis.
- **App actual:** NÃO existe. ETAPA 7 do `[[../../SEMANTIC-KW-PIPELINE-DESIGN]]` desenha isto, mas zero código.
- **Impacto:** **é o output final do método EAV**. Sem isto, a extracção é inerte — entities/attributes ficam no DB mas nunca geram queries novas.
- **Implementação:** ~2 dias. Inclui validação via DataForSEO (search volume + SERP).

### P1 — High (capacidade analítica do módulo)

#### P1 #4 — Knowledge Graph integration
- **Ensina (Aula 2 / final):** Google KG Search API devolve metadata (Wiki URL, KG ID, descrição) + top-N entidades relacionadas (5 default).
- **App actual:** NÃO existe.
- **Impacto:** enriquece ETAPA 2 com referências real-world + expansão automática do universo via "related entities".
- **Quota:** 100k chamadas/dia gratuita.
- **Implementação:** <100 linhas. Quick win.

#### P1 #5 — Fuzzy matching para query distance
- **Ensina (Aula 3 / approach 1):** para cada keyword, top-N keywords semanticamente próximas + similarity score. Detecta query sequences/paths sem necessitar LLM.
- **App actual:** comentário `// Try exact and fuzzy matching` em `keyword-mapper.ts` mas zero implementação.
- **Implementação:** `fuse.js` ou `string-similarity`. ~30 linhas.

#### P1 #6 — DataForSEO SERP scraping
- **Ensina (Aula 3 / approach 2):** scrape de Related Searches, PAA, People Also Search For, People Search Next — indicam query path semanticamente relacionada.
- **App actual:** DataForSEO está no stack mas **não usado para SERP scrape**. ETAPA 5 do `[[../../SEMANTIC-KW-PIPELINE-DESIGN]]` planeia isto.
- **Implementação:** ~150 linhas.

### P2 — Medium

#### P2 #7 — Google Autocomplete (Aula 4)
- Search auto-suggest + YouTube auto-suggest. Não precisa API key — scrape directo. ~50 linhas.
- Trade-off: autocomplete dá "next likely query"; SERP dá "related queries". **São complementares.**

#### P2 #8 — Semantic relationship graph (TF-IDF + cosine)
- Visualização e análise topológica das relações entre entidades.
- Interesse mais analítico do que operacional. Pode ser produzido on-demand para o Rui inspeccionar o universo de entidades.

#### P2 #9 — K-means clustering de entidades + PCA visualization
- Usado para "topical authority" decisions: que clusters expandir baseado em proximidade ao que já se rankeia.
- Verificar primeiro se `clustering-service` (já existe no stack) faz isto.

### P3 — Discutíveis / fora de scope imediato

- Persona-based query maps cross-platform (Pinterest/TikTok/etc.) — Aula 3 / approach 5
- User interviews / surveys — Aula 3 / approach 4 (input qualitativo offline; não é trabalho de código)

---

## 📂 Divergência Doc Design vs Implementação

`[[../../SEMANTIC-KW-PIPELINE-DESIGN]]` **desenha ETAPA 2 como heurística pattern-based + dictionary lookup** (PT-PT regex patterns hardcoded). A implementação real **usa Claude CLI**. O design doc precisa de update — feito separadamente em commit dedicado.

---

## 🎯 Sequenciamento de Execução Recomendado

Ordem por retorno × esforço:

1. **P0 #1 + P0 #2** — Custom prominence + co-occurring n-grams. Juntos: ~1 dia. Desbloqueiam ETAPA 3 (Validation) que está desenhada no pipeline-design.
2. **P0 #3** — EAV combination generator. ~2 dias. Output principal do método.
3. **P1 #4** — Knowledge Graph enrichment. ~½ dia. Quick win, alto valor analítico.
4. **P1 #6** — DataForSEO SERP scrape. ~1 dia. Alimenta query paths e content gap detection.
5. **P1 #5 + P2 #7** — Fuzzy matching + Autocomplete. Juntos: ~1 dia.
6. **P2 #8 + P2 #9** — Semantic graph + K-means. ~1 dia juntos (analítico).

**Total:** ~5-6 dias para fechar o módulo "Fundamentals of Semantic KW Research" inteiro em código.

---

## 🔗 Tasks Lançadas

Cada P0/P1/P2 acima tem task correspondente em `memory/todo.md` secção "Module 1 Semantic KW — Recomendação 2026-05-07". Cada uma deve ser executada como uma task force dedicada, com auditor agent no fim.

Template do prompt da task force + auditor: ver `vault/04-Templates/TASK-FORCE-MODULE-1-TEMPLATE.md` (criado nesta sessão).

---

## 🔗 Relacionados

- `[[SOP-2-KEYWORD-RESEARCH-V2]]` — Pipeline operacional onde estes outputs são consumidos
- `[[CONCEITO-Keyword-Research]]` — Conceito hub
- `[[../../SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS]]` — Material-fonte completo (17 lições MLforSEO)
- `[[../../SEMANTIC-KW-PIPELINE-DESIGN]]` — ETAPA 1-9 design (precisa update vs Claude)
- `[[../../ETAPA2_DOCUMENTATION_INDEX]]` — Índice de docs ETAPA 2
- `[[../../ETAPA2_IMPROVEMENT_SUMMARY]]` — Última iteração do prompt
