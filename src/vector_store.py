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

