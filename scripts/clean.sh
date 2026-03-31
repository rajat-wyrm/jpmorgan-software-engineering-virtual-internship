#!/usr/bin/env bash
set -euo pipefail
find . -type d -name node_modules -exec rm -rf {} + 2>/dev/null || true
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
echo 'Cleaned.'
