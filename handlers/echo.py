from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F, Router

router_echo = Router()

@router_echo.message()
async def echo(message: Message):
    await message.answer(f"Ты написал: {message.text}")