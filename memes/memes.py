import asyncio
from fake_useragent import UserAgent
import os
import random
import asyncpraw

from PIL import Image, ImageDraw, ImageFont

# Mine
from .local_tools import lst_subreddits

funny_post = []

async def get_memes():
 
    ua = UserAgent()
    # reddit = praw.Reddit(
    reddit = asyncpraw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        user_agent=str(ua.chrome),

    )

    # posts = await reddit.subreddit("FunnyAnimals").top(limit=100)

    # lst_subreddits = ['WTF', 'hmmm', 'memes', 'aww', 'funny', 'shitposting', 'funnysigns', 'Cursed_Images', 'Funnypics', 'FunnyPhotoshop']
    # lst_subreddits = lst_subreddits
    # lst_subreddits = ['WTF', 'hmmm']
    # lst_subreddits = ['FunnyAnimals', 'shitposting', 'Pikabu', 'perfectlycutscreams', 'funny', 'Funnypics']

    subreddit = await reddit.subreddit(random.choice(lst_subreddits))
    # subreddit = await reddit.subreddit("perfectlycutscreams")
    # subreddit = await reddit.subreddit("aww")
    # posts = subreddit.top(limit=10)
    # subs = []




    async for post in subreddit.hot(limit=100):
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
            # if post.subreddit in ['hmmm', 'aww', 'funny', 'Cursed_Images', 'funnysigns', 'shitposting']:
                # dct = {'type': 'picture', 'title': '', 'url': post.url}
            # else:
            dct = {'type': 'picture', 'url': post.url}
            # dct = {'type': 'picture', 'title': post.title, 'url': post.url}
            funny_post.append(dct)
    
    return random.choice(funny_post)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_memes())

