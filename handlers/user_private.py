from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f


user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('П')

@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Меню:')

@user_private_router.message(Command('about'))
async def about_cmd(message:types.Message):
    await message.answer('О нас:')


@user_private_router.message(or_f(Command('payement'), ((F.text.lower().contains('оплат')) | (F.text.lower().contains('заплат')))))
async def payement_cmd(message:types.Message):
    await message.answer('Варианты оплаты:')
    

@user_private_router.message(or_f(Command('shipping'), F.text.lower().contains('доставк') | F.text.lower().coтtains('даставк')))
async def shipping_cmd(message:types.Message):
    await message.answer('Варианты доставки:')