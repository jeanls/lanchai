from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface.chat_models.huggingface import ChatHuggingFace
from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
import langchain

langchain.debug = True

load_dotenv()

modelo = "mistralai/Mixtral-8x7B-Instruct-v0.1"
llm = HuggingFaceEndpoint(repo_id=modelo)
chat = ChatHuggingFace(llm=llm)

mensagens = [
    HumanMessage(content='quanto é 1 + 1?'),
    AIMessage(content='2'),
    HumanMessage(content='quanto é 10 * 5?'),
    AIMessage(content='50'),
    HumanMessage(content='quanto é 10 + 3?'),
]

resposta = chat.invoke(mensagens)
print(resposta.content)