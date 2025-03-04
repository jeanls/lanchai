from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
prompt_template = PromptTemplate.from_template('''
    Responda a seguinte pergunta do usuário:
    {pergunta} em até {n} parágrafos.
''', partial_variables={'n': 3})

pergunta = prompt_template.format(pergunta='O que é um buraco negro?')

llm = OpenAI()

for sentence in llm.stream(pergunta):
    print(sentence, end='')
