from aiogram import Router, F
from aiogram.filters import Command,CommandStart
from aiogram.types import Message, CallbackQuery
import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message:Message):
    await message.answer("Wellcome to the simple bot!!!")
    await message.answer("Say ping!!!")

@router.message(Command('/help'))
async def helping(message:Message):
    await message.answer("Hey i've just heard what you want a help?")

@router.message(Command('/robotics'))
async def robot(message:Message):
    await message.answer("Check the robotics FTC by FIRST")

@router.message()
async def ping_pong(message:Message):
    if message.text.lower() == 'ping':
        await message.answer('pong', reply_markup=kb.ping_pong)

@router.callback_query(F.data == 'pong')
async def ponging(callback:CallbackQuery):
    await callback.answer()
    await callback.message.answer("pong")