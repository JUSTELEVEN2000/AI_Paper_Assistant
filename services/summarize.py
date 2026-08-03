from rag.retriever import retrieve
from rag.llm import get_llm
from rag.prompts import SUMMARY_PROMPT


def summarize_paper():

    docs = retrieve("""
        Find the title, abstract, introduction,
        conclusion, contribution, research question,
        methodology, sample, hypothesis.
        """)

    context = "\n\n".join(doc.page_content for doc in docs)

    llm = get_llm()

    prompt = SUMMARY_PROMPT.format(context=context)

    response = llm.invoke(prompt)

    return response.content
