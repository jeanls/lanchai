from langchain_community.document_loaders.pdf import PyPDFLoader
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders.web_base import WebBaseLoader
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.blob_loaders.youtube_audio import YoutubeAudioLoader
from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

loader = PyPDFLoader('../docs/Explorando o Universo das IAs com Hugging Face.pdf')
documentos = loader.load()

loader_csv = CSVLoader('../docs/Top 1000 IMDB movies.csv')
csv = loader_csv.load()

print(len(documentos))
print(len(csv))

chat = ChatOpenAI(model="gpt-4o-mini")
chain = load_qa_chain(llm=chat, chain_type='stuff', verbose=True)

# pergunta = 'Quais assuntos são tratados no documento'
# resposta = chain.run(input_documents=documentos[:10], question=pergunta)


# pergunta = 'qual o filme com maior nota?'
# resposta = chain.run(input_documents=csv[:10], question=pergunta)
#
# print(resposta)

# url = 'https://www.youtube.com/watch?v=KHoEbRH46Zk'
# save_dir = '../docs/youtube'
# gen_loader = GenericLoader(
#     YoutubeAudioLoader([url], save_dir),
#     OpenAIWhisperParser()
# )
#
# youtube_audio_doc = gen_loader.load()
# print(len(youtube_audio_doc))
#
# print(youtube_audio_doc)

# print(youtube_audio_doc[0].page_content[:500])
# pergunta = 'qual o filme com maior nota?'
# resposta = chain.run(input_documents=csv[:10], question=pergunta)

url = 'https://hub.asimov.academy/blog/listas-em-python/'
web_loader = WebBaseLoader(url)
web_documentos = web_loader.load()

print(web_documentos)
