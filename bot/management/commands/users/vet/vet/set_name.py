from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.models import User
from ....loader import dp, bot
from .... import texts, buttons
from ....states import VetClientState

import asyncio

async def set_name_task(message: types.Message, state: FSMContext=None):
    name = message.text
    await state.set_data(
        {
            "name":name
        }
    )
    await message.answer(text=texts.vet_client_phone, reply_markup=buttons.cancel)
    
    await VetClientState.phone.set()
    
    
@dp.message_handler(content_types='text', state=VetClientState.name)
async def func(message: types.Message, state: FSMContext=None):
    asyncio.create_task(set_name_task(message, state))