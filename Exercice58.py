def nbPieces(somme,valeurs):
  if somme==0:
    return 0
  for v in valeurs[::-1]:
    if v<=somme:
      print(f'On utilise une pièce de {v}.')
      return 1+nbPieces(somme-v,valeurs)

aRendre = 11
pieces = [2,5,10,50,100]
# pieces.insert(0,1)

print(f'Il faudra {nbPieces(aRendre,pieces)} pièces pour rendre {aRendre} centimes.')


'''
Le programme plante car il n'y a pas de pièces de 1 centime dans la liste. Il prend la valeur en dessous de la somme restante a payer. Il pourrait utiliser 1 pièce de 5 centime et 3 pieces de 2 centimes ou ajouter la pièce de 1 la ligne 10.
'''