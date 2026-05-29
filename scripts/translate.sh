#!/usr/bin/env bash
# Run doc translations via Docker (no local pip install).
set -euo pipefail
cd "$(dirname "$0")/.."
docker compose -f docker-compose.translate.yml run --rm translate "$@"
