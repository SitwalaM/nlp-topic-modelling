# Topic Modeling with Natural Language Process (NLP)

## Introduction

Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can. Its end applications are many — chatbots, recommender systems, search, virtual assistants, etc.

For this project we chose to focus on the **Topic Modeling** aspect of Natural Language Processing. 

Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document. For example, there are 1000 documents and 500 words in each document. So to process this it requires 500*1000 = 500000 threads. So when you divide the document containing certain topics then if there are 5 topics present in it, the processing is just 5*500 words = 2500 threads. This is simplier than processing the entire document and this is how topic modelling works.

IntTopic modelling, topics that best describes a set of documents are identified. These topics will only emerge during the topic modelling process (therefore called latent). And one popular topic modelling technique is known as Latent Dirichlet Allocation (LDA). It is an unsupervised approach of recognizing or extracting the patterns of word clusters and frequencies of words in the document by detecting the patterns like clustering algorithms which divides the data into different parts. 

The text preprocessing phase in NLP involves removing stopwords, punctuation marks and other unnecessary symbols, stemming, lemmatization and encoding them to ML language using Countvectorizer or Tfidf vectorizer to make text processing easier.

## Dataset Used

We would use Machine Learning to explore which topics our followers on twitter are engaging with the most. Next step is to actually get the data from a Twitter api using Tweepy (http://docs.tweepy.org/en/latest/) and other tools to pull data and refine data to get to the data we need. We set our region to South Africa to enbale us track.......(ask sitwala).

## Preprocessing

After pulling and refining the data from the Twitter api and importing the required packages, we the converted it into a data frame and cleaned the data using a regex function to remove emojis, hashtags, extra spaces, punctuations, usernames, urls, and other unecessary signs and symbols so we can tokenize it for the next steps.

### Word Cloud

Before we performed the tokenization on the dataset, we created a word cloud with our cleaned dataset to visualize the most important words. A word cloud is a visual representation of text data, which is often used to depict keyword metadata on websites, or to visualize free form text. Tags are usually single words, and the importance of each tag is shown with font size or color.



### Tokenization
### Stemming & Lemmentization
### Vectorization
## Modeling
## Dashboard

*sources: 
https://www.ibm.com/cloud/learn/natural-language-processing
https://www.analyticsvidhya.com/blog/2021/05/topic-modelling-in-natural-language-processing/
*




