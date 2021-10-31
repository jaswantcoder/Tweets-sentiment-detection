# Install Libraries
!pip install textblob
!pip install tweepy

# Import Libraries
from textblob import TextBlob
import sys
import tweepy
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import nltk

!pip install pycountry
import pycountry

!pip install langdetect
import langdetect

import re
import string
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from langdetect import detect
from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer

# copy the dataframe with selected columns
selected_columns = new_df[["text","keyword","label"]]
tw_list = selected_columns.copy()
tw_list.head()

#Calculating Negative, Positive, Neutral and Compound values
tw_list[['polarity', 'subjectivity']] = tw_list['text'].apply(lambda Text: pd.Series(TextBlob(Text).sentiment))
for index, row in tw_list['text'].iteritems():
 score = SentimentIntensityAnalyzer().polarity_scores(row)
 neg = score['neg']
 neu = score['neu']
 pos = score['pos']
 comp = score['compound']
 if neg > pos:
  tw_list.loc[index, 'sentiment'] = "negative"
 elif pos > neg:
  tw_list.loc[index, 'sentiment'] = "positive"
 else:
  tw_list.loc[index, 'sentiment'] = "neutral"
 tw_list.loc[index, 'neg'] = neg
 tw_list.loc[index, 'neu'] = neu
 tw_list.loc[index, 'pos'] = pos
 tw_list.loc[index, 'compound'] = comp
  
  #Creating new data frames for all sentiments (positive, negative and neutral)
tw_list_negative = tw_list[tw_list["sentiment"]=="negative"]
tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

def count_values_in_column(data,feature):
 total=data.loc[:,feature].value_counts(dropna=False)
 percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
 return pd.concat([total,percentage],axis=1,keys=['Total','Percentage'])
#Count_values for sentiment
count_values_in_column(tw_list,"sentiment")

tw_list.head()

#Creating new data frames for all sentiments (positive, negative and neutral)
tw_list_nondep_neg = tw_list[tw_list["sentiment"]=="negative"]
tw_list_nondep_neg = tw_list_nondep_neg[tw_list_nondep_neg["label"]==0]
tw_list_nondep_pos = tw_list[((tw_list["sentiment"]=="positive") ) & (tw_list["label"]==0)]
tw_list_nondep_neu = tw_list[(tw_list["sentiment"]=="neutral") & (tw_list["label"]==0)]
tw_list_dep_neg = tw_list[(tw_list["sentiment"]=="negative") & (tw_list["label"]==1)]
tw_list_dep_pos = tw_list[(tw_list["sentiment"]=="negative") & (tw_list["label"]==1)]
tw_list_dep_neu = tw_list[(tw_list["sentiment"]=="negative") & (tw_list["label"]==1)]


tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

tw_list.head()
