import json


def json_valid(result: str):

    try:

        json.loads(result)

        return True

    except Exception:

        return False


def completeness(data):

    total = 0
    filled = 0

    def walk(obj):

        nonlocal total, filled

        if isinstance(obj, dict):

            for value in obj.values():

                walk(value)

        elif isinstance(obj, list):

            for value in obj:

                walk(value)

        else:

            total += 1

            if obj not in [
                "",
                None,
                "null",
                "NULL",
                "Not found",
                "Not found in retrieved context.",
            ]:

                filled += 1

    walk(data)

    if total == 0:

        return 0

    return round(filled / total * 100, 1)
