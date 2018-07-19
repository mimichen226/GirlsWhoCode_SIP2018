# Import libraries
import json

file = open("tweets.json", "r")
data = json.load(file) # Load from file into a json object

for d in data: # data is a list, d is a dictionary
    # Loop through the dictionary (which corresponds to a single
    # tweet)
    print(d["retweet_count"])
    # TO PRINT OUR DICTIONARY
#    for info_category, info in d.items():
#        print(info_category, info)

    # TO PRINT THE ACTUAL TEXT OF OUR TWEET
    # print(d["text"])

    # PRINT THE TOTAL FAVORITES OF A USER
    # print(d["user"]["favourites_count"])
    # d is our dictionary about our tweet

    # TO PRINT THE USER
    #for user_mention in d["user_mentions"]:
        # Each user_mention is a dictionary
        # it corresopnds
    #    print(user_mention["screen_name"])
    break
