from __future__ import annotations

import argparse
import json
import logging
import os
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from .config import Settings
from .generator import generate_daily_image
from .publisher import publish_photo_sync

MOSCOW = ZoneInfo("Europe/Moscow")


def setup_logging(log_dir: Path) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_dir / "comicbot.log", encoding="utf-8"),
        ],
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate and publish daily ComicBot episode")
    parser.add_argument("--force", action="store_true", help="Ignore today's success marker")
    parser.add_argument("--dry-run", action="store_true", help="Generate image but do not publish")
    args = parser.parse_args()

    settings = Settings.load()
    setup_logging(settings.log_dir)
    today = datetime.now(MOSCOW).date()
    settings.state_dir.mkdir(parents=True, exist_ok=True)
    marker = settings.state_dir / f"published_{today.isoformat()}.json"

    if marker.exists() and not args.force:
        logging.info("Выпуск за %s уже опубликован. Повтор пропущен.", today)
        return 0

    logging.info("Начинаем выпуск за %s", today)
    image, caption = generate_daily_image(settings, today)

    if args.dry_run:
        logging.info("Тестовый режим: изображение создано, публикация пропущена: %s", image)
        return 0

    message_id = publish_photo_sync(settings, image, caption)
    record = {
        "date": today.isoformat(),
        "published_at": datetime.now(MOSCOW).isoformat(),
        "channel": settings.channel_id,
        "message_id": message_id,
        "image": str(image),
    }
    temporary = marker.with_suffix(".tmp")
    temporary.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
    temporary.replace(marker)
    logging.info("Опубликовано в %s, message_id=%s", settings.channel_id, message_id)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
