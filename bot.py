import asyncio
from configer import config
import logging

from aiogram import Bot, Dispatcher, types

from handlers.start import register_start_handler
from handlers.game import register_game_handler
from handlers.pinok import register_pinok_handler
from handlers.callin import register_callin_handler
from handlers.familycoins import register_family_handler

logging.basicConfig(level=logging.INFO)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Стартуем 🚀"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=config.TOKEN)
    dp = Dispatcher(bot)

    register_start_handler(dp)
    register_game_handler(dp)
    register_pinok_handler(dp)
    register_callin_handler(dp)
    register_family_handler(dp)

    await set_commands(bot)

    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())