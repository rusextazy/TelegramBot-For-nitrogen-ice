from typing import Callable, Awaitable, Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message
from app.keyboards.inline import kb_subscription


class CheckSubscription(BaseMiddleware):

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            msg: Message,
            data: Dict[str, Any]
    ) -> Any:
        """ Проверка подписки на канал

        - [!] Чтобы все работало, бот должен состоять в группе/канале с правами администратора.
        """

        chat_member = await msg.bot.get_chat_member("-1002031293786", msg.from_user.id)

        if chat_member.status == "left":
            await msg.answer(
                "📲 <b>Подписка на канал</b>\n\nЧтобы использовать бот, требуется подписаться на канал.\n\n"
                "<b>Подпишитесь на канал и нажмите кнопку 'Проверить'.</b>", reply_markup=kb_subscription)
        else:
            return await handler(msg, data)
