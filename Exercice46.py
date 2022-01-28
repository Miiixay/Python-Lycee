def createTree(valeur):
  return [valeur,None,None]

def appendLeftTree(tree,leftTree):
  return [tree[0],leftTree,tree[2]]

def appendRightTree(tree,rightTree):
  return [tree[0],tree[1],rightTree]

cinq = createTree(5)
onze = createTree(11)
six = createTree(6)
deux = createTree(2)
sept = createTree(7)
neuf = createTree(9)
quatre = createTree(4)
deux1 = createTree(21)
cinq1 = createTree(51)

cinq1 = appendRightTree(cinq1,None)
cinq1 = appendLeftTree(cinq1,None)

quatre = appendRightTree(quatre,None)
quatre = appendLeftTree(quatre,None)

onze = appendRightTree(onze,None)
onze = appendLeftTree(onze,None)

six = appendLeftTree(six,cinq)
six = appendRightTree(six,onze)

neuf = appendLeftTree(neuf,quatre)
neuf = appendRightTree(neuf, None)

deux1 = appendLeftTree(deux1,None)
deux1 = appendRightTree(deux1,None)

sept = appendLeftTree(sept,deux1)
sept = appendRightTree(sept,six)

cinq = appendRightTree(cinq,neuf)
cinq = appendLeftTree(cinq,None)

deux = appendLeftTree(deux,sept)
deux = appendRightTree(deux,cinq)

print(deux)