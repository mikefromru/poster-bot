import asyncio
import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
import os, sys
import random
import praw
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




from PIL import Image
import pytesseract

def change_text_on_pic():
    # Open the image file
    # image = Image.open('pic.jpg')
    # # Perform OCR using PyTesseract
    # text = pytesseract.image_to_string(image)
    # # Print the extracted text
    # print(text)





    # Открываем изображение
    image_path = 'pic.jpg'
    image = Image.open(image_path)

    # Создаем объект для рисования на изображении
    draw = ImageDraw.Draw(image)

    # Определяем координаты и размер области, содержащей текст
    # В этом примере используются произвольные координаты
    text_position = (0, 0)
    text_width = 500
    text_height = 50

    # Заменяем текст на область фона
    # В данном случае просто закрашиваем область наложением прямоугольника с цветом фона
    background_color = (255, 255, 255)  # Цвет фона (белый)
    draw.rectangle([text_position, (text_position[0] + text_width, text_position[1] + text_height)], fill=background_color)

    # Сохраняем обработанное изображение
    processed_image_path = 'image.jpg'
    image.save(processed_image_path)




def foo():
    image = Image.open('pic.jpg')
    draw = ImageDraw.Draw(image)

    # Выбор шрифта и размера текста
    font = ImageFont.truetype("OpenSans-Bold.ttf", 36)  # Здесь вы можете выбрать другой шрифт и размер

    # Определение текста, который нужно заменить
    text_to_replace = "ME BEING PREPARED FOR 2020:"

    # Задание координат и замена текста
    x, y = 100, 100  # Примерные координаты, где вы хотите разместить новый текст
    new_text = "New Text"
    draw.text((x, y), new_text, fill="black", font=font)

    # Сохранение измененного изображения
    image.save('modified_image.jpg')




# if __name__ == "__main__":
    # change_text_on_pic()
    # foo()
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_funnypics())

