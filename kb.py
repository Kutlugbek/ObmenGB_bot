from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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