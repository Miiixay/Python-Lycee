while True:
  nb=input("Donnez moi un nombre impair : ")
  try:
    nb=int(nb)
    if nb<0:
      print("Un nombre positif !")
    if nb%2==1:
      break
    else:
      print("Impair !")
  except:
    print("Un entier !")

tableau=[["." for i in range(0,nb)] for j in range(nb)]

for i in range(nb):
  for j in range(nb):
    if i==j or i==(nb-1)-j or i==nb//2 or j==nb//2:
      tableau[i][j]='*'

for ligne in tableau:
  aff = ""
  for car in ligne:
    aff+=car+' '
  print(aff)
  print(aff)