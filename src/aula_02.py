from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

#pergunta = "Qual é a capital do Brasil?"

#resposta = llm.invoke(pergunta)  #chama a api sem stream

#print(resposta)

#pergunta = "conte uma história sobre um cachorro"

#chamando a api com stream
#for trecho in llm.stream(pergunta):
#    print(trecho, end="")

#chamando a api com multiplas perguntas

perguntas = ["Qual é a capital do Brasil?", "Qual é a capital da França?", "Qual é a capital da Argentina?"]

respostas = llm.batch(perguntas)
for resposta in respostas:
    print(resposta)

