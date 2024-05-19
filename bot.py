import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext


from config import TOKEN
from text import *
from kb import *
from bot_states import *

bot = Bot(TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def send_welcome(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=request_contact_text, reply_markup=request_contact_kb)
    sql_insert_user(message.from_user.id, message.from_user.full_name)


@dp.message(F.contact)
async def msg_get_contact(message: Message):
    sql_update_contact(message.from_user.id, message.contact.phone_number)
    await bot.send_message(chat_id=message.chat.id, text=send_welcome_text, reply_markup=send_welcome_kb)

@dp.message(F.text == "Главное меню")
async def cancel(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=f"{message.text} была нажата", reply_markup=send_welcome_kb)


@dp.message(F.text == "❌ Отменить")
@dp.message(Command("cancel"))
async def cancel(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    
    await state.clear()
    await bot.send_message(chat_id=message.chat.id, text=f"{message.text} была нажата", reply_markup=send_welcome_kb)


@dp.message(F.text == "💰 Купить")
async def buy_reply(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=f"{message.text} была нажата", reply_markup=main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text=buy_reply_text, reply_markup=buy_reply_kb)


@dp.message(F.text == "💼 Продать")
async def sell_reply(message: Message):
    await bot.send_message(chat_id=message.chat.id, text=f"{message.text} была нажата", reply_markup=main_menu_kb)
    await bot.send_message(chat_id=message.chat.id, text=sell_reply_text, reply_markup=sell_reply_kb)


@dp.callback_query(F.data.startswith("sell_"))
async def buy_callback_operator(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(operator=callback_query.data[5:])
    await bot.send_message(chat_id=callback_query.message.chat.id, text=sell_callback_operator_text(callback_query.data[5:]), reply_markup=cancel_kb)
    
    await state.set_state(SellCreateOrderState.gb_amount)


@dp.message(SellCreateOrderState.gb_amount, lambda message: not message.text.isdigit())
async def sell_callback_gb_amount(message: Message, state: FSMContext):
    return await bot.send_message(chat_id=message.chat.id, text=error_gb_amount_text, reply_markup=cancel_kb)

@dp.message(SellCreateOrderState.gb_amount, F.text.isdigit())
async def sell_callback_gb_amount(message: Message, state: FSMContext):
    await state.update_data(gb_amount=int(message.text))
    await bot.send_message(chat_id=message.chat.id, text=sell_callback_gb_amount_text, reply_markup=cancel_kb)

    await state.set_state(SellCreateOrderState.price)


@dp.message(SellCreateOrderState.price, lambda message: not message.text.isdigit())
async def sell_callback_price(message: Message, state: FSMContext):
    return await bot.send_message(chat_id=message.chat.id, text=error_gb_price_text, reply_markup=cancel_kb)


@dp.message(SellCreateOrderState.price, F.text.isdigit())
async def sell_callback_price(message: Message, state: FSMContext):
    await state.update_data(price=int(message.text))
    data = await state.get_data()
    await bot.send_message(chat_id=message.chat.id, text=verify_order_text(data['operator'], data['gb_amount'], data['price']), reply_markup=verify_kb)

    await state.set_state(SellCreateOrderState.done)


@dp.message(SellCreateOrderState.done, F.text == "✅ Подтвердить")
async def done(message: Message, state: FSMContext):
    data = await state.get_data()
    sql_insert_order(message.from_user.id, data['operator'], data['gb_amount'], data['price'])
    await state.update_data(done=True)
    await bot.send_message(chat_id=message.chat.id, text=announcement_is_done_text, reply_markup=send_welcome_kb)

    await state.clear()






@dp.callback_query(F.data.startswith("buy_"))
async def buy_callback_operator(callback_query: CallbackQuery):
    active_orders = get_orders(callback_query.data[4:])

    await bot.send_message(chat_id=callback_query.message.chat.id, text=buy_callback_operator_text(callback_query.data[4:]), reply_markup=buy_callback_operator_kb(active_orders))

@dp.callback_query(F.data.startswith("user_"))
async def msg_send_contact(callback_query: CallbackQuery):
    contact = get_contact(callback_query.data[5:])
    username = get_username(callback_query.data[5:])
    await bot.send_contact(chat_id=callback_query.message.chat.id, phone_number=str(contact), first_name=str(username))



@dp.message(F.text == "👤 Мой профиль")
async def msg_profile(message: Message):
    contact = get_contact(message.from_user.id)
    username = get_username(message.from_user.id)
    await bot.send_contact(chat_id=message.chat.id, phone_number=str(contact), first_name=str(username))
    await bot.send_message(chat_id=message.chat.id, text=msg_profile_text, reply_markup=msg_profile_kb(message.from_user.id))

@dp.callback_query(F.data.startswith("del_order_"))
async def msg_send_contact(callback_query: CallbackQuery):
    sql_change_order_status(callback_query.data[10:])
    await bot.send_message(chat_id=callback_query.message.chat.id, text="Объявление удалено", reply_markup=send_welcome_kb)

if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot, skip_updates=True))