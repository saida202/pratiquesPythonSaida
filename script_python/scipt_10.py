str1="salut tout le monde"
#si je veux acceder a la lettre u

print(str1[3])

#pour recuperer la 1ere lettre
print(str1[0])

#pour recuperer la dernier lettre
print(str1[-1])

#pour recuperer la lettre avant la dernier
print(str1[-2])

#pour avoit la taille de toutes la chaine de caracteres qu on a ecrit
print(len(str1))

print(str1[len(str1)-1])
#la ligne 10 et 18 c est la meme chose on general la ligne 18 on lutilise dans des boucles
#quand on connait pas le nombre d element dans la chaine de caracteres

#on va faire mnt le salycine c est le decoupage de chaines de caracteres
#Decoupage de chaine de caracteres

print(str1[0:5])

#il fo toujours commencer par 0 et c est le mot se termine a 4 par ex on met 5

#par ex si on ve recuperer le mot tout
print(str1[6:10])

#pour avoir tout la phrase
print(str1[0:])
#pour avoir juste tout le monde
print(str1[6:])

str2="sabacada"
#pour recuperer juste les a on met deux fois ::(ca ve dire des saut des pas on saute de deux pas
#pour afficher ce qio vien apres on met le 1er caractere on saut de deux pas et affiche ce qui vien apres pour toutes la cjhaine de caractere
print(str2[1::2])
print(str1[1::2])
#la il va sauter de 3 pas
print(str2[1::3])
#la il va sauter de 4 pas
print(str2[1::4])
#si on ve recupere les 6 premier caracteres
print(str1[:7])
#pour commencer de la fin on l'inversant
print(str1[::-1])
#pour afficher juste le dernier mot monde
print(str1[-5:])

#pour afficher deux chaines de caracteres avec un espace entre les deux
str3="saida"
str4="abraz"
str5=str3+" "+str4
print(str5)
print(str3+" "+str4)
print(str3,str4)

#pour concatiner une chaine de caractere
str2=str2+str2
print(str2)

#parcourire une chaine de cafractere avec une boucle for
str2="sabacada"
for i in str2:
    print(i)
#pour afficher chaque caractere avec le numero qu il a dans la chaines de caracteres
for i in enumerate(str2):
    print(i)















