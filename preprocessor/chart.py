
from sklearn.feature_extraction.text import CountVectorizer

freqdf = new_df.copy()
freqdf = freqdf.loc[freqdf['label']==1]

cv = CountVectorizer(stop_words = 'english')
words = cv.fit_transform(freqdf.text)

sum_words = words.sum(axis=0)

words_freq = [(word, sum_words[0, i]) for word, i in cv.vocabulary_.items()]
words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)

frequency = pd.DataFrame(words_freq, columns=['word', 'freq'])

frequency.head(30).plot(x='word', y='freq', kind='bar', figsize=(15, 7), color = 'blue')
plt.title("Most Frequently Occuring Words - Top 30")
