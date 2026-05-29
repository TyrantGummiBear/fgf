# Repair locale markdown links (Docker)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
docker compose -f docker-compose.translate.yml run --rm fix-links @args
