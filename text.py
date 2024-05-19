send_welcome_text = """
👋 Добро пожаловать!

Приветствую вас! Я - ваш личный бот для обмена ГБ.

Выберите одно из следующих действий:

1. Купить: 💰 Купить
2. Продать: 💼 Продать
3. Мой профиль: 👤 Просмотреть ваш профиль и баланс
4. Помощь: ❓ Получить помощь и поддержку
"""


buy_reply_text = """
🛒 Покупка ГБ

Выберите оператора, у которого хотите приобрести ГБ:

1. Beeline: 🐝
2. Active: 🔋
3. Tele2: 📞
"""


sell_reply_text = """
🛒 Продажа ГБ

Выберите оператора, у которого хотите продать ГБ:

1. Beeline: 🐝
2. Active: 🔋
3. Tele2: 📞
"""

def sell_callback_operator_text(operator):
    return f"""
    ✍️ Продажа ГБ ({operator})
    
    Введите количество ГБ, которое вы хотите продать. Пожалуйста, введите только число (например, 1, 2, 3):
    """

error_gb_amount_text = """
⚠️ Ошибка

Пожалуйста, введите только числовое значение, например, 1, 2 или 3. Попробуйте еще раз:
"""

sell_callback_gb_amount_text = """
✅ Количество ГБ принято
✍️ Укажите цену за каждый ГБ

Пожалуйста, введите цену за каждый ГБ. Пожалуйста, укажите только числовое значение (например, 100):
"""

error_gb_price_text = """
⚠️ Ошибка

Пожалуйста, введите только числовое значение для цены за каждый ГБ. Попробуйте еще раз:
"""

def verify_order_text(operator, gb_amount, price):
    return f"""
    ✅ Цена принята

    Спасибо за указание цены за каждый ГБ для оператора {operator}. Пожалуйста, подтвердите правильность введенных данных:

        Количество ГБ: {gb_amount}
        Цена за каждый ГБ: {price} ₸

    Если данные верны, нажмите кнопку "Подтвердить".
    """

announcement_is_done_text = """
✅ Объявление создано

Ваше объявление о продаже ГБ успешно создано! Вы будете оповещены, когда кто-то захочет купить ГБ у вас.
"""

request_contact_text = """
📩 Отправьте свой контакт

Пожалуйста, предоставьте свой контакт.
"""

def buy_callback_operator_text(operator):
    return f"""
    ✍️ Купить ГБ ({operator})
    
    Выберите продавца, у которого хотите приобрести ГБ:
    """

msg_profile_text = """
👤 Профиль

Ваши объявления, нажмите на кнопку если вы хотите их удалить:
"""