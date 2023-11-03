# ai-adventure-game (Choose Your Own Adventure)

<br>

## Introduction
This project, Choose Your Own Adventure, is an interactive text-based game that allows users to embark on a time travel journey. 
In this game, the player will navigate a post-apocalyptic world overrun by zombies, guided by a Language Model (LLM). 
The game dynamically adapts its storyline based on user decisions, offering a branching narrative experience.

<br>

In this project, we incorporate the concept of Retrieval Augmented Generation (RAG) to enhance the user experience and storytelling capabilities. 
Retrieval augmented generation is a technique used with Language Models (LLMs) where external documents are retrieved and integrated into the prompt. 
This method enhances LLMs by providing additional context and grounding their responses beyond their training data.

<br>

My focus is to learn and use some new technologies, including Cassandra, LangChain, OpenAI, and DataStax Vector Database.

<br>

## Objectives
- Interactive Storytelling: Leverage LLM that responds dynamically to user inputs, creating an interactive narrative based on user choices.
- Utilize LangChain: LangChain is used to interact with OpenAI's GPT-3 model.
- Data Storage with AstraDB: DataStax AstraDB is employed to store and manage the game's chat history and conversation data efficiently.


<br>

## High-Level Design
#### Cassandra Database
We use Cassandra, a distributed NoSQL database, to store chat history and conversation data. 
The Cassandra cluster is connected to the AstraDB service, enabling secure and scalable data storage.

<br>

#### LangChain & OpenAI
LangChain is a Python library that interfaces with OpenAI's GPT-3 model. 
It allows us to have interactive and dynamic conversations with the AI, enhancing the game's narrative capabilities.

<br>

#### Chat Message History
CassandraChatMessageHistory is a component that manages and stores the chat history in Cassandra. 
It provides a structured and organized way to store user interactions with the AI.

<br>

#### Game Logic
The game logic is implemented using a custom-made prompt template, which sets the stage for the adventure and provides rules and guidelines for players. 
LangChain and OpenAI work together to generate responses based on user inputs.

<br>

#### DataStax AstraDB
AstraDB is a vector DB for generative AI, used for data storage and management.
It enables fast and context-sensitive search.

<br>

## References
- LangChain: https://python.langchain.com/docs/get_started/introduction
- DataStax Astra DB: https://docs.datastax.com/en/astra-serverless/docs/index.html
- OpenAI API: https://platform.openai.com/docs/introduction
- Retrieval Augmented Generation (RAG): https://blog.langchain.dev/conversational-retrieval-agents/

