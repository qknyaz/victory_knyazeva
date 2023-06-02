from aiogram import types
from aiogram.fsm.state import StatesGroup, State


# Машина состояний
class FSM(StatesGroup):
	text = State()
	photo = State()
	file = State()
	audio = State()
	groups = State()
