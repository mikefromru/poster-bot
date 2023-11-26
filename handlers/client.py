from aiogram import Router
from aiogram.filters import Command 
from aiogram.utils.markdown import hbold
from aiogram.types import Message

client_router = Router()

@client_router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"This is help part of help, {hbold(message.from_user.full_name)}!")

@client_router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

