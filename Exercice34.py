n=input("Ecrivez une phrase: ")

voy=["a","e","i","o","u"]

nSplit=n.split(' ')
for mot in nSplit:
  if mot[0] in voy:
    index=nSplit.index(mot)
    nSplit[index]=mot+'hay'
  else:
    premiereLettre=mot[0]
    index=nSplit.index(mot)
    nSplit[index]=mot[1:]+premiereLettre+'ay'

print(nSplit)
