from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from src.classes.auxiliares import Categorizador

load_dotenv()

model = ChatOpenAI(model='gpt-4o-mini')


def route(input):
    if input['categoria'].area_conhecimento == 'matemática':
        return chain_matematica

    if input['categoria'].area_conhecimento == 'fisíca':
        return chain_fisica

    if input['categoria'].area_conhecimento == 'história':
        return chain_historia

    return chain_generica


prompt = ChatPromptTemplate.from_template('''Você é um professor de matemática de ensino fundamental
capaz de dar respostas muito detalhadas e didáticas. Responda a seguinte pergunta de um aluno:
Pergunta: {pergunta}''')
chain_matematica = prompt | model

prompt = ChatPromptTemplate.from_template('''Você é um professor de física de ensino fundamental
capaz de dar respostas muito detalhadas e didáticas. Responda a seguinte pergunta de um aluno:
Pergunta: {pergunta}''')
chain_fisica = prompt | model

prompt = ChatPromptTemplate.from_template('''Você é um professor de história de ensino fundamental
capaz de dar respostas muito detalhadas e didáticas. Responda a seguinte pergunta de um aluno:
Pergunta: {pergunta}''')
chain_historia = prompt | model

prompt = ChatPromptTemplate.from_template('''{pergunta}''')
chain_generica = prompt | model

prompt = ChatPromptTemplate.from_template('você deve categorizar a seguinte pergunta: {pergunta}')

model_estruturado = prompt | model.with_structured_output(Categorizador)

chain = RunnablePassthrough().assign(categoria=model_estruturado) | route
print(chain.invoke({'pergunta': 'Quanto é 3X + 10 = 50?'}))


