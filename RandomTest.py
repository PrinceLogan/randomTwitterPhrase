from CredData import *
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import random
import re

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = tweepy.API(auth)

trends1 = api.trends_place(23424977) # from the end of your code # trends1 is a list with only one element in it, which
data = trends1[0]
trends = data['trends']
names = [trend['name'] for trend in trends]
random_choixe = random.choice(names)

for k in random_choixe.split("\n"):
    rando_word = re.sub(r"[^a-zA-Z0-9]+", '', k)

print(rando_word)
