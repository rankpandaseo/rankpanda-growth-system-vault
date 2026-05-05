---
name: Prisma Client Path Mismatch — Root Cause & Fix
description: Critical lesson from Phase 1 deployment blocker - custom output paths cause runtime initialization errors
type: pepita
date: 2026-05-04
severity: critical
---

# Pepita #47: Prisma Custom Output Path Mismatch

**Contexto:** Redeploying Phase 1 microservices on VPS 76.13.58.79. All 4 services (keywords, nlp, clustering, datacollection) started but crashed immediately with `@prisma/client did not initialize yet`.

**Problema Identificado:**
```prisma
# ❌ WRONG — Schema generates to custom location
generator client {
  provider = "prisma-client-js"
  output = "../node_modules/.prisma/client-keywords"
}
```

```typescript
// ❌ But code imports from default location
import { PrismaClient } from '@prisma/client'
```

**Mismatch:** Prisma *generated* to `.prisma/client-keywords/index.js` but code looked for default `@prisma/client/default.js`. Caused runtime error even though Prisma generate succeeded during Docker build.

---

## ✅ Solução

**Remove custom output entirely** — use Prisma defaults:

```prisma
generator client {
  provider = "prisma-client-js"
  # NO output line — defaults to ./node_modules/@prisma/client
}
```

**Aplicar em:** Todos os 4 schema.prisma:
- services/keywords-service/prisma/schema.prisma
- services/nlp-service/prisma/schema.prisma
- services/clustering-service/prisma/schema.prisma
- services/datacollection-service/prisma/schema.prisma

**Rebuild:** Docker `--no-cache` obrigatório (força regenoração Prisma):
```bash
docker compose up -d --build
```

---

## 🔑 Por Que Isto Importa

1. **Silent failure:** Dockerfile build succeeds (`prisma generate` completes), container starts, but crashes on first line that needs DB access
2. **Path independence:** Custom output paths são úteis em monorepos mas não em microservices com separate import paths
3. **Multi-tenant safety:** Cada serviço tem seu próprio `.prisma/client` no seu `/app/node_modules` — não há conflito mesmo com imports idênticos

---

## 📖 Como Aplicar em Futuro

1. **Regra:** Prisma schemas em microservices = sempre use defaults, nunca custom output
2. **Verificação:** `grep -r 'output =' services/*/prisma/` — se encontrar matches, é red flag
3. **Test:** Depois do build, rodar `npm ls @prisma/client` — deve apontar para `./node_modules/@prisma/client`, não `.prisma/client-*`
4. **Diagnóstico:** Se tiver "did not initialize", check logs para path mismatch:
   ```bash
   docker logs container_name 2>&1 | grep -i prisma | head -5
   ```

---

## 🛡️ Prevenção

- Adicionar a CI/CD check: validar que schema.prisma não tem `output` lines
- Template schema.prisma: nunca incluir custom output por default
- Monorepo warning: se aplicar Prisma em monorepo, documentar que custom paths são necessários e por quê

---

**Status:** RESOLVED — All 4 services running 2026-05-04 18:02 PT  
**Tempo até fix:** ~2.5h (SSH auth issue + rebuild)  
**Learning:** Schema validation deve ser parte do build pipeline
