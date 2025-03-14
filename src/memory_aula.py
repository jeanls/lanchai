from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from dotenv import load_dotenv

load_dotenv()
memory = InMemoryChatMessageHistory()
model = ChatOpenAI(model="gpt-4o-mini")

memory.add_user_message('Olá modelo')
memory.add_ai_message('Olá user')

prompt = ChatPromptTemplate.from_messages([
    ("system", "você é um tutor de programação chamado Asimo. Responda as perguntas de forma didática."),
    ("placeholder", "{history}"),
    ("human", "{pergunta}"),
])

chain = prompt | model
store = {

}


def get_by_session_id(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


chain_com_memoria = RunnableWithMessageHistory(
    chain,
    get_by_session_id,
    input_messages_key='pergunta',
    history_messages_key='history'
)

config = {'configurable': {'session_id': 'usuario_a'}}

resposta = chain_com_memoria.invoke({'pergunta': 'Olá meu nome é Jean'}, config=config)
print(resposta)
resposta = chain_com_memoria.invoke({'pergunta': 'Qual é o meu nome?'}, config=config)
print(resposta)

