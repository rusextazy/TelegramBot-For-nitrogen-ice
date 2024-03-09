from aiogram import F, Router, types

from app.keyboards.inline import kb_price
from app.database.models import get_text
from app.database.models import check_user_to_db

router = Router()


@router.callback_query(F.data.in_(('loading_works', 'a_liquid_nitrogen', 'dry_ice', 'rental_of_thermoses')))
async def price_get(callback: types.CallbackQuery):
    name = callback.from_user.username
    chat_id = callback.from_user.id
    await check_user_to_db(name, chat_id)
    if callback.data == 'loading_works':
        result = await get_text(id_text=1)
        loading_works = result.replace(r'\n', '\n')
        await callback.message.edit_text(f"<b><i>Прайс на разгрузочно-погрузочные работы при заправке сосудов "
                                         f"Дьюара</i></b>\n\n"
                                         f"{loading_works}", reply_markup=kb_price)
    if callback.data == 'a_liquid_nitrogen':
        result = await get_text(id_text=2)
        loading_works = result.replace(r'\n', '\n')
        await callback.message.edit_text(f"<b><i>Жидкий азот</i></b>\n\n"
                                         f"{loading_works}", reply_markup=kb_price)
    if callback.data == 'dry_ice':
        result = await get_text(id_text=3)
        loading_works = result.replace(r'\n', '\n')
        await callback.message.edit_text(f"<b><i>Сухой лёд</i></b>\n\n"
                                         f"{loading_works}", reply_markup=kb_price)
    if callback.data == 'rental_of_thermoses':
        result = await get_text(id_text=4)
        loading_works = result.replace(r'\n', '\n')
        await callback.message.edit_text(f"<b><i>Аренда Термосов</i></b>\n\n"
                                         f"{loading_works}", reply_markup=kb_price)
