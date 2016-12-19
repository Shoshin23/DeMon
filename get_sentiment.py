## Use Indico.io to get sentiment for tweets. Save them to a file. 

import indicoio as indico
import pandas as pd 
import numpy as np
from tqdm import tqdm

## configure indicioio API.

indico.config.api_key = '2bb985d054973c662d29e4b9686eb711'

write_f = open('tweets_sentiment.csv', 'w')
write_f.write('text,sentiment')
write_f.close


# Get all unique texts from the tweets_english.csv dataset. 

tweets = pd.read_csv('tweets_english.csv',engine='python')

# tweet_list_str = list(map(str,tweets['text'].unique().tolist()))
# tweet_list = tweet_list_str
# sentiment_list = indico.sentiment_hq(tweet_list)
# print("Done with the sentiment_hq work.")

# #tweet_dict = {}

# write_f = open('tweets_sentiment.csv', 'a')


# for idx, tweet in enumerate(tweet_list):
# 		write_f.write('\n"%s","%f"' % (tweet,sentiment_list[idx]))

# write_f.close

tweet_list_str = list(map(str,tweets['text'].unique().tolist()))
chunks = np.array_split(np.array(tweet_list_str), 100)
print(len(chunks))

#[tweet_list_str[x:x+100] for x in range(0, len(tweet_list_str), 100)]
write_f = open('tweets_sentiment.csv', 'a')

for tweets in tqdm(chunks):
	tweets = tweets.tolist()
	#print(type(tweets))
	sentiment = indico.sentiment_hq(tweets)
	#np.random.uniform(low=0.5, high=13.3, size=(len(tweets),))
	for idx,tweet in enumerate(tweets):
		tweet = tweet.strip("\"")
		write_f.write('\n"%s","%f"' % (tweet,sentiment[idx]))


write_f.close


# write_f = open('tweets_sentiment.csv', 'a')


# for tweet in tqdm(tweet_list_str):
# 	write_f.write('\n"%s","%f"' % (tweet,indico.sentiment_hq(tweet)))
# write_f.close

