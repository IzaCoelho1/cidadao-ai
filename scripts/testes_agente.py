from app.rag import responder


perguntas = [
    "Quais documentos preciso para solicitar poda de uma árvore?",
    "Fiz uma obra e preciso retirar o entulho. Como faço?",
    "Quanto custa a retirada de entulho e qual é o prazo?",
    "Qual é o salário do prefeito de Pinheiral?"
]


for numero, pergunta in enumerate(perguntas, start=1):

    print("\n" + "=" * 80)
    print(f"TESTE {numero}")
    print("=" * 80)

    print("\nPERGUNTA:")
    print(pergunta)

    resposta, documentos = responder(pergunta)

    print("\nRESPOSTA:")
    print(resposta)

    print("\nFONTES RECUPERADAS:")

    for documento in documentos:
        titulo = documento.metadata.get("titulo", "Não informado")
        unidade = documento.metadata.get(
            "unidade_responsavel",
            "Não informado"
        )

        print(f"- {titulo} | {unidade}")