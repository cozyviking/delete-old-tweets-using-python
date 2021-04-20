# Twitter API: Deleting Old Tweets using Python
## About

This is a simple Python script that utilizes the Twitter API to delete a range of tweets.
## Prerequisite

### 1. Twitter Data Archive

Before you begin, you need to download your Twitter data archive.

To download your archive, navigate to **Settings & Privacy -> Account -> Download an archive of your twitter data**. Once requested, it will take 24-48 hours for the data to become available. 

### 2. Twitter Developer Account

To access the Twitter API, you will need a Twitter Developer Account. If you don't already have one, acccess https://developer.twitter.com/en/apps and create one!

### 3. Python Modules

This script depends on the `python-twitter` module, so make sure you install it if you don't already have it: 

```bash
pip3 install python-twitter
```

## Data Formatting

In the Twitter Data Archive, you want to pull the file data/tweet.js and modify it to be in JSON format. The first line should look like this:

```JSON
   window.YTD.tweet.part0 = [ {
```

Change it to:

```JSON
{"data": [{ 
```

And the last line should look like this:

```JSON
} ]
```

Change it to: 

```JSON
} ] }
```

Save the modified file as "tweetList.json."

The rest of the file should already be in a good JSON format, so we're ready to move on to the next step! 

## Setup Credentials

Using your Twitter Developer Account, initialize the access keys/tokens required for API access: 

```python
########################################
# API Credentials

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN_KEY = ""
ACCESS_TOKEN_SECRET = ""
```

Note: You will need to create an app inside the Twitter Developer Portal before you can generate the requried keys/tokens.

## Configure Date Range

Next, set the desired start and end date range for the tweets you wish to delete: 

```python
########################################
# Range (in UTC offset) for tweet deletion

range_start = datetime.strptime('Jan 01 00:00:00 +0000 2021', '%b %d %H:%M:%S %z %Y')
range_end = datetime.strptime('Jan 02 00:00:00 +0000 2021', '%b %d %H:%M:%S %z %Y')
```

I would highly recommend setting a very small date range as a test first, just to make sure this is going to work as you intend! 

## Run!

Once you've tested and are happy with the results, you're all set to run! The high-level logic of this script is to read in the file `tweetList.json`, create an array of tweets that match the date range you wish to delete, and then iterate over this array using the Twitter API to actually delete them. 