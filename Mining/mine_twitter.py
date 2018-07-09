## ---- author : Manohar ---- ####


# importing libraries
import tweepy
from tweepy import OAuthHandler
import csv
import re


# authenting to twitter
consumer_key = '2UBbLFsytRFLrWXmKWaKCEmLK'
consumer_secret = '	LOKYj9X3FKUppWoXedPFiu2FQ3lz5h5O9lu961L3UBUfOLZh0O'
access_token = '422674417-zS7gUKmnQLeCYBMoNBGqTfXRm8yz17fRDFExmrZo'
access_secret = 'MNpt1OkzICSFJAiYYocce3052IoveOeGtHxjiwRUGUHp4'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


# tweets of an user
tweets = []

new_tweets = api.user_timeline(screen_name='PawanKalyan', count=20, tweet_mode='extended')
for tweet in new_tweets:
    if 'retweeted_status' in tweet._json:
        te = tweet.retweeted_status.full_text
    else:
        te = tweet.full_text
    te = re.sub(r"https://t.co\S+", "", te)
    tweets.append(te)
print(tweets)


# writing it to a fille
wr_file = open('Data/tweets.csv', 'a', encoding='utf-8', newline='')
csv_writer = csv.writer(wr_file)

for i in range(len(tweets)):
    csv_writer.writerow([tweets[i], ' '])

wr_file.close()



