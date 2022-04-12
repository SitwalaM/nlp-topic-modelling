# import libraries
import tweepy
import configparser
import csv
import pandas as pd
import datetime as dt
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def extract():
    #read configs -- setup ini file using API credentials
    #returns tweets in pandas dataframe


    f = open("config.ini", "r")
    print(f.read())
    config = configparser.ConfigParser()
    config.read("config.ini")
    api_key = config["twitter"]["api_key"]
    api_key_secret = config["twitter"]["api_key_secret"]
    access_token = config["twitter"]["access_token"]
    access_token_secret = config["twitter"]["access_token_secret"]

    #authentication handler
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # Get tweet using api.seaarch_tweets

    tweets = [page for page in tweepy.Cursor(api.search_tweets, q ="south africa -filter:RT", lang = "en",
                                            result_type = "mixed",
                                            count = 10).pages(20)]# Open/create a file to append data to

    # write to csv file
    filename = str(dt.date.today()) + ".csv"
    if  os.path.exists(filename):
    	os.remove(filename)
    else:
        	pass
    csvFile = open(filename, 'a')
    #Use csv writer
    csvWriter = csv.writer(csvFile, delimiter = ",")
    csvWriter.writerow(["id","retweet_count",
                        "date_created",
                        "tweet"])
    for page in tweets:
        for tweet in page:
            csvWriter.writerow([tweet.id,tweet.retweet_count,
                                tweet.created_at, 
                                tweet.text.encode('utf-8')])
    csvFile.close()

    return pd.read_csv(filename)
