# -*- coding: utf-8 -*-
"""InformationExtraction&Comparsion.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y5r3CWgxhh8OJxtWpOQAMuCGjRcC_XL2
"""

import spacy
import numpy as np
nlp=spacy.load("en_core_web_sm")
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
import nltk

nltk.download('all')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()
from IPython.display import display
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
import sys
np.set_printoptions(threshold=sys.maxsize)

"""# **Pre Processing the Text: Tokenization,Lemmatization,Removing StopWords**"""

def preProcess(paragraph):
  doc=nlp(paragraph)
  processed_sentences=[]
  for sentence in doc.sents:
    tokens=[token.lemma_.lower() for token in sentence if not token.is_stop and not token.is_punct and not token.is_space]
    processed_sentence=" ".join(tokens)
    processed_sentences.append(processed_sentence)
  return processed_sentences

"""# **Finding Number Of Sentences in Given**"""

def findNumberOfSentences(text):
   doc = nlp(text)
   num_sentences = len(list(doc.sents))
   return num_sentences

"""# **Checking whether a Sentence Has Numerical Data or not**"""

def checkNumerical(sentence):
    doc = nlp(sentence)
    for token in doc:
        if token.like_num:
            try:                #for avoiding figures like million,billion etc.
                a=float(token.text)
                return 1
            except ValueError:
                pass
    return 0

def containNumerical_data(text):
  arr=[]
  for sentence in text:
    has_numerical=checkNumerical(sentence)
    arr.append(has_numerical)
  return arr

"""# **Creating Matrix for Similar Sentences in Both Paragraphs**"""

def check_similarity(sentence1,sentence2):
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform([sentence1, sentence2])
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def comparing_sentences(sentences1,sentences2):
    similarity_matrix = np.zeros((len(sentences2), len(sentences1)))
    for i, sentence1 in enumerate(sentences1):
        for j, sentence2 in enumerate(sentences2):
            similarity_score = check_similarity(sentence1, sentence2)
            similarity_matrix[j][i] = similarity_score

    for i in range(len(sentences2)):
        max_similarity_index = np.argmax(similarity_matrix[i])
        max_similarity_score = similarity_matrix[i][max_similarity_index]
        similarity_matrix[i] = 0
        similarity_matrix[i][max_similarity_index] = max_similarity_score
    return similarity_matrix

"""# **Extracting the Major attribute of each sentence**"""

def extract_keywords(sentence):
    doc = nlp(sentence)
    keywords = []
    for token in doc:
        if token.pos_ in ['NOUN', 'PROPN', 'ADJ']:
            keywords.append(token.text)
    return keywords

def determine_context(sentence1,sentence2):
  keywords1=extract_keywords(sentence1)
  keywords2=extract_keywords(sentence2)

  common_keywords=set(keywords1).intersection(keywords2)

  if common_keywords:
    keyword_counts = Counter(common_keywords)
    return max(keyword_counts, key=keyword_counts.get)
  else:
    return 0

"""# **Sentiment Analysis**"""

def get_sentiment_score(sentence):
    sentiment_score = sid.polarity_scores(sentence)
    return sentiment_score['compound']

def compare_sentences(sentence1, sentence2):
    sentiment_score1 = get_sentiment_score(sentence1)
    sentiment_score2 = get_sentiment_score(sentence2)

    if sentiment_score1 > sentiment_score2:
        return 1
    elif sentiment_score1 < sentiment_score2:
        return -1
    else:
        return 0

"""# **Comparing Numerical Values**"""

def extract_numerical_values(sentence):
    doc = nlp(sentence)
    numerical_values = []
    for token in doc:
        if token.pos_ == 'NUM':
            try:
                numerical_values.append(float(token.text))
            except ValueError:
                pass
    return max(numerical_values)

def compare_numerical_values(sentence1, sentence2):
    values1 = extract_numerical_values(sentence1)
    values2 = extract_numerical_values(sentence2)

    if not values1 or not values2:
        return "No numerical values found in one or both sentences"

    max_value1 = values1
    max_value2 = values2

    if max_value1 == max_value2:
        return "0"
    elif max_value1 > max_value2:
        return "1"
    else:
        return "-1"

s1="Apple Inc. is a multinational technology company headquartered in Cupertino, California.Ram is a 5 good boy.Ram got 30 marks in maths test."
s2="Tellicus Inc. is a national technology company headquartered in Delhi,India.Shyam is an average boy.Shyam got 32 marks in maths test."
t1=preProcess(s1)
a1=sum(containNumerical_data(t1))
print(a1)
t2=preProcess(s2)
a2=containNumerical_data(t2)
print(a2)
matrix=comparing_sentences(t1,t2)
for row in matrix:
        print(row)
sentences1=t1[0]
sentences2=t2[0]
for i in range(min(len(sentences1), len(sentences2))):
    sentence1 = sentences1[i]
    sentence2 = sentences2[i]
print(f"Common subject in sentences {i+1}: {determine_context(t1[0],t2[0])}")
print(compare_sentences(t1[1], t2[1]))

from types import prepare_class
def main(p1,p2):
  processedP1=preProcess(p1)
  processedP2=preProcess(p2)
  matrix2d=comparing_sentences(processedP1,processedP2)
  isNum1=containNumerical_data(processedP1)
  isNum2=containNumerical_data(processedP2)
  rows=np.count_nonzero(matrix2d)+2
  columns=4
  print("Sentence_Similarity_Matrix")
  print(matrix2d)
  finalMatrix=np.empty((rows,columns),dtype=np.dtype('U50'))
  finalMatrix[0][1]="Text1"
  finalMatrix[0][2]="Text2"
  finalMatrix[0][3]="Output"
  finalMatrix[rows-1][0]="Total"

  for i in range(0,rows-2):
    for j in range(0,findNumberOfSentences(p1)):
      if matrix2d[i][j]!=0:
        common_keyword=determine_context(processedP2[i],processedP1[j])
        finalMatrix[i+1][0]=common_keyword
        if isNum1[j]!=0 and isNum2[i]!=0:
          if get_sentiment_score(processedP1[j])>0 and get_sentiment_score(processedP2[i])>0:
            finalMatrix[i+1][1]=extract_numerical_values(processedP1[j])
            finalMatrix[i+1][2]=extract_numerical_values(processedP2[i])
            finalMatrix[i+1][3]=compare_numerical_values(processedP1[j],processedP2[i])
          elif get_sentiment_score(processedP1[j])>0 and get_sentiment_score(processedP2[i])<0:
            finalMatrix[i+1][1]=extract_numerical_values(processedP1[j])
            finalMatrix[i+1][2]=extract_numerical_values(processedP2[i])
            finalMatrix[i+1][3]="1"
          elif get_sentiment_score(processedP1[j])<0 and get_sentiment_score(processedP2[i])>0:
            finalMatrix[i+1][1]=extract_numerical_values(processedP1[j])
            finalMatrix[i+1][2]=extract_numerical_values(processedP2[i])
            finalMatrix[i+1][3]="-1"
          else:
            finalMatrix[i+1][1]=extract_numerical_values(processedP1[j])
            finalMatrix[i+1][2]=extract_numerical_values(processedP2[i])
            finalMatrix[i+1][3]=-1*int(compare_numerical_values(processedP1[j],processedP2[i]))
        else:
          finalMatrix[i+1][1]=get_sentiment_score(processedP1[j])
          finalMatrix[i+1][2]=get_sentiment_score(processedP2[i])
          finalMatrix[i+1][3]=compare_sentences(processedP1[j],processedP2[i])
  sum=0
  for i in range(1,rows-1):
    sum=sum+int(finalMatrix[i][columns-1])
  finalMatrix[rows-1][columns-1]=sum



  print("Final_Matrix:-")
  for row in finalMatrix:
    print("[", end="")
    for element in row:
        print(f"{element:10}", end=" ")
    print("]")

#Printing Final descision
  if finalMatrix[rows-1][columns-1]>"0":
      print("Entity in Text 1 is better than Entity in Text 2 ")
  elif finalMatrix[rows-1][columns-1]<"0":
      print("Entity in Text 2 is better than Entity in Text 1 ")
  else:
      print("Entity in Text 1 is equal to Entity in Text 2 ")



t1='''Modi increased the education budget by 20%. It resulted in the construction of 25 new schools.
 Modi also implemented a scholarship program for underprivileged students, which helped 10000 children attend school.
 Additionally, Modi's reforms in the education sector led to a 10% increase in the literacy rate.
 Modi decreased health facility by 15%.'''
t2='''Gandhi introduced a new Education budget with the increase of 10%.
Gandhi led many developments including the construction of 100 new schools.
These projects led to 100000 underprivelidged Children going to schools.
Gandhi's efforts in improving number of schools also resulted in a 20% decrease in Literacy rate.
Gandhi increased health facility by 10%.'''

main(t1,t2)

q1='''Raman is a good boy.Raman got 25 marks in Maths by using unfair means.
Raman always help his mother in her work.He smokes 2 cigrattes in a day which is bad for his health.'''
q2='''Pathak is a bad boy.He eat 2 apple daily for better health.
Pathak got 23 marks in Maths by his own hardwork.Pathak never helps his mother ,infact create trouble for her.'''
main(q1,q2)

w1='''Ram was king of Ayodhya.He always obeyed is father.He killed 10000 demons to save mankind.He respected women.
     Ram was the symbol of discipline.He got 14 years of vanvaas from his father.Ram was a devotee of lord Shiva'''
w2='''Ravan was king of Lanka.He never respect women.He  never obeyed his father.Ravan was the biggest devotee of Lord Shiva.
      He has 100000 demons in his army to destroy mankind.Ravan was the symbol of Arrogance.'''
main(w1,w2)