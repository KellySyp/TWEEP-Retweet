import tweepy
from config import buildKey
from log import writeLog

api = tweepy.API(buildKey())
user = api.me()

def retweet(str, num = 5):
	for tweet in tweepy.Cursor(api.search, str).items(num):
		try:
			if tweet.user.screen_name != user.screen_name:
				tweet.favorite()
				tweet.retweet()
				writeLog('Retweeted tweet by: ' + tweet.user.screen_name)
		except tweepy.TweepError as e:
			writeLog(e.reason)
		except StopInteration:
				break
				
retweet("#GameDev", 5)