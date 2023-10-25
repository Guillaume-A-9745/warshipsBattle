#!/usr/bin/env python
# -*- coding: utf-8 -*-

GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"

# Position initiale des navires
aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9
# Liste des navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

all_ships_destroyed = False

print("Bienvene sur la bataille navale !   Détruisez tous les navires ennemis pour gagner")
while not all_ships_destroyed:
    user_input = input("Entrez les coordonnées de votre tir (exemple: 'A1' ou 'J10'): ")
    user_input = user_input.strip().upper()
    if len(user_input) < 2:
        print("Coordonnées invalides. Veuillez entrer des coordonnées valides.")
        continue
    col_letter, row_str = user_input[0], user_input[1:]
    if col_letter not in LETTERS:
        print("Coordonnées invalides. Veuillez entrer des coordonnées valides.")
        continue
    try:
        row = int(row_str)
    except ValueError:
        print("Coordonnées invalides. Veuillez entrer des coordonnées valides.")
        continue
    col = LETTERS.index(col_letter) + 1
    if not (1 <= row <= GRID_SIZE and 1 <= col <= GRID_SIZE):
        print("Coordonnées en dehors de la grille. Veuillez entrer des coordonnées valides.")
        continue
    coordinate = (col, row)

    hit = False
    for ship in ships_list:
        if coordinate in ship:
            ship[coordinate] = False
            hit = True
            print("Touché!")
            if all(value == False for value in ship.values()):
                print("Un navire a été coulé!")
            break
    if not hit:
        print("Manqué!")

    all_ships_destroyed = all(all(value is False for ship in ships_list for value in ship.values()))
    # if not all_ships_destroyed:
    #     for ship in ships_list:
    #         for position in ship.values():
    #             if position:
    #                 all_ships_destroyed = False

print("Tous les navires ennemis ont été coulés. Vous avez gagné!")