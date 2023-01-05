import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from handlers.start import buttons, start
from handlers.gamee import get_keyboard, get_keyboard2

from configer import config

bot = Bot(token=config.TOKEN)

sappbut = types.InlineKeyboardButton('5x5|24 бомбы', callback_data='5but')
back_button = types.InlineKeyboardButton('Назад 🔙', callback_data='cancel')
sapperKB = types.InlineKeyboardMarkup(row_width=2).add(sappbut).row(back_button)


async def sapper(message: types.Message):
    await message.answer('Батя, вот она, та самая игра, в которую можно играть часы напролет)) И даже нужно)', reply_markup=sapperKB)


async def fith(call: types.CallbackQuery):
    reply_markupp = await get_keyboard()
    await call.message.edit_text(text='Игра 5х5|24 бомбы\nВсе будет зависеть от твоего первого хода. Ну и последнего соответственно))', reply_markup=reply_markupp)


async def trust(call: types.CallbackQuery):
    reply_markupp = await get_keyboard2()
    await call.message.edit_text(text='Ура, +200 руб в Семейную казну', reply_markup=reply_markupp)
    config.familycoin = config.familycoin + 200
    await asyncio.sleep(2)
    await call.message.edit_text(text='Ура, +200 руб в Семейную казну', reply_markup=None)
    await call.message.answer(text='Вы вернулись в главное меню.', reply_markup=start)


async def trustwin(call: types.CallbackQuery):
    reply_markupp = await get_keyboard2()
    await  call.message.edit_text(text='Ничего себе, я поражен. -100 руб из Семейной казны', reply_markup=reply_markupp)
    config.familycoin = config.familycoin - 100
    await asyncio.sleep(2)
    await call.message.edit_text(text='Ничего себе, я поражен. -100 руб из Семейной казны', reply_markup=None)
    await call.message.answer(text='Вы вернулись в главное меню.', reply_markup=start)


async def nopetap(call: types.CallbackQuery):
    await call.answer(text='Нельзя', show_alert=True)


async def cancel(call: types.CallbackQuery):
    await call.message.edit_text(text='Ну назад, так назад', reply_markup=None)
    await call.message.answer(text='Вы вернулись в главное меню', reply_markup=start)


def register_game_handler(dp: Dispatcher):
    dp.register_message_handler(sapper, Text(equals=buttons[2]), state='*')
    dp.register_callback_query_handler(cancel, lambda call: call.data == 'cancel')
    dp.register_callback_query_handler(fith, lambda call: call.data == '5but')
    dp.register_callback_query_handler(trust, lambda call: call.data == 'bomb')
    dp.register_callback_query_handler(trustwin, lambda call: call.data == 'win')
    dp.register_callback_query_handler(nopetap, lambda call: call.data == 'nope')
