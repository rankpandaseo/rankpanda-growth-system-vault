# Aula 1.2 — As 4 Fases em Detalhe: O que Acontece em Cada Semana do Sprint

> **Nível:** Iniciante  
> **Duração estimada:** 25 minutos  
> **Pré-requisito:** Aula 1.1 (O que é 45D Sprint)  
> **Status:** Em produção

---

## 🎯 Objetivo da Aula

Ao final desta aula, o aluno será capaz de:

1. Descrever o que acontece em cada uma das 4 fases (Kickoff, Diagnostic, Execution, Validation)
2. Entender o timeline semanal e o que entregar ao fim de cada semana
3. Reconhecer os aprovação-gates que marcam transições entre fases
4. Preparar-se mentalmente para o ritmo intenso do sprint

---

## 🎬 ABERTURA (0:00 — 1:30)

**[Apresentação direta]**

> "Aula 1.2 — agora que sabem o QUÊ é 45D Sprint e POR QUÊ funciona, vamos ao COMO."
>
> "Estas 4 fases não são teóricas. São o que fazemos toda a semana na RankPanda. Cada fase tem um objetivo claro, um deliverable claro, e um momento em que o cliente aprova ou diz 'isto não funciona'."
>
> "Isto é importante: se a Fase 0 não for bem feita, a Fase 1 fica comprometida. Se a Fase 1 não identificar os problemas certos, a Fase 2 é 30% menos eficaz. Este é um sistema sequencial com gates de aprovação."

---

## 📚 SECÇÃO 1: FASE 0 — Kickoff (Dias 1-5) (1:30 — 5:30)

**[Tela: timeline visual FASE 0]**

### Objetivo

Alinhar cliente, equipa, e ferramentas. Zero execução. Puro setup.

### Timeline Detalhado

```
Segunda (Dia 1-2): Kickoff Call + Briefing
  - 2h chamada síncrona (cliente, PM, 1-2 especialistas)
  - Explicar o modelo 45D
  - Recolher informações críticas (histórico, objetivos, restrições)
  - Setup de acesso (GSC, GA4, ClickUp, Discord, Shopify)

Terça-Quarta (Dia 2-3): Documentação + Setup
  - Criar workspace no ClickUp
  - Criar canal privado no Discord
  - Conectar integrações (GSC API, GA4, Shopify, SE Ranking)
  - Baseline metrics: impressões, cliques, CTR, posições atuais

Quinta (Dia 5): Apresentação do Plano
  - Resumo briefing ao cliente
  - Explicar o que vai acontecer em cada fase
  - Feedback: "fazem sentido estas 4 fases?"
  - Aprovação: GO/NO-GO para Fase 1
```

### Deliverables

- ✅ Briefing document (2-3 páginas com contexto cliente)
- ✅ ClickUp space totalmente configurado
- ✅ Discord canal pronto
- ✅ Baseline metrics registadas
- ✅ Aprovação cliente para Fase 1

**Pepita #1:** "Documentação clara no Kickoff evita 10 conversas depois"

---

## 📚 SECÇÃO 2: FASE 1 — Diagnostic (Dias 6-14) (5:30 — 12:00)

**[Tela: timeline visual FASE 1]**

### Objetivo

Identificar os 3-5 problemas que MAIS travam crescimento. Não auditoria completa. Diagnóstico cirúrgico.

### Timeline Detalhado

```
Semana 2:

Segunda:   GSC Audit
           - Quais pages estão impressionadas mas não clicam?
           - Quais queries têm CTR < 5%?
           - Quais queries são "branded" vs "topical"?
           → Task no ClickUp: "Relatório GSC — Top 20 opportunities"

Terça:     GA4 + Behavioral Audit
           - De onde vem o tráfego atual?
           - Qual a taxa de bounce por página?
           - Qual a conversão por traffic source?
           → Task: "GA4 behavioral analysis"

Quarta:    Technical Audit (Rápido)
           - Robots.txt está correto?
           - Sitemap.xml está completo?
           - Core Web Vitals: verde, amarelo, ou vermelho?
           - Canonical tags: configurados?
           → Task: "Technical audit checklist"

Quinta:    Competitive Analysis (Nível Alto)
           - Top 3 competitors: quais keywords rankam?
           - Qual a estratégia deles (conteúdo, links, estrutura)?
           → Task: "Competitive landscape summary"

Sexta:     Consolidação + Apresentação
           - Sintetizar tudo em "Top 5 Opportunidades"
           - Apresentar ao cliente: "Aqui estão os 5 problemas que matam o vosso crescimento"
           - Aprovação: "Concordam? Isto faz sentido?"
           → Approval gate: Cliente aprova os 5 problemas identificados
```

### Deliverables

- ✅ GSC opportunity report (top 20 queries com ação clara)
- ✅ GA4 behavioral analysis (fontes, bounce, conversões)
- ✅ Technical audit (checklist + prioridades)
- ✅ Competitive landscape (3 competitors, 10-15 keywords cada)
- ✅ "Top 5 Opportunidades" apresentadas e aprovadas

**Pepita #2:** "Diagnóstico que cliente não aprova = trabalho desperdiçado na Fase 2"

---

## 📚 SECÇÃO 3: FASE 2 — Execution (Dias 15-28) (12:00 — 18:30)

**[Tela: timeline visual FASE 2 com streams paralelos]**

### Objetivo

Implementar as 5 oportunidades identificadas em paralelo. Isso é onde o "45D funciona onde 6 meses falha".

### Timeline Detalhado (Paralelo, não serial)

```
Semana 3-4: EXECUÇÃO PARALELA

Stream A: KW Research + Briefing
  Segunda:   Investigar top 20 keywords (volume, intent, difficulty)
  Terça:     Redator escreve briefing para content
  Quarta:    Cliente aprova keywords + tone of voice
  Quinta:    Redator escreve 5-10 peças de conteúdo

Stream B: Collections Optimization
  Segunda:   Listar todas collections/categorias
  Terça:     Escrever meta description + description para cada
  Quarta:    Implementar no Shopify
  Quinta:    Monitorar indexação

Stream C: Product Optimization
  Segunda:   Template de produto otimizado (title, description, schema)
  Terça:     Revisar top 50 produtos (volume, conversão)
  Quarta:    Implementar otimizações
  Quinta:    Validar via GSC (estão descobertos?)

Stream D: Technical Push
  Segunda:   Implementar structured data (JSON-LD)
  Terça:     Optimizar core web vitals (imagens, lazy loading)
  Quarta:    Submit sitemap para GSC
  Quinta:    Monitorar crawl status

Weekly Approvals (Quarta-Quinta):
  - Cliente aprova keywords: GO para redação
  - Cliente aprova descriptions: GO para publicação
  - Monitorar: primeiros produtos indexados? Collections descobertas?
```

### Deliverables

- ✅ 5-10 peças de conteúdo otimizado
- ✅ 100% collections com metadescription + description
- ✅ Top 50 produtos re-optimizados
- ✅ Schema JSON-LD implementado
- ✅ Core Web Vitals: Lighthouse score > 80
- ✅ Dashboard semanal: "X novos produtos descobertos, Y pages re-crawled, Z keywords já a rankear"

**Pepita #3:** "Parallelização é o que comprime 4 meses em 2 semanas"

---

## 📚 SECÇÃO 4: FASE 3 — Validation (Dias 29-35) (18:30 — 24:00)

**[Tela: timeline visual FASE 3]**

### Objetivo

Medir antes/depois. Contar a história dos resultados. Planear os próximos 90 dias.

### Timeline Detalhado

```
Semana 5:

Segunda:   Data Consolidation
           - GSC: nova baseline (impressões, cliques, CTR)
           - GA4: novo tráfego comparado a 6 semanas atrás
           - SE Ranking: quais keywords começaram a rankear?
           - Shopify: qual a mudança em tráfego orgânico?

Terça:     Before/After Report
           - Gráfico 1: Impressões (antes vs depois)
           - Gráfico 2: Cliques (antes vs depois)
           - Gráfico 3: Keywords descobertas
           - Gráfico 4: Taxa de crescimento/semana
           → Template: "Before/After Report 45D"

Quarta:    Roadmap 90D
           - "Isto funcionou — aqui estão os próximos passos"
           - Link building strategy (se aplicável)
           - Content expansion (quais keywords prioritárias?)
           - Technical ongoing (Core Web Vitals monitoring)

Quinta:    Apresentação + Decisão de Continuidade
           - Mostrar números
           - Apresentar roadmap 90D
           - Oferecer opções:
             A) Retainer mensal (manutenção + crescimento)
             B) Segunda fase 45D (expansão agressiva)
             C) Consultoria mensal (cliente faz internamente)
           → Approval gate: Cliente aprova roadmap? Quer continuar?
```

### Deliverables

- ✅ Before/After metrics report
- ✅ Keywords que começaram a rankear
- ✅ Tráfego orgânico growth (%)
- ✅ 90D Roadmap (3 meses de prioridades)
- ✅ Continuity options apresentadas
- ✅ Decisão do cliente (retainer, phase 2, consultoria)

**Pepita #4:** "Métricas antes/depois são o que convence cliente a continuar"

---

## 📚 SECÇÃO 5: Os Approval Gates (24:00 — 25:30)

**[Tela: resumo dos 4 gates decisivos]**

> "Isto é crítico. Cada fase tem um momento em que o cliente aprova — ou diz 'não, isto não funciona'."

| Fase | Gate | Questão | Resultado |
|------|------|---------|-----------|
| **FASE 0** | Fim Quinta (Dia 5) | "Faz sentido este plano?" | GO para Fase 1 ou REWORK |
| **FASE 1** | Fim Sexta (Dia 14) | "Estes 5 problemas são os reais?" | GO para Fase 2 ou REDIAGNOSE |
| **FASE 2** | Semanal (Quarta/Quinta) | "Aprovam keywords/descriptions?" | Continua execução ou REWORK |
| **FASE 3** | Fim Quinta (Dia 35) | "Continuam com roadmap 90D?" | Retainer, Phase 2, ou fim |

---

## 🎯 RESUMO

```
FASE 0 (Dias 1-5):    Setup + Briefing     [Gate: Cliente aprova plano]
FASE 1 (Dias 6-14):   Diagnostic          [Gate: Cliente aprova Top 5]
FASE 2 (Dias 15-28):  Execution Paralela  [Gate: Weekly approvals]
FASE 3 (Dias 29-35):  Validation + Roadmap [Gate: Cliente decide continuidade]
```

Cada fase é **sequencial mas comprimida**. Fase 1 não começaa até Fase 0 aprovado. Fase 2 começa enquanto Fase 1 ainda está sendo documentada. Este é o ritmo.

---

## 💡 Próxima Aula

Aula 1.3 — Papéis e Responsabilidades: Quem faz o quê, e quando?

---

**Status:** ✅ Completa  
**Última atualização:** [hoje]  
**Autor:** RankPanda Growth System
