#!/bin/bash

# Refactor Curso 45D files to COURSE-* pattern

cd "/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault"

echo "🔄 Refactoring Curso 45D files..."

# Main course files
git mv 05-Curso-45D/00-STRUCTURE.md 05-Curso-45D/COURSE-00-STRUCTURE.md
git mv 05-Curso-45D/COURSE_STATUS.md 05-Curso-45D/COURSE-STATUS.md
git mv 05-Curso-45D/pepitas-de-ouro.md 05-Curso-45D/COURSE-PEPITAS-DE-OURO.md

# M01 - Fundamentos
git mv "05-Curso-45D/M01-Fundamentos/1.1-O-que-e-45D-Sprint.md" "05-Curso-45D/M01-Fundamentos/COURSE-M01-1.1-O-Que-E-45D-Sprint.md"
git mv "05-Curso-45D/M01-Fundamentos/1.2-As-4-fases-em-detalhe.md" "05-Curso-45D/M01-Fundamentos/COURSE-M01-1.2-As-4-Fases-Em-Detalhe.md"
git mv "05-Curso-45D/M01-Fundamentos/1.3-Papeis-e-responsabilidades.md" "05-Curso-45D/M01-Fundamentos/COURSE-M01-1.3-Papeis-E-Responsabilidades.md"
git mv "05-Curso-45D/M01-Fundamentos/1.4-Por-que-vence-agencias-tradicionais.md" "05-Curso-45D/M01-Fundamentos/COURSE-M01-1.4-Por-Que-Vence-Agencias-Tradicionais.md"
git mv "05-Curso-45D/M01-Fundamentos/README.md" "05-Curso-45D/M01-Fundamentos/REFERENCE-M01-README.md"

# M02 - Memoria e Contexto
git mv "05-Curso-45D/M02-Memoria-e-Contexto/README.md" "05-Curso-45D/M02-Memoria-e-Contexto/REFERENCE-M02-README.md"

# M03 - Integrações
git mv "05-Curso-45D/M03-Integrações/README.md" "05-Curso-45D/M03-Integrações/REFERENCE-M03-README.md"

# M04 - Gestao de Equipa
git mv "05-Curso-45D/M04-Gestao-de-Equipa/README.md" "05-Curso-45D/M04-Gestao-de-Equipa/REFERENCE-M04-README.md"

# M05 - Automacoes e Agents
git mv "05-Curso-45D/M05-Automacoes-e-Agents/README.md" "05-Curso-45D/M05-Automacoes-e-Agents/REFERENCE-M05-README.md"

# M06 - Vault e Sync
git mv "05-Curso-45D/M06-Vault-e-Sync/README.md" "05-Curso-45D/M06-Vault-e-Sync/REFERENCE-M06-README.md"

# M07 - Reporting e Dashboards
git mv "05-Curso-45D/M07-Reporting-e-Dashboards/README.md" "05-Curso-45D/M07-Reporting-e-Dashboards/REFERENCE-M07-README.md"

# M08 - Qualidade e Anti-Padroes
git mv "05-Curso-45D/M08-Qualidade-e-Anti-Padroes/README.md" "05-Curso-45D/M08-Qualidade-e-Anti-Padroes/REFERENCE-M08-README.md"

# M09 - Scaling e Sistemas
git mv "05-Curso-45D/M09-Scaling-e-Sistemas/README.md" "05-Curso-45D/M09-Scaling-e-Sistemas/REFERENCE-M09-README.md"

# M10 - Bonus Infraestrutura
git mv "05-Curso-45D/M10-Bonus-Infraestrutura/README.md" "05-Curso-45D/M10-Bonus-Infraestrutura/REFERENCE-M10-README.md"

# Session data
git mv "00-Memory/sessions/2026-04-18.md" "00-Memory/sessions/REFERENCE-SESSION-2026-04-18.md"

echo "✅ Curso 45D + Session data refacturado (25 ficheiros)"
