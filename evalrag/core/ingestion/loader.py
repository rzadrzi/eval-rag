# loader.py
import codecs
import chardet
from typing import List
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


def document_encoding(path: str) -> str:
    with open(path, "rb") as f:
        raw = f.read(4096)  # Read a larger sample for better detection

    # Check for BOM markers first
    if raw.startswith(codecs.BOM_UTF16_LE):
        return "utf-16-le"
    elif raw.startswith(codecs.BOM_UTF16_BE):
        return "utf-16-be"
    elif raw.startswith(codecs.BOM_UTF16):
        return "utf-16"
    elif raw.startswith(codecs.BOM_UTF8):
        return "utf-8-sig"
    elif raw.startswith(codecs.BOM_UTF32_LE):
        return "utf-32-le"
    elif raw.startswith(codecs.BOM_UTF32_BE):
        return "utf-32-be"

    # Use chardet to detect encoding if no BOM is found
    result = chardet.detect(raw)
    encoding = result.get("encoding")
    if encoding:
        return encoding.lower()
    # Return utf-8 if can not other encoding detected
    return "utf-8"


def pdf_loader(path) -> List[Document]:
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs
