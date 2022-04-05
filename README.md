# Topic Modeling with Natural Language Process (NLP)

## Introduction

Natural language processing (NLP) refers to the branch of computer science—and more specifically, the branch of artificial intelligence or AI—concerned with giving computers the ability to understand text and spoken words in much the same way human beings can.

*source: https://www.ibm.com/cloud/learn/natural-language-processing*

For this project we chose to focus on the **Topic Modeling** aspect of Natural Language Processing. 

Topic modelling is recognizing the words from the topics present in the document or the corpus of data. This is useful because extracting the words from a document takes more time and is much more complex than extracting them from topics present in the document. For example, there are 1000 documents and 500 words in each document. So to process this it requires 500*1000 = 500000 threads. So when you divide the document containing certain topics then if there are 5 topics present in it, the processing is just 5*500 words = 2500 threads. This is simplier than processing the entire document and this is how topic modelling works.

The text preprocessing phase in NLP involves removing stopwords, punctuation marks and other unnecessary symbols, stemming, lemmatization and encoding them to ML language using Countvectorizer or Tfidf vectorizer to make text processing easier.

## Data Extraction and Preprocessing






