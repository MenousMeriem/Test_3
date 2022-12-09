 
#Exercice sur les condition : Version 1 : 
print("Est ce qu'il pleut, réponds par Oui ou Non :")
a = input()

if (a == "Oui") :
    print("il faut rester à la maison !! y t il du courant, réponds par Oui ou Non")
    b = input()
    if (b == "Oui") : 
        print("Regarder Netflix !!")
    elif ( b == "Non") : 
        print("Lire un roman !! ")
    else : 
        print (" La réponse n'est ni oui ni non ")
elif (a == "Non") : 
    print("Sors de la maison, Il fait chaud ?? Réponds par Oui ou Non")
    c = input()
    if (c == "Oui") : 
        print("Aller visiter un Mall")
    elif ( c == "Non") : 
        print (" Aller visiter un jardin !! ")
    else : 
        print("La réponse n'est ni oui ni non")
else : 
    print(" La réponse n'est ni Oui ni Non !! ")



