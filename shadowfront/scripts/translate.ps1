# Run doc translations via Docker (no local pip install).
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
docker compose -f docker-compose.translate.yml run --rm translate @args
