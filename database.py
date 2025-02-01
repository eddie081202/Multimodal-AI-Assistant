from pinecone import Pinecone
from app.config import Config

class VectorDB:
    def __init__(self):
        # Initialize Pinecone client
        self.pc = Pinecone(api_key=Config.PINECONE_API_KEY)
        self.index = self.pc.Index(Config.PINECONE_INDEX)
    
    def upsert_context(self, user_id: str, embedding: list) -> None:
        self.index.upsert(vectors=[(user_id, embedding)])
    
    def retrieve_context(self, query_embedding: list, k: int = 3) -> list:
        results = self.index.query(vector=query_embedding, top_k=k)
        return [match["id"] for match in results["matches"]]