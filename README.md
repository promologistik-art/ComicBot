# ComicBot

Отдельный Telegram-бот для ежедневной генерации авторских комиксов и публикации в Telegram.

## Текущая конфигурация

- Telegram-бот: `@zentestmp_bot`
- Канал: `@zentestdigest`
- Генератор: Hugging Face Space `Qwen/Qwen-Image-2.1`
- Референс героини на VPS: `/root/hero_qwen_v1.png`
- Python: 3.12
- Секреты: только локальный файл `/root/comicbot.env`, никогда не коммитить.

## Расписание

Первый запуск планируется через 24 часа после включения `comicbot-initial.timer`. После его успешного выполнения автоматически включается ежедневная публикация в 09:00 по часовому поясу `Europe/Moscow`. Системный часовой пояс VPS остаётся UTC.

## Env-файл VPS

В `/root/comicbot.env` должны быть заданы:

```dotenv
HF_TOKEN=...
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHANNEL_ID=@zentestdigest
HERO_REFERENCE=/root/hero_qwen_v1.png
```

Не публикуйте содержимое этого файла и не добавляйте его в Git.

## Установка на VPS

```bash
git clone https://github.com/promologistik-art/ComicBot.git /opt/comicbot
cd /opt/comicbot
bash deploy/install.sh
```

Скрипт проверит токены, установит зависимости, проверит права бота в канале и установит systemd units. Он не включает расписание автоматически.

После успешной проверки включить первый запуск:

```bash
systemctl enable --now comicbot-initial.timer
```

Проверка:

```bash
systemctl list-timers --all | grep comicbot
journalctl -u comicbot-initial.service -n 100 --no-pager
journalctl -u comicbot.service -n 100 --no-pager
```

## Ручной запуск и тесты

Проверка доступа к Telegram без публикации:

```bash
COMICBOT_ENV=/root/comicbot.env /opt/comicbot/venv/bin/python -m comicbot.check_access
```

Генерация без публикации:

```bash
COMICBOT_ENV=/root/comicbot.env /opt/comicbot/venv/bin/python -m comicbot.runner --dry-run
```

Обычный запуск публикует выпуск и записывает маркер даты в `/var/lib/comicbot/state`, чтобы не допустить повторную публикацию за тот же день. `--force` отключает эту защиту и применять его следует только осознанно.

## Содержание

История первого сезона — «Ящик Пандоры: семейный VPN». Промпты первых четырёх эпизодов находятся в `comicbot/prompts.py`. Генерация использует референс героини и просит менять позу, одежду и окружение. Сохранение точного лица при радикальной смене позы зависит от модели и не может быть гарантировано.
