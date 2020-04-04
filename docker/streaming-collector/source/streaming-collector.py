import tweepy
import os
from pymongo import MongoClient
import time
import requests


tweets = MongoClient(host='mongodb').streamingCollector.tweets_portuguese

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.lang == 'pt':
            print(status.text)
            requests.post('http://queue:5000/api/v1/cache',data = {'text': status.text})
            tweets.insert_one(status._json)


def get_api():
    auth = tweepy.OAuthHandler(os.environ['API_KEY'], os.environ['API_SECRET_KEY'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def run():
    api = get_api()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['*'])


if __name__ == '__main__':
    print('starting...')
    run()