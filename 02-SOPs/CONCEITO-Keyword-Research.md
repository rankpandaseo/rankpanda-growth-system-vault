---
name: conceito-keyword-research
description: Central hub for keyword research methodology, data sources,
analysis patterns, and decision frameworks across RankPanda 45D sprint
type: conceito
status: active
foco: seo
tags: [keyword-research, methodology, data-sources, analysis, intent-mapping]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[FASE-1-DIAGNOSTIC]],
[[FASE-2-EXECUTION]], [[SOP-3-CLUSTERING-COLLECTION-MAPPING]],
[[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# CONCEITO — Keyword Research (Hub Agregador)

**Resumo:** Central hub para toda a metodologia, fontes de dados, padrões de análise e decisões de keyword research. Agrupa conceitos de SOP-2, insights de FASE-1, e aplicação prática em FASE-2.

---

## 🎯 Por Que Isto Importa

- **Coesão entre fases:** Keyword research não é isolado. FASE-1 (diagnóstico) alimenta SOP-2 (pipeline), que alimenta SOP-3 (clustering), que alimenta FASE-2 (execução). Hub liga tudo.
- **Decision framework consistente:** "High volume + low difficulty = P0" é critério objectivo que evita bias. Mesma regra aplica-se a todos os clientes.
- **Padrões replicáveis:** Quick Wins, Strategic Clusters, Long-tail Accumulation são 3 estratégias que funcionam em 90%+ dos casos. Documentado aqui, executado em todo o sprint.

---

## ⚡ Quick Checklist

- [ ] SE Ranking data de keywords disponível (volume, difficulty, trends)
- [ ] GSC baseline extraído (keywords que já rankeiam)
- [ ] Cliente definiu intent match (quais keywords fazem sentido para o negócio)
- [ ] SOP-2 pipeline aplicado (Claude gate → DataForSEO → Crawl4AI)
- [ ] Clustering definido por SOP-3 (keywords agrupadas por intent)
- [ ] 3 padrões replicáveis mapeados (Quick Wins, Strategic Clusters, Long-tail)

---

## 📖 Conteúdo Principal

1. **Volume** — Quantas pessoas procuram por mês? (SE Ranking)
2. **Difficulty** — Quão competitivo é o termo? (SE Ranking)
3. **Intent Match** — Encaixa com o que o cliente vende? (Manual) **Padrão de
Decisão:**
```
HIGH volume + LOW difficulty + HIGH intent match = P0 (Quick Win)
HIGH volume + MEDIUM difficulty + HIGH intent match = P1 (Investimento
estratégico)
LOW volume + LOW difficulty + HIGH intent match = P2 (Long-tail, acumular
volume)
HIGH volume + HIGH difficulty + LOW intent match = Skip (não vale esforço)
``` **Referência:** [[FASE-1-DIAGNOSTIC]] — Competitive context alimenta priorização --- ### 3. **Estrutura de KW Briefing (Cliente Approval)** **Elementos Obrigatórios por Collection:**
1. ✅ SE Ranking data validada (não estão vencidos, volume realista)
2. ✅ GSC data comparada (keywords já rankeiam?)
3. ✅ Cliente aprovou briefing (sign-off formal)
4. ✅ Integração com clustering confirmada (KW → collection mapeados) **Feedback
Loop:**
FASE 1 — DIAGNOSTIC
└─ Competitive analysis + GSC insights └─ Identifica gaps (keywords competitors
rankeiam que nós não) FASE 2 — EXECUTION (SOP-2)
├─ SE Ranking + GSC + Claude
├─ Estruturar briefing
├─ Client approval
└─ Document keywords.json + learnings FASE 2 — EXECUTION (SOP-3)
├─ Pega keywords aprovadas
├─ Clusters por intent + volume
└─ Mapeia para collections → titles, meta desc, schema FASE 3 — VALIDATION
├─ Compara: keywords rankeadas semana 5 vs semana 1
├─ Identifica: novas keywords que subiram de posição
└─ Insights: qual clustering funcionou melhor?
``` --- ## 💡 Padrões Replicáveis ### Pattern 1 — Quick Wins (3 dias) **Quando:** Cliente tem keywords em GSC com volume mas posição baixa (pos 15+) **Como:**
1. Extrair keywords de GSC (volume > 10/mês, pos > 10)
2. Otimizar titles/meta desc para esses keywords (sem novo conteúdo)
3. Submeter a GSC
4. Monitorar posição (esperar 2 semanas) **Resultado esperado:** 10-15 keywords
sobem para top 5 em 4 semanas ### Pattern 2 — Strategic Clusters (2 semanas)
**Quando:** 5-10 keywords de alto volume, clustering claro (e.g., "vibrador"
variations) **Como:**
1. SE Ranking: extrair todas as variações semânticas
2. Cluster por intent + diferenciação (e.g., "vibrador em silicone", "vibrador à
prova de água")
3. 1 collection principal + 2-3 sub-clusters (product filters/categories)
4. Cada cluster tem keywords mapeadas + content diferenciado **Resultado
esperado:** Dominar família inteira de keywords (pos 1-10 para 80% do cluster)
### Pattern 3 — Long-tail Accumulation (4+ semanas) **Quando:** 50+ produtos com
potencial mas baixo tráfego individual **Como:**
1. Extrair long-tail keywords de SE Ranking (volume < 50/mês, difficulty < 20)
2. Batch-aplicar a product titles/descriptions (Shopify bulk API)
3. Monitorar GSC por 4 semanas
4. Identificar winners (keywords que sobem) vs losers (não indexar) **Resultado esperado:** Acumular 200+ long-tail keywords em top 50, +30% tráfego total --- ## 🛠️ Ferramentas & Integração | Ferramenta | Uso | Integration |
|---|---|---|
| **SE Ranking API** | Volume, difficulty, SERP trends | Direct Python/Node calls |
| **GSC** | Queries que já rankeiam | Monthly export + analysis |
| **GA4** | Query patterns de conversão | Dashboard analysis |
| **Claude** | Brainstorm KW variations + intent | Batch analysis |
| **Shopify API** | Bulk apply keywords a titles/meta | GraphQL mutations | --- ## 📊 Métricas de Sucesso **Por Collection:**

---

## 🔗 Relacionados

- [[SOP-2-KEYWORD-RESEARCH-V2]] — Pipeline API-first que operacionaliza este conceito
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Clustering de keywords por intent
- [[FASE-1-DIAGNOSTIC]] — Competitive analysis que alimenta priorização
- [[FASE-2-EXECUTION]] — Aplicação prática de keywords em collections + products

---
