# Imports
import tweepy
import random
import time

# Keys and Access Tokens
CONSUMER_KEY    = 'xT8Ast2gsQ8yVgMA7HSYPpMBf'
CONSUMER_SECRET = 'V4fQ59HGKmemDBYswXhCYJXrurUwz386RhDDduVhoxtUmSbNWR'

ACCESS_TOKEN    = '798616100338601988-pU6RZaCsB93z5vqkDLqtvGrC8L4nY4b'
ACCESS_SECRET   = 'k7VViFvkK2UiVICAWI60KonnJ0QAwEKZMzVx82nrk711T'

tweets = ["you are a snacc", "are you google? cuz i just found what i was looking for", "lookin' like a whole meal", "r u chocolate pudding? cuz u thicc"]

# Authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api  = tweepy.API(auth)

# Update Status
count = 0
while True:
    count += 1
    index = random.randint(0, len(tweets) - 1)
    api.update_status(tweets[index] + " " + str(count))  # randomly a tweets from tweets
    time.sleep(10)
