from dataclasses import dataclass
from datetime import date, time
from typing import Optional

@dataclass
class Commitment:
    id: int
    title: str
    date: date
    time: Optional[time]
    done: bool = False
