from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseModel, Field

from src.classes.auxiliares import Piada, AvaliacaoReview

load_dotenv()

chat = ChatOpenAI(model="gpt-4o-mini")
output_parser = StrOutputParser()

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "Você é um assistente engraçado chamado: {nome_assistente}"),
        ("human", "{pergunta}")
    ]
)

# resposta = chat.invoke(chat_template.format(nome_assistente="Jean", pergunta="quanto é 1 + 2?"))

# print(output_parser.invoke(resposta))

# llm_estruturada = chat.with_structured_output(Piada)
# resposta = llm_estruturada.invoke('conte uma piada sobre gatinhos')
# print(resposta)

llm_estruturada = chat.with_structured_output(AvaliacaoReview)
resposta = llm_estruturada.invoke("""
    Este soprador de folhas é bastante incrível. Ele tem quatro configurações: sopro de vela, brisa suave, cidade ventosa e
    tornado. Chegou em dois dias, bem a tempo para o presente de aniversário da minha esposa. Acho que minha esposa gostou
    tanto que ficou sem palavras. Até agora, fui o único a usá-lo, e tenho usado em todas as manhãs alternadas para limpar
    as folhas do nosso gramado. É um pouco mais caro do que os outros sopradores de folhas disponíveis no mercado,
    mas acho que vale a pena pelas características extras.
""")

print(resposta)
