from langchain.prompts import ChatPromptTemplate
from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
chat = ChatOpenAI(model="gpt-3.5-turbo")

chat_template_1 = ChatPromptTemplate.from_template('''
    Essa é minha dúvida: {duvida}
''')

chat_template_2 = ChatPromptTemplate.from_messages(
    [
        ('system', 'Você é um assitente engraçado e se chama {nome_assistente}'),
        ('human', 'Olá como vai?'),
        ('ai', 'Melhor agora! como posso ajudá-lo?'),
        ('human', '{pergunta}'),
    ]
)

# resposta = chat.invoke(chat_template_2.format(nome_assistente='JokeBot', pergunta='Qual é seu nome?'))
# print(resposta)

exemplos = [
    {"pergunta": "Quem viveu mais tempo, Muhammad Ali ou Alan Turing?",
     "resposta":
         """São necessárias perguntas de acompanhamento aqui: Sim.
         Pergunta de acompanhamento: Quantos anos Muhammad Ali tinha quando morreu?
         Resposta intermediária: Muhammad Ali tinha 74 anos quando morreu.
         Pergunta de acompanhamento: Quantos anos Alan Turing tinha quando morreu?
         Resposta intermediária: Alan Turing tinha 41 anos quando morreu.
         Então a resposta final é: Muhammad Ali
         """,
     },
    {"pergunta": "Quando nasceu o fundador do craigslist?",
     "resposta":
         """São necessárias perguntas de acompanhamento aqui: Sim.
         Pergunta de acompanhamento: Quem foi o fundador do craigslist?
         Resposta intermediária: O craigslist foi fundado por Craig Newmark.
         Pergunta de acompanhamento: Quando nasceu Craig Newmark?
         Resposta intermediária: Craig Newmark nasceu em 6 de dezembro de 1952.
         Então a resposta final é: 6 de dezembro de 1952
         """,
     },
    {"pergunta": "Quem foi o avô materno de George Washington?",
     "resposta":
         """São necessárias perguntas de acompanhamento aqui: Sim.
         Pergunta de acompanhamento: Quem foi a mãe de George Washington?
         Resposta intermediária: A mãe de George Washington foi Mary Ball Washington.
         Pergunta de acompanhamento: Quem foi o pai de Mary Ball Washington?
         Resposta intermediária: O pai de Mary Ball Washington foi Joseph Ball.
         AsimovAcademy
         16
        Aplicações IA com LangChain
         Então a resposta final é: Joseph Ball
         """,
     }
]

example_prompt = PromptTemplate.from_template('Pergunta {pergunta}\nResposta {resposta}\n')
print(example_prompt.format(**exemplos[0]))

prompt = FewShotPromptTemplate(
    examples=exemplos,
    example_prompt=example_prompt,
    suffix='Pergunta: {input}',
    input_variables=['input']
)

resposta = chat.invoke(prompt.format(input='Quem fez mais gols Messe ou Gabigol?'))
print(resposta)
