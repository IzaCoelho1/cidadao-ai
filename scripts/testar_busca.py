from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

banco = Chroma(
    collection_name="carta_servicos",
    embedding_function=embeddings,
    persist_directory="data/chroma"
)

pergunta = "Fiz uma obra e preciso retirar o entulho. Como faço?"

resultados = banco.similarity_search(
    pergunta,
    k=3
)

print("\nPergunta:")
print(pergunta)

print("\nResultados encontrados:")

for indice, documento in enumerate(resultados, start=1):
    print("\n" + "=" * 60)
    print(f"RESULTADO {indice}")
    print("Título:", documento.metadata.get("titulo"))
    print("Unidade responsável:", documento.metadata.get("unidade_responsavel"))
    print("\nConteúdo:")
    print(documento.page_content)