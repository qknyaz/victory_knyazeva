from typing import Union

from aiogram import Router
from aiogram.filters import Filter, BaseFilter

from config import GROUP
from loader import dp


from aiogram import F
from aiogram.types import Message, Chat

class ChatIdFilter(BaseFilter):  # [1]
    def __init__(self, chat_id: Union[str, list]): # [2]
        self.chat_id = chat_id

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_id, str):

            return message.chat.id == self.chat_id
        else:
            return message.chat.id in self.chat_id


router = Router()
@router.message(F.message.chat.id == GROUP)
async def message_handler(message: Message):
	print(GROUP)