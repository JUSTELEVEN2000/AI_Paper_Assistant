import os

from langchain_community.document_loaders import PyPDFLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):

    print("\nLoading PDF...")

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    print(f"PDF pages: {len(documents)}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=150)

    chunks = splitter.split_documents(documents)

    print(f"Created chunks: {len(chunks)}")

    return chunks
