# WarshipsBattle
**Jeu de la bataille navale** pour mon premier code en python.

# Sur le main → Le jeu complet  (...en cours de développement...)

* La grille de jeu virtuelle est composée de 10 x 10 cases.
* Une case est identifiée par ses coordonnées ( no colonne, no ligne).
* Une colonne sera identifiée par une lettre (de 'A' à 'J').
* Une ligne sera identifiée par un nombre (de 1 à 10).
    + exemple:  A1  ou  J10

## Lancement d'une partie
    
* Au lancement de la partie 5 navires sont placés sur la carte.
* Pour gagner, il faut réussir à détruire les navires en éffectuent le moins de tir possible.

# Sur la branche partie_1 → La partie 1 de l'exercice

Sur cette partie :
* La grille n'est pas affichée.
* Une demande de coordonnée est effectuer tant que tous les navires ne sont pas détruits.
* Un retour indique si le tir à touché ou manqué une cible et indique quand un navire est coulé.
* Les navires sont placés à des places fixes.


* Ajout d'un fichier V2 sans fonction pour respecter les directives de l'exercice.

Position des navires:
+ aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
+ cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
+ destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
+ submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
+ torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9

# Sur la branche partie_2 → La partie 2 de l'exercice

Sur cette partie :
* Une demande de coordonnée est effectué tant que tous les navires ne sont pas détruits.
* La grille est affiché après chaque entrée de coordonnée.
* Un retour indique si le tir à toucher ou manqué une cible et indique quand un navire est coulé.
* Si le tire est réussi, la grille affiche un X sur la case ciblée.
* Si le tire échoue, la grille affiche un O sur la case ciblée.
* Les navires sont placés à des places fixes.


* Ajout de la version en anglais.
* Ajout de la docstrings.
* Ajout d'une version à partir du corriger de la partie 1.

Question :

+ Quels sont les avantages et inconvénients comparés d'un ensemble ou d'une liste pour stocker les coups joués de la partie ?
  + Avantages de l'utilisation d'un ensemble (set) :
    + Recherche rapide.
    + Elimination des doublons.
  + Inconvénients de l'utilisation d'un ensemble (set) :
    + Pas d'ordre spécifique.
    + Non Indexé.


+ Comment s'affichent les navires coulés ? Pourquoi en est-ce ainsi ?


+ Que pensez-vous de l'efficacité de la fonction grid_square_state(coord) ? Exposer une idée d'évolution de la structure des données du programme qui permettrait de l'améliorer à cet égard.

# Sur la branche partie_3 → La partie 3 de l'exercice

* coming soon...

# Installation et configuration

* coming soon...

