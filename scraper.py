import sys
import os
import tweepy
import json
import time

# Array that contains all post
list_of_posts = []

# This listener will print out all tweets it receives
class print_listener(tweepy.StreamListener):
    def __init__(self, time_limit = 10): # Set the time limit
        self.start_time = time.time()
        self.limit = time_limit

    def on_data(self, data):
        if (time.time() - self.start_time) < self.limit: # Time not yet at it's limit
            # Decode the JSON data
            tweet = json.loads(data)

            # Append the tweet to list of post
            list_of_posts.append(tweet['text'].encode('ascii', 'ignore').decode('utf-8'))
            return True

        else:
            return False

    def on_error(self, status):
        print(status)

# Dumping list_of_posts to a json file
def get_tweet_posts(posts) :
    return json.dumps(list_of_posts)


# Listener to tweepy
listener = print_listener()

# Consumer keys and access tokens, used for OAuth
consumer_key = '0jXK5oAWkQgYh7fMwhOPhUuQe'
consumer_secret = 'kALTJ1ZFthv25r4iCskTCxXjhPodq53NIybPCZU6KUeYM1RL0p'
access_token = '985003482422829057-Wr7CJHgcbR3Enf90VySd05HXPjgTVtU'
access_token_secret = 'o4wpHsDLomI59bPmhjoPMMKEN6AKRVEZYKI5UR1FZJzzg'


if __name__ == '__main__':
    # Authenticate
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Connect the stream to the listener
    stream = tweepy.Stream(auth, listener)
    # Set filter so the post will be in Indonesian
    stream.filter(track = ['Aku'])

    # Print generated tweet posts
    print (get_tweet_posts(sys.argv[1]))