from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command

from app.keyboards.reply import kb_menu
from app.filters.admin_type import IsBotAdminFilter
from app.handlers.admin.kb_admin import kb_admin, kb_admin_text


router = Router()


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "🔙 Назад")
async def main_menu(msg: types.Message, state: FSMContext):
    await state.clear()
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_admin)


@router.message(IsBotAdminFilter(is_admin=True),
                Command("admin_panel"))
async def admin_start(msg: types.Message):
    await msg.answer(text="Поздравляю! Вы вошли в Админ_Панель", reply_markup=kb_admin)


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📊 Статистика")
async def main_menu(msg: types.Message):
    await msg.reply(text="В разработке", reply_markup=kb_admin)


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📄 Поменять текст")
async def change_price(msg: types.Message):
    await msg.answer(text="Тут вы можете поменять текст для прайса или контактов!\nВыбери на клавиатуре!",
                     reply_markup=kb_admin_text)


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "🔙 Вернуться в user_menu")
async def change_price(msg: types.Message):
    await msg.answer(text="Вы вернулись в меню!", reply_markup=kb_menu)
