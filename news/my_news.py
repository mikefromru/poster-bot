import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import random
import time



lst = []
lst = [d for d in lst if not any(value is None for value in d.values())]

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
    url = 'https://news.ru/rss/type/post/'

    try:
        r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        print(err)

    soup = bs(r.text, "xml")
    try:
        item = soup.find('item')
        dct = {
                'title': item.title.text, 
                'description': item.description.text,
                # 'pub': item.puDate,
                'enclosure': item.enclosure.get('url'),
                'category': item.category.text,
            }
        if current_post.get('title') != dct.get('title'):
            print('Posting ...')
            current_post = dct
            return dct
        else:
            print('This post is posted already ...')
            return None

    except AttributeError as err:
        print(err)
        return None


    # dct = {
        # 'title': kak.title.text,

    # }
    '''
    for item in soup.find_all('item'):
        dct = {
                'title': item.title.text, 
                'description': item.description.text,
                # 'pub': item.puDate,
                'enclosure': foo(item.enclosure),
                'category': item.category.text,
            }

        lst.append(dct)
        updated_lst.append(dct)
    '''

    print(f'Amount: {len(lst)}')
    # if lst[0].get('title')
    return None
    # return {'title': '', 'description': '', 'category': ''}


'''
lst = []

def get_news() -> dict():

    if len(lst) == 0:
        ua = UserAgent()
        header = {'User-Agent':  str(ua.chrome)}
        url = 'https://news.ru/rss/type/post/'

        try:
            r = requests.get(url, headers=header)
        except Exception as err:
            print(f'Error fetching the URL {url}')
            print(err)

        soup = bs(r.text, "xml")

        for item in soup.find_all('item'):
            dct = {
                    'title': item.title.text, 
                    'description': item.description.text,
                    # 'pub': item.puDate,
                    'enclosure': foo(item.enclosure),
                    'category': item.category.text,
                }
            lst.append(dct)


    print(f'Amount: {len(lst)}')
    # print(lst)
    return lst.pop()
    # return random.choice(lst)
'''
