import math


class Frac():
    def __init__(self, num, denom=1):
        self.num = num
        self.denom = denom

    def __add__(self, other):  # gère le +
        if type(other) != Frac:  # Si on ajoute un entier à une fraction
            other = Frac(other)  # On le convertit en fraction
        nouveauNum = self.num * other.denom + other.num * self.denom  # calcul du numérateur
        nouveauDenom = self.denom * other.denom  # calcul du dénominateur
        simplification = math.gcd(nouveauNum, nouveauDenom)  # plus grand commun diviseur
        nouveauNum = nouveauNum // simplification  # simplification entière du numérateur
        nouveauDenom = nouveauDenom // simplification  # simplification entière du dénominateur
        return Frac(nouveauNum, nouveauDenom)  # on renvoie le résultat

    def __sub__(self, other):  # gère le - (soustraction)
        if type(other) != Frac:  # Si on ajoute un entier à une fraction
            other = Frac(other)  # On le convertit en fraction
        nouveauNum = self.num * other.denom - other.num * self.denom  # calcul du numérateur
        nouveauDenom = self.denom * other.denom  # calcul du dénominateur
        simplification = math.gcd(nouveauNum, nouveauDenom)  # plus grand commun diviseur
        nouveauNum = nouveauNum // simplification  # simplification entière du numérateur
        nouveauDenom = nouveauDenom // simplification  # simplification entière du dénominateur
        return Frac(nouveauNum, nouveauDenom)  # on renvoie le résultat

    def __mul__(self, other):  # gère le *
        if type(other) != Frac:  # Si on ajoute un entier à une fraction
            other = Frac(other)  # On le convertit en fraction
        nouveauNum = self.num * other.num  # calcul du numérateur
        nouveauDenom = self.denom * other.denom  # calcul du dénominateur
        simplification = math.gcd(nouveauNum, nouveauDenom)  # plus grand commun diviseur
        nouveauNum = nouveauNum // simplification  # simplification entière du numérateur
        nouveauDenom = nouveauDenom // simplification  # simplification entière du dénominateur
        return Frac(nouveauNum, nouveauDenom)  # on renvoie le résultat

    def __truediv__(self, other):  # gère le /
        if type(other) != Frac:  # Si on ajoute un entier à une fraction
            other = Frac(other)  # On le convertit en fraction
        nouveauNum = self.num * other.denom  # calcul du numérateur
        nouveauDenom = self.denom * other.denom  # calcul du dénominateur
        simplification = math.gcd(nouveauNum, nouveauDenom)  # plus grand commun diviseur
        nouveauNum = nouveauNum // simplification  # simplification entière du numérateur
        nouveauDenom = nouveauDenom // simplification  # simplification entière du dénominateur
        return Frac(nouveauNum, nouveauDenom)  # on renvoie le résultat

    def __lt__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom < nouveauNum:
            return True
        else:
            return False

    def __le__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom <= nouveauNum:
            return True
        return False

    def __eq__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom == nouveauNum:
            return True
        else:
            return False

    def __ne__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom != nouveauNum:
            return True
        else:
            return False

    def __gt__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom > nouveauNum:
            return True
        else:
            return False

    def __ge__(self, other):
        if type(other) != Frac:
            other = Frac(other)
        nouveauNum = other.num * self.denom
        if self.num * other.denom >= nouveauNum:
            return True
        else:
            return False

    def __neg__(self):

        return Frac(-self.denom, self.num)

    def __str__(self):

        return str(self.num) + "/" + str(self.denom)


print(Frac(3, 2) * Frac(1, 2) != Frac(3, 8) / Frac(1, 2))

a = Frac(1, 3) + Frac(1, 6)

print(a)
