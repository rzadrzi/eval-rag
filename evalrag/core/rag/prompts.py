# rag/prompts.py

from typing import List, Dict

RAG_PROMPT_TEMPLATE = """You are an assistant that answers questions based only on the provided context.

Question:
{question}

Context:
{context_block}

Instructions:
- If the answer is not in the context, say you don't know.
- Answer in a concise and precise way.

Answer:
"""


def build_context_block(contexts: List[Dict], max_chars: int = 4000) -> str:
    parts = []
    total = 0
    for c in contexts:
        txt = c["text"].strip()
        if not txt:
            continue
        if total + len(txt) > max_chars:
            break
        parts.append(txt)
        total += len(txt)
    return "\n\n---\n\n".join(parts)


def build_rag_prompt(question: str, contexts: List[Dict]) -> str:
    context_block = build_context_block(contexts)
    return RAG_PROMPT_TEMPLATE.format(
        question=question,
        context_block=context_block,
    )
