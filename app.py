from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import CommandStart

bot = Bot(token='6903256584:AAH_B-UtzEiQ0y0RJ1scJ9_pNOpz_tbL4Ys')

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Введите свой тег')

@dp.message()
async def stst(message: types.Message, bot: Bot):
    await bot.send_message(message.chat.id, )



async def main():
    await dp.start_polling(bot)


asyncio.run(main())
