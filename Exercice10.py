montant=float(input("Quel est votre montant: "))
montantf=0
if 2000<=montant<=5000:
  montantf=1/100*montant
  print("Le montant net obtenu est: ",montantf)
elif montant>5000:
  montantf=2/100*montant
  print("Le montant net obtenu est: ",montantf)
else:
  print("Le montant est: ",montant)