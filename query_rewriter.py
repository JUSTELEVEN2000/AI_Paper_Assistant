class QueryRewriter:

    def rewrite(self, question: str):

        q = question.lower()

        if "hypothesis" in q or "h1" in q:

            return (
                "hypothesis H1 H2 H3 "
                "we hypothesize "
                "prediction "
                "theoretical development"
            )

        elif "method" in q:

            return (
                "methodology "
                "empirical strategy "
                "regression "
                "dataset "
                "sample "
                "variable"
            )

        elif "data" in q:

            return "sample " "dataset " "observation " "period " "firm"

        elif "research question" in q or "purpose" in q:

            return (
                "research question " "objective " "purpose " "introduction " "abstract"
            )

        elif "finding" in q or "result" in q:

            return "results " "finding " "conclusion " "discussion"

        else:

            return question
