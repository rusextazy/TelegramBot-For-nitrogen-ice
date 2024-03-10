import re

from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command

from app.keyboards.reply import kb_menu, kb_exit, kb_goods, kb_choice, kb_delivery, kb_address
from app.keyboards.inline import kb_price
from app.text.main import reply
from app.utils.state import Application
from app.database.models import check_user_to_db, get_text, add_application_to_table

router = Router()


@router.message(F.text.in_(("🔙 Главное меню", "Отмена", "Меню")))
async def main_menu(msg: Message, state: FSMContext):
    await state.clear()
    await msg.reply(text="Вы вернулись на главное меню!", reply_markup=kb_menu)


@router.message(F.text == "📱 Контакты")
@router.message(Command("contacts"))
async def get_contacts(msg: Message):
    name = msg.from_user.username
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    result = await get_text(id_text=5)
    loading_works = result.replace(r'\n', '\n')
    await msg.answer(text=f'{loading_works}', parse_mode='HTML')


@router.message(F.text == "👨‍💻 Прайс")
@router.message(Command("price"))
async def get_price(msg: Message):
    name = msg.from_user.username
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    await msg.answer(text="<b><i>Прайс Азот - Сухой лед</i></b>\n\n(воспользуйся кнопками)", reply_markup=kb_price)


@router.message(F.text == "☕️ Подать заявку")
@router.message(Command("application"))
async def get_application(msg: Message, state: FSMContext):
    name = msg.from_user.username
    chat_id = msg.from_user.id
    await check_user_to_db(name, chat_id)
    await msg.answer("Форма подачи заявка (Пожалуйста будьте внимательны при заполнении)👇\n"
                     "Вы всегда сможете вернуться на главное меню и заполнить заявку заново.")
    await msg.answer("Введите Дату.\nФормат: 00.00.0000", reply_markup=kb_exit)
    await state.set_state(Application.Date)


async def check_date_format(date):
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"  # Паттерн для даты в формате 00.00.0000
    if re.match(pattern, date):
        return True
    else:
        return False


@router.message(Application.Date)
async def application_data(msg: Message, state: FSMContext):
    if await check_date_format(msg.text):
        await state.update_data(data_user=msg.text)
        await msg.answer(text="Введите интервал времени\nФормат: 00:00-00:00\nПожалуйста будьте внимательные "
                              "и следуйте инструкциям")
        await state.set_state(Application.Time_Interval)
    else:
        await msg.answer(text="Извините, будьте внимательны при заполнении!\nПри каждом шаге есть Формат заполнения!")


async def check_time_format(time):
    pattern = r"^\d{2}:\d{2}-\d{2}:\d{2}$"  # Паттерн для времени в формате 00:00-00:00
    if re.match(pattern, time):
        return True
    else:
        return False


@router.message(Application.Time_Interval)
async def application_time(msg: Message, state: FSMContext):
    if await check_time_format(msg.text):
        await state.update_data(time_interval_user=msg.text)
        await msg.answer(text="Выберете товар, какой вам нужен(нажмите кнопку снизу)", reply_markup=kb_goods)
        await state.set_state(Application.Goods)
    else:
        await msg.answer(
            text="Извините, будьте внимательны при заполнении!\nПри каждом шаге есть Формат заполнения!")


@router.message(Application.Goods)
async def application_goods(msg: Message, state: FSMContext):
    if msg.text == "Лед":
        await state.update_data(goods_user=msg.text)
        await msg.answer(text="Введите количество кг (лед)", reply_markup=kb_exit)
        await state.set_state(Application.Quantity)
    elif msg.text == "Азот":
        await state.update_data(goods_user=msg.text)
        await msg.answer(text="Введите количество литров (азот)", reply_markup=kb_exit)
        await state.set_state(Application.Quantity)
    else:
        await msg.answer(
            text="Извините, будьте внимательны при заполнении!\nПри каждом шаге есть Формат заполнения!")


@router.message(Application.Quantity)
async def application_quantity(msg: Message, state: FSMContext):
    await state.update_data(quantity_user=msg.text)
    await msg.answer(text="Введите наличие тары\nФормат: Нет (Если нет тары), Есть (Если есть тара)")
    await state.set_state(Application.Availability_Of_Packaging)


@router.message(Application.Availability_Of_Packaging)
async def application_availability(msg: Message, state: FSMContext):
    await state.update_data(availability_of_packaging_user=msg.text)
    await msg.answer(text="Выберете нужна ли вам доставка (нажмите кнопку снизу)", reply_markup=kb_delivery)
    await state.set_state(Application.Delivery)


@router.message(Application.Delivery)
async def application_delivery(msg: Message, state: FSMContext):
    if msg.text == "Да, нужна":
        await state.update_data(delivery_user=msg.text)
        await msg.answer(text="Введите адрес доставки.", reply_markup=kb_exit)
        await state.set_state(Application.Address)
    elif msg.text == "Нет, не нужна":
        await state.update_data(delivery_user=msg.text)
        await msg.answer(text="Выберете откуда заберете товар: (нажмите кнопку снизу)", reply_markup=kb_address)
        await state.set_state(Application.Address)
    else:
        await msg.answer(
            text="Извините, будьте внимательны при заполнении!\nПри каждом шаге есть Формат заполнения!")


@router.message(Application.Address)
async def application_address(msg: Message, state: FSMContext):
    await state.update_data(address_user=msg.text)
    await msg.answer(text="Введите контактный номер телефона\n"
                          "Формат: 89503352178", reply_markup=kb_exit)
    await state.set_state(Application.Client_Phone)


async def check_phone_number(phone_number):
    pattern = r"^89\d{9}$"  # Паттерн для номера в формате 89*********
    if re.match(pattern, phone_number):
        return True
    else:
        return False


@router.message(Application.Client_Phone)
async def application_phone(msg: Message, state: FSMContext):
    if await check_phone_number(msg.text):
        await state.update_data(client_phone_user=msg.text)
        await msg.answer(text="Выберете, кем вы являетесь(нажмите кнопку снизу)", reply_markup=kb_choice)
        await state.set_state(Application.Choice)
    else:
        await msg.answer(text="Введите корректный номер телефона\n"
                              "Формат: 89503352178")


@router.message(Application.Choice)
async def application_choice(msg: Message, state: FSMContext):
    if msg.text == "Юр.Лицо":
        await state.update_data(choice_user=msg.text)
        await msg.answer(text="Введите наименование организации(Юрлица)", reply_markup=kb_exit)
        await state.set_state(Application.Name_Of_Organization)
    elif msg.text == "Физ.Лицо":
        await state.update_data(choice_user=msg.text)
        await msg.answer(text="Введите ваше ФИО", reply_markup=kb_exit)
        await state.set_state(Application.Name_Of_Organization)
    else:
        await msg.answer(
            text="Извините, будьте внимательны при заполнении!\nПри каждом шаге есть Формат заполнения!")


@router.message(Application.Name_Of_Organization)
async def application_name(msg: Message, bot: Bot, state: FSMContext):
    await state.update_data(name_of_organization_user=msg.text)
    data = await state.get_data()
    await add_application_to_table(date=data['data_user'], product=data['goods_user'], address=data['address_user'],
                                   client_phone=data['client_phone_user'], full_name=data['name_of_organization_user'],
                                   chat_id=msg.from_user.id)
    await msg.answer(text="Ваша заявка успешно отправлена! Спасибо и ожидайте ответа!", reply_markup=kb_menu)
    await bot.send_message(chat_id="-4086537550",
                           text=reply.format(id=msg.from_user.username,
                                             chat_id=msg.from_user.id,
                                             Date=data['data_user'],
                                             Time_Interval=data['time_interval_user'],
                                             Goods=data['goods_user'],
                                             Quantity=data['quantity_user'],
                                             Availability_Of_Packaging=data['availability_of_packaging_user'],
                                             Delivery=data['delivery_user'],
                                             Address=data['address_user'],
                                             Client_Phone=data['client_phone_user'],
                                             Choice=data['choice_user'],
                                             Name_Of_Organization=data['name_of_organization_user']))

    await state.clear()
