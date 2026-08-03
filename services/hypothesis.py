from rag.retriever import retrieve
from rag.llm import get_llm
from rag.prompts import HYPOTHESIS_PROMPT


def find_hypothesis():

    docs = retrieve("""
    Find the hypothesis development section of the paper.

    Extract every hypothesis:
    H1, H2, H3, H4...

    Prioritize:
    - Introduction
    - Theory development
    - Hypothesis development

    Do not use references or empirical results.
    """)

    context = "\n\n".join(f"""
PAGE: {doc.metadata.get('page_label')}

CONTENT:
{doc.page_content}
""" for doc in docs)

    llm = get_llm()

    prompt = HYPOTHESIS_PROMPT.format(context=context)

    response = llm.invoke(prompt)

    return response.content
