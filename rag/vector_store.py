from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from rag.loader import load_pdf


def create_vector_store(pdf_path):

    print("\nLoading Embedding Model...")

    embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

    documents = load_pdf(pdf_path)

    print("\nCreating Vector Database...")

    db = FAISS.from_documents(documents, embedding)

    db.save_local("vector_db")

    print("\nVector database saved!")

    return db
