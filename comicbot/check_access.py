from __future__ import annotations

import asyncio

from telegram import Bot
from telegram.request import HTTPXRequest

from .config import Settings


async def main() -> None:
    settings = Settings.load()
    request = HTTPXRequest(connect_timeout=20, read_timeout=30, write_timeout=30)
    async with Bot(token=settings.telegram_token, request=request) as bot:
        me = await bot.get_me()
        print(f"Telegram bot: @{me.username} (id={me.id})")
        chat = await bot.get_chat(settings.channel_id)
        print(f"Канал: {chat.title or chat.username or settings.channel_id}")
        member = await bot.get_chat_member(settings.channel_id, me.id)
        status = member.status
        can_post = getattr(member, "can_post_messages", None)
        print(f"Статус бота в канале: {status}")
        print(f"Право публикации: {can_post}")
        if status not in ("administrator", "creator"):
            raise RuntimeError("Бот не является администратором канала.")
        if can_post is False:
            raise RuntimeError("У бота нет права публикации сообщений.")
        print("Доступ к публикации подтверждён.")


if __name__ == "__main__":
    asyncio.run(main())
