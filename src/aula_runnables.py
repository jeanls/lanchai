from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini")

prompt_nome = ChatPromptTemplate.from_template('Crie um nome para o seguinte produto: {produto}')
chain_nome = prompt_nome | model | StrOutputParser()

prompt_clientes = ChatPromptTemplate.from_template('Descreva os clientes e potenciais para o seguinte produto: {produto}')
chain_clientes = prompt_clientes | model | StrOutputParser()

prompt_final = ChatPromptTemplate.from_template("""
    Dado o produto com o seguinte nome e seguinte público potencial, desenvolva um anúncio para o produto.
    
    Nome do produto: {nome_produto}
    público: {publico}
""")

parallel = RunnableParallel(
    {'nome_produto': chain_nome, 'publico': chain_clientes}
)

# resposta = parallel.invoke({'produto': 'Um copo inquebrável'})


chain = parallel | prompt_final | model | StrOutputParser()
# resposta = chain.invoke({'produto': 'iphone 14 pro max'})
#
# print(resposta)


def cumprimentar(nome):
    return f'Olá {nome}'


runnable_cumprimentar = RunnableLambda(cumprimentar)

resultado = runnable_cumprimentar.invoke('Jean')
print(resultado)
