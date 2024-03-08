from aiogram import Router, types
from aiogram.filters import Command

from app.keyboards.reply import kb_menu
from app.database.models import check_user_to_db

router = Router()


@router.message(Command("start"))
async def start_cmd(msg: types.Message):
    name = msg.from_user.username
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    await msg.answer(text="Добро пожаловать.", reply_markup=kb_menu)


@router.message(Command("help"))
async def start_cmd(msg: types.Message):
    name = msg.from_user.username
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    await msg.answer(text="for help bot")
