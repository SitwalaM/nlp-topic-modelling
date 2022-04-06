# Topic Modelling with Natural Language Processing (NLP)

## Introduction

Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can. Its end applications are many — chatbots, recommender systems, search, virtual assistants, etc.

For this project we chose to focus on the **Topic Modelling** aspect of Natural Language Processing. 

Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document. For example, there are 1000 documents and 500 words in each document. So to process this it requires 500x1000 = 500000 threads. So when you divide the document containing certain topics then if there are 5 topics present in it, the processing is just 5x500 words = 2500 threads. This is simplier than processing the entire document and this is how topic modelling works.

In Topic modelling, topics that best describes a set of documents are identified. These topics will only emerge during the topic modelling process (therefore called latent). And one popular topic modelling technique is known as Latent Dirichlet Allocation (LDA). It is an unsupervised approach of recognizing or extracting the patterns of word clusters and frequencies of words in the document by detecting the patterns like clustering algorithms which divides the data into different parts. 

The text preprocessing phase in NLP involves removing stopwords, punctuation marks and other unnecessary symbols, stemming, lemmatization and encoding them to ML language using Countvectorizer or Tfidf vectorizer to make text processing easier.

## Dataset Used

We used Machine Learning to explore which topics our followers on twitter are engaging with the most. Next step is to actually get the data from a Twitter api using Tweepy (http://docs.tweepy.org/en/latest/) and other tools to pull data and refine data to get to the data we need. We set our region to South Africa to enbale us track the change in activities on topics such as unrest and riots.

## Preprocessing

After pulling and refining the data from the Twitter api and importing the required packages, we then converted it into a data frame and cleaned the data using a regex function to remove emojis, hashtags, extra spaces, punctuations, usernames, urls, and other unecessary signs and symbols so we can tokenize it for the next steps.

### Word Cloud

Before we performed the tokenization on the dataset, we created a word cloud with our cleaned dataset to visualize the most important words. A word cloud is a visual representation of text data, which is often used to depict keyword metadata on websites, or to visualize free form text. Tags are usually single words, and the importance of each tag is shown with font size or color.

![WordCloud](https://github.com/SitwalaM/nlp-topic-modelling/blob/develop/images/wordcloud.png)

From our word cloud above, we see our most dominant and important words aside South Africa relate to violence and that exactly is what we are tracking.

### Tokenization

Next we performed tokenization by using the **Python split() Function** to split the tweets into smaller units, such as individual so the meaning of the text could easily be interpreted by analyzing the words present in the text. Before processing a natural language, we need to identify the words that constitute a string of characters. That’s why tokenization is the most basic step to proceed with NLP (text data). 

### Lemmentization

Lemmatization brings a shorter word or base word. The difference between it and stemming is it gets a much more meaningful form than what stemming does and it is more accurate than stemming.  Using lemmatization is useful but it comes at a cost to the accuracy of the models which we experienced. Our topic results improved when we skipped the lemmatization step.

### Vectorization

To build any model in machine learning or deep learning, the final level data has to be in numerical form because models don’t understand text or image data directly as humans do. Word vectorization is done to convert the text data into numerical vectors which are used to find word predictions, and word similarities/semantics. We first tried the CountVectorizer but had to switch to using TfidfVectorizer because it showed better results with n-grams.

#### (talk about ngrams)	

## Modeling
## Dashboard

*sources:  

https://www.ibm.com/cloud/learn/natural-language-processing  

https://www.analyticsvidhya.com/blog/2021/05/topic-modelling-in-natural-language-processing/  

https://www.analyticsvidhya.com/blog/2019/07/how-get-started-nlp-6-unique-ways-perform-tokenization/#:~:text=Tokenization%20using%20Gensim-,What%20is%20Tokenization%20in%20NLP%3F,as%20individual%20words%20or%20terms.
*




