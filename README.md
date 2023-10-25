# warshipsBattle
**jeu bataille navale** avec premier code en python 

# Sur le main --> Le jeu complet

    La grille de jeu virtuelle est composée de 10 x 10 cases.
    Une case est identifiée par ses coordonnées ( no colonne, no ligne).
    Une colonne sera identifiée par une lettre (de 'A' à 'J').
    Une ligne sera identifiée par un nombre (de 1 à 10).
        exemple:  A1  ou  J10

## Lancement d'une partie
    
    Au lancement de la partie 5 navires sont placés sur la carte.
    Pour gagné, il faut réussir à détruir les navires en éffectuent le moins de tir possible.

# Sur la branche partie_1 --> La partie 1 de l'exercice

    Sur cette partie, 
    la grille n'est pas affichée,
    une demande de coordonnée est effectuer tant que tous les navires ne sont pas détruits,
    un retour indique si le tir à touché ou manqué une cible,
    les navire sont placés à des places fixes.

Position des navires:
  + aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
  + cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
  + destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
  + submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
  + torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9

# Sur la branche partie_2 --> La partie 2 de l'exercice

# Sur la branche partie_3 --> La partie 3 de l'exercice