from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from langchain.memory import CassandraChatMessageHistory, ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import json
import config
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)


# Connect to Astra DB
cloud_config= {
  'secure_connect_bundle': 'secure-connect-choose-your-own-adventure.zip'
}

with open("choose_your_own_adventure-token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]
ASTRA_DB_KEYSPACE = "database"
OPENAI_API_KEY = config.OPENAI_API_KEY

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()


# Initialize LLM Memory
message_history = CassandraChatMessageHistory(
    session_id="test_session",
    session=session,
    keyspace=ASTRA_DB_KEYSPACE,
    ttl_seconds=3600 # 60 minutes
)

message_history.clear()

cass_buff_memory = ConversationBufferMemory(
    memory_key="chat_history",
    chat_memory=message_history,
)


# Create Prompt Template
template = """
Welcome to the world of time travel, where you will guide a time traveler from the year 2050,
sent back to the fateful date of October 31, 2035 in New York City. In this grim reality, a devastating pandemic
swept the globe during the spring of 2033, resulting in the Earth's grim transformation into a
post-apocalyptic wasteland infested with hordes of zombies.

A time traveler named Peach seeks the lost vaccine and duplicate it to prevent the spread of virus.
You must navigate her through challenges, choices, and consequences,
dynamically adapting the tale based on the traveler's decisions.
Your goal is to create a branching narrative experience where each choice
leads to a new path, ultimately determining Peach's fate.

Here are some rules to follow:
1. Start by asking the player to choose some kind of weapons that will be used later in the game
2. Have the player to choose at least 5 paths
3. Have a few paths that lead to success
4. Have some paths that lead to death. If the user dies generate a response that explains the death and ends in the text: "The End.", I will search for this text to end the game

Here is the chat history, use this to understand what to say next: {chat_history}
Human: {human_input}
AI:"""

prompt = PromptTemplate(
    input_variables=["chat_history", "human_input"],
    template=template
)


# Initialize Connection to OpenAI
llm = OpenAI(openai_api_key=OPENAI_API_KEY)
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=cass_buff_memory
)


# Start the Game
choice = "start"

while True:
    response = llm_chain.predict(human_input=choice)
    print(response.strip())

    if "The End." in response:
        break

    choice = input("Your reply: ")
