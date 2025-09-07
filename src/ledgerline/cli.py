from __future__ import annotations

from pathlib import Path

import typer

from .io import read_csv
from .reconciler import reconcile

app = typer.Typer(help="LedgerLine — reconcile bank and ledger CSVs")


@app.command()
def reconcile_cmd(
    bank_csv: Path = typer.Argument(..., exists=True, readable=True),
    ledger_csv: Path = typer.Argument(..., exists=True, readable=True),
    date_window: int = typer.Option(3, help="Allowed date difference in days"),
):
    bank = read_csv(bank_csv, source="bank")
    ledger = read_csv(ledger_csv, source="ledger")
    result = reconcile(bank, ledger, date_window_days=date_window)

    typer.echo(f"Matches: {len(result.matches)}")
    for b, l in result.matches:
        typer.echo(f"  {b.date} {b.amount:>8} :: {b.description}  <=>  {l.date} {l.amount:>8} :: {l.description}")

    typer.echo(f"Unmatched bank: {len(result.bank_unmatched)}")
    typer.echo(f"Unmatched ledger: {len(result.ledger_unmatched)}")


app.command(name="reconcile")(reconcile_cmd)
