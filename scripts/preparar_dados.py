import json
from pathlib import Path

CAMINHO_JSON = Path("documents/carta_servicos.json")
CAMINHO_SAIDA = Path("data/servicos_processados.json")


with open(CAMINHO_JSON, "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)


# Os serviços estão no terceiro item da exportação do phpMyAdmin
servicos = dados[2]["data"]

servicos_processados = []


for servico in servicos:
    if servico.get("status") != "publicado":
        continue

    texto = f"""
SERVIÇO: {servico.get("titulo", "")}

RESUMO:
{servico.get("resumo", "")}

DESCRIÇÃO:
{servico.get("descricao", "")}

PÚBLICO-ALVO:
{servico.get("publico_alvo", "")}

REQUISITOS:
{servico.get("requisitos") or "Não informado"}

DOCUMENTOS NECESSÁRIOS:
{servico.get("documentos") or "Não informado"}

ETAPAS:
{servico.get("etapas") or "Não informado"}

PRAZO:
{servico.get("prazo") or "Não informado"}

CUSTO:
{servico.get("custo") or "Não informado"}

CANAIS DE ATENDIMENTO:
{servico.get("canais") or "Não informado"}

UNIDADE RESPONSÁVEL:
{servico.get("unidade_responsavel") or "Não informado"}

CONTATO:
{servico.get("contato") or "Não informado"}

LEGISLAÇÃO:
{servico.get("legislacao") or "Não informado"}

PALAVRAS-CHAVE:
{servico.get("palavras_chave") or "Não informado"}
""".strip()

    servicos_processados.append(
        {
            "id": servico.get("id"),
            "titulo": servico.get("titulo"),
            "texto": texto,
            "metadata": {
                "id": servico.get("id"),
                "titulo": servico.get("titulo"),
                "slug": servico.get("slug"),
                "unidade_responsavel": servico.get("unidade_responsavel"),
                "publico_alvo": servico.get("publico_alvo"),
                "status": servico.get("status"),
                "updated_at": servico.get("updated_at"),
            },
        }
    )


CAMINHO_SAIDA.parent.mkdir(parents=True, exist_ok=True)

with open(CAMINHO_SAIDA, "w", encoding="utf-8") as arquivo:
    json.dump(
        servicos_processados,
        arquivo,
        ensure_ascii=False,
        indent=2
    )


print("Processamento concluído.")
print("Serviços processados:", len(servicos_processados))
print("Arquivo gerado:", CAMINHO_SAIDA)