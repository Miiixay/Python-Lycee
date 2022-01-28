relations = {
    "Matthieu": ("Claire", "Charly"),
    "Claire": ("Matthieu", "Sébastien", "Charly"),
    "Sébastien": ("Claire", "Alice"),
    "Alice": ("Sébastien", "Charly", "Aurélie"),
    "Charly": ("Matthieu", "Claire", "Alice"),
    "Aurélie": ("Alice"),
}


def listeAmis(a):
    return relations[a]


print(listeAmis("Charly"))
