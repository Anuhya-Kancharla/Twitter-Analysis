import tweepy
import time

ACCESS_TOKEN = '805985548854820864-nNzelcVTIEfAEls2XSgH8Ts9qIH2j0S'
ACCESS_SECRET = 'XNpdbKAR8vopkczFHm7qOI6xe3UAiYycwvkBx8dUULYM3'
CONSUMER_KEY = 'ybcV2RWX0wsoCDzC3FjabEqyA'
CONSUMER_SECRET = 'B1AzgD75Q8ucMYxsU8lHbGVpCfkUEEBoKfOVbzsDxW1W9TZU8q'
SEARCH=input("Enter the search string ")
FROM=input("Enter the from date (YYYY-MM-DD format) ")
TO=input("Enter the to data (YYYY-MM-DD format) ")
INPUT_FILE_PATH= './'+SEARCH+'.txt'

num=int(input("Enter the number of tweets you want to retrieve for the search string "))
auth = tweepy.auth.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)
i=0;

f = open(INPUT_FILE_PATH, 'w', encoding='utf-8')

for res in tweepy.Cursor(api.search, q=SEARCH, rpp=100, count=20, result_type="recent", since = FROM,until =TO, include_entities=True, lang="en").items(num):
	i+=1
	f.write(res.user.screen_name)
	f.write('   ')
	f.write('[')
	f.write(res.created_at.strftime("%d/%b/%Y:%H:%M:%S %Z"))
	f.write(']')	
	f.write("   ")
	f.write('"')
	f.write(res.text.replace('\n',''))
	f.write('"')
	f.write("   ")
	f.write(str(res.user.followers_count))
	f.write("   ")
	f.write(str(res.retweet_count))
	f.write('\n')
f.close
print("Tweets retrieved ",i)