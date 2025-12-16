# loader.py
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def pdf_loader(path) -> List[Document]:
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs
