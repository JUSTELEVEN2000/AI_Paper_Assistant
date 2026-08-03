def classify_question(question):

    q = question.lower()

    if any(word in q for word in ["hypothesis", "hypotheses", "h1", "h2", "h3", "h4"]):
        return "hypothesis"

    if any(
        word in q
        for word in [
            "methodology",
            "method",
            "data",
            "sample",
            "regression",
            "model",
            "variable",
        ]
    ):
        return "methodology"

    if any(
        word in q
        for word in [
            "research question",
            "question",
            "motivation",
            "purpose",
            "objective",
        ]
    ):
        return "introduction"

    if any(
        word in q for word in ["summary", "summarize", "main finding", "conclusion"]
    ):
        return "abstract"

    return "general"
