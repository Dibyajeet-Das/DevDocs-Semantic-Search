import logging
#from EmbeddingService import EmbeddingService
#from ChromaService import ChromaService

from .EmbeddingService import EmbeddingService
from .ChromaService import ChromaService

logger = logging.getLogger(__name__)

class SearchService:

    def __init__(self):
        try:
            logger.info("Starting SearchService")

            self.embedding_service = EmbeddingService()
            self.chroma_service = ChromaService()

            logger.info("SearchService initialized successfully.")

        except Exception:
            logger.exception("Failed to initialize SearchService")
            raise

    def search(self, query, top_k=3, category=None):
        try:
            logger.info( "Searching documents. query=%s",  query)

            # Convert user's query into a vector
            query_embedding = (
                self.embedding_service.create_embedding(query)
            )

            # Search ChromaDB using that vector
            results = self.chroma_service.search(
                query_embedding=query_embedding,
                top_k=top_k,
                category=category
            )

            # Create a clean response for the API
            searchResults = []

            ids = results["ids"][0]
            documents = results["documents"][0]
            metadatas = results["metadatas"][0]
            distances = results["distances"][0]

            for i in range(len(ids)):
                searchResults.append({
                    "document": metadatas[i]["source"],
                    "content": documents[i],
                    "distance": distances[i]
                })

            logger.info("Search completed successfully.")

            return {
                "query": query,
                "results": searchResults
            }

        except Exception:
            logger.exception("Failed to search documents. query=%s",query )
            raise


# Test SearchService directly
if __name__ == "__main__":

    search_service = SearchService()

    query = "How does Spring manage objects?"

    results = search_service.search(
        query=query,
        top_k=3
    )

    print("\nQuery:")
    print(query)

    print("\nSearch Results:")
    print(results)