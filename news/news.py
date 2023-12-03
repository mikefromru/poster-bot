import asyncio
import aiohttp
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import os, sys
import random

current_post = {}


async def get_news() -> dict():
    global current_post
    ua = UserAgent()
    header = {'User-Agent':  str(ua.chrome)}
    url = os.getenv('URL_RSS_1')


    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as r:    

            soup = bs(await r.text(), "xml")

            item = soup.find('item')
            post = {
                    'title': item.title.text.strip(), 
                    'description': item.description.text.replace('<br />', '').strip(),
                    # 'category': item.category.text.strip(),
                }

            link_pic = item.enclosure.get('url')

            # check a picture for extension
            # not add the pic that is not related to the post
            if os.path.splitext(link_pic)[1] != '.png':
                post['enclosure'] = link_pic

            if current_post.get('title') != post.get('title'):
                print('Posting ...')
                current_post = post
                return current_post
            else:
                print('This post is posted already ...')
                return None




# def get_news() -> dict():
#     global current_post
#     ua = UserAgent()
#     header = {'User-Agent':  str(ua.chrome)}
#     url = os.getenv('URL_RSS_1')

#     try:
#         r = requests.get(url, headers=header)
#     except Exception as err:
#         print(f'Error fetching the URL {url}')
#         print(err)

#     soup = bs(r.text, "xml")

#     item = soup.find('item')
#     post = {
#             'title': item.title.text.strip(), 
#             'description': item.description.text.replace('<br />', '').strip(),
#             # 'category': item.category.text.strip(),
#         }

#     link_pic = item.enclosure.get('url')

#     # check a picture for extension
#     # not add the pic that is not related to the post
#     if os.path.splitext(link_pic)[1] != '.png':
#         post['enclosure'] = link_pic

#     if current_post.get('title') != post.get('title'):
#         print('Posting ...')
#         current_post = post
#         return current_post
#     else:
#         print('This post is posted already ...')
#         return None




if __name__ == "__main__":
    # change_text_on_pic()
    # foo()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_news())


