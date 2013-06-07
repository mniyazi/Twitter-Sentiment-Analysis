import json
import string
import sys

#Function to create a dictiory of words from the sample score file.
#term will be the key and score will be the value
def create_dict(sent_file):
	afinnfile=open(sent_file)
	scores={}
	for line in afinnfile:
		term, score=line.split("\t") #Tab-delimited file
		scores[term]=int(score)
	return scores

def calc_sentiment(sent_file, tweet_f):
	scores=create_dict(sent_file)
	tweet_file=open(tweet_f)
	tweet_file_content=tweet_file.read().splitlines()
	for line in tweet_file_content:
		content=json.loads(line)
		sentiment=0;
		try:
			tweet_raw=content['text']
			tweet=''.join([x for x in tweet_raw if x in string.ascii_letters+'\'- '])
			tweet_words=tweet.split()
			for word in tweet_words:
				try:
					sentiment=sentiment+scores[word]
				except:
					continue;
			print float(sentiment)
		except:
			print float(sentiment)

sent_file=sys.argv[1]
tweet_file=sys.argv[2]
calc_sentiment(sent_file, tweet_file)	
