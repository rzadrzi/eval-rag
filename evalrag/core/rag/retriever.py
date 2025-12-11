# rag/retriever.py

from typing import List, Dict


class Retriever:
    def __init__(self, vector_client, embedder, top_k: int = 5):
        self.vector_client = vector_client
        self.embedder = embedder
        self.top_k = top_k

    def retriever(self):
        pass
