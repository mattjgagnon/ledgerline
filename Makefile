
.PHONY: build shell test lint format type check sample

build:
	docker compose build --no-cache

shell:
	docker compose run --rm app bash

test:
	docker compose run --rm app pytest -q

lint:
	docker compose run --rm app ruff check src tests

format:
	docker compose run --rm app black src tests

type:
	docker compose run --rm app mypy src

check: lint type test

sample:
	docker compose run --rm app ledgerline reconcile examples/bank.csv examples/ledger.csv --date-window 3
