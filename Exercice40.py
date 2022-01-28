def nbChiffres(n):
  if n//10>0 :
    return nbChiffres(n//10)+1

  return 0

print(nbChiffres(3**100)+1)