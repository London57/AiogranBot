from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_groups_router
from commands.bot_cmnds_list import private

ALLOWED_UPDATES = ['message', 'edited_message']
bot = Bot(token=os.getenv('TOKEN'))

dp = Dispatcher()
dp.include_routers(user_private_router, user_groups_router)





async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
