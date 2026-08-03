from rag.retriever import retrieve
from rag.llm import get_llm
from rag.prompts import QA_PROMPT
from rag.memory import add_message, get_history


def ask_question(question):

    q = question.lower()

    # ==========================
    # Special query routing
    # ==========================

    if "hypothesis" in q or "h1" in q:

        docs = retrieve(question, mode="hypothesis")

    elif "methodology" in q or "method" in q:

        docs = retrieve(question, mode="methodology")

    elif (
        "research question" in q
        or "motivation" in q
        or "contribution" in q
        or "purpose" in q
    ):

        docs = retrieve(
            """
            abstract
            introduction
            research question
            research motivation
            contribution
            purpose of study
            """,
            mode="general",
        )

    else:

        docs = retrieve(question, mode="general")

    context = "\n\n".join(f"""
PAGE {doc.metadata.get('page')}

{doc.page_content}
""" for doc in docs)

    llm = get_llm()

    history = get_history()

    prompt = QA_PROMPT.format(
        context=context,
        history=history,
        question=question,
    )

    response = llm.invoke(prompt)

    add_message("User", question)

    add_message("Assistant", response.content)

    return response.content
