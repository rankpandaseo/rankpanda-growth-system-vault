---
name: template-approval-gate-collections
description: Approval Gate form template for collection optimization samples validation
type: template
status: active
foco: operational
tags: [template, approval-gate, collections, form]
wikilinks: [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-2-EXECUTION]], [[CONCEITO-Client-Approval]]
---

# TEMPLATE — Approval Gate: Collections Optimization

**Resumo:** Google Form para validar amostra de 2-3 collections otimizadas antes de bulk apply de todas as collections na loja.

---

## 🎯 Por Que Isto Importa

- **Sampling de collections:** Apresentamos 2-3 collections como exemplos. Cliente valida título, descrição, schema. Depois aplicamos padrão a todas.
- **Evita retrabalho massivo:** Se cliente não aprova estrutura aqui, descobrimos antes de aplicar a 50+ collections.
- **Validação de tone:** Cliente vê exemplos reais (title, meta desc, schema) e aprova tom, comprimento, abordagem.

---

## ⚡ Quick Checklist

- [ ] 2-3 collections selecionadas para amostra (representativas)
- [ ] Claude gerou drafts (title, meta desc, schema)
- [ ] Drafts carregados no form (screenshots ou preview)
- [ ] Form enviado ao cliente
- [ ] Cliente respondeu (turnaround: 48-72h típico)
- [ ] Aprovação documentada → lock-in padrão
- [ ] Pronto para bulk apply via Shopify API

---

## 📖 Conteúdo Principal

### Form Header

```
TITLE: Aprovação de Otimização de Collections — [Store Name]

INTRO TEXT:
Olá [Client Name],

Baseado na keyword research e estratégia de clustering, otimizámos as titles, 
descriptions e schema de várias collections.

Abaixo estão 2-3 exemplos do que propomos. Aprova a abordagem?

Se sim, aplicamos este padrão a todas as [TOTAL] collections.
```

### Section 1: Summary

```
SPRINT: _________________ 
FASE: 2 — Execução
DATA: ___________________

Total Collections na Loja: _____
Amostra para Revisão: _____ (típico: 2-3)
Foco de Otimização: Title + Description + Schema + Navigation
```

### Section 2: Sample Collection 1

```
COLLECTION 1: [Collection Name]

#### ESTADO ACTUAL:
Title: ___________________________________ 
Meta Description (160 chars): ____________________________________________________________
Meta Tags: ___________________________________

#### VERSÃO OPTIMIZADA:
New Title (50-60 chars): ___________________________________
New Description (120-155 chars): ____________________________________________________________
Schema Added: [ ] ProductCollection [ ] BreadcrumbList

#### POR QUE MUDOU:
Reasoning for Title: _________________________________________________ 
Reasoning for Description: _________________________________________________ 
Expected Impact: _________________________________________________

---

[Repeat Section 2 for Collections 2, 3 if applicable]
```

### Section 3: Optimization Approach

```
ABORDAGEM DE OTIMIZAÇÃO:

Total Collections a Otimizar: _____ (across store)
Tempo para Aplicar: _____ horas (via Shopify bulk API)
Timeline: Week _____ to Week _____

Teste A/B?
☐ Sim, testar antes de rollout completo
☐ Não, aplicar a todas directamente
```

### Section 4: Client Approval

```
APROVAÇÃO:

Aprova a abordagem de otimização de collections apresentada?

☐ ✅ APROVADO — Proceder com implementação em massa
☐ ⚠️ APROVADO COM AJUSTES — Detalhes abaixo
☐ ❌ REJEITADO — Feedback para revisão

[Open text field for comments]

Turnaround esperado: 48 horas
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

- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Clustering que mapeia keywords → collections
- [[FASE-2-EXECUTION]] — FASE que executa a otimização
- [[CONCEITO-Shopify-Collections]] — Detalhes técnicos de metafields + schema
