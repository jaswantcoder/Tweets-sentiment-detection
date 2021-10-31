# import pandas as pd 
import matplotlib.pyplot as plt
# libraries for dataset preparation, feature engineering, model training 
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer
from sklearn import decomposition, ensemble
from textblob import TextBlob as tb
import pandas, xgboost, numpy, string
from keras.preprocessing import text, sequence
from keras import layers, models, optimizers
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
from sklearn.metrics import auc
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
#nltk.download('punkt')
from html.parser import HTMLParser
import re
import sys
import nltk
import numpy as np
# import pandas lib as pd 
import pandas as pd 
import re
from html.parser import HTMLParser
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# append first file of depression related tweets
#creating dataframe

search_words = ["glad","joy","new","welcome","congrats","depressed","sad","alone","stressed","upset"];

nondep = {"glad","joy","new","welcome","congrats"}
dep = {"depressed","sad","alone","stressed","upset"}


date = ["_18","_19","_20","_21","_22"]
suff = "0421"

traindf = pd.DataFrame(columns = ['id', 'text', 'keyword','label'])

for key in search_words:
  strr = key
  for dt in date:
    path = "/content/drive/MyDrive/finalyearproject/tweets/"+strr+dt+suff+".csv"
    df = pd.read_csv(path)
    tempdf =pd.DataFrame()
    tempdf['id'] = df.iloc[:,1]
    #tempdf['user'] = df.iloc[:,2]
    tempdf['text'] = df.iloc[:,0]
    tempdf['keyword'] = pd.Series([key for x in range(len(df.index))])
 
    if(key in dep):
      label = 1
    else:
        label =0

    tempdf['label'] = pd.Series([label for x in range(len(df.index))])

    traindf = traindf.append(tempdf, ignore_index=True)




    traindf.count()
