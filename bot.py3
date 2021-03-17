import tweepy
import io
from time import sleep
import codecs
import requests
import random
import os
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

f = open ("poems.txt", 'r', encoding='utf-8')
text = f.read()
x = text.split("।")
random.shuffle(x);
random.shuffle(x);

for i in x:
    try:
        if (i!='\n') :
            api.update_status(i+'\n\n#FarmersProtest')
            tweets = api.mentions_timeline()
            for tweet in tweets:
                tweet.favorite()
            sleep(7200)
        else:
            pass
    except tweepy.TweepError as e:
    	print(e.reason)
    	sleep(7200)
f.close()



#text = f.read()
#f.close()
#print(text)






#for line in file_lines:
#    api.update_status(line)
#    print(file_lines)
#    sleep(3)

