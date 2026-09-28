# 💰 FinanIA — Assistente Inteligente de Organização Financeira

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual com Inteligência Artificial"** da Digital Innovation One (DIO).

O projeto foi desenvolvido a partir do repositório-base disponibilizado pela DIO e adaptado para criar o **FinanIA**, um assistente virtual capaz de consultar e explicar informações financeiras presentes em uma base de conhecimento.

## 🎯 Objetivo

O FinanIA utiliza Inteligência Artificial Generativa para permitir que uma pessoa usuária faça perguntas em linguagem natural sobre informações financeiras fictícias.

O agente pode auxiliar na consulta de:

- transações;
- gastos por categoria;
- receitas;
- metas financeiras;
- perfil financeiro;
- histórico de atendimento;
- informações sobre produtos presentes na base.

## 🤖 Exemplos de perguntas

```text
Quanto gastei com alimentação?

Qual foi minha maior despesa?

Quanto recebi de salário?

Qual é meu objetivo financeiro principal?

Quanto tenho atualmente na reserva de emergência?

Quais produtos financeiros estão disponíveis na base?

```

O agente também deve informar quando uma informação não estiver disponível ou quando uma pergunta estiver fora do escopo.

## 🧠 Arquitetura

```text
Usuário
   ↓
Interface Streamlit
   ↓
FinanIA
   ↓
Base de conhecimento
   ↓
Google Gemini
   ↓
Resposta

```

## 📚 Base de conhecimento

O projeto utiliza os dados mockados fornecidos pelo Lab:

```text
data/
├── historico_atendimento.csv
├── perfil_investidor.json
├── produtos_financeiros.json
└── transacoes.csv

```

Os dados são fictícios e utilizados exclusivamente para fins educacionais.

## 🛠️ Tecnologias

* Python
* Pandas
* Streamlit
* Google Gemini API
* Git e GitHub

## 📁 Estrutura do projeto

```text
dio-lab-bia-do-futuro/
│
├── data/
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   ├── produtos_financeiros.json
│   └── transacoes.csv
│
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
│
├── src/
│   ├── agente.py
│   ├── app.py
│   └── requirements.txt
│
├── assets/
├── examples/
└── README.md

```

## 🔐 Segurança e confiabilidade

O agente foi configurado para:

* utilizar somente informações disponíveis na base;
* não inventar dados;
* informar quando não houver informação suficiente;
* reconhecer perguntas fora do escopo;
* não realizar recomendações personalizadas de investimento.

## 📊 Avaliação

Foram definidos 10 casos de teste para avaliar:

* assertividade;
* segurança das respostas;
* coerência com a base de conhecimento;
* comportamento diante de informações inexistentes;
* comportamento diante de perguntas fora do escopo.

Os resultados são registrados em:
`docs/04-metricas.md`

## ▶️ Como executar

### 1. Instalar as dependências

```bash
pip install -r src/requirements.txt

```

### 2. Configurar a chave da API Gemini

Linux/macOS:

```bash
export GEMINI_API_KEY="SUA_CHAVE_AQUI"

```

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="SUA_CHAVE_AQUI"

```

### 3. Executar a aplicação

```bash
streamlit run src/app.py

```

A aplicação será aberta no navegador.

## ⚠️ Observação

Este projeto é um protótipo educacional.

Os dados são fictícios e a aplicação não possui acesso a contas bancárias reais. O FinanIA não substitui orientação profissional financeira.

```

```
