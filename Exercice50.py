relations = [
    [0, 1, 0, 0, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 1],
    [1, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
]

noms = {1: "Matthieu", 2: "Claire", 3: "Sébastien", 4: "Alice", 5: "Charly", 6: "Aurélie"}
numéros = {"Matthieu": 1, "Claire": 2, "Sébastien": 3, "Alice": 4, "Charly": 5, "Aurélie": 6}


def listeAmis(a):
    amis = []
    n = numéros[a]
    listeRelations = relations[n - 1]
    for i in range(len(listeRelations)):
        nom = noms[i + 1]
        if listeRelations[i] == 1:
            amis.append(nom)

    return amis


print(listeAmis("Matthieu"))
