import tweepy
from random import randint
Friends = "follow.txt"
Added = "added.txt"

def twitter_api():
	ckey = 'qnuK8Jmf0ofzN9QGCWoCN5qff'
	csecret = 'y49eh5mvu731AmrFobBItYFofnVUn1VQUTVnjz856w5AxIhT3v'
	atoken = '886441868069875712-ZgWx0wS57xvapyJ5FxZkf79CRUxL8up'
	asecret = '8vJ8Si7Ocoj1GnvpQ0CZ0G1lifKB2rei39GCujUtiKmqN'
	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(atoken, asecret)
	api = tweepy.API(auth)
	return api

def get_following():
	prev = []
	with open(Friends) as f:
		for line in f:
			prev.append(line.rstrip('\n'))
	f.close()
	return prev

def get_added():
	prev = []
	with open(Added) as f:
		for line in f:
			prev.append(line.rstrip('\n'))
	f.close()
	return prev

def update_following(person1, people1):
	people1.append(person1)
	if(len(people1)>500):
		people1.pop(0)
	f = open(Friends, 'w')
	for follower1 in people1:
		f.write("%s\n" % follower1)
	f.close()
	return 0

def update_added(person2, people2):
	people2.append(person2)
	f = open(Added, 'w')
	for follower2 in people2:
		f.write("%s\n" % follower2)
	f.close()
	return 0

def get_followers(name):
	ids = api.followers_ids(name)
	return ids


api = twitter_api()
following = get_following()
added = get_added()
followers = get_followers("TrumpBotDonny")
sizeOne = len(followers)

guyOne = followers[randint(0,sizeOne)]
followersTwo = get_followers(guyOne)
sizeTwo = len(followersTwo)
new = False
num = 0
while (new == False):
	guyTwo = followersTwo[num]
	if guyTwo not in added:
		api.create_friendship(guyTwo)
		update_added(guyTwo, following)
		update_following(guyTwo, added)
		new = True
	num - num + 1
	if(num > sizeTwo):
		new = True

#print(followers)

#for tweet in api.search(q = '#meme',count =1):
#	print(tweet.user.id)
#print(followers)
print(following)