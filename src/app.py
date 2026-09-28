import os

import streamlit as st

from agente import responder


st.set_page_config(
    page_title="FinanIA",
    page_icon="💰",
    layout="centered",
)


st.title("💰 FinanIA")
st.subheader("Assistente Inteligente de Organização Financeira")

st.write(
    "Faça perguntas sobre as informações financeiras disponíveis "
    "na base de conhecimento do projeto."
)

st.info(
    "Os dados utilizados são fictícios e foram disponibilizados "
    "para fins educacionais."
)


if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                "Olá! Eu sou o FinanIA. 👋\n\n"
                "Posso ajudar você a consultar informações sobre "
                "transações, gastos, metas, perfil financeiro e "
                "histórico de atendimento."
            ),
        }
    ]


for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["role"]):
        st.markdown(mensagem["content"])


pergunta = st.chat_input(
    "Ex.: Quanto gastei com alimentação?"
)


if pergunta:
    st.session_state.mensagens.append(
        {
            "role": "user",
            "content": pergunta,
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)

    api_key = os.getenv("GEMINI_API_KEY")

    with st.chat_message("assistant"):
        with st.spinner("Consultando a base de conhecimento..."):
            try:
                resposta = responder(pergunta, api_key)
            except Exception as erro:
                resposta = (
                    "Não foi possível processar a pergunta no momento. "
                    f"Verifique a configuração da aplicação. "
                    f"Detalhe técnico: {erro}"
                )

        st.markdown(resposta)

    st.session_state.mensagens.append(
        {
            "role": "assistant",
            "content": resposta,
        }
    )


with st.sidebar:
    st.header("Sobre o projeto")

    st.write(
        "O FinanIA é um protótipo desenvolvido para o Lab "
        "\"Construa Seu Assistente Virtual com Inteligência Artificial\" "
        "da DIO."
    )

    st.write("**Tecnologias:**")
    st.write("- Python")
    st.write("- Pandas")
    st.write("- Streamlit")
    st.write("- Google Gemini API")

    st.divider()

    st.caption(
        "Projeto educacional com dados fictícios."
    )
