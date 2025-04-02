from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.globals import set_debug

set_debug(True)

load_dotenv()

caminhos = [
    '../docs/Explorando o Universo das IAs com Hugging Face.pdf',
    '../docs/Explorando a API da OpenAI.pdf',
    '../docs/Explorando a API da OpenAI.pdf'
]

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
# Textos iguais são levados em consideração, observar import duplicado dos documentos
pergunta = 'O que é openai?'
# docs = vectorstore.similarity_search(pergunta, k=5)
# for doc in docs:
#     print(doc.page_content)
#     print(f'=============== {doc.metadata}\n\n')


# MMR
# docs = vectorstore.max_marginal_relevance_search(pergunta, k=5, fetch_k=10)
# for doc in docs:
#     print(doc.page_content)
#     print(f'=============== {doc.metadata}\n\n')

# Filter
docs = vectorstore.similarity_search('O que a apostila de hugging face fala sobre openai e o chat gpt?', k=5,
                                     filter={'source': '../Explorando o Universo das IAs com Hugging Face.pdf'})
# for doc in docs:
#     print(doc.page_content)
#     print(f'=============== {doc.metadata}\n\n')

chat = ChatOpenAI(model="gpt-4o-mini")



chain_prompt = PromptTemplate.from_template(
    '''
        Utilize o contexto fornecido para responder a pergunta ao final.
        Se você não sabe a resposta, apenas diga que não sabe e não tente inventar a resposta.
        Utilize três frases no máximo, mantenha a resposta concisa.
        
        Contexto: {context}
        
        Pergunta: {question}
        
        Resposta: 
    '''
)

chat_chain = RetrievalQA.from_chain_type(
    llm=chat,
    retriever=vectorstore.as_retriever(search_type='mmr'),
    chain_type_kwargs={'prompt': chain_prompt},
    return_source_documents=True,
    chain_type='stuff'
)

# stuff é o mais simples,pega tudo e joga no prompt
# map_recuce separa os prompts por documento ou seja cada documento em um prompt
# refine vai perguntando por documento e utiliza a resposta para fazer uma nova pergunta

pergunta = 'O que é hugging face e como faço para acessá-lo?'

resposta = chat_chain.invoke({'query': pergunta})
print(resposta)
