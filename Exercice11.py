print("=====Menu=====")
sandwiches = ["Royal Cheese", "Big Mac", "Mac Bacon", "Mac Deluxe"]
for index in range(len(sandwiches)):
 print (index+1, sandwiches[index])
choix=int(input("Quel sandwich désirez-vous ? "))-1
print ("Vous avez choisi le",sandwiches[choix],", c'est un très bon choix!")
