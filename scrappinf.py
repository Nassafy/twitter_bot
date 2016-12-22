from lxml import html
import requests
from random import shuffle


def melanger(fichier_texte):
    with open(fichier_texte, 'r') as f:
        texte = f.read()
    list_texte = texte.split('        ')
    shuffle(list_texte)
    with open(fichier_texte, 'w') as f:
        for line in list_texte:
            f.write(line)


chucknorrisfacts = ''
fichier = open('cnfact.txt', 'w')
fichier.close()
for i in range(100):
    page = requests.get('https://www.chucknorrisfacts.fr/facts/top?p='+str(i+1))
    tree = html.fromstring(page.content)
    chucknorrisfacts = tree.xpath("//div[contains(@class, 'factbody')]/text()")
    print(i)
    fichier = open('cnfact.txt', 'r')  # lecture du fichier
    save = fichier.read()
    fichier.close()
    fichier = open('cnfact.txt', 'w')
    fichier.write(save)
    for fact in chucknorrisfacts:
        if fact != '':
            fichier.write(fact)
    fichier.close()
