#!/usr/bin/env python3
########################################
# Import required modules

from datetime import datetime
import twitter
import json

########################################
# API Credentials
#
# See README for specifics on setting up API Credentials:
# https://github.com/cozyviking/delete-old-tweets-using-python#setup-credentials

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""

########################################
# Initialize

api = twitter.Api(consumer_key = CONSUMER_KEY,
                  consumer_secret = CONSUMER_SECRET,
                  access_token_key = ACCESS_TOKEN_KEY,
                  access_token_secret = ACCESS_TOKEN_SECRET)

########################################
# Function to delete tweet by ID

def deleteTweet(tweetId):
    try:
        print("Deleting tweet #{0})".format(tweetId))
        api.DestroyStatus(tweetId)
        print("Deleted")

    except Exception as err:
        print("Execption %s\n" % err)

########################################
# Read JSON file as variable

myData = None
with open('tweetList.json') as json_file:
    myData = json.load(json_file)

########################################
# Range (in UTC offset) for tweet deletion

range_start = datetime.strptime('Jan 01 00:00:00 +0000 2021', '%b %d %H:%M:%S %z %Y')
range_end = datetime.strptime('Jan 02 00:00:00 +0000 2021', '%b %d %H:%M:%S %z %Y')

########################################
# Create list of tweet IDs

tweetsToBeDeleted = []
tweetsToBeIgnored = []

for element in myData["data"]:
    tweet_post_time = datetime.strptime(element["tweet"]["created_at"], '%a %b %d %H:%M:%S %z %Y')
    if (tweet_post_time >= range_start and tweet_post_time <= range_end):
        tweetsToBeDeleted.append(element["tweet"]["id_str"])
    else:
        tweetsToBeIgnored.append(element["tweet"]["id_str"])

print(len(tweetsToBeDeleted),len(tweetsToBeIgnored))

########################################
# Iterate over list and process deletions

for id in tweetsToBeDeleted:
    deleteTweet(id)
