from aiogram import Bot, Dispatcher, types

from configer import config

buttons = ['Прописать пинка', 'Ты мне нужен', 'Сапер', 'Семейная казна']
start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True).add(*buttons[:2]).row(*buttons[2:])


bot = Bot(token=config.TOKEN)


async def bot_start(message: types.Message):
    if str(message.chat.id) == config.batia:
        await message.answer('Привет, батя! Как твое самочувствие? Может ты хочешь прописать кому-нибудь пинка? или вызвать в срочном порядке!!! А может ты хочешь поиграть в одну замечательную игру?? В нее стоит играть много, очень много))', reply_markup=start)
    else:
        await message.answer('Не дозволено')
    mes = f'{message.from_user.username} пользуется твоим ботом\nID: {message.from_user.id}'
    await bot.send_message(config.mija, mes)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands='start')


