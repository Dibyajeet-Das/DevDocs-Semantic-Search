import logging
import chromadb
from pathlib import Path

#__name__ represents the current module name where the logs will be generated.
logger = logging.getLogger(__name__)

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# ChromaDB database location
CHROMA_DB_PATH = BASE_DIR / "chroma_db"


class ChromaService:
    #It will get called automatically when we create an object
    #self -> it is just like this keyword calling the current value
    def __init__(self):
        try:
            logger.info("Initializing ChromaDB || Start ")
            #Create connection
            self.client = chromadb.PersistentClient(
                path=str(CHROMA_DB_PATH)
            )
            #try to connect with the collection if not there then create it
            self.collection = self.client.get_or_create_collection(
                name="devdocs"
            )

            logger.info("ChromaDB initialized successfully. Collection: %s",self.collection.name)

        except Exception:
            logger.exception("Failed to initialize ChromaDB")
            raise

    #Take a document from the user then store it in our vector db
    def add_document(self, document_id, text, embedding, metadata):
        try:

            logger.info("Adding document to ChromaDB. document_id=%s",document_id)
            # Here self is used so that the collection will belong to this current object or class only
            # self.collection.add-> adding the data in the current collection
            # metadatas -> addition information about the document
            self.collection.add(
                ids=[document_id],
                documents=[text],
                embeddings=[embedding],
                metadatas=[metadata]
            )

            logger.info( "Document added successfully. document_id=%s",document_id)

        except Exception:
            logger.exception("Failed to add document. document_id=%s",document_id)
            raise

    #It tells how many documents are being stored in the db
    def count_documents(self):
        try:
            count = self.collection.count()

            logger.info("Total documents in ChromaDB: %s",count)
            return count

        except Exception:
            logger.exception("Failed to count documents")
            raise


    # Search the document in the Db for the user to return the response
    def search(self, query_embedding, top_k=3):
        try:
            logger.info("Searching ChromaDB. top_k=%s",top_k)

            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )

            logger.info("ChromaDB search completed successfully.")

            return results

        except Exception:
            logger.exception( "Failed to search ChromaDB")
            raise