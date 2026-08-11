from pathlib import Path
from pypdf import PdfReader


CAMINHO_PDF = Path("documents/carta_de_servicos.pdf")


reader = PdfReader(CAMINHO_PDF)

print("Carta de Serviços carregada com sucesso.")
print("Quantidade de páginas:", len(reader.pages))


# Exibe somente um pequeno trecho da primeira página
primeira_pagina = reader.pages[0]
texto = primeira_pagina.extract_text() or ""

print("\nTrecho da primeira página:")
print(texto[:1000])