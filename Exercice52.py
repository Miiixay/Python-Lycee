class Client():
    def __init__(self, prenom, nom, ville, cp, age, numeroClient):
        self.prenom = prenom
        self.nom = nom
        self.ville = ville
        self.cp = cp
        self.age = age
        self.numeroClient = numeroClient


jpv = Client(" Jean Pierre ", " Vernant ", "Sèvres", "92310", "93", "JV123456")
jpv.numeroClient = "JV654321"
print(jpv.numeroClient)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y






