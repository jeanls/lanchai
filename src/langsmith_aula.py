from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
model = ChatOpenAI()

prompt_curiosidade = ChatPromptTemplate.from_template('fale uma curiosidade sobre o assunto: {assunto}')
chain_curiosidade = prompt_curiosidade | model | StrOutputParser()

prompt_historia = ChatPromptTemplate.from_template('Crie uma historia sobre o seguinte assunto: {assunto}')
chain_historia = prompt_historia | model | StrOutputParser()

chain = chain_curiosidade | chain_historia
# resposta = chain.invoke({'assunto': 'futebol'})
resposta = chain.batch([{'assunto': 'política'}, {'assunto': 'religião'}], config={'max_concurrency': 2})

print(resposta)

