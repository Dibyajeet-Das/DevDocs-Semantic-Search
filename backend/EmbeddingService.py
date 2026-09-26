import logging
from sentence_transformers import SentenceTransformer

logger = logging.getLogger(__name__)

class EmbeddingService:

    def __init__(self):
        try:
            logger.info("embedding model || Start")
            #SentenceTransformer -> it is Python library/class which is used to convert
            #                       the text into vector embedding
            # The SentenceTransformer library loads the pretrained model.
            # the model will be loaded once
            self.model = SentenceTransformer("all-MiniLM-L6-v2")

            logger.info("Embedding model loaded successfully.")

        except Exception:

            logger.exception("Failed to load embedding model")

            raise

    def create_embedding(self, text):
        try:
            logger.info("Creating vector embedding for text")
            #converts teh text into vector embedding
            embedding = self.model.encode(text).tolist()

            logger.info("Embedding created successfully. Dimensions=%s",len(embedding))

            return embedding

        except Exception:
            logger.exception("Failed to create embedding")
            raise