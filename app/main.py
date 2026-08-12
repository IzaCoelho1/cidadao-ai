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


# --------------------------------------------------
# Histórico da conversa
# --------------------------------------------------

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []


# --------------------------------------------------
# Exemplos de perguntas
# --------------------------------------------------

st.markdown("### 💡 Experimente uma pergunta")

coluna1, coluna2 = st.columns(2)

pergunta_exemplo = None

with coluna1:

    if st.button(
        "🌳 Árvore com cupim",
        use_container_width=True
    ):
        pergunta_exemplo = (
            "Tenho uma árvore com cupim no meu quintal. "
            "O que devo fazer?"
        )

    if st.button(
        "🗑️ Retirada de entulho",
        use_container_width=True
    ):
        pergunta_exemplo = (
            "Como faço para solicitar a retirada de entulho?"
        )


with coluna2:

    if st.button(
        "🐶 Castração de animais",
        use_container_width=True
    ):
        pergunta_exemplo = (
            "Como faço para solicitar a castração de um animal?"
        )

    if st.button(
        "✂️ Poda de árvore",
        use_container_width=True
    ):
        pergunta_exemplo = (
            "Quais documentos preciso para solicitar "
            "a poda de uma árvore?"
        )


st.divider()


# --------------------------------------------------
# Exibe mensagens anteriores
# --------------------------------------------------

for mensagem in st.session_state.mensagens:

    with st.chat_message(mensagem["papel"]):
        st.markdown(mensagem["conteudo"])


# --------------------------------------------------
# Campo para pergunta digitada
# --------------------------------------------------

pergunta_digitada = st.chat_input(
    "Digite sua pergunta sobre os serviços municipais..."
)


# A pergunta pode vir de um botão ou do campo de texto
pergunta = pergunta_exemplo or pergunta_digitada


# --------------------------------------------------
# Processa a pergunta
# --------------------------------------------------

if pergunta:

    # Salva a pergunta no histórico
    st.session_state.mensagens.append(
        {
            "papel": "user",
            "conteudo": pergunta
        }
    )

    # Mostra a pergunta
    with st.chat_message("user"):
        st.markdown(pergunta)


    # Gera a resposta
    with st.chat_message("assistant"):

        with st.spinner(
            "Consultando a Carta de Serviços..."
        ):

            try:

                resposta, documentos = responder(pergunta)

                st.markdown(resposta)

                # Evita mostrar uma fonte irrelevante
                # quando o agente informa que não encontrou
                # a resposta na Carta de Serviços.
                resposta_minuscula = resposta.lower()

                nao_encontrou = (
                    "não encontrei" in resposta_minuscula
                    or
                    "não foi possível encontrar" in resposta_minuscula
                )

                if documentos and not nao_encontrou:

                    fonte = documentos[0]

                    st.divider()

                    titulo = fonte.metadata.get(
                        "titulo",
                        "Serviço não informado"
                    )

                    unidade = fonte.metadata.get(
                        "unidade_responsavel",
                        "Unidade não informada"
                    )

                    st.caption(
                        "📚 Fonte principal: "
                        f"{titulo} — {unidade}"
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