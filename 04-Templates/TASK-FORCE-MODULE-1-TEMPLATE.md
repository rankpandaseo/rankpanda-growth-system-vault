---
name: TASK-FORCE-MODULE-1-TEMPLATE
description: Template para lançar uma "task force" (sub-agent) por cada gap P0-P2 do módulo MLforSEO Fundamentals + auditor no fim
type: template
status: active
foco: technical
tags: [task-force, semantic-kw, etapa-2, agent-prompt, audit]
wikilinks: [[../02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07]], [[../02-SOPs/SOP-2-KEYWORD-RESEARCH-V2]]]
---

# Task Force Template — Module 1 Semantic KW Gaps

**Resumo:** Padrão para lançar agents de implementação dos gaps P0-P2 identificados em [[../02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07]], seguidos de auditor agent.

---

## 🎯 Quando Usar

Sempre que se queira fechar um dos 9 gaps do módulo MLforSEO Fundamentals (ver `[[../02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07]]` secção "Gaps Priorizados"):
- P0 #1 — Custom prominence metric
- P0 #2 — Co-occurring n-grams por entidade
- P0 #3 — EAV combination generator
- P1 #4 — Knowledge Graph integration
- P1 #5 — Fuzzy matching para query distance
- P1 #6 — DataForSEO SERP scraping
- P2 #7 — Google Autocomplete
- P2 #8 — Semantic relationship graph (TF-IDF + cosine)
- P2 #9 — K-means clustering + PCA

---

## ⚡ Workflow (3 fases)

### Fase 1 — Implementação (general-purpose agent)

Lança um sub-agent com o template abaixo. Isolation `worktree` recomendado para mudanças não-triviais.

```
description: "P[0-2] #N — [nome curto do gap]"
subagent_type: general-purpose
isolation: worktree
prompt: |
  [Ver Prompt Template "Implementador" abaixo]
```

### Fase 2 — Verificação manual (Rui ou agent main)

- Rever diff completo (não confiar em sumário do agent)
- Smoke-test no VPS se aplicável
- Aprovar antes de merge

### Fase 3 — Auditor (agent dedicado)

Lança um segundo sub-agent depois do merge para audit.

```
description: "Auditor — P[0-2] #N — [nome curto]"
subagent_type: general-purpose
prompt: |
  [Ver Prompt Template "Auditor" abaixo]
```

---

## 📝 Prompt Template — Implementador

```
És um implementador de uma task force focada em fechar UM gap específico do módulo
"Fundamentals of Semantic Keyword Research" (MLforSEO/Lazarina Stoy) na nossa app
RankPanda Shopify.

CONTEXTO OBRIGATÓRIO (lê antes de tocar em código):
1. /Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07.md
   — relatório completo dos 9 gaps. Lê especialmente a secção do gap que vais fechar.
2. /Users/rankpanda/.claude/projects/-Users-rankpanda-Shopify-RankPanda-APP---Oficial-2026/memory/reference_app_routes_and_structure.md
   — mapa de rotas, services, DB requirements.
3. /Users/rankpanda/.claude/projects/-Users-rankpanda-Shopify-RankPanda-APP---Oficial-2026/memory/reference_vps_deployment.md
   — paths reais no VPS, deploy flow.

GAP A FECHAR: [P0/P1/P2 #N — nome do gap]

REQUISITO FUNCIONAL:
[Especificação do que deve ser implementado, copiada da secção do gap em ETAPA-2-VALIDATION-MLforSEO-2026-05-07.md]

REGRAS DE OURO:
- Não duplicar funcionalidade que já exista. Procura primeiro com grep antes de criar.
- Não tocar em ficheiros fora do scope deste gap.
- Não fazer "improvements" laterais — só o que é estritamente pedido.
- Se descobrires que o gap depende de outro gap não-fechado, PARA e reporta. Não inventes solução paralela.
- Manter padrões existentes (Prisma, Express routes, Remix actions, etc.).
- Migrations Prisma: criar em shopify-app/prisma/migrations/ se necessário.
- Tests: se houver test harness existente para o módulo afectado, adicionar test mínimo.

ENTREGÁVEIS:
1. Código implementado e a passar typecheck (npx tsc --noEmit -p shopify-app/).
2. Migration Prisma se a feature exigir DB changes.
3. Curto README inline (comments) explicando o porquê das decisões críticas.
4. Sumário em markdown (max 300 palavras) com:
   - Ficheiros tocados (paths)
   - Decisões importantes
   - Trade-offs
   - O que NÃO foi feito mas devia ser (deixar para o auditor)
   - Como testar end-to-end

NÃO FAZER:
- Não fazer commit nem push. Deixa em working tree para revisão do Rui.
- Não correr migrations contra DB de produção.
- Não tocar em CLAUDE.md, no vault, nem em memory/ — esses são domínio do Rui.
```

---

## 📝 Prompt Template — Auditor

```
És um auditor independente de uma implementação acabada de fazer. Não confias no
sumário do implementador — verificas tudo contra o código real.

ALVO DA AUDITORIA:
- Gap fechado: [P0/P1/P2 #N — nome do gap]
- Branch: [branch onde foi implementado]
- Commits a auditar: [SHAs ou range]

CONTEXTO OBRIGATÓRIO:
1. /Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07.md
   — especificação original do gap.
2. Ver os transcripts da MLforSEO em /SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS.md
   para o conceito teórico que o gap implementa.

CHECKS OBRIGATÓRIOS (todos):

A. Cobertura funcional
   - O código implementa O QUE A AULA ENSINA, ou só uma versão diluída?
   - Compara o output gerado com o exemplo da aula. Listar divergências.

B. Bugs / regressões
   - Correr npx tsc --noEmit -p shopify-app/ — listar erros novos vs pré-existentes
     (pré-existentes documentados em memory/sessions/estado-atual.md)
   - Procurar TODOs / FIXMEs introduzidos
   - Verificar nullability / edge cases
   - Verificar error handling em chamadas a APIs externas
   - Verificar se há queries SQL não-parametrizadas (SQL injection)
   - Verificar se há credenciais hardcoded

C. Padrões do codebase
   - Usa o pattern de Prisma transaction onde aplicável?
   - Está a usar o ShopRequest middleware para shop-aware routes?
   - Usa o INTERNAL_SERVICE_TOKEN nas chamadas keywords-service?
   - Migrations Prisma seguem a convenção de naming + timestamp?

D. Performance
   - Há N+1 queries?
   - Há loops síncronos sobre datasets grandes?
   - Há leitura completa de tabelas que deveria ser paginada?

E. Documentação
   - Há comentário a explicar decisões não-óbvias?
   - O sumário do implementador bate certo com o que está no código?

F. Cobertura do gap
   - Volta a ler ETAPA-2-VALIDATION-MLforSEO-2026-05-07.md secção do gap.
   - O gap está REALMENTE fechado, ou só parcialmente? Listar partes em falta.

ENTREGÁVEIS:
- Relatório em markdown (max 800 palavras) com:
  1. Veredicto: ✅ Pronto / ⚠️ Pronto com correções menores / ❌ Não pronto
  2. Lista de bugs encontrados (severidade + path:line + fix sugerido)
  3. Lista de regressões / risk areas
  4. Lista de melhorias (não-bloqueantes mas recomendadas)
  5. Lista do que está em falta para o gap ficar 100% fechado
  6. Sugestão de testes adicionais

NÃO FAZER:
- Não corrigir nada. Só auditar.
- Não fazer commit. Não tocar no código.
```

---

## 🔁 Sequenciamento Recomendado

Para fechar o módulo inteiro em ~5-6 dias:

1. **Onda 1 (P0):** #1 + #2 paralelo (~1 dia) → #3 (~2 dias)
2. **Onda 2 (P1):** #4 (~½ dia) → #6 (~1 dia)
3. **Onda 3 (P1+P2):** #5 + #7 paralelo (~1 dia)
4. **Onda 4 (P2 analítica):** #8 + #9 (~1 dia)

Após cada gap fechado: **auditor + verificação Rui + merge para main**. CI faz deploy automático.

---

## 🔗 Relacionados

- `[[../02-SOPs/ETAPA-2-VALIDATION-MLforSEO-2026-05-07]]` — Especificação completa dos 9 gaps
- `[[../02-SOPs/SOP-2-KEYWORD-RESEARCH-V2]]` — Pipeline operacional onde os outputs são consumidos
- `[[../../SEMANTIC-KEYWORD-RESEARCH-COURSE-MATERIALS]]` — Source teórico (17 lições MLforSEO)
