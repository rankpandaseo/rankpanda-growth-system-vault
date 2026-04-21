---
name: template-approval-gate-keywords
description: Approval Gate form template for keyword research validation before FASE-2 execution
type: template
status: active
foco: operational
tags: [template, approval-gate, keyword-research, form]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[FASE-2-EXECUTION]], [[CONCEITO-Client-Approval]]
---

# TEMPLATE — Approval Gate: Keywords Research

**Resumo:** Google Form template para apresentar keyword research ao cliente e obter aprovação antes de prosseguir para collection + product optimization (FASE-2).

---

## 🎯 Por Que Isto Importa

- **Sampling pattern:** Cliente aprova amostra de 10-20 keywords do total. Valida estratégia, não cada detalhe. Acelera 10x.
- **Sign-off obrigatório:** Antes de gastar 3 semanas em otimizações, cliente confirma "sim, faz sentido". Evita retrabalho.
- **Baseado em dados:** Cada keyword tem volume, difficulty, position atual. Cliente vê números, não "acho que".

---

## ⚡ Quick Checklist

- [ ] Form enviado ao cliente (Google Form ou Typeform)
- [ ] 10-20 keywords selecionadas para amostra (representativas do total)
- [ ] Dados validados (volume, difficulty, position actual from GSC)
- [ ] Cliente respondeu (turnaround: 48h típico)
- [ ] Aprovação ou pedido de ajuste documentado
- [ ] Aprovação recebida → locked-in, prosseguir para SOP-3 clustering

---

## 📖 Conteúdo Principal

### Form Header

```
TITLE: Aprovação de Keywords — [Store Name]

INTRO TEXT:
Olá [Client Name],

Baseado na análise de GSC, SE Ranking e investigação competitiva, identificámos 
[TOTAL] keywords de oportunidade para [Collection Name]. 

Abaixo está uma amostra de 15 keywords que recomendamos otimizar nos próximos 3 semanas.
Aprova a abordagem e a seleção?

[Análise completa: https://rankpanda.local/kw-research-[client]-[date].md]
```

### Section 1: Summary

```
SPRINT: _________________ 
FASE: 2 — Execução
DATA: ___________________

Total Keywords Identificadas: _____
Keywords Aprovadas para Otimização: _____
Data Source: SE Ranking + GSC Analysis
Período de Análise: _____ dias
```

### Section 2: Keywords by Collection

```
COLLECTION 1: [Collection Name]
_________________________________

| Keyword | Volume/mês | Difficulty | Pos Atual | Intent | Ação |
|---------|-----------|-----------|----------|--------|------|
| [KW1] | [Vol] | [Diff] | [Pos] | [Intent] | Optimize title + meta |
| [KW2] | [Vol] | [Diff] | [Pos] | [Intent] | New collection |
| [KW3] | [Vol] | [Diff] | [Pos] | [Intent] | Product clustering |

STRATEGY: 
[Brief explanation of approach for this collection]

---

[Repeat Section 2 for Collection 2, 3, etc.]
```

### Section 3: Top Quick Wins

```
3 KEYWORDS COM MELHOR POTENCIAL (30-45 dias):

1. [Keyword] — Volume: [X] searches/mês | Posição Atual: [Y] | Oportunidade: [Brief]
2. [Keyword] — Volume: [X] searches/mês | Posição Atual: [Y] | Oportunidade: [Brief]
3. [Keyword] — Volume: [X] searches/mês | Posição Atual: [Y] | Oportunidade: [Brief]
```

### Section 4: Impact Projection

```
IMPACT ESTIMADO (45 days após otimização):

• Estimated New Sessions: +[X] (based on CTR + volume)
• Estimated Revenue Impact: €[Y] (sessions × CR × AOV)
• Expected Ranking Improvement: [X] keywords moving to top 10
• Collections Affected: [List]
```

### Section 5: Client Approval (Obrigatório)

```
APROVAÇÃO:

Aprova a estratégia de keyword research e o plano de otimização de collections?

☐ ✅ APROVADO — Prosseguir com execução
☐ ⚠️ APROVADO COM AJUSTES — Detalhes abaixo
☐ ❌ REJEITADO — Feedback para revisão

[Open text field for feedback/comments]

Turnaround esperado: 48 horas
```

### Section 6: Sign-off

```
CONFIRMAÇÃO:

Nome do Cliente: _________________________
Data: _______________

Assinatura/Aprovação: _________________________ 

RankPanda Manager: _________________________ 
Data: _______________
```

### Section 7: Notes

```
📌 NOTAS:
- Keywords podem ser refinadas durante FASE-2 se novas oportunidades surgirem
- Após aprovação, prosseguimos para clustering (SOP-3) nos próximos 2-3 dias
- Timeline total FASE-2: 3 semanas (keywords + collections + products)
```

---

## 🔗 Relacionados

- [[SOP-2-KEYWORD-RESEARCH-V2]] — Pipeline que gera as keywords deste form
- [[FASE-2-EXECUTION]] — FASE que executa as keywords aprovadas
- [[CONCEITO-Client-Approval]] — Padrões de approval e escalation path
