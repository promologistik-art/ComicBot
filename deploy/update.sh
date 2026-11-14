#!/usr/bin/env bash
set -euo pipefail
cd /opt/comicbot
git pull --ff-only origin main
venv/bin/pip install -r requirements.txt
systemctl daemon-reload
echo "ComicBot обновлён. Состояние таймеров не менялось."
