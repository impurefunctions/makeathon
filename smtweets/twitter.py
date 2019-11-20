from twython import Twython
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
message = "Wastes at zone 2"
twitter.update_status(status=message)
#twitter.get_retweets()
print("Tweeted: %s" % message)