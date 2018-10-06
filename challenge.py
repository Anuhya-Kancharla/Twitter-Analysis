import string 
import operator
import sys
from collections import defaultdict
from collections import Counter
from operator import itemgetter,attrgetter


file=input("enter file path")
f=open(file,'r',encoding="latin-1")


def maxtweets():
	usernames = []
	for line in f:
		usernames.append(line.split(None, 1)[0]) # add only first word
	#print( sorted(usernames, key=Counter(usernames).get, reverse=True))
	usernames=sorted(usernames, key=Counter(usernames).get, reverse=True)

	TEXT_FILE = open("./Maxtweets.txt", "w")
	TEXT_FILE.write("Top 10 users who have tweeted the max in entire timeline are:")
	x=0
	c=0
	while(c<10):
		TEXT_FILE.write('\n'+usernames[x])
		c+=1 
		x+=1
		while(usernames[x]==usernames[x-1]):
			x+=1

	TEXT_FILE.close()
maxtweets()
f.close()




f=open(file,'r',encoding="latin-1")

def maxfollowers():	
	sep=[]
	for line in f:
		sep.append(line.split("   "))

	sep=sorted(sep,key=itemgetter(4),reverse=False)
	
	TEXT_FILE = open("./MaxFollowers.txt", "w")
	TEXT_FILE.write("Top 10 users who have the max number of followers are:")
	for i in range (0,10):
		TEXT_FILE.write('\n'+sep[i][0])
	TEXT_FILE.close()
maxfollowers()
f.close()





f=open(file,'r',encoding="latin-1")
def maxretweets():
	temp=[]
	for line in f:
		temp.append(line.split("   "))
		
	
	TEXT_FILE = open("./MaxRetweets.txt", "w", encoding="utf-8")
	TEXT_FILE.write("Top 10 tweets which have the max retweet count are:")
	for i in range (0,10):
		TEXT_FILE.write('\n'+temp[i][2])
	TEXT_FILE.close()
	
maxretweets()
f.close()
