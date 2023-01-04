from aiogram import types
from config import EMOJIS

import random


async def get_keyboard() -> types.InlineKeyboardMarkup:
    global bombID
    bombID = sorted(random.sample(range(0, 25), 24))
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for y in range(5):
        markup = []

        for x in range(5):
            idx = y * 5 + x
            if idx in bombID:
                markup.append(types.InlineKeyboardButton(text=EMOJIS[0], callback_data='bomb'))
            else:
                markup.append(types.InlineKeyboardButton(text=EMOJIS[0], callback_data='win'))
        keyboard.add(markup[0], markup[1], markup[2], markup[3], markup[4])

    return keyboard


async def get_keyboard2() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=5)
    for y in range(5):
        markup = []

        for x in range(5):
            idx = y * 5 + x
            if idx in bombID:
                markup.append(types.InlineKeyboardButton(text=EMOJIS[2], callback_data='nope'))
            else:
                markup.append(types.InlineKeyboardButton(text=EMOJIS[1], callback_data='nope'))
        keyboard.add(markup[0], markup[1], markup[2], markup[3], markup[4])

    return keyboard
