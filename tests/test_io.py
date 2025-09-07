from pathlib import Path

from ledgerline.io import read_csv


def test_read_csv_parses_transactions(tmp_path: Path):
    csv_path = tmp_path / "bank.csv"
    csv_path.write_text("date,amount,description\n2025-01-02,-10.50,Test\n")
    items = read_csv(csv_path, source="bank")
    assert len(items) == 1
    t = items[0]
    assert t.source == "bank"
    assert str(t.date) == "2025-01-02"
    assert t.amount == -10.50
    assert t.description == "Test"
