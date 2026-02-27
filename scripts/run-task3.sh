#!/usr/bin/env bash
set -euo pipefail
cd '$(dirname "$0")/../JPMC-tech-task-3-PY3/datafeed'
python3 server3.py &
SERVER_PID=$!
sleep 1
cd ../src && npm start
kill $SERVER_PID
