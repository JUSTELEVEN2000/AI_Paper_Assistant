from langchain_ollama import ChatOllama


class PaperAnalyzer:

    def __init__(self, retriever):

        self.retriever = retriever

        self.llm = ChatOllama(model="qwen2.5:7b", temperature=0.3)

    def search_paper(self, keywords):

        docs = self.retriever.invoke(keywords)

        context = "\n\n".join([doc.page_content for doc in docs])

        return context

    def ask_llm(self, question, context):

        prompt = f"""

You are an academic research assistant.

Your task is to analyze an academic paper.

Rules:

1. Only use the provided paper content.
2. Do not guess or create information.
3. If information is unclear, say:
"I cannot find this information in the paper."
4. Mention page numbers when available.
5. Be precise and academic.

Paper content:

{context}

Question:

{question}

"""

        response = self.llm.invoke(prompt)

        return response.content

    def summarize(self):

        question = """

Analyze this paper and summarize:

1. Research question

2. Theoretical background

3. Hypothesis

4. Data and sample

5. Methodology

6. Main findings

7. Contribution


"""

        context = self.search_paper(
            "research question hypothesis methodology data findings contribution"
        )

        return self.ask_llm(question, context)

    def find_hypothesis(self):

        question = """

Find all hypotheses in this paper.

For each hypothesis explain:

- Hypothesis number
- Expected relationship
- Theoretical reason


"""

        context = self.search_paper("hypothesis H1 H2 H3 theoretical prediction")

        return self.ask_llm(question, context)

    def find_methodology(self):

        question = """

Explain the methodology of this paper.

Include:

- Dataset
- Sample period
- Variables
- Regression model
- Identification strategy


"""

        context = self.search_paper(
            "data sample regression model methodology empirical strategy"
        )

        return self.ask_llm(question, context)
