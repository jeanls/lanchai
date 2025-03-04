from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

mensagens = [
    SystemMessage(content='você é um assistente que conta piadas.'),
    HumanMessage(content='quanto é 1 + 1?'),
]

#resposta = chat.invoke(mensagens)
#print(resposta)

for trecho in chat.stream(mensagens):
    print(trecho.content, end='')




