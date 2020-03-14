import tweepy
import os
from pymongo import MongoClient
import time


def get_connection():
    return MongoClient(host='mongodb').test.simpleCollector

def get_api():
    auth = tweepy.OAuthHandler(os.environ['API_KEY'], os.environ['API_SECRET_KEY'])
    auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
    return tweepy.API(auth)


def run(database_connection):
    api = get_api()
    tweets = api.search(q="belo horizonte", count=50, result_type="mixed")
    for tweet in tweets:
        print(tweet.text)
        database_connection.insert_one(tweet._json)


if __name__ == '__main__':
    print('starting...')
    connection = get_connection()
    run(connection)
    print('stopping...')

#temporarizador para dar tempo de observar que o status do container está como health
time.sleep(60)