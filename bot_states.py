from aiogram.fsm.state import State, StatesGroup

class SellCreateOrderState(StatesGroup):
    operator = State()
    gb_amount = State()
    price = State()
    done = State()