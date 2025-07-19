from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

documents = [
    "Delhi is the capital of India",
    "New Delhi is the seat of the Government of India",
    "India is a country in South Asia",
    "The capital of India is New Delhi",
    "Delhi is known for its rich history and culture",
]

result = embedding.embed_documents(documents)
# result = embedding.embed_query("Delhi is the capital of India")
print(str(result))