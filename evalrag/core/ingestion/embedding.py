from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings


def get_embedding_model(provider_name: str = "HF"):
    if provider_name == "HF":
        return HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-mpnet-base-v2"
        )
    elif provider_name == "OPENAI":
        return OpenAIEmbeddings(model="text-embedding-3-large")
