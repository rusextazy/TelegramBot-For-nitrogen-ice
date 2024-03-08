from aiogram import types
from aiogram.filters import BaseFilter


class IsBotAdminFilter(BaseFilter):

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def __call__(self, message: types.Message) -> bool:
        # Список ID администраторов вашего бота
        admin_ids = [5779603673, 6352426469, 6628882779]

        # Проверяем, есть ли ID отправителя среди администраторов
        return message.from_user.id in admin_ids
