import tweepy
from time import sleep
from secret import *


# authentificaton twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_secret)
api = tweepy.API(auth)
for user in tweepy.Cursor(api.followers).items():
    if api.lookup_friendships(user.screen_name, str(api.user_timeline()[0].id)):
        print('Vrai')
        api.create_friendship(user.screen_name)

message = api.direct_messages(count=1)[0].text
fichier = open('cnfact.txt', 'r')

for line in fichier:
    nom = message.replace("Name=", "")
    if len(line) > 10:
        new_line = line.replace('Chuck Norris', nom)
        print(new_line)
        api.update_status(new_line)
        sleep(900)
fichier.close()
