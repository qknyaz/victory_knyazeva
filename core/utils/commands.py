from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChatAdministrators

from config import ADMINS, GROUP
from loader import bot

async def set_commands(bot: Bot):
	commands = [
		BotCommand(
			command='start',
			description='Начало работы'
		),
		BotCommand(
			command='help',
			description='Помощь'
		),
		BotCommand(
			command='level',
			description='Мой текущий уровень'
		)
	]
	await bot.set_my_commands(commands, BotCommandScopeDefault())

	commands_admin = [
		BotCommand(
			command='start',
			description='Начало работы'
		),
		BotCommand(
			command='help',
			description='Помощь'
		)
	]
	# await bot.set_my_commands(commands_admin, BotCommandScopeChatAdministrators(chat_ad=GROUP))
