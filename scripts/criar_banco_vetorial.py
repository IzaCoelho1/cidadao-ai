import json
import time
from pathlib import Path

from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

CAMINHO_DADOS = Path("data/servicos_processados.json")
CAMINHO_BANCO = "data/chroma"

TAMANHO_LOTE = 20
PAUSA_ENTRE_LOTES = 25


with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
    servicos = json.load(arquivo)


documentos = []

for servico in servicos:
    documento = Document(
        page_content=servico["texto"],
        metadata=servico["metadata"]
    )
    documentos.append(documento)


print(f"Documentos carregados: {len(documentos)}")


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)


banco = Chroma(
    collection_name="carta_servicos",
    embedding_function=embeddings,
    persist_directory=CAMINHO_BANCO
)


quantidade_existente = banco._collection.count()

print(f"Documentos já existentes no banco: {quantidade_existente}")


documentos_restantes = documentos[quantidade_existente:]


for inicio in range(0, len(documentos_restantes), TAMANHO_LOTE):

    fim = inicio + TAMANHO_LOTE
    lote = documentos_restantes[inicio:fim]

    numero_inicial = quantidade_existente + inicio + 1
    numero_final = quantidade_existente + min(
        fim,
        len(documentos_restantes)
    )

    print(
        f"\nProcessando documentos "
        f"{numero_inicial} até {numero_final}..."
    )

    banco.add_documents(lote)

    print("Lote processado com sucesso.")

    if fim < len(documentos_restantes):
        print(
            f"Aguardando {PAUSA_ENTRE_LOTES} segundos..."
        )
        time.sleep(PAUSA_ENTRE_LOTES)


print("\nBanco vetorial criado com sucesso.")
print(f"Documentos armazenados: {banco._collection.count()}")
print(f"Local: {CAMINHO_BANCO}")