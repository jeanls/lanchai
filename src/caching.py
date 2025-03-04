from dotenv import load_dotenv
from langchain.globals import set_llm_cache
from langchain_community.cache import InMemoryCache
from langchain_community.cache import SQLiteCache
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()
# set_llm_cache(InMemoryCache())
set_llm_cache(SQLiteCache(database_path='../data/cache.sqlite'))
chat = ChatOpenAI(model="gpt-3.5-turbo")

mensagens = [
    SystemMessage(content='você é um assistente engraçado.'),
    HumanMessage(content='quanto é 1 + 1?'),
]

print(chat.invoke(mensagens).content)
print(chat.invoke(mensagens).content)