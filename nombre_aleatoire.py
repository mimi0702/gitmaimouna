
import random

x = random.randint(0, 9)
chiffre_secret = random.randint(0, 9)
reponse  = None
while reponse != chiffre_secret:
	reponse =int(input("entrer une valeur entre 0 et 9"))
	if reponse > chiffre_secret:
		print("le chiffre secret est plus petit que ca:")
	elif reponse < chiffre_secret:
		print("le chiffre secret est plus grand que ca":)
	else:
		print("vous avez gagne")
