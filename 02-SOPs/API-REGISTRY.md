---
name: api-registry
description: Central registry of all external APIs, credentials, endpoints, and integration patterns used in RankPanda 45D workflow
type: reference
status: active
foco: technical
tags: [api, integrations, credentials, endpoints, automation]
wikilinks: [[[FASE-0-KICKOFF]], [[FASE-2-EXECUTION]], [[FASE-3-VALIDATION]], [[PILOT-VIBRADORES-00-MASTER-PLAN]]]
---

# REFERENCE — API Registry (Central Integration Hub)

**Resumo:** Central registry de todas as APIs externas, credentials, endpoints e padrões de integração. Isto NÃO é documentação de como usar cada API — é um index + quick-start para developers.

---

## 🎯 Propósito deste Registry

Quando desenvolvimento precisa chamar uma API:
- "Como faço call a Shopify Products API?"
- "Qual é o endpoint de SE Ranking?"
- "Como autenticar com GSC?"
- "Preciso de qual credential file?"

→ Este registry aponta ao local correto + quick-start (não full docs).

---

## 🔐 Credenciais & Autenticação (Local Storage)

**IMPORTANTE:** Todos os credentials em `/vault/.env.local` (gitignore'd):
```bash
# Shopify
SHOPIFY_ACCESS_TOKEN=shppa_xxxxx
SHOPIFY_API_VERSION=2024-01
SHOPIFY_STORE_URL=https://mystore.myshopify.com

# Google (OAuth Service Account)
GOOGLE_SERVICE_ACCOUNT_EMAIL=rankpanda@project.iam.gserviceaccount.com
GOOGLE_SERVICE_ACCOUNT_KEY=~/.rankpanda-google-sa-key.json

# SE Ranking
SE_RANKING_API_KEY=serank_xxxxx

# ClickUp
CLICKUP_API_TOKEN=pk_xxxxx

# Leexi
LEEXI_API_KEY=leexi_xxxxx

# Discord (Optional, for webhooks)
DISCORD_WEBHOOK_URL=https://discordapp.com/api/webhooks/xxxxx

# GitHub (for vault commits)
GITHUB_TOKEN=ghp_xxxxx
```

**Loading in Code:**
```python
import os
from dotenv import load_dotenv

load_dotenv('/vault/.env.local')
shopify_token = os.getenv('SHOPIFY_ACCESS_TOKEN')
```

---

## 📋 API Registry (By System)

### 1. **Shopify — Store Management API**

**Endpoint:** GraphQL (primary) + REST (legacy)  
**Auth:** OAuth Access Token  
**Version:** 2024-01 (latest stable)

**Common Operations:**

| Operation | GraphQL Query | Use Case |
|---|---|---|
| **Fetch Collections** | `query { collections(first: 50) { edges { node { id, title, handle } } } }` | Map store structure (SOP-1) |
| **Fetch Products** | `query { products(first: 100, query: "collection:vibrador") { edges { node { id, title, handle, metafields } } } }` | Get products for batch optimization (FASE-2) |
| **Update Collection Metafields** | `mutation { collectionUpdate(input: { id: "gid://shopify/Collection/123", metafields: [...] }) { collection { id } } }` | Apply SEO titles/descriptions (FASE-2) |
| **Bulk Mutation** | `mutation { bulkOperationRunMutation(mutation: "...") { bulkOperation { id, status } } }` | Batch apply 50-100 items (FASE-2) |

**Quick Start:**
```python
import shopify
from shopify import Session

api_version = "2024-01"
shop_url = os.getenv('SHOPIFY_STORE_URL')  # e.g., "mystore.myshopify.com"
access_token = os.getenv('SHOPIFY_ACCESS_TOKEN')

session = Session(shop_url, api_version, access_token)
shopify.ShopifyResource.activate_session(session)

# Fetch collections
collections = shopify.Collection.find()
for collection in collections:
    print(collection.title, collection.handle)
```

**Documentation:** https://shopify.dev/docs/api/admin-graphql  
**Rate Limits:** 2 requests/second (or burst 40/second)  
**Errors to Handle:**
- `UNPROCESSABLE_ENTITY` — Invalid metafield definition
- `THROTTLED` — Rate limit hit, retry with backoff
- `UNAUTHENTICATED` — Token expired/invalid

**Reference in Vault:**
- [[FASE-2-EXECUTION]] → "Bulk apply via Shopify API"
- [[SOP-1-STORE-CONTEXT-SETUP]] → Collection mapping

---

### 2. **Google Search Console (GSC) — Organic Search Data**

**Endpoint:** REST API  
**Auth:** OAuth Service Account (or User OAuth)  
**Docs:** https://developers.google.com/webmaster-tools/search-console-api-original

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Query Insights** | `GET searchanalytics/query` | Extract clicks, impressions, position, queries (FASE-1, FASE-3) |
| **Coverage Report** | `GET urlInspection/index` | Check indexed pages, errors (FASE-1) |
| **Submit URL** | `POST urlTestingTools/mobileFriendlyTest` | Submit collections/products for indexing (FASE-2) |

**Quick Start:**
```python
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

scopes = ['https://www.googleapis.com/auth/webmasters.readonly']
credentials = Credentials.from_service_account_file(
    os.getenv('GOOGLE_SERVICE_ACCOUNT_KEY'),
    scopes=scopes
)

from googleapiclient.discovery import build
service = build('webmasters', 'v3', credentials=credentials)

# Query search data (last 30 days)
request_body = {
    'startDate': '2026-03-21',
    'endDate': '2026-04-21',
    'dimensions': ['query', 'page'],
    'rowLimit': 10000
}
response = service.searchanalytics().query(
    siteUrl='https://mystore.com/',
    body=request_body
).execute()

for row in response['rows']:
    print(f"{row['keys'][0]}: {row['clicks']} clicks")
```

**Rate Limits:** 600 calls/minute  
**Data Latency:** ~2 days behind real-time

**Reference in Vault:**
- [[FASE-1-DIAGNOSTIC]] → GSC analysis workflow
- [[FASE-3-VALIDATION]] → Before/after metrics extraction

---

### 3. **Google Analytics 4 (GA4) — Traffic & Conversion Data**

**Endpoint:** Data API (v1) + Admin API  
**Auth:** OAuth Service Account  
**Docs:** https://developers.google.com/analytics/devguides/reporting/data/v1

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Query Organic Traffic** | `POST properties/{property}/runReport` | Extract sessions, conversions by landing page (FASE-1, FASE-3) |
| **Event Tracking** | `POST properties/{property}/runReport` | Validate purchase events, add-to-cart (FASE-0) |

**Quick Start:**
```python
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import RunReportRequest, Dimension, Metric, DateRange

client = BetaAnalyticsDataClient(credentials=credentials)

request = RunReportRequest(
    property=f"properties/{property_id}",
    date_ranges=[DateRange(start_date="2026-03-21", end_date="2026-04-21")],
    dimensions=[Dimension(name="pagePath")],
    metrics=[Metric(name="organicSessions"), Metric(name="conversions")]
)

response = client.run_report(request)
for row in response.rows:
    print(f"{row.dimension_values[0].value}: {row.metric_values[0].value} sessions")
```

**Rate Limits:** 500 requests/minute  
**Data Latency:** ~24 hours behind

**Reference in Vault:**
- [[FASE-1-DIAGNOSTIC]] → GA4 analysis workflow
- [[FASE-3-VALIDATION]] → Traffic before/after comparison

---

### 4. **SE Ranking — Keyword Research & Tracking**

**Endpoint:** REST API  
**Auth:** API Key  
**Docs:** https://www.seranking.com/api/v3/

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Get Domain Rank** | `GET /domain/{domain}/rank` | Overall domain SEO strength (FASE-1) |
| **Search Keywords** | `GET /keywords/search` | Find keywords by volume, difficulty (SOP-2) |
| **Get SERP Data** | `GET /serps/{keyword}` | Extract top 10 competitors, positions (FASE-1) |

**Quick Start:**
```python
import requests

api_key = os.getenv('SE_RANKING_API_KEY')
base_url = "https://api.seranking.com/v3"

# Search keywords by volume + difficulty
params = {
    'apiKey': api_key,
    'query': 'vibrador',
    'country': 'pt',
    'order': 'volume',
    'limit': 50
}
response = requests.get(f"{base_url}/keywords/search", params=params)
keywords = response.json()['keywords']

for kw in keywords:
    print(f"{kw['keyword']}: {kw['volume']} volume, {kw['difficulty']} difficulty")
```

**Rate Limits:** 100 requests/second  
**Data Freshness:** Keywords updated daily

**Reference in Vault:**
- [[SOP-2-KEYWORD-RESEARCH-V2]] → SE Ranking as primary data source
- [[FASE-1-DIAGNOSTIC]] → Competitive analysis

---

### 5. **ClickUp — Project Management**

**Endpoint:** REST API  
**Auth:** API Token  
**Docs:** https://clickup.com/api

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Create Task** | `POST /team/{team_id}/list/{list_id}/task` | Create task from automation (FASE-2) |
| **Update Task** | `PUT /task/{task_id}` | Update status, assignee, dates (continuous) |
| **Get Team Tasks** | `GET /team/{team_id}/task` | List all sprint tasks, filter by status |

**Quick Start:**
```python
import requests

api_key = os.getenv('CLICKUP_API_TOKEN')
headers = {'Authorization': api_key}

# Create task
task_data = {
    'name': 'Optimize Products Batch 1',
    'list_id': 'list_123',
    'description': 'Apply approved product descriptions via Shopify API',
    'due_date': 1714003200000  # timestamp in ms
}
response = requests.post(
    'https://api.clickup.com/api/v2/task',
    json=task_data,
    headers=headers
)
print(response.json()['task']['id'])
```

**Rate Limits:** 300 requests/minute  
**Webhook Support:** Yes (for real-time updates)

**Reference in Vault:**
- [[FASE-2-EXECUTION]] → Synchronizing work via ClickUp
- [[CONCEITO-Client-Approval]] → Tracking approvals in tasks

---

### 6. **GitHub — Vault Sync**

**Endpoint:** REST API  
**Auth:** Personal Access Token  
**Docs:** https://docs.github.com/en/rest

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Create Commit** | `git commit` (via CLI) | Commit changes to vault (every session) |
| **Push to Remote** | `git push origin main` (via CLI) | Sync vault to GitHub backup |

**Quick Start:**
```bash
cd /Users/rankpanda/Shopify\ RankPanda\ APP\ -\ Oficial\ 2026/vault
git add .
git commit -m "refactor: [description]"
git push origin main
```

**Rate Limits:** Depends on API tier (typically 5000 requests/hour for authenticated)

**Reference in Vault:**
- [[CLAUDE.md]] — "Protocolo de FECHO de Sessão" (vault-sync.sh)

---

### 7. **Leexi — Meeting Transcription** (Optional)

**Endpoint:** REST API  
**Auth:** API Key  
**Docs:** https://docs.leexi.ai/

**Common Operations:**

| Operation | Endpoint | Use Case |
|---|---|---|
| **Get Transcript** | `GET /transcripts/{id}` | Extract key points from client call (post-meeting) |

**Reference in Vault:**
- [[FASE-0-KICKOFF]] → Kickoff call transcription
- [[FASE-3-VALIDATION]] → Final presentation call notes

---

## 🔄 Integration Patterns (Across FASEs)

### Pattern 1 — Data Extraction Pipeline

```
Week 1 (FASE-1):
├─ GSC API: fetch 30-day metrics (impressions, clicks, position)
├─ GA4 API: fetch organic traffic, conversions
├─ SE Ranking API: fetch top competitors keywords
└─ Store in `/vault/01-Clientes/[client]/data/`

Week 3 (FASE-2):
├─ Use SE Ranking to get keywords
├─ Use Shopify API to bulk-update collections/products
└─ Use ClickUp API to track progress

Week 5 (FASE-3):
├─ GSC API: fetch new 30-day metrics (after execution)
├─ Compare vs Week 1 → calculate impact
└─ Report in client presentation
```

### Pattern 2 — Bulk Operations Automation

```
Manual Draft (1-2h):
└─ Generate titles/descriptions (Claude)

Client Approval (48h):
└─ Sampling form (Google Form or Typeform)

Bulk Apply (1-2h):
├─ Build CSV from approved pattern
├─ Call Shopify bulk API
└─ Monitor bulk operation status via API polling

QA Validation (30 min):
└─ Spot-check items on live site
```

---

## 📊 API Call Budget (Per Sprint)

**Typical 45D Sprint:**
- Shopify API: ~500 calls (bulk operations, metafield reads)
- GSC API: ~20 calls (diagnostic + validation queries)
- GA4 API: ~15 calls (traffic analysis + before/after)
- SE Ranking: ~100 calls (keyword research)
- ClickUp: ~200 calls (task creation, updates)
- **Total: ~835 calls** (well within rate limits)

---

## 🛠️ Error Handling Patterns

**Rate Limit Hit:**
```python
import time
from requests.exceptions import HTTPError

def call_with_retry(func, max_retries=3):
    for attempt in range(max_retries):
        try:
            return func()
        except HTTPError as e:
            if e.response.status_code == 429:  # Too Many Requests
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise
    raise Exception(f"Failed after {max_retries} retries")
```

**Authentication Error:**
```python
# Check token expiry before calling API
# Re-authenticate if needed
# Log error for debugging
```

---

## 🔗 Relacionados

**SOPs/FASEs que usam APIs:**
- [[FASE-0-KICKOFF]] → Validar que todas APIs estão funcionando
- [[FASE-1-DIAGNOSTIC]] → GSC + GA4 + SE Ranking data extraction
- [[FASE-2-EXECUTION]] → Shopify + ClickUp automation
- [[FASE-3-VALIDATION]] → GSC + GA4 before/after comparison

**Documentação Complementar:**
- Official API docs (links inclusos acima)
- `/vault/03-Automações/` → Scripts que chamam estas APIs

---

**Versão:** 1.0  
**Data:** 2026-04-21  
**Status:** ACTIVE  
**Próximo:** Adicionar novos APIs conforme projeto escala
