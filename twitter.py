from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "775795818586484736-LkcA44T2QkOgbSOfxBYgcwUnHTv5Bra"
access_token_secret = "sgctVnFxaHl6x4mBek2BkeFyknfAhRSi4u8jYWqO5bJOZ"
consumer_key = "pqQubwme26Rh73vvRQ5ptuXm7"
consumer_secret = "HcZdBbGm0X1hu9yH1XnBMVnaINArQAQYavXRlD2pCTzdqvUpuc"

class StdOutListener(StreamListener):
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status


if __name__ == '__main__':
	l = StdOutListener()
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)
	stream.filter(track=['ow', 'overwatch', 'ufc', 'nba', 'nfl', 'nhl', 'lol', 'dota', 'csgo', 'mlb', 'basketball'])
