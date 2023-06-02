from aiogram import Bot, Dispatcher
from config import TG_TOKEN


bot = Bot(TG_TOKEN, parse_mode='HTML')
dp = Dispatcher()  # инициализация диспетчера, доставщик обновлений