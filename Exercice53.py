import math


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p1, p2):
        return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y))

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

print(a.proche(a, liste))
