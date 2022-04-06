import numpy as np
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)



# load model
with open("lda_model.pk","rb") as f:
  lda_model = pickle.load(f)

# vectorizer  
vectorizer = pickle.load(open("vectorizer.pickle", 'rb'))

# topics
topics = list(np.arange(0,10))

def get_inference(model, vectorizer, topics, text, threshold):
    """
    runs inference on text input

    paramaters
    ----------
    model: loaded model to use to transform the input
    vectorizer: instance of the vectorizer e.g TfidfVectorizer(ngram_range=(2, 3))
    topics: the list of topics in the model
    text: input string to be classified
    threshold: float of threshold to use to output a topic

    returns
    -------
    tuple => top score
    
    """
    v_text = vectorizer.transform([text])
    score = model.transform(v_text)

    labels = set()
    for i in range(len(score[0])):
        if score[0][i] > threshold:
            labels.add(topics[i])
    if not labels:
        return 'None', -1, set()

    return topics[np.argmax(score)]


#for testing predictions
data = pd.read_csv("dataset.csv", parse_dates=["date_created"],   encoding="ISO-8859-1")
from twitter_preprocessing import process_tweets
cleaned_df = process_tweets(data)
cleaned_df["topic"] = cleaned_df.clean_tweet.apply(lambda x: get_inference(lda_model,vectorizer,topics,x,0))
cleaned_df.to_csv("output.csv")
