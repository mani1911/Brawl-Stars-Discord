import discord
import os
import re

from dotenv import load_dotenv
from helpers.content import BOT_HELP
from helpers.scrape import ScrapeBSBlog

# Load all env
load_dotenv()
token = os.getenv('BOT_TOKEN')
bot_name = os.getenv('BOT_NAME')
brawl_stars_blog_url = os.getenv('BRAWL_STARS_BLOG_URL')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Client Events
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # print(f'Message : {message.content}')
    msg_arr = message.content.split()
    if len(msg_arr) < 2 or msg_arr[0] != bot_name:
        return
    if msg_arr[1] == 'help':
        await message.channel.send('Poda Punda')
    elif msg_arr[1] == 'desc':
        await message.channel.send(BOT_HELP)
    elif msg_arr[1] == 'news':
        try:
            news_len = int(msg_arr[2]) if len(msg_arr) == 3 else 10000
            news = ScrapeBSBlog(brawl_stars_blog_url)
            if type(news) is list:
                for ind in range(min(news_len, len(news))):
                    new = news[ind]
                    await message.channel.send(new[0])
            else:
                await message.channel.send(news)
        except Exception as e:
            print(f"An error occurred: {e}")
            return 'I am unable to fetch Brawl Stars news at the moment'
    



client.run(token)