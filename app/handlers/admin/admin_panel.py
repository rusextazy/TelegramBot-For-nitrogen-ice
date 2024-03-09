from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import FSInputFile

from app.keyboards.reply import kb_menu
from app.filters.admin_type import IsBotAdminFilter
from app.handlers.admin.kb_admin import kb_admin, kb_admin_text
from app.database.models import count_users_in_db, count_total_orders

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
    total_users = await count_users_in_db()
    total_orders = await count_total_orders()
    photo_main = FSInputFile('app/photo/main.png')
    await msg.answer_photo(photo=photo_main, caption=f"<b><i>Общая статистика нашего проекта:</i></b>\n\n"
                                                     f"🫂 Всего Пользователей: <code>{total_users}</code>\n"
                                                     f"👨‍💻 Заявок за весь период: <code>{total_orders}</code>",
                           reply_markup=kb_admin)


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📄 Поменять текст")
async def change_price(msg: types.Message):
    await msg.answer(text="Тут вы можете поменять текст для прайса или контактов!\nВыбери на клавиатуре!",
                     reply_markup=kb_admin_text)


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "🔙 Вернуться в user_menu")
async def change_price(msg: types.Message):
    await msg.answer(text="Вы вернулись в меню!", reply_markup=kb_menu)
