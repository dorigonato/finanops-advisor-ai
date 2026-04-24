## ▶️ Passo a Passo de Execução

Siga as etapas abaixo para executar o projeto localmente:

### 1. Clone o repositório

```bash
git clone https://github.com/dorigonato/finanops-advisor-ai.git
cd finanops-advisor-ai

```

### 2. Crie e ative um ambiente virtual (opcional, recomendado)

python -m venv venv

Ativar no Windows:
venv\Scripts\activate

Ativar no Linux/Mac:
source venv/bin/activate

### 3. Instale as dependências

pip install -r requirements.txt

Caso não exista o arquivo, instale manualmente:
pip install streamlit pandas requests

### 4. Instale e execute o Ollama

Baixe e instale o Ollama:
https://ollama.com/

Após a instalação, execute o modelo:
ollama run llama3

⚠️ Esse passo é obrigatório para o funcionamento do agente.

### 5. Execute a aplicação

streamlit run src/app.py

### 6. Acesse no navegador

http://localhost:8501

### 7. Teste o agente

Exemplos de perguntas:

"Quais são meus maiores gastos?"
"Quanto gastei com alimentação?"
"Como posso melhorar minha organização financeira?"

⚙️ Observações importantes

-  O agente utiliza um modelo local via Ollama (sem custo de API)
-  Os dados estão na pasta /data
-  O sistema foi projetado para evitar alucinações, utilizando:
   -  cálculo no backend (Python)
   -  interpretação via LLM

🧠 Estrutura do Projeto

finanops-advisor-ai/
│
├── data/ # Base de dados (perfil, transações, produtos)
├── docs/ # Documentação das etapas
├── src/ # Código da aplicação
│ └── app.py
├── README.md
