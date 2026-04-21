---
name: sop-vault-new-document
description: Como criar um novo documento conforme no vault
type: sop
status: ready
foco: operational
tags: [vault, documentation, agents]
wikilinks: []
---

# SOP — Criar Novo Documento no Vault

**Resumo:** Protocolo automatizado para criar documentos conformes. Garante YAML correto, nomenclatura padrão, e estrutura validada.

---

## 🎯 Por Que Isto Importa

Documentos malformados quebram o grafo de conhecimento:
- Wikilinks quebram (nomes inconsistentes)
- Validação falha (YAML incompleto)
- Agents ficam confusos (estrutura inconsistente)

Este SOP garante conformidade automática. Zero erros. Zero fricção.

---

## ⚡ Quick Checklist

- [ ] Decidir: tipo (sop, fase, template, etc) + nome + descrição
- [ ] Correr script: `create-vault-document.py`
- [ ] Preencher conteúdo (tudo menos YAML)
- [ ] Commitar

---

## 📖 How-To: Criar Novo Documento

### Passo 1: Preparar Inputs

Precisa de:
- **Type:** sop, fase, conceito, template, reference, automation, course, skill, api
- **Name:** Nome legível (ex: "Store Context Setup")
- **Description:** Uma linha, 80 chars máx (ex: "Criar contexto inicial da loja")
- **Foco:** seo, technical, operational, course

### Passo 2: Rodar Script

```bash
cd /Users/rankpanda/Shopify\ RankPanda\ APP\ -\ Oficial\ 2026/vault/
python3 create-vault-document.py \
  --type sop \
  --name "Store Context Setup" \
  --description "Criar contexto inicial da loja" \
  --foco seo
```

**Output:**
```
✅ Created: 02-SOPs/SOP-StoreContextSetup.md
📝 Edit and commit when ready
```

O ficheiro é criado com:
- ✅ YAML frontmatter correto
- ✅ Filename padrão: `[TYPE]-[CamelCaseName].md`
- ✅ Estrutura base (4 secções obrigatórias)
- ✅ Placeholders para preenchimento

### Passo 3: Editar Conteúdo

Abre o ficheiro recém-criado:

```markdown
---
name: sop-store-context-setup
description: Criar contexto inicial da loja
type: sop
status: draft
foco: seo
tags: []
wikilinks: []
---

# SOP — Store Context Setup

**Resumo:** ...

## 🎯 Por Que Isto Importa

[⬅️ PREENCHER: impacto no projeto]

## ⚡ Quick Checklist

[⬅️ PREENCHER: steps/checklist]

## 📖 Conteúdo Principal

[⬅️ PREENCHER: instruções detalhadas]

## 🔗 Relacionados

- [[related-doc-1]] — descrição
```

**O que preencher:**

| Campo | Tipo | Como |
|-------|------|------|
| **"Por Que Isto Importa"** | Obrigatório | Explica impacto direto (métrica, resultado, risco evitado) |
| **"Quick Checklist"** | Obrigatório (se SOP/FASE) | 3-5 passos práticos |
| **"Conteúdo Principal"** | Obrigatório | Instruções passo-a-passo, contexto, exemplos |
| **"Relacionados"** | Obrigatório | Mínimo 2 wikilinks: pré-requisitos (←) e outputs (→) |
| **tags** | Opcional | Adiciona 2-3 tags semânticas (ex: `[keyword-research, approval, validation]`) |

### Passo 4: Validar e Commitar

Antes de commitar, confirma:

```bash
# Testa wikilinks (se added)
python3 ../interlinking-validator.py

# Testa filename compliance
python3 ../filename-validator.py

# Git commit
git add 02-SOPs/SOP-StoreContextSetup.md
git commit -m "docs: Adicionar SOP — Store Context Setup"
```

---

## 📋 Tipos de Documentos

### SOP (Standard Operating Procedure)
- **Quando:** Passo-a-passo operacional
- **Exemplo:** "How to run GSC analysis"
- **Local:** `/02-SOPs/`
- **Estrutura:** Por Que → Checklist → Conteúdo → Relacionados

### FASE (Project Phase)
- **Quando:** Fase de projeto (FASE-0, FASE-1, etc)
- **Exemplo:** "FASE-1: Diagnóstico"
- **Local:** `/02-SOPs/`
- **Estrutura:** Objetivo → Deliverables → Timeline → Dependencies

### CONCEITO (Concept Hub)
- **Quando:** Tema agregador (palavra-chave, metodologia, padrão)
- **Exemplo:** "CONCEITO-Keyword-Research"
- **Local:** `/02-SOPs/`
- **Estrutura:** O Que É → Quando Usar → SOPs Relacionadas → Fluxo

### TEMPLATE
- **Quando:** Template reutilizável (form, checklist, report)
- **Exemplo:** "TEMPLATE-Weekly-Update"
- **Local:** `/04-Templates/`
- **Estrutura:** Propósito → Exemplos → How-To Use

### AUTOMATION
- **Quando:** Script, webhook, scheduled task
- **Exemplo:** "AUTOMATION-Vault-Sync"
- **Local:** `/03-Automações/`
- **Estrutura:** O Que Faz → Triggers → Config → How to Test

### REFERENCE
- **Quando:** Documentação de referência (índice, lookup, anexo)
- **Exemplo:** "REFERENCE-Memory-Index"
- **Local:** `/00-Memory/`
- **Estrutura:** Contents → How to Use → Updates

---

## ⚠️ Erros Comuns (Evita!)

| Erro | Porquê Não | Solução |
|------|-----------|---------|
| Ficheiro sem YAML | Validator falha, wikilinks quebram | Usa script, não copia manualmente |
| Nome em lowercase | `sop-my-document.md` quebra wikilinks | Script converte automaticamente para CamelCase |
| Sem "Por Que Isto Importa" | Documento fica descontextualizado | Sempre preenche — é obrigatório |
| Wikilinks quebradas | `[[sop-1]]` em vez de `[[SOP-1-STORE-CONTEXT-SETUP-V2]]` | Copia exactamente do filename (case-sensitive) |
| Tags em português | `[pesquisa de keywords]` é ilegível | Usa tags lowercase, sem espaços, tipo `[keyword-research]` |

---

## 🔗 Relacionados

- [[SOP-1-STORE-CONTEXT-SETUP-V2]] — Primeiro passo em qualquer projeto
- [[REFERENCE-VAULT-PADROES]] — Padrões obrigatórios (quando existir)
- [[AUTOMATION-VAULT-SYNC-SETUP]] — Como sincronizar vault para GitHub
