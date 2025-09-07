from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Tuple

from .models import Transaction
from .rules import Rule, RuleEngine, amount_equal, date_within


@dataclass
class ReconcileResult:
    matches: List[Tuple[Transaction, Transaction]]
    bank_unmatched: List[Transaction]
    ledger_unmatched: List[Transaction]


def reconcile(
    bank: Iterable[Transaction],
    ledger: Iterable[Transaction],
    date_window_days: int = 3,
) -> ReconcileResult:
    engine = RuleEngine(
        Rule("amount_equal", amount_equal),
        Rule("date_within", lambda a, b: date_within(a, b, days=date_window_days)),
    )
    bank_list = list(bank)
    ledger_list = list(ledger)

    matches: List[Tuple[Transaction, Transaction]] = []
    matched_ledger_indices: set[int] = set()

    for b in bank_list:
        for idx, l in enumerate(ledger_list):
            if idx in matched_ledger_indices:
                continue
            if engine.passes(b, l):
                matches.append((b, l))
                matched_ledger_indices.add(idx)
                break

    bank_unmatched = [b for b in bank_list if b not in {m[0] for m in matches}]
    ledger_unmatched = [l for i, l in enumerate(ledger_list) if i not in matched_ledger_indices]

    return ReconcileResult(matches=matches, bank_unmatched=bank_unmatched, ledger_unmatched=ledger_unmatched)
