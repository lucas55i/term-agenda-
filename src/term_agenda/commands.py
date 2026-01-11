from datetime import date, time
from .storage import load, save
from .models import Commitment

def list_items():
    items = load()
    if not items:
        print("Nenhum compromisso cadastrado.")
        return

    for i in items:
        status = "✔" if i.done else " "
        t = i.time.strftime("%H:%M") if i.time else "--:--"
        print(f"[{status}] {i.id} | {i.date} {t} | {i.title}")

def add_item(title, d, t=None):
    items = load()
    next_id = max([i.id for i in items], default=0) + 1

    item = Commitment(
        id=next_id,
        title=title,
        date=date.fromisoformat(d),
        time=time.fromisoformat(t) if t else None
    )
    items.append(item)
    save(items)

def mark_done(item_id):
    items = load()
    for i in items:
        if i.id == item_id:
            i.done = True
            save(items)
            return

    print("Compromisso não encontrado")
