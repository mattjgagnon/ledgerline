from ledgerline.models import Transaction
from ledgerline.reconciler import reconcile


def t(date: str, amount: float, desc: str, src: str) -> Transaction:
    return Transaction(date=date, amount=amount, description=desc, source=src)


def test_reconcile_matches_and_unmatched():
    bank = [
        t("2025-08-01", -25.0, "STARBUCKS #123", "bank"),
        t("2025-08-03", 1500.0, "ACME CORP PAYROLL", "bank"),
        t("2025-08-05", -60.0, "CHECK 1022", "bank"),
    ]
    ledger = [
        t("2025-08-01", -25.0, "Coffee with client", "ledger"),
        t("2025-08-03", 1500.0, "Paycheck", "ledger"),
        t("2025-08-06", -60.0, "Check #1022 - Rent", "ledger"),
    ]

    result = reconcile(bank, ledger, date_window_days=3)

    assert len(result.matches) == 3
    assert len(result.bank_unmatched) == 0
    assert len(result.ledger_unmatched) == 0
