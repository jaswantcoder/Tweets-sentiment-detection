import tweepy
import csv
import time
## all my twitter API credentials are in this file, this should be in the same directory as is this script
#consumer_key = "qq3XbjipYWGX1gsqSlwbvkD12"
#consumer_secret = "RMJroEqHceSlPdyoNzcnqeYJ8j2jMQ3yAY9lLCZoGDvq3sR2By"
#access_token = "1312452774949384192-4yhCk1xMzNV3HtWKTNPn9RwEl8VLjo"
#access_secret = "5VAZrVFUOHkCoXKnGvRvFoyTDjyAS60dwLr1yAue1FTYS"

consumer_key = "F0l0nk3VT9rcB0PHEzBPvy5Zd"
consumer_secret = "nyTiwN1XI3higrJRYLnPiefXC1IG28htLDgmSdtOt0IxYvQqCL"
access_token = "1312452774949384192-V7DKY1IjYvuy5hVR6L7PsT8IpzhOvN"
access_secret = "Yq7V5Iy0xBrhgh9fCPBTN5FOvsiBCd9j1rml9GYZMFhuf"

## set API connection
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
    
api = tweepy.API(auth, wait_on_rate_limit=True)    # set wait_on_rate_limit =True; as twitter may block you from querying if it finds you exceeding some limits

