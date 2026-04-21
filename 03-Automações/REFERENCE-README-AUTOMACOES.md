---
name: reference-readme-automacoes
description: 03-Automações — RankPanda Automation Framework Orquestra diária de
colecção de métricas, processamento de onboarding, e atualização de memory
system. --- ## 🏗️ Architecture ```
type: reference
status: active
foco: operational
tags: [reference, index]
wikilinks: []
---

# 03-Automações — RankPanda Automation Framework Orquestra diária de colecção de métricas, processamento de onboarding, e atualização de memory system. --- ## 🏗️ Architecture ```

**Resumo:** 03-Automações — RankPanda Automation Framework Orquestra diária de
colecção de métricas, processamento de onboarding, e atualização de memory
system. --- ## 🏗️ Architecture ```

---

## 🎯 Por Que Isto Importa

[Adiciona contexto: impacto direto no projeto, porquê isto importa]
- Ponto 1
- Ponto 2
- Ponto 3

---

## ⚡ Quick Checklist

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

---

## 📖 Conteúdo Principal

Cliente preenche form ↓
onboarding-scaffold.py ← Processa automaticamente ↓
memory/projects/[cliente].md criado (com baseline) ↓
FASE 0 approval gate (Rui valida) ↓
Scheduled task: metrics-aggregator.py executado @ 08:00 PT diariamente ↓
metrics-aggregator chama: ├─ api_clients.GSCClient → impressões, clicks, posição
(últimos 7D) ├─ api_clients.GA4Client → sessões, conversões, AOV (últimos 7D) ├─
api_clients.ShopifyClient → produtos, pedidos, receita (actuais) └─
api_clients.SERankingClient → rankings, distribuição (actuais) ↓
memory/projects/[cliente].md actualizado (tabela "Métricas Diárias") ↓
MEMORY.md índice atualizado com "Last run: {timestamp}"
``` --- ## 📋 Scripts Disponíveis ### 1. `onboarding-scaffold.py` **Objetivo:** Processar kickoff-briefing-form.md automaticamente quando cliente preenche **Input:**
```
/vault/01-Clientes/[cliente]/kickoff-briefing-form.md
``` **Output:**
```bash
python onboarding-scaffold.py
/vault/01-Clientes/pilot-vibradores/kickoff-briefing-form.md
``` **Automação:**
```bash
python metrics-aggregator.py
``` **Automação:**
```python
from api_clients import GSCClient, GA4Client, ShopifyClient, SERankingClient gsc
= GSCClient(property_id="12345", credentials_path="/vault/credentials/gsc.json")
metrics = gsc.get_metrics_30d()
``` --- ## 🔑 Credential Management Todas credenciais armazenadas em **GitHub rankpandaseo/rankpanda-vault** (nunca hardcoded): ```
rankpanda-vault/
├── credentials/
│ ├── gsc.json ← {"property_id": "...", "api_key": "..."}
│ ├── ga4.json ← {"measurement_id": "...", "api_key": "..."}
│ ├── shopify.json ← {"stores": {"client1": {"access_token": "..."}}}
│ └── se-ranking.json ← {"project_id": "...", "api_key": "..."}
└── (SOPs, templates, course, etc.)
``` **Loading:**
1. Script detecta credenciais faltantes → retorna erro "Credentials not found"
2. Rui clona vault: `git clone git@github.com:rankpandaseo/rankpanda-vault.git
~/.rankpanda/vault`
3. Scripts carregam de `~/.rankpanda/vault/credentials/[service].json` --- ## ⚙️ Implementation Status | Script | Status | Next Steps |
|--------|--------|-----------|
| `onboarding-scaffold.py` | ✅ Complete | Aguarda credenciais de integração ClickUp para auto-create tasks |
| `metrics-aggregator.py` | ✅ Skeleton | Implementar loop de clientes + error handling |
| `api_clients.py` | ✅ Skeleton | Implementar OAuth2/API calls para GSC, GA4, Shopify, SE Ranking |
| **Scheduled Task Setup** | ⏳ TODO | Criar via CLAUDE.md PERIÓDICO ou scheduled-tasks MCP |
| **Webhook for Onboarding** | ⏳ TODO | Form submission trigger (Discord bot, GitHub Actions, ou manual) | --- ## 🎯 Next Steps ### Phase 1: Implement API Clients (ASAP)
```python
``` ### Phase 2: Load Credentials from GitHub Vault
```python
``` ### Phase 3: Hook Metrics to CLAUDE.md
```markdown
``` ### Phase 4: Onboarding Trigger
```python
``` --- ## 📊 Expected Daily Metrics Flow ```
08:00 PT: 1. metrics-aggregator.py starts 2. Lê memory/projects/*.md → encontra 5 clientes 3. Para cada cliente: - GSC: Puxa últimos 7D impressões, clicks, posição - GA4: Puxa últimos 7D sessões, conversões, AOV - Shopify: Puxa stats actuais (produtos, pedidos) - SE Ranking: Puxa positions, distribuição top 10/30/50/100 4. Append nova row à tabela "Métricas Diárias" em cada memory file 5. Log: "✅ 2026-04-18 08:15 | Processed 5 clients in 12.3s | Errors: 0" Claude next session (08:15): 1. Lê memory/projects/[cliente].md via INÍCIO protocol 2. Vê "Last updated: 08:15" 3. Analisa trends nas métricas 4. Propõe optimizações baseadas em data
``` --- **Versão:** 1.0 **Criado:** 2026-04-18 **Owner:** Claude (Operações) **Próximo Review:** Após credenciais GitHub vault estarem disponíveis

---

## 🔗 Relacionados

- [[Related-Doc-1]] — descrição
- [[Related-Doc-2]] — descrição

---
