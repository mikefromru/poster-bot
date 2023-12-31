import asyncio
from aiogram import Router
from aiogram.filters import Command 
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from aiogram import Bot
import os
import random

from memes.memes import get_memes
from news.news import get_news


client_router = Router()

@client_router.message(Command('post_memes'))
async def command_mems_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        while True:
            post = await get_memes()
            if post.get('type') == 'video':
                await bot.send_video(
                    chat_id=os.getenv('HUMOR_CHAT_ID'), 
                    video=post.get('url'),
                )
            else:
                await bot.send_photo(
                    chat_id=os.getenv('HUMOR_CHAT_ID'), 
                    photo=post.get('url'),
                )
            await asyncio.sleep(random.randint(3600, 7200))


@client_router.message(Command('post_news'))
async def command_news_handler(message: Message, bot: Bot) -> None:
    if int(os.getenv('USER_ID')) == message.from_user.id:
        while True:
            post = await get_news()
            if post != None:
                try:
                    await bot.send_photo(
                        chat_id=os.getenv('NEWS_CHAT_ID'), 
                        photo=post.get('enclosure'),
                        caption=f'{hbold(post.get("title"))}\n\n{post.get("description")}',
                    )
                except:
                    await bot.send_message(
                        chat_id=os.getenv('NEWS_CHAT_ID'), 
                        text=f'{hbold(post.get("title"))}\n\n{post.get("description")}',
                    )
            await asyncio.sleep(180) 
    else:
        await message.answer(f'You can not use it, {message.from_user.id}')
