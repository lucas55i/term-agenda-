import json
from pathlib import Path
from datetime import date, time
from .models import Commitment

DATA_FILE = Path("data/agenda.json")

def load():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE) as f:
        raw = json.load(f)

    items = []
    for r in raw:
        items.append(
            Commitment(
                id=r["id"],
                title=r["title"],
                date=date.fromisoformat(r["date"]),
                time=time.fromisoformat(r["time"]) if r["time"] else None,
                done=r["done"]
            )
        )
    return items

def save(items):
    DATA_FILE.parent.mkdir(exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(
            [
                {
                    "id": i.id,
                    "title": i.title,
                    "date": i.date.isoformat(),
                    "time": i.time.isoformat() if i.time else None,
                    "done": i.done
                }
                for i in items
            ],
            f,
            indent=2
        )
