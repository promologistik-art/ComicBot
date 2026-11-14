#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="/opt/comicbot"
VENV_DIR="$REPO_DIR/venv"

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Запустите установку от root: bash deploy/install.sh"
  exit 1
fi

if [[ ! -f /root/comicbot.env ]]; then
  echo "Не найден /root/comicbot.env. Сначала добавьте HF_TOKEN и TELEGRAM_BOT_TOKEN."
  exit 1
fi

for key in HF_TOKEN TELEGRAM_BOT_TOKEN; do
  if ! grep -Eq "^\${key}=.+" /root/comicbot.env; then
    echo "В /root/comicbot.env отсутствует или не заполнен ${key}."
    exit 1
  fi
done

if [[ -d "$REPO_DIR/.git" ]]; then
  git -C "$REPO_DIR" pull --ff-only origin main
elif [[ -e "$REPO_DIR" ]]; then
  echo "$REPO_DIR уже существует, но это не Git-репозиторий. Переместите каталог вручную; установщик не будет его перезаписывать."
  exit 1
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

echo "Проверяем права @zentestmp_bot в @zentestdigest..."
"$VENV_DIR/bin/python" -m comicbot.check_access

echo "Проверяем расписание ежедневного запуска на 09:00 Europe/Moscow..."
systemd-analyze calendar '*-*-* 09:00:00 Europe/Moscow'

# Стартуем однократный таймер только после успешной проверки Telegram.
# Первый выпуск будет через 24 часа после выполнения этой команды.
systemctl enable --now comicbot-initial.timer

echo
echo "ComicBot установлен и расписание активировано."
echo "Первый выпуск: через 24 часа с момента включения таймера."
echo "Следующие выпуски: ежедневно в 09:00 Europe/Moscow."
echo "Состояние: systemctl list-timers --all | grep comicbot"
