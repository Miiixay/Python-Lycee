import random

def chercheMin(t):#Oui, il est aussi possible d'appeler la fonction min()
  minimum=t[0]
  indice=0
  for k,valeur in enumerate(t):
    if valeur<minimum:
      minimum=valeur
      indice=k
  return indice

def triNaif(t): # algorithme de tri récursif sur une liste
  print(t)
  minimum = chercheMin(t)
  print("min : ",t[chercheMin(t)])
  if len(t) == 1: # si la liste contient un seul élément
    return [t[0]]
  else: # sinon
    return [t[minimum]] + triNaif(t[:minimum] + t[minimum+1:])
table=[random.randint(1,100) for i in range(10)]

tableTriee = triNaif(table)

print("\n fin : ",tableTriee)