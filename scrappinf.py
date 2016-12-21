from lxml import html
import requests


page = requests.get('https://www.chucknorrisfacts.fr/facts')
tree = html.fromstring(page.content)
chucknorrisfacts = tree.xpath("//div[contains(@class, 'factbody')]/text()")

fichier=open('cnfact.txt','w')
for fact in chucknorrisfacts:
    fichier.write(fact)
fichier.close()

