import csv
import tweepy
import pandas as pd
####input your credentials here
from tweepy.auth import OAuthHandler
auth = OAuthHandler('WNUpykrIjiGF0NKoV7qk7uiNj', 'Nhe0GjOkbaQKbPMLTqcAYQnqMnz3Edpdup28h2R2KqRLa6iBDN')
auth.set_access_token('956917059287375875-EThit80MxgQPTJlh7ZObqyHsoV8Q2D7', 'eLv893meGppqfX3xOr8SJ93kpsbZpoOiRsVM3XTgJryZM')

auth = tweepy.OAuthHandler('WNUpykrIjiGF0NKoV7qk7uiNj', 'Nhe0GjOkbaQKbPMLTqcAYQnqMnz3Edpdup28h2R2KqRLa6iBDN')
auth.set_access_token('956917059287375875-EThit80MxgQPTJlh7ZObqyHsoV8Q2D7', 'eLv893meGppqfX3xOr8SJ93kpsbZpoOiRsVM3XTgJryZM')
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('data.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search,q="#ootd",count=100,
                           include_entities=True,
                           lang="en",
                           since="2018-11-13").items():

    if 'media' in tweet.entities:
        for image in tweet.entities['media']:
            if tweet.favorite_count > 50:
                print(image['media_url'])
                print(image['url'])
 
    # csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])