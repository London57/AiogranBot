from aiogram import types, Router, F


from settings import BAD_PHRASES as BAD_PHRASES_LIST


user_groups_router = Router()

@user_groups_router.message()
async def cleaner(message: types.Message):
    for b in BAD_PHRASES_LIST:
        if b.decode() in message.text.lower().split():
            await message.answer(f'{message.from_user.full_name}, соблюдайте порядок в чате!')
            await message.delete()                                 

