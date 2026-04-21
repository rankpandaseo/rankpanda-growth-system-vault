---
name: sop-1-store-context-setup
description: Onboarding oficial — recolher contexto de loja (industria, categorias, AOV, CR, objetivos)
type: sop
status: active
foco: operacional
tags: [onboarding, store-context, baseline, phase-0]
wikilinks: [[[sop-2-keyword-research]], [[sop-3-clustering-collection-mapping]], [[fase-0-kickoff]], [[pilot-vibradores]]]
---

# SOP 1 — Store Context Setup

**Fase:** PRÉ-FASE 0 (Onboarding Oficial)  
**Quando:** Imediatamente após **contrato assinado**  
**Duração:** 2-4 horas  
**Proprietário:** Rui + Cliente  
**Próximo Passo:** [[SOP-2-KEYWORD-RESEARCH-V2|SOP 2 — Keyword Research]]

---

## 🎯 POR QUE ISTO IMPORTA

Este é o **ponta-pé de saída oficial do projecto**. Sem Store Context bem preenchido, tudo o que vem depois falha:

### Para SEO
- **SOP 2 (Keyword Research):** Sem indústria, mercado, e categorias, o Claude relevance gate não consegue distinguir keywords relevantes de noise. Resultado: desperdício de API spend + keywords inúteis
- **SOP 3 (Clustering):** Sem saber exatamente o que a loja vende, não consegues agrupar keywords em collections lógicas
- **Revenue Potential:** Sem AOV (ticket médio) e Conversion Rate benchmark, todas as métricas de priorização (effort score, revenue potential) ficam inúteis

### Para RankPanda
- Documenta **decisões iniciais** que impactam todo o projecto (6 meses)
- **Valida realismo** do cliente (objetivos alinhados? Conhecem o seu mercado?)
- **Cria base durável** — se tudo mudar em FASE 2, voltamos aqui para rever

**Analogia:** É como construir uma casa. Alicerce fraco = tudo desaba depois.

---

## 📋 Pré-requisitos

Antes de começar SOP-1:
- ← [[FASE-0-KICKOFF]] — **Setup técnico:** Acesso a Shopify, Google Search Console, Google Analytics 4 devem estar em vias de confirmação. Métricas baseline devem estar agendadas.

**Nota:** SOP-1 é o primeiro passo formal. Se cliente não assinou contrato ainda, aguarda assinatura.

---

## 📋 ESTRUTURA DO PROCESSO

```
Contrato Assinado
    ↓
[HOJE] SOP 1: Preencher Store Context (2-4h)
    ↓
Outputs: SQLite record + Briefing preenchido
    ↓
[AMANHÃ] SOP 2: Keyword Research (8-12h)
    ↓
SOP 3: Clustering + Collections (6-8h)
    ↓
FASE 0: Kickoff oficial
```

---

## 🔧 PARTE A — Campos Obrigatórios (5 campos)

### ⚠️ INSTRUÇÕES GERAIS
- **Todos os 5 campos são BLOQUEADORES.** Se não consegues responder, marca como "TBD (to be determined)" e volta em call síncrona com o cliente
- **Duração esperada:** 45-60 minutos
- **Formato:** Respostas claras, concretas, sem buzzwords

---

### **1️⃣ STORE NAME** (Obrigatório)

**O que é:** Nome comercial da loja, usado em comunicações e relatórios.

**Formato esperado:**
- ✅ Texto simples (permite acentos, hífens)
- ✅ Tamanho: 3-50 caracteres
- ✅ Exemplos: "Loja do Inseto", "VibradoresLux", "Benedita Formosinho", "TechGear Portugal"

**Rejeição:**
- ❌ Vazio
- ❌ Genérico demais ("Shopify Store", "Online Shop", "Loja 123")
- ❌ Apenas código/ID

**Se cliente tem dúvidas:**
> "Este é o nome que apareça em emails, relatórios, e documentação interna. Deve ser o nome comercial da marca."

---

### **2️⃣ INDUSTRY / VERTICAL** (Obrigatório)

**O que é:** Vertical industrial da loja (impacta benchmark de conversion rate, intent analysis, seasonal trends).

**Opções disponíveis (dropdown):**
1. **Adult Wellness** (sexual products, wellness)
2. **Fashion & Apparel** (roupa, acessórios)
3. **Beauty & Cosmetics** (cosméticos, skincare)
4. **Health & Supplements** (suplementos, health)
5. **Food & Beverage** (alimentos, bebidas)
6. **Home & Lifestyle** (móveis, decoração, lifestyle)
7. **Electronics** (tecnologia, eletrónicos)
8. **Luxury Goods** (artigos premium/luxo)
9. **Other: [Descrever]** (outra indústria — descrever em 1-2 linhas)

**Se cliente não encaixa:**
> "Escolhe 'Other' e descreve em 1-2 frases. Exemplo: 'Serviços de fotografia profissional para eventos'."

**Impacto no projecto:**
- Define **benchmark de conversion rate** (tabela em PARTE B)
- Define **padrões de intent semântico** (Adult Wellness ≠ Fashion ≠ Health)
- Alimenta **análise competitiva** (quem mais rankeia?)

---

### **3️⃣ PRIMARY MARKET / GEOGRAPHY** (Obrigatório)

**O que é:** Mercado geográfico principal (país/região onde a loja pretende rankear).

**Formato esperado:**
- ✅ Código ISO 2 caracteres: **PT, ES, BR, GB, US, DE, FR, IT, etc.**
- ⚠️ **UMA ÚNICA OPÇÃO** (mercado principal)

**Exemplos corretos:**
- ✅ "PT" (Portugal)
- ✅ "BR" (Brasil)
- ✅ "ES" (Espanha)

**Exemplos ERRADOS:**
- ❌ "Portugal" (use código ISO)
- ❌ "PT + ES" (escolhe o primário; ES fica para FASE 2)
- ❌ "Europa" (muito vago)

**Se cliente quer múltiplos mercados:**
> "Escolhe o mercado com MAIOR revenue esperado (primário). Os outros ficam para FASE 2 (mês 4-6), quando temos autoridade."

**Impacto no projecto:**
- Define **idioma de keyword research** (PT → português, BR → português + brasileiro, ES → espanhol)
- Define **market-specific keywords** (Rui vs tu, vosotros vs os)
- Define **sazonalidade local** (Black Friday em PT é diferente de BR)

---

### **4️⃣ TARGET PRODUCT CATEGORIES** (Obrigatório)

**O que é:** 3-10 categorias principais de produtos que a loja vende.

**Formato esperado:**
- ✅ Lista de 3-10 categorias
- ✅ Nomes descritivos (não genéricos)
- ✅ Hierarquia clara

**Exemplo (Adult Wellness):**
```
1. Vibradores para Clítoris
2. Vibradores Ponto G
3. Masturbadores
4. Premium / Luxury
5. Acessórios & Características (recargáveis, impermeáveis, etc.)
```

**Exemplo (Fashion):**
```
1. Blusas & Camisas
2. Calças & Jeans
3. Cardigans & Malhas
4. Acessórios (cintos, echarpes)
5. Colecções Temáticas (Primavera, Inverno)
```

**Rejeição:**
- ❌ Menos de 3 categorias (horizonte muito estreito)
- ❌ Mais de 10 (confuso, difícil de rankear em tudo)
- ❌ Genérico demais ("Produtos", "Homem", "Mulher")
- ❌ Sem hierarquia (1º nível vs subcategorias misturado)

**Se cliente tem muitas categorias (15+):**
> "Prioriza pelas 3-5 categorias com MAIOR volume/margem esperado. Resto pode entrar em FASE 2."

**Impacto no projecto:**
- Define **Shopify collection structure** (SOP 3)
- Define **keyword clustering** (cada cluster = categoria)
- Define **prioritização de effort** (some categories mais fáceis de rankear que outras)

---

### **5️⃣ BRAND CONTEXT DESCRIPTION** (Obrigatório)

**O que é:** Descrição breve da marca, posicionamento, diferenciadores. Alimenta análise de keyword intent + posicionamento SEO.

**Formato esperado:**
- ✅ **150-300 palavras** (linguagem clara, sem fluff)
- ✅ Deve conter:
  1. **O que vende** (traços gerais)
  2. **Para quem vende** (público-alvo)
  3. **Diferenciadores chave** (por que é diferente?)
  4. **Valores da marca** (sustentabilidade, qualidade, inovação, etc.)
  5. **Contexto de mercado** (online only, loja física, ambos?)

**Exemplo BOAS:**

> **Adult Wellness (Vibradores):**
> "Loja online especializada em produtos de wellness sexual para mulheres e casais. Focada em educação, privacidade, e qualidade. Diferenciadores: silicone premium (não PVC), design discreto, recarga USB, garantia 2 anos, shipping anónimo em caixa neutra. Target: mulheres 25-50 que buscam produtos de qualidade com confidencialidade. Valores: educação sexual (sem tabus), consentimento, sustentabilidade (packaging reutilizável)."

> **Fashion (Benedita):**
> "Marca portuguesa de moda sustentável com foco em peças de alta qualidade, design intemporal e produção local. Vende blusas, camisas, calças, cardigans, malhas em algodão orgânico e linho. Diferenciadores: produção em Portugal, design premium, sustentabilidade certificada, combinabilidade entre coleções (armário intercambiável). Target: mulheres 30-55 que valorizam qualidade, sustentabilidade e design atemporal. Presença física: loja em Lisboa (Príncipe Real) e pop-up em Cascais."

**Exemplo FRACO (REJEITA):**
> "Vendemos bons produtos a preços baixos." ❌ (vago, genérico, sem diferenciadores)

> "Loja de roupas para todos." ❌ (sem público-alvo claro)

> "Oferecemos qualidade." ❌ (toda a gente diz isto)

**Validação rápida:**
Depois de cliente responder, faz 3 perguntas mentalmente:
1. ✅ Consigo diferenciar esta marca de 5 concorrentes só lendo isto?
2. ✅ Entendo exatamente para quem é?
3. ✅ Entendo por que um cliente escolheria isto em vez de concorrente?

Se resposta ≥2x SIM → OK. Se ≤1x SIM → pedir reescrever.

**Impacto no projecto:**
- Alimenta **Claude relevance gate** em SOP 2 (distinguir keywords relevantes)
- Alimenta **semantic keyword analysis** (variações semânticas que fazem sentido para marca)
- Guia **messaging em product titles/descriptions** (como escrevemos sobre produtos?)

---

## 💰 PARTE B — Métricas Comerciais (2 campos, 1 condicional)

### ⚠️ INSTRUÇÕES GERAIS
- **Campos 6-7:** Obrigatórios
- **Campo 8 (Objectives):** Condicional — se cliente quer definir objetivo específico. Se não, usar default
- **Duração esperada:** 15-20 minutos

---

### **6️⃣ AVERAGE ORDER VALUE (AOV)** (Obrigatório)

**O que é:** Ticket médio esperado de venda (produto × quantidade por order).

**Formato esperado:**
- ✅ Número em EUR (moeda única do sistema)
- ✅ Baseado em: **média de produtos + quantidade esperada por order**

**Exemplos:**
- Vibradores: €35 (1 vibrador por order, €20-€50 range)
- Fashion: €75 (2-3 peças por order)
- Electronics: €200 (1 item, mais caro)

**Se cliente não sabe:**
1. Pedir **lista de top 10 produtos + preços**
2. Calcular média simples: (preço_1 + preço_2 + ... + preço_10) / 10
3. **Ajustar por quantity esperada:** se esperas 1.5 items/order, multiplica por 1.5

**Impacto no projecto:**
- Alimenta **revenue potential calculation** em SOP 2:
  ```
  Revenue Potential = Search Volume × CTR × CR × AOV
  Exemplo: 800 × 0.025 × 0.02 × €35 = €14/mês
  ```

**Validação:**
- ✅ AOV >= €10 (viável para ecommerce)
- ❌ AOV < €5 (difficulty in making sense financially)

---

### **7️⃣ CONVERSION RATE BENCHMARK** (Obrigatório)

**O que é:** Taxa de conversão esperada (% de visitantes que compram). Usada como default até ter GA4 data real.

**Tabela de Defaults por Indústria (2026):**

| Indústria | Benchmark CR | Nota |
|-----------|-------------|------|
| **Food & Beverage** | 6.0% | Muito maturo, impulse buying |
| **Health/Beauty/Personal Care** | 4.5% | Estabelecido, alguma research |
| **Adult Wellness** | 2.5% | Nicho, buyer persona mais seletiva |
| **Fashion & Apparel** | 2.5% | Maturo, mas custo acquisition alto |
| **Consumer Goods** | 2.8% | Médio |
| **Electronics** | 1.5% | Pesquisa extensa, comparison shopping |
| **Luxury** | 1.0% | Muito seletivo, venda consultiva |

**IMPORTANTE — Decision Tree:**

```
Cliente tem GA4 data real?
├─ SIM → Use o CR real de GA4 (mais fiável)
│        Nota: "Validar com GA4 após primeiros 30 dias"
│
└─ NÃO → Use benchmark da tabela
         ├─ Loja nova/baseline? → Use default
         │
         └─ Razão específica para desvio?
            (ex: "Espero ser mais alto porque tem brand awareness")
            → OK, mas documenta assumption
            → Rever em FASE 1 com dados reais
```

**Exemplo (Pilot-Vibradores):**
- Indústria: Adult Wellness → benchmark 2.5%
- Loja: **NOVA** → Conservative → **Set to 2.0%**
- Reasoning: "Loja nova sem histórico, no mercado português que é nicho. Usar 2.0% como expectativa conservadora, refinar em FASE 1."

**Validação:**
- ✅ CR entre 0.5%-10% (viável)
- ❌ CR > 15% (unrealistic para produto novo)
- ❌ CR = 0% (não faz sense)

**Impacto no projecto:**
- Alimenta **revenue potential** em SOP 2
- Usa em **ROI projections** (quanto vale rankear keyword X?)
- **Base comparativa** quando GA4 data chegar (se real é 4%, beat 2% expectation)

---

### **8️⃣ BUSINESS OBJECTIVES — SEO SPECIFIC** (Condicional)

**O que é:** Objetivo específico para os 6 meses do projecto. **Apenas SEO**, não vendas genéricas.

**Formato esperado:**

**SEO objectives válidos:**
- ✅ "50 keywords em TOP 30, 5-10 em TOP 10, dentro de 6 meses"
- ✅ "€2000-€5000/mês em organic revenue (via SEO traffic) em 3 meses"
- ✅ "1000+ organic sessions/mês em FASE 3"
- ✅ "Dominar 3 product categories em TOP 5 (keywords principais)"

**Não são SEO objectives:**
- ❌ "Aumentar conversion rate" (está fora de scope SEO — isso é CRO)
- ❌ "Vender mais" (vago, não mensurável)
- ❌ "Ser conhecido" (brand awareness, não SEO)
- ❌ "Ter 1000 customers" (sales target, não SEO)

**Se cliente não sabe:**
> "O nosso foco em 6 meses é: X keywords em TOP 10 + Y keywords em TOP 30 + Z organic sessions/mês. Qual é realista para vós?"

**Default (se não responde):**
> "Objetivo: Dominar top 3 categorias de products (15-20 keywords) em TOP 10 e expandir para 50-100 keywords em TOP 30 em 6 meses."

**Impacto no projecto:**
- Define **KPIs de sucesso** para FASE 1-3
- Define **priorização** (se objetivo é "50 TOP 30", atacamos volume; se "5 TOP 10", atacamos dificuldade)
- Define **cliente satisfaction** (no fim, isto é sucesso ou fracasso?)

---

## ✅ PARTE C — Contexto Operacional (Condicional)

### ⚠️ INSTRUÇÕES GERAIS
- **Campos 9-11:** Condicional — nice-to-have, não bloqueadores
- **Impacto:** Operacional (comunicação, timing, access)
- **Duração esperada:** 10-15 minutos

---

### **9️⃣ COMMUNICATION PREFERENCES** (Condicional — nice-to-have)

**O que é:** Como comunicar com cliente (contactos, frequência, canal preferido).

**Campos:**
- `primary_contact_name` (string)
- `primary_contact_phone` (phone)
- `primary_contact_email` (email)
- `secondary_contact_name` (string — opcional)
- `communication_channel` (email / WhatsApp / Slack — preferência)

**Exemplo:**
```
Primary: Rui Patarrana — 919718842 — rui@rankpanda.pt
Secondary: Sara Leal — 927644901 — sara@rankpanda.pt
Channel: WhatsApp para urgências, Email para briefings de fase
Frequency: Update semanal (segunda de manhã)
```

**Se cliente não sabe:**
> "Coloca o teu contacto principal e como preferes ser contactado (email é default)."

**Impacto no projecto:**
- Define **communication cadence** e **responsiveness**
- Evita delays de weeks por falta de input

---

### **🔟 ACCESS & TOOLS CONFIRMATION** (Condicional — nice-to-have)

**O que é:** Confirmação de accesso a ferramentas necessárias (Shopify, Google).

**Campos:**
- `shopify_access` (boolean) — Cliente confirmou acesso ao Shopify admin?
- `gsc_configured` (boolean) — Google Search Console já está setup?
- `ga4_installed` (boolean) — Google Analytics 4 já está rastreando?
- `other_stakeholders` (string) — Há outras agências/pessoas envolvidas?

**Exemplo:**
```
Shopify: SIM (cliente tem acesso, email confirmado)
GSC: NÃO (pendente — fazer setup em FASE 0)
GA4: NÃO (pendente — instalar em FASE 0)
Other stakeholders: Aero Agency (criou design, pode dar input em estilo)
```

**Se cliente não tem:**
> "OK, fazemos setup em FASE 0. Precisamos de acesso Shopify e Google account — vamos guiar."

**Impacto no projecto:**
- Define **workflow de integração** (quanto tempo custa setup?)
- Identifica **bloqueadores** (se agência terceira controla Shopify, há latência)

---

### **1️⃣1️⃣ PRODUCT CATALOG — SKIP SE LOJA NOVA** (Condicional — PASSAR se novo)

**⚠️ REGRA: Se loja é nova (0 produtos), SKIP este campo completamente.**

**O que é (se loja existente):** Confirmação de produtos, specs, descrições disponíveis.

**Campos (só para lojas com produto):**
- `total_skus` (number) — Quantos produtos?
- `product_descriptions_exist` (boolean) — Descrições já escritas?
- `technical_specs_available` (boolean) — Especificações técnicas (material, tamanho, etc.) disponíveis?

**Exemplo (se loja existente):**
```
Total SKUs: 120
Descriptions: SIM, mas muitas são curtas (<100 palavras)
Technical Specs: SIM, estão em ficheiro interno, não no site
```

**Se loja é nova:**
```
[SKIP - Loja será criada em setup de 7D]
Será preenchido retrospectivamente após produtos serem uploaded.
```

**Impacto no projecto:**
- Define **on-page optimization scope** em SOP 4
- Se descriptions fracas, precisam reescrita (SEO-friendly)
- Se specs em ficheiro, cria oportunidade de enriquecimento

---

## 🔍 VALIDAÇÃO & STORAGE

### **Checklist de Preenchimento**

```markdown
BLOQUEADORES (Obrigatório):
- [ ] Store Name preenchido
- [ ] Industry selecionado (ou Other descrito)
- [ ] Primary Market (country code)
- [ ] Target Categories (3-10)
- [ ] Brand Context Description (150-300 palavras, com diferenciadores)
- [ ] AOV preenchido
- [ ] Conversion Rate Benchmark (real GA4 ou default escolhido)

NICE-TO-HAVE:
- [ ] Business Objectives (SEO-specific)
- [ ] Communication Preferences
- [ ] Access & Tools confirmado
- [ ] Product Catalog (apenas se loja não é nova)

Se tudo ✅ → Proceder para SOP 2
Se algo ❌ → Mark TBD, schedule follow-up call
```

---

### **Database Schema (SQLite)**

```sql
CREATE TABLE store_context (
  id INTEGER PRIMARY KEY,
  store_name TEXT NOT NULL,
  industry TEXT NOT NULL,
  primary_market TEXT NOT NULL,
  categories JSON NOT NULL,
  context TEXT NOT NULL,
  aov REAL NOT NULL,
  conversion_rate_benchmark REAL NOT NULL,
  objectives TEXT,
  communication_contacts JSON,
  access_info JSON,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status TEXT DEFAULT 'ready_for_sop2'
);
```

---

## ❓ FREQUENTLY ASKED QUESTIONS

### **P: O que fazer se cliente não consegue responder a um campo?**
**R:** Mark como "TBD (to be determined)". BLOQUEADORES (1-7) = call síncrona needed. Nice-to-have (8-11) = pode deixar vazio por agora.

### **P: Posso reeditar SOP 1 depois de preenchido?**
**R:** **SIM**, mas documenta a mudança (update field `updated_at` em DB). Vai impactar SOP 2-3. Se mudança é grande (ex: categoria completamente diferente), rever keyword strategy em SOP 2.

### **P: AOV é obrigatório? E se cliente tem mix de produtos muito variável?**
**R:** **SIM, é obrigatório.** Se ticket varia (€15-€80), usa a **média ponderada** (produtos com mais volume pesam mais). Exemplo: "€35 (média de 1 clítoris vibrador €25 + 1 vibrador ponto G €45)."

### **P: Conversion Rate — quando usar real vs default?**
**R:** 
- **Tem GA4 data 30+ dias?** → Use real
- **Loja nova / sem data?** → Use default + nota "Refinar em FASE 1 com dados reais"
- **Cliente insiste valor diferente?** → OK, documenta assumption e razão

### **P: Se cliente tem 25 categorias, o que fazer?**
**R:** "Prioriza top 5 por revenue + margem. Resto entra em FASE 2 (após dominar primárias)."

### **P: Brand Context Description — quanto é realmente mínimo?**
**R:** 
- **Mínimo:** 150 palavras + diferenciadores + público-alvo = SIM
- **Inaceitável:** <100 palavras OU genérico OU "vendemos produtos bons"
- **Se cliente envia fraco:** Devolve com feedback, pede reescrita

### **P: Se loja é nova, verdadeiramente skip Product Catalog?**
**R:** **SIM, skip completamente.** Será preenchido após upload de produtos em 7D setup. Não é bloqueador.

### **P: Posso começar SOP 2 sem SOP 1 completo?**
**R:** **Não recomendado.** SOP 2 precisa de indústria + categories + AOV/CR para funcionar. Sem isto, relevance gate e revenue potential falham.

### **P: Qual é o máximo de mercados/países?**
**R:** SOP 1 = **1 mercado primário apenas**. Multi-mercado entra em FASE 2-3 (após dominar primário).

---

## 🚨 CENÁRIOS DE ERRO & RESOLUÇÃO

### **Cenário 1: Cliente não sabe Conversion Rate**
**Erro comum:** Cliente quer usar 50% CR (unrealistic).
**Resolução:** 
1. Mostrar tabela de benchmarks (industry-specific)
2. Explicar: "2.5% significa 1 em 40 visitantes compra — isto é normal para ecommerce"
3. Usar default da tabela, documentar como "Conservative estimate, validar em FASE 1"

### **Cenário 2: Cliente tem múltiplos mercados (PT + ES)**
**Erro comum:** Preencher primary_market como "PT+ES" (não é válido).
**Resolução:**
1. "Qual mercado tem maior potencial de revenue?"
2. Usar esse como primary
3. Documentar: "ES será expandido em FASE 2, após dominar PT"

### **Cenário 3: Loja é nova, sem histórico de vendas**
**Erro comum:** Cliente não consegue estimar AOV nem CR.
**Resolução:**
1. **AOV:** Pedir lista de top 5 produtos + preços → calcular média
2. **CR:** Usar default por indústria + "Conservador para loja nova" → refinar em FASE 1

### **Cenário 4: Brand Context Description é genérico demais**
**Erro comum:** "Vendemos roupas de qualidade para mulheres."
**Resolução:**
1. Devolver com feedback: "Precisa de: diferenciadores (por que VOSSO vs concorrentes), valores (sustentabilidade?), público-alvo específico (idade, income)"
2. Pedir reescrita com template:
   ```
   O que vendem: [específico]
   Para quem: [público-alvo + características]
   Por que diferente: [diferenciadores vs concorrentes]
   Valores: [sustentabilidade, qualidade, inovação, etc.]
   ```

### **Cenário 5: Objetivo de negócio é "vender mais"**
**Erro comum:** "Objetivo é aumentar vendas em 50%."
**Resolução:**
1. Redirecionar: "O nosso foco é **SEO traffic** — vender mais via organic search. Qual é realista?"
2. Traduzir para SEO KPIs: "Objetivo: X keywords em TOP 10 = Y organic sessions = estimado Z vendas (via AOV × CR)"

---

## ✅ PRÓXIMAS ETAPAS

**Após SOP 1 preenchido:**

1. **Guardar em SQLite** (1-2 minutos)
2. **Exportar para internal briefing** (para RankPanda context)
3. **Proceed para [[SOP-2-KEYWORD-RESEARCH-V2|SOP 2]]** (keyword research — 8-12h)

---

## 📊 CHECKLIST FINAL

- [ ] Cliente assinou contrato
- [ ] SOP 1 fields preenchidos (5 obrigatórios + optional)
- [ ] Validação passou (qualidade de respostas OK)
- [ ] Stored em SQLite
- [ ] RankPanda team tem briefing
- [ ] ✅ Ready para SOP 2

---

## 🔗 Links Relacionados

**Dependências & Fluxo Sequencial:**
- [[FASE-0-KICKOFF]] ← **Pré-requisito:** Setup técnico (Shopify, GSC, GA4) e baseline metrics obrigatórios antes de SOP-1
- [[SOP-2-KEYWORD-RESEARCH-V2]] → **Output:** Store context completo alimenta keyword research strategy (industria, categorias, AOV, CR determinam scoring de keywords)
- [[SOP-3-CLUSTERING-COLLECTION-MAPPING]] ↔ **Conceito Transversal:** Shopify Collections são mapeadas a partir de Target Categories definidas aqui em SOP-1

**Exemplos & Referência:**
- [[pilot-vibradores]] → **Caso Real:** Implementação concreta de SOP-1 com Adult Wellness vertical, PT market, 5 categorias, €35 AOV

---

**Versão:** 2.0  
**Data:** 2026-04-21  
**Status:** ATIVO  
**Próximo:** [[SOP-2-KEYWORD-RESEARCH-V2]] (após store context validado)
