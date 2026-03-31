#!/usr/bin/env bash
set -euo pipefail
echo 'Verifying all tasks...'
for t in 1 2 3; do
  cd "JPMC-tech-task-$t-PY3"
  python3 -c "import ast; ast.parse(open('server3.py').read())"
  cd ..
done
echo 'All tasks OK'
