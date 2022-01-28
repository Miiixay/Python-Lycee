import random
n=10
liste=[random.randint(1,100) for i in range(n)]
for i in range(n):
  for j in range(n):
    if liste[i]<liste[j]:
      liste[j],liste[i]=liste[i],liste[j]
print(liste)