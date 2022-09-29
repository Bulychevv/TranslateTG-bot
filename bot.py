import asyncio
import logging

from aiogram import Bot, Dispatcher, types, Router
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.filters.text import Text
from aiogram.filters.content_types import ContentTypesFilter
from aiogram.fsm.storage.memory import MemoryStorage

from config import TOKEN
from handlers import startbot, translate
from data.client import data_manager


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    # data_manager._clear_users()

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(TOKEN)
    
    dp.include_router(startbot.router)
    dp.include_router(translate.router)
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())

