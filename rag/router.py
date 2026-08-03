def classify_query(question):

    question = question.lower()

    # Research Question
    if any(
        keyword in question
        for keyword in [
            "research question",
            "research objective",
            "purpose",
            "motivation",
            "research gap",
        ]
    ):
        return "introduction"

    # Summary
    elif any(
        keyword in question
        for keyword in ["summary", "summarize", "overview", "main idea"]
    ):
        return "summary"

    # Hypothesis
    elif any(
        keyword in question
        for keyword in ["hypothesis", "hypotheses", "h1", "h2", "h3", "h4"]
    ):
        return "hypothesis"

    # Methodology
    elif any(
        keyword in question
        for keyword in [
            "method",
            "methodology",
            "model",
            "regression",
            "data",
            "sample",
            "variable",
        ]
    ):
        return "methodology"

    else:
        return "general"


def get_search_query(question):

    category = classify_query(question)

    if category == "introduction":

        return """
        Find the abstract, introduction,
        research question,
        motivation,
        research gap,
        and contribution of this paper.
        """

    elif category == "summary":

        return """
        Find the overall paper information,
        abstract,
        introduction,
        theoretical background,
        findings,
        and conclusion.
        """

    elif category == "hypothesis":

        return """
        Find all hypotheses H1 H2 H3 H4,
        theoretical arguments,
        expected relationships.
        """

    elif category == "methodology":

        return """
        Find research methodology,
        data source,
        sample,
        variables,
        regression models,
        empirical strategy.
        """

    else:

        return question
