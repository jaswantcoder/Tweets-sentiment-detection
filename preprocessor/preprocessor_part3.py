
import re
import sys
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
import nltk
nltk.download('stopwords')

def preprocess(tweet):
  obj = TwitterPreprocessor(tweet)
  obj.fully_preprocess()
  return obj.text

new_df=traindf.copy()
new_df['text'] = new_df['text'].apply(preprocess)

new_df.head()

my_label = ['0','1']
plt.figure(figsize=(10,4))
traindf.label.value_counts().plot(kind='bar');


from sklearn.feature_extraction.text import CountVectorizer


cv = CountVectorizer(stop_words = 'english')
words = cv.fit_transform(new_df.text)

sum_words = words.sum(axis=0)

words_freq = [(word, sum_words[0, i]) for word, i in cv.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)

frequency = pd.DataFrame(words_freq, columns=['word', 'freq'])

frequency.head(30).plot(x='word', y='freq', kind='bar', figsize=(15, 7), color = 'blue')
plt.title("Most Frequently Occuring Words - Top 30")
