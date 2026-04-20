# API REGISTRY — RankPanda

**Single source of truth para todas as integrações.** Cada API documentada com: quando usar, como chamar, credenciais, exemplo.

---

## 🛍️ SHOPIFY API

**Tipo:** GraphQL REST  
**Credencial:** Access token (por loja)  
**Rate limit:** 2 requests/segundo  

### Quando usar

- **FASE 0:** Verificar acesso + recolher loja info (nome, temas, collections)
- **FASE 1:** Contar products, analisar estrutura de collections
- **FASE 2:** Bulk product updates (titles, descriptions, metafields, tags)
- **FASE 3:** Comparar antes/depois (product count, metafield usage)

### Endpoints principais

#### Get Collections
```graphql
query {
  collections(first: 250) {
    edges { node { id, title, handle, productsCount } }
  }
}
```

**Quando:** FASE 1 (discovery), FASE 2 (optimization)  
**Output:** Lista de collections com count de products

#### Batch Update Products
```graphql
mutation {
  productUpdate(input: { id, title, descriptionHtml, metafields }) {
    product { id, title }
  }
}
```

**Quando:** FASE 2 (bulk optimization)  
**Output:** Confirmação de update

---

## 📊 GOOGLE SEARCH CONSOLE API

**Tipo:** REST  
**Credencial:** OAuth (Rui) ou Service Account  
**Rate limit:** 1000 requests/day  

### Quando usar

- **FASE 1:** Coverage analysis (indexed pages, 404s, crawl errors)
- **FASE 1:** Search performance (impressions, clicks, CTR, position)
- **FASE 3:** Metrics comparison (before/after)

### Endpoints principais

#### Get Search Analytics
```bash
GET https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/searchAnalytics/query
POST body: {
  "startDate": "YYYY-MM-DD",
  "endDate": "YYYY-MM-DD",
  "dimensions": ["query", "page", "device", "country"]
}
```

**Quando:** FASE 1 (baseline), FASE 3 (final metrics)  
**Output:** Impressions, clicks, CTR, position por keyword/page  
**Processing:** Calcular baseline, identificar oportunidades de posição (pages in 11-50 range)

#### Get Index Status
```bash
GET https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/sitemaps
GET https://www.googleapis.com/webmasters/v3/sites/{siteUrl}/sitemap/{sitemapUrl}
```

**Quando:** FASE 1 (tech audit)  
**Output:** Total indexed, submitted vs indexed, pending  
**Alert:** Se indexed < 50% submitted, há problema técnico

---

## 📈 GOOGLE ANALYTICS 4 API

**Tipo:** REST  
**Credencial:** OAuth (Rui) ou Service Account  
**Rate limit:** 10,000 requests/day per project  

### Quando usar

- **FASE 1:** Organic traffic baseline (sessions, users, conversion rate)
- **FASE 1:** Landing page analysis (top pages, bounce rate, conversion)
- **FASE 3:** Metrics comparison (before/after organic)

### Endpoints principais

#### Run Report
```bash
POST https://analyticsreporting.googleapis.com/v4/reports:batchGet
body: {
  "reportRequests": [{
    "viewId": "...",
    "dateRanges": [{ "startDate": "YYYY-MM-DD", "endDate": "YYYY-MM-DD" }],
    "metrics": [{ "expression": "ga:organicSessions" }, { "expression": "ga:goal1Completions" }],
    "dimensions": [{ "name": "ga:landingPagePath" }]
  }]
}
```

**Quando:** FASE 1 (baseline), FASE 3 (final metrics)  
**Output:** Organic sessions, conversions, conversion rate  
**Processing:** Calcular baseline, identificar top landing pages

---

## 🔍 SE RANKING API

**Tipo:** REST  
**Credencial:** API key (Rui)  
**Rate limit:** Depende plano (investigar)  

### Quando usar

- **FASE 0/1:** Keyword research (volume, difficulty, intent)
- **FASE 1:** Competitive landscape (top 5 competitors, keywords they rank for)
- **FASE 2:** Keyword tracking setup (monitorizar posições alvo)
- **FASE 3:** Rank tracking results (posições finais)

### Endpoints principais

#### Keyword Research
```bash
GET /v2/keywords/research
Params: q={query}, region={region}, intent={intent}
```

**Quando:** FASE 1 (discovery)  
**Output:** Keywords com volume, difficulty, intent, serp features  
**Processing:** Filtrar por volume > 100, dificuldade < 50, intent = commercial

#### Rank Tracking
```bash
GET /v2/rank-tracker/domain/{domain}/keywords
```

**Quando:** FASE 2 (setup), FASE 3 (results)  
**Output:** Current position para cada keyword rastreado  
**Alert:** Se nenhuma keyword em top 30, há problema

---

## 📋 CLICKUP API

**Tipo:** REST  
**Credencial:** API token (Rui)  
**Rate limit:** 100 requests/minute  

### Quando usar

- **FASE 0:** Criar task list do sprint (FASE 0 → FASE 3 templates)
- **Contínuo:** Atualizar status de tasks (completadas, bloqueadas)
- **FASE 3:** Gerar relatório de progresso (% tasks completas)

### Endpoints principais

#### Create Task
```bash
POST /v2/list/{list_id}/task
body: {
  "name": "...",
  "description": "...",
  "assignees": [...],
  "due_date": "...",
  "priority": "..."
}
```

**Quando:** Início de cada FASE  
**Output:** Task ID (guardar para referência)

#### Update Task Status
```bash
PUT /v2/task/{task_id}
body: { "status": "completed" }
```

**Quando:** Quando uma task é completada  
**Output:** Confirmação de update

---

## 💬 DISCORD API

**Tipo:** REST + Webhooks  
**Credencial:** Bot token (para API) ou Webhook URL (para notificações)  

### Quando usar

- **FASE 0:** Notificar cliente que sprint começou
- **FASE 1:** Enviar diagnostic briefing
- **FASE 2:** Weekly progress updates
- **FASE 3:** Final presentation + roadmap
- **Contínuo:** Alertas (jobs completos, erros)

### Endpoints principais

#### Send Message (via Webhook)
```bash
POST {webhook_url}
body: {
  "content": "...",
  "embeds": [{ "title": "...", "description": "..." }]
}
```

**Quando:** Notificações rápidas (fase completada, alerta)  
**Output:** Mensagem no channel

#### Send Message (via Bot API)
```bash
POST /v10/channels/{channel_id}/messages
body: { "content": "..." }
```

**Quando:** Mensagens rich (embeds, threads)  
**Output:** Message ID

---

## 📧 GMAIL API

**Tipo:** REST  
**Credencial:** OAuth (Rui)  

### Quando usar

- **FASE 0:** Enviar welcome email ao cliente
- **FASE 3:** Enviar relatório final + roadmap
- **Contínuo:** Notificações e confirmações

### Endpoints principais

#### Send Email
```bash
POST /gmail/v1/users/me/messages/send
body: {
  "raw": "base64-encoded email"
}
```

**Quando:** Comunicações importantes ao cliente  
**Output:** Message ID

---

## 📅 GOOGLE CALENDAR API

**Tipo:** REST  
**Credencial:** OAuth (Rui)  

### Quando usar

- **FASE 0:** Agendar kick-off call
- **FASE 1:** Agendar diagnostic presentation
- **FASE 3:** Agendar final presentation

### Endpoints principais

#### Create Event
```bash
POST /calendar/v3/calendars/primary/events
body: {
  "summary": "...",
  "description": "...",
  "start": { "dateTime": "...", "timeZone": "Europe/Lisbon" },
  "end": { "dateTime": "...", "timeZone": "Europe/Lisbon" },
  "attendees": [{ "email": "..." }]
}
```

**Quando:** Agendar calls importantes  
**Output:** Event ID + calendar link

---

## 📄 GOOGLE DRIVE API

**Tipo:** REST  
**Credencial:** OAuth (Rui)  

### Quando usar

- **FASE 1:** Criar pasta do cliente (organizar docs)
- **FASE 3:** Upload relatório final

### Endpoints principais

#### Create Folder
```bash
POST /drive/v3/files
body: {
  "name": "...",
  "mimeType": "application/vnd.google-apps.folder",
  "parents": ["..."]
}
```

**Quando:** Início do sprint  
**Output:** Folder ID

---

## 🎙️ LEEXI API

**Tipo:** REST  
**Credencial:** API token (Rui)  

### Quando usar

- **Contínuo:** Extrair transcripts de reuniões
- **Contínuo:** Analisar discussões (feedback do cliente)

### Endpoints principais

#### Get Call Transcripts
```bash
GET /v1/calls/{call_id}/transcripts
```

**Quando:** Pós-reunião  
**Output:** Transcript completo + metadata

---

## 📌 CHECKLISTS por FASE

### FASE 0 — Kickoff
```
✓ Shopify: Get collections + product count
✓ GSC: Baseline (impressions, clicks, coverage)
✓ GA4: Baseline (organic sessions, conversions)
✓ SE Ranking: Setup tracking
✓ ClickUp: Create task list
✓ Discord: Notify client
✓ Google Calendar: Confirm dates
```

### FASE 1 — Diagnostic
```
✓ Shopify: Analyze collection structure
✓ GSC: Coverage analysis + search performance
✓ GA4: Landing page analysis + funnel
✓ SE Ranking: Keyword research + competitor analysis
✓ ClickUp: Update findings
✓ Discord: Send diagnostic brief
```

### FASE 2 — Execution
```
✓ Shopify: Bulk product updates (titles, descriptions, metafields)
✓ ClickUp: Track completion
✓ Discord: Weekly progress
✓ SE Ranking: Monitor keyword tracking
```

### FASE 3 — Validation
```
✓ GSC: Final metrics (position changes, new keywords)
✓ GA4: Final organic traffic + conversions
✓ SE Ranking: Rank tracking results
✓ ClickUp: Mark complete
✓ Gmail: Send final report
✓ Discord: Send final presentation
✓ Google Calendar: Schedule follow-up
```

---

**Versão:** 1.0  
**Data:** 2026-04-20  
**Status:** VIVO — atualizar com cada novo cliente/fase
