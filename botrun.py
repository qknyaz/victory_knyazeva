import asyncio
import logging
from aiogram import Bot
# from aiogram import types
from aiogram.filters.command import Command

from aiogram.types import Message
from loader import dp, bot
from config import *
from core.utils import *

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
	from core.handler import *
	from core.filter import *
	from core.utils import *
	try:
		asyncio.run(main())
	except KeyboardInterrupt as kbi:
		print(kbi)
