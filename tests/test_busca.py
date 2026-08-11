from app.rag import buscar_documentos


def test_busca_poda_arvore():
    documentos = buscar_documentos(
        "Quais documentos preciso para solicitar poda de uma árvore?"
    )

    assert len(documentos) > 0

    titulo_principal = documentos[0].metadata.get("titulo")

    assert titulo_principal == "Corte e Poda de Árvore"


def test_busca_retirada_entulho():
    documentos = buscar_documentos(
        "Fiz uma obra e preciso retirar o entulho."
    )

    assert len(documentos) > 0

    titulo_principal = documentos[0].metadata.get("titulo")

    assert titulo_principal == "Retirada de Entulhos"


def test_busca_castracao_animais():
    documentos = buscar_documentos(
        "Quero castrar meu cachorro. Como faço?"
    )

    assert len(documentos) > 0

    titulo_principal = documentos[0].metadata.get("titulo")

    assert titulo_principal == "Castração de Cães e Gatos"