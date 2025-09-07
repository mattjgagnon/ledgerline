from ledgerline.models import Transaction
from ledgerline.rules import amount_equal, date_within, description_overlap, Rule, RuleEngine


def tx(d: str, amt: float, desc: str, src: str):
    return Transaction(date=d, amount=amt, description=desc, source=src)


def test_amount_equal():
    a = tx("2025-01-01", -25.0, "Coffee", "bank")
    b = tx("2025-01-01", -25.0, "Cafe", "ledger")
    assert amount_equal(a, b) is True


def test_date_within():
    a = tx("2025-01-05", -25.0, "Coffee", "bank")
    b = tx("2025-01-02", -25.0, "Coffee", "ledger")
    assert date_within(a, b, days=3) is True
    assert date_within(a, b, days=2) is False


def test_description_overlap():
    a = tx("2025-01-05", -25.0, "STARBUCKS 123", "bank")
    b = tx("2025-01-05", -25.0, "Client Starbucks", "ledger")
    assert description_overlap(a, b, min_tokens=1) is True
    assert description_overlap(a, b, min_tokens=2) is False


def test_rule_engine_all_must_pass():
    a = tx("2025-01-03", -25.0, "Coffee", "bank")
    b = tx("2025-01-01", -25.0, "Coffee", "ledger")
    engine = RuleEngine(Rule("amount", amount_equal), Rule("date", lambda x, y: date_within(x, y, 2)))
    assert engine.passes(a, b) is True
