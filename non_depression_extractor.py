
date_since = "2020-11-01"

## the geocode is for India; format for geocode="lattitude,longitude,radius"
## radius should be in miles or km


tweetcount=0;



search_words = ["glad","joy","new","welcome","congrats"];


for word in search_words:
    strr = "/content/drive/MyDrive/finalyearproject/tweets/"+word+"_250421.csv"
    csvFile = open(strr, 'w',  newline='', encoding='utf-8')
    csvWriter = csv.writer(csvFile)
    cnt=5000
    '''
    if word == "glad" or word=="depressed":
      cnt=8000
    elif word == "joy" or word=="sad":
      cnt=6000
    elif word == "new" or word=="alone":
      cnt=6000
    elif word == "welcome" or word=="stressed":
      cnt=5000
    elif word == "congrats" or word=="upset":
      cnt=4000
      '''

    for tweet in tweepy.Cursor(api.search, q=word,since="2021-02-20", lang="en").items(cnt): 
       # s = '2021-04-05 23:10:27'
        #dtime1 = '2021-04-05 23:50:27'
       # new_datetime1 = datetime.strptime(dtime,'%Y-%m-%d %H:%M:%S')
        #dtime2 = '2021-04-09 23:10:27'
        #new_datetime2 = datetime.strptime(dtime,'%Y-%m-%d %H:%M:%S')
        #if((tweet.created_at>new_datetime1)):
        time.sleep(0.00001)
        csvWriter.writerow([tweet.text.encode('utf-8'), tweet.id, tweet.created_at, tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
