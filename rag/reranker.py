from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        print("Loading Reranker...")
        self.model = CrossEncoder("BAAI/bge-reranker-base")

    def rerank(self, question, docs, top_k=5):
        """
        docs: LangChain Document list
        """

        query = question.lower()

        if "hypoth" in query:
            query = "research hypothesis H1 H2 H3 H4"

        elif "method" in query:

            query = (
                "research methodology "
                "sample "
                "variables "
                "regression model "
                "empirical model "
                "fixed effects "
                "estimation "
                "robustness "
                "equation"
            )

        pairs = [(query, doc.page_content) for doc in docs]

        scores = self.model.predict(pairs)
        for score, doc in sorted(zip(scores, docs), reverse=True):
            print("=" * 50)
            print(score)
            print(doc.metadata)
            print(doc.page_content[:500])

        ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)

        print("\n===== RERANK =====")

        for score, doc in ranked[:10]:
            print(
                f"{score:.3f}",
                "PAGE",
                doc.metadata.get("page"),
                doc.page_content[:80].replace("\n", " "),
            )

        print("==================\n")

        return [doc for score, doc in ranked[:top_k]]
