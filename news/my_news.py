import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs

lst = []
# lst = [d for d in lst if not any(value is None for value in d.values())]

def foo(a):
    try:
        kak = a.get('url')
        return kak 
    except:
        return None

lst = []
current_post = {}

def get_news() -> dict():
    global current_post
    updated_lst = []
    # if len(lst) == 0:
    ua = UserAgent()
    header = {'User-Agent':  str(ua.chrome)}
    # url = 'https://tass.ru/rss/anews.xml?sections=NDczMA%4D%3D'
    # url = 'https://news.ru/rss/type/post/'
    url = 'https://lenta.ru/rss/'

    try:
        r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        print(err)

    soup = bs(r.text, "xml")
    try:
        item = soup.find('item')
        post = {
                'title': item.title.text, 
                'description': item.description.text,
                # 'pub': item.puDate,
                'enclosure': item.enclosure.get('url'),
                'category': item.category.text,
            }
        if current_post.get('title') != dct.get('title'):
            print('Posting ...')
            current_post = post
            return current_post
        else:
            print('This post is posted already ...')
            return None

    except AttributeError as err:
        print(err)
        return None