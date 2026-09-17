# 🤖 LLM & NLP — Processamento de Linguagem Natural

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NLP](https://img.shields.io/badge/NLP-Natural%20Language%20Processing-purple)
![LLM](https://img.shields.io/badge/LLM-Large%20Language%20Models-orange)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Application-red?logo=streamlit)
![Status](https://img.shields.io/badge/Status-Concluído-success)

## 📌 Visão Geral

Este projeto apresenta uma aplicação prática de conceitos de **Inteligência Artificial Generativa, Large Language Models (LLMs) e Natural Language Processing (NLP)**.

O projeto foi desenvolvido a partir de diferentes etapas de estudo e aplicação prática, envolvendo:

* Fundamentos de Large Language Models;
* Processamento de Linguagem Natural;
* Transformers;
* Embeddings;
* Attention;
* Fine-Tuning;
* Named Entity Recognition (NER);
* Engenharia de Prompts;
* Chain of Thought;
* Desenvolvimento de aplicações com LLM;
* Integração entre **Streamlit, LangChain e modelos de linguagem**.

O objetivo é demonstrar a aplicação dos conceitos de NLP e LLMs em diferentes cenários, indo desde os fundamentos até a construção de uma aplicação interativa.

---

# 🎯 Objetivos

O projeto foi desenvolvido com os seguintes objetivos:

* Compreender os principais conceitos relacionados a LLMs;
* Explorar fundamentos de NLP;
* Entender o funcionamento de Transformers;
* Trabalhar com representações vetoriais de texto;
* Aplicar técnicas de Named Entity Recognition;
* Desenvolver e avaliar diferentes estratégias de prompting;
* Explorar técnicas de estruturação de prompts;
* Integrar um modelo de linguagem a uma aplicação;
* Construir uma interface interativa utilizando Streamlit;
* Utilizar LangChain para organizar o fluxo de interação com o modelo.

---

# 🧠 Conceitos Fundamentais de LLMs

Uma das etapas do projeto aborda os principais conceitos utilizados na construção e utilização de modelos modernos de linguagem.

## Pre-training

Processo no qual um modelo é treinado previamente utilizando grandes volumes de texto para aprender padrões linguísticos e representações da linguagem.

## Transfer Learning

Utilização de um modelo previamente treinado como base para outras tarefas relacionadas.

## Embeddings

Representações numéricas utilizadas para transformar palavras, frases ou documentos em vetores que podem ser processados matematicamente.

## Transformers

Arquitetura fundamental para diversos modelos modernos de linguagem, baseada principalmente no mecanismo de atenção.

## Attention

Mecanismo que permite ao modelo atribuir diferentes níveis de importância às partes de uma sequência durante o processamento.

## Fine-Tuning

Processo de adaptação de um modelo previamente treinado para uma tarefa ou domínio específico utilizando dados direcionados.

---

# 📚 NLP — Natural Language Processing

O projeto também aborda fundamentos de **Processamento de Linguagem Natural**, área da Inteligência Artificial responsável pelo processamento e análise de informações presentes em linguagem humana.

Entre os conceitos trabalhados estão:

* Tokenização;
* Modelos de linguagem;
* Transformers;
* Representação de texto;
* Embeddings;
* Reconhecimento de entidades;
* Engenharia de prompts;
* Geração de texto.

---

# 🧪 NER — Named Entity Recognition

Uma das aplicações práticas do projeto utiliza **Named Entity Recognition (NER)** para identificar entidades presentes em textos jornalísticos.

## Dataset

Foi utilizado o **Folha UOL News Dataset** para analisar notícias e identificar organizações mencionadas na seção de **Mercado durante o primeiro trimestre de 2015**.

## Modelo utilizado

```text
monilouise/ner_pt_br
```

## Objetivo

O objetivo foi identificar e extrair organizações mencionadas nas notícias e, posteriormente, analisar a frequência dessas entidades.

### Pipeline

```text
Dataset
   ↓
Textos jornalísticos
   ↓
Modelo NER
   ↓
Extração de entidades
   ↓
Filtragem de organizações
   ↓
Contagem das ocorrências
   ↓
Análise dos resultados
```

Essa etapa demonstra como técnicas de NLP podem ser utilizadas para transformar textos não estruturados em informações estruturadas.

---

# ✍️ Engenharia de Prompts

Outra etapa importante do projeto foi dedicada à **Prompt Engineering**.

O objetivo foi compreender como a estrutura de uma instrução pode influenciar a qualidade e a especificidade da resposta produzida por um modelo de linguagem.

## Exemplo

### Prompt pouco específico

```text
Escreva sobre cachorros.
```

### Prompt estruturado

```text
Descreva os principais cuidados ao adotar um cachorro de uma raça específica,
considerando alimentação, vacinação, exercícios físicos e cuidados preventivos.
```

A comparação demonstra a importância de fornecer **contexto, objetivo e especificidade** ao trabalhar com modelos de linguagem.

---

# 🧩 Chain of Thought

O projeto também explora estratégias de estruturação de prompts para orientar o modelo na elaboração de respostas mais organizadas.

Um exemplo trabalhado foi a solicitação:

```text
Explique como funciona a energia solar.
```

A abordagem foi estruturada para incentivar uma resposta organizada por etapas e aspectos do problema.

> Observação: em aplicações reais, estratégias de prompting devem ser utilizadas de forma apropriada ao contexto e sem depender da exposição de raciocínio interno do modelo.

---

# 💻 Aplicação Prática

A etapa principal de desenvolvimento consiste na criação de um **Assistente Médico Virtual** utilizando:

* Streamlit;
* LLM;
* LangChain.

A aplicação permite que o usuário envie perguntas relacionadas a sintomas, cuidados gerais e informações de saúde.

O objetivo da aplicação é demonstrar a integração entre uma **interface web**, um **framework de orquestração** e um **modelo de linguagem**.

---

# 🏗️ Arquitetura da Aplicação

O fluxo da aplicação pode ser representado da seguinte maneira:

```text
                    ┌────────────────────┐
                    │       Usuário      │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     Streamlit      │
                    │   Interface Web    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │     LangChain      │
                    │ Orquestração/Fluxo │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │        LLM         │
                    │ Modelo de Linguagem│
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      Resposta      │
                    └────────────────────┘
```

---

# 🩺 Assistente Médico Virtual

A aplicação foi construída como uma demonstração de uso de LLM em um cenário relacionado à saúde.

### Fluxo da aplicação

1. O usuário insere uma pergunta;
2. A aplicação recebe a entrada através do Streamlit;
3. O LangChain organiza o fluxo da solicitação;
4. A pergunta é encaminhada ao modelo de linguagem;
5. O modelo gera uma resposta contextualizada;
6. A resposta é apresentada ao usuário através da interface.

### ⚠️ Importante

Esta aplicação possui finalidade **educacional e demonstrativa**.

As respostas geradas não devem ser utilizadas como diagnóstico, prescrição ou substituição de atendimento médico profissional.

---

# 🛠️ Tecnologias Utilizadas

| Tecnologia      | Aplicação                            |
| --------------- | ------------------------------------ |
| 🐍 Python       | Desenvolvimento                      |
| 🤖 LLM          | Geração e processamento de linguagem |
| 🧠 NLP          | Processamento de textos              |
| 🔗 LangChain    | Orquestração da aplicação            |
| 🎨 Streamlit    | Interface web interativa             |
| 🏷️ NER         | Extração de entidades                |
| 🔤 Transformers | Arquiteturas modernas de NLP         |
| 📊 Pandas       | Manipulação e análise de dados       |

---

# 📁 Estrutura do Projeto

```text
llm-nlp-project/
│
├── README.md
│
├── requirements.txt
│
├── question/
│
└── src/
    └── medico_agent/
```

A estrutura atual do repositório contém uma pasta `src/medico_agent`, além do arquivo de dependências e materiais utilizados no projeto.

---

# 🚀 Como Executar

## 1. Clone o repositório

```bash
git clone https://github.com/luizfelipesouzaivo/llm-nlp-project.git
```

## 2. Acesse a pasta

```bash
cd llm-nlp-project
```

## 3. Crie um ambiente virtual

### Windows

```bash
python -m venv .venv
```

Ative:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Ative:

```bash
source .venv/bin/activate
```

## 4. Instale as dependências

```bash
pip install -r requirements.txt
```

## 5. Execute a aplicação

Caso o arquivo principal do agente esteja configurado como aplicação Streamlit:

```bash
streamlit run app.py
```

> O comando exato pode variar conforme o arquivo de entrada definido no projeto.

---

# 📊 Principais Aprendizados

O desenvolvimento deste projeto permitiu trabalhar conceitos importantes relacionados à área de **Inteligência Artificial Generativa e NLP**:

* Fundamentos de LLMs;
* Pre-training;
* Transfer Learning;
* Embeddings;
* Transformers;
* Attention;
* Fine-Tuning;
* Natural Language Processing;
* Named Entity Recognition;
* Engenharia de Prompts;
* Estruturação de prompts;
* LangChain;
* Streamlit;
* Integração de LLMs em aplicações;
* Extração de informações de textos;
* Desenvolvimento de aplicações baseadas em linguagem natural.

---

# 🔄 Fluxo Geral do Projeto

```text
Fundamentos de LLM
        ↓
NLP
        ↓
Transformers
        ↓
NER
        ↓
Análise de textos
        ↓
Prompt Engineering
        ↓
LLM + LangChain
        ↓
Streamlit
        ↓
Aplicação prática
```

---

# 📌 Possíveis Aplicações

Os conhecimentos explorados neste projeto podem ser utilizados em diferentes soluções de Inteligência Artificial, como:

* Assistentes virtuais;
* Chatbots;
* Classificação de textos;
* Extração de informações;
* Análise de documentos;
* Busca semântica;
* Sistemas de perguntas e respostas;
* Automação de tarefas textuais;
* Análise de notícias;
* Processamento de documentos corporativos;
* Sistemas baseados em LLM.

---

# 👨‍💻 Autor

## Luiz Felipe Souza Ivo

Graduado em **Sistemas de Informação**, com foco de desenvolvimento profissional em:

* 🤖 Inteligência Artificial
* 🧠 Machine Learning
* 💬 NLP
* 📊 Análise de Dados
* 🐍 Python
* 🗄️ SQL
* 📈 Power BI

### 🔗 Contatos

[![GitHub](https://img.shields.io/badge/GitHub-Luiz%20Felipe-181717?logo=github)](https://github.com/luizfelipesouzaivo)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Luiz%20Felipe-0A66C2?logo=linkedin)](https://linkedin.com/in/luiz-felipe-souza-ivo/)

---

## 📚 Referências

* Hugging Face — Natural Language Processing
* LangChain
* Streamlit
* Modelos de linguagem e Transformers

---

## 📌 Sobre o Projeto

Este projeto faz parte do meu portfólio de estudos em **Inteligência Artificial, Natural Language Processing e Large Language Models**.

A implementação reúne fundamentos teóricos e aplicações práticas, demonstrando desde conceitos essenciais de modelos de linguagem até a construção de uma aplicação interativa utilizando **LLM, LangChain e Streamlit**.

O projeto foi desenvolvido como trabalho final do curso **Introdução às LLMs para Processamento de Linguagem Natural**.
