# SOP FASE 3 — Validação + Growth Roadmap (Semana 4-5)

## 🎯 Objetivo

Provar impacto, preparar continuidade, definir prescrição para crescimento pós-sprint.

---

## CAMADA 1 — AUDITORIA (Weak Points Detection)

### Checklist de Validação

**Metrics Capture:**
- [ ] Indexed pages before/after recolhidas
- [ ] Impressions before/after recolhidas
- [ ] Clicks before/after recolhidas
- [ ] Average position before/after calculada
- [ ] Core Web Vitals before/after medidos

**Impact Analysis:**
- [ ] New queries que rankeiam identificadas
- [ ] Keywords que subiram de posição documentadas
- [ ] Traffic projection 90D calculada
- [ ] Revenue impact estimada

**Continuation Planning:**
- [ ] 90D roadmap definido
- [ ] 6M roadmap esboçado
- [ ] 3 opções de continuidade apresentadas ao cliente
- [ ] Next steps claros

### Gaps Identified

_Se há gaps na execução:_

**Gap:** [descrição]
- **Causa:** [root cause]
- **Impact:** [no metrics, client satisfaction, etc]
- **Learning:** [para future sprints]

---

## CAMADA 2 — FORMATIVO (How-To / Teaching Module)

### Porque Validação é Crítica

Sem validação clara:
- Não sabemos se 45D valeu a pena
- Cliente fica inseguro sobre continuidade
- Não temos dados para prescrição futura
- Não capturamos learnings

**Princípio:** Data transparency. Cliente vê antes/after. Credibilidade gerada.

### Como Fazer Before/After Report

**Timeline:** Comparação Dia 1 (Fase 0) vs Dia 35 (Fim Fase 2)

**Métricas a capturar:**

1. **GSC Metrics:**
   - Indexed pages: Comparar count
   - Impressions: 4-week average before vs after
   - Clicks: 4-week average before vs after
   - Average position: Median position change
   - New queries ranking: Quantas keywords novas

2. **Performance Metrics:**
   - Core Web Vitals: LCP, FID, CLS before/after
   - Mobile score improvement
   - Page speed comparison

3. **Volume Metrics:**
   - Collections optimized: 5-10
   - Products optimized: 50-200+
   - Schema coverage: before/after %

**How to gather:**
1. Login to GSC
2. Date range: Semana 1 (Fase 0 baseline) vs Semana 5 (end Fase 2)
3. Export data
4. Calculate % change
5. Create simple chart (visual impact)

### Como Fazer Semantic Impact Analysis

**Novas keywords rankeando:**
1. GSC: Compare queries list between date ranges
2. Identify keywords that appear in Week 5 but not in Week 1
3. Document volume + position for each
4. Example: "vibradores em silicone" now ranks position 15 (before: not in top 100)

**Keywords que subiram:**
1. GSC: Compare position for same keywords
2. Identify movement (e.g., "vibrador" went from pos 45 → pos 12)
3. Quantify impact (click lift from position change)

**Traffic projection:**
1. Current: X clicks/week at current positions
2. Estimate: If positions move closer to top 3 (CTR goes up), expect Y clicks/week
3. Calculate expected sessions in 90D (12 weeks × avg clicks/week)
4. Revenue estimate: sessions × conversion rate × AOV

### Como Estruturar Roadmap 90D + 6M

**90D Roadmap (próxima fase):**

Based on diagnostic + execution learnings:
- Qual será a próxima ação de maior impacto?
- Examplos: otimizar mais X produtos, criar Y peças de conteúdo, implementar Z estratégia
- Timeline + effort estimate

**6M Roadmap:**
- Qual é a visão a 6 meses?
- Examplos: estar rankeado em top 10 para N keywords, gerar P sessões/mês, contribute Q% da revenue
- Estratégia de continuidade (blog content, link building, local SEO, etc)

### Como Apresentar 3 Opções de Continuidade ao Cliente

**Opção 1 — Consultoria À La Carte**
- Continuidade mensal: X horas/mês
- Escopo: Prescrição em blocos (categorias, feeds, conteúdo, etc)
- Investment: $$$/month
- Best for: Clientes com budget e vontade de crescer steady

**Opção 2 — Auditoria Aprofundada**
- Se identificadas issues estruturais grandes
- Scope: Diagnóstico completo + plano de ação detalhado
- Investment: $$$ one-time
- Best for: Clientes que querem compreender raiz dos problemas

**Opção 3 — Self-Service + Checkpoints**
- Cliente implementa roadmap sozinho
- RankPanda faz checkpoints mensais (1h call)
- Investment: $/month (minimal)
- Best for: Clientes com equipa interna, budget limitado

---

## CAMADA 3 — TEMPLATE ClickUp (Operational Tasks)

### ClickUp Space Structure (FASE 3)

**Project:** `[Loja] — 45D Sprint → FASE 3 Validation`

**Using Templates:** See `/04-Templates/` for before-after-report-template.md and pepita-capture-template.md

**Folders:**

1. **METRICS COLLECTION**
   - [ ] GSC before/after data downloaded
   - [ ] GA4 before/after data downloaded
   - [ ] Core Web Vitals measured
   - [ ] Calculations done

2. **BEFORE/AFTER REPORT**
   - [ ] Indexed pages growth calculated
   - [ ] Impressions growth calculated
   - [ ] Clicks growth calculated
   - [ ] Position movement analyzed
   - [ ] Visual charts created

3. **SEMANTIC IMPACT**
   - [ ] New keywords identified
   - [ ] Keywords position movement tracked
   - [ ] Traffic projection calculated
   - [ ] Revenue estimate done

4. **OPPORTUNITY MAPPING**
   - [ ] 90D roadmap drafted
   - [ ] 6M roadmap outlined
   - [ ] Next opportunities identified

5. **CONTINUITY PRESCRIPTION**
   - [ ] 3 options presented
   - [ ] Client feedback gathered
   - [ ] Contract prepared (if applicable)

6. **CLOSING**
   - [ ] Final presentation done
   - [ ] Client sign-off obtained
   - [ ] Celebration 🎉

### Tarefas Específicas (9 Tasks)

#### Task 1 — Collect Metrics
- **Assignee:** [RankPanda analytics]
- **Due:** Day 29-30
- **Description:** Download GSC, GA4, CWV data for before/after comparison. Store in Vault.
- **Dependencies:** Fase 2 complete

#### Task 2 — Calculate Before/After
- **Assignee:** [RankPanda analytics]
- **Due:** Day 31
- **Description:** Compare Week 1 vs Week 5. Calculate % growth. Create chart.
- **Dependencies:** Task 1

#### Task 3 — Semantic Analysis
- **Assignee:** [RankPanda SEO]
- **Due:** Day 32
- **Description:** Identify new keywords, position movements. Estimate 90D impact.
- **Dependencies:** Task 1

#### Task 4 — Opportunity Mapping
- **Assignee:** [RankPanda owner]
- **Due:** Day 33-34
- **Description:** Draft 90D + 6M roadmaps. Identify next biggest opportunities.
- **Dependencies:** Task 3

#### Task 5 — Continuity Options
- **Assignee:** [RankPanda owner]
- **Due:** Day 34
- **Description:** Prepare 3 continuity options with pricing/scope. Draft proposal.
- **Dependencies:** Task 4

#### Task 6 — Create Final Presentation
- **Assignee:** [RankPanda owner]
- **Due:** Day 35
- **Description:** Compile before/after, impact analysis, roadmap, options into presentation deck or Loom.
- **Dependencies:** Tasks 2, 3, 4, 5

#### Task 7 — Final Presentation Call
- **Assignee:** [RankPanda owner]
- **Due:** Day 35-36
- **Description:** Call com cliente. Present findings. Discuss continuity options. Get feedback.
- **Dependencies:** Task 6

#### Task 8 — Document Learnings
- **Assignee:** [RankPanda owner]
- **Due:** Day 36-37
- **Description:** Record pepitas de ouro (learnings). Update Vault. Update course material.
- **Dependencies:** Task 7

#### Task 9 — Close Sprint
- **Assignee:** [RankPanda owner]
- **Due:** Day 37
- **Description:** Archive ClickUp tasks. Send thank you to client. Mark Sprint complete.
- **Dependencies:** All above

---

## ✅ Entregáveis Fase 3

1. ✅ Before/After report com métricas claras
2. ✅ Semantic impact analysis (new keywords, position changes)
3. ✅ Traffic projection 90D + revenue estimate
4. ✅ 90D + 6M roadmaps definidos
5. ✅ 3 opções de continuidade com pricing
6. ✅ Pepitas de ouro documentadas (learnings for future)
7. ✅ Client sign-off + celebration

---

## 📊 Exemplo de Relatório

**Loja XYZ — 45D Sprint Results**

**Before (Dia 1):**
- Indexed pages: 250
- Monthly impressions: 1,200
- Monthly clicks: 45
- Average position: 23

**After (Dia 35):**
- Indexed pages: 380 (**+52%**)
- Monthly impressions: 2,100 (**+75%**)
- Monthly clicks: 120 (**+167%**)
- Average position: 18 (**-5 positions**)

**New Keywords Ranking:**
- "vibrador em silicone": pos 15
- "vibrador à prova de água": pos 12
- "vibrador para mulher": pos 8
- ... (3 more)

**Impact:**
- Projected 90D organic sessions: **2,400** (at current growth rate)
- Estimated revenue impact (at 5% conv, $50 AOV): **~$6,000**

**Next Opportunities:**
- Optimize 200+ more products
- Create 10 category guides
- Implement product feeds

---

**Versão:** 1.0  
**Última Atualização:** [data]  
**Owner:** [nome]
