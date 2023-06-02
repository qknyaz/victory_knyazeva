from aiogram import Bot, Router
from config import *
from loader import dp, bot
from aiogram.types import Message


async def start_mes(bot: Bot):
	await bot.send_message(ADMIN_ID, text="Бот запущен!")


async def stop_mes(bot: Bot):
	await bot.send_message(ADMIN_ID, text="Бот остановлен!")


async def statistics(message: Message):
	if message.from_user.id in ADMINS:
		await message.answer(text="statistics")


# Рассылка
async def sender():
	pass