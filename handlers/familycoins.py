from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from handlers.start import buttons, start

import config

bot = Bot(token=config.TOKEN)


async def familyy(message: types.Message):
    await message.answer(text=f'Семейная казна\nБаланс: {config.familycoin} руб.', reply_markup=start)


def register_family_handler(dp: Dispatcher):
    dp.register_message_handler(familyy, Text(equals=buttons[3]))