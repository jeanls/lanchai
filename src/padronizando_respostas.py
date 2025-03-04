from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

mensagens = [
    HumanMessage(content='quanto é 1 + 1?'),
    AIMessage(content='2'),
    HumanMessage(content='quanto é 10 * 5?'),
    AIMessage(content='50'),
    HumanMessage(content='quanto é 10 + 3?'),
]

resposta = chat.invoke(mensagens)
print(resposta.content)