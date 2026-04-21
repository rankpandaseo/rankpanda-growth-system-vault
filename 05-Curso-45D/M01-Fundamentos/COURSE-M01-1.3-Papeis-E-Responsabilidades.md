# Aula 1.3 — Papéis e Responsabilidades: O que Cada Um Faz > **Nível:** Iniciante > **Duração estimada:** 15 minutos > **Pré-requisito:** Aula 1.2 (As 4 fases) > **Status:** Em produção --- ## 🎯 Objetivo da Aula Ao final desta aula, o aluno será capaz de: 1. Identificar os 5 papéis principais num 45D Sprint (PM, SEO Specialist, Technical, Content, Cliente)
2. Entender quem aprova o quê e quando
3. Reconhecer o padrão "IA propõe → PM aprova → Especialista executa"
4. Preparar a equipa RankPanda para um sprint (ou adaptar para cliente interno) --- ## 🎬 ABERTURA (0:00 — 1:00) **[Apresentação direta]** > "Aula 1.3 — alguém perguntou-me uma vez: 'Rui, quem é que faz o quê durante o sprint?' Ótima pergunta. Porque se não forem claros os papéis, metade do tempo anda-se a dizer 'eu pensava que tu fazias isto'."
>
> "Isto é especialmente importante se trabalham com clientes internamente vs. com a RankPanda como agência. Os papéis são DIFERENTES."
>
> "Vou mostrar: (1) se a RankPanda faz todo o trabalho, (2) se o cliente faz tudo, e (3) a zona cinzenta onde ambos trabalham." --- ## 📚 SECÇÃO 1: Os 5 Papéis Principais (1:00 — 5:30) **[Tela: organograma 45D Sprint]** ### 1. Project Manager (PM) **Quem:** RankPanda PM ou cliente com papel de PM **Responsabilidades:**
- Garantir que cada fase termina no dia correto
- Agendas das chamadas de aprovação
- Manter cliente informado (Discord updates 3x/semana)
- Escalada se algo fica bloqueado
- Documentar decisões no ClickUp **Exemplo:** "Segunda é kickoff? Segunda as 10h é kickoff, estou a enviar Zoom link agora." --- ### 2. SEO Strategist **Quem:** SEO Specialist RankPanda **Responsabilidades:**
- Conduzir GSC audit (Fase 1)
- Escolher keywords estratégicas (Fase 2)
- Definir estrutura de content (Fase 2)
- Analisar competitive landscape (Fase 1)
- Validar métricas before/after (Fase 3) **Exemplo:** "Estes 5 keywords têm intent alto e tráfego. Isto é por onde começamos." --- ### 3. Technical Specialist **Quem:** Dev RankPanda ou cliente (se tiver) **Responsabilidades:**
- Auditar robots.txt, sitemap, canonical (Fase 1)
- Implementar JSON-LD schema (Fase 2)
- Optimizar Core Web Vitals (Fase 2)
- Monitorar crawl/indexation (Fase 2-3)
- Troubleshooting de erros técnicos **Exemplo:** "Robots.txt está bloqueando 80% dos products. 2 horas para desbloquear." --- ### 4. Content/Copywriter **Quem:** Redator RankPanda ou cliente **Responsabilidades:**
- Escrever conteúdo otimizado (Fase 2)
- Rever titles/descriptions de produtos (Fase 2)
- Criar copy para email/social (fora do 45D, mas coordenado)
- Garantir brand voice mantém-se **Exemplo:** "Briefing aprovado. Entrego 5 peças quinta-feira." --- ### 5. Cliente (Stakeholder Principal) **Quem:** Owner loja ou marketing lead do cliente **Responsabilidades:**
- Aprovar diagnóstico (Fase 1, fim sexta)
- Aprovar keywords + descriptions (Fase 2, semanal)
- Dar acesso a ferramentas (GSC, GA4, Shopify, etc)
- Responder a perguntas rápidas (dentro de 24h, idealmente)
- Decisão final em continuidade (Fase 3, sexta) **Exemplo:** "Aprovam estes keywords? Têm 24 horas para feedback." --- ## 📚 SECÇÃO 2: O Padrão "IA Propõe → PM Aprova → Especialista Executa" (5:30 — 8:30) **[Tela: fluxo da decisão]** > "Isto é CRÍTICO. Este padrão é o que permite RankPanda com 4 pessoas gerir 10+ clientes." ### Exemplo Real: KW Research ```
SEGUNDA MANHÃ: IA (Claude Code): "Analisei GSC. Top 20 keywords por oportunidade: 1. 'vibrador silencioso' — 800/mês, 15% CTR, 5ª posição 2. 'brinquedo discreto' — 600/mês, 12% CTR, 12ª posição ... Proposta: Começar por top 5 + criar conteúdo para top 10" PM (Rui): "Isto faz sentido. Concordo. Vou apresentar ao cliente." PM → CLIENTE (via Discord): "Aprovam estes keywords para começar? Resposta esperada: 24 horas" TERÇA MANHÃ (se cliente disse SIM): SEO Specialist: "Aprovado. Criei briefing para redator: - KW1: Meta description < 160 chars - KW2: Title com long-tail variant - KW3: Headers optimizados ..." REDATOR: "Briefing recebido. Entrego 3 peças quarta." QUINTA: Cliente aprova peças. Technical faz upload. GSC submit.
``` **Pepita #5:** "IA propõe (minutos), PM aprova (segundos), especialista executa (horas). Isto é parallelização real." --- ## 📚 SECÇÃO 3: Variações: Agência vs. Cliente Interno (8:30 — 12:00) **[Tela: tabela comparativa]** ### Cenário A: RankPanda Executa Tudo (Agência) ```
PM: Rui (RankPanda)
SEO: João (RankPanda)
Technical: Pedro (RankPanda)
Content: Sara (RankPanda)
Cliente: Proprietário loja (aprova, feedback, acesso) Vantagem: Consistência, velocidade, expertise centralizada
Risco: Cliente menos envolvido, ownership difuso
``` --- ### Cenário B: Cliente Faz Execução (Consultoria) ```
PM: Rui (RankPanda)
SEO: Rui (RankPanda)
Technical: Dev cliente
Content: Redator cliente
Cliente: Coordena execução interna Vantagem: Cliente aprende, ownership forte, sustentável
Risco: Mais lento (cliente tem outras prioridades)
``` --- ### Cenário C: Híbrido (Mais Comum) ```
PM: Rui (RankPanda)
SEO: João (RankPanda) + Cliente consultant
Technical: Pedro (RankPanda)
Content: Sara (RankPanda) + redator cliente
Cliente: Aprova, feedback, acesso Vantagem: Velocidade + aprendizagem + scalability
Risco: Coordenação entre partes
``` > "Na RankPanda, fazemos Cenário A por default. Clientes que querem Cenário B pagam menos (consultoria). Cenário C é o mais comum quando cliente tem internals fracos." --- ## 📚 SECÇÃO 4: Cadência de Comunicação (12:00 — 14:00) **[Tela: calendário semanal]** | Dia | Hora | O quê | Quem | Duração |
|-----|------|-------|------|---------|
| **Segunda** | 10:00 | Kickoff (Fase 0) ou Status check | PM + Equipa + Cliente | 1h |
| **Terça** | 14:00 | Mid-week diagnostics | PM + Specialists | 30min |
| **Quarta** | 16:00 | Approval gate (keywords, descriptions) | PM + Cliente | 15-30min |
| **Sexta** | 10:00 | Weekly status + metrics | PM + Equipa | 30min |
| **Sexta** | 16:00 | Cliente update (Discord) | PM | 5min (async) | **Extra:** Escalação imediata se algo fica bloqueado (e-mail, Discord mention) --- ## 🎯 RESUMO ```
5 Papéis: PM, SEO Specialist, Technical, Content, Cliente
1 Padrão: IA propõe → PM aprova → Especialista executa
3 Cenários: Agência (RankPanda faz tudo), Consultoria (cliente faz), Híbrido
1 Cadência: 4-5 touchpoints/semana, aprovações on-demand
``` **Pepita #6:** "Papéis claros = zero retrabalho. Papéis confusos = 30% do tempo em reuniões." --- ## 💡 Próxima Aula Aula 1.4 — Por que Este Framework Vence os 6 Meses de Agência Tradicional --- **Status:** ✅ Completa **Última atualização:** [hoje] **Autor:** RankPanda Growth System
