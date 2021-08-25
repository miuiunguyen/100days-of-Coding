pip install instabot
from instabot import Bot
bot = Bot()
bot.login(username="", password="")
######  get follower info #######
my_followers = bot.get_user_followers("thepresentwriter")
for follower in my_followers:
    print(follower)

