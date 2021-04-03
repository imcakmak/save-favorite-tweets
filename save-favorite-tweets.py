import oauth2 as oauth
import json

TWITTER_USERNAME = ""  # Target's twitter username. (Can be yourself or someone else)
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""  # aka access token
ACCESS_SECRET = ""  # aka access token secret
TWEETS_PER_REQUEST = "200"  # You don't want to modify this unless the maximum number of tweet retrieval per request is changed by Twitter dev team

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
client = oauth.Client(consumer, access_token)
endpoint = "https://api.twitter.com/1.1/favorites/list.json?count=" + TWEETS_PER_REQUEST + "&screen_name=" + TWITTER_USERNAME

text_file = open("output.txt", "w", encoding="utf-8")

def fn_save(endpoint):
    response, data = client.request(endpoint)
    print("Access was successful.")
    tweets = json.loads(data)
    print(str(len(tweets)) + " new tweets are retrieved")
    print("Retrieved tweets are being saved..")
    for tweet in tweets:
        text_file.write(tweet['text'] + "\n")
        print("|", end="")
    print("")
    print("Save was successful.")
    if len(tweets) > 1:
        print("Trying to access " + str(len(tweets) - 1) + "th tweet's ID..")
        max_id = tweets[len(tweets)-1]["id"]
        endpoint = "https://api.twitter.com/1.1/favorites/list.json?count=" + TWEETS_PER_REQUEST + "&screen_name=" + TWITTER_USERNAME + "&max_id=" + str(max_id)
        fn_save(endpoint)
    else:
        return

fn_save(endpoint)
print("All tweets are saved.")
text_file.close()
