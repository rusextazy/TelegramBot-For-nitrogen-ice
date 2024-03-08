from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_menu = [
    [KeyboardButton(text="📱 Контакты"),
     KeyboardButton(text="👨‍💻 Прайс")],
    [KeyboardButton(text="☕️ Подать заявку")]
]

kb_menu = ReplyKeyboardMarkup(keyboard=kb_menu, resize_keyboard=True)

kb_exit = [
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_exit = ReplyKeyboardMarkup(keyboard=kb_exit, resize_keyboard=True)

kb_goods = [
    [KeyboardButton(text="Азот"),
     KeyboardButton(text="Лед")],
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_goods = ReplyKeyboardMarkup(keyboard=kb_goods, resize_keyboard=True)

kb_choice = [
    [KeyboardButton(text="Юр.Лицо"),
     KeyboardButton(text="Физ.Лицо")],
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_choice = ReplyKeyboardMarkup(keyboard=kb_choice, resize_keyboard=True)

kb_delivery = [
    [KeyboardButton(text="Да, нужна"),
     KeyboardButton(text="Нет, не нужна")],
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_delivery = ReplyKeyboardMarkup(keyboard=kb_delivery, resize_keyboard=True)

kb_address = [
    [KeyboardButton(text="Даурская 41"),
     KeyboardButton(text="Окольная 94 а корп. 1")],
    [KeyboardButton(text="🔙 Главное меню")]
]

kb_address = ReplyKeyboardMarkup(keyboard=kb_address, resize_keyboard=True)

