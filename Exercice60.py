def nbPieces(somme,valeurs):
  if somme==0:
    return 0
  mini = 10**6
  for v in valeurs:
    if v<=somme:
      nb = 1+nbPieces(somme-v,valeurs)
      if nb < mini:
        mini = nb
  return mini

aRendre = 11
pieces = [2,5,10,50,100]

print(f'Il faudra {nbPieces(aRendre,pieces)} pièces pour rendre {aRendre} centimes.')


# On constate que le programme trouve une solution sans utiliser de pièce de 1 centime. Dans le cas de 11, il utilise une pièce de 5 et trois pièce de 2.

#Ce programme ne resout pas le problème pour 177 centimes car il effectue trop de calculs et met donc beaucoup trop de temps pour trouver la solution.