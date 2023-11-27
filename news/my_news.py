import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import random
import time


lst = []

async def foo(a):
    try:
        kak = a.get('url')
        return kak 
    except:
        return None

'''
async def get_news() -> dict():
    ua = UserAgent()
    header = {
        'User-Agent':  str(ua.chrome),
    }
    # print(ua.chrome)
    url = 'https://news.ru/rss/type/post/'

    try:
        r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        print(err)

    # soup = bs(r.text, "html.parser")
    soup = bs(r.text, "xml")

    for item in soup.find_all('item'):
        dct = {
                'title': item.title.text, 
                'description': item.description.text,
                # 'pub': item.puDate,
                'enclosure': await foo(item.enclosure),
                'category': item.category.text,
            } 
        lst.append(dct)

    # return (f'{lst}, Amount: {len(lst)}')
    return lst
'''

async def get_news() -> dict():
    ua = UserAgent()
    header = {
        'User-Agent':  str(ua.chrome),
    }
    # print(ua.chrome)
    # url = 'https://news.ru/rss/type/post/'

    try:
        r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        print(err)

    # soup = bs(r.text, "html.parser")
    soup = bs(r.text, "xml")

    for item in soup.find_all('item'):
        dct = {
                'title': item.title.text, 
                'description': item.description.text,
                # 'pub': item.puDate,
                'enclosure': await foo(item.enclosure),
                'category': item.category.text,
            } 
        lst.append(dct)

    # return (f'{lst}, Amount: {len(lst)}')
    return lst


async def run_posts__():
    print('kak')
    try:
        print(lst[1])
        return lst[1]
    except:
        await get_news()

async def run_posts():
    j = 0
    while True:
        await asyncio.sleep(3)
        run_posts__()
        # time.sleep(3)
        print(j)
        j += 1



# run_posts()
'''
def run_posts():
    while True:
        if len(lst) > 0:
            # return (f'{lst}, Amount: {len(lst)}')
            print(random.choice(lst))
            lst.pop()
            # return (f'{lst}, Amount: {len(lst)}')
        else:
            print('The END >>>')
            get_news()
        time.sleep(1)

# print(run_posts())
'''