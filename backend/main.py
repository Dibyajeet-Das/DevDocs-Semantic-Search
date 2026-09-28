from fastapi import FastAPI

from backend.SearchService import SearchService

app = FastAPI()

search_service = SearchService()


@app.get("/")
def home():
    return {
        "message": "Welcome to DevDocs Semantic Search"
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }


@app.get("/search")
def search(query: str, top_k: int = 3,category: str = None):

    count = search_service.chroma_service.count_documents()

    print("ChromaDB document count:", count)

    results = search_service.search(
        query=query,
        top_k=top_k,
        category=category
    )

    return results