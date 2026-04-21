---
name: template-before-after-report
description: Before/After metrics report template for FASE 3 validation and ROI proof
type: template
status: active
foco: operational
tags: [template, validation, metrics, report, fase-3]
wikilinks: [[FASE-3-VALIDATION]], [[CONCEITO-Client-Approval]]
---

# TEMPLATE — Before/After Report: FASE 3 Metrics

**Resumo:** Google Sheet ou Word template para apresentar resultados completos da FASE 3 — baseline (FASE 0) vs. métricas atuais (FASE 3) com impacto comprovado em GSC, GA4, SE Ranking, ROI. Cliente vê prova da otimização. RankPanda vê oportunidade de continuidade.

---

## 🎯 Por Que Isto Importa

- **Prova de impacto:** Cliente não aprova continuidade sem números. Baseline vs. Current mostra exatamente quanto melhorou (impressões +X%, clicks +Y%, revenue +Z€).
- **ROI justifica investimento:** Sem ROI section, parecemos agência genérica. Com ROI, demonstramos que 45D sprint pagou-se em 60-90 dias e continua a gerar valor.
- **Estrutura para 90D continuity:** Cliente vê resultados → aprova continuidade monthly (€X/month). Cada relatório que enviamos, é nova oportunidade de upsell ou expansion.

---

## ⚡ Quick Checklist

- [ ] Baseline metrics coletadas em FASE 0 (GSC 30d, GA4 30d, SE Ranking)
- [ ] Current metrics coletadas em FASE 3 (GSC últimos 30d, GA4 últimos 30d, SE Ranking)
- [ ] Dados validados (sem gaps, datas corretas)
- [ ] ROI calculado (Investment ÷ Revenue Generated)
- [ ] Deliverables Completed preenchidos (3-5 items reais do que foi feito)
- [ ] Recomendações para continuidade documentadas
- [ ] Client Approval obtida (signed-off)
- [ ] Relatório enviado ao cliente + arquivo no project folder

---

## 📖 Conteúdo Principal

### Report Header

```
BEFORE/AFTER REPORT — FASE 3 Validation
_____________________________________

Client: _________________________ 
Store URL: _________________________
Sprint Duration: 45 days
Report Date: _______________

Reporting Period:
  Baseline: _____________ (FASE 0 snapshot, 30-day window)
  Current: _____________ (FASE 3 snapshot, 30-day window, ~5 weeks later)

Baseline Captured: _____________ | Current Measured: _____________
```

### Executive Summary

```
OVERALL RESULT:

[ ] ✅ Success — Target Met + (Exceeded expectations)
[ ] ✅ On Target — Goal Achieved (Within +/- 5%)
[ ] ⚠️ Partial Success — Moving Right Direction (50-90% of goal)
[ ] ❌ Needs Work — Below Target (Action plan required)

KEY METRICS SNAPSHOT:
```

| Metric | Baseline | Current | Change | % Change | Status |
|--------|----------|---------|--------|----------|--------|
| **Organic Sessions (GA4)** | _____ | _____ | +_____ | +____% | [ ] ✅ [ ] ⚠️ |
| **Total Impressions (GSC)** | _____ | _____ | +_____ | +____% | [ ] ✅ [ ] ⚠️ |
| **Total Clicks (GSC)** | _____ | _____ | +_____ | +____% | [ ] ✅ [ ] ⚠️ |
| **Avg Position (GSC)** | _____ | _____ | _____ spots | _____ % | [ ] ✅ [ ] ⚠️ |
| **Revenue from Organic (GA4)** | €_____ | €_____ | +€_____ | +____% | [ ] ✅ [ ] ⚠️ |

---

### Section 1: Google Search Console Metrics

#### Indexation

| Metric | Baseline | Current | Change | % Change |
|--------|----------|---------|--------|----------|
| **Total Indexed Pages** | _____ | _____ | +_____ | +____% |
| **Indexed Collections** | _____ | _____ | +_____ | +____% |
| **Indexed Products** | _____ | _____ | +_____ | +____% |

**Analysis:** ________________________________________________________________

#### Search Impressions

| Metric | Baseline | Current | Change | % Change |
|--------|----------|---------|--------|----------|
| **Total Impressions** | _____ | _____ | +_____ | +____% |
| **Top 10 Impressions** | _____ | _____ | +_____ | +____% |
| **Top 3 Impressions** | _____ | _____ | +_____ | +____% |

**Analysis:** ________________________________________________________________

#### Search Clicks

| Metric | Baseline | Current | Change | % Change |
|--------|----------|---------|--------|----------|
| **Total Clicks** | _____ | _____ | +_____ | +____% |
| **Clicks from Top 10** | _____ | _____ | +_____ | +____% |
| **Clicks from Top 3** | _____ | _____ | +_____ | +____% |

**Analysis:** ________________________________________________________________

#### Average Position

| Metric | Baseline | Current | Change | Improvement |
|--------|----------|---------|--------|-------------|
| **Overall Avg Position** | _____ | _____ | _____ spots | [ ] ⬆️ Better [ ] ⬇️ Worse |
| **Collection Avg Position** | _____ | _____ | _____ spots | [ ] ⬆️ Better [ ] ⬇️ Worse |
| **Product Avg Position** | _____ | _____ | _____ spots | [ ] ⬆️ Better [ ] ⬇️ Worse |

#### Top 10 Keywords — Biggest Risers

```
1. Keyword: _________________ | Position: _____ → _____ (+_____ spots)
2. Keyword: _________________ | Position: _____ → _____ (+_____ spots)
3. Keyword: _________________ | Position: _____ → _____ (+_____ spots)
4. Keyword: _________________ | Position: _____ → _____ (+_____ spots)
5. Keyword: _________________ | Position: _____ → _____ (+_____ spots)
```

---

### Section 2: Google Analytics 4 Metrics

#### Organic Traffic

| Metric | Baseline | Current | Change | % Change |
|--------|----------|---------|--------|----------|
| **Organic Sessions** | _____ | _____ | +_____ | +____% |
| **Organic Users** | _____ | _____ | +_____ | +____% |
| **Organic Pageviews** | _____ | _____ | +_____ | +____% |

**Analysis:** ________________________________________________________________

#### Conversions & Revenue

| Metric | Baseline | Current | Change | % Change |
|--------|----------|---------|--------|----------|
| **Total Conversions** | _____ | _____ | +_____ | +____% |
| **Conversion Rate** | ____% | ____% | +_____ % points | _____ % improvement |
| **Revenue from Organic** | €_____ | €_____ | +€_____ | +____% |

**Analysis:** ________________________________________________________________

#### Engagement

| Metric | Baseline | Current | Change |
|--------|----------|---------|--------|
| **Avg Session Duration** | _____ sec | _____ sec | +_____ sec |
| **Bounce Rate** | ____% | ____% | _____ % points |
| **Pages per Session** | _____ | _____ | +_____ |

**Analysis:** ________________________________________________________________

---

### Section 3: SE Ranking Metrics (Competitive View)

#### Keyword Rankings

| Metric | Baseline | Current | Change |
|--------|----------|---------|--------|
| **Keywords Ranking #1-3** | _____ | _____ | +_____ |
| **Keywords Ranking #4-10** | _____ | _____ | +_____ |
| **Keywords Ranking #11-30** | _____ | _____ | +_____ |

**New Keywords Ranking #1-10:** _____ keywords

**Competitive Position:** Baseline rank _____ → Current rank _____ (improved by _____ spots)

**Analysis:** ________________________________________________________________

---

### Section 4: ROI Analysis

#### Investment vs. Revenue

| Metric | Value |
|--------|-------|
| **Sprint Cost** | €_____ |
| **Revenue Generated (Organic)** | €_____ |
| **Net Profit** | €_____ |
| **ROI Multiple** | _____x |
| **ROI %** | ____% |

**Payback Period:** _____ days

**Projected 6-Month Value:** €_____ (assuming _____ conversions/month at current conversion rate)

---

### Section 5: Deliverables Completed

**What We Delivered in FASE 2 Execution:**

1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________
4. _________________________________________________________________
5. _________________________________________________________________

**What Could Improve:**

1. _________________________________________________________________
2. _________________________________________________________________

---

### Section 6: Recommendation for Continuity

**90-Day Options:**

```
[ ] Option 1: Monthly Monitoring & Optimization (€_____ /month)
    └─ Weekly metric reviews, identify new quick wins, monitor rankings

[ ] Option 2: Expanded Optimization (€_____ /month)
    └─ Monthly collection/product optimization, new keyword research, A/B testing

[ ] Option 3: Pause & Monitor (Free)
    └─ No active work. We check metrics monthly. Resume if traffic drops.
```

**Recommendation:** ________________________________________________________________

---

### Section 7: Sign-Off

```
CONFIRMAÇÃO:

Report Prepared By: _________________________ | Date: _______________

Client Reviewed By: _________________________ | Date: _______________

Client Approval: 

[ ] ✅ Accepted — Ready to proceed with continuity option
[ ] ⚠️ Requires Discussion — Schedule follow-up call
[ ] ❌ Not Approved — Feedback required

Next Steps Agreed:

_________________________________________________________________
_________________________________________________________________

Follow-up Meeting Scheduled: _________________ at _________________
```

---

## 🔗 Relacionados

- [[FASE-3-VALIDATION]] — FASE que coleta métricas para este relatório
- [[CONCEITO-Client-Approval]] — Padrões de aprovação e sign-off

---
