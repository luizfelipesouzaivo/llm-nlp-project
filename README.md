# Projeto de Introdução às LLMs para Processamento de Linguagem Natural

Este repositório contém o código e os recursos relacionados ao projeto final do curso "Introdução às LLMs para Processamento de Linguagem Natural". O objetivo do projeto foi explorar conceitos fundamentais sobre Modelos de Linguagem de Grande Escala (LLMs), engenharia de prompts, análise de dados com Named Entity Recognition (NER) e a criação de uma aplicação prática utilizando Streamlit, LLM e LangChain. O repositório está dividido nas seguintes seções:


Parte 1: Fundamentos das LLMs

Parte 2: Quizzes do Curso de NLP da Hugging Face

Parte 3: Análise de Dados com NER

Parte 4: Engenharia de Prompts

Parte 5: Projeto Prático com Streamlit, LLM e LangChain

# Parte 1: Fundamentos das LLMs
Nesta seção, conceitos fundamentais dos LLMs foram explorados e explicados com exemplos práticos:

1- Pre-training: Processo inicial de treinamento de um modelo de linguagem em grandes corpora de texto para aprender padrões linguísticos.

2- Transfer Learning: Utilização de um modelo pré-treinado para resolver uma tarefa diferente, mas relacionada.

3- Embeddings: Representação vetorial das palavras, permitindo que o modelo entenda o significado semântico.

4- Transformers: Arquitetura que utiliza mecanismos de atenção para processar sequências de dados.

5- Attention: Mecanismo que permite ao modelo focar em partes específicas de uma sequência de entrada ao gerar saídas.

6- Fine-Tuning: Ajuste do modelo pré-treinado para tarefas específicas utilizando um conjunto de dados menor e mais focado.

# Parte 2: Quizzes do Curso de NLP da Hugging Face

Foram acessados e resolvidos os quizzes dos capítulos 1, 2 e 3 do curso de NLP da Hugging Face. Os quizzes cobrem tópicos como:

1- Introdução a NLP

2- Modelos de Linguagem

3- Transformers

Screenshots dos resultados dos quizzes foram anexadas, e as explicações dos conceitos abordados em cada quiz foram incluídas na avaliação.

# Parte 3: Análise de Dados com NER

# Conjunto de Dados:

O conjunto de dados "Folha UOL News Dataset" foi utilizado para identificar e extrair entidades mencionadas nas notícias.

1- Modelo Usado: 'monilouise/ner_pt_br'

2- Objetivo: Identificar as organizações mencionadas na seção "Mercado" no primeiro trimestre de 2015.

# Metodologia:

1- Carregamento do dataset e aplicação do modelo NER para extração de entidades.

2- Criação de um ranking das organizações mais mencionadas.

# Parte 4: Engenharia de Prompts

# Análise de Prompts:

Foram analisados prompts mal formulados e reformulados para melhorar a qualidade das respostas. Exemplos incluem:

# EXEMPLO 1:

Prompt Original: "Escreva sobre cachorros."

Reformulação: "Descreva os principais cuidados ao adotar um cachorro de raça específica."

# EXEMPLO 2:

Prompt Original: "Explique física."

Reformulação: "Explique os princípios da física quântica em termos simples."

# Técnica Chain of Thought (CoT)

Foi aplicada a técnica Chain of Thought para melhorar o prompt "Explique como funciona a energia solar." Ao decompor o raciocínio necessário para uma resposta mais clara e detalhada, a aplicação do CoT resultou em uma explicação mais coerente e bem estruturada.

# Parte 5: Projeto Prático com Streamlit, LLM e LangChain

# Aplicação Desenvolvida:

Um Agente Virtual de Viagens foi desenvolvido utilizando Streamlit, LLM e LangChain.

Objetivo: Fornecer informações sobre destinos turísticos, itinerários e dicas de viagem.

- Tecnologias Usadas:

1- Streamlit: Para a interface interativa do usuário.

2- LLM: Para responder perguntas sobre destinos de forma precisa e relevante.

3- LangChain: Para orquestrar o fluxo de dados entre a interface e o modelo de linguagem.

# Arquitetura do Aplicativo:
1- A interface do usuário permite inserir perguntas sobre destinos turísticos.

2- O modelo LLM utiliza o LangChain para processar as perguntas e fornecer respostas contextuais.
