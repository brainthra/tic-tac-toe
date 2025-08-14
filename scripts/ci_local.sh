#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   scripts/ci_local.sh           # fast checks (good for pre-commit)
#   scripts/ci_local.sh --full    # full CI-like run incl. coverage (good before push)

MODE="fast"
if [[ "${1:-}" == "--full" ]]; then
  MODE="full"
fi

echo "Python version: $(python -V)"
echo "Mode: ${MODE}"
echo

echo "==> Ruff (lint)"
ruff check .

echo "==> Black (check format)"
black .

echo "==> isort (check imports)"
isort --check-only .

echo "==> mypy (type check)"
mypy .

echo "==> pytest"
if [[ "$MODE" == "full" ]]; then
  # match CI flags (coverage + xml)
  pytest -q --cov=engine --cov=players --cov=cli --cov-report=term-missing --cov-report=xml
else
  # quick run (no coverage)
  pytest -q
fi

echo
echo "Local CI passed (${MODE} mode)"
