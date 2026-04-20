#!/usr/bin/env python3
"""
Onboarding Scaffold — Processa kickoff-briefing-form.md automaticamente

Fluxo:
1. Cliente preenche /vault/01-Clientes/[cliente]/kickoff-briefing-form.md
2. Script lê form, extrai dados estruturados
3. Cria memory/projects/[cliente].md com IDs de ferramentas + baseline
4. Popula memory/context/people.md com squad member novo
5. Gera memory/pending.md com FASE 0 tasks
6. Cria memory/sessions/estado-atual.md com current state
7. Retorna: "✅ [Cliente] pronto para FASE 0"

Requer: Shopify API, GSC API, GA4 API, SE Ranking API credentials em GitHub vault
"""

import os
import re
import json
import sys
from datetime import datetime
from pathlib import Path

# Stub: In production, import API clients from ../api-clients/
# from api.shopify_api import ShopifyClient
# from api.gsc_api import GSCClient
# from api.ga4_api import GA4Client
# from api.se_ranking_api import SERankingClient


def parse_kickoff_form(form_path: str) -> dict:
    """Parse kickoff-briefing-form.md e extrai dados estruturados"""

    if not os.path.exists(form_path):
        raise FileNotFoundError(f"Form not found: {form_path}")

    with open(form_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract fields using regex (forma simplificada)
    # Expected format: "**Field Name:** value"

    data = {
        'cliente': extract_field(content, r'\*\*Cliente:\*\*\s*(.+)'),
        'aov': extract_field(content, r'\*\*AOV estimado:\*\*\s*(.+)'),
        'volume_mensal': extract_field(content, r'\*\*Volume mensal:\*\*\s*(.+)'),
        'sazonalidade': extract_field(content, r'\*\*Sazonalidade:\*\*\s*(.+)'),
        'shopify_store': extract_field(content, r'\*\*Shopify Store:\*\*\s*(.+)'),
        'gsc_property': extract_field(content, r'\*\*GSC Property ID:\*\*\s*(.+)'),
        'ga4_measurement_id': extract_field(content, r'\*\*GA4 Measurement ID:\*\*\s*(.+)'),
        'se_ranking_project': extract_field(content, r'\*\*SE Ranking Project ID:\*\*\s*(.+)'),
        'discord_channel': extract_field(content, r'\*\*Discord Channel:\*\*\s*(.+)'),
        'clickup_list_id': extract_field(content, r'\*\*ClickUp List ID:\*\*\s*(.+)'),
        'contact_email': extract_field(content, r'\*\*Contact Email:\*\*\s*(.+)'),
        'contact_name': extract_field(content, r'\*\*Contact Name:\*\*\s*(.+)'),
        'competitors': extract_field(content, r'\*\*Competitors:\*\*\s*(.+)'),
    }

    return data


def extract_field(content: str, pattern: str) -> str:
    """Extract field value from content using regex"""
    match = re.search(pattern, content, re.IGNORECASE)
    return match.group(1).strip() if match else ""


def fetch_baseline_metrics(cliente_data: dict) -> dict:
    """Fetch baseline metrics from GSC, GA4, SE Ranking, Shopify APIs"""

    baseline = {
        'gsc': {
            'indexed_pages': 0,
            'impressions_30d': 0,
            'clicks_30d': 0,
            'avg_position': 0.0,
        },
        'ga4': {
            'organic_sessions_30d': 0,
            'organic_conversions_30d': 0,
            'aov': 0.0,
            'bounce_rate': 0.0,
        },
        'shopify': {
            'total_products': 0,
            'total_collections': 0,
            'total_orders': 0,
            'avg_order_value': 0.0,
        },
        'se_ranking': {
            'keywords_tracked': 0,
            'avg_position': 0.0,
            'top_10_keywords': [],
        },
        'captured_at': datetime.now().isoformat(),
    }

    # TODO: Implement actual API calls once clients are ready
    # This is placeholder; replace with real API integrations

    # Example (commented out):
    # gsc = GSCClient(property_id=cliente_data['gsc_property'])
    # baseline['gsc'] = gsc.get_metrics_30d()
    #
    # ga4 = GA4Client(measurement_id=cliente_data['ga4_measurement_id'])
    # baseline['ga4'] = ga4.get_metrics_30d()
    #
    # shopify = ShopifyClient(store_url=cliente_data['shopify_store'])
    # baseline['shopify'] = shopify.get_inventory_stats()

    return baseline


def create_project_memory(cliente_name: str, cliente_data: dict, baseline: dict) -> str:
    """Create memory/projects/[cliente].md file"""

    template = f"""# {cliente_name} — Sprint 001

**Data Início:** {datetime.now().strftime('%Y-%m-%d')}
**Cliente:** {cliente_name}
**Contact:** {cliente_data['contact_name']} ({cliente_data['contact_email']})

---

## 🔗 IDs de Ferramentas

- **Shopify Store:** {cliente_data['shopify_store']}
- **GSC Property ID:** {cliente_data['gsc_property']}
- **GA4 Measurement ID:** {cliente_data['ga4_measurement_id']}
- **SE Ranking Project ID:** {cliente_data['se_ranking_project']}
- **ClickUp List ID:** {cliente_data['clickup_list_id']}
- **Discord Channel:** {cliente_data['discord_channel']}

---

## 📊 Baseline Metrics (Capturado {baseline['captured_at']})

### GSC
- Indexed Pages: {baseline['gsc']['indexed_pages']}
- Impressions (30D): {baseline['gsc']['impressions_30d']}
- Clicks (30D): {baseline['gsc']['clicks_30d']}
- Avg Position: {baseline['gsc']['avg_position']:.1f}

### GA4
- Organic Sessions (30D): {baseline['ga4']['organic_sessions_30d']}
- Organic Conversions (30D): {baseline['ga4']['organic_conversions_30d']}
- AOV: €{baseline['ga4']['aov']:.2f}
- Bounce Rate: {baseline['ga4']['bounce_rate']:.1f}%

### Shopify
- Total Products: {baseline['shopify']['total_products']}
- Total Collections: {baseline['shopify']['total_collections']}
- Total Orders (All Time): {baseline['shopify']['total_orders']}
- Avg Order Value: €{baseline['shopify']['avg_order_value']:.2f}

### SE Ranking
- Keywords Tracked: {baseline['se_ranking']['keywords_tracked']}
- Avg Position: {baseline['se_ranking']['avg_position']:.1f}
- Top 10: {', '.join(baseline['se_ranking']['top_10_keywords'][:10])}

---

## 📈 Métricas Diárias (Últimos 7 Dias)

_Preenchidas automaticamente diariamente via API_

| Data | Impressões | Clicks | Posição | Sessões | Conversões | Receita |
|------|-----------|--------|---------|---------|-----------|---------|
| TBD  | -         | -      | -       | -       | -         | -       |

---

## 🎯 Estado Actual da FASE

**FASE 0 — Kickoff (3-5 dias)**

| Task | Status | Due | Owner |
|------|--------|-----|-------|
| Briefing + Business Validation | ⏳ Pending | D1 | Rui |
| Setup Técnico — Shopify | ⏳ Pending | D2 | Claude |
| Setup Técnico — GSC + GA4 | ⏳ Pending | D2 | Claude |
| Setup Técnico — SE Ranking | ⏳ Pending | D3 | Claude |
| Baseline Metrics Collected | ⏳ Pending | D4 | Claude |
| Approval Gate — Go/No-go | ⏳ Pending | D5 | Rui |

---

## 📚 Histórico de FASES

- FASE 0: ⏳ In Progress
- FASE 1: ⏳ Pending
- FASE 2: ⏳ Pending
- FASE 3: ⏳ Pending

---

## 📝 Notas

_Preenche-se ao longo do sprint_

---

**Versão:** 1.0
**Criado:** {datetime.now().isoformat()}
**Próxima atualização:** Automática (daily metrics via API)
"""

    return template


def create_pending_tasks(cliente_name: str, cliente_data: dict) -> str:
    """Create memory/pending.md com FASE 0 tasks"""

    template = f"""# Pending Tasks — {cliente_name}

## FASE 0 — Kickoff (Dias 1-5)

### D1: Briefing + Business Validation
- [ ] AOV estimado: {cliente_data['aov']}
- [ ] Volume mensal: {cliente_data['volume_mensal']}
- [ ] Sazonalidade: {cliente_data['sazonalidade']}
- [ ] Top 5 Competitors: {cliente_data['competitors']}
- **Owner:** Rui
- **Due:** D1

### D2: Setup Técnico (Shopify, GSC, GA4)
- [ ] Shopify Admin access validado
- [ ] GSC linked à property {cliente_data['gsc_property']}
- [ ] GA4 events (purchase, add_to_cart) active
- **Owner:** Claude
- **Due:** D2

### D3: Setup Técnico (SE Ranking)
- [ ] SE Ranking API integrated
- [ ] Project {cliente_data['se_ranking_project']} active
- [ ] Initial rankings captured
- **Owner:** Claude
- **Due:** D3

### D4: Baseline Metrics Collected
- [ ] GSC baseline snapshot
- [ ] GA4 baseline snapshot
- [ ] Shopify inventory snapshot
- [ ] SE Ranking positions
- **Owner:** Claude
- **Due:** D4

### D5: Approval Gate (Go/No-go FASE 1)
- [ ] All technical setup validated
- [ ] Baseline metrics documented
- [ ] Client approval obtained
- **Owner:** Rui
- **Due:** D5

---

**Criado:** {datetime.now().isoformat()}
"""

    return template


def main():
    """Main orchestration: Process form → Create memory files → Return status"""

    if len(sys.argv) < 2:
        print("Usage: python onboarding-scaffold.py <path-to-kickoff-form>")
        sys.exit(1)

    form_path = sys.argv[1]

    try:
        # 1. Parse form
        print(f"📋 Parsing form: {form_path}")
        cliente_data = parse_kickoff_form(form_path)
        cliente_name = cliente_data.get('cliente', 'unknown')

        if not cliente_name or cliente_name == '':
            raise ValueError("Cliente name not found in form")

        # 2. Fetch baseline metrics
        print(f"📊 Fetching baseline metrics for {cliente_name}...")
        baseline = fetch_baseline_metrics(cliente_data)

        # 3. Create project memory file
        print(f"💾 Creating memory/projects/{cliente_name}.md...")
        project_content = create_project_memory(cliente_name, cliente_data, baseline)
        project_path = f"/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/00-Memory/projects/{cliente_name}.md"

        os.makedirs(os.path.dirname(project_path), exist_ok=True)
        with open(project_path, 'w', encoding='utf-8') as f:
            f.write(project_content)

        # 4. Create pending tasks
        print(f"✅ Creating memory/pending.md...")
        pending_content = create_pending_tasks(cliente_name, cliente_data)
        pending_path = f"/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/00-Memory/pending.md"

        with open(pending_path, 'w', encoding='utf-8') as f:
            f.write(pending_content)

        # 5. Summary
        print(f"\n✅ {cliente_name} pronto para FASE 0!")
        print(f"\n📁 Ficheiros criados:")
        print(f"  - {project_path}")
        print(f"  - {pending_path}")
        print(f"\n🎯 Próximo passo: Rui aprova FASE 0 baseline (memory/projects/{cliente_name}.md)")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
