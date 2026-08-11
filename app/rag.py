from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)

load_dotenv()


# Configuração dos embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)


# Carrega o banco vetorial já criado
banco = Chroma(
    collection_name="carta_servicos",
    embedding_function=embeddings,
    persist_directory="data/chroma"
)


# Configuração do modelo de linguagem
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


def buscar_documentos(pergunta, quantidade=3):
    """Busca os serviços mais relacionados à pergunta."""

    documentos = banco.similarity_search(
        pergunta,
        k=quantidade
    )

    return documentos


def responder(pergunta):
    """Responde usando somente informações recuperadas da Carta de Serviços."""

    documentos = buscar_documentos(pergunta)

    contexto = "\n\n---\n\n".join(
        documento.page_content
        for documento in documentos
    )

    prompt = f"""
Você é o Cidadão.AI, um assistente virtual especializado na
Carta de Serviços da Prefeitura Municipal de Pinheiral.

Sua função é orientar cidadãos sobre os serviços públicos municipais.

REGRAS IMPORTANTES:

- Responda somente com base no CONTEXTO fornecido.
- Não invente informações.
- Se a resposta não estiver presente no contexto, informe claramente
  que não encontrou essa informação na Carta de Serviços.
- Responda em português do Brasil.
- Utilize linguagem simples, educada e objetiva.
- Quando disponível, informe documentos necessários, etapas, prazo,
  custo, canais de atendimento e unidade responsável.
- Não diga que realizou solicitações ou procedimentos em nome do cidadão.

PERGUNTA DO CIDADÃO:

{pergunta}

CONTEXTO DA CARTA DE SERVIÇOS:

{contexto}

Responda à pergunta do cidadão utilizando apenas as informações acima.
"""

    resposta = llm.invoke(prompt)

    if isinstance(resposta.content, str):
        texto_resposta = resposta.content
    else:
        partes_texto = []

        for bloco in resposta.content:
            if isinstance(bloco, dict) and bloco.get("type") == "text":
                partes_texto.append(bloco.get("text", ""))

        texto_resposta = "\n".join(partes_texto)

    return texto_resposta, documentos