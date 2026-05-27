import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("research_memory")

model = SentenceTransformer("all-MiniLM-L6-v2")


def save_research(topic, content):
    embedding = model.encode(content).tolist()

    collection.add(
        ids=[topic],
        documents=[content],
        embeddings=[embedding]
    )


def retrieve_research(query):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results
