# Enhance the existing data. 
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup ##Prefer using this to the goddamn api or Tweepy.
import requests
from tqdm import tqdm #Make a neat progressbar.
import tweepy

tweets_df = pd.read_csv("tweets.csv")
consumer_key = "oMaEJOpyKtzo5h8mpPJHrBltF"
consumer_secret = "SSqRgUgkj3ottsHx5UNGE6IyFWe44kzMVfKvDPuFaU4Dfrp7Cy"
access_key= "1154080303-5zsguuV7EVixqMfPTuDwIZfQRTTQ5SDP6rYSmN1"
access_secret= "J0NryP5VvCjuB4DvxPXIPx16VyY2ti6Eqqz3xJ3TJH8A3"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api=tweepy.API(auth)

##CSV file. 
write_f = open('follower_count.csv', 'w')
write_f.write('handle,followers_count,location')
write_f.close

users = tweets_df[' user name'].unique().tolist()


# location_dict = {}
# follower_dict = {}

write_f = open('follower_count.csv', 'a')

    
for user in tqdm(users):
	try:
		usr = api.get_user(user)
		write_f.write(('\n"%s","%d","%s"' % (usr.screen_name, usr.followers_count,usr.location)))
	except Exception as e:
		pass

write_f.close()

