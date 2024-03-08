from aiogram.fsm.state import State, StatesGroup


class Application(StatesGroup):
    Date = State()
    Time_Interval = State()
    Goods = State()
    Quantity = State()
    Availability_Of_Packaging = State()
    Delivery = State()
    Address = State()
    Client_Phone = State()
    Choice = State()
    Name_Of_Organization = State()
