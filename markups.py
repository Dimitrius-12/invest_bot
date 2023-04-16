from aiogram import types

def menu_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🔑 Личный кабинет', '🆘 Тех. поддержка', '📖 Как начать инвестировать', 'ℹ️ О проекте']
    markup.add(*buttons)
    return markup

def per_office_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['💰 Баланс', '🤝 Инвестиции', '🗣️ Реферальная система', '📠 Калькулятор', '🔙 Главное меню 🔙']
    markup.add(*buttons)
    return markup

def balance_kb():
    markup = types.InlineKeyboardMarkup(row_width=2)
    button1 = types.InlineKeyboardButton(text="Пополнить", callback_data='repl')
    button2 = types.InlineKeyboardButton(text="Вывести средства", callback_data='withdraw')
    markup.insert(button1)
    markup.insert(button2)
    return markup

def invest_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['🤝 Краткосрочно', '🤝 Долгосрочно', '🆘 Тех. поддержка', '🔑 Личный кабинет']
    markup.add(*buttons)
    return markup

def support_kb():
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton(text="Служба поддержки", callback_data='@', url='https://t.me/encore_013')
    markup.insert(button1)
    return markup

def how_to_kb():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Продолжить", callback_data="continue", url='https://telegra.ph/InvestFund-03-27')
    markup.insert(btn1)
    return markup

def about_kb():
    markup = types.InlineKeyboardMarkup(row_width=1)
    btn1 = types.InlineKeyboardButton(text="Подробнее", callback_data="about", url='https://telegra.ph/INVEST-FUND-03-27')
    markup.insert(btn1)
    return markup