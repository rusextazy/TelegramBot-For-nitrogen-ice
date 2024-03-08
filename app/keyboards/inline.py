from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

kb_subscription = [
    [InlineKeyboardButton(text="Подписаться 🥷", url="https://t.me/+od5KGdLJrAc0ZmFi"),
     InlineKeyboardButton(text="Проверить ✅", callback_data="sub_check")]
]

kb_subscription = InlineKeyboardMarkup(inline_keyboard=kb_subscription)

kb_price = [
    [InlineKeyboardButton(text="Прайс на разгрузочно-погрузочные работы", callback_data="loading_works")],
    [InlineKeyboardButton(text="Жидкий азот", callback_data="a_liquid_nitrogen"),
     InlineKeyboardButton(text="Сухой лёд", callback_data="dry_ice")],
    [InlineKeyboardButton(text="Аренда Термосов", callback_data="rental_of_thermoses")]
]

kb_price = InlineKeyboardMarkup(inline_keyboard=kb_price)
