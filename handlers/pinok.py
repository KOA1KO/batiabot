from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from handlers.start import buttons, start

import config

bot = Bot(token=config.TOKEN)

jena = types.InlineKeyboardButton('Жена', callback_data='for_mom')
griga = types.InlineKeyboardButton('Гриша', callback_data='for_griga')
dania = types.InlineKeyboardButton('Даня', callback_data='for_dania')
mija = types.InlineKeyboardButton('Миша', callback_data='for_mija')
back_buttonss = types.InlineKeyboardButton('Назад 🔙', callback_data='backk')
pinok = types.InlineKeyboardMarkup(row_width=4).add(jena, griga, dania, mija).row(back_buttonss)


async def funok(message: types.Message):
    await message.answer('Кого пнуть?', reply_markup=pinok)


async def pinokformommy(call: types.CallbackQuery):
    await call.message.edit_text(text='Пинок отправлен обратно. Маму нельзя пинать.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def pinokforgriga(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.mommy, text='Батя отправил Грише пинка.')
    await call.message.edit_text(text='Пинок отправлен Грише.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def pinokfordania(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.dania, text='Батя отправил тебе пинка.')
    await call.message.edit_text(text='Пинок отправлен Даниле.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def pinokformija(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.mija, text='Батя отправил тебе пинка.')
    await call.message.edit_text(text='Пинок отправлен Мише.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def cancelll(call: types.CallbackQuery):
    await call.message.edit_text(text='Ну назад, так назад', reply_markup=None)
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


def register_pinok_handler(dp: Dispatcher):
    dp.register_message_handler(funok, Text(equals=buttons[0]))
    dp.register_callback_query_handler(pinokformommy, lambda call: call.data == 'for_mom')
    dp.register_callback_query_handler(pinokforgriga, lambda call: call.data == 'for_griga')
    dp.register_callback_query_handler(pinokfordania, lambda call: call.data == 'for_dania')
    dp.register_callback_query_handler(pinokformija, lambda call: call.data == 'for_mija')
    dp.register_callback_query_handler(cancelll, lambda call: call.data == 'backk')
