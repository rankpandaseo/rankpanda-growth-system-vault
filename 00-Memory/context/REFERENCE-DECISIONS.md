---
name: reference-decisions
description: Decisões Arquitecturais — Rules that cannot be violated (Zero Duplicação, API-First, etc)
type: reference
status: active
foco: operational
tags: [reference, index, decisions, architecture]
wikilinks: [[REFERENCE-MEMORY-INDEX]]
---

# Decisões Arquitecturais — RankPanda Shopify SEO System

**Resumo:** Decisões permanentes que não podem ser violadas. Zero Duplicação, API-First (zero MCPs), Memory System, Vault Markdown Standard. Cada decisão tem regra, contexto, e impacto.

---

## 🎯 Por Que Isto Importa

- **Consistency:** Decisões documentadas = zero contradição entre sessões
- **Governance:** Novas iniciativas validadas contra decisões existentes
- **Scaling:** Padrões provados replicados em novos clientes/projetos
- **Transparency:** Rui sabe que Claude respeitou as regras

---

## ⚡ Quick Checklist

- [ ] Ler todas as decisões antes de iniciar trabalho
- [ ] Se uma decisão é violada, stop e documentar
- [ ] Propostas de MUDANÇA de decisão = discussion, não implementação

---

## 📖 Conteúdo Principal

|-------|-------|
| **Título** | Decisões Arquitecturais (INVIOLÁVEL) |
| **Data Criação** | 2026-04-18 | --- ## 1. APIs Diretas, Nunca MCP (2026-04-18) **Decisão:** Todas as integrações via API diretas (Shopify, GSC, GA4, SE Ranking, ClickUp, Gmail, Calendar, Drive, Leexi). NUNCA via MCP. **Razão:** - APIs dão acesso direto às credenciais do Rui (já estão no GitHub rankpandaseo/rankpanda-vault)
1. Cria `memory/projects/[cliente].md`
2. Lê `kickoff-briefing-form.md` preenchido pelo cliente
3. Extrai dados (AOV, volume, IDs de ferramentas, etc.)
4. Popula `memory/context/people.md` (contacts, dinâmicas)
5. Cria `memory/pending.md` (o que cliente prometeu)
6. Cria primeira entrada em `memory/sessions/estado-atual.md` **Razão:**

---

## 🔗 Relacionados

- [[REFERENCE-MEMORY-INDEX]] — Índice central do sistema de memória
- [[REFERENCE-LESSONS]] — Erros que não podem repetir
- [[REFERENCE-PEOPLE]] — Squad e dinâmicas
- [[REFERENCE-ESTADO-ATUAL]] — Estado atual da operação

---
