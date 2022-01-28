nb = int(input("Donnez moi un nombre: "))
entiers = [2]
liste = []

for i in range(3, nb + 1):
    premier = True
    for j in entiers:
        if i % j == 0:
            premier = False
        if i % j != 0:
            premier = True

if nb == 1 or nb == 2:
    print("Votre nombre est premier")

if nb > 2:
    if premier == True:
        print("Votre nombre est premier")
    else:
        print("Votre nombre n'est pas premier")
    liste = []
premiers = [2]

for i in range(2, nb):
    liste.append(i + 1)

for i in liste:
    premier = True
    for j in premiers:
        if i % j == 0:
            premier = False
    if premier == True:
        premiers.append(i)

print("Tous les nombres premiers avant ta valeur sont :", premiers)

