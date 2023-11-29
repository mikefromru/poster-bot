import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import os

lst = []

current_post = {}

def get_news() -> dict():
    global current_post
    ua = UserAgent()
    header = {'User-Agent':  str(ua.chrome)}
    url = os.getenv('URL_RSS_1')

    try:
        r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        print(err)

    soup = bs(r.text, "xml")

    item = soup.find('item')
    post = {
            'title': item.title.text.strip(), 
            'description': item.description.text.replace('<br />', '').strip(),
            'category': item.category.text.strip(),
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