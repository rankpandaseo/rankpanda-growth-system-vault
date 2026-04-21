---
name: reference-lessons
description: Lessons — Erros que não podem repetir (organizational learning to prevent regression)
type: reference
status: active
foco: operational
tags: [reference, index, lessons, learnings]
wikilinks: [[REFERENCE-MEMORY-INDEX]]
---

# Lessons — Erros Que Não Podem Repetir

**Resumo:** Aprendizados organizacionais que devem prevenir regressão. Cada lição documenta ERRO, IMPACTO, COMO EVITAR. Crescem a cada sprint.

---

## 🎯 Por Que Isto Importa

- **Regression prevention:** Erro cometido uma vez nunca mais
- **Institutional knowledge:** Squad nova não repete erros do sprint anterior
- **Efficiency:** Tempo não gasto em "vimos isto antes"
- **Pattern recognition:** Semelhança com erros passados = early warning

---

## ⚡ Quick Checklist

- [ ] Ler todas as lições antes de novo trabalho
- [ ] Se reconheces padrão de erro passado, stop e documentar
- [ ] Após erro novo, adicionar a esta lista imediatamente
- [ ] Item 2
- [ ] Item 3

---

## 📖 Conteúdo Principal

### Lições Críticas — Erros que Não Podem Repetir

**1. Vault Standardization is Non-Negotiable**
- Erro: Ficheiros sem padrão → agentes não conseguem ler
- Aprendizado: Estrutura (Properties + 4 sections) é blocking para automação
- Como aplicar: Sempre validar YAML frontmatter antes de commitar

**2. Content Over Appearance**
- Erro: Focar em design/UI antes de ter dados estruturados
- Aprendizado: Dados estruturados (Properties) > Dashboard visual
- Como aplicar: Vault + API-first antes de qualquer interface

**3. API-First, Zero MCPs**
- Erro: Tentar integrar tudo via MCPs (28% overhead)
- Aprendizado: APIs on-demand, documentadas, zero ambiguidade
- Como aplicar: Cada FASE tem checklist API claro

**4. Placeholder Content is a Blocker**
- Erro: Deixar ficheiros com `[content]`
- Aprendizado: Agents não conseguem processar placeholders
- Como aplicar: Audit completo antes de passado a agents

**5. Wikilink Resolution Must Work**
- Erro: Broken wikilinks → grafo de conhecimento quebra
- Aprendizado: Resolver `[[SOP-1]]` dinamicamente é essencial
- Como aplicar: Usar WikilinkResolver em tudo que lê vault

---

## 🔗 Relacionados

- [[REFERENCE-MEMORY-INDEX]] — Índice central do sistema
- [[REFERENCE-DECISIONS]] — Decisões que governam
- [[REFERENCE-ESTADO-ATUAL]] — Estado e progresso
- [[COURSE-PEPITAS-DE-OURO]] — Lições que alimentam o course

---
