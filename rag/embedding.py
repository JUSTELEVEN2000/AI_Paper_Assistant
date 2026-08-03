from langchain_huggingface import HuggingFaceEmbeddings

_embedding = None


def get_embedding():
    """
    Singleton Pattern
    整个程序只加载一次Embedding模型
    """

    global _embedding

    if _embedding is None:
        print("Loading Embedding Model...")
        _embedding = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base")

    return _embedding
