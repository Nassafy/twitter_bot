from random import shuffle


def melanger(fichier_texte):
    with open(fichier_texte, 'r') as f:
        texte = f.read()
    list_texte = texte.split('        ')
    shuffle(list_texte)
    with open(fichier_texte, 'w') as f:
        for line in list_texte:
            f.write(line)


melanger('cnfact.txt')
