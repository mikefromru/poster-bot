import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import os, sys
import random
import praw
import asyncpraw

def get_funny_animals():
    ua = UserAgent()
    header = {'User-Agent':  str(ua.chrome)}

    # url = os.getenv('URL_RSS_4')
    url = 'https://www.reddit.com/r/FunnyAnimals/'
    try:
        s = requests.Session()

        r = s.get(url, headers=header)
        # r = requests.get(url, headers=header)
    except Exception as err:
        print(f'Error fetching the URL {url}')
        return sys.exit()

    soup = bs(r.content, 'lxml')
    item = soup.find("h1", class_="_2yYPPW47QxD4lFQTKpfpLQ")

    # item = soup.find('h3', class_='_eYtD2XCVieq6emjKBH3m')
    # item = soup.find_all('h3')
    # item = soup.find_all('h3')
    
    print(item)

# get_funny_animals()

# current_funny_pic = {'id': 3, 'title': None}
# lst = []

# funny_post = {}
funny_post = []

async def get_funnypics():
 
    ua = UserAgent()
    # reddit = praw.Reddit(
    reddit = asyncpraw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        user_agent=str(ua.chrome),

    )

    # posts = await reddit.subreddit("FunnyAnimals").top(limit=100)

    lst_subreddits = ['WTF', 'hmmm', 'memes', 'aww', 'Cursed_Images', 'Funnypics', 'FunnyPhotoshop']
    # lst_subreddits = ['WTF', 'hmmm']
    # lst_subreddits = ['FunnyAnimals', 'shitposting', 'Pikabu', 'perfectlycutscreams', 'funny', 'Funnypics']
    subreddit = await reddit.subreddit(random.choice(lst_subreddits))
    # subreddit = await reddit.subreddit("perfectlycutscreams")
    # subreddit = await reddit.subreddit("aww")
    # posts = subreddit.top(limit=10)
    # subs = []




    async for post in subreddit.top(limit=100):
        # print(post.media)
        if post.is_video:
            # video_url = post.media["reddit_video"]["fallback_url"]
            # audio_url = video_url.split("DASH_")[0] + "audio"
            # audio_url_alternatvie = video_url.split("DASH_")[0] + "DASH_audio.mp4"
            # dct = {'type': 'video', 'url': audio_url_alternatvie}

            # dct = {'type': 'video', 'url': post.media.get('reddit_video').get('fallback_url')}
            # funny_post.append(dct)
            pass

        elif os.path.splitext(post.url)[1] in ['.jpg', '.png']: 
            if post.subreddit in ['hmmm', 'aww']:
                dct = {'type': 'picture', 'title': '', 'url': post.url}
            else:
                dct = {'type': 'picture', 'title': post.title, 'url': post.url}
            funny_post.append(dct)
    
    return random.choice(funny_post)










    # print(random.choice(funny_post))
        # subs.append(posts.title)

        # print(list(posts))
        # posts = reddit.subreddit("perfectlycutscreams").top(limit=10)

        # var = list(posts)
        # bar = random.choice(var)
        # if bar.is_video:
        #     print('video')
        #     print(bar.media)
        #     funny_post['type'] = 'video'
        #     funny_post['url'] = bar.media.get('reddit_video').get('scrubber_media_url')

        # elif os.path.splitext(bar.url)[1] in ['.jpg', '.png']: 
        #     funny_post['type'] = 'picture'
        #     funny_post['url'] = bar.url
        
        # return funny_post







        # print(bar.title, bar.)
    # print(random.choice(var.title))
    # var = random.choice(posts)
    # print(var.title)
    # for post in posts:
        # print(post.title)
        # if post.is_video:
            # print(post.media)
        # scrubber_media_url
        # 'fallback_url'
        # if post.is
        # if post.is_video:
        # print(post.id, ' <<< post.id')
            # print(post.url, post.name, ' <<< post.url')


        # if os.path.splitext(post.url)[1] == '.jpg' and post.id != current_funny_pic.get('id'): 
        # if os.path.splitext(post.url)[1] == '.jpg': 
            # lst.append(rrent_funny_pic['id'] = post.id)
            # lst.append({'id': post.id, 'title': post.title, 'url': post.url, 'name': post.name})
            # current_funny_pic['url'] = post.url

    # print(lst, len(lst)) 
    # return lst

    # ua = UserAgent()
    # header = {'User-Agent':  str(ua.chrome)}



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

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_funnypics())

