# LedgerLine — Bank Reconciliation

LedgerLine is a Python-based finance service designed to handle bank transaction ingestion, deduplication, and categorization with user-defined rules. It provides statement reconciliation and spend reporting through a clean FastAPI interface. Built with SQLAlchemy, Alembic, and PostgreSQL, LedgerLine demonstrates best practices for building extensible, test-driven backend systems in Python.

## Features list (to be added)
- Transaction import from CSV/OFX formats
- Idempotent deduplication using stable transaction hashes
- Priority-based rule engine for categorization and normalization
- Statement reconciliation with variance reporting
- Spend-by-category reporting endpoints
- FastAPI interface with OpenAPI docs
- Postgres persistence with migrations (Alembic)
- TDD-first architecture with pytest + hypothesis

## Installation

This is a Docker-first setup so you don't need anything but Docker/Compose locally.

### One-time
```bash
docker compose build
```

### Dev loop
```bash
# run tests
make test
# type-check
make type
# lint
make lint
# format
make format
# all checks
make check
```

## Try the sample reconciliation
```bash
make sample
```

## Interactive shell
```bash
make shell
```
