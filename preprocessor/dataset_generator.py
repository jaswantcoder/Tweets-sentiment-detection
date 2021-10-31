# create final dataset
#final dataframe
finaldf = pd.DataFrame(columns = ['text','keyword', 'label','sentiment','polarity'])

#only required columns
selected_columns = tw_list_nondep_pos[["text","keyword","label","sentiment","polarity"]]

temp = selected_columns.copy()
finaldf = finaldf.append(temp, ignore_index=True)

selected_columns = tw_list_dep_neg[["text","keyword","label","sentiment","polarity"]]

temp = selected_columns.copy()
finaldf = finaldf.append(temp, ignore_index=True)




finaldf.head()

finaldf.loc[:,"polarity"].value_counts(dropna=False)
finaldf.count()

import nltk
nltk.download('vader_lexicon')

tweet_list.drop_duplicates(inplace = True)
tweet_list
