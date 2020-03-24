import tweepy
import os
from pymongo import MongoClient
import time

tweets = MongoClient(host='mongodb').test.streamingCollector

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if status.lang == 'pt':
            print(status.text)
            tweets.insert_one(status._json)


def get_api():
    auth = tweepy.OAuthHandler(os.environ['API_KEY'], os.environ['API_SECRET_KEY'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def run():
    api = get_api()
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['bh', 'belo','horizonte'])


if __name__ == '__main__':
    print('starting...')
    run()