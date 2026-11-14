from __future__ import annotations

import asyncio
from pathlib import Path

from telegram import Bot
from telegram.request import HTTPXRequest

from .config import Settings


async def publish_photo(settings: Settings, photo: Path, caption: str) -> int:
    request = HTTPXRequest(
        connect_timeout=30,
        read_timeout=180,
        write_timeout=180,
        pool_timeout=30,
    )
    async with Bot(token=settings.telegram_token, request=request) as bot:
        message = await bot.send_photo(
            chat_id=settings.channel_id,
            photo=photo.open("rb"),
            caption=caption,
        )
        return message.message_id


def publish_photo_sync(settings: Settings, photo: Path, caption: str) -> int:
    return asyncio.run(publish_photo(settings, photo, caption))
