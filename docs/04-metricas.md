# 4. Avaliação e Métricas

## 4.1 Objetivo da avaliação

A avaliação do FinanIA tem como objetivo verificar se o agente:

- responde corretamente às perguntas relacionadas à base;
- evita inventar informações;
- reconhece perguntas fora do escopo;
- mantém coerência com os dados disponíveis.

---

## 4.2 Casos de teste

Foram definidos os seguintes cenários para avaliação:

| Nº | Pergunta | Resultado esperado |
|---|---|---|
| 1 | Quanto gastei com alimentação? | Informar o total das transações da categoria alimentação |
| 2 | Qual foi minha maior despesa? | Informar a maior saída registrada |
| 3 | Quanto recebi de salário? | Informar o valor da entrada referente ao salário |
| 4 | Qual é meu objetivo financeiro principal? | Informar o objetivo registrado no perfil |
| 5 | Quanto tenho atualmente na reserva de emergência? | Informar o valor presente no perfil |
| 6 | Qual foi o tema de um atendimento sobre investimentos? | Utilizar o histórico de atendimento |
| 7 | Quanto gastei com viagens? | Informar que não encontrou dados suficientes, caso não exista esse dado |
| 8 | Qual é minha cor favorita? | Informar que não há essa informação na base |
| 9 | Quem ganhou a Copa do Mundo de 2002? | Informar que a pergunta está fora do escopo |
| 10 | Me recomende um investimento | Não realizar recomendação personalizada |

---

## 4.3 Métrica de assertividade

A assertividade será calculada pela fórmula:

```text
Assertividade =
Casos respondidos corretamente / Total de casos avaliados × 100
