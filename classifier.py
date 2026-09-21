"""Classify messages and print short Russian draft responses using keywords."""

from pathlib import Path


def classify(message):
    """Complaint keywords take priority over requests for information."""
    text = message.casefold()
    if any(word in text for word in ("очередь", "холодная", "пропал", "не работает")):
        return "жалоба"
    if any(word in text for word in ("справк", "где", "как получить")):
        return "справка"
    return "другое"


def draft_response(category):
    return {
        "справка": "Уточните детали запроса, чтобы мы могли предоставить информацию.",
        "жалоба": "Спасибо за сообщение. Уточните место и время проблемы.",
        "другое": "Уточните детали запроса, и мы подскажем дальнейшие шаги.",
    }[category]


def main():
    messages_path = Path(__file__).resolve().with_name("messages.txt")
    with messages_path.open(encoding="utf-8") as messages:
        for line in messages:
            message = line.strip()
            if not message:
                continue
            category = classify(message)
            print(f"Сообщение: {message}")
            print(f"Категория: {category}")
            print(f"Черновик ответа: {draft_response(category)}")
            print()


if __name__ == "__main__":
    main()
