"""
On souhaite ouvrir un fichier, et le chiffrer/déchiffrer à l’aide d’une clef de chiffrage. L’idée est, à l’instar du programme précédent, d’ajouter une quantité à chaque caractère. On choisira d’ajouter le code ASCII des lettres du mot "secret" dans cet ordre.

Ainsi, le premier caractère sera augmenté de 115, le second de 101, etc.

La procédure pour ouvrir un fichier en lecture et un en écriture est la suivante :
"""

# chiffrer le fichier

def chiffrer():
  with open("texteClair.txt", "r") as fichier: #ouvre "texteClair.txt" en lecture
    with open("texteChiffre.txt", "w") as fichierChiffre: #créé ou efface et recréé "texteChiffre.txt" et l'ouvre en écriture
      n=0
      for ligne in fichier: #on balaye les lignes les unes après les autres
        for car in ligne: #on parcourt tous les caractères
          fichierChiffre.write(chr(ord(car) + ord("secret"[n%6])))
          n+=1


# chiffrer()


# déchiffrer le fichier dans un autre fichier : "texteClair_bis.txt"

def dechiffrer():
  with open("texteChiffre.txt", "r") as fichier: #ouvre "texteClair.txt" en lecture
    with open("texteClair_bis.txt", "w") as fichierClair: #créé ou efface et recréé "texteChiffre.txt" et l'ouvre en écriture
      n=0
      for ligne in fichier: #on balaye les lignes les unes après les autres
        for car in ligne: #on parcourt tous les caractères
          fichierClair.write(chr(ord(car) - ord("secret"[n%6])))
          n+=1

dechiffrer()