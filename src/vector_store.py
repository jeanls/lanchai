from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv


load_dotenv()

caminho = '../docs/Explorando o Universo das IAs com Hugging Face.pdf'
loader = PyPDFLoader(caminho)
paginas = loader.load()

recursive_char_split = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, separators=['\n\n', '\n', '.',
                                                                                                    ' '])
documents = recursive_char_split.split_documents(paginas)
print(len(documents))

embedings_model = OpenAIEmbeddings()

dir_chroma = '../docs/chroma_vectorstore'

# Criando base
# vectorstore = Chroma.from_documents(
#     documents=documents,
#     embedding=embedings_model,
#     persist_directory=dir_chroma
# )

# Importando a base
vectorstore = Chroma(
    embedding_function=embedings_model,
    persist_directory=dir_chroma
)

pergunta = 'O que é o hugging face?'
docs = vectorstore.similarity_search(pergunta, k=5)
print(len(docs))
for doc in docs:
    print(doc.page_content)
    print(f'=============== {doc.metadata}\n\n')