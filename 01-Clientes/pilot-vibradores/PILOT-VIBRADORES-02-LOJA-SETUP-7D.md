# CRONOGRAMA 7D — Setup Loja Shopify **Objectivo:** Loja live, funcional, otimizada, pronta para 45D Sprint. **Duração:** Máximo 7 dias (segunda a domingo) **Recurso:** Rui (PM/owner) + possível ajuda técnica **Tooling:** Shopify, Horizon theme, SE Ranking, GSC, GA4 --- ## 📅 DIA 1 (Segunda) — Keyword Research + Domínio ### Manhã (4h) **Tarefa 1: Pesquisa de Keywords (SE Ranking)**
- [ ] Login SE Ranking
- [ ] Pesquisar 5 seed keywords (vibradores, variações)
- [ ] Documentar: volume, difficulty, competition
- [ ] Filtrar por difficulty < 40 e volume > 100 **Tempo estimado:** 2h **Output:** `/vault/01-Clientes/pilot-vibradores/01-keyword-research.md` preenchido **Tarefa 2: Análise de Competidores**
- [ ] Verificar top 3 sites que rankam para "vibradores"
- [ ] Notar: domínio, theme, estrutura de colecções
- [ ] Identificar opportunities (gaps que eles não cobrem) **Tempo estimado:** 1h **Output:** Insights de competição **Tarefa 3: Proposta de Domínio + Colecções**
- [ ] Definir domínio final (das 3 opções)
- [ ] Confirmar 4-5 colecções principais
- [ ] Mapear keywords para cada colecção **Tempo estimado:** 1h **Output:** Decisão tomada, documentada ### Tarde (2h) **Tarefa 4: Registar Domínio**
- [ ] Verificar disponibilidade (vibradores.pt, vibradorespremium.pt, alternativa)
- [ ] Registar via Namecheap / GoDaddy / Cloudflare
- [ ] Configurar nameservers para Shopify (resolver depois, apontamento DNS) **Tempo estimado:** 0.5h **Output:** Domínio registado **Tarefa 5: Criar Shopify Store**
- [ ] Ir a shopify.com/pt
- [ ] Criar account (email: geral@rankpanda.pt ou separado?)
- [ ] Setup inicial wizard
- [ ] Conectar domínio (apontamento DNS) **Tempo estimado:** 1h **Output:** Shopify store criada, domínio apontado **Nota:** Não há pressa com DNS — pode levar 24h, começa tema enquanto propaga. --- ## 📅 DIA 2 (Terça) — Tema + Estrutura Base ### Manhã (5h) **Tarefa 1: Instalar Tema Horizon**
- [ ] Na Shopify admin, ir a "Online Store" → "Themes"
- [ ] Search "Horizon" (tema gratuito da Shopify)
- [ ] Instalar + confirmar **Tempo estimado:** 0.5h **Output:** Tema ativo **Tarefa 2: Customização Base**
- [ ] Logo upload (criar logo simples ou usar placeholder)
- [ ] Cores: palette (brand colors)
- [ ] Typography: escolher fontes
- [ ] Configurar header, footer, menu principal **Tempo estimado:** 2h **Output:** Site com branding básico **Tarefa 3: Criar Estrutura de Colecções**
- [ ] Ir a "Products" → "Collections"
- [ ] Criar colecções (NÃO adicionar produtos ainda): - Colecção 1: [Nome] - Colecção 2: [Nome] - Colecção 3: [Nome] - Colecção 4: [Nome]
- [ ] Para cada colecção: - Definir title + handle (URL slug) - Escrever description (50-150 chars, incluir keywords) - Upload imagem de capa - Deixar "Manually add products" (não automática ainda) **Tempo estimado:** 2h **Output:** Colecções criadas com estrutura **Tarefa 4: Criar Páginas Base**
- [ ] Home (deixar template do Horizon por enquanto)
- [ ] About Us (200 palavras sobre marca, missão)
- [ ] Contacto (formulário simples)
- [ ] FAQ (5-10 perguntas comuns sobre vibradores — informacional)
- [ ] Privacy Policy (template legal)
- [ ] Terms & Conditions (template legal) **Tempo estimado:** 2h **Output:** Páginas criadas (não otimizadas ainda) ### Tarde (2h) **Tarefa 5: Setup Analytics**
- [ ] Google Analytics 4: - Criar property (vibradores.pt) - Conectar em Shopify (instalar "Google Analytics app") - Validar: página inicial deve começar a recolher dados **Tempo estimado:** 0.5h **Output:** GA4 rastreando **Tarefa 6: Google Search Console**
- [ ] Ir a search.google.com/search-console
- [ ] Adicionar propriedade (vibradores.pt)
- [ ] Validação: via DNS TXT record ou HTML file (DNS é preferível)
- [ ] Submeter sitemap.xml (Shopify gera automaticamente) **Tempo estimado:** 1h **Output:** GSC configurado, sitemap submetido **Tarefa 7: Verificações Técnicas Base**
- [ ] Robots.txt: verificar se está correcto (Shopify default está ok)
- [ ] Sitemap: verificar se está listado (vibradores.pt/sitemap.xml)
- [ ] Mobile responsiveness: testar em telemóvel (site deve funcionar bem)
- [ ] SSL: verificar se tem certificado (Shopify fornece automático) **Tempo estimado:** 0.5h **Output:** Site tecnicamente sólido --- ## 📅 DIA 3 (Quarta) — Produtos + Metafields ### Manhã (6h) **Tarefa 1: Preparar Dados de Produtos**
- [ ] Criar spreadsheet (CSV) com estrutura: - Title (50-60 chars, incluir keywords) - Description (200-300 chars, benefits + features) - Price - Category/Collection - Tags (cor, tamanho, material, feature) - Images (URLs ou upload) - Metafields (custom SEO fields, se necessário) **Exemplo de estrutura:**
```
Title: "Vibrador Clítoris Premium Recargável — Silicone de Qualidade"
Description: "Vibrador profissional para clítoris, 8 modos, silicone premium, impermeável. Recargável via USB. Garantia 2 anos."
Collection: "Vibradores para Clítoris"
Tags: "clitoriano, recargável, silencioso, premium"
``` **Meta SEO customizadas (se Shopify suporta via Bulk Operations):**
- SEO Meta Title (se diferente do product title)
- SEO Meta Description (155-160 chars)
- Slug personalizado (se necessário) **Tempo estimado:** 3h **Output:** CSV pronto (mínimo 5-10 produtos por colecção, total 20-40 produtos) **Tarefa 2: Upload Bulk de Produtos**
- [ ] Shopify Bulk Operations (CSV upload) - Ir a "Products" → "Bulk" - Upload CSV - Mapear campos - Review + confirmar - Processar (pode levar 10-30 minutos) **Tempo estimado:** 1h + processamento **Output:** Produtos importados **Tarefa 3: Verificar e Ajustar Produtos**
- [ ] Verificar alguns produtos no storefront (imagens, descrições)
- [ ] Corrigir erros óbvios
- [ ] Confirmar que produtos aparecem nas colecções **Tempo estimado:** 1h **Output:** Produtos OK para public **Tarefa 4: Configurar Metafields (Opcional, depende de needs)**
- [ ] Se quer campos customizados (ex: "material", "bateria"), definir em Settings
- [ ] Preencher via Bulk ou manualmente (menos priority agora) **Tempo estimado:** 1h (se necessário) **Output:** Metafields customizados (nice-to-have) ### Tarde (3h) **Tarefa 5: Schema Markup**
- [ ] Verificar se Horizon + Shopify auto-incluem schema (fazer check via Google Rich Results Test)
- [ ] Schema necessário: - Product schema (já em Shopify) - Collection schema (testar se está) - BreadcrumbList (testar em colecções) - Organization schema (verificar) - [ ] Se faltar, adicionar via Shopify theme editor ou arquivo JSON-LD **Tempo estimado:** 1h **Output:** Schema valido (testar em https://search.google.com/test/rich-results) **Tarefa 6: Optimizações Rápidas**
- [ ] URLs slugs: confirmar que são SEO-friendly (kebab-case, keywords)
- [ ] Alt text: adicionar alt text a imagens principais (colecções, alguns produtos)
- [ ] Links internos: adicionar breadcrumbs + "related products" (Horizon pode ter isso built-in) **Tempo estimado:** 1h **Output:** Site com SEO basics --- ## 📅 DIA 4 (Quinta) — Optimizações + Integrações ### Manhã (4h) **Tarefa 1: Optimização de Colecções**
- [ ] Para cada colecção, escrever: - H1 claro (nome colecção) - Meta description (155-160 chars, incluir keywords) - Intro text (100-200 words, natural, não keyword-stuffing) - Breadcrumb visual **Tempo estimado:** 1.5h **Output:** Colecções otimizadas **Tarefa 2: Configurar Política de Privacidade + Legal**
- [ ] Privacy Policy: atualizar com Shopify specifics (cookies, data handling)
- [ ] Termos e Condições: template legal português
- [ ] Contacto: email de suporte + formulário funcional **Tempo estimado:** 1h **Output:** Legal OK **Tarefa 3: Email Setup**
- [ ] Email de suporte (geral@rankpanda.pt ou suporte@vibradores.pt?)
- [ ] Teste: enviar email de contacto e confirmar que chega
- [ ] Newsletter signup (opcional, pode adicionar depois): Shopify tem formulário de signup built-in **Tempo estimado:** 0.5h **Output:** Email funcional **Tarefa 4: Verificações de Performance**
- [ ] Google PageSpeed Insights: - Testar homepage - Testar página de colecção - Notar scores (performance, SEO, accessibility) - Otimizações rápidas (se houver problemas críticos) **Tempo estimado:** 1h **Output:** Performance baseline (não precisa ser perfeito agora) ### Tarde (2h) **Tarefa 5: IndexNow Setup**
- [ ] IndexNow permite notificar Google/Bing imediatamente de novas páginas
- [ ] Gerar API key (via search.google.com ou bing.com)
- [ ] Configurar em Shopify (via app ou manual JSON API calls)
- [ ] Testar: notificar URL de teste, confirmar em GSC dentro de segundos **Tempo estimado:** 1h **Output:** IndexNow funcional **Tarefa 6: Final Checklist**
- [ ] [ ] Domínio propagado (deve estar +/- OK)
- [ ] [ ] Site responsivo (testar em mobile)
- [ ] [ ] Analytics rastreando
- [ ] [ ] GSC reconhecendo site
- [ ] [ ] Schema OK (testar rich results)
- [ ] [ ] Imagens otimizadas
- [ ] [ ] URLs amigáveis **Tempo estimado:** 0.5h **Output:** Check list preenchida --- ## 📅 DIA 5 (Sexta) — QA + Bug Fixes ### Manhã + Tarde (6h) **Tarefa 1: Teste Completo de UX**
- [ ] Desktop: home, colecção, produto, checkout (até confirmação, não comprar)
- [ ] Mobile: mesmas páginas
- [ ] Notar: links quebrados, imagens faltando, texto estranhamente formatado **Tempo estimado:** 1.5h **Output:** Lista de bugs (se houver) **Tarefa 2: Fix de Bugs**
- [ ] Corrigir qualquer coisa óbvia encontrada
- [ ] Se há problemas maiores (checkout não funciona, theme crashado), resolver imediatamente **Tempo estimado:** 1.5h **Output:** Site funcional **Tarefa 3: Performance Final**
- [ ] Lighthouse novamente (esperamos melhoria ou pelo menos baseline)
- [ ] Mobile usability check (Google Mobile-Friendly Test)
- [ ] 404 check (Screaming Frog quick crawl ou GSC) **Tempo estimado:** 1h **Output:** Performance OK **Tarefa 4: Preparação para Go-Live**
- [ ] Remover qualquer "coming soon" banner
- [ ] Confirmar que "Notify customers" está desativado (não queremos spam)
- [ ] Backup: Shopify backups are automatic, mas confirmar **Tempo estimado:** 0.5h **Output:** Pronto para public **Tarefa 5: Documentação de Setup**
- [ ] Criar doc rápido com: - Shopify store URL - Admin login - GA4 property ID - GSC verified - Domínio registado - Theme usado (Horizon) - Colecções criadas (lista) - Produtos count por colecção **Tempo estimado:** 1h **Output:** Doc de referência --- ## 📅 DIA 6 (Sábado) — Launch Day ### Manhã (2h) **Tarefa 1: Teste Final**
- [ ] Última verificação: site carrega, colecções visíveis, produtos listados
- [ ] Analytics está recolhendo
- [ ] GSC diz: "site is healthy" **Tempo estimado:** 0.5h **Output:** Go ahead para launch **Tarefa 2: Launch!**
- [ ] Se o site estava em "preview" ou "coming soon", aktivar como público
- [ ] Anunciar em Discord / email pessoal (ou não, depende strategy)
- [ ] Registar momento: "Launch time = [timestamp] em Lisbon" **Tempo estimado:** 0.5h **Output:** Loja LIVE **Tarefa 3: Monitoring Primeiro Dia**
- [ ] Monitor GA4: algum tráfego? (pode ser muito pouco no dia 1)
- [ ] Verificar GSC: Google já a rastrear?
- [ ] Check errors: algum erro 404, 500? **Tempo estimado:** 1h **Output:** Baseline de dia 1 --- ## 📅 DIA 7 (Domingo) — Prep para FASE 0 ### Manhã (3h) **Tarefa 1: Recolher Baseline Métricas**
- [ ] GSC: indexed pages (provavelmente muito baixo, ok)
- [ ] GA4: sessions (provavelmente 0 ou muito poucas)
- [ ] Check: todos os products estão indexados? (via site:vibradores.pt em Google, ou GSC) **Tempo estimado:** 1h **Output:** Baseline.json completo **Tarefa 2: Preparação para FASE 0 (Kickoff)**
- [ ] Criar documento FASE 0 Kickoff (se cliente externo, isto seria formalizado)
- [ ] Definir timeline FASE 1-3
- [ ] Confirmar KPIs (top 10 posição para X keywords) **Tempo estimado:** 1h **Output:** Kickoff doc pronto **Tarefa 3: Documentação**
- [ ] Atualizar MASTER-PLAN com status "LOJA LIVE"
- [ ] Criar primeira entrada de metrics (baseline.json)
- [ ] Registar qualquer learnings (que dificuldades teve, o que correu bem) **Tempo estimado:** 1h **Output:** Tudo documentado --- ## ⚡ Checkpoints Críticos | Checkpoint | Dia | Status | Bloqueador? |
|-----------|-----|--------|-------------|
| Domínio registado | 1 | [ ] | SIM |
| Shopify criado | 1 | [ ] | SIM |
| Tema Horizon instalado | 2 | [ ] | SIM |
| Colecções criadas | 2 | [ ] | Não (pode adicionar produtos depois) |
| Produtos uploadados | 3 | [ ] | Não (mínimo 20, pode expandir) |
| Analytics rastreando | 2 | [ ] | SIM (baseline crítica) |
| GSC verificado | 2 | [ ] | SIM (discovery crítica) |
| Schema válido | 4 | [ ] | Não (pode melhorar pós-launch) |
| Loja LIVE | 6 | [ ] | SIM | --- ## 📊 Recursos Necessários - **Shopify:** Account + plano (plan básico ~€29/mês)
- **Domínio:** Registar (~€10-15/ano)
- **Google Analytics:** FREE (account Google)
- **Google Search Console:** FREE
- **SE Ranking:** Acesso Rui (API key)
- **Imagens:** Precisa de ~50-100 imagens de produtos (stock photos, ou setup fotografia) --- ## 🔄 Handoff para FASE 0 Quando DIA 7 acabar:
1. Loja LIVE ✓
2. Baseline métricas recolhidas ✓
3. Documentação completa ✓
4. FASE 0 Kickoff pronto para começar **Próximo:** `/vault/01-Clientes/pilot-vibradores/03-45d-sprint-fase-0.md` --- **Versão:** 1.0 **Data:** 2026-04-20 **Status:** PRONTO PARA EXECUTAR **Duração:** 7 dias máximo (segunda-domingo)
