from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embedding_model = OpenAIEmbeddings()

embeddings = embedding_model.embed_documents(
    [
        'Eu gosto de cachorros',
        'Eu gosto de animais',
        'O tempo está ruim lá fora',
    ]
)

print(np.dot(embeddings[0], embeddings[1]))
print(np.dot(embeddings[0], embeddings[2]))

for i in range(len(embeddings)):
    for j in range(len(embeddings)):
        print(round(np.dot(embeddings[i], embeddings[j]), 2), end=' | ')
    print()

pergunta = 'O que é um cachorro?'
emb_query = embedding_model.embed_query(pergunta)

