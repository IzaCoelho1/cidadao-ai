# 🏛️ Cidadão.AI

Assistente inteligente baseado em **RAG (Retrieval-Augmented Generation)** para consulta à **Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ**.

O projeto permite que cidadãos façam perguntas em linguagem natural sobre serviços públicos municipais e recebam respostas baseadas nas informações oficiais disponíveis na Carta de Serviços.

---

## 🎯 Objetivo

O **Cidadão.AI** foi desenvolvido com o objetivo de facilitar o acesso dos cidadãos às informações sobre serviços públicos municipais.

O sistema permite responder perguntas como:

- Quais documentos preciso para solicitar poda de uma árvore?
- Como solicitar a retirada de entulho?
- Como solicitar a castração de um animal?
- Quanto custa determinado serviço?
- Qual é o prazo para atendimento?
- Onde posso solicitar um serviço?
- Qual secretaria é responsável?

A interface também disponibiliza **sugestões de perguntas por meio de botões interativos**, facilitando a utilização do agente e apresentando exemplos de consultas que podem ser realizadas.

Quando uma informação não está disponível na Carta de Serviços, o agente informa que não encontrou a resposta na base consultada, reduzindo a geração de informações sem fundamento.

---

## 🧠 Como funciona

O projeto utiliza a arquitetura **RAG (Retrieval-Augmented Generation)**.

O funcionamento ocorre nas seguintes etapas:

1. Os dados da Carta de Serviços são carregados e processados.
2. Cada serviço é transformado em um documento para consulta.
3. Os documentos são convertidos em embeddings.
4. Os embeddings são armazenados no banco vetorial **ChromaDB**.
5. A pergunta do cidadão também é transformada em uma representação vetorial.
6. O sistema realiza uma busca semântica para encontrar os serviços mais relacionados à pergunta.
7. Os documentos recuperados são utilizados como contexto para o modelo de linguagem.
8. O **Google Gemini** gera a resposta utilizando as informações recuperadas.
9. A resposta é apresentada ao cidadão por meio da interface desenvolvida em **Streamlit**.

---

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
Google Gemini
       ↓
Resposta ao cidadão
       ↓
Interface Streamlit
       ↓
Deploy na Oracle Cloud
```

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **LangChain**
- **Google Gemini 3.5 Flash-Lite**
- **Google Generative AI Embeddings**
- **ChromaDB**
- **Streamlit**
- **Pytest**
- **Git**
- **GitHub**
- **Podman**
- **systemd / Quadlet**
- **Oracle Cloud Infrastructure (OCI)**
- **Oracle Linux 9**

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
├── docs/
│   └── evidencias/
│       ├── cidadao-ai-deploy-oci.png
│       ├── cidadao-ai-oci.png
│       └── cidadao-ai-resposta-fora-base.png
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

---

## 🔎 Busca semântica

O Cidadão.AI utiliza embeddings para representar semanticamente tanto os serviços da Carta de Serviços quanto as perguntas realizadas pelos cidadãos.

Quando uma pergunta é enviada, o sistema realiza uma busca no **ChromaDB** para recuperar os documentos semanticamente mais relacionados à consulta.

Os documentos recuperados são enviados ao modelo de linguagem como contexto, permitindo que a resposta seja produzida com base nas informações da documentação utilizada pelo projeto.

---

## 💬 Exemplos de perguntas

O agente pode receber perguntas em linguagem natural, como:

> Tenho uma árvore com cupim no meu quintal. O que devo fazer?

> Como faço para solicitar a retirada de entulho?

> Como faço para solicitar a castração de um animal?

> Quais documentos preciso para solicitar a poda de uma árvore?

A interface também possui botões com sugestões de perguntas para facilitar a demonstração e a utilização do sistema.

---

## 🤖 Exemplo de resposta gerada

### Pergunta

> Como faço para solicitar retirada de entulho?

### Resposta

O Cidadão.AI recupera as informações relacionadas ao serviço e orienta o cidadão sobre os documentos, etapas, prazo, custo, canais de atendimento e unidade responsável.

Entre as informações recuperadas estão:

**Documentos necessários:**

- Formulário de solicitação
- RG
- CPF
- Comprovante de residência
- Comprovante de pagamento da taxa de serviço

**Etapas:**

1. Solicitar presencialmente no Protocolo da Prefeitura ou pelo aplicativo.
2. Aguardar a vistoria para quantificação do entulho.
3. Receber a guia de recolhimento.
4. Realizar o pagamento da taxa.
5. Aguardar a realização do serviço.

**Prazo:**

Até 7 dias.

**Custo:**

R$ 72,00.

**Unidade responsável:**

Secretaria Municipal de Serviços Públicos.

---

## 🛡️ Controle de respostas fora da base

Uma característica importante do projeto é evitar respostas sem fundamento na documentação utilizada.

Por exemplo:

### Pergunta

> Qual é o salário do prefeito de Pinheiral?

Como essa informação não está disponível na Carta de Serviços utilizada como base de conhecimento, o agente informa que **não encontrou a informação na documentação consultada**.

Esse comportamento ajuda a reduzir alucinações e mantém o agente focado no domínio para o qual foi desenvolvido.

---

## 💡 Sugestões interativas

A versão final da interface possui botões com exemplos de consultas:

- 🌳 **Árvore com cupim**
- 🐶 **Castração de animal**
- 🗑️ **Retirada de entulho**
- ✂️ **Poda de árvore**

Ao clicar em uma das opções, a pergunta é enviada ao mesmo fluxo RAG utilizado pelas perguntas digitadas manualmente.

O cidadão também pode escrever livremente sua própria pergunta no campo de conversa.

---

## 🧪 Testes

O projeto possui testes automatizados com **Pytest** para verificar a recuperação semântica dos serviços.

Para executar:

```bash
python -m pytest -v
```

Os testes verificam consultas relacionadas a serviços como:

- poda de árvores;
- retirada de entulho;
- castração de animais.

Também foram realizados testes manuais para verificar:

- recuperação dos documentos;
- geração de embeddings;
- busca semântica;
- integração com o Gemini;
- funcionamento completo do fluxo RAG;
- tratamento de perguntas fora da base;
- funcionamento da aplicação após o deploy.

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

### 3. Ative o ambiente virtual

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```text
GOOGLE_API_KEY=SUA_CHAVE_DA_API
```

> ⚠️ Nunca envie sua chave de API para o GitHub.

### 6. Crie o banco vetorial

```bash
python scripts/criar_banco_vetorial.py
```

### 7. Execute a aplicação

```bash
python -m streamlit run app/main.py
```

A aplicação poderá ser acessada localmente pelo navegador.

---

## 🔐 Segurança

Chaves de API e outras informações sensíveis **não são armazenadas no repositório**.

O arquivo:

```text
.env
```

está incluído no `.gitignore`.

Dessa forma, as credenciais utilizadas para acessar serviços externos permanecem fora do controle de versão.

---

## ☁️ Deploy na Oracle Cloud Infrastructure

O **Cidadão.AI** foi implantado em uma instância de computação da **Oracle Cloud Infrastructure (OCI)** utilizando **Oracle Linux 9**.

A aplicação é executada em container utilizando **Podman** e disponibilizada pela porta **8501**.

Para manter a aplicação em execução de forma independente da sessão SSH, o container foi configurado como um serviço utilizando **systemd e Quadlet**.

### Infraestrutura utilizada

- **Oracle Cloud Infrastructure (OCI)**
- **Oracle Linux 9**
- **VM.Standard.E2.1.Micro**
- **1 OCPU**
- **1 GB de memória**
- **Podman**
- **systemd / Quadlet**
- **Streamlit**
- **ChromaDB**
- **Google Gemini**

### Fluxo do deploy

```text
GitHub
   ↓
Oracle Cloud VM
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

## 🌐 Aplicação publicada

A aplicação está disponível publicamente por meio da instância da Oracle Cloud:

**Cidadão.AI**

http://163.176.12.14:8501

> A disponibilidade do endereço depende da instância da Oracle Cloud permanecer ativa.

---

## 📸 Evidências do funcionamento

### Deploy na Oracle Cloud Infrastructure

A imagem abaixo mostra a instância **`cidadao-ai`** em execução (`Running`) na **Oracle Cloud Infrastructure**, com endereço IP público associado.

![Deploy do Cidadão.AI na Oracle Cloud Infrastructure](docs/evidencias/cidadao-ai-deploy-oci.png)

### Aplicação em funcionamento

A imagem abaixo apresenta a versão final do **Cidadão.AI** acessível pela internet após o deploy na OCI.

![Cidadão.AI executado na Oracle Cloud](docs/evidencias/cidadao-ai-oci.png)

### Tratamento de pergunta fora da base

A imagem abaixo demonstra o comportamento do agente quando recebe uma pergunta cuja resposta não está disponível na Carta de Serviços.

![Cidadão.AI respondendo pergunta fora da base](docs/evidencias/cidadao-ai-resposta-fora-base.png)

---

## 🎥 Demonstração em vídeo

Uma demonstração da versão final do **Cidadão.AI**, incluindo a interface com sugestões de perguntas interativas e o funcionamento do agente RAG, está disponível no YouTube:

▶️ [Assistir à demonstração do Cidadão.AI](https://youtube.com/shorts/7_HsWOoxg5o?feature=share)

---

## 🚀 Diferenciais do projeto

Entre os principais recursos implementados estão:

- respostas baseadas na documentação utilizada como fonte de conhecimento;
- arquitetura RAG;
- busca semântica utilizando embeddings;
- banco vetorial com ChromaDB;
- integração com Google Gemini;
- interface conversacional desenvolvida em Streamlit;
- sugestões de perguntas por meio de botões interativos;
- histórico da conversa durante a sessão;
- indicação da fonte principal utilizada na resposta;
- tratamento de perguntas fora da base;
- testes automatizados;
- containerização com Podman;
- serviço persistente com systemd/Quadlet;
- deploy público na Oracle Cloud Infrastructure.

---

## 🔮 Melhorias futuras

Algumas possíveis evoluções do projeto incluem:

- persistência otimizada do banco vetorial entre reinicializações;
- redução do número de chamadas às APIs externas;
- cache de consultas frequentes;
- melhoria do tratamento de limites de requisição da API;
- expansão da base de conhecimento;
- integração com novas fontes de dados municipais;
- inclusão de novos serviços;
- melhorias contínuas na experiência de uso da interface;
- utilização de domínio próprio e HTTPS;
- monitoramento da aplicação em produção.

---

## 📚 Aprendizados

O desenvolvimento do projeto permitiu aplicar conceitos importantes de Inteligência Artificial e desenvolvimento de software, incluindo:

- Retrieval-Augmented Generation (RAG);
- embeddings;
- bancos vetoriais;
- busca semântica;
- engenharia de prompts;
- integração com modelos de linguagem;
- tratamento de respostas fora da base de conhecimento;
- desenvolvimento de interfaces com Streamlit;
- testes automatizados;
- Git e GitHub;
- containerização;
- deploy de aplicações de IA em ambiente de nuvem.

---

## 👩‍💻 Autoria

**Iza Paloma Maciel Coelho**

GitHub: [@IzaCoelho1](https://github.com/IzaCoelho1)

Projeto desenvolvido como parte do **Challenge Alura — Agente Inteligente**, utilizando arquitetura **RAG (Retrieval-Augmented Generation)** para facilitar o acesso dos cidadãos às informações da Carta de Serviços da Prefeitura Municipal de Pinheiral - RJ.

---

## 📄 Finalidade

Projeto desenvolvido para fins educacionais e de demonstração da aplicação de técnicas de Inteligência Artificial.

As respostas do agente são geradas a partir das informações recuperadas da Carta de Serviços utilizada como base de conhecimento.