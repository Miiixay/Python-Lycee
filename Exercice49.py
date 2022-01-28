def parcoursGauche(t):
    if t != None:
        print(t[0])
        parcoursGauche(t[1])
        parcoursGauche(t[2])


# Lorque l'on deplace la ligne 3 a la place de la 4 ou la 5 ca ne fonctionne pas
def size(t): xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


if t != None:
    return 1 + size(t[1]) + size(t[2])
return 0

tree = [
    2, [7, [2, None, None], [6, [5, None, None], [11, None, None]]],
    [5, None, [9, [4, None, None], None]]]

parcoursGauche(tree)

print("nombre de nœuds : ", size(tree))

