---
name: fase-1-diagnostic
description: Analyze GSC, GA4, technical foundation, and competitive landscape to identify highest-impact opportunities
type: fase
status: active
foco: análise
tags: [diagnostic, gsc-analysis, ga4, competitive, technical-audit]
wikilinks: [[FASE-0-KICKOFF]], [[SOP-2-KEYWORD-RESEARCH-V2]], [[FASE-2-EXECUTION]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
--- # SOP FASE 1 — Diagnóstico Estratégico (Semana 1-2) **Resumo:** Analisar dados de GSC, GA4, performance técnica e landscape competitivo para identificar 3-5 oportunidades de maior impacto. Não é auditoria completa — é diagnóstico focado. --- ## 🎯 Por Que Isto Importa **Impacto na eficácia do sprint:**
- **Data-driven prioritization:** Sem diagnóstico, otimizamos ao acaso. Com diagnóstico claro (GSC gaps, GA4 trends, competitive analysis), sabemos exatamente que 3-5 keywords/coleções vão render mais tráfego com menos esforço.
- **Evita retrabalho:** Se diagnosticamos que problema é indexation (não keywords), focamos em robots.txt/canonical em SOP 4. Se é keywords, focamos em SOP 2-3.
- **Client confidence:** Apresentar diagnóstico claro = cliente vê que recomendações viêm de dados, não de achismo. Buy-in imediato para FASE 2.
- **Baseline para prova de ROI:** Capturamos posição atual de top competitors, keywords que rankiam, tráfego que vem. Em FASE 3, comparamos: "éramos rank 25, agora 5. Impressões subiram de X para Y." **Sem FASE 1 bem feita:** Propomos estratégia sem base. Cliente questiona. Semana perdida. --- ## 📋 Pré-requisitos Antes de começar FASE-1:
- ← [[FASE-0-KICKOFF]] — **Input Obrigatório:** Setup técnico (Shopify access, GSC, GA4 configurados) + baseline metrics capturados (indexed, impressions, clicks, position) --- ## ⚡ Quick Checklist - [ ] GSC coverage report analisado (indexed vs discovered vs errors)
- [ ] Indexation gaps por tipo identificados (product, collection, blog)
- [ ] GA4 organic traffic trends (90 dias) extraídos
- [ ] Top 10 landing pages (por sessões, conversão, bounce rate) documentadas
- [ ] Core Web Vitals medidos (LCP, FID, CLS)
- [ ] Mobile usability testado
- [ ] Top 5 competitors mapeados
- [ ] Competitive keywords gap análisado (eles rankiam, nós não)
- [ ] 3-5 maiores oportunidades identificadas + prioridades
- [ ] Client presentation aprovada → Ready for [[FASE-2-EXECUTION]] --- ## 🔑 Key Principles 1. **Data Over Assumption:** Sempre verificar GSC, GA4, PageSpeed. Nunca recomendar baseado em feeling.
2. **Pareto Focus:** 80% do impacto vem de 20% das oportunidades. Diagnóstico encontra esse 20%.
3. **Competitive Context:** Entender onde competitors rankiam ajuda-nos a atacar gaps reais.
4. **Quick Wins First:** FASE 1 identifica o que pode ser fixado em 3 dias (canonical, robots.txt) vs 21 dias (novo conteúdo).
5. **Documentation for Reuse:** Cada diagnóstico alimenta o playbook. Patterns recorrentes = novos SOPs. --- ## Operacional: ANÁLISE (Weak Points Detection) ### Checklist de Diagnóstico **GSC Analysis:**
- [ ] Coverage report analisado (descobertas, rastreadas, indexadas)
- [ ] Indexation gaps por tipo identificados (produtos vs coleções vs outras)
- [ ] Canonical issues documentados
- [ ] Robots.txt validado
- [ ] Sitemap.xml validado
- [ ] Mobile usability issues listados **GA4 Analysis:**
- [ ] Organic traffic trends (últimos 90 dias) extraídos
- [ ] Top landing pages (onde vem o tráfego) identificadas
- [ ] Conversion funnel análisado
- [ ] Bounce rate por page type calculado
- [ ] Event tracking validado **Technical Foundation:**
- [ ] Core Web Vitals analisados (LCP, FID, CLS)
- [ ] Mobile responsiveness testado
- [ ] Page speed benchmarks
- [ ] Schema.org coverage atual **Competitive Landscape:**
- [ ] Top 5 competitors SEO mapeados
- [ ] Suas top keywords listadas
- [ ] Collection structure deles comparada
- [ ] Content strategy overview documentado ### Gaps Identificados _Preencher durante FASE 1:_ **Gap 1:** [descrição + impacto]
**Gap 2:** [descrição + impacto]
**Gap 3:** [descrição + impacto]
... **Priorização:** Quais 3-5 gaps têm maior impacto no crescimento? --- ## Como Fazer GSC Analysis 1. **Abrir GSC** → "Coverage" report
2. **Ler gráfico de cobertura:** - Linhas vermelhas (erros) → normalmente 404s ou bloqueadas - Linhas laranja (aviso) → descobertas mas não indexadas - Linhas azuis (sucesso) → indexadas
3. **Identificar padrões:** - Todas as products têm erro? → Canonical issue, robots.txt bloqueando, etc - Coleções indexadas mas não products? → Estrutura problema - Tudo OK mas poucas impressões? → Problema de visibilidade (content, links) 4. **Documentar findings:** - Quantas páginas indexadas? - Quantas descobertas mas não indexadas? - Qual é o gap? ### Como Fazer GA4 Analysis 1. **Ir a Acquisition → Organic Search**
2. **Analisar trending:** - Sessions growing, flat, or declining? - From which pages is traffic coming? - What's the conversion rate? 3. **Analisar landing pages:** - Top 10 pages by sessions - Compare bounce rate (high bounce = problema) - Compare conversion rate 4. **Documentar:** - Organic sessions/month (trend) - Top 3 landing pages - Average conversion rate - Where is the traffic going? (categories, products, blog?) ### Como Mapear Competitive Landscape 1. **Identificar top 5 competitors** (SEO, não só brand)
2. **Para cada competitor, analisar:** - Usando SE Ranking ou similar: top 20 keywords ranked - Collection structure (quantas coleções, nomes, keywords) - Content strategy (têm blog? Quanto conteúdo?) - Backlink profile (rough) 3. **Documentar gaps vs competitors:** - Keywords eles rankeiam que nós não - Content que eles têm que nós não - Structure diferenças --- ## Execução: ClickUp Space + Tarefas ### ClickUp Space Structure (FASE 1) **Project:** `[Loja] — 45D Sprint → FASE 1 Diagnostic` **Using Templates:** See `/04-Templates/` for weekly-update-template.md and before-after-report-template.md **Folders:** 1. **GSC ANALYSIS** - [ ] Coverage report downloaded - [ ] Gaps identified + documented - [ ] Indexation issues prioritized 2. **GA4 ANALYSIS** - [ ] Traffic trends charted - [ ] Top pages identified - [ ] Conversion funnel analyzed 3. **TECHNICAL AUDIT** - [ ] Core Web Vitals measured - [ ] Mobile testing completed - [ ] Schema coverage checked 4. **COMPETITIVE LANDSCAPE** - [ ] Top 5 competitors mapped - [ ] Keywords gap analysis - [ ] Content comparison 5. **REPORTING** - [ ] Insights synthesized - [ ] Opportunities prioritized - [ ] Loom video recording (optional) - [ ] Client presentation ready ### Tarefas Específicas (7 Tasks) #### Task 1 — GSC Coverage Analysis
- **Assignee:** [RankPanda analytics]
- **Due:** Day 1-2
- **Description:** Download coverage report. Analyze indexation gaps by page type. Document findings in Vault.
- **Dependencies:** Baseline metrics (FASE 0) #### Task 2 — GA4 Traffic Analysis
- **Assignee:** [RankPanda analytics]
- **Due:** Day 2-3
- **Description:** Extract 90-day trends, top pages, conversion funnel. Create simple chart.
- **Dependencies:** Nenhuma #### Task 3 — Technical Audit
- **Assignee:** [RankPanda tech]
- **Due:** Day 3-4
- **Description:** Run PageSpeed Insights, mobile test, schema validator. Document findings.
- **Dependencies:** Nenhuma #### Task 4 — Competitive Analysis
- **Assignee:** [RankPanda SEO]
- **Due:** Day 4-5
- **Description:** Map top 5 competitors, extract top keywords, analyze collection structure.
- **Dependencies:** Nenhuma (pode correr paralelo) #### Task 5 — Synthesis & Prioritization
- **Assignee:** [RankPanda owner]
- **Due:** Day 5-6
- **Description:** Consolidate all findings. Identify 3-5 highest-impact opportunities. Draft presentation.
- **Dependencies:** Tasks 1-4 #### Task 6 — Client Communication
- **Assignee:** [RankPanda owner]
- **Due:** Day 7
- **Description:** Send Loom + summary to client. Gather feedback.
- **Dependencies:** Task 5 #### Task 7 — Approve to PHASE 2
- **Assignee:** [RankPanda owner]
- **Due:** Day 7
- **Description:** Client sign-off on diagnostic. Confirm top 5-10 collections para otimizar. Go/No-go FASE 2.
- **Dependencies:** Task 6 --- ## Validação & Entregáveis - ✅ Diagnóstico estruturado (GSC, GA4, Technical, Competitive)
- ✅ 3-5 oportunidades prioritárias identificadas + documentadas
- ✅ Roadmap de execução para FASE 2 (KW research, collections, products)
- ✅ Client buy-in (aprovação de estratégia proposta)
- ✅ Vault atualizado com learnings + competitive intelligence --- ## 🔗 Relacionados **Dependências & Fluxo Sequencial:**
- [[FASE-0-KICKOFF]] ← **Input:** Setup técnico + baseline metrics
- [[SOP-2-KEYWORD-RESEARCH-V2]] → **Output:** Insights competitivos alimentam priorização de keywords
- [[FASE-2-EXECUTION]] → **Próximo:** Diagnóstico orienta scope e priorização de execução **Exemplos & Referência:**
- [[PILOT-VIBRADORES-00-MASTER-PLAN]] → **Caso Real:** Diagnóstico real do projeto --- **Versão:** 2.0 **Data:** 2026-04-21 **Status:** ATIVO **Próximo:** [[SOP-2-KEYWORD-RESEARCH-V2]] (baseado em diagnóstico) **Versão:** 2.0 **Data:** 2026-04-21 **Status:** ATIVO **Próximo:** [[FASE-2-EXECUTION]] (após client sign-off de diagnóstico)
