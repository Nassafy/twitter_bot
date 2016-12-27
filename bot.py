import tweepy
from time import sleep
from secret import *


# Création d'un stream listener pour les message privées
class MyStreamListener(tweepy.StreamListener):
    def on_direct_message(self, status):
        global i
        print(i)
        message = api.direct_messages(count=1)[0].text
        print(message)
        if 'Nom=' in message:
            nom = message.replace("Nom=", "")
            print(nom)
            with open('cnfact.txt', 'r') as f:
                print("fichier ouvert!")
                nb_ligne = 0
                for line in f:
                    nb_ligne += 1
                    if nb_ligne >= i + 2:
                        if len(line) > 1:
                            print(i)
                            i = nb_ligne
                            new_line = line.replace('Chuck Norris', nom)
                            print(new_line)
                            break
            api.update_status(new_line)

# authentificaton twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, acces_secret)
api = tweepy.API(auth)

# Initialiation du stream listener
StreamMessage = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=StreamMessage)

# Activation du listener
myStream.userstream(async=True)

# On follow les followers
for user in tweepy.Cursor(api.followers).items():
    if api.lookup_friendships(user.screen_name, str(api.user_timeline()[0].id)):
        api.create_friendship(user.screen_name)


# Lecture du fichier contenant les CN facts
fichier = open('cnfact.txt', 'r')

nb_ligne = 0
for line in fichier:
    nb_ligne += 1
    try:
        with open('data.txt', 'r') as f:
            i = int(f.read())
            if i > 6137:
                i = 0
# Si le fichier contenant le nombre de fact publié n'existe pas, on le crée
    except IOError:
        f = open('data.txt', 'w')
        f.close()
        i = 0

# On parcour le fichier contenant les CN facts jusqu'a arrivée après le
# dernier publié.
    if nb_ligne == i + 1:
        i = nb_ligne
        message = api.direct_messages(count=1)[0].text
        if len(line) > 1:  # Si la ligne n'es pas vide
            # Si le dernier message envoyé contient 'nom=', on change le nom
            try:
                if 'Nom=' in message:
                    nom = message.replace("Nom=", "")
                new_line = line.replace('Chuck Norris', nom)
            except NameError:
                new_line = line
                print('NameError occured')
            print(new_line)
            # On publie le tweet
            try:
                api.update_status(new_line)
                sleep(900)  # Attente de 15mn

            except tweepy.error.TweepError as e:
                print(e)
    with open('data.txt', 'w') as f:
        f.write(str(i))

fichier.close()
