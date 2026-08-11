from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

texto = "Solicitação de retirada de entulhos após uma obra."

vetor = embeddings.embed_query(texto)

print("Embedding gerado com sucesso.")
print("Quantidade de dimensões:", len(vetor))
print("Primeiros valores:", vetor[:5])