import streamlit as st
import pandas as pd
import json
import requests
import os

# =========================
# CONFIGURAÇÃO DE CAMINHOS
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data")

# =========================
# CARREGAR DADOS
# =========================

def carregar_dados():
    try:
        with open(os.path.join(DATA_PATH, "perfil_investidor.json"), "r", encoding="utf-8") as f:
            perfil = json.load(f)

        historico = pd.read_csv(os.path.join(DATA_PATH, "historico_atendimento.csv"))
        transacoes = pd.read_csv(os.path.join(DATA_PATH, "transacoes.csv"))

        with open(os.path.join(DATA_PATH, "produtos_financeiros.json"), "r", encoding="utf-8") as f:
            produtos = json.load(f)

        return perfil, historico, transacoes, produtos

    except Exception as e:
        st.error(f"Erro ao carregar dados: {e}")
        return None, None, None, None


# =========================
# PROCESSAMENTO DE DADOS
# =========================

def calcular_resumo(transacoes):
    try:
        df = transacoes.copy()

        # Garantir que valor é numérico
        df["valor"] = (
            df["valor"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        # 🔥 EXCLUIR RECEITA EXPLICITAMENTE
        df = df[df["categoria"].str.lower() != "receita"]

        # Trabalhar apenas com despesas
        df["valor"] = df["valor"].abs()

        resumo = (
            df.groupby("categoria")["valor"]
            .sum()
            .sort_values(ascending=False)
        )

        total = resumo.sum()

        percentual = (resumo / total) * 100

        df_resumo = pd.DataFrame({
            "total": resumo,
            "percentual (%)": percentual.round(2)
        })

        return df_resumo, total

    except Exception as e:
        st.error(f"Erro ao processar transações: {e}")
        return None, None


# =========================
# MONTAR CONTEXTO
# =========================

def montar_contexto(perfil, historico, transacoes, produtos):
    resumo_df, total = calcular_resumo(transacoes)

    contexto = f"""
Perfil do cliente:
{json.dumps(perfil, indent=2, ensure_ascii=False)}

Resumo de gastos por categoria (dados oficiais):
{resumo_df.to_string()}

Total de gastos:
{total}

IMPORTANTE:
- Apenas despesas foram consideradas
- Valores já tratados (positivos)
- Percentuais já calculados
- NÃO recalcular

Histórico de interações:
{historico.head(10).to_string(index=False)}

Produtos financeiros:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""
    return contexto


# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
Você é o Finan, um assistente financeiro analítico, consultivo e confiável.

Seu objetivo é ajudar o usuário a entender seus gastos com base EXCLUSIVA nos dados fornecidos.

========================
REGRAS OBRIGATÓRIAS
========================

- Utilize SOMENTE as informações presentes no contexto
- NÃO invente valores, percentuais ou categorias
- NÃO faça estimativas ou aproximações
- NÃO recalcular números já fornecidos
- NÃO incluir receitas na análise de gastos
- NÃO criar conclusões que não estejam diretamente suportadas pelos dados
- Se não houver dados suficientes, informe claramente

========================
INTERPRETAÇÃO DOS DADOS
========================

- Os valores e percentuais já foram previamente calculados
- Considere apenas o resumo de despesas fornecido
- Identifique os maiores gastos com base nos valores apresentados
- Não altere, reordene ou recompute os dados

========================
FORMATO DA RESPOSTA
========================

- Comece direto com a análise (evitar introduções longas)
- Liste os principais gastos em ordem decrescente
- Apresente sempre:
  - Categoria
  - Valor total
  - Percentual (%)
- Utilize linguagem clara, objetiva e profissional
- Evite explicações desnecessárias

========================
LIMITAÇÕES
========================

- Não fornecer recomendações de investimento
- Não substituir um consultor financeiro
- Não responder perguntas fora do contexto financeiro
- Não responder perguntas sem dados suficientes

========================
COMPORTAMENTO
========================

- Seja direto, analítico e confiável
- Priorize precisão em vez de criatividade
- Evite frases genéricas ou motivacionais
- Não personalize excessivamente (evitar informalidade)

"""

# =========================
# CHAMADA AO MODELO
# =========================

def perguntar_llm(pergunta, contexto):
    url = "http://localhost:11434/api/generate"

    prompt = f"""
{SYSTEM_PROMPT}

Contexto:
{contexto}

Pergunta:
{pergunta}
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return response.json().get("response", "Erro ao obter resposta.")
        else:
            return f"Erro na API: {response.status_code}"

    except requests.exceptions.ConnectionError:
        return "Erro: Ollama não está rodando. Execute 'ollama run llama3'."

    except Exception as e:
        return f"Erro inesperado: {e}"


# =========================
# INTERFACE STREAMLIT
# =========================

st.set_page_config(page_title="FinanOps Advisor AI", layout="centered")

st.title("💰 FinanOps Advisor AI")
st.caption("Assistente financeiro baseado em dados reais")

perfil, historico, transacoes, produtos = carregar_dados()

if perfil is None:
    st.stop()

contexto = montar_contexto(perfil, historico, transacoes, produtos)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta financeira...")

if pergunta:
    st.session_state.messages.append({"role": "user", "content": pergunta})

    with st.chat_message("user"):
        st.markdown(pergunta)

    resposta = perguntar_llm(pergunta, contexto)

    with st.chat_message("assistant"):
        st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})