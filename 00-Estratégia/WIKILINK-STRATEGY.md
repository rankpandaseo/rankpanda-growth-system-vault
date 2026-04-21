---
name: wikilink-strategy
description: Semantic interlinking strategy for vault obsidian graph enrichment
type: reference
status: draft
foco: documentação
tags: [interlinking, semantic-graph, obsidian-cli, bidirectional]
---

# Estratégia de Interlinking Semântico — Vault RankPanda

**Objetivo:** Transformar vault numa rede semântica robusta (não sequencial linear).

---

## 🎯 Por Que Isto Importa

**Sem interlinking semântico:**
- SOPs são silos (SOP-1 não conhece conceitos em SOP-4)
- Contexto fragmentado (um team member lê SOP-2 sem saber que FASE-0 fornece baseline)
- Obsidian graph é um fio reto (linear), não uma rede
- Reutilização de conceitos é manual, não automática

**Com interlinking semântico:**
- Conceito "Shopify Collection" aparece uma vez, referenciado em SOP-1, SOP-3, FASE-2
- Team member lê SOP-2, vê "Collection" linkado → compreende contexto completo
- Obsidian graph é uma rede densa = melhor navegação, melhor contexto, melhor compreensão

---

## Princípios de Interlinking

### 1. Bidirecionalidade (A ↔ B)
Se SOP-2 cita SOP-3, então SOP-3 deve citar SOP-2 ("input de SOP-2", "output para SOP-3").

```markdown
# SOP-2
- **Próximo:** [[SOP-3]] — Transforma keywords em clusters
- **Dependências:** [[SOP-1]] — Requer store context

# SOP-3
- **Anterior:** [[SOP-2]] — Input: keywords.json
- **Próximo:** [[SOP-4]] — Output: clusters aplicados em on-page
```

### 2. Granularidade Semântica (Conceitos > Documentos)
Não é apenas "SOP-2 → SOP-3". É:
- **Conceitual:** "Keyword Research" é um conceito que toca SOP-2, SOP-3, FASE-1, FASE-2, Templates
- **Transversal:** "Shopify Collection" aparece em SOP-1 (context), SOP-3 (mapeamento), FASE-2 (execução), Templates (aprovação)

```markdown
## 🔗 Conceitos Relacionados

**Keyword Research (conceito)**
- [[SOP-2-KEYWORD-RESEARCH-V2]] — Pipeline: Semrush → DataForSEO → Claude
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Agrupa keywords em clusters
- [[FASE-1-DIAGNOSTIC]] — Identifica gaps de keywords
- [[FASE-2-EXECUTION]] — Executa KW research com client approvals

**Shopify Collection (conceito)**
- [[SOP-1-STORE-CONTEXT-SETUP]] — Recolhe estrutura de collections
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Mapeia keywords → collections
- [[FASE-2-EXECUTION]] — Otimiza e publica collections
- [[Template-Collection-Review]] — Approval form para collections
```

### 3. Tipo de Link (Semântica Explícita)
Cada link deve ter tipo:
- **→ Input:** Este documento depende de X
- **→ Output:** Este documento alimenta X
- **↔ Relacionado:** Conceito transversal
- **→ Exemplo:** Implementação concreta de X
- **→ Validação:** Como verificar se X foi bem feito

```markdown
**Relacionados:**
- [[SOP-1]] ← **Input:** Store context recolhido
- [[SOP-2]] → **Output:** Keywords para cluster em SOP-3
- [[FASE-0-KICKOFF]] ↔ **Contexto:** Setup paralelo
- [[PILOT-VIBRADORES-00-MASTER-PLAN]] → **Exemplo:** Implementação real
- [[Template-KW-Approval]] → **Validação:** Como aprovar KWs
```

---

## Mapa de Interlinking por Conceito

### CONCEITO: Keyword Research & SEO Discovery
| Documento | Input | Output | Validação |
|-----------|-------|--------|-----------|
| [[SOP-2-KEYWORD-RESEARCH-V2]] | [[SOP-1]] | [[SOP-3]] | [[FASE-1-DIAGNOSTIC]] |
| [[FASE-1-DIAGNOSTIC]] | [[FASE-0-KICKOFF]] | [[FASE-2-EXECUTION]] | [[SOP-2]] |
| [[Template-KW-Research]] | [[SOP-1]] | [[SOP-2]] | [[Template-KW-Approval]] |

### CONCEITO: Collection Structure & Organization
| Documento | Input | Output | Validação |
|-----------|-------|--------|-----------|
| [[SOP-1-STORE-CONTEXT-SETUP]] | [[FASE-0-KICKOFF]] | [[SOP-3]] | [[PILOT-VIBRADORES-00-MASTER-PLAN]] |
| [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] | [[SOP-2]] | [[FASE-2-EXECUTION]] | [[Template-Collection-Review]] |
| [[FASE-2-EXECUTION]] | [[FASE-1-DIAGNOSTIC]] | [[FASE-3-VALIDATION]] | [[GSC-Monitoring]] |

### CONCEITO: Client Communication & Approval Gates
| Documento | Touchpoint | Tipo | Relacionado |
|-----------|-----------|------|-----------|
| [[FASE-0-KICKOFF]] | Client intro call | Setup | [[Discord-Setup]] |
| [[Template-Weekly-Update]] | Friday report | Ongoing | [[FASE-2-EXECUTION]] |
| [[Template-Collection-Review]] | Approval gate | Sync | [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] |
| [[FASE-3-VALIDATION]] | Final presentation | Closure | [[Template-Pepita-Capture]] |

### CONCEITO: Technical Implementation (Shopify + APIs)
| Documento | System | Input | Output |
|-----------|--------|-------|--------|
| [[SOP-1-STORE-CONTEXT-SETUP]] | Shopify API | [[FASE-0-KICKOFF]] | [[SOP-2]] |
| [[API-REGISTRY]] | DataForSEO, Crawl4AI, SE Ranking | [[SOP-2]] | [[FASE-1-DIAGNOSTIC]] |
| [[FASE-2-EXECUTION]] | Bulk operations, metafields | [[SOP-3]] | [[FASE-3-VALIDATION]] |

---

## Audit: Gaps de Interlinking PHASE 1

### ✅ Já Feito (SOP 1-3 + FASE 0-3)
- [x] Interlinking sequencial (A → B → C)
- [x] Próximos passos documentados
- [x] Relacionados secção com wikilinks
- [ ] **MISSING:** Interlinking bidirecional
- [ ] **MISSING:** Tags semânticas por conceito
- [ ] **MISSING:** Conexões transversais (ex: Shopify Collection em 5 docs)
- [ ] **MISSING:** Links explícitos tipo (Input/Output/Exemplo/Validação)

### 🔴 Interlinking Bidirecional Faltante

**SOP-1 → SOP-2:**
- [ ] SOP-1 cita SOP-2 ✅
- [ ] SOP-2 cita SOP-1 como prerequisito ❌

**SOP-2 → SOP-3:**
- [ ] SOP-2 cita SOP-3 ✅
- [ ] SOP-3 explica que input é SOP-2 ✅

**SOP-3 → SOP-4:**
- [ ] SOP-3 cita SOP-4 ✅
- [ ] SOP-4 não existe ainda ❌

**FASE-0 → FASE-1:**
- [ ] FASE-0 cita FASE-1 ✅
- [ ] FASE-1 cita FASE-0 como prerequisito ✅

### 🟡 Conceitos Transversais não Linkados

**"Shopify Collection" conceito:**
- [ ] SOP-1: recolhe coleções ✅
- [ ] SOP-3: mapeia keywords → coleções ✅
- [ ] FASE-2: otimiza coleções ✅
- [ ] Templates: approval form para coleções ❌ (não existe Template-Collection-Review)
- [ ] [ ] MISSING: Link bidirecional entre estes 4 documentos sob conceito "Shopify Collection"

**"Client Approval Gates" conceito:**
- [ ] FASE-0: setup approval
- [ ] FASE-1: go/no-go decision
- [ ] FASE-2: sampling approval
- [ ] FASE-3: sign-off + celebration
- [ ] [ ] MISSING: Conceito explícito "Client Approval Gates" que liga todos os 4 FASE docs

**"API Integration" conceito:**
- [ ] SOP-1: Shopify API validation
- [ ] SOP-2: DataForSEO, SE Ranking APIs
- [ ] FASE-2: Shopify bulk operations API
- [ ] API-REGISTRY: centralized (⚠️ não existe ainda)
- [ ] [ ] MISSING: Centralizar "APIs" como conceito transversal

---

## Ação: Enriquecimento Semântico

### FASE A: Bidirecionalidade (SOP 1-3 + FASE 0-3)
Para cada SOP/FASE, adicionar seção "**Pré-requisitos**":
```markdown
## Pré-requisitos
- [[SOP-1-STORE-CONTEXT-SETUP]] — Requer store context completamente preenchido
- [[FASE-0-KICKOFF]] — Requer setup técnico e baseline metrics
```

### FASE B: Conceitos Transversais (Tags + Links)
Criar "Concept Hub" documents:
- `CONCEITO-Keyword-Research.md` — centraliza TODOS os links relacionados a KW research
- `CONCEITO-Shopify-Collections.md` — centraliza TODOS os links relacionados a collections
- `CONCEITO-Client-Approval.md` — centraliza TODOS os approval gates

Exemplo structure:
```markdown
# CONCEITO: Shopify Collections

**Definição:** [Uma linha]

**Documentos relacionados:**
- [[SOP-1-STORE-CONTEXT-SETUP]] — Recolhe estrutura (input)
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] — Mapeia keywords (processamento)
- [[FASE-2-EXECUTION]] — Otimiza e publica (execução)
- [[Template-Collection-Review]] — Approval form (validação)
- [[FASE-3-VALIDATION]] — Indexação e monitoring (resultado)

**Fluxo:**
1. SOP-1 recolhe collections existentes
2. SOP-3 mapeia keywords a collections
3. FASE-2 otimiza collection metadata
4. Template aprova drafts
5. FASE-3 valida indexação

**Métricas associadas:**
- GSC indexed collections
- Impressions por collection
- Click-through rate por collection
```

### FASE C: Obsidian CLI Integration
```bash
# Validar interlinking bidirecional
obsidian-cli validate --bidirectional vault/02-SOPs/

# Gerar graph statistics
obsidian-cli graph --stats vault/ > interlinking-report.md

# Encontrar documentos órfãos (sem inlinks)
obsidian-cli orphans vault/
```

---

## Próximos Passos

1. **Enriquecer SOP 1-3 + FASE 0-3** com bidirecionalidade (2-3h)
2. **Criar Concept Hubs** para keywords, collections, approval (3h)
3. **Criar API-REGISTRY** central (interlinking de APIs) (1h)
4. **PHASE 2-6:** Aplicar padrão completo + enriquecimento semântico (24-36h restantes)
5. **Obsidian CLI validation** no final

---

**Versão:** 1.0  
**Data:** 2026-04-21  
**Status:** DRAFT  
**Próximo:** Implementar FASE A (bidirecionalidade nos 7 SOPs atuais)
