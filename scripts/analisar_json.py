import json
from pathlib import Path

CAMINHO_JSON = Path("documents/carta_servicos.json")

with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

print("Tipo do conteúdo principal:", type(dados))
print("Quantidade de itens no nível principal:", len(dados))

print("\nTipos encontrados:")
for indice, item in enumerate(dados):
    print(indice, "-", item.get("type"))

# O terceiro item contém a tabela com os serviços
tabela = dados[2]

print("\nNome da tabela:", tabela.get("name"))

servicos = tabela.get("data", [])

print("Quantidade de serviços:", len(servicos))

if servicos:
    primeiro_servico = servicos[0]

    print("\nPrimeiro serviço:")
    print("ID:", primeiro_servico.get("id"))
    print("Título:", primeiro_servico.get("titulo"))
    print("Resumo:", primeiro_servico.get("resumo"))
    print("Prazo:", primeiro_servico.get("prazo"))
    print("Custo:", primeiro_servico.get("custo"))
    print("Unidade responsável:", primeiro_servico.get("unidade_responsavel"))