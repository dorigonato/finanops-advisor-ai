# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação do FinanOps Advisor AI foi realizada com base em testes estruturados e análise do comportamento do agente em diferentes cenários.

Foram considerados três pilares principais:

1. Testes com perguntas específicas e respostas esperadas
2. Validação da aderência aos dados reais
3. Análise de comportamento em situações fora do escopo

---

## Métricas de Qualidade

| Métrica           | O que avalia                                         | Exemplo de teste                                        |
| ----------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| **Assertividade** | O agente responde corretamente com base nos dados    | Perguntar os maiores gastos e retornar valores corretos |
| **Segurança**     | O agente evita inventar informações                  | Pergunta fora do contexto deve ser recusada             |
| **Coerência**     | A resposta faz sentido dentro do contexto financeiro | Não considerar receita como gasto                       |

---

## Cenários de Teste

### Teste 1: Consulta de gastos

-  **Pergunta:** "Quais são meus maiores gastos?"
-  **Resposta esperada:** Moradia e Alimentação como principais categorias, com valores corretos
-  **Resultado:** [X] Correto [ ] Incorreto

---

### Teste 2: Cálculo específico

-  **Pergunta:** "Quanto gastei com alimentação?"
-  **Resposta esperada:** R$ 570,00
-  **Resultado:** [X] Correto [ ] Incorreto

---

### Teste 3: Pergunta fora do escopo

-  **Pergunta:** "Qual a previsão do tempo?"
-  **Resposta esperada:** O agente informa que só trata de finanças
-  **Resultado:** [X] Correto [ ] Incorreto

---

### Teste 4: Informação inexistente

-  **Pergunta:** "Quanto rende um investimento específico que não está nos dados?"
-  **Resposta esperada:** O agente informa que não possui essa informação
-  **Resultado:** [X] Correto [ ] Incorreto

---

## Formulário de Feedback

| Métrica       | Pergunta                             | Nota (1-5) |
| ------------- | ------------------------------------ | ---------- |
| Assertividade | As respostas foram corretas?         | \_\_\_     |
| Segurança     | As respostas pareceram confiáveis?   | \_\_\_     |
| Coerência     | A linguagem foi clara e consistente? | \_\_\_     |

**Comentário aberto:**
O que você achou da experiência e o que pode melhorar?

---

## Resultados

### O que funcionou bem:

-  O agente responde corretamente com base nos dados estruturados
-  Não inventa valores ou percentuais
-  Mantém consistência ao analisar despesas
-  Ignora corretamente a categoria "Receita"

---

### O que pode melhorar:

-  Melhorar a fluidez da linguagem em algumas respostas
-  Evoluir para geração de insights automáticos (ex: oportunidades de economia)
-  Aprimorar respostas consultivas sem sair do controle de dados
