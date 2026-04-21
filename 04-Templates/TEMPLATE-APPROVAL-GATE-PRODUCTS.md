---
name: template-approval-gate-products
description: Approval Gate form template for product optimization samples validation
type: template
status: active
foco: operational
tags: [template, approval-gate, products, form]
wikilinks: [[FASE-2-EXECUTION]], [[CONCEITO-Client-Approval]]
---

# TEMPLATE — Approval Gate: Products Optimization

**Resumo:** Google Form para validar amostra de 5-10 produtos otimizados antes de bulk apply a 50-100+ produtos na loja.

---

## 🎯 Por Que Isto Importa

- **Sampling de produtos:** Apresentamos 5-10 produtos como exemplos (title, description, metafields). Cliente valida padrão. Depois aplicamos a todos.
- **Reduz risco:** Se cliente não aprova estrutura aqui, descobrimos antes de aplicar a 50+ produtos via API.
- **Batch operations scale:** Aprovação = lock-in → bulk API apply em 1-2h. Sem aprovação = retrabalho de 20h.

---

## ⚡ Quick Checklist

- [ ] 5-10 produtos selecionados para amostra (mix de categorias)
- [ ] Claude gerou drafts (title, description, metafields)
- [ ] Drafts carregados no form (screenshots)
- [ ] Form enviado ao cliente
- [ ] Cliente respondeu (turnaround: 48-72h típico)
- [ ] Aprovação documentada → lock-in padrão
- [ ] Pronto para bulk apply via Shopify API

---

## 📖 Conteúdo Principal

### Form Header

```
TITLE: Aprovação de Otimização de Produtos — [Store Name]

INTRO TEXT:
Olá [Client Name],

Baseado na keyword research, otimizámos titles e descriptions de vários produtos.

Abaixo estão 5-10 exemplos da amostra. Aprova a abordagem?

Se sim, aplicamos este padrão a [TOTAL] produtos.
```

### Section 1: Summary

```
SPRINT: _________________ 
FASE: 2 — Execução
DATA: ___________________

Total Produtos na Loja: _____
Amostra para Revisão: _____ (típico: 5-10)
Foco: Title + Description + SEO Metafields
```

### Section 2: Sample Products (5-10 items)

```
PRODUTO 1: [Product Name]

#### ESTADO ACTUAL:
Title: ___________________________________ 
Description (160 chars): ____________________________________________________________
Tags: ___________________________________

#### VERSÃO OPTIMIZADA:
New Title (70-80 chars): ___________________________________
New Description (120-155 chars): ____________________________________________________________
Metafields Added: ___________________________________

#### POR QUE MUDOU:
Why Title: _________________________________________________ 
Why Description: _________________________________________________ 
Expected Benefit: _________________________________________________

---

[Repeat for Products 2-10 with condensed format:
PRODUTO 2: [Name] | Current: [X] | New: [Y] | Why: [...] | Benefit: [...]
]
```

### Section 3: Batch Summary

```
RESUMO DA BATCH:

Produtos a Otimizar: _____ (full catalog scan)
Tempo para Aplicar: _____ horas (via Shopify bulk API, não manual)
Processo: 
  1. Aprovação cliente ✓
  2. Build batch CSV
  3. Submit Shopify API mutation
  4. Monitor bulk operation (5-30 min típico)

Quality Control:
☐ Manual review de 10%
☐ 100% PM review
☐ Staged rollout (50% first, monitor, then 100%)
```

### Section 4: Client Approval

```
APROVAÇÃO:

Aprova a abordagem de otimização de produtos apresentada?

☐ ✅ APROVADO — Proceder com batch optimization
☐ ⚠️ APROVADO COM AJUSTES — Detalhes abaixo
☐ ❌ REJEITADO — Feedback para revisão

[Open text field for comments]

Turnaround esperado: 48-72 horas
```

### Section 5: Sign-off

```
CONFIRMAÇÃO:

Nome do Cliente: _________________________
Data: _______________

Assinatura/Aprovação: _________________________ 

RankPanda Manager: _________________________ 
Data: _______________
```

---

## 🔗 Relacionados

- [[FASE-2-EXECUTION]] — FASE que executa a otimização
- [[CONCEITO-Client-Approval]] — Padrões de approval gate
