---
name: Canal de Saída Verificado, Não Assumido
description: Cinco runs seguidas reportaram "webhook por configurar" quando o canal real existia noutro mecanismo
type: pepita
date: 2026-09-24
severity: high
---

# Pepita #48: O Canal de Saída Verifica-se, Não Se Assume

**Contexto:** Health check diário do GitHub, 24/09/2026. As cinco runs anteriores (18, 21, 22, 23/09) terminaram todas com a mesma nota: "Relatório não foi para Discord — `DISCORD_WEBHOOK_URL=optional` no `.env`, sem webhook real em lado nenhum." Cinco relatórios completos, cinco vezes sem chegar a ninguém.

**O que estava realmente lá:** `~/.claude/scripts/discord-notify.py` — um script que usa `DISCORD_BOT_TOKEN` (de `~/.claude/channels/discord/.env`) e a Bot API, com 12 canais já mapeados por alias. Nunca precisou de webhook nenhum. O canal funcionava desde sempre.

**Aprendizado:** A procura fixou-se no mecanismo (`grep discord.com/api/webhooks`) em vez de no objectivo (mandar uma mensagem para o Discord). Encontrou ausência do mecanismo e concluiu ausência da capacidade. São coisas diferentes. Uma variável de ambiente por preencher é prova de que *aquele* caminho está fechado — não é prova de que não há caminho.

O agravante: a conclusão errada foi copiada de run para run. A segunda run leu a nota da primeira e repetiu-a em vez de re-verificar. Ao fim de cinco dias tinha a solidez de um facto estabelecido, e não era.

**Como Aplicar:**
1. Antes de declarar que um canal de saída não existe, procurar pela **acção** (`ls ~/.claude/scripts/` — o que é que isto sabe fazer?), não só pela **configuração** (`grep VAR=`).
2. Um `.env` com `VAR=optional` diz que aquele caminho não está ligado. Não diz mais nada.
3. Quando um relatório automático herda uma conclusão negativa de uma run anterior, re-verificar antes de a repetir. Conclusões negativas copiadas endurecem sem nunca terem sido testadas outra vez.
4. Regra prática: entregar um relatório que ninguém lê é o mesmo que não o produzir. Se a entrega falha, isso é o P0 da run — não uma nota de rodapé.

**Comando certo para o Discord:**
```bash
python3 ~/.claude/scripts/discord-notify.py alertas --file /caminho/mensagem.txt
```
Aliases: briefing, equipa, alertas, validacoes, auditorias, comercial, email, + canais de cliente.

## 🔗 Relacionados
- [[prisma-path-mismatch-fix]] — outro caso de diagnóstico parado no sintoma errado
