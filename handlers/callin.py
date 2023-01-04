from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from handlers.start import buttons, start

import config

bot = Bot(token=config.TOKEN)

cjena = types.InlineKeyboardButton('Жена', callback_data='call_mom')
cgriga = types.InlineKeyboardButton('Гриша', callback_data='call_griga')
cdania = types.InlineKeyboardButton('Даня', callback_data='call_dania')
cmija = types.InlineKeyboardButton('Миша', callback_data='call_mija')
back_button = types.InlineKeyboardButton('Назад 🔙', callback_data='cancellk')
callinnn = types.InlineKeyboardMarkup(row_width=4).add(cjena, cgriga, cdania, cmija).row(back_button)


async def funcal(message: types.Message):
    await message.answer('Кого позвать?', reply_markup=callinnn)


async def calmommy(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.mommy, text='Батя вызывает тебя. Пшшшшш... Прием')
    await call.message.edit_text(text='Вызов успешно отправлен Жене.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def calgriga(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.mommy, text='Батя вызывает Гришу. Пшшшшш... Прием')
    await call.message.edit_text(text='Вызов успешно отправлен Грише.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def calrdania(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.dania, text='Батя вызывает тебя. Пшшшшш... Прием')
    await call.message.edit_text(text='Вызов успешно отправлен Даниле.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def calmija(call: types.CallbackQuery):
    await bot.send_message(chat_id=config.mija, text='Батя вызывает тебя. Пшшшшш... Прием')
    await call.message.edit_text(text='Вызов успешно отправлен Мише.')
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


async def cancell(call: types.CallbackQuery):
    await call.message.edit_text(text='Ну назад, так назад', reply_markup=None)
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


def register_callin_handler(dp: Dispatcher):
    dp.register_message_handler(funcal, Text(equals=buttons[1]))
    dp.register_callback_query_handler(calmommy, lambda call: call.data == 'call_mom')
    dp.register_callback_query_handler(calgriga, lambda call: call.data == 'call_griga')
    dp.register_callback_query_handler(calrdania, lambda call: call.data == 'call_dania')
    dp.register_callback_query_handler(calmija, lambda call: call.data == 'call_mija')
    dp.register_callback_query_handler(cancell, lambda call: call.data == 'cancellk')

