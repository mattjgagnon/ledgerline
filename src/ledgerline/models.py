from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, field_validator


class Transaction(BaseModel):
    date: date
    amount: float
    description: str
    source: str  # "bank" or "ledger"
    id: Optional[str] = None

    @field_validator("description")
    @classmethod
    def normalize_desc(cls, v: str) -> str:
        return v.strip()

    def key_amount(self) -> float:
        return float(self.amount)
