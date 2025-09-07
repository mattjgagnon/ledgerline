# LedgerLine (MVP) — Dockerized TDD Bank Reconciliation

This is a Docker-first setup so you don't need anything but Docker/Compose locally.

## One-time
```bash
docker compose build
```

## Dev loop
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
