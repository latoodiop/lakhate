import random

def afficher_plateau(plateau):
    for ligne in plateau:
        print("|".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, joueur):
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True
    for colonne in range(3):
        if all(plateau[i][colonne] == joueur for i in range(3)):
            return True
    if all(plateau[i][i] == joueur for i in range(3)) or all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def tour_ordi(plateau, joueur):
    print("Tour de l'ordinateur")
    while True:
        ligne = random.randint(0, 2)
        colonne = random.randint(0, 2)
        if plateau[ligne][colonne] == " ":
            plateau[ligne][colonne] = joueur
            break

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    tour = 0
    joueurs = ["X", "O"]
    
    while True:
        afficher_plateau(plateau)
        joueur_actuel = joueurs[tour % 2]
        
        if joueur_actuel == "X":
            print("Tour de l'humain")
            ligne = int(input("Choisissez la ligne (0, 1, 2): "))
            colonne = int(input("Choisissez la colonne (0, 1, 2): "))
            
            if plateau[ligne][colonne] != " ":
                print("Case déjà occupée. Réessayez.")
                continue
            
            plateau[ligne][colonne] = joueur_actuel
        else:
            tour_ordi(plateau, joueur_actuel)
        
        if verifier_victoire(plateau, joueur_actuel):
            afficher_plateau(plateau)
            print("Victoire de", joueur_actuel)
            break
        
        tour += 1
        
        if tour == 9:
            afficher_plateau(plateau)
            print("Match nul !")
            break

morpion()