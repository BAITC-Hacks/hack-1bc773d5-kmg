"""Print critical monitoring events and their count."""

import json
from pathlib import Path
import sys


def main():
    events_path = Path(__file__).resolve().with_name("events.json")
    try:
        with events_path.open(encoding="utf-8") as source:
            events = json.load(source)
    except FileNotFoundError:
        print("Ошибка: файл events.json не найден.", file=sys.stderr)
        return 1
    except json.JSONDecodeError:
        print("Ошибка: некорректный JSON в events.json.", file=sys.stderr)
        return 1

    count = 0
    for event in events:
        if event["level"] == "critical":
            print(event["event"])
            count += 1
    print(f"критичных {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
