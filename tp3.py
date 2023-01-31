import random

vie = 20
boucle_jeu = True
choix = 0
force_adversaire = 0
victoire = 0
defaite = 0

while boucle_jeu:
    if choix != 3:
        force_adversaire = random.randint(1, 5) + random.randint(1, 5)
        print("Vous etes en difficulté dure")

    if victoire % 3 == 0 and victoire > 0 :
        force_adversaire = random.randint(4, 5)
        print("Vous etes en diffuclté facile")


    #force_adversaire = random.randint(4, 5)

    print(f"Vous tombez face a face avec un adversaire de difficulté {force_adversaire}")
    print("1- Combattre cet adversaire")
    print('2- Contourner cet adversaire et aller ouvrir une autre porte')
    print('3- Afficher les règles du jeu')
    print('4- Quitter la partie')
    choix = int(input('Que voulez vous faire'))
    if choix == 1:
        force_joueur = random.randint(1, 6) + random.randint(1, 6)
        print ("Le dé va determiner l'issue du combat")

        if force_joueur > force_adversaire :
            vie = vie + force_adversaire
            print ("Vous avez gagné le combat bravo.")
            victoire += 1
        elif force_joueur <= force_adversaire:
            print("vous avez perdu le combat car la force de l'adversaire etait superieure a ta force ")
            vie = vie - force_adversaire
            defaite += 1

        print(f"il vous reste {vie} point de vie")
        print(f"vous avez {victoire} victoire et {defaite} defaite")

    elif choix == 2:
        print("Vous contournez le monstre ")
        vie -= 1
    elif choix == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print("Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print("La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
        print("L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")
    elif choix == 4:
        print("Merci et au revoir ")
        boucle_jeu = False

    if vie < 1:
        print (" Vous avez perdu ")
        boucle_jeu = False






