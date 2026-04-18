# SOP FASE 1 — Diagnóstico Estratégico (Semana 1-2)

## 🎯 Objetivo

Descobrir o que está a travar crescimento orgânico e indexação através de análise estruturada (não auditoria completa).

---

## CAMADA 1 — AUDITORIA (Weak Points Detection)

### Checklist de Diagnóstico

**GSC Analysis:**
- [ ] Coverage report analisado (descobertas, rastreadas, indexadas)
- [ ] Indexation gaps por tipo identificados (produtos vs coleções vs outras)
- [ ] Canonical issues documentados
- [ ] Robots.txt validado
- [ ] Sitemap.xml validado
- [ ] Mobile usability issues listados

**GA4 Analysis:**
- [ ] Organic traffic trends (últimos 90 dias) extraídos
- [ ] Top landing pages (onde vem o tráfego) identificadas
- [ ] Conversion funnel análisado
- [ ] Bounce rate por page type calculado
- [ ] Event tracking validado

**Technical Foundation:**
- [ ] Core Web Vitals analisados (LCP, FID, CLS)
- [ ] Mobile responsiveness testado
- [ ] Page speed benchmarks
- [ ] Schema.org coverage atual

**Competitive Landscape:**
- [ ] Top 5 competitors SEO mapeados
- [ ] Suas top keywords listadas
- [ ] Collection structure deles comparada
- [ ] Content strategy overview documentado

### Gaps Identificados

_Preencher durante FASE 1:_

**Gap 1:** [descrição + impacto]
**Gap 2:** [descrição + impacto]
**Gap 3:** [descrição + impacto]
...

**Priorização:** Quais 3-5 gaps têm maior impacto no crescimento?

---

## CAMADA 2 — FORMATIVO (How-To / Teaching Module)

### Porque é Diagnóstico Importante

Sem diagnóstico claro:
- Vamos otimizar coisas erradas
- Vamos gastar tempo em low-impact fixes
- Vamos perder oportunidades óbvias
- Cliente vai desconfiar (why these recommendations?)

**Princípio:** Data-driven decision making. Nunca assumir; sempre verificar.

### Como Fazer GSC Analysis

1. **Abrir GSC** → "Coverage" report
2. **Ler gráfico de cobertura:**
   - Linhas vermelhas (erros) → normalmente 404s ou bloqueadas
   - Linhas laranja (aviso) → descobertas mas não indexadas
   - Linhas azuis (sucesso) → indexadas
3. **Identificar padrões:**
   - Todas as products têm erro? → Canonical issue, robots.txt bloqueando, etc
   - Coleções indexadas mas não products? → Estrutura problema
   - Tudo OK mas poucas impressões? → Problema de visibilidade (content, links)

4. **Documentar findings:**
   - Quantas páginas indexadas?
   - Quantas descobertas mas não indexadas?
   - Qual é o gap?

### Como Fazer GA4 Analysis

1. **Ir a Acquisition → Organic Search**
2. **Analisar trending:**
   - Sessions growing, flat, or declining?
   - From which pages is traffic coming?
   - What's the conversion rate?

3. **Analisar landing pages:**
   - Top 10 pages by sessions
   - Compare bounce rate (high bounce = problema)
   - Compare conversion rate

4. **Documentar:**
   - Organic sessions/month (trend)
   - Top 3 landing pages
   - Average conversion rate
   - Where is the traffic going? (categories, products, blog?)

### Como Mapear Competitive Landscape

1. **Identificar top 5 competitors** (SEO, não só brand)
2. **Para cada competitor, analisar:**
   - Usando SE Ranking ou similar: top 20 keywords ranked
   - Collection structure (quantas coleções, nomes, keywords)
   - Content strategy (têm blog? Quanto conteúdo?)
   - Backlink profile (rough)

3. **Documentar gaps vs competitors:**
   - Keywords eles rankeiam que nós não
   - Content que eles têm que nós não
   - Structure diferenças

---

## CAMADA 3 — TEMPLATE ClickUp (Operational Tasks)

### ClickUp Space Structure (FASE 1)

**Project:** `[Loja] — 45D Sprint → FASE 1 Diagnostic`

**Using Templates:** See `/04-Templates/` for weekly-update-template.md and before-after-report-template.md

**Folders:**

1. **GSC ANALYSIS**
   - [ ] Coverage report downloaded
   - [ ] Gaps identified + documented
   - [ ] Indexation issues prioritized

2. **GA4 ANALYSIS**
   - [ ] Traffic trends charted
   - [ ] Top pages identified
   - [ ] Conversion funnel analyzed

3. **TECHNICAL AUDIT**
   - [ ] Core Web Vitals measured
   - [ ] Mobile testing completed
   - [ ] Schema coverage checked

4. **COMPETITIVE LANDSCAPE**
   - [ ] Top 5 competitors mapped
   - [ ] Keywords gap analysis
   - [ ] Content comparison

5. **REPORTING**
   - [ ] Insights synthesized
   - [ ] Opportunities prioritized
   - [ ] Loom video recording (optional)
   - [ ] Client presentation ready

### Tarefas Específicas (7 Tasks)

#### Task 1 — GSC Coverage Analysis
- **Assignee:** [RankPanda analytics]
- **Due:** Day 1-2
- **Description:** Download coverage report. Analyze indexation gaps by page type. Document findings in Vault.
- **Dependencies:** Baseline metrics (FASE 0)

#### Task 2 — GA4 Traffic Analysis
- **Assignee:** [RankPanda analytics]
- **Due:** Day 2-3
- **Description:** Extract 90-day trends, top pages, conversion funnel. Create simple chart.
- **Dependencies:** Nenhuma

#### Task 3 — Technical Audit
- **Assignee:** [RankPanda tech]
- **Due:** Day 3-4
- **Description:** Run PageSpeed Insights, mobile test, schema validator. Document findings.
- **Dependencies:** Nenhuma

#### Task 4 — Competitive Analysis
- **Assignee:** [RankPanda SEO]
- **Due:** Day 4-5
- **Description:** Map top 5 competitors, extract top keywords, analyze collection structure.
- **Dependencies:** Nenhuma (pode correr paralelo)

#### Task 5 — Synthesis & Prioritization
- **Assignee:** [RankPanda owner]
- **Due:** Day 5-6
- **Description:** Consolidate all findings. Identify 3-5 highest-impact opportunities. Draft presentation.
- **Dependencies:** Tasks 1-4

#### Task 6 — Client Communication
- **Assignee:** [RankPanda owner]
- **Due:** Day 7
- **Description:** Send Loom + summary to client. Gather feedback.
- **Dependencies:** Task 5

#### Task 7 — Approve to PHASE 2
- **Assignee:** [RankPanda owner]
- **Due:** Day 7
- **Description:** Client sign-off on diagnostic. Confirm top 5-10 collections para otimizar. Go/No-go FASE 2.
- **Dependencies:** Task 6

---

## ✅ Entregáveis Fase 1

1. ✅ Diagnóstico estruturado (GSC, GA4, Technical, Competitive)
2. ✅ 3-5 oportunidades prioritárias identificadas + documentadas
3. ✅ Roadmap de execução para FASE 2 (KW research, collections, products)
4. ✅ Client buy-in (aprovação de estratégia proposta)
5. ✅ Vault atualizado com learnings

---

**Versão:** 1.0  
**Última Atualização:** [data]  
**Owner:** [nome]
