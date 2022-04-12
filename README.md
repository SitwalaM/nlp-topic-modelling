# Topic Modelling with Natural Language Processing (NLP)
## Project Motivation and Description

Public sentiment can often be gauged by activity and discussions on social media platforms such as twitter. Topic modelling is an unsupervised machine learning algorithm that can be used to collect abstract topics in a collection of documents. In this project, the aim is to use topic modelling to monitor activity on tweets that are polarizing in nature and could lead to public unrest. This type of modelling can be used for other use cases such as tracking activity in discussions around investments such as cryptocurrency. In this project, we use data from South Africa to use topic modelling to attempt to isolate tweets centred around anti-foreigner sentiment. These insights can be used as an alert for possible unrest due to rise in polarizing discussions on social media. The architecture of the for the pipeline used is shown below, a topic model is used to process a batch of tweets every 8 hours and the metrics for the topic of interest (anti-foreigner sentiment) are monitored in a dashboard.

![system](https://github.com/SitwalaM/nlp-topic-modelling/blob/develop/images/system.png)

## Introduction

Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can. Its end applications are many — chatbots, recommender systems, search, virtual assistants, etc.

For this project we chose to focus on the **Topic Modelling** aspect of Natural Language Processing. 

Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document. For example, there are 1000 documents and 500 words in each document. So to process this it requires 500x1000 = 500000 threads. So when you divide the document containing certain topics then if there are 5 topics present in it, the processing is just 5x500 words = 2500 threads. This is simplier than processing the entire document and this is how topic modelling works.

In Topic modelling, topics that best describes a set of documents are identified. These topics will only emerge during the topic modelling process (therefore called latent). And one popular topic modelling technique is known as Latent Dirichlet Allocation (LDA). It is an unsupervised approach of recognizing or extracting the patterns of word clusters and frequencies of words in the document by detecting the patterns like clustering algorithms which divides the data into different parts.

A very important thing to keep in mind here is that it's actually very difficult to evaluate an unsupervised learning model's effectiveness because we didn't actually know the correct topic or the right answer to begin with. All we know is that the documents clustered together share some sort of similar topic ideas. It's up to the user to identify what these topics actually represent. 

The text preprocessing phase in NLP involves removing stopwords, punctuation marks and other unnecessary symbols, stemming, lemmatization and encoding them to ML language using [Countvectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) or [Tfidf](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) vectorizer to make text processing easier.

## Dataset Used

We used Machine Learning to explore which topics our followers on twitter are engaging with the most. Next step is to actually get the data from a Twitter api using [Tweepy](http://docs.tweepy.org/en/latest/) and other tools to pull data and refine data to get to the data we need. We set our region to South Africa to enbale us track the change in activities on topics such as unrest and riots.

Notebook used to extract data:[ Data Pull Notebook](https://github.com/SitwalaM/nlp-topic-modelling/blob/develop/notebooks/twitter_starter.ipynb)

## Preprocessing

After pulling and refining the data from the Twitter api and importing the required packages, we then converted it into a data frame and cleaned the data using a regex function to remove emojis, hashtags, extra spaces, punctuations, usernames, urls, and other unecessary signs and symbols so we can tokenize it for the next steps. Also, all stop words were removed using nltk stopwords.

### Word Cloud

Before we performed the tokenization on the dataset, we created a word cloud with our cleaned dataset to visualize the most important words. A word cloud is a visual representation of text data, which is often used to depict keyword metadata on websites, or to visualize free form text. Tags are usually single words, and the importance of each tag is shown with font size or color.

![WordCloud](https://github.com/SitwalaM/nlp-topic-modelling/blob/develop/images/wordcloud%20new.png)

From our word cloud above, we see our most dominant and important words aside South Africa relate to violence and that exactly is what we are tracking.

### Tokenization

Next we performed tokenization by using the **Python split() Function** to split the tweets into smaller units, such as individual so the meaning of the text could easily be interpreted by analyzing the words present in the text. Before processing a natural language, we need to identify the words that constitute a string of characters. That’s why tokenization is the most basic step to proceed with NLP (text data). 

### Lemmentization

Lemmatization brings a shorter word or base word. The difference between it and stemming is it gets a much more meaningful form than what stemming does and it is more accurate than stemming. The advantage of this is, we get to reduce the total number of unique words in the dictionary. As a result, the number of columns in the document-word matrix created by TfidfVectorizer will be denser with lesser columns.

### Vectorization

To build any model in machine learning or deep learning, the final level data has to be in numerical form because models don’t understand text or image data directly as humans do. Word vectorization is done to convert the text data into numerical vectors which are used to find word predictions, and word similarities/semantics. We used the TfidfVectorizer with n-grams so that instead of a single word count, we can count the word pairs. In our case bigrams and trigrams so that we are no longer treating a single word, we are now dealing with double and triple words frequently occurring together in the document. Using n_grams together with the TfidVectorizer improved our LDA model significantly.

## Modeling

In natural language processing, the latent Dirichlet allocation (LDA) discovers topics in a collection of documents, and then automatically classify any individual document within the collection in terms of how "relevant" it is to each of the discovered topics. A topic is considered to be a set of terms (i.e. individual words or phrases) that, taken together, suggest a shared theme. LDA represents documents as mixtures of topics that spit out words with certain probabilities. We started with 10 topic numbers but after Grid searching, 5 was returned as the optimal number of topics.

We also tried modelling with Non-Negative Matrix Factorization and the results from it didnt vary much from LDA so we settled on using LDA and fine tuned it to perform better using grid search.

## Dashboard

## Credits

1. [Airflow on AWS EC2](https://christo-lagali.medium.com/getting-airflow-up-and-running-on-an-ec2-instance-ae4f3a69441)

2. [IBM NLP Tutorial](https://www.ibm.com/cloud/learn/natural-language-processing ) 

3. [NLP Tutorial Blog - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/05/topic-modelling-in-natural-language-processing/)  

4. [NLP Tutorial Blog - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2019/07/how-get-started-nlp-6-unique-ways-perform-tokenization/#:~:text=Tokenization%20using%20Gensim-,What%20is%20Tokenization%20in%20NLP%3F,as%20individual%20words%20or%20terms.)

5. [LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

6. [Sklearn LDA](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html)

7. [Grid Searching LDA](https://www.machinelearningplus.com/nlp/topic-modeling-python-sklearn-examples/#9buildldamodelwithsklearn)

## Authors
1. [Nancy](https://github.com/NancyArmah)
2. [Douglas](https://github.com/obengdouglas0)
3. [Mary](https://github.com/githinjimary)
4. [Siwala](https://github.com/SitwalaM)


