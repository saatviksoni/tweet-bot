import songs
import tweepy
import re
from dotenv import load_dotenv
import os

load_dotenv()    
auth = tweepy.OAuthHandler(os.environ.get('api_key'), os.environ.get('api_secret_key'))
auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))
username_bot = 'LanaDelReyBot_'
api = tweepy.API(auth)
api = tweepy.API(auth, wait_on_rate_limit=True)
pattern = re.compile(r'id.([0-9]+)')
songs.lyrics()
with open('lyrics.txt') as file:
    text = file.read()
count = 0
words = text.split('\n\n')
thread_len = len(words)
initial_tweet_text = words[0]
try:
    api.update_status(f'{initial_tweet_text}')
    count += 1
except:
    api.update_status(f'{initial_tweet_text}[:140]')
    count += 1
    tweet = api.home_timeline()
    matches = pattern.findall(str(tweet))
    last_tweet_id = matches[0]
    api.update_status(f'{initial_tweet_text}[140:]')    


for count in range(count, thread_len):
    tweet_text = words[count]                       
    tweet = api.home_timeline()
    matches = pattern.findall(str(tweet))
    last_tweet_id = matches[0]
    try:    
        api.update_status(f'{tweet_text}', int(last_tweet_id)) 
    except:
        api.update_status(f'{tweet_text[:140]}', int(last_tweet_id))
        tweet = api.home_timeline()
        matches = pattern.findall(str(tweet))
        last_tweet_id = matches[0]
        count += 1
        api.update_status(f'{tweet_text[140:]}', int(last_tweet_id))     

