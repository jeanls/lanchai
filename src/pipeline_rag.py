from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
# set_debug(True)

load_dotenv()

caminhos = [
    '../docs/Explorando o Universo das IAs com Hugging Face.pdf',
    '../docs/Explorando a API da OpenAI.pdf',
    '../docs/Explorando a API da OpenAI.pdf'
]

def join_documents(input):
    input['contexto'] = '\n\n'.join([c.page_content for c in input['contexto']])
    return input


paginas = []

for caminho in caminhos:
    loader = PyPDFLoader(caminho)
    paginas.extend(loader.load())

recursive_char_split = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=['\n\n', '\n', '.',
                                                                                                    ' '])
documents = recursive_char_split.split_documents(paginas)
print(len(documents))

for index, document in enumerate(documents):
    document.metadata['source'] = document.metadata['source'].replace("../docs/", "")
    document.metadata['doc_id'] = index

embedings_model = OpenAIEmbeddings()

dir_chroma = '../docs/chroma_vectorstore_retrieval'

# Criando base
# vectorstore = Chroma.from_documents(
#     documents=documents,
#     embedding=embedings_model,
#     persist_directory=dir_chroma
# )

# # Importando a base
vectorstore = Chroma(
    embedding_function=embedings_model,
    persist_directory=dir_chroma
)

prompt = ChatPromptTemplate.from_template(
    '''
        Responda as perguntas abaixo se baseando no contexto fornecido.
        
        contexto: {contexto}
        
        Pergunta: {pergunta}
    '''
)

retriever = vectorstore.as_retriever(search_type='mmr', search_kwargs={'k': 5, 'fetch_k': 25})

setup = RunnableParallel({
    'pergunta': RunnablePassthrough(),
    'contexto': retriever
}) | join_documents

resposta = setup.invoke('O que é a openAI?')
# print(resposta)

chat = ChatOpenAI(model="gpt-4o-mini")

chain = setup | prompt | chat
resposta = chain.invoke('O que é a openAI?')

print(resposta)

