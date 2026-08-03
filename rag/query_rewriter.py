from rag.llm import get_llm

llm = get_llm()


def rewrite_query(question: str):

    prompt = f"""
You are an expert research assistant.

Rewrite the following question into several different search queries.

The rewritten queries should use different academic expressions.

Return ONLY the queries.

Question:

{question}
"""

    response = llm.invoke(prompt)

    queries = [
        q.strip("-•1234567890. ").strip()
        for q in response.content.split("\n")
        if q.strip()
    ]

    queries.append(question)

    return list(set(queries))
