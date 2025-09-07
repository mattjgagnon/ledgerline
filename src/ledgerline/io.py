from __future__ import annotations

import csv
from pathlib import Path
from typing import List

from .models import Transaction


def read_csv(path: str | Path, source: str) -> List[Transaction]:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: {p}")
    rows: List[Transaction] = []
    with p.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(
                Transaction(
                    date=row["date"],
                    amount=float(row["amount"]),
                    description=row["description"],
                    source=source,
                )
            )
    return rows
