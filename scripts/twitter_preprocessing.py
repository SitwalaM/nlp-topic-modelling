import pandas as pd
import numpy as np
import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import pickle

# download stop_words
nltk.download('stopwords')


data = pd.read_csv("scripts/dataset.csv", parse_dates=["date_created"],   encoding="ISO-8859-1")


def clean(text):
    """cleans the text to prepare for NLP using regex"""
    
    text = str(text).lower()
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub(r'[^a-z A-Z]', ' ',text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = re.sub(r'[^\w\s]','',text)
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'[^\w\s]','',text)
    text = re.sub(r'@[A-Za-z0–9]+', '', text) 
    text = re.sub(r' +', ' ', text)
    return text

def process_tweets(df):

    # clean tweets
    df['clean_tweet'] = df.tweet.apply(clean)

    # remove the stopwords
    stop_words = set(stopwords.words("english"))
    df["clean_tweet"] = df["clean_tweet"].apply(lambda x : " ".join([w.lower() for w in x.split() if w not in stop_words and len(w) > 3]))

    return df

