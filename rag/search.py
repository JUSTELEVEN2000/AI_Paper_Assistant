from rag.retriever import get_retriever

retriever = get_retriever()


def retrieve(query):

    docs = retriever.invoke(query)

    return docs


def retrieve_for_summary():

    queries = [
        "abstract",
        "introduction",
        "research question",
        "contribution",
        "conclusion",
    ]

    all_docs = []

    seen = set()

    for q in queries:

        docs = retriever.invoke(q)

        for doc in docs:

            text = doc.page_content

            if text not in seen:

                seen.add(text)

                all_docs.append(doc)

    return all_docs
