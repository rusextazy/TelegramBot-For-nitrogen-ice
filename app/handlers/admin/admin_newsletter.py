import asyncio

from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.filters.admin_type import IsBotAdminFilter
from app.handlers.admin.kb_admin import kb_admin, kb_exit_admin
from app.database.models import get_all_chat_ids


class MyForm(StatesGroup):
    Message_text = State()


router = Router()


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📩 Рассылка")
async def send_message(msg: types.Message, state: FSMContext):
    await msg.answer(text="<b><i>Тут вы можете послать рассылку всем пользователям бота!</i></b>\n\n"
                          "Пришлите фотку с текстом, либо просто текст!", reply_markup=kb_exit_admin)
    await state.set_state(MyForm.Message_text)


@router.message(MyForm.Message_text)
async def send_message_to_users(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    users = await get_all_chat_ids()
    UserCount = 0
    NotUserCount = 0
    for UserID in users:
        try:
            # Формируем сообщение
            await msg.send_copy(UserID)
            await asyncio.sleep(0.036)
            UserCount += 1
        except:
            NotUserCount += 1
            pass
    await msg.bot.send_message(chat_id=msg.from_user.id, text=f"<b><i>📊 Статистика по рассылке</i></b>\n\n"
                                                              f"Отправлено сообщений: <code>{UserCount}</code>\n"
                                                              f"Заблокированных пользователей: <code>{NotUserCount}</code>",
                               reply_markup=kb_admin)
    await state.clear()

