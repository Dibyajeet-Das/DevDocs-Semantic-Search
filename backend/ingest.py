import logging
from pathlib import Path

from EmbeddingService import EmbeddingService
from ChromaService import ChromaService

logging.basicConfig(level=logging.INFO,format="%(asctime)s | %(levelname)s | %(name)s | %(message)s")

logger = logging.getLogger(__name__)

# Location of our documentation files where we are going to store or add
#DOCUMENTS_PATH = Path("data/documents")
DOCUMENTS_PATH = (Path(__file__).resolve().parent.parent/ "data"/ "documents")

def ingest_documents():

    try:
        logger.info("Document ingestion started.")

        # Create our services
        embedding_service = EmbeddingService()
        chroma_service = ChromaService()

        # Find all .txt files or we can say it will process the documents one by one
        document_files = DOCUMENTS_PATH.glob("*.txt")

        for file_path in document_files:

            logger.info("Processing document: %s",file_path.name)

            # Read the documents
            text = file_path.read_text(
                encoding="utf-8"
            )

            # Generate vector embedding from our text file
            embedding = embedding_service.create_embedding(text)

            # Use filename as document ID
            document_id = file_path.stem

            # Document metadata
            metadata = {
                "source": file_path.name
            }

            # Store document in ChromaDB
            chroma_service.add_document(
                document_id=document_id,
                text=text,
                embedding=embedding,
                metadata=metadata
            )

            logger.info("Document processed successfully: %s",file_path.name)

        total_documents = chroma_service.count_documents()

        logger.info( "Document ingestion completed. Total documents=%s",total_documents)

    except Exception:
        logger.exception("Document ingestion failed.")
        raise

# when we execute our file this think will get called
if __name__ == "__main__":
    ingest_documents()