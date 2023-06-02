from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


reply_keyboard_adm = ReplyKeyboardMarkup(keyboard=[
	[
		KeyboardButton(text='Помощь'),
		KeyboardButton(text='Статистика')
	],
	[
		KeyboardButton(text='Рассылка'),
	]

],resize_keyboard=True, one_time_keyboard=True)


reply_keyboard = ReplyKeyboardMarkup(keyboard=[
	[
		KeyboardButton(text='Уровень'),
		KeyboardButton(text='Помощь'),
	],
],resize_keyboard=True, one_time_keyboard=True)



textbutton1 = 'Мастер'
textbutton2 = 'Профи'
textbutton3 = 'Бизнес'
textbutton4 = 'Помощь'
textbutton5 = 'Статистика'
textbutton6 = 'Мой_уровень'
textbutton7 = 'Изменить_уровень'
textbutton8 = 'Рассылка'
textbutton9 = 'Пропустить'
textbutton10 = 'Отмена'
textbutton11 = 'Отмена'

# b1 = KeyboardButton(f'/{textbutton1}')
# b2 = KeyboardButton(f'/{textbutton2}')
# b3 = KeyboardButton(f'/{textbutton3}')


def kb_clients():
	b4 = KeyboardButton(f'/{textbutton4}')
	b6 = KeyboardButton(f'/{textbutton6}')
	b7 = KeyboardButton(f'/{textbutton7}')
	kb_clients = ReplyKeyboardMarkup(resize_keyboard=True)
	return kb_clients.add(b6).insert(b7).add(b4)  # button |_b1_|_b2_|_b3_|


def kb_admin():
	b4 = KeyboardButton(f'/{textbutton4}')
	b5 = KeyboardButton(f'/{textbutton5}')
	b8 = KeyboardButton(f'/{textbutton8}')
	kb_admin = ReplyKeyboardMarkup(resize_keyboard=True)
	return kb_admin.add(b4).insert(b5).add(b8)


def kb_send_out():
	b9 = KeyboardButton(f'/{textbutton9}')
	b10 = KeyboardButton(f'/{textbutton10}')
	kb_send_out = ReplyKeyboardMarkup(resize_keyboard=True)
	return kb_send_out.add(b9).insert(b10)