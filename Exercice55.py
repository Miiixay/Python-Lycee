class Compte():
    LeCompte = 0
    LeTotal = 0

    def __init__(self, prenom, nom, solde=0):
        self.prenom = prenom
        self.nom = nom
        self.solde = solde
        Compte.LeCompte += 1
        Compte.LeTotal += solde

    def depot(self, somme):
        self.solde += somme
        Compte.LeTotal += somme
        return self.solde

    def retrait(self, somme):
        self.solde -= somme
        Compte.argent
        return self.solde


Marwan = Compte("Marwan", "Jaffres", 1000)
Jérémie = Compte("Jérémie", "Loison", 1200)

Marwan.depot(100)

print(Compte.LeTotal)