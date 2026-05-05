---
name: claude-cli-integration
description: Como o Claude CLI está integrado na Shopify App — spawn, OAuth, multi-tenant
type: reference
status: active
foco: technical
tags: [claude, cli, oauth, shopify-app, spawn, docker]
wikilinks: []
---

# Claude CLI — Integração na Shopify App

**Resumo:** O Claude está integrado via CLI (`spawn`), não via API key. A autenticação é OAuth, feita uma vez no servidor. Zero configuração por loja.

---

## 🎯 Por Que Isto Importa

Usar o Claude CLI em vez da API directa tem implicações operacionais críticas:
- **Sem API keys por cliente** — zero fricção de onboarding
- **Custo de operação controlado** — uma subscrição RankPanda cobre todos os clientes
- **OAuth é mais seguro** — sem chaves em `.env`, sem rotação manual
- **Multi-tenant out-of-the-box** — cada `spawn` é um processo isolado

---

## ⚡ Quick Checklist — Setup Novo Servidor

- [ ] Instalar Claude CLI no container: `npm install -g @anthropic-ai/claude-code`
- [ ] Correr `claude login` no Mac (ou qualquer máquina com browser)
- [ ] Copiar credenciais para o servidor: `scp ~/.claude/.credentials.json root@IP:~/.claude/`
- [ ] Confirmar volume mount no `docker-compose.yml`: `~/.claude:/root/.claude`
- [ ] Verificar dentro do container: `docker exec rankpanda_app claude --version`
- [ ] Testar chamada real: `echo "OK" | docker exec -i rankpanda_app claude --print --model claude-haiku-4-5 --output-format json --no-session-persistence`

---

## 📖 Arquitectura

### Ficheiros Relevantes

```
app/
├── services/
│   ├── claude.server.ts          ← callClaude() + isClaudeAvailable()
│   └── businessContext.server.ts ← generateProductTermsFromContext()
└── routes/
    └── app.settings.tsx          ← UI: status do CLI + Contexto do Negócio
```

### Fluxo de uma chamada

```
Utilizador clica "Gerar Termos Produto"
  → action() no app.settings.tsx
  → generateProductTermsFromContext(shop, context)
  → callClaude(prompt, { model: "claude-haiku-4-5" })
  → spawn("claude", ["--print", "--model", ..., "--no-session-persistence"])
  → stdin.write(prompt) → stdin.end()
  → stdout recebe JSON: { result, is_error, cost_usd }
  → parse → devolver string[]
  → applyGeneratedTerms(shop, terms) → guarda na DB
```

### Padrão spawn (claude.server.ts)

```typescript
const proc = spawn("claude", [
  "--print",
  "--model", model,
  "--output-format", "json",
  "--no-session-persistence",  // ← CRÍTICO: sem estado entre chamadas
], { stdio: ["pipe", "pipe", "pipe"] });

proc.stdin.write(prompt);
proc.stdin.end();

// Resposta JSON: { result: "...", is_error: false, cost_usd: 0.009 }
```

---

## 🐳 Docker — Configuração

### Dockerfile.dev

```dockerfile
# Instalar Claude CLI (Node 20 é suficiente)
RUN npm install -g @anthropic-ai/claude-code
```

### docker-compose.yml

```yaml
app:
  volumes:
    # Credenciais OAuth do host → container
    # Corre `claude login` no host UMA vez; container herda
    - ~/.claude:/root/.claude
```

### Como as credenciais chegam ao servidor

```bash
# 1. Autenticar no Mac (com browser)
claude login

# 2. Copiar para o servidor
scp ~/.claude/.credentials.json root@76.13.58.79:~/.claude/.credentials.json

# 3. Container apanha automaticamente (volume mount, sem restart)
```

---

## 👥 Modelo Multi-Tenant

### Uma subscrição, N clientes

```
VPS RankPanda
├── rankpanda_app (Docker)
│   ├── claude CLI (instalado)
│   └── ~/.claude/.credentials.json (OAuth RankPanda)
│
├── Loja A → spawn("claude") ──┐
├── Loja B → spawn("claude") ──┼──► Claude API (conta RankPanda)
└── Loja C → spawn("claude") ──┘
```

**Sem conflitos** porque:
- Cada `spawn` é um processo OS independente
- `--no-session-persistence` = zero estado partilhado entre chamadas
- Concorrência limitada naturalmente (geração de termos é evento raro, não por page load)

**Custo** = operacional da RankPanda, como o VPS. Não faturado por cliente.

---

## 🔑 Renovação de Credenciais OAuth

O token pode expirar. Sintoma: Settings mostra "✓ Disponível" mas "Gerar Termos" dá erro.

**Fix:**
```bash
# No Mac
claude login  # re-autentica

# Copia token renovado para o servidor
scp ~/.claude/.credentials.json root@76.13.58.79:~/.claude/.credentials.json
# Sem restart necessário — é um volume mount
```

**Frequência:** tokens OAuth do Claude tendem a durar meses. Monitorizar apenas se reportado.

---

## 🔮 Alternativa Futura — Per-Cliente

Se um dia um cliente quiser usar a **própria conta Claude** (ex: enterprise):

1. Adicionar campo `claudeApiKey` na Settings UI
2. `claude.server.ts`: se a loja tem API key → usa SDK Anthropic; se não → usa CLI servidor
3. Barreira: cliente precisa de conta Anthropic (atrito maior no onboarding)

**Recomendação actual:** manter modelo servidor. Só mudar se houver procura explícita de clientes enterprise.

---

## 🔗 Relacionados

- `app/services/claude.server.ts` — implementação do spawn
- `app/services/businessContext.server.ts` — geração de product terms
- `app/routes/app.settings.tsx` — UI de status e contexto
- `Dockerfile.dev` — instalação do CLI
- `docker-compose.yml` — volume mount das credenciais
