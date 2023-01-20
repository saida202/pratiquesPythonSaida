#Type de donnees===quand on met# ca devient un commentaire
import sys
v1=10
print(type(v1))

#pour voir la taille que occupe l'entier v1 on import le module sys en haut
print(sys.getsizeof(v1))
v2=25.5
print(type(v2))
print(sys.getsizeof(v2))

v3=25+5j
print(type(v3))
print(sys.getsizeof(v3))

v4=True

print(type(v4))
print(sys.getsizeof(v4))
v5=False

print(type(v5))
print(sys.getsizeof(v5))


