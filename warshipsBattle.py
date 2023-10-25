#!/usr/bin/env python
# -*- coding: utf-8 -*-

GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"
previous_shots = []

# Position initiale des navires
aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9
# Liste des navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

def engage():
    print("Bienvene sur la bataille navale !   Détruisez tous les navires ennemis pour gagner")
    while not all_ships_destroyed(ships_list):
        user_input = input("Entrez les coordonnées de votre tir (exemple: 'A1' ou 'J10'): ")
        coordinate = get_user_shot(user_input)
        result = check_hit(coordinate, ships_list)
        previous_shots.append(coordinate)       # ajouter les coordonnées au tableau
        display_battlefield(previous_shots)     # afficher la grille avec les tirs précédents

    print("Tous les navires ennemis ont été coulés. Vous avez gagné!")

def is_valid_coordinate(coordinate):
    return coordinate[0] in range(1, GRID_SIZE + 1) and coordinate[1] in range(1, GRID_SIZE + 1)

def check_hit(coordinate, ships):
    for ship in ships:
        if coordinate in ship:
            ship[coordinate] = False  # Marquer la position comme touchée
            print("Touché!")
            if all(value == False for value in ship.values()):
                print("Un navire a été coulé!")
            return True
    print("Manqué!")
    return False

def get_user_shot(user_input):
    user_input = user_input.strip().upper()
    if len(user_input) >= 2:
        col_letter, row_str = user_input[0], user_input[1:]
        if col_letter in LETTERS and row_str.isdigit():
            row = int(row_str)
            col = LETTERS.index(col_letter) + 1
            if is_valid_coordinate((col, row)):
                return (col, row)
    print("Coordonnées invalides. Veuillez entrer des coordonnées valides.")
    return get_user_shot(input("Entrez les coordonnées de votre tir (exemple: 'A1' ou 'J10'): "))

def all_ships_destroyed(ships):
    for ship in ships:
        for position in ship.values():
            if position:
                return False
    return True

def display_battlefield(previous_shots):
    num_rows = GRID_SIZE
    num_cols = GRID_SIZE

    # Afficher les étiquettes des colonnes (A, B, C, ...)
    print("    " + "   ".join(LETTERS))

    for row in range(num_rows):
        row_label = str(row + 1).rjust(2)  # Ajoute un espace pour l'alignement
        row_display = [row_label]

        for col in range(num_cols):
            cell_value = ' '
            if previous_shots is not None:
                for shot in previous_shots:
                    if (shot[0]-1) == col and (shot[1]-1) == row:
                        cell_value = 'O'  # Marquer la zone ciblée
                        break
            row_display.append(f"[{cell_value}]")

        print(" ".join(row_display))
engage()
