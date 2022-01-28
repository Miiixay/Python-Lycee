phrase=input('Phrase contenant "Jean" : ')
mot=1
liste = phrase.split(" ")
for i in liste:
  if i.lower()!="jean":
    mot=mot+1
  else:
    print("Le mot jean est en",mot,"position")

