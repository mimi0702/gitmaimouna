import random
	
x = random.randint(0, 9)
chiffre_secret = random.randint(0, 9)
print(chiffre_secret)
reponse  = None
while True:
	reponse =int(input("entrer une valeur entre 0 et 9"))
	if reponse == chiffre_secret:
		print("vous avez gagné")	
	if reponse > chiffre_secret:
		print("le chiffre secret est plus petit que la reponse.")
	elif reponse < chiffre_secret:
		print("le chiffre secret est plus grand que la reponse.")
	break

