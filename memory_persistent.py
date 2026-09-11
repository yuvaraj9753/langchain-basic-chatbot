import json
import os


MEMORY_FILE = "chat_history.json"


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, OSError):
        return []


def save_memory(messages):

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(
            messages,
            file,
            indent=4,
            ensure_ascii=False
        )


def clear_memory():

    if os.path.exists(MEMORY_FILE):
        os.remove(MEMORY_FILE)