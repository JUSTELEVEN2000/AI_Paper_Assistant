from langchain_community.vectorstores import FAISS

from rag.embedding import get_embedding
from rag.reranker import Reranker
from rag.query_rewriter import rewrite_query

DB_PATH = "vector_db"


_retriever = None
_reranker = None


def load_vectorstore():

    embedding = get_embedding()

    db = FAISS.load_local(DB_PATH, embedding, allow_dangerous_deserialization=True)

    return db


def get_retriever():

    global _retriever

    if _retriever is None:

        db = load_vectorstore()

        _retriever = db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 20,
                "fetch_k": 80,
                "lambda_mult": 0.4,
            },
        )

    return _retriever


def get_reranker():

    global _reranker

    if _reranker is None:

        _reranker = Reranker()

    return _reranker


def retrieve(question, mode="general"):

    retriever = get_retriever()

    reranker = get_reranker()

    # ==========================
    # Query expansion
    # ==========================

    if mode == "hypothesis":

        queries = [
            question,
            "H1 hypothesis",
            "H2 hypothesis",
            "H3 hypothesis",
            "H4 hypothesis",
            "we hypothesize",
            "we expect",
            "hypothesize that",
            "baseline model testing hypothesis",
            "theoretical framework",
            "research question",
            "expected relationship",
        ]

    elif mode == "methodology":

        queries = [
            question,
            "methodology",
            "sample methodology",
            "sample selection",
            "data source",
            "dataset",
            "sample period",
            "variables",
            "variable definitions",
            "dependent variable",
            "independent variable",
            "control variable",
            "empirical model",
            "regression model",
            "fixed effects",
            "equation",
            "estimation",
            "OLS",
            "2SLS",
            "difference in differences",
            "instrumental variable",
            "robustness check",
            "appendix table A1",
        ]

    else:

        queries = rewrite_query(question)

    # ==========================
    # Retrieve documents
    # ==========================

    all_docs = []

    seen = set()

    for q in queries:

        docs = retriever.invoke(q)

        for doc in docs:

            key = (
                doc.metadata.get("page"),
                doc.page_content[:100],
            )

            if key not in seen:

                seen.add(key)

                all_docs.append(doc)

    # ===============================
    # DEBUG Retriever
    # ===============================

    print("\n========== Retrieved Chunks ==========\n")

    for i, doc in enumerate(all_docs):

        print(
            f"{i+1:02d}",
            "PAGE",
            doc.metadata.get("page"),
            doc.page_content[:120].replace("\n", " "),
        )

    print("\n======================================\n")

    # ==========================
    # Remove useless chunks
    # ==========================

    filtered_docs = []

    if mode == "hypothesis":

        filtered_docs = all_docs

    else:

        filtered_docs = []

        for doc in all_docs:

            text = doc.page_content.lower()

            if len(text) < 80:
                continue

            if "references" in text:
                continue

            if "received" in text:
                continue

            if "copyright" in text:
                continue

            if "journal of" in text and len(text) < 1000:
                continue

            filtered_docs.append(doc)

    # ==========================
    # Better rerank query
    # ==========================

    rerank_query = question

    if mode == "hypothesis":

        rerank_query = (
            "research hypotheses "
            "H1 H2 H3 H4 "
            "expected relationship "
            "theoretical framework"
        )

    elif mode == "methodology":

        rerank_query = (
            "research methodology "
            "empirical model "
            "data sample "
            "variables "
            "regression"
        )

    docs = reranker.rerank(
        rerank_query,
        filtered_docs,
        top_k=12,
    )

    return docs
