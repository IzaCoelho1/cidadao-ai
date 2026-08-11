import os
from dotenv import load_dotenv

load_dotenv()

chave = os.getenv("GOOGLE_API_KEY")

if chave:
    print("Chave da API encontrada com sucesso.")
else:
    print("Chave da API NÃO foi encontrada.")