import asyncio
from fake_useragent import UserAgent
import os
import random
import asyncpraw


# Mine
from .local_tools import lst_subreddits

funny_post = []

async def get_memes():
 
    ua = UserAgent()
    reddit = asyncpraw.Reddit(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        user_agent=str(ua.chrome),

    )
    subreddit = await reddit.subreddit(random.choice(lst_subreddits))

    async for post in subreddit.hot(limit=100):
        if post.is_video:
            # print(post.media)
            pass

        elif os.path.splitext(post.url)[1] in ['.jpg', '.png']: 
            dct = {'type': 'picture', 'url': post.url}
            funny_post.append(dct)
    
    return random.choice(funny_post)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_memes())

