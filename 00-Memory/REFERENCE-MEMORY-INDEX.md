---
name: reference-memory-index
description: Memory Index — RankPanda Growth System. Persistent context that enables Claude to maintain project awareness and become increasingly proactive.
type: reference
status: active
foco: operational
tags: [reference, index, memory, context]
wikilinks: []
---

# Memory Index — RankPanda Growth System

**Resumo:** Persistent context that enables Claude to maintain project awareness, learn from past decisions, and become increasingly proactive across sprints.

---

## 🎯 Por Que Isto Importa

- **Continuity:** Each session starts with full context, not from zero
- **Proactivity:** Claude anticipates problems and proposes solutions
- **Learning:** Organizational learnings persist across projects
- **Scaling:** New sprints reference what worked before
- **Efficiency:** No context switching = faster execution

---

## ⚡ Quick Checklist

- [ ] Ler `00-Memory/MEMORY.md` (índice principal)
- [ ] Ler `memory/context/*.md` (decisions, lessons, people)
- [ ] Ler `memory/projects/[cliente].md` (cliente específico, se aplicável)
- [ ] Ler `memory/sessions/estado-atual.md` (onde ficámos)

---

## 📖 Conteúdo Principal

### Estrutura da Memória

```
00-Memory/
├── MEMORY.md                    ← Índice (entry point — START HERE)
├── context/
│   ├── decisions.md             ← Decisões invioláveis
│   ├── lessons.md               ← Erros que não podem repetir
│   ├── people.md                ← Squad, dinâmicas, alertas
│   └── pending.md               ← O que espera feedback
├── projects/
│   ├── [cliente-1].md           ← Estado do cliente (task IDs, métricas)
│   ├── [cliente-2].md
│   └── ...
├── sessions/
│   ├── estado-atual.md          ← Snapshot: onde ficámos agora
│   ├── 2026-04-21.md            ← Log da sessão (data)
│   └── ...
└── integrations/
    ├── reference_external_systems.md
    └── ...
```

### Como Usar

1. **Start:** Ler `MEMORY.md` (este é o índice)
2. **Context:** Ler ficheiros em `context/` (decisions, lessons, people)
3. **Project:** Se trabalhando com cliente específico, ler `projects/[cliente].md`
4. **Session:** Ler `estado-atual.md` para saber exatamente onde ficámos
5. **Before closing:** Atualizar `estado-atual.md` + commit

### Princípios

- **Single source of truth:** Cada facto vive num ÚNICO ficheiro
- **Atomic updates:** Quando algo muda, update imediatamente (não adia)
- **Durability:** Tudo commitado para GitHub (backup durável)
- **Clarity:** Memória deve ser legível por future-you após 3 meses

---

## 🔗 Relacionados

- [[CLAUDE.md]] — Instruções de projeto (INVIOLÁVEL)
- [[SOP-VAULT-FORMAT-SPECIFICATION]] — Padrão de documentação
- [[MEMORY.md]] — O índice principal (aponta para tudo)
