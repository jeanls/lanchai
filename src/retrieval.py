from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

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


#MMR
# docs = vectorstore.max_marginal_relevance_search(pergunta, k=5, fetch_k=10)
# for doc in docs:
#     print(doc.page_content)
#     print(f'=============== {doc.metadata}\n\n')

#Filter
docs = vectorstore.similarity_search('O que a apostila de hugging face fala sobre openai e o chat gpt?', k=5, filter={'source': '../Explorando o Universo das IAs com Hugging Face.pdf'})
for doc in docs:
    print(doc.page_content)
    print(f'=============== {doc.metadata}\n\n')