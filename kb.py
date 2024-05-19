from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sql_db import *

send_welcome_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💰 Купить"),
            KeyboardButton(text="💼 Продать"),
        ],
        [
            KeyboardButton(text="👤 Мой профиль"),
            KeyboardButton(text="❓ Помощь"),
        ],
    ],
    resize_keyboard=True
)

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Главное меню"),
        ],
    ],
    resize_keyboard=True
)

buy_reply_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Beeline", callback_data="buy_Beeline"),
            InlineKeyboardButton(text="Active", callback_data="buy_Active"),
            InlineKeyboardButton(text="Tele2", callback_data="buy_Tele2"),
        ],
    ]
)

sell_reply_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Beeline", callback_data="sell_Beeline"),
            InlineKeyboardButton(text="Active", callback_data="sell_Active"),
            InlineKeyboardButton(text="Tele2", callback_data="sell_Tele2"),
        ],
    ]
)

cancel_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="❌ Отменить"),
        ],
    ],
    resize_keyboard=True
)

verify_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✅ Подтвердить"),
            KeyboardButton(text="❌ Отменить"),
        ],
    ],
    resize_keyboard=True
)

request_contact_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить контакт", request_contact=True),
        ],
    ],
    resize_keyboard=True
)

def buy_callback_operator_kb(active_orders):
    builder = InlineKeyboardBuilder()
    for order in active_orders:
        username = get_username(order[1])
        builder.row(InlineKeyboardButton(text=f"{username}({order[3]} ГБ - {order[4]} KZT)", callback_data=f"user_{order[1]}"))
    return builder.as_markup()

def msg_profile_kb(user_id):
    user_orders = sql_get_orders_by_user(user_id)
    builder = InlineKeyboardBuilder()
    for order in user_orders:
        builder.row(InlineKeyboardButton(text=f"❌   {order[3]} ГБ - {order[4]} KZT   ❌", callback_data=f"del_order_{order[0]}"))
    return builder.as_markup()
