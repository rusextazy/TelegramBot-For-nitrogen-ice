from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from app.filters.chat_type import ChatTypeFilter

router = Router()


@router.message(
    ChatTypeFilter(chat_type=["group", "supergroup"]),
    Command("reply"))
async def cmd_reply_in_group(msg: Message):
    if len(msg.text.split()) > 1:  # Проверяем, есть ли после команды еще текст
        chat_id, text_new = msg.text.split(maxsplit=2)[1:]
        try:
            await msg.bot.get_chat(chat_id)
            await msg.bot.send_message(chat_id=chat_id, text=text_new)
            await msg.answer(text="✅ Сообщение отправлено Пользователю!")
        except:
            await msg.answer(text="❌ Ваше сообщение не доставлено!\n\n"
                                  "Причина: Убедитесь, что вы ввели правильный формат\n"
                                  "<i>Формат: /reply ID TEXT</i>\n\n"
                                  "<i>Возможно пользователь заблокировал бота, поэтому сообщение не может быть "
                                  "доставлено</i>")
    else:
        await msg.answer(text="Отправь сообщение пользователю с помощью его CHAT_ID и текст в одном сообщении\n\n"
                              "<i>Формат: /reply ID TEXT</i>")
