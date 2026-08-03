def detect_section(text):

    text_lower = text.lower()

    # Abstract

    if "abstract" in text_lower:
        return "abstract"

    # Introduction

    introduction_words = [
        "introduction",
        "we investigate",
        "this paper examines",
        "research question",
        "motivation",
    ]

    for word in introduction_words:
        if word in text_lower:
            return "introduction"

    # Literature Review

    literature_words = ["literature review", "previous studies", "prior research"]

    for word in literature_words:
        if word in text_lower:
            return "literature"

    # Hypothesis

    hypothesis_words = ["hypothesis", "hypotheses", "h1", "h2", "h3"]

    for word in hypothesis_words:
        if word in text_lower:
            return "hypothesis"

    # Methodology

    method_words = [
        "methodology",
        "empirical model",
        "regression model",
        "data",
        "sample",
    ]

    for word in method_words:
        if word in text_lower:
            return "methodology"

    # Results

    result_words = ["results", "table", "regression", "coefficient"]

    for word in result_words:
        if word in text_lower:
            return "results"

    # Conclusion

    if "conclusion" in text_lower:
        return "conclusion"

    return "unknown"
