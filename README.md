# 🤖 Cidadão.AI

Assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** para consulta à Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ.

O projeto permite que cidadãos façam perguntas em linguagem natural sobre serviços públicos municipais e recebam respostas baseadas nas informações oficiais disponíveis na Carta de Serviços.

---

## 🎯 Objetivo

O Cidadão.AI foi desenvolvido com o objetivo de facilitar o acesso às informações sobre serviços públicos municipais.

O sistema permite responder perguntas como:

- Quais documentos preciso para solicitar poda de uma árvore?
- Como solicitar a retirada de entulho?
- Quanto custa determinado serviço?
- Qual é o prazo para atendimento?
- Onde posso solicitar um serviço?
- Qual secretaria é responsável?

Quando uma informação não está disponível na Carta de Serviços, o agente informa que não encontrou a resposta na base consultada, evitando gerar informações sem fundamento.

---

## 🧠 Como funciona

O projeto utiliza a arquitetura **RAG (Retrieval-Augmented Generation)**.

O funcionamento ocorre, de forma simplificada, nas seguintes etapas:

1. Os dados da Carta de Serviços são carregados e processados.
2. Cada serviço é transformado em um documento para consulta.
3. Os documentos são convertidos em embeddings.
4. Os embeddings são armazenados no banco vetorial ChromaDB.
5. A pergunta do cidadão também é convertida em uma representação vetorial.
6. O sistema realiza uma busca semântica para encontrar os serviços mais relacionados à pergunta.
7. Os documentos recuperados são utilizados como contexto para o modelo Gemini.
8. O modelo gera uma resposta utilizando as informações recuperadas da Carta de Serviços.

---

## 🏗️ Arquitetura RAG

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
Google Gemini
        ↓
Resposta ao cidadão
        ↓
Interface Streamlit
```

---

## 🛠️ Tecnologias utilizadas

O projeto utiliza as seguintes tecnologias:

- Python
- LangChain
- LangChain Chroma
- Google Gemini
- Google Generative AI Embeddings
- ChromaDB
- Streamlit
- Python Dotenv
- Pandas
- PyPDF
- Pytest
- Git
- GitHub
- Podman
- systemd / Quadlet
- Oracle Cloud Infrastructure (OCI)
- Oracle Linux 9

> Pandas, PyPDF e Pytest são utilizados em etapas auxiliares de desenvolvimento, processamento e testes. O ambiente de produção utiliza um conjunto reduzido de dependências.

---

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
│   ├── preparar_dados.py
│   ├── testar_busca.py
│   ├── testar_embeddings.py
│   ├── testar_gemini.py
│   ├── testar_rag.py
│   └── testes_agente.py
│
├── tests/
│   └── test_busca.py
│
├── .dockerignore
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## 📊 Base de conhecimento

A base utilizada pelo agente é composta pela **Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ**.

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

Essas informações são utilizadas pelo mecanismo de busca semântica para recuperar os serviços mais relacionados à pergunta realizada pelo cidadão.

---

## 🔎 Exemplo de utilização

### Pergunta relacionada à base

> Tem uma árvore com cupim no meu quintal, e agora?

O agente identifica semanticamente o serviço relacionado a **Corte e Poda de Árvore** e utiliza as informações disponíveis na Carta de Serviços para apresentar orientações, documentos necessários, etapas, prazo, custo e canais de atendimento.

### Pergunta cuja informação não está disponível

> Qual é o nome do prefeito?

Caso essa informação não esteja presente na Carta de Serviços utilizada como base de conhecimento, o agente informa que não encontrou a resposta.

### Pergunta fora do domínio

> Quantas Copas do Mundo o Brasil tem?

O agente não utiliza conhecimento externo para responder e informa que essa informação não está disponível na Carta de Serviços.

Esse comportamento ajuda a manter as respostas vinculadas à base oficial utilizada pelo sistema.

---

## 🧪 Testes

O projeto possui testes para verificar o funcionamento da recuperação semântica.

Entre as consultas utilizadas durante o desenvolvimento estão perguntas relacionadas a:

- poda de árvores;
- retirada de entulho;
- castração de animais;
- serviços municipais;
- consultas fora do domínio da Carta de Serviços.

Para executar os testes no ambiente de desenvolvimento:

```bash
python -m pytest -v
```

---

## ▶️ Executando o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/IzaCoelho1/cidadao-ai.git
```

Entre na pasta:

```bash
cd cidadao-ai
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux:

```bash
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure a API Key

Crie um arquivo `.env` na raiz do projeto:

```text
GOOGLE_API_KEY=sua_chave_aqui
```

O arquivo `.env` não deve ser enviado para o GitHub.

### 5. Crie o banco vetorial

```bash
python scripts/criar_banco_vetorial.py
```

### 6. Execute a aplicação

```bash
streamlit run app/main.py
```

Por padrão, o Streamlit poderá ser acessado em:

```text
http://localhost:8501
```

---

## 🐳 Containerização

O projeto possui um `Dockerfile` que permite executar a aplicação em um container compatível com tecnologias de containers OCI.

No ambiente de produção foi utilizado **Podman**.

Para construir a imagem:

```bash
podman build -t cidadao-ai .
```

Para executar manualmente:

```bash
podman run -d \
  --name cidadao-ai \
  --env-file .env \
  -p 8501:8501 \
  localhost/cidadao-ai:latest
```

A porta utilizada pela aplicação é:

```text
8501/TCP
```

---

## ☁️ Deploy na Oracle Cloud Infrastructure

O Cidadão.AI foi implantado na **Oracle Cloud Infrastructure (OCI)** utilizando uma máquina virtual com Oracle Linux 9.

A aplicação é executada em container com Podman e disponibilizada publicamente através do Streamlit.

### Infraestrutura utilizada

- Oracle Cloud Infrastructure (OCI)
- Oracle Linux 9
- VM.Standard.E2.1.Micro
- Podman
- systemd
- Quadlet
- Streamlit
- ChromaDB
- Google Gemini

### Arquitetura do deploy

```text
GitHub
   ↓
Oracle Cloud Infrastructure
   ↓
Oracle Linux 9
   ↓
Podman
   ↓
Container Cidadão.AI
   ↓
ChromaDB
   ↓
Google Gemini
   ↓
Streamlit
   ↓
Internet
```

---

## 🌐 Acesso público

A aplicação foi disponibilizada publicamente através da instância da Oracle Cloud:

```text
http://163.176.12.14:8501
```

> **Observação:** o endereço público depende da disponibilidade e configuração da instância utilizada na Oracle Cloud Infrastructure.

---

## ✅ Validação do deploy

Após a implantação, a aplicação foi validada diretamente na máquina virtual.

Foi realizado o teste:

```bash
curl -I http://127.0.0.1:8501
```

A aplicação respondeu:

```text
HTTP/1.1 200 OK
```

O processo de indexação da base também foi concluído com sucesso:

```text
Banco vetorial criado com sucesso.
Documentos armazenados: 138
```

O container em execução disponibiliza a aplicação através da porta:

```text
0.0.0.0:8501
```

Esses testes confirmam o funcionamento do servidor Streamlit, do container e da base vetorial na infraestrutura da OCI.

---

## 💬 Exemplos de perguntas testadas

Durante a validação do agente foram realizadas perguntas como:

> Tem uma árvore com cupim no meu quintal, e agora?

Nesse caso, o agente encontrou o serviço relacionado a corte e poda de árvores e apresentou as orientações existentes na Carta de Serviços.

Outro teste realizado foi:

> Construí uma casa nova e preciso ligar o esgoto.

Como o procedimento específico para uma nova ligação de esgoto não estava disponível na base consultada, o agente informou que não encontrou esse serviço específico.

Também foram realizadas perguntas fora do domínio:

> Quantas Copas do Mundo o Brasil tem?

Nesse caso, o agente informou que a resposta não estava disponível na Carta de Serviços.

Esse comportamento demonstra que o sistema procura manter as respostas fundamentadas no contexto recuperado pela arquitetura RAG.

---

## 🔄 Execução persistente na OCI

Para que a aplicação permaneça disponível mesmo após o encerramento da sessão SSH, o container é gerenciado pelo **systemd utilizando Podman Quadlet**.

Foi criado um serviço:

```text
cidadao-ai.service
```

O serviço gerencia o container responsável pela aplicação.

Também foi habilitado o recurso **linger** para o usuário responsável pelo container, permitindo que os serviços de usuário continuem sendo executados mesmo sem uma sessão SSH ativa.

O status do serviço pode ser consultado com:

```bash
systemctl --user status cidadao-ai.service
```

E o container pode ser verificado com:

```bash
podman ps
```

---

## 🔐 Segurança

O projeto adota algumas medidas para evitar a exposição de informações sensíveis.

A chave utilizada para acessar a API do Gemini é armazenada em:

```text
.env
```

O arquivo está incluído no `.gitignore` e não deve ser versionado.

No servidor, o arquivo também pode ter suas permissões limitadas:

```bash
chmod 600 .env
```

A chave de API não é armazenada no `Dockerfile` nem diretamente no código-fonte.

---

## 🚧 Limitações atuais

O projeto foi desenvolvido como uma solução de demonstração utilizando RAG e uma base específica de serviços municipais.

Entre as limitações atuais estão:

- as respostas dependem das informações presentes na Carta de Serviços;
- informações externas à base não são respondidas pelo agente;
- alterações na Carta de Serviços exigem atualização da base vetorial;
- a disponibilidade pública depende da infraestrutura utilizada para hospedar a aplicação.

---

## 🚀 Melhorias futuras

Como possíveis evoluções do projeto:

- atualização automática da Carta de Serviços;
- persistência otimizada do banco vetorial entre reinicializações;
- inclusão de fontes nas respostas;
- melhoria da interface do Streamlit;
- criação de domínio próprio com HTTPS;
- monitoramento da aplicação;
- ampliação da base de conhecimento;
- integração com outros canais de atendimento ao cidadão.

---

## 👩‍💻 Autoria

Projeto desenvolvido como parte de um desafio de Inteligência Artificial utilizando arquitetura **RAG (Retrieval-Augmented Generation)** para facilitar o acesso dos cidadãos às informações sobre serviços públicos municipais.

O Cidadão.AI utiliza dados da Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ como base de conhecimento.