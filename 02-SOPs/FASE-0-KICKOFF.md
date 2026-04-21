---
name: fase-0-kickoff
description: Align business context, validate technical setup, capture baseline metrics, prepare for 45D sprint
type: fase
status: active
foco: operacional
tags: [kickoff, setup, baseline, alignment]
wikilinks: [[SOP-1-STORE-CONTEXT-SETUP-v2]], [[FASE-1-DIAGNOSTIC]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
--- # SOP FASE 0 — Kickoff (3-5 dias) **Resumo:** Alinhar negócio com cliente, recolher acessos técnicos, desenhar baseline de métricas, preparar organização (Obsidian, Discord, ClickUp) para sprint. --- ## 🎯 Por Que Isto Importa **Impacto no sucesso do sprint:**
- **Alinhamento comercial:** Sem compreensão clara de AOV, sazonalidade, concorrência, gastamos 45 dias a otimizar keywords que não convertem. Kickoff claro = direção certa desde dia 1.
- **Setup técnico completo:** Falta de GSC, GA4, Shopify API = cegueira durante execução. Não conseguimos medir impacto real das mudanças (SOP 4-5) até FASE 2-3. Validação aqui evita surpresas.
- **Baseline metrics:** Sem impressões/clicks/posição iniciais em GSC, não temos como provar sucesso em FASE 3. Kickoff captura este snapshot.
- **Comunicação estruturada:** Cliente sabe o que esperar, prazos, processos. Reduz churn, aumenta confiança, permite feedback rápido durante execução. **Sem FASE 0 bem feita:** Começamos SOP 1 sem contexto. Resultado: refactoring no meio (dias perdidos), cliente confuso, métricas incompletas, roadmap vago. --- ## 📋 Pré-requisitos Antes de começar FASE-0:
- ↔ Contrato assinado (oficial)
- ↔ Cliente tem acesso administrativo a Shopify
- ↔ Cliente tem conta Google (para GSC + GA4)
- ↔ Paralelo com [[SOP-1-STORE-CONTEXT-SETUP-v2]] — podem correr em simultâneo após kickoff inicial --- ## ⚡ Quick Checklist - [ ] Kickoff call agendada e concluída (1h)
- [ ] Briefing form (negócio + técnico) preenchido
- [ ] Acesso Shopify, GSC, GA4 validado
- [ ] SE Ranking API key testada
- [ ] Discord channel criado + cliente convidado
- [ ] ClickUp space criado com templates
- [ ] Obsidian vault `/memory/projects/[loja]/` inicializado
- [ ] Baseline metrics capturados (indexed, impressions, clicks, avg position)
- [ ] Roadmap visual de 45 dias aprovado com cliente
- [ ] Go/No-go decision tomada → Pronto para [[FASE-1-DIAGNOSTIC]] --- ## 🔑 Key Principles 1. **Clarity First:** Kickoff não é "vamos fazer SEO". É "implementaremos SOP 1-5 nesta ordem, com aprovações aqui, e esperamos X resultados".
2. **Technical Validation:** Todos os acessos API testados ANTES de iniciar. Não descobrimos GSC broken na FASE 1.
3. **Baseline is Truth:** Capturamos snapshot (dia 0) de indexed, impressions, clicks, position. Qualquer análise futura compara contra este baseline.
4. **Shared Ownership:** Cliente sabe que vai receber relatórios semanais, vai ser consultado em decisões estratégicas, tem propriedade do resultado.
5. **Operational Excellence:** Obsidian + Discord + ClickUp integrados desde dia 1. Zero fricção para comunicação e documentation. --- ## Operacional: AUDITORIA (Weak Points Detection) ### Checklist de Audição **Negócio:**
- [ ] Modelo de negócio compreendido (dropshipping, estoque próprio, marketplace, etc)
- [ ] AOV (Average Order Value) e volume mensal conhecidos
- [ ] Sazonalidade e ciclos de procura identificados
- [ ] Concorrência direta listada (3-5 players) **Técnico:**
- [ ] Acesso Shopify admin confirmado (OAuth integrado)
- [ ] Google Search Console vinculado
- [ ] Google Analytics 4 ativo e com eventos configurados
- [ ] SE Ranking API key validada
- [ ] Robots.txt existente e analisado
- [ ] Sitemap.xml existente **Comum:**
- [ ] Acesso Discord do cliente confirmado
- [ ] Acesso ao ClickUp space validado
- [ ] Email client para notificações em ficheiro ### Gaps Identificados _Preencher aqui durante kickoff call:_ **Gap 1:** [descrição]
- **Impacto:** [alto/médio/baixo]
- **Ação:** [o que fazer] **Gap 2:** [descrição]
- **Impacto:** [alto/médio/baixo]
- **Ação:** [o que fazer] --- ## Como Estruturar Kickoff Call (1h) 1. **Warm-up (5 min)** — Apresentação da equipa, tom casual, segurança psicológica
2. **Contexto (10 min)** — Explicar o que é 45D, 4 fases, entregáveis
3. **Negócio (15 min)** — Entender loja, AOV, target, concorrência
4. **Expectativas (10 min)** — O que é realista esperar, desmistificar SEO
5. **Processo (15 min)** — Explicar aprovações, timeline, comunicação
6. **Acessos (5 min)** — Listar o que precisamos, confirmar prazos ### Como Preencher Briefing Form Dados obrigatórios:
- Nome da loja + domínio
- Produto principal (nicho, categoria)
- Volume mensal (aproximado)
- AOV (price point)
- Principais coleções (top 5-10)
- Tom de voz (formal, casual, funny, etc)
- Goals (sessões/mês, conversões, CPA) ### Como Validar Setup Técnico **GSC:**
- Verificar que está linkado à propriedade correta
- Verificar Search Appearance (title templates, metadata) **GA4:**
- Confirmar eventos básicos (page_view, purchase, add_to_cart)
- Verificar que trackingId está correto **Shopify API:**
- Testar que conseguimos ler collections e products
- Testar metafields read/write --- ## Execução: ClickUp Space + Tarefas ### ClickUp Space Template (FASE 0) **Project Name:** `[Loja] — 45D Sprint` **Using Templates:** See `/04-Templates/` for kickoff-briefing-form.md and weekly-update-template.md **Folders:**
1. **KICKOFF** (3-5 dias) - [ ] Kickoff call agendada - [ ] Briefing form enviado ao cliente - [ ] Respostas recebidas e validadas - [ ] Setup técnico (Obsidian vault, Discord, ClickUp) - [ ] Integrações ativas (Shopify, GSC, GA4) - [ ] Baseline metrics recolhidas 2. **PHASE 1 PREP** (antes de iniciar) - [ ] Diagnóstico planejado - [ ] Templates carregados - [ ] Briefing aprovado - [ ] Go/No-go decision ### Tarefas Específicas (7 Tasks) #### Task 1 — Agendar Kickoff Call
- **Assignee:** [RankPanda owner]
- **Due:** Day 1
- **Description:** Coordenar com cliente melhor dia/hora para 1h call
- **Dependencies:** Nenhuma #### Task 2 — Enviar Briefing Form
- **Assignee:** [RankPanda owner]
- **Due:** Day 1 (após kickoff call)
- **Description:** Enviar form com campos de negócio + técnico
- **Dependencies:** Kickoff call completa #### Task 3 — Criar Obsidian Vault
- **Assignee:** [RankPanda tech]
- **Due:** Day 2
- **Description:** Criar pasta `/memory/projects/[loja-slug]/` com templates iniciais
- **Dependencies:** Briefing form recebido #### Task 4 — Setup Discord Channel
- **Assignee:** [RankPanda tech]
- **Due:** Day 2
- **Description:** Criar #shopify-[loja-nome] com bot integrado, convidar cliente
- **Dependencies:** Nenhuma #### Task 5 — Validar Integrações
- **Assignee:** [RankPanda tech]
- **Due:** Day 3
- **Description:** Testar GSC, GA4, SE Ranking, Shopify API. Documentar erros.
- **Dependencies:** Setup técnico #### Task 6 — Recolher Baseline Metrics
- **Assignee:** [RankPanda analytics]
- **Due:** Day 4
- **Description:** Capturar indexed pages, impressions, clicks, avg position de GSC
- **Dependencies:** GSC integração ativa #### Task 7 — Kickoff Approval Gate
- **Assignee:** [RankPanda owner]
- **Due:** Day 5
- **Description:** Validar que tudo está pronto. Decisão: Go FASE 1 ou ajustes?
- **Dependencies:** Todas as tasks acima --- ## Validação & Entregáveis 1. ✅ Sprint briefing aprovado
2. ✅ Vault + Discord + ClickUp prontos
3. ✅ Baseline metrics capturadas (indexed, impressions, clicks, position)
4. ✅ Roadmap visual de 45 dias
5. ✅ Comunicação Clara com cliente sobre próximas etapas --- ## 🔗 Relacionados **Fluxo Sequencial:**
- [[SOP-1-STORE-CONTEXT-SETUP-v2]] → **Output:** Setup técnico e baseline metrics alimentam SOP-1 (contexto da loja)
- [[FASE-1-DIAGNOSTIC]] → **Próximo:** Diagnóstico estratégico com dados de GSC e GA4 capturados aqui em FASE-0 **Conceitos Técnicos (Hubs):**
- [[API-REGISTRY]] ↔ **Referência:** Validar que todas APIs (Shopify, GSC, GA4, SE Ranking, ClickUp) estão funcionando **Contexto Paralelo:**
- ↔ [[SOP-1-STORE-CONTEXT-SETUP-v2]] — pode correr em paralelo com FASE-0 após kickoff inicial **Exemplos & Referência:**
- [[PILOT-VIBRADORES-00-MASTER-PLAN]] → **Caso Real:** Kickoff do projeto pilot com vibradores --- **Versão:** 2.0 **Data:** 2026-04-21 **Status:** ATIVO **Próximo:** [[SOP-1-STORE-CONTEXT-SETUP-v2]] + [[FASE-1-DIAGNOSTIC]] **Data:** 2026-04-21 **Status:** ATIVO **Próximo:** [[FASE-1-DIAGNOSTIC]] (após aprovação go/no-go)
