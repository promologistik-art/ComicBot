from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    hf_token: str
    telegram_token: str
    channel_id: str
    hero_reference: Path
    output_dir: Path
    state_dir: Path
    log_dir: Path
    env_file: Path

    @classmethod
    def load(cls) -> "Settings":
        env_file = Path(os.getenv("COMICBOT_ENV", "/root/comicbot.env"))
        if not env_file.is_file():
            raise RuntimeError(f"Не найден env-файл: {env_file}")
        load_dotenv(env_file, override=False)

        required = ("HF_TOKEN", "TELEGRAM_BOT_TOKEN")
        missing = [name for name in required if not os.getenv(name)]
        if missing:
            raise RuntimeError(
                "В env-файле не заданы обязательные переменные: "
                + ", ".join(missing)
            )

        return cls(
            hf_token=os.environ["HF_TOKEN"],
            telegram_token=os.environ["TELEGRAM_BOT_TOKEN"],
            channel_id=os.getenv("TELEGRAM_CHANNEL_ID", "@zentestdigest"),
            hero_reference=Path(os.getenv("HERO_REFERENCE", "/root/hero_qwen_v1.png")),
            output_dir=Path(os.getenv("OUTPUT_DIR", "/var/lib/comicbot/generated")),
            state_dir=Path(os.getenv("STATE_DIR", "/var/lib/comicbot/state")),
            log_dir=Path(os.getenv("LOG_DIR", "/var/log/comicbot")),
            env_file=env_file,
        )
