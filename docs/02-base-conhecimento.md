# 2. Base de Conhecimento

## 2.1 Objetivo

A base de conhecimento do FinanIA reúne informações financeiras fictícias utilizadas pelo agente para responder às perguntas da pessoa usuária.

Os dados foram disponibilizados no repositório do Lab da DIO e são utilizados exclusivamente para fins educacionais.

---

## 2.2 Fontes de dados

### transacoes.csv

Contém o histórico de movimentações financeiras.

Principais campos:

| Campo | Descrição |
|---|---|
| data | Data da movimentação |
| descricao | Descrição da movimentação |
| categoria | Categoria financeira |
| valor | Valor da movimentação |
| tipo | Entrada ou saída |

Exemplos de categorias presentes:

- receita;
- moradia;
- alimentação;
- lazer;
- saúde;
- transporte.

---

### historico_atendimento.csv

Contém informações sobre atendimentos anteriores.

Principais campos:

| Campo | Descrição |
|---|---|
| data | Data do atendimento |
| canal | Canal utilizado |
| tema | Tema do atendimento |
| resumo | Resumo da solicitação |
| resolvido | Indica se o atendimento foi resolvido |

---

### perfil_investidor.json

Contém informações sobre o perfil financeiro utilizado no cenário fictício.

Entre as informações disponíveis estão:

- renda mensal;
- perfil de investidor;
- objetivo principal;
- patrimônio;
- reserva de emergência;
- metas financeiras;
- prazo das metas.

---

### produtos_financeiros.json

Contém os produtos financeiros disponíveis na base de conhecimento.

Entre as informações estão:

- nome do produto;
- categoria;
- risco;
- rentabilidade informada na base;
- aporte mínimo;
- público indicado na base.

---

## 2.3 Estratégia de utilização

A aplicação carrega os arquivos e transforma suas informações em um contexto estruturado para o modelo de Inteligência Artificial.

O modelo recebe:

1. as instruções de comportamento;
2. as informações disponíveis na base;
3. a pergunta feita pela pessoa usuária.

A resposta deve ser produzida com base nesse contexto.

---

## 2.4 Princípio de confiabilidade

A principal regra da base de conhecimento é:

> Se a informação não estiver disponível na base, o agente deve informar que não possui dados suficientes para responder.

Essa regra ajuda a reduzir respostas inventadas e facilita a avaliação do comportamento do agente.

---

## 2.5 Dados fictícios

Nenhuma informação pessoal real é utilizada no projeto.

Os dados disponíveis no repositório são dados mockados para fins de aprendizagem e desenvolvimento do protótipo.

---

## 2.6 Fluxo dos dados

```text
Arquivos CSV/JSON
       ↓
Python + Pandas/JSON
       ↓
Contexto estruturado
       ↓
Prompt do agente
       ↓
Modelo Gemini
       ↓
Resposta ao usuário
