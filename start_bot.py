from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

# Об'єкт бота
TOKEN="6096465408:AAF1lQ-eTaE5kN-jI9cD0u37Jgi_pDvJdHA"
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher(bot, storage=storage)