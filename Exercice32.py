nombre=0
response=input("Phrase : ")
voy=["a","e","i","o","u","A","E","I","O","U"]
for lettre in response:
  if lettre in voy:
    nombre=nombre+1
print("Nombre de consonnes : ", (len(response)-nombre))
print("Nombres de voyelles : ", (nombre))