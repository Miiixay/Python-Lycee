pile=[1,1]
i=2

while len(pile)<10:
 pile.append(pile[i-1] + pile[i-2])
 i=i+1
print(pile)
