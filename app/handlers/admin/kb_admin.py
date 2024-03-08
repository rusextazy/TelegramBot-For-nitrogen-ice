from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_admin = [
    [KeyboardButton(text="📊 Статистика"),
     KeyboardButton(text="📩 Рассылка")],
    [KeyboardButton(text="📄 Поменять текст")],
    [KeyboardButton(text="🔙 Вернуться в user_menu")]
]

kb_admin = ReplyKeyboardMarkup(keyboard=kb_admin, resize_keyboard=True)

kb_admin_text = [
    [KeyboardButton(text="📄 Поменять прайс"),
     KeyboardButton(text="📲 Поменять контакты")],
    [KeyboardButton(text="🔙 Назад")]
]

kb_admin_text = ReplyKeyboardMarkup(keyboard=kb_admin_text, resize_keyboard=True)

kb_admin_price = [
    [KeyboardButton(text="Прайс на разгрузочно-погрузочные работы при заправке сосудов Дьюара")],
    [KeyboardButton(text="Жидкий азот"),
     KeyboardButton(text="Сухой лёд")],
    [KeyboardButton(text="Аренда Термосов")],
    [KeyboardButton(text="🔙 Назад")],
]

kb_admin_price = ReplyKeyboardMarkup(keyboard=kb_admin_price, resize_keyboard=True)

kb_exit_admin = [
    [KeyboardButton(text="🔙 Назад")]
]

kb_exit_admin = ReplyKeyboardMarkup(keyboard=kb_exit_admin, resize_keyboard=True)
