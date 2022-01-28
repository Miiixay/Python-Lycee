import random # pour utiliser randint
n=random.randint (1,100) # n prend une valeur pseudo-aléatoire
m=0
print("Essayez de trouver le nombre n entre 1 et 100!")
essai=int(input("Nombre d'essais: "))
for i in range(essai-1):
  while m!=n:
    if essai<=0:
      print("Vous avez perdu")
      break
    print("il vous reste",essai,"essai(s)")
    m=int(input("Votre essai ? "))
    if m<n :
     print("C'est plus !")
    elif m>n :
      print("C'est moins ! ")
    elif m==n :
     print("Vous avez gagné!")
    essai=essai-1




#1) On entre forcément dans la boucle car n est un nombre pseudo aléatoire entre 1 et 100 et m est forcement égale a 0
