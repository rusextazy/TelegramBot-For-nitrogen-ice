from aiogram import F, Router, types, Bot

from app.keyboards.reply import kb_menu
from app.keyboards.inline import kb_subscription

router = Router()


@router.callback_query(F.data.in_('sub_check'))
async def sub_check(callback: types.CallbackQuery, bot: Bot):
    if callback.data == 'sub_check':
        check = await bot.get_chat_member("-1002031293786", callback.from_user.id)
        if check.status in ["member", "creator", "administrator"]:
            await callback.message.answer(text=f"Привет, {callback.from_user.first_name}\nДобро пожаловать", reply_markup=kb_menu)
            await callback.message.delete()
        else:
            await callback.answer(text="Вы не подписались. Попробуйте ещё раз. ✨", reply_markup=kb_subscription)
