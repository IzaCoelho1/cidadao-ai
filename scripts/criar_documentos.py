import json
from pathlib import Path
from langchain_core.documents import Document

CAMINHO_DADOS = Path("data/servicos_processados.json")

with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
    servicos = json.load(arquivo)

documentos = []

for servico in servicos:
    documento = Document(
        page_content=servico["texto"],
        metadata=servico["metadata"]
    )

    documentos.append(documento)

print("Quantidade de documentos criados:", len(documentos))

if documentos:
    print("\nPrimeiro documento:")
    print(documentos[0])

    print("\nConteúdo:")
    print(documentos[0].page_content)

    print("\nMetadados:")
    print(documentos[0].metadata)