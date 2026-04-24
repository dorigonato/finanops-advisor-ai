# 💰 FinanOps Advisor AI

Assistente financeiro inteligente baseado em dados reais, desenvolvido com IA generativa.

---

## 📌 Sobre o Projeto

O **FinanOps Advisor AI** é um agente financeiro que ajuda usuários a entender e organizar suas finanças pessoais a partir de dados reais.

A solução analisa receitas e despesas e transforma essas informações em insights claros, objetivos e confiáveis.

---

## 🎯 Problema

Muitas pessoas não têm clareza sobre como utilizam seu dinheiro no dia a dia.

Mesmo com acesso a extratos bancários, falta uma visão consolidada dos gastos, dificultando o controle financeiro e a tomada de decisão.

---

## 🚀 Solução

O projeto utiliza:

-  Processamento de dados no backend (Python)
-  Inteligência artificial para interpretação (LLM)
-  Interface interativa com Streamlit

O agente responde perguntas financeiras com base em dados estruturados, garantindo maior precisão e evitando respostas incorretas.

---

## ⚙️ Tecnologias Utilizadas

-  Python
-  Streamlit
-  Pandas
-  Ollama (LLM local)
-  Requests

---

## 🧠 Como Funciona

1. Os dados do usuário são carregados da pasta `/data`
2. O backend processa e organiza as informações
3. Um contexto estruturado é enviado ao modelo de IA
4. O agente responde com base exclusivamente nos dados

---

## 📂 Estrutura do Projeto

finanops-advisor-ai/
│

├── data/ # Base de dados (perfil, transações, produtos)

├── docs/ # Documentação das etapas do projeto

├── src/ # Código da aplicação

│ └── app.py

├── README.md

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/dorigonato/finanops-advisor-ai.git
cd finanops-advisor-ai

```

### 2. Instale as dependências

pip install streamlit pandas requests

### 3. Instale e execute o Ollama

Baixe em:
https://ollama.com/

Execute um modelo local:

ollama run llama3

### 4. Execute a aplicação

streamlit run src/app.py

### 5. Acesse no navegador

http://localhost:8501

💬 Exemplos de Uso
"Quais são meus maiores gastos?"
"Quanto gastei com alimentação?"
"Como posso melhorar minha organização financeira?"

🔒 Segurança e Confiabilidade
Não inventa informações
Utiliza apenas dados reais
Evita alucinações da IA
Processamento híbrido (backend + LLM)

📊 Métricas

O agente foi avaliado com base em:

Assertividade
Coerência
Segurança (não gerar informações incorretas)

🚧 Limitações
Não recomenda investimentos
Depende dos dados fornecidos
Modelo local pode ser mais lento

💡 Diferenciais
Execução 100% local (sem custo de API)
Privacidade dos dados
Separação entre cálculo e interpretação
Respostas baseadas em dados reais

📌 Autor

Projeto desenvolvido por Dorival Rigonato Junior
