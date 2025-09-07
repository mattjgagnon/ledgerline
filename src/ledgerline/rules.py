from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .models import Transaction


Predicate = Callable[[Transaction, Transaction], bool]


def amount_equal(a: Transaction, b: Transaction) -> bool:
    return a.key_amount() == b.key_amount()


def date_within(a: Transaction, b: Transaction, days: int = 3) -> bool:
    delta = abs((a.date - b.date).days)
    return delta <= days


def description_overlap(a: Transaction, b: Transaction, min_tokens: int = 1) -> bool:
    toks_a = set(a.description.lower().split())
    toks_b = set(b.description.lower().split())
    return len(toks_a & toks_b) >= min_tokens


@dataclass(frozen=True)
class Rule:
    name: str
    predicate: Predicate


class RuleEngine:
    def __init__(self, *rules: Rule):
        self.rules = list(rules)

    def passes(self, bank: Transaction, ledger: Transaction) -> bool:
        return all(r.predicate(bank, ledger) for r in self.rules)
