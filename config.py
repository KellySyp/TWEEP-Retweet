#https://realpython.com/twitter-bot-python-tweepy/
import tweepy

def buildKey():
	consumer_key = "[INSERT KEY]"
	consumer_secret = "[INSERT SECRET KEY]"
	access_token = "[INSERT TOKEN]"
	access_token_secret = "[INSERTSECRETTOKEN]"

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
		
	return auth