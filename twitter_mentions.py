import tweepy
from secrets import twitter_api_key, twitter_access_token, twitter_bearer_token, twitter_api_key_secret, twitter_access_token_secret
import time

auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

api = tweepy.API(auth)
mentions = api.mentions_timeline()

for mention in mentions:
    dict = mention.__dict__()
    for key, value in dict.items():
        print(dict.auth())
