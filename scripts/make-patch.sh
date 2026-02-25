#!/usr/bin/env bash
set -euo pipefail
git format-patch HEAD~1 --stdout > '0001-Create-Patch-File.patch'
