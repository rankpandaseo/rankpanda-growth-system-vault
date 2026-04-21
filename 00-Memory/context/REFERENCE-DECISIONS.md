# Decisões Arquitecturais — RankPanda Shopify SEO System | Campo | Valor |
|-------|-------|
| **Título** | Decisões Arquitecturais (INVIOLÁVEL) |
| **Data Criação** | 2026-04-18 | --- ## 1. APIs Diretas, Nunca MCP (2026-04-18) **Decisão:** Todas as integrações via API diretas (Shopify, GSC, GA4, SE Ranking, ClickUp, Gmail, Calendar, Drive, Leexi). NUNCA via MCP. **Razão:** - APIs dão acesso direto às credenciais do Rui (já estão no GitHub rankpandaseo/rankpanda-vault)
- MCP adicionaria complexidade desnecessária
- Performance e agilidade são críticos **Implicações:**
- Código de integração fica no `/vault/03-Automações/`
- Cada integração tem um script (gscs-api.py, ga4-api.py, shopify-api.py, etc.)
- Scheduled tasks chamam estes scripts periodicamente
- Métricas diárias são puxadas automaticamente (GSC, GA4, Shopify) --- ## 2. 45D Sprint como Unidade de Execução (2026-04-18) **Decisão:** Cada cliente passa por um 45D Sprint estruturado em 4 FASES:
- FASE 0: Kickoff (Dia 1-5)
- FASE 1: Diagnostic (Dia 6-12)
- FASE 2: Execution (Dia 13-40) — 4 streams paralelos
- FASE 3: Validation (Dia 41-45) **Razão:**
- Garante entrega de resultados em tempo fixo
- Estrutura a operacionalização do método RankPanda
- Permite paralelização e agilização
- Gera métricas mensuráveis (antes/depois) **Implicações:**
- Vault organizado por `/01-Clientes/[cliente]/FASE-X-*.md`
- ClickUp estruturado com 4 listas (uma por FASE)
- Memory atualizado a cada FASE
- ROI calculado no fim (FASE 3) --- ## 3. Vault como Fonte de Verdade (2026-04-18) **Decisão:** O vault (GitHub) é a source-of-truth para SOPs, templates, course material, e decisões. **Razão:**
- Tudo versionado no Git
- Replicável para novos clientes (copia o SOP, adapta aos IDs específicos)
- Transparência: Rui pode auditar tudo
- Suporta evolução contínua (lições alimentam SOPs) **Implicações:**
- `/vault/02-SOPs/FASE-*-*.md` são o playbook para cada fase
- `/vault/04-Templates/` são templates reutilizáveis
- `/vault/05-Curso-45D/` cresce com learnings reais
- Cada commit documenta evolução do sistema --- ## 4. Scaffold Automático para Novos Clientes (2026-04-18) **Decisão:** Quando um cliente entra, um script automático:
1. Cria `memory/projects/[cliente].md`
2. Lê `kickoff-briefing-form.md` preenchido pelo cliente
3. Extrai dados (AOV, volume, IDs de ferramentas, etc.)
4. Popula `memory/context/people.md` (contacts, dinâmicas)
5. Cria `memory/pending.md` (o que cliente prometeu)
6. Cria primeira entrada em `memory/sessions/estado-atual.md` **Razão:**
- Zero overhead manual
- Cliente onboard instantaneamente
- Memory alimentado desde dia 1
- Escalável para múltiplos clientes **Implicações:**
- Script em `/vault/03-Automações/onboarding-scaffold.py`
- Triggered quando cliente submete kickoff-briefing-form.md
- Output: ficheiros prePoulados, prontos para Rui revisar
- Mensagem confirma Rui: "Cliente [nome] onboarded. [N] fields pendentes para validação." --- **Próxima revisão:** Após Sprint 001 — Vibradores (FASE 3)
