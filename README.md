# 💰 FinanIA — Assistente Inteligente de Organização Financeira

Projeto desenvolvido para o Lab **"Construa Seu Assistente Virtual com Inteligência Artificial"** da Digital Innovation One (DIO).

O FinanIA é um assistente virtual desenvolvido em Python que utiliza a API do Google Gemini para responder perguntas em linguagem natural sobre informações financeiras fictícias presentes em uma base de conhecimento.

## 🎯 Objetivo

O objetivo do projeto é demonstrar a construção de um assistente virtual capaz de consultar, interpretar e explicar informações presentes em uma base de conhecimento.

O FinanIA pode auxiliar na consulta de:

- transações;
- gastos;
- receitas;
- metas financeiras;
- perfil financeiro;
- histórico de atendimento;
- produtos financeiros disponíveis na base.

## 🤖 Exemplos de perguntas

```text
Quanto gastei com alimentação?

Quais são meus maiores gastos?

Quanto recebi de salário?

Qual é meu objetivo financeiro principal?

Quanto tenho atualmente na reserva de emergência?

Quais produtos financeiros estão disponíveis?
````

O assistente também foi configurado para informar quando uma informação não está disponível na base ou quando uma pergunta está fora do escopo da aplicação.

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

O projeto utiliza dados fictícios para fins educacionais:

```text
data/
├── historico_atendimento.csv
├── perfil_investidor.json
├── produtos_financeiros.json
└── transacoes.csv
```

A aplicação utiliza esses arquivos como fonte de informações sobre o perfil e o histórico financeiro apresentado ao assistente.

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
├── src/
│   ├── agente.py
│   ├── app.py
│   └── requirements.txt
│
└── README.md
```

## 🔐 Segurança e confiabilidade

O agente foi configurado para:

* utilizar somente informações disponíveis na base de conhecimento;
* não inventar dados;
* informar quando não houver informação suficiente;
* reconhecer perguntas fora do escopo;
* não realizar recomendações personalizadas de investimento.

A chave da API Gemini deve ser configurada por meio da variável de ambiente `GEMINI_API_KEY` e não deve ser armazenada no código ou no repositório.

## 🧪 Testes realizados

Durante a validação da aplicação, foram testadas perguntas relacionadas a:

* gastos com alimentação;
* maiores gastos;
* perfil financeiro;
* produtos financeiros;
* histórico de atendimento;
* perguntas sobre informações que não estão presentes na base.

Também foi verificado o comportamento do assistente diante de uma pergunta fora do escopo, que resultou em uma resposta informando que não havia dados suficientes para respondê-la.

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

A aplicação será disponibilizada no navegador pelo Streamlit.

## ⚠️ Observação

Este projeto é um protótipo educacional.

Os dados utilizados são fictícios e a aplicação não possui acesso a contas bancárias reais. O FinanIA não substitui orientação profissional financeira.
