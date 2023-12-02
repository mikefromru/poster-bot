import asyncio
from aiogram import Router
from aiogram.filters import Command 
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from aiogram import Bot
import os

from news.my_news import get_news, get_funnypics

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


# https://v.redd.it/h6y4pu255q3c1

@client_router.message(Command('post_mems'))
async def command_mems_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        while True:
            post = await get_funnypics()
            if post.get('type') == 'video':
                await bot.send_video(
                    chat_id=os.getenv('HUMOR_CHAT_ID'), 
                    video=post.get('url'),
                )
            else:
                await bot.send_photo(
                    chat_id=os.getenv('HUMOR_CHAT_ID'), 
                    photo=post.get('url'),
                    caption=f'{hbold(post.get("title"))}',
                )
            await asyncio.sleep(600)


@client_router.message(Command('post_mems__'))
async def command_mems_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        # post = get_funnypics()
        # while len(post) != 0:
        # chat_id=os.getenv('HUMOR_CHAT_ID'), 
        await bot.send_video(
                # chat_id=os.getenv('HUMOR_CHAT_ID'), 
            message.chat.id,
            'https://v.redd.it/h6y4pu255q3c1',
                # photo=post[0].get('url'),
                # caption=f'{hbold(post[0].get("title"))}',
        )
            # post.pop(0)
            # await asyncio.sleep(3) 


    # while True:
        # await message.answer('Mems!')
        # await asyncio.sleep(10) 

@client_router.message(Command('post_news'))
async def command_news_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        while True:
            post = get_news()
            if post != None:
                try:
                    await bot.send_photo(
                        chat_id=os.getenv('NEWS_CHAT_ID'), 
                        photo=post.get('enclosure'),
                        caption=f'{hbold(post.get("title"))}\n\n{post.get("description")}\n{post.get("category")}',
                    )

                except:
                    await bot.send_message(
                        chat_id=os.getenv('CHAT_ID'), 
                        text=f'{hbold(post.get("title"))}\n\n{post.get("description")}\n{post.get("category")}',
                    )
            await asyncio.sleep(180) 
        else:
            pass
    else:
        await message.answer(f'You can not use it, {message.from_user.id}')
