#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/opt/comicbot"
VENV_DIR="$REPO_DIR/venv"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Запустите установку от root: sudo bash deploy/install.sh"
  exit 1
fi

if [[ ! -f /root/comicbot.env ]]; then
  echo "Не найден /root/comicbot.env. Сначала создайте env-файл с HF_TOKEN и TELEGRAM_BOT_TOKEN."
  exit 1
fi

if ! grep -q '^TELEGRAM_BOT_TOKEN=.' /root/comicbot.env; then
  echo "В /root/comicbot.env отсутствует TELEGRAM_BOT_TOKEN."
  exit 1
fi

install -d -m 0755 "$REPO_DIR"
if [[ -d "$REPO_DIR/.git" ]]; then
  git -C "$REPO_DIR" pull --ff-only origin main
else
  git clone https://github.com/promologistik-art/ComicBot.git "$REPO_DIR"
fi

python3 -m venv "$VENV_DIR"
"$VENV_DIR/bin/pip" install --upgrade pip
"$VENV_DIR/bin/pip" install -r "$REPO_DIR/requirements.txt"

install -d -m 0755 /var/lib/comicbot/generated /var/lib/comicbot/state /var/log/comicbot
chmod 600 /root/comicbot.env

install -m 0644 "$REPO_DIR/deploy/comicbot.service" /etc/systemd/system/comicbot.service
install -m 0644 "$REPO_DIR/deploy/comicbot-daily.timer" /etc/systemd/system/comicbot-daily.timer
install -m 0644 "$REPO_DIR/deploy/comicbot-initial.service" /etc/systemd/system/comicbot-initial.service
install -m 0644 "$REPO_DIR/deploy/comicbot-initial.timer" /etc/systemd/system/comicbot-initial.timer

systemctl daemon-reload
"$VENV_DIR/bin/python" -m comicbot.check_access

echo
echo "Установка завершена. Проверка доступа к Telegram успешна."
echo "Первый запуск будет через 24 часа после включения таймера."
echo "После первого запуска включится ежедневный таймер на 09:00 Europe/Moscow."
echo "Включить первый таймер: systemctl enable --now comicbot-initial.timer"
