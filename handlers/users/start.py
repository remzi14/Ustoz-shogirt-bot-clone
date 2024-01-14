from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import requests
from loader import dp,bot
from data.config import ADMINS
from keyboards.default.menyu import menu

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text=f"<b>Assalom alaykum {message.from_user.full_name}</b>\n"
    text+=f"<b>UstozShogird kanalining rasmiy botiga xush kelibsiz!</b>\n"
    text+=f"/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!\n"
    await message.answer(text,reply_markup=menu)

