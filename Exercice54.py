import math


def distanceNombres(a, b, c, d):
    return math.sqrt((a - b) * (a - b) + (c - d) * (c - d))


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x:' + str(self.x) + ' y:' + str(self.y)

    def proche(self, a, liste):
        listeproche = []
        for point in liste:
            listeproche.append(self.distance(a, point))
        listeproche = min(listeproche)
        for point in liste:
            if self.distance(a, point) == listeproche:
                return point

    def __str__(self):
        return f'{self.x} {self.y}'


liste = [Point(3, 1), Point(2, 4), Point(2, 5), Point(0, 4), Point(-1, 2)]
a = Point(1, 3)

valeur = []

for point in liste:
    print("x = ", point.x)
    print("y = ", point.y)

    print("distance a et b est : ", distanceNombres(a.x, point.x, a.y, point.y))

    valeur.append(distanceNombres(a.x, point.x, a.y, point.y))
    print()

print(valeur)

value = (valeur.index(min(valeur)))
print("le point le plus proche du point a est : ", liste[value])
