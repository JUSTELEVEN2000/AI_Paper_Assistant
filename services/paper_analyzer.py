from rag.retriever import get_retriever
from rag.llm import get_llm
from rag.prompts import SUMMARY_PROMPT, HYPOTHESIS_PROMPT, METHODOLOGY_PROMPT, QA_PROMPT

from rag.search import retrieve_for_summary


class PaperAnalyzer:

    def __init__(self):

        self.retriever = get_retriever()

        self.llm = get_llm()

    def _format_docs(self, docs):

        filtered_docs = []

        for doc in docs:

            content = doc.page_content

            # remove reference section noise
            if "References" in content:
                continue

            page = doc.metadata.get("page_label", doc.metadata.get("page", "unknown"))

            filtered_docs.append(f"""
PAGE {page}

{content}
""")

        return "\n\n".join(filtered_docs)

    def _retrieve(self, query):

        docs = self.retriever.invoke(query)

        return self._format_docs(docs)

    def summarize(self):

        docs = retrieve_for_summary()

        context = self._format_docs(docs)

        prompt = SUMMARY_PROMPT.format(context=context)

        response = self.llm.invoke(prompt)

        return response.content

    def find_hypothesis(self):

        queries = [
            "hypothesis H1 H2 H3 H4 theoretical development",
            "research hypotheses expected relationship",
        ]

        contexts = []

        for q in queries:

            contexts.append(self._retrieve(q))

        context = "\n\n".join(contexts)

        prompt = HYPOTHESIS_PROMPT.format(context=context)

        response = self.llm.invoke(prompt)

        return response.content

    def find_methodology(self):

        methodology_queries = [
            "sample data source database dataset firms observations",
            "variable definitions dependent variable independent variable control variables",
            "baseline model regression equation empirical model",
            "fixed effects estimation method",
            "robustness checks endogeneity test instrumental variable",
        ]

        contexts = []

        for q in methodology_queries:

            contexts.append(self._retrieve(q))

        context = "\n\n".join(contexts)

        prompt = METHODOLOGY_PROMPT.format(context=context)

        response = self.llm.invoke(prompt)

        return response.content

    def ask(self, question):

        context = self._retrieve(question)

        prompt = QA_PROMPT.format(context=context, question=question, history="")

        response = self.llm.invoke(prompt)

        return response.content
