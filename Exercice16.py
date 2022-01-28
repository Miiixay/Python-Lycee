phrase = input("Entrez un mot: \n")
phraseChiffree=""
choix=int(input("Tapez 1 si vous voulez chiffrer ou 2 si vous voulez le déchiffrer: "))

if choix==1:
  for ch in phrase:
    if ch=="z" or ch=="Z":
      phraseChiffree += chr(ord(ch)-25)
    else :
      phraseChiffree += chr(ord(ch)+1)
else:
  for ch in phrase:
    if ch=="z" or ch=="Z":
      phraseChiffree += chr(ord(ch)+25)
    else :
      phraseChiffree += chr(ord(ch)-1)

print(phraseChiffree)

#1) Ce programme change les lettres due mot d'une lettre après dans l'alphabet
#2) La condition sert dans le cas où il y a le dernière lettre de l'alphabet (z,Z) pour retourner a la premiere lettre de l'alphabet (a,A)
