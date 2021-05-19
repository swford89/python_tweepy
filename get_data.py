import os
import tweepy
import json
from pprint import pprint

# get secret virtual environment variables
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_SECRET = os.environ['ACCESS_SECRET']

# authenticate connection to the API
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create API object
api = tweepy.API(auth)

# define user to get tweets from
handle = 'codingnomads'
tweets = api.user_timeline(handle, tweet_mode="extended")       # get untruncated text from tweets

# iterate through tweets and append to list
tweet_list = []
for tweet in tweets:
    pprint(tweet._json)
    tweet_list.append(tweet._json)

tweet_path = 'twitter-data-master/data.json'

# write list of tweets to json file
with open(tweet_path, 'w') as file:
    json.dump(tweet_list, file, indent=4)
