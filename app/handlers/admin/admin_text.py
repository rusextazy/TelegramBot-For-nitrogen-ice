from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.database.models import add_text
from app.filters.admin_type import IsBotAdminFilter
from app.handlers.admin.kb_admin import kb_admin, kb_exit_admin, kb_admin_text, kb_admin_price


class NewText(StatesGroup):
    Text = State()
    Unloading_And_Loading = State()
    Liquid_Nitrogen = State()
    Dry_Ice = State()
    Thermos_Rental = State()


class Contact(StatesGroup):
    NumberText = State()


router = Router()


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📄 Поменять прайс")
async def price_menu_admin(msg: types.Message, state: FSMContext):
    await msg.answer(text="Выбери какой текст хочешь изменить!",
                     reply_markup=kb_admin_price)
    await state.set_state(NewText.Text)


@router.message(IsBotAdminFilter(is_admin=True),
                NewText.Text)
async def change_price_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    if msg.text == "Прайс на разгрузочно-погрузочные работы при заправке сосудов Дьюара":
        await msg.answer("Пришлите новый текст!", reply_markup=kb_exit_admin)
        await state.set_state(NewText.Unloading_And_Loading)
    elif msg.text == "Жидкий азот":
        await msg.answer("Пришлите новый текст!", reply_markup=kb_exit_admin)
        await state.set_state(NewText.Liquid_Nitrogen)
    elif msg.text == "Сухой лёд":
        await msg.answer("Пришлите новый текст!", reply_markup=kb_exit_admin)
        await state.set_state(NewText.Dry_Ice)
    elif msg.text == "Аренда Термосов":
        await msg.answer("Пришлите новый текст!", reply_markup=kb_exit_admin)
        await state.set_state(NewText.Thermos_Rental)


@router.message(IsBotAdminFilter(is_admin=True),
                NewText.Unloading_And_Loading)
async def change_text_1_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    await add_text(msg.text, id_text=1)
    await msg.answer(text="Текст успешно поменялся!", reply_markup=kb_admin)
    await state.clear()


@router.message(IsBotAdminFilter(is_admin=True),
                NewText.Liquid_Nitrogen)
async def change_text_2_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    await add_text(msg.text, id_text=2)
    await msg.answer(text="Текст успешно поменялся!", reply_markup=kb_admin)
    await state.clear()


@router.message(IsBotAdminFilter(is_admin=True),
                NewText.Dry_Ice)
async def change_text_3_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    await add_text(msg.text, id_text=3)
    await msg.answer(text="Текст успешно поменялся!", reply_markup=kb_admin)
    await state.clear()


@router.message(IsBotAdminFilter(is_admin=True),
                NewText.Thermos_Rental)
async def change_text_4_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    await add_text(msg.text, id_text=4)
    await msg.answer(text="Текст успешно поменялся!", reply_markup=kb_admin)
    await state.clear()


@router.message(IsBotAdminFilter(is_admin=True),
                F.text == "📲 Поменять контакты")
async def change_contacts_admin(msg: types.Message, state: FSMContext):
    await msg.answer(text="Пришли новые контакты!",
                     reply_markup=kb_exit_admin)
    await state.set_state(Contact.NumberText)


@router.message(IsBotAdminFilter(is_admin=True),
                Contact.NumberText)
async def change_contacts_5_admin(msg: types.Message, state: FSMContext):
    await state.update_data(data_user=msg.text)
    await add_text(msg.text, id_text=5)
    await msg.answer(text="Текст успешно поменялся!", reply_markup=kb_admin)
    await state.clear()
