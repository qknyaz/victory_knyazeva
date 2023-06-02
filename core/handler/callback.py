from aiogram.types import CallbackQuery
from loader import bot, dp


async def level_master(call: CallbackQuery):
	# db.level(level=0, user_id=message.from_user.id)
	await call.message.answer(f'Выбран уровень \n<b>"Мастер"</b>')
	await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)


async def level_profy(message: CallbackQuery, ):
	# db.level(level=1, user_id=message.from_user.id)
	await bot.send_message(message.from_user.id, f'Выбран уровень \n<b>"Профи"</b>')
	await bot.delete_message(chat_id=message.from_user.id, message_id=message.message.message_id)
	# dir = os.path.abspath()
	# print(dir)
	# file = open(r'D:\pyscripts\BotTelegram\victory_knyazeva\files\novichok\подарочек.pdf', 'rb')
	# await bot.send_document(message.from_user.id, document=file)

async def level_business(message: CallbackQuery, ):
	# db.level(level=2, user_id=message.from_user.id)
	await bot.send_message(message.from_user.id, f'Выбран уровень \n<b>"Биснесмен"</b>')
	await bot.delete_message(chat_id=message.from_user.id, message_id=message.message.message_id)
	# await bot.send_message(message.from_user.id, yt2)
