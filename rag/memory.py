from collections import deque

MAX_HISTORY = 6

_history = deque(maxlen=MAX_HISTORY)


def add_message(role, content):

    _history.append(
        {
            "role": role,
            "content": content,
        }
    )


def get_history():

    history = ""

    for msg in _history:

        history += f"{msg['role']}: {msg['content']}\n"

    return history


def clear_history():

    _history.clear()
