from app.rag import responder


pergunta = "Fiz uma obra e preciso retirar o entulho. Como faço?"

resposta, documentos = responder(pergunta)


print("\nPERGUNTA:")
print(pergunta)


print("\nRESPOSTA DO CIDADÃO.AI:")
print(resposta)


print("\nFONTES CONSULTADAS:")

for documento in documentos:
    print(
        "-",
        documento.metadata.get("titulo"),
        "|",
        documento.metadata.get("unidade_responsavel")
    )