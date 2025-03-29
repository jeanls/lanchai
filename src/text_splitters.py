from langchain_text_splitters import CharacterTextSplitter
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import TokenTextSplitter
from langchain_community.document_loaders.pdf import PyPDFLoader
from dotenv import load_dotenv
import string

load_dotenv()

texto = '''
Já conhece a lista em Python? Quer entender como manipular listas e quais são suas principais utilidades e métodos? Sabe qual a diferença entre listas e tuplas? Este artigo responde responde isso e muito mais! Aproveite ao máximo todo o potencial dessa estrutura de dados essencial para a programação em Python.

A lista em Python é uma das estruturas de dados fundamentais da linguagem Python. Além de possuir grande versatilidade, as listas são extremamente relevantes para iniciantes na programação, por incorporar uma variedade de conceitos básicos de Python como mutabilidade, indexação, iteração e slicing. Mas você já conhece as listas de Python a fundo?

Neste artigo, vamos nos aprofundar nas listas em Python e aprender a utilizá-las em seus códigos. Ao longo do texto, você aprenderá como criar e manipular uma lista em Python, quais os principais métodos de listas, e como elas se relacionam e com outros tipos de dados de Python, como strings, tuplas e vetores. Vamos lá!

'''

chunk_size = 50
chunk_overlap = 5  # 10%

char_split = CharacterTextSplitter(chunk_size=50, chunk_overlap=0, separator=' ')
recursive_char_split = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=0, separators=['.', ' '])
token_char_split = TokenTextSplitter(chunk_size=50, chunk_overlap=0)
# texto = ''.join(f'{string.ascii_lowercase}' for _ in range(5))

print(char_split.split_text(text=texto))
print(recursive_char_split.split_text(text=texto))
print(token_char_split.split_text(text=texto))

caminho = '../docs/Explorando o Universo das IAs com Hugging Face.pdf'
loader = PyPDFLoader(caminho)
docs = loader.load()

splits = char_split.split_documents(docs)
print(splits)
