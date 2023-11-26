from aiogram import Router
from aiogram.filters import Command 
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from aiogram import Bot
import os

client_router = Router()

@client_router.message(Command('help'))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"This is help part of help, {hbold(message.from_user.id)}!")

@client_router.message(Command('description'))
async def command_help_handler(message: Message) -> None:
    await message.answer(f"This is help part of description, {hbold(message.from_user.full_name)}!")

@client_router.message(Command('start'))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

@client_router.message(Command('post'))
async def command_start_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        await bot.send_message(chat_id=os.getenv('CHAT_ID'), text='New news')
    else:
        await message.answer(f'You can not use it, {message.from_user.id}')
