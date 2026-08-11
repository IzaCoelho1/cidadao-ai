import streamlit as st

from rag import responder


st.set_page_config(
    page_title="Cidadão.AI",
    page_icon="🏛️",
    layout="centered"
)


st.title("🏛️ Cidadão.AI")

st.subheader(
    "Assistente Inteligente da Carta de Serviços de Pinheiral"
)

st.write(
    """
    Faça perguntas sobre os serviços oferecidos pela
    Prefeitura Municipal de Pinheiral.

    As respostas são geradas com base nas informações
    disponíveis na Carta de Serviços.
    """
)


# Histórico da conversa
if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# Exibe mensagens anteriores
for mensagem in st.session_state.mensagens:
    with st.chat_message(mensagem["papel"]):
        st.markdown(mensagem["conteudo"])


# Campo onde o cidadão digita a pergunta
pergunta = st.chat_input(
    "Digite sua pergunta sobre os serviços municipais..."
)


if pergunta:

    # Mostra pergunta do usuário
    st.session_state.mensagens.append(
        {
            "papel": "user",
            "conteudo": pergunta
        }
    )

    with st.chat_message("user"):
        st.markdown(pergunta)


    # Gera resposta
    with st.chat_message("assistant"):

        with st.spinner("Consultando a Carta de Serviços..."):

            try:
                resposta, documentos = responder(pergunta)

                st.markdown(resposta)

                # Fonte principal
                if documentos:

                    fonte = documentos[0]

                    st.divider()

                    st.caption(
                        "📚 Fonte principal: "
                        f"{fonte.metadata.get('titulo')} — "
                        f"{fonte.metadata.get('unidade_responsavel')}"
                    )

            except Exception as erro:

                resposta = (
                    "Não foi possível consultar a Carta de Serviços "
                    "neste momento. Tente novamente em instantes."
                )

                st.error(resposta)

                print("Erro:", erro)


    # Salva a resposta no histórico
    st.session_state.mensagens.append(
        {
            "papel": "assistant",
            "conteudo": resposta
        }
    )