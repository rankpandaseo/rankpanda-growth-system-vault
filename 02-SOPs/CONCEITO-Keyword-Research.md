---
name: conceito-keyword-research
description: Central hub for keyword research methodology, data sources, analysis patterns, and decision frameworks across RankPanda 45D sprint
type: conceito
status: active
foco: seo
tags: [keyword-research, methodology, data-sources, analysis, intent-mapping]
wikilinks: [[[SOP-2-KEYWORD-RESEARCH-V2]], [[FASE-1-DIAGNOSTIC]], [[FASE-2-EXECUTION]], [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[pilot-vibradores]]]
---

# CONCEITO — Keyword Research (Hub Agregador)

**Resumo:** Central hub para toda a metodologia, fontes de dados, padrões de análise e decisões de keyword research. Agrupa conceitos de SOP-2, insights de FASE-1, e aplicação prática em FASE-2.

---

## 🎯 Propósito deste Hub

Este documento é um **aggregator** para todo o conhecimento de keyword research transversal. Quando perguntas:
- "Como estruturamos KW research no RankPanda?"
- "Quais são as fontes de dados confiáveis?"
- "Como fazemos prioritização de keywords?"
- "Qual é o fluxo de aprovação de cliente?"

→ Este hub aponta para o local correto na documentação + padrões replicáveis.

---

## 📚 Estrutura Conceptual

### 1. **Fundações — De Onde Vêm Keywords?**

**Fontes Primárias:**
- **SE Ranking API** — Volume, dificuldade, SERP features
- **Google Search Console (GSC)** — Keywords actuais que já rankeiam (low-hanging fruit)
- **Google Analytics 4** — Query patterns de tráfego que converte
- **Análise Manual** — Brain-dump do cliente, conhecimento de domínio

**Integração:**
- SE Ranking + GSC = keywords que já traem tráfego (otimizar posição)
- SE Ranking + GA4 = keywords em volume que NÃO trazem tráfego ainda (gap)
- Análise manual = keywords estratégicas que merecem investimento

**Referência:** [[SOP-2-KEYWORD-RESEARCH-V2]] — Workflow completo

---

### 2. **Análise — Como Priorizamos?**

**Modelo de Priorização (3 dimensões):**
1. **Volume** — Quantas pessoas procuram por mês? (SE Ranking)
2. **Difficulty** — Quão competitivo é o termo? (SE Ranking)
3. **Intent Match** — Encaixa com o que o cliente vende? (Manual)

**Padrão de Decisão:**
```
HIGH volume + LOW difficulty + HIGH intent match = P0 (Quick Win)
HIGH volume + MEDIUM difficulty + HIGH intent match = P1 (Investimento estratégico)
LOW volume + LOW difficulty + HIGH intent match = P2 (Long-tail, acumular volume)
HIGH volume + HIGH difficulty + LOW intent match = Skip (não vale esforço)
```

**Referência:** [[FASE-1-DIAGNOSTIC]] — Competitive context alimenta priorização

---

### 3. **Estrutura de KW Briefing (Cliente Approval)**

**Elementos Obrigatórios por Collection:**
- **Primary Keywords** (3-5) — Main target, maior volume/relevância
- **Secondary Keywords** (5-10) — Supporting, semântica relacionada
- **Long-tail Variations** — Volume menor, intent muito específico
- **Search Volume + Difficulty** — Dados concretos
- **Intent Classification** — Transactional, informational, navigational

**Formato de Aprovação:**
- Enviar form estruturado ao cliente
- Cliente aprova ou pede ajustes
- Uma vez aprovado = locked-in para FASE 2

**Referência:** [[SOP-2-KEYWORD-RESEARCH-V2]] — Seção "Como Fazer KW Research"

---

### 4. **Mapeamento KW → Collections (Semantic Linking)**

**Padrão:**
- Cada collection tem 1-3 "primary keywords" que devem estar em:
  - Title tag (60 chars, keyword-rich)
  - Meta description (120-155 chars, com CTA implícito)
  - H1 (natural language, não stuffing)
  - Schema.org ProductCollection (JSON-LD)

**Integração com SOP-3:**
- SOP-2 = keywords finalizadas
- SOP-3 = clustering (qual keyword → qual collection)
- FASE-2 = aplicação em Shopify (metafields, schema)

**Referência:** [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Bidirectional mapping

---

### 5. **Validação & Iteração**

**Checkpoints:**
1. ✅ SE Ranking data validada (não estão vencidos, volume realista)
2. ✅ GSC data comparada (keywords já rankeiam?)
3. ✅ Cliente aprovou briefing (sign-off formal)
4. ✅ Integração com clustering confirmada (KW → collection mapeados)

**Feedback Loop:**
- Se cliente rejeita keywords propostas → reanalisar intent
- Se em FASE-2 vemos que keywords não convertem → learnings para futuro

**Referência:** [[FASE-2-EXECUTION]] — Implementação e monitoragem

---

## 🔄 Fluxo Cross-Phase

```
FASE 1 — DIAGNOSTIC
└─ Competitive analysis + GSC insights
   └─ Identifica gaps (keywords competitors rankeiam que nós não)

FASE 2 — EXECUTION (SOP-2)
├─ SE Ranking + GSC + Claude
├─ Estruturar briefing
├─ Client approval
└─ Document keywords.json + learnings

FASE 2 — EXECUTION (SOP-3)
├─ Pega keywords aprovadas
├─ Clusters por intent + volume
└─ Mapeia para collections → titles, meta desc, schema

FASE 3 — VALIDATION
├─ Compara: keywords rankeadas semana 5 vs semana 1
├─ Identifica: novas keywords que subiram de posição
└─ Insights: qual clustering funcionou melhor?
```

---

## 💡 Padrões Replicáveis

### Pattern 1 — Quick Wins (3 dias)

**Quando:** Cliente tem keywords em GSC com volume mas posição baixa (pos 15+)

**Como:**
1. Extrair keywords de GSC (volume > 10/mês, pos > 10)
2. Otimizar titles/meta desc para esses keywords (sem novo conteúdo)
3. Submeter a GSC
4. Monitorar posição (esperar 2 semanas)

**Resultado esperado:** 10-15 keywords sobem para top 5 em 4 semanas

### Pattern 2 — Strategic Clusters (2 semanas)

**Quando:** 5-10 keywords de alto volume, clustering claro (e.g., "vibrador" variations)

**Como:**
1. SE Ranking: extrair todas as variações semânticas
2. Cluster por intent + diferenciação (e.g., "vibrador em silicone", "vibrador à prova de água")
3. 1 collection principal + 2-3 sub-clusters (product filters/categories)
4. Cada cluster tem keywords mapeadas + content diferenciado

**Resultado esperado:** Dominar família inteira de keywords (pos 1-10 para 80% do cluster)

### Pattern 3 — Long-tail Accumulation (4+ semanas)

**Quando:** 50+ produtos com potencial mas baixo tráfego individual

**Como:**
1. Extrair long-tail keywords de SE Ranking (volume < 50/mês, difficulty < 20)
2. Batch-aplicar a product titles/descriptions (Shopify bulk API)
3. Monitorar GSC por 4 semanas
4. Identificar winners (keywords que sobem) vs losers (não indexar)

**Resultado esperado:** Acumular 200+ long-tail keywords em top 50, +30% tráfego total

---

## 🛠️ Ferramentas & Integração

| Ferramenta | Uso | Integration |
|---|---|---|
| **SE Ranking API** | Volume, difficulty, SERP trends | Direct Python/Node calls |
| **GSC** | Queries que já rankeiam | Monthly export + analysis |
| **GA4** | Query patterns de conversão | Dashboard analysis |
| **Claude** | Brainstorm KW variations + intent | Batch analysis |
| **Shopify API** | Bulk apply keywords a titles/meta | GraphQL mutations |

---

## 📊 Métricas de Sucesso

**Por Collection:**
- Baseline: Quantas keywords rankeavam antes? Qual posição?
- Target: +50% keywords em top 10 após 4 semanas
- Win condition: Principais 3 keywords em pos 1-5

**Por Sprint:**
- Novo tráfego gerado: X clicks/semana (comparar semana 1 vs semana 5)
- Revenue impact: Clicks × CR × AOV = $estimado
- Learnings: Qual clustering funcionou melhor? Por quê?

**Documentação:**
- Guardar keywords.json no vault (source of truth)
- Documentar decisões de prioritização (por quê estes keywords?)
- Capture learnings em pepitas-de-ouro.md

---

## 🔗 Relacionados

**SOPs & FASEs que dependem deste conceito:**
- [[SOP-2-KEYWORD-RESEARCH-V2]] → Implementação completa de KW research
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] → Clustering baseado em keywords aprovadas
- [[FASE-1-DIAGNOSTIC]] ← Competitive insights informam priorização
- [[FASE-2-EXECUTION]] → Onde keywords são implementadas + monitoradas
- [[FASE-3-VALIDATION]] → Medição de impacto (novas keywords rankeadas)

**Casos Reais:**
- [[pilot-vibradores]] → Implementação end-to-end de KW research em projeto piloto

**Recursos:**
- `/vault/04-Templates/approval-gate-keywords.md` — Template de aprovação de keywords
- `/vault/05-Curso-45D/pepitas-de-ouro.md` — Learnings de KW research acumulados

---

**Versão:** 1.0  
**Data:** 2026-04-21  
**Status:** ACTIVE  
**Próximo:** Validação de integração com todos SOPs/FASEs
