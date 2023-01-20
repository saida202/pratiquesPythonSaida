#pour les fonctions
#dans python il ya duex types de fonctiones
#il y a des fonctions pilt in cad native a python et des
# fonctions que nous allons developper nous meme et puis chaq type
# a ses fonctions par ex une chaine de caracteres a ses propres fonctions liee

ch="  Salut tout le monde  "
#parfois les espaces son considere comme des chaines de caracteres avec  python offre la possibilite de les enlever
#si il sont ajouter par erreur

print(len(ch))
ch1=ch.strip()
print(ch1)
print(len(ch1))
#avec la fonction strip() on a la possibilite d enlever les espaces et de compter juste les caractere avec la fonction len()

#pour supprimer uniquement l espace a gauche
ch2=ch.lstrip()
print(ch2)
print(len(ch2))
#pour supprimer uniquement l espace a droite
ch3=ch.rstrip()
print(ch3)
print(len(ch3))

#pour remplacer qlq chose par espace (par ex remplacer des *** avec des espaces)
ch4="***salut***tout***le***monde***"
print(ch4)
ch5=ch4.strip("*")
print(ch5)
print(len(ch5))

#pour enlever les *** a gauche lstrip
ch6="***salut***tout***le***monde***"
print(ch6)
ch7=ch6.lstrip("*")
print(ch7)
print(len(ch7))

#pour enlever les *** a droite rstrip
ch6="***salut***tout***le***monde***"
print(ch6)
ch7=ch6.rstrip("*")
print(ch7)
print(len(ch7))

#pour remplacer les * par rien
print(ch6.replace("*",""))

#pour remplacer les * par espace
print(ch6.replace("*"," "))

#pour afficher la chaine de caractere en miniscule on met lower et pour l afficher en majiscule on met upper
ch8="SALUT TOUT LE MONDE"
print(ch8.lower())
print(ch8.upper())
#pour compter le mot monde dans cet phrase on met .count("le mot desirer")
ch9="salut tout le monde le monde le monde"
print(ch9.count("monde"))
#pour verifer si la chaine de caractere commence par salut on met .startswith("le mot desire") cava donner un resultat
#en booleen soit True or False
print(ch9.startswith("salut"))
#pour verifer si la chaine de caractere se termine par salut on met .endswith("le mot desire") cava donner un resultat
#en booleen soit True or False
print(ch9.endswith("salut"))

#pour afficher les chiffre en une liste on le fait avec la fonction split()
ch10="un-deux-trois-quatre-cinq-six-sept-huit-neuf-dix"
print(ch10.split("-"))

#pour verifier le sgtatus de notre projet on le fait avec la commande dans le terminal avec la commande git status
#si il reconnu pas la commande git status on fait la commande git init pour le initialiser
#et on refait git status
#