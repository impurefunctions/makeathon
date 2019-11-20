from twython import TwythonStreamer
from string import punctuation, whitespace
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            username = data['user']['screen_name']
            tweet = data['text']
            date = data['created_at']
            print("{}, @{}: {}".format(date,username, tweet))
            print("----------")
stream = MyStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track='#SmartGreenMakeathon')