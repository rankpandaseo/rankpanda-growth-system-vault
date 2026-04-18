# SOP FASE 0 — Kickoff (3-5 dias)

## 🎯 Objetivo

Alinhar negócio, recolher acessos, desenhar baseline e preparar a loja para sprint de 45 dias.

---

## CAMADA 1 — AUDITORIA (Weak Points Detection)

### Checklist de Audição

**Negócio:**
- [ ] Modelo de negócio compreendido (dropshipping, estoque próprio, marketplace, etc)
- [ ] AOV (Average Order Value) e volume mensal conhecidos
- [ ] Sazonalidade e ciclos de procura identificados
- [ ] Concorrência direta listada (3-5 players)

**Técnico:**
- [ ] Acesso Shopify admin confirmado (OAuth integrado)
- [ ] Google Search Console vinculado
- [ ] Google Analytics 4 ativo e com eventos configurados
- [ ] SE Ranking API key validada
- [ ] Robots.txt existente e analisado
- [ ] Sitemap.xml existente

**Comum:**
- [ ] Acesso Discord do cliente confirmado
- [ ] Acesso ao ClickUp space validado
- [ ] Email client para notificações em ficheiro

### Gaps Identificados

_Preencher aqui durante kickoff call:_

**Gap 1:** [descrição]
- **Impacto:** [alto/médio/baixo]
- **Ação:** [o que fazer]

**Gap 2:** [descrição]
- **Impacto:** [alto/médio/baixo]
- **Ação:** [o que fazer]

---

## CAMADA 2 — FORMATIVO (How-To / Teaching Module)

### Porque é Importante Kickoff

O kickoff bem estruturado evita:
- Retrabalho no meio da execução
- Falta de comunicação com cliente
- Setup técnico incompleto (acessos missing)
- Definição vaga de objetivos
- Desperdício de 45 dias em caminhos errados

**Princípio:** Startup mental para ambos os lados (RankPanda + Cliente)

### Como Estruturar Kickoff Call (1h)

1. **Warm-up (5 min)** — Apresentação da equipa, tom casual, segurança psicológica
2. **Contexto (10 min)** — Explicar o que é 45D, 4 fases, entregáveis
3. **Negócio (15 min)** — Entender loja, AOV, target, concorrência
4. **Expectativas (10 min)** — O que é realista esperar, desmistificar SEO
5. **Processo (15 min)** — Explicar aprovações, timeline, comunicação
6. **Acessos (5 min)** — Listar o que precisamos, confirmar prazos

### Como Preencher Briefing Form

Dados obrigatórios:
- Nome da loja + domínio
- Produto principal (nicho, categoria)
- Volume mensal (aproximado)
- AOV (price point)
- Principais coleções (top 5-10)
- Tom de voz (formal, casual, funny, etc)
- Goals (sessões/mês, conversões, CPA)

### Como Validar Setup Técnico

**GSC:**
- Verificar que está linkado à propriedade correta
- Verificar Search Appearance (title templates, metadata)

**GA4:**
- Confirmar eventos básicos (page_view, purchase, add_to_cart)
- Verificar que trackingId está correto

**Shopify API:**
- Testar que conseguimos ler collections e products
- Testar metafields read/write

---

## CAMADA 3 — TEMPLATE ClickUp (Operational Tasks)

### ClickUp Space Template (FASE 0)

**Project Name:** `[Loja] — 45D Sprint`

**Folders:**
1. **KICKOFF** (3-5 dias)
   - [ ] Kickoff call agendada
   - [ ] Briefing form enviado ao cliente
   - [ ] Respostas recebidas e validadas
   - [ ] Setup técnico (Obsidian vault, Discord, ClickUp)
   - [ ] Integrações ativas (Shopify, GSC, GA4)
   - [ ] Baseline metrics recolhidas

2. **PHASE 1 PREP** (antes de iniciar)
   - [ ] Diagnóstico planejado
   - [ ] Templates carregados
   - [ ] Briefing aprovado
   - [ ] Go/No-go decision

### Tarefas Específicas

#### Task 1 — Agendar Kickoff Call
- **Assignee:** [RankPanda owner]
- **Due:** Day 1
- **Description:** Coordenar com cliente melhor dia/hora para 1h call
- **Dependencies:** Nenhuma

#### Task 2 — Enviar Briefing Form
- **Assignee:** [RankPanda owner]
- **Due:** Day 1 (após kickoff call)
- **Description:** Enviar form com campos de negócio + técnico
- **Dependencies:** Kickoff call completa

#### Task 3 — Criar Obsidian Vault
- **Assignee:** [RankPanda tech]
- **Due:** Day 2
- **Description:** Criar pasta `/memory/projects/[loja-slug]/` com templates iniciais
- **Dependencies:** Briefing form recebido

#### Task 4 — Setup Discord Channel
- **Assignee:** [RankPanda tech]
- **Due:** Day 2
- **Description:** Criar #shopify-[loja-nome] com bot integrado, convidar cliente
- **Dependencies:** Nenhuma

#### Task 5 — Validar Integrações
- **Assignee:** [RankPanda tech]
- **Due:** Day 3
- **Description:** Testar GSC, GA4, SE Ranking, Shopify API. Documentar erros.
- **Dependencies:** Setup técnico

#### Task 6 — Recolher Baseline Metrics
- **Assignee:** [RankPanda analytics]
- **Due:** Day 4
- **Description:** Capturar indexed pages, impressions, clicks, avg position de GSC
- **Dependencies:** GSC integração ativa

#### Task 7 — Kickoff Approval Gate
- **Assignee:** [RankPanda owner]
- **Due:** Day 5
- **Description:** Validar que tudo está pronto. Decisão: Go FASE 1 ou ajustes?
- **Dependencies:** Todas as tasks acima

---

## ✅ Entregáveis Fase 0

1. ✅ Sprint briefing aprovado
2. ✅ Vault + Discord + ClickUp prontos
3. ✅ Baseline metrics capturadas (indexed, impressions, clicks, position)
4. ✅ Roadmap visual de 45 dias
5. ✅ Comunicação Clara com cliente sobre próximas etapas

---

**Versão:** 1.0  
**Última Atualização:** [data]  
**Owner:** [nome]
