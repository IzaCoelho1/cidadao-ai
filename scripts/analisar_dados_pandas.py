import json
from pathlib import Path

import pandas as pd


CAMINHO_JSON = Path("documents/carta_servicos.json")


with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


# A exportação do phpMyAdmin possui:
# 0 = header
# 1 = database
# 2 = table
servicos = dados[2]["data"]


# Transforma os registros em uma tabela do Pandas
df = pd.DataFrame(servicos)


print("Quantidade total de serviços:", len(df))
print("Quantidade de colunas:", len(df.columns))


print("\nColunas disponíveis:")
for coluna in df.columns:
    print("-", coluna)


# Mantém somente serviços publicados
df_publicados = df[df["status"] == "publicado"].copy()


print("\nServiços publicados:", len(df_publicados))


print("\nServiços por unidade responsável:")
print(
    df_publicados["unidade_responsavel"]
    .value_counts()
    .to_string()
)


print("\nCampos sem informação:")
print(
    df_publicados[
        [
            "requisitos",
            "documentos",
            "etapas",
            "prazo",
            "custo",
            "legislacao"
        ]
    ]
    .isna()
    .sum()
    .to_string()
)