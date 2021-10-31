# Libraries
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create a list of word
#wordcloud2 = WordCloud().generate(' '.join(text2['Crime Type']))

# Create the wordcloud object
wordcloud = WordCloud(width=1000, height=1000, margin=0).generate(' '.join( rev for rev in new_df.text))

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
