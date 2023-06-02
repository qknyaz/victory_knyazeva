from aiogram import F
from aiogram.filters import Command, Text
from .client import *
from .admin import *
from .callback import *

'''
регистрация хендлеров и коллбеков
инициализируются в инит-файле'''

# for admin service message
dp.startup.register(start_mes)
dp.shutdown.register(stop_mes)

# commands for user
dp.message.register(start, Command("start"))
dp.message.register(help, Command("help"))
dp.message.register(level, Command("level"))
dp.message.register(change_level, Command("change_level"))

dp.message.register(level, Text("Уровень"))
dp.message.register(help, Text("Помощь"))

# commands for admin
dp.message.register(statistics, Text(["stat", "Stat", "ста", "Ста", "Стат"]))

# callbacks for user
dp.callback_query.register(level_master, Text('master'))
dp.callback_query.register(level_profy, Text('profi'))
dp.callback_query.register(level_business, Text('business'))


dp.message.register(allreadytext)
