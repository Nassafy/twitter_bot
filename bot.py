import tweepy
import sys
from time import sleep
from secret import *


# authentificaton twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_secret)
api = tweepy.API(auth)
for user in tweepy.Cursor(api.followers).items():
    if api.lookup_friendships(user.screen_name, str(api.user_timeline()[0].id)):
        api.create_friendship(user.screen_name)


fichier = open('cnfact.txt', 'r')

for line in fichier:
    message = api.direct_messages(count=1)[0].text
    if len(line) > 1:
        try:
            if 'Nom=' in message:
                nom = message.replace("Nom=", "")
            new_line = line.replace('Chuck Norris', nom)
        except NameError:
            new_line = line
            print('NameError occured')
        print(new_line)
        try:
            api.update_status(new_line)
            sleep(900)
        except tweepy.error.TweepError as e:
            print(e)
fichier.close()
