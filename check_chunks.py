from rag.retriever import get_retriever

retriever = get_retriever()


docs = retriever.invoke("hypothesis H1 H2 H3 H4")


for i, doc in enumerate(docs):

    print("\n======================")
    print("DOC", i + 1)

    print("PAGE:", doc.metadata.get("page"))

    print(doc.page_content[:1000])
