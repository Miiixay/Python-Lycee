import math

a = int(input("abscisse du premier point : "))
c = int(input("ordonnée du premier point : "))
b = int(input("abscisse du second point : "))
d = int(input("ordonnée du second point : "))
e = int(input("abscisse du troisième point : "))
f = int(input("ordonnée du troisième point : "))

cote1 = math.sqrt((a - b)**2 + (c - d)**2)
cote2 = math.sqrt((a - e)**2 + (c - f)**2)
cote3 = math.sqrt((b - e)**2 + (d - f)**2)


def identique(cote1, cote2, cote3):
    if cote1 == cote2 and cote2 == cote3:
        return "le triangle est equilatéral"
    if cote1 == cote2 or cote2 == cote3 or cote3 == cote1:
        return "le triangle est isocèle"
    return "le triangle est quelconque"


def pythagore(cote1, cote2, cote3):
  if cote1**2 == cote2**2 + cote3**2 or cote2**2 == cote1**2 + cote3**2 or cote3**2 == cote1**2 + cote2**2:
    return " le triangle est rectangle"
  return "le triangle n'est pas rectangle"


#cote1, cote2, cote3 = distance(0,0,2,0,1,3**(1/2))
print(pythagore(cote1, cote2, cote3))
print(identique(cote1, cote2, cote3))
