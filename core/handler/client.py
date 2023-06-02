from aiogram import Bot
from aiogram.types import Message
from config import *
from core.keyboard import inline_level
from core.keyboard.reply import *
from core.utils import set_commands
from loader import dp, bot




async def start(message: Message):
	await set_commands(bot)
	await message.answer(HELLO, reply_markup=reply_keyboard)
	await message.answer('Если ты мастер, профи или бизнесмен, выбери...', reply_markup=inline_level)


async def level(message: Message):
	await message.answer('Ваш уровень ...\n можете изменить выбор')
	await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
	await message.answer('Если ты мастер, профи или бизнесмен, выбери...', reply_markup=inline_level)


async def change_level(message: Message):
	await message.answer('Если ты мастер, профи или бизнесмен, выбери...', reply_markup=inline_level)


async def help(message: Message):
	await message.answer(HELP)
	await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


async def allreadytext(message: Message):
	# print(message)
	# print(message.from_user.id)
	# print(message.from_user.first_name)
	# print(message.chat.id)
	if message.from_user.id in ADMINS and message.chat.id == -1001916405960:
		text_for_user = message.text  # ответ админа на сообщение пользователя
		if bool(message.reply_to_message.text):
			chat_id = message.reply_to_message.text.split('\n')[0].split('|')[0]  # парсит id из сообщения которое приходит в группу
		if bool(message.reply_to_message.caption):
			chat_id = message.reply_to_message.caption.split('\n')[0].split('|')[0]  # парсит id из сообщения(фото) которое приходит в группу
		if bool(message.reply_to_message.text):
			id_msg = message.reply_to_message.text.split('\n')[0].split('|')[1]
		if bool(message.reply_to_message.caption):
			id_msg = message.reply_to_message.caption.split('\n')[0].split('|')[1]
		await bot.send_message(chat_id=chat_id, text=message.text, reply_to_message_id=id_msg,)

	else:
		text = f"{message.from_user.id}|{message.message_id}\n" \
		       f"{message.from_user.first_name}\n" \
		       f"📬\n{message.text}"
		await bot.send_message(GROUP, text)




