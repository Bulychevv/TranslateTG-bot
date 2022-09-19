from email.message import Message
from aiogram import Router
from aiogram.types import Message
from aiogram.filters.text import Text

from googletrans import Translator
from data.client import data_manager

router = Router()
translator = Translator()

@router.message()
async def translate_answer(message: Message):

    lang = data_manager.get_lang(id_user=str(message.from_user.id))
    result = translator.translate(message.text, dest=lang)

    await message.answer(f"{result.text}\n\nДля смены языка - /updlang")
