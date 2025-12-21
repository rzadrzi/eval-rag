# indexing.py
from ingestion.loader import pdf_loader
from ingestion.chunkers import text_splitter
from ingestion.embedding import get_embedding_model
from ingestion.vector_store import vector_store_

from core.config import load_config


class Indexing:
    def __init__(self) -> None:
        setting = load_config().ingestion

        docs = pdf_loader(path=setting.data_dir)

        splits = text_splitter(
            docs=docs,
            chunk_size=setting.default_chunk_size,
            chunk_overlap=setting.default_chunk_overlap,
        )

        embedding = get_embedding_model(provider_name=setting.provider_name)

        vector_store_(
            embeddings=embedding,
            splits=splits,
            vector_store_path=setting.vector_store_path,
        )
