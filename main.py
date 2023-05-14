import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InputFile
from aiogram.utils import executor
import markups as nav
import state

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Об'єкт бота
bot = Bot(token="6096465408:AAF1lQ-eTaE5kN-jI9cD0u37Jgi_pDvJdHA")
# Диспетчер
dp = Dispatcher(bot)

# Клавіатура головного меню


# Хендлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    photo = InputFile('assets/photo_2023-04-16_11-13-42.jpg')
    #await message.answer(f"👋 Добро пожаловать, {message.from_user.full_name}!\nInvestFunds\nАналитика по рынкам акций, облигаций, валют, макроэкономике. 200+ источников. Российский и глобальные рынки.\n Уникальная возможность для стабильного заработка в Telegram\n \n🔸 Выберите пункт меню:", reply_markup=nav.menu_kb())
    await bot.send_photo(message.chat.id, photo=photo, caption=f"👋 Добро пожаловать, {message.from_user.full_name}!\n \nInvestFunds\n \nАналитика по рынкам акций, облигаций, валют, макроэкономике. 200+ источников. Украинский и глобальные рынки.\n \nУникальная возможность для стабильного заработка в Telegram\n \n🔸 Выберите пункт меню:", reply_markup=nav.menu_kb())

@dp.callback_query_handler(text='repl')
async def repl_msg(call: types.CallbackQuery):
    # photo = InputFile('assets/balance.jpg')
    await call.message.answer(text="Выберите тип пополнения" ,reply_markup=nav.repl_kb())


# Обробник повідомлень
@dp.message_handler()
async def bot_msg(message: types.Message):
    stt= state.state
    admin_id = '1418252017'
    match stt:
        case 0:
            match message.text:
                case "🔑 Личный кабинет":
                    photo = InputFile('assets/personal_office.jpg')
                    await bot.send_photo(message.chat.id, photo=photo,
                                         caption=f"👤 {message.from_user.full_name}\n \n💰 Баланс Вашего счета: 0.0 $\n \n🔄 Инвестировано: 0.0 $\n \n🗣 Рефералов: 0 чел.",
                                         reply_markup=nav.per_office_kb())
                case "🔙 Главное меню 🔙":
                    photo = InputFile('assets/photo_2023-04-16_11-13-42.jpg')
                    await bot.send_photo(message.chat.id, photo=photo,
                                         caption=f"👋 Добро пожаловать, {message.from_user.full_name}!\n \nInvestFunds\n \nАналитика по рынкам акций, облигаций, валют, макроэкономике. 200+ источников. Украинский и глобальные рынки.\n \nУникальная возможность для стабильного заработка в Telegram\n \n🔸 Выберите пункт меню:",
                                         reply_markup=nav.menu_kb())
                case "💰 Баланс":
                    photo = InputFile('assets/balance.jpg')
                    await bot.send_photo(message.chat.id, photo=photo,
                                         caption=f"👤 {message.from_user.full_name}\n \n💰 Баланс Вашего счета: 0.0 $\n \n⚠️ Напоминаем:\nМинимальная сумма пополнения от 1500$ для долгосрочных инвестиций;\nМинимальная сумма пополнения от 5000$ для краткосрочных инвестиций;\nМинимальная сумма для вывода от 200$\n \nВыберите нужное действие 👇🏻:",
                                         reply_markup=nav.balance_kb())
                case "🤝 Инвестиции":
                    photo = InputFile('assets/invest.jpg')
                    await bot.send_photo(message.chat.id, photo=photo,
                                         caption="Краткосрочные инвестиции:\n🔸Минимальная сумма от 5000 $;\n🔸Срок инвестиции - 168 часов (7 дней);\n🔸% прибыли - 35% (за весь период);\n \nДолгосрочные инвестиции:\n🔸Минимальная сумма от 1500 $;\n🔸Срок инвестиции- неограничен;\n🔸Процент прибыли - 2% (за 24 часа);\n \nВыберите тип инвестирования:",
                                         reply_markup=nav.invest_kb())
                case "🗣️ Реферальная система":
                    await bot.send_message(message.chat.id, "Реферальная система вреенно недоступна")
                case "📠 Калькулятор":
                    await bot.send_message(message.chat.id, "Калькулятор временно недоступен")
                case "🆘 Тех. поддержка":
                    await bot.send_message(message.chat.id, "Для связи с тех.поддержкой нажмите кнопку ниже:",
                                           reply_markup=nav.support_kb())
                case '📖 Как начать инвестировать':
                    img = InputFile('assets/photo_2023-04-16_18-45-49.jpg')
                    await bot.send_photo(message.chat.id, photo=img,
                                         caption="В данной статье Вы узнаете обо всех аспектах по работе с нашей платформой",
                                         reply_markup=nav.how_to_kb())
                case 'ℹ️ О проекте':
                    img = InputFile('assets/photo_2023-04-16_11-13-42.jpg')
                    await bot.send_photo(message.chat.id, photo=img,
                                         caption="InvestFunds\n \nНезависимый источник данных для частного инвестора в Украине\nСтарт проекта: 01.10.2022 г.\n \nВсего инвесторов: 2156 чел.\n \nВсего инвестировано: 7904271.070000002 $",
                                         reply_markup=nav.about_kb())
                case "QIWI":
                    await bot.send_message(message.chat.id, "ddtlb ceve gjgjdytyyz ',kfy")
                    state.state = 1
                case "Visa MasterCard":
                    await bot.send_message(message.chat.id, "ddtlb ceve gjgjdytyyz ',kfy")
                    state.state = 1
                case "USDT TRC20":
                    await bot.send_message(message.chat.id, "ddtlb ceve gjgjdytyyz ',kfy")
                    state.state = 1

        case 1:

            try:
                a = float(message.text)
                if a >= 1500.0 and a < 150000.0:
                    await bot.forward_message(chat_id=admin_id, from_chat_id=message.chat.id, message_id=message.message_id)
                    await bot.send_message(message.chat.id, 'піздєц, тепер чекай повідомлення від техпідйобки, єблан кончений')
                    state.state = 0
                elif a > 150000.0:
                    await bot.send_message(message.chat.id, 'ти шо йобу дав, з якої пизди ти такі бабки витягнеш? а, знаю. З пизди своєї мамки')
                    state.state = 0
                else:
                    await bot.send_message(message.chat.id, 'Сумма поповнення має бути рівна або більша за 1500')

            except:
                print("huinya")
                await bot.send_message(message.chat.id, 'Дебіла кусок, введи ціле число нахуй')


async def inline_kb_handler(call: types.CallbackQuery):
    match call.data:
        case "repl":
            pass
        case "withdraw":
            pass

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)