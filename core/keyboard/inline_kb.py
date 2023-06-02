from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_level = InlineKeyboardMarkup(inline_keyboard=[
	[
		InlineKeyboardButton(text='Мастер', callback_data='master')
	],
	[
		InlineKeyboardButton(text='Профи', callback_data='profi')
	],
	[
		InlineKeyboardButton(text='Бизнес', callback_data='business')
	]
])
