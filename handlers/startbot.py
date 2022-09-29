from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.simple_row import make_row_keyboard
from data.client import data_manager

from datetime import date
# zh-cn
language_interface = ["RU🇷🇺", "EN🇺🇸", "CH🇨🇳"]

router = Router()
class StartBot(StatesGroup):
    language_selection = State()


@router.message(Command(commands=['start', 'updlang']))
async def command_start_handler(message: Message, state: FSMContext):
    await message.answer(
        text="Привет, Я бот переводчик!😊\n" \
             "Я автоматически определяю язык, на котором ты пишешь.🤔\n" \
             "Выбери язык перевода:",
        reply_markup=make_row_keyboard(language_interface)
    )
    await state.set_state(StartBot.language_selection)


@router.message(StartBot.language_selection, F.text.in_(language_interface))
async def translation_language(message: Message, state: FSMContext):
    await state.update_data(lang_selection=message.text.lower())

    if message.text == "CH🇨🇳":
        lang_user = "zh-cn"
    else:
        lang_user = message.text[0:2].lower()

    data_manager.create_user(name_user=message.from_user.full_name,
                             id_user=message.from_user.id,
                             lang_user=lang_user,
                             created_at=date.today())

    await message.answer(text="Спасибо. Теперь вводи текст для перевода!",
                        reply_markup=ReplyKeyboardRemove())
    data_manager._show_table()
