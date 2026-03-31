#!/usr/bin/env bash
set -euo pipefail
cd '$(dirname "$0")/../JPMC-tech-task-1-PY3'
python3 server3.py &
SERVER_PID=$!
sleep 1
python3 client3.py
kill $SERVER_PID
