from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    diagnose = message.text

    # set data in state
    state_data = await state.get_data()
    state_data['diagnose'] = diagnose
    await state.set_data(state_data)

    # send message from user
    await message.answer(texts.vet_media, reply_markup=buttons.cancel)
    
    # chaneg state
    await VetClientState.media.set()
    
@dp.message_handler(content_types='text', state=VetClientState.diagnose)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))