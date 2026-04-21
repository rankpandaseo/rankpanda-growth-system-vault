---
name: 00-readme
description: RankPanda Growth System — Vault central único (projetos, SOPs, automações, templates, cursos)
type: reference
status: active
foco: operational
tags: [vault, index, operations, structure]
wikilinks: [[REFERENCE-MEMORY-INDEX]], [[SOP-VAULT-FORMAT-SPECIFICATION]], [[IMPLEMENTATION-ROADMAP]]
---

# RankPanda Growth System — Obsidian Vault

**Resumo:** Vault central único para operação RankPanda: projetos de clientes, SOPs, automações, templates reutilizáveis, e curso 45D. Single source of truth para toda a organização.

---

## 🎯 Por Que Isto Importa

- **Single Source of Truth:** Vault é única fonte autorizada para processos RankPanda (não duplicação, não dispersão)
- **Agent-Readable:** Estrutura padronizada permite agentes ler/criar/atualizar documentos sem intervenção manual
- **Escalabilidade:** Conforme novos clientes/projetos surgem, padrão permite crescimento organizado e replicável

---

## ⚡ Quick Checklist

- [ ] Ler documentação vault (00-README, SOP-VAULT-FORMAT-SPECIFICATION)
- [ ] Compreender hierarquia de diretorias (01-Clientes, 02-SOPs, 03-Automações, 04-Templates, 05-Curso)
- [ ] Validar que novo documento segue padrão (YAML, 4 secções, wikilinks)
- [ ] Registar novo documento em MEMORY.md index

---

## 📖 Conteúdo Principal

### Estrutura do Vault

```
/vault/
├── 00-Memory/          ← Context persistence entre sessões
├── 01-Clientes/        ← Pasta por cliente com FASEs do sprint
├── 02-SOPs/            ← Protocolos operacionais (FASE 0-3)
├── 03-Automações/      ← Scripts, scheduled tasks, webhooks
├── 04-Templates/       ← Templates reutilizáveis
└── 05-Curso-45D/       ← Material de curso + pepitas de ouro
```

### 5 Pilares de Operação

1. **Structure Standardization** → YAML + 4 mandatory sections
2. **Vault Sync** → Git sincroniza automático (local → GitHub)
3. **Memory System** → Claude context persistence entre sessões
4. **API-First Integration** → Todas integrações via APIs diretas
5. **Zero Duplicação** → Cada conteúdo existe UM único lugar

---

## 🔗 Relacionados

- [[SOP-VAULT-FORMAT-SPECIFICATION]] — Padrão Markdown obrigatório para todos documentos
- [[IMPLEMENTATION-ROADMAP]] — Roadmap de implementação 3 phases
- [[REFERENCE-MEMORY-INDEX]] — Índice de sistema de memória persistente
- [[REFERENCE-DECISIONS]] — Decisões arquiteturais invioláveis
- [[COURSE-00-STRUCTURE]] — Estrutura do curso RankPanda 45D

---
