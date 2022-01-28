liste = []
nb_valeurs = int(input("Donnez le nombre de valeurs que vous voulez entrer "))
n = 0
while n != nb_valeurs :
  valeurs = int(input("Donnez ces valeurs " )) 
  liste.append (valeurs)
  n=n+1


def maxi():
  m = liste[0]
  for i in range (len(liste)):
    if m < liste[i]:
      m = liste[i]
  return m

def mini():
  p = liste[0]
  for i in range (len(liste)):
    if p > liste[i]:
      p = liste[i]
  return p

def moyenne():
  moy = 0
  for i in range(len(liste)):
    moy = moy + liste[i]
  return moy/n

print("La moyenne est",moyenne())
print("Le minimum est ",mini())
print("Le maximum est ",maxi())