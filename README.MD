# Cidadão.AI

Assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** para consulta à Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ.

O projeto permite que cidadãos façam perguntas em linguagem natural sobre serviços públicos municipais e recebam respostas baseadas nas informações oficiais disponíveis na Carta de Serviços.

## 🎯 Objetivo

O Cidadão.AI foi desenvolvido com o objetivo de facilitar o acesso às informações sobre serviços públicos municipais.

O sistema permite responder perguntas como:

- Quais documentos preciso para solicitar poda de uma árvore?
- Como solicitar a retirada de entulho?
- Quanto custa determinado serviço?
- Qual é o prazo para atendimento?
- Onde posso solicitar um serviço?
- Qual secretaria é responsável?

Quando uma informação não está disponível na Carta de Serviços, o agente informa que não encontrou a resposta, evitando gerar informações sem fundamento.

## 🧠 Como funciona

O projeto utiliza a arquitetura RAG (Retrieval-Augmented Generation).

O funcionamento ocorre, de forma simplificada, nas seguintes etapas:

1. Os dados da Carta de Serviços são carregados e processados.
2. Cada serviço é transformado em um documento para consulta.
3. Os documentos são convertidos em embeddings.
4. Os embeddings são armazenados em um banco vetorial ChromaDB.
5. A pergunta do cidadão também é transformada em uma representação vetorial.
6. O sistema realiza uma busca semântica para encontrar os serviços mais relacionados à pergunta.
7. Os documentos recuperados são enviados como contexto para o modelo Gemini.
8. O modelo gera uma resposta utilizando as informações recuperadas.

## 🏗️ Arquitetura

```text
Carta de Serviços
      ↓
Processamento dos dados
      ↓
Documentos LangChain
      ↓
Embeddings
      ↓
ChromaDB
      ↓
Busca semântica
      ↓
Contexto recuperado
      ↓
Gemini
      ↓
Resposta ao cidadão
      ↓
Interface Streamlit
```

## 🛠️ Tecnologias utilizadas

- Python
- Pandas
- LangChain
- Google Gemini
- Google Generative AI Embeddings
- ChromaDB
- Streamlit
- Pytest
- Git e GitHub

## 📂 Estrutura do projeto

```text
cidadao-ai/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── rag.py
│
├── data/
│   └── servicos_processados.json
│
├── documents/
│   ├── carta_de_servicos.pdf
│   └── carta_servicos.json
│
├── scripts/
│   ├── analisar_json.py
│   ├── analisar_dados_pandas.py
│   ├── criar_documentos.py
│   ├── criar_banco_vetorial.py
│   ├── ler_pdf.py
│   ├── testar_busca.py
│   ├── testar_embeddings.py
│   ├── testar_gemini.py
│   ├── testar_rag.py
│   └── testes_agente.py
│
├── tests/
│   └── test_busca.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 📊 Base de conhecimento

A base utilizada pelo agente é composta pela Carta de Serviços da Prefeitura Municipal de Pinheiral.

Atualmente, o conjunto de dados processado contém **138 serviços públicos municipais**.

Entre as informações disponíveis estão:

- título do serviço;
- descrição;
- público-alvo;
- documentos necessários;
- etapas;
- prazo;
- custo;
- canais de atendimento;
- unidade responsável;
- contato;
- legislação;
- palavras-chave.

## 🔎 Exemplo de utilização

Pergunta:

> Quais documentos preciso para solicitar poda de uma árvore?

O agente recupera o serviço **Corte e Poda de Árvore** e utiliza as informações encontradas na Carta de Serviços para elaborar a resposta.

Outro exemplo:

> Qual é o salário do prefeito de Pinheiral?

Como essa informação não está disponível na Carta de Serviços, o agente informa que não encontrou a informação na base consultada.

## 🧪 Testes

O projeto possui testes automatizados com Pytest para verificar a recuperação semântica dos serviços.

Para executar:

```bash
python -m pytest -v
```

Os testes verificam consultas relacionadas a serviços como:

- poda de árvores;
- retirada de entulho;
- castração de animais.

## ▶️ Executando o projeto

Com o ambiente virtual ativado, instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e configure a chave da API necessária para utilização do Gemini.

Depois execute a aplicação:

```bash
streamlit run app/main.py
```

A aplicação poderá ser acessada localmente pelo navegador.

## 🔐 Segurança

Chaves de API e outras informações sensíveis não são armazenadas no repositório.

O arquivo `.env` está incluído no `.gitignore`.

## 👩‍💻 Autoria

Projeto desenvolvido como parte de um desafio de Inteligência Artificial utilizando arquitetura RAG para facilitar o acesso dos cidadãos às informações sobre serviços públicos municipais.