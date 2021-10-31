tw_list_positive = tw_list[tw_list["sentiment"]=="positive"]
tw_list_negative = tw_list[tw_list["sentiment"]=="negative"]
tw_list_neutral = tw_list[tw_list["sentiment"]=="neutral"]

def count_label_sentiment(tot,posdata,negdata,neudata):
 total = tot.loc[:,"label"].value_counts(dropna=False)
 positive = posdata.loc[:,"label"].value_counts(dropna=False)
 negative = negdata.loc[:,"label"].value_counts(dropna=False)
 neutral = neudata.loc[:,"label"].value_counts(dropna=False)
 #positive = 
 #percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
 return pd.concat([total,positive,negative,neutral],axis=1,keys=['tot','positive','negative','neutral'])
#Count_values for sentiment
count_label_sentiment(tw_list,tw_list_positive,tw_list_negative,tw_list_neutral)

def count_polarity_sentiment(tot,posdata,negdata,neudata):
 total = tot.loc[:,"polarity"].value_counts(dropna=False)
 positive = posdata.loc[:,"polarity"].value_counts(dropna=False)
 negative = negdata.loc[:,"polarity"].value_counts(dropna=False)
 neutral = neudata.loc[:,"polarity"].value_counts(dropna=False)
 #positive = 
 #percentage=round(data.loc[:,feature].value_counts(dropna=False,normalize=True)*100,2)
 return pd.concat([total,positive,negative,neutral],axis=1,keys=['total','positive','negative','neutral'])
#Count_values for sentiment
print(count_polarity_sentiment(tw_list,tw_list_positive,tw_list_negative,tw_list_neutral))

print("\nToal number of tweets : ",tw_list["id"].count())
