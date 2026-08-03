import json
import re


def extract_json(text: str):
    """
    从LLM输出中提取JSON。
    """

    if text is None:
        return None

    text = text.strip()

    # -------------------------
    # 去掉Markdown代码块
    # -------------------------

    text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^```", "", text)
    text = re.sub(r"```$", "", text)

    text = text.strip()

    # -------------------------
    # 已经是JSON
    # -------------------------

    try:
        return json.loads(text)
    except Exception:
        pass

    # -------------------------
    # 截取第一个{}
    # -------------------------

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        return None

    candidate = text[start : end + 1]

    try:
        return json.loads(candidate)
    except Exception:
        return None


def pretty_json(text: str):

    data = extract_json(text)

    if data is None:
        return text

    return json.dumps(
        data,
        indent=2,
        ensure_ascii=False,
    )


def is_valid_json(text: str):

    return extract_json(text) is not None
