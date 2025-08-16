from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

documents = [
    "Delhi is the capital of India",
    "New Delhi is the seat of the Government of India",
    "India is a country in South Asia",
    "The capital of India is New Delhi",
    "Delhi is known for its rich history and culture",
]

result = embedding.embed_documents(documents)
print(str(result))

