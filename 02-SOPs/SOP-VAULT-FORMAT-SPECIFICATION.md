---
name: sop-vault-format-specification
description: Especificação de formato para documentos no vault (Obsidian Properties)
type: sop
status: ready
foco: operational
tags: [vault, agents, documentation, format]
wikilinks: [[SOP-VAULT-NEW-DOCUMENT]]
---

# SOP — Vault Format Specification (Obsidian Properties)

**Resumo:** Padrão obrigatório de formatação para todos os documentos no vault. Define Properties nativas do Obsidian + estrutura markdown esperada. Garante leitura consistente por agents.

---

## 🎯 Por Que Isto Importa

Agents leem documentos no vault para:
- Extrair contexto (Properties: name, type, foco)
- Entender fluxo (wikilinks: ← inputs, → outputs)
- Executar ações (estrutura markdown previsível)

Formato inconsistente = agents confusos = erros em cascata.

---

## ⚡ Quick Checklist

- [ ] Todo documento tem Properties completo (obrigatório)
- [ ] Properties estão no topo: `---\nname: ...\n---`
- [ ] Structure markdown em 4 secções: Por Que + Checklist + Conteúdo + Relacionados
- [ ] Wikilinks são case-sensitive (CamelCase)
- [ ] Nenhuma linha solta fora das secções

---

## 📖 FORMATO OBRIGATÓRIO

### Seção 1: Obsidian Properties (OBRIGATÓRIO)

```yaml
---
name: kebab-case-id
description: Uma linha, máx 80 chars
type: sop
status: draft
foco: seo
tags: [tag1, tag2]
wikilinks: [[Related-Doc-1]], [[Related-Doc-2]]
---
```

**Regras:**

| Property | Valores | Obrigatório? | Notas |
|----------|---------|--------------|-------|
| `name` | kebab-case | ✅ Sim | Identifica único do ficheiro, sem extensão |
| `description` | String, max 80 chars | ✅ Sim | Uma linha clara. Aparece em índices |
| `type` | sop, fase, conceito, template, reference, automation, course, skill, api | ✅ Sim | Define localização + estrutura esperada |
| `status` | draft, ready, active | ✅ Sim | draft = em progresso, ready = pronto para usar, active = em uso |
| `foco` | seo, technical, operational, course | ✅ Sim | Eixo principal do documento |
| `tags` | [tag1, tag2, tag3] | ⚠️ Recomendado | Categorias semânticas, lowercase, sem espaços |
| `wikilinks` | [[Doc-1]], [[Doc-2]] | ⚠️ Recomendado | Referências a documentos relacionados |

**Exemplos válidos:**

```yaml
---
name: sop-store-context-setup
description: Criar contexto inicial da loja
type: sop
status: active
foco: operational
tags: [onboarding, baseline, phase-0]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[FASE-0-KICKOFF]]
---
```

```yaml
---
name: conceito-keyword-research
description: Agregador temático: metodologia + fluxo de keyword research
type: conceito
status: ready
foco: seo
tags: [research, strategy]
wikilinks: [[SOP-2-KEYWORD-RESEARCH-V2]], [[SOP-3-CLUSTERING-COLLECTION-MAPPING]], [[FASE-1-DIAGNOSTIC]]
---
```

### Seção 2: Markdown Structure (OBRIGATÓRIO)

Após Properties `---`, documento segue esta estrutura **rígida:**

```markdown
# [TÍTULO PRINCIPAL]

**Resumo:** 1-2 frases do que isto é

---

## 🎯 Por Que Isto Importa

[MANDATORY: 3-5 bullets explicando impacto]
- Ponto 1
- Ponto 2
- Ponto 3

---

## ⚡ Quick Checklist

[MANDATORY for SOP/FASE: 3-5 actionable items]
- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

[Optional for CONCEITO/TEMPLATE/REFERENCE: pode ser resumido a bullets]

---

## 📖 Conteúdo Principal

[MANDATORY: corpo principal com instruções/explicação]

[Use H3 headers para subsecções se necessário]

---

## 🔗 Relacionados

- [[Document-1]] — descrição breve
- [[Document-2]] — descrição breve
- [[Document-3]] — descrição breve
```

**Regras:**

1. **4 secções principais obrigatórias** (mesmos headers sempre):
   - `## 🎯 Por Que Isto Importa`
   - `## ⚡ Quick Checklist` (ou resumido se não-SOP/FASE)
   - `## 📖 Conteúdo Principal`
   - `## 🔗 Relacionados`

2. **Headings são H2 (`##`), subsecções são H3 (`###`)**

3. **Sem conteúdo fora das 4 secções** — cada coisa tem um lar

4. **Wikilinks são case-sensitive:**
   - ❌ Errado: `[[sop-1-store-context-setup]]`
   - ✅ Correto: `[[SOP-1-STORE-CONTEXT-SETUP-V2]]`

5. **Emojis obrigatórios** nos headers principais (facilita parsing visual)

---

## 🤖 Como Agents Leem Isto

### Passo 1: Extract Properties

Agent faz `grep "^name:" documento.md` → extrai identificador único.

Agent faz `grep "^type:" documento.md` → entende que é um SOP, FASE, etc.

Agent faz `grep "^foco:" documento.md` → sabe se é SEO-focused ou technical.

### Passo 2: Extract Structure

Agent procura seções pelos headers `## 🎯`, `## ⚡`, etc.

Agent sabe que conteúdo entre secções é o que importa.

Agent ignora formatação — parse por headers.

### Passo 3: Extract Wikilinks

Agent encontra `[[...]]` em qualquer secção → extrai referências.

Agent sabe que "Relacionados" tem os links mais importantes.

Agent resolve wikilinks para encontrar ficheiros relacionados.

---

## ❌ Erros Fatais (Agents Falham)

| Erro | Porquê Falha | Como Evitar |
|------|-------------|------------|
| Properties incompleto | Agent não consegue classificar documento | Usa script `create-vault-document.py` |
| Wikilinks em lowercase | Links não resolvem (case-sensitive) | Copia exactamente do filename (CamelCase) |
| Seção faltando | Agent procura `## 🎯` e não encontra | Sempre usa as 4 secções |
| Header em H1 (`#`) na secção | Parser quebra (espera H2) | Headers principales = H2 (`##`) sempre |
| Conteúdo fora das secções | Agent não consegue parse | Coloca tudo dentro de uma das 4 secções |

---

## 🔄 Evolução Futura (TODO)

Estas funcionalidades estão documentadas para desenvolvimento posterior:

### TODO 1: Agent Reading Parser

**O quê:** Criar classe Python `VaultDocumentParser` que agents usam para ler documentos.

**Por quê:** Standardiza forma como agents extraem Properties, seções, wikilinks.

**Como:**
```python
from vault_parser import VaultDocumentParser

doc = VaultDocumentParser('02-SOPs/SOP-1-STORE-CONTEXT-SETUP-v2.md')

# Extract properties
doc.properties()  # → {'name': 'sop-...', 'type': 'sop', ...}

# Extract sections
doc.section('Por Que Isto Importa')  # → text content
doc.section('Conteúdo Principal')    # → text content

# Extract wikilinks
doc.wikilinks()  # → [['SOP-2-...'], ['FASE-0-...']]
```

**Status:** Pending development post-standardization.

### TODO 2: Obsidian Plugin Integration

**O quê:** Criar plugin Obsidian que valida Documents em real-time.

**Por quê:** Quando Rui ou agents abrem documento, validator mostra warnings se Properties incompleto ou estrutura errada.

**Como:** Plugin hooka em `file-open` evento. Valida Properties. Mostra notificação. ✅ Ready / ⚠️ Incomplete / ❌ Invalid.

**Status:** Pending plugin development.

### TODO 3: Agent Document Generation Template

**O quê:** Expandir `create-vault-document.py` para agnostic template generation.

**Por quê:** Agents conseguem gerar novos documentos dinamicamente durante execução.

**Funcionalidades futuras:**
- Generate com template customizado por type
- Auto-populate com sugestões iniciais
- Validação ao criar (não espera commit manual)

**Status:** Pending after MVP validation.

### TODO 4: Wikilink Resolution Graph

**O quê:** Sistema que resolve wikilinks dinamicamente para agents.

**Por quê:** Agent lê `[[SOP-2-KEYWORD-RESEARCH-V2]]` → sistema resolve para path real → agent carrega arquivo.

**Implementação:** Hash map de (name → filepath), atualizado com cada file add/rename.

**Status:** Pending graph system design.

### TODO 5: Property Validation Rules

**O quê:** Expandir validator para check custom rules per document type.

**Por quê:** Agents conseguem validar que FASE tem "Duração", SOP tem "Checklist", etc.

**Exemplo:**
```
FASE must have:
  - Objetivo
  - Duração
  - Deliverables
  - Timeline

SOP must have:
  - Checklist
  - Pré-requisitos
```

**Status:** Pending rule engine design.

---

## 🔗 Relacionados

- [[SOP-VAULT-NEW-DOCUMENT]] — Como criar novo documento (passo-a-passo)
- [[AUTOMATION-VAULT-SYNC-SETUP]] — Como sincronizar vault para GitHub
- [[SOP-1-STORE-CONTEXT-SETUP-V2]] — Exemplo de SOP bem-formatado
