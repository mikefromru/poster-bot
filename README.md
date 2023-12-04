# Poster Bot
## _Welcome to poster-bot_

Poster Bot is about Telegram bot.
It is totally asynchronous. This bot posts in two channels. From Reddit it gets some Subreddits only Top posts every about 2 hours then put it on memes Telegram channel. Also this bot get some news from RSS then put the news on news Telegram channel.

## Tech

Poster-bot uses a number of open source projects to work properly:

- Python - interpreted, object-oriented, high-level programming language!
- Asyncio - library to write concurrent code using the async/await syntax.
- Aiogram - modern and fully asynchronous framework for Telegram Bot.
- Aiohttp - HTTP client/server for asyncio.
- BeautifulSoup4 - library for pulling data out of HTML and XML files.
- Asyncpraw - python package that allows for simple access to Reddit's API.

Set the environment variables in the .env file (Required variables are given below for development)

```
# Telegram token
BOT_TOKEN=

# Channal IDS
HUMOR_CHAT_ID=
NEWS_CHAT_ID=
USER_ID=

# Reddit enviroment variabels
CLIENT_ID=
CLIENT_SECRET=
REDIRECT_URI=
```

Make a python file `memes/local_tools.py`
```
lst_subreddits = ['funny','memes']
```

## Installation

Poster-bot requires [Python](https://www.python.org/) v3+ to run.

Install the dependencies and run the bot.

```sh
cd poster-bot
pip install -r requirements.txt
python main.py
```

## Docker

Poster Bot is very easy to install and deploy in a Docker container.

```sh
cd poster-bot
docker build -t poster .
```

This will create the poster image and pull in the necessary dependencies.
Now you can run the Docker image.
```sh
docker run -d poster
```

