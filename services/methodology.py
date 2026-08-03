from rag.retriever import retrieve
from rag.llm import get_llm
from rag.prompts import METHODOLOGY_PROMPT

import json


def find_methodology():

    # 使用 Methodology 专用 Retrieval
    docs = retrieve(
        """
        Find the methodology section.

        Focus on:

        - data source
        - sample
        - variables
        - regression model
        - empirical model
        - estimation method
        - robustness check
        - equation
        """,
        mode="methodology",
    )

    # ==========================
    # Build Context
    # ==========================

    context = "\n\n".join(f"""
====================
Page {doc.metadata.get("page")}
====================

{doc.page_content}
""" for doc in docs)

    llm = get_llm()

    prompt = METHODOLOGY_PROMPT.format(context=context)

    response = llm.invoke(prompt)

    text = response.content.strip()

    # ==========================
    # JSON Validation
    # ==========================

    try:

        parsed = json.loads(text)

        return json.dumps(
            parsed,
            indent=2,
            ensure_ascii=False,
        )

    except Exception:

        return text
