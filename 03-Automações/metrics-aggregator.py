#!/usr/bin/env python3
"""
Metrics Aggregator — Colecta diária de métricas de todas as fontes

Fluxo:
1. Lê memory/projects/[todos clientes].md
2. Para cada cliente:
   - Chama gsc-api.py → ultimos 7 dias impressões, clicks, posição
   - Chama ga4-api.py → ultimos 7 dias sessões, conversões, AOV
   - Chama shopify-api.py → stats actuais (produtos, colecções, pedidos)
   - Chama se-ranking-api.py → keywords, posições
3. Agrega num JSON daily snapshot
4. Append ao memory/projects/[cliente].md tabela "Métricas Diárias"
5. Update MEMORY.md índice com "Last run: {timestamp}"

Executado diariamente via scheduled task @ 08:00 PT

Requer: Credenciais de API guardadas em GitHub rankpandaseo/rankpanda-vault
"""

import os
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
import glob

# TODO: Import API clients (quando credenciais estiverem disponíveis)
# from api.gsc_api import GSCClient
# from api.ga4_api import GA4Client
# from api.shopify_api import ShopifyClient
# from api.se_ranking_api import SERankingClient


def get_all_clients() -> list:
    """Find all memory/projects/[cliente].md files"""

    memory_dir = Path("/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/00-Memory/projects")
    files = glob.glob(str(memory_dir / "*.md"))

    clients = [Path(f).stem for f in files if Path(f).stem != "__pycache__"]
    return clients


def collect_metrics_for_client(cliente_name: str) -> dict:
    """Collect all metrics for one client from all sources"""

    metrics = {
        'cliente': cliente_name,
        'timestamp': datetime.now().isoformat(),
        'gsc': {},
        'ga4': {},
        'shopify': {},
        'se_ranking': {},
    }

    # TODO: Implement actual API calls
    #
    # Example structure:
    # gsc = GSCClient(property_id=cliente_data['gsc_property'])
    # metrics['gsc'] = {
    #     'impressions_7d': gsc.get_impressions_7d(),
    #     'clicks_7d': gsc.get_clicks_7d(),
    #     'avg_position': gsc.get_avg_position(),
    # }
    #
    # ga4 = GA4Client(measurement_id=cliente_data['ga4_measurement_id'])
    # metrics['ga4'] = {
    #     'organic_sessions_7d': ga4.get_organic_sessions_7d(),
    #     'organic_conversions_7d': ga4.get_organic_conversions_7d(),
    #     'aov': ga4.get_aov(),
    # }
    #
    # shopify = ShopifyClient(store_url=cliente_data['shopify_store'])
    # metrics['shopify'] = shopify.get_current_stats()
    #
    # se_ranking = SERankingClient(project_id=cliente_data['se_ranking_project'])
    # metrics['se_ranking'] = se_ranking.get_rankings()

    # Placeholder (returns empty for now)
    return metrics


def update_client_memory(cliente_name: str, metrics: dict) -> bool:
    """Update memory/projects/[cliente].md com novos metrics"""

    project_file = f"/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/00-Memory/projects/{cliente_name}.md"

    if not os.path.exists(project_file):
        print(f"⚠️  Project file not found: {project_file}")
        return False

    # TODO: Append row à tabela "Métricas Diárias" com data + metrics
    # Read file, find table, append new row, write back

    print(f"✅ Updated {cliente_name} metrics")
    return True


def log_aggregation(start_time: datetime, clients_processed: int, errors: int):
    """Log aggregation run to metrics-aggregator.log"""

    log_file = "/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/03-Automações/metrics-aggregator.log"

    elapsed = (datetime.now() - start_time).total_seconds()
    status = "✅" if errors == 0 else "⚠️"

    log_entry = f"{datetime.now().isoformat()} | {status} Processed {clients_processed} clients in {elapsed:.1f}s | Errors: {errors}\n"

    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(log_entry)


def main():
    """Main aggregation loop"""

    start_time = datetime.now()
    print(f"🚀 Starting metrics aggregation @ {start_time.isoformat()}")

    try:
        clients = get_all_clients()
        print(f"📊 Found {len(clients)} clients")

        if not clients:
            print("⚠️  No clients found in memory/projects/")
            return

        errors = 0
        for cliente in clients:
            try:
                print(f"  Collecting metrics for {cliente}...")
                metrics = collect_metrics_for_client(cliente)
                update_client_memory(cliente, metrics)
            except Exception as e:
                print(f"  ❌ Error for {cliente}: {e}")
                errors += 1

        print(f"\n✅ Aggregation complete: {len(clients) - errors}/{len(clients)} clients processed")

        log_aggregation(start_time, len(clients), errors)

    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
