import json


class Evaluation:

    def __init__(self):

        pass

    def validate_json(self, data):

        if isinstance(data, dict):

            return True

        return False

    def calculate_completeness(self, data):

        total = 0
        filled = 0

        def check(value):

            nonlocal total, filled

            if isinstance(value, dict):

                for v in value.values():

                    check(v)

            elif isinstance(value, list):

                total += 1

                if len(value) > 0:
                    filled += 1

            else:

                total += 1

                if value not in [None, "", []]:

                    filled += 1

        check(data)

        if total == 0:

            return 0

        return round(filled / total * 100, 2)

    def evaluate(self, data):

        json_valid = self.validate_json(data)

        completeness = self.calculate_completeness(data)

        overall_score = round(completeness, 2)

        return {
            "json_valid": json_valid,
            "completeness": completeness,
            "overall_score": overall_score,
        }
