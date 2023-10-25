#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Définition de la taille de la grille et des lettres de colonne
GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"

# Initialisation du dictionnaire pour stocker les résultats des tirs précédents
previous_shots = {}

# Position initiale des navires avec des coordonnées et des états
aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9
# Liste des navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]

# Fonction principale du jeu
def engage():
    """
    Main function of the game. Manages the flow of the battleship game.
    """
    print("Bienvene sur la bataille navale !   Détruisez tous les navires ennemis pour gagner")
    while not all_ships_destroyed(ships_list):
        user_input = input("Entrez les coordonnées de votre tir (exemple: 'A1' ou 'J10'): ")
        coordinate = get_user_shot(user_input)
        result = check_hit(coordinate, ships_list)
        update_previous_shots(coordinate, result)
        display_battlefield(previous_shots)         # afficher la grille avec les tirs précédents

    print("Tous les navires ennemis ont été coulés. Vous avez gagné!")

# Vérifie si les coordonnées sont valides
def is_valid_coordinate(coordinate):
    """
    Check if the coordinates are valid within the grid.
    :param coordinate (tuple): The coordinates as a tuple (column, row).
    :return: bool: True if the coordinates are valid, False otherwise.
    """
    return coordinate[0] in range(1, GRID_SIZE + 1) and coordinate[1] in range(1, GRID_SIZE + 1)

# Vérifie si un tir touche un navire
def check_hit(coordinate, ships):
    """
    Checks if a shot hits a ship
    :param coordinate: The coordinates of the shot (column, row).
    :param ships: the list of boats
    :return: bool: True if ship hit, False otherwise
    """
    for ship in ships:
        if coordinate in ship:
            ship[coordinate] = False  # Marquer la position comme touchée
            print("Touché!")
            if all(value == False for value in ship.values()):
                print("Un navire a été coulé!")
            return True
    print("Manqué!")
    return False

# Obtenir les coordonnées du tir de l'utilisateur
def get_user_shot(user_input):
    """
    Function used to obtain the coordinates of the user's shot digitally
    :param user_input: the coordinates of the user's shot
    :return: the row and column number
    """
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

# Vérifie si tous les navires ont été détruits
def all_ships_destroyed(ships):
    """
    Checks if all ships have been destroyed
    :param ships: the list of boats
    :return: Bool: False if one of them have a value True,  True otherwise
    """
    for ship in ships:
        for position in ship.values():
            if position:
                return False
    return True

# Met à jour les résultats des tirs précédents
def update_previous_shots(coordinate, result):
    """
    Update the dictionary of previous shots with the result of a shot.
    :param coordinate: The coordinates of the shot (column, row).
    :param result: True if the shot hit, False if it missed.
    """
    col_letter = LETTERS[coordinate[0] - 1]         # Convertir l'indice en lettre
    row_number = coordinate[1]
    cell_state = "Touché" if result else "Manqué"   # Mettre à jour l'état en fonction du résultat
    previous_shots[(col_letter, row_number)] = cell_state

# Affiche la grille avec les tirs précédents
def display_battlefield(previous_shots):
    """
    Display the game grid with the results of previous shots.
    :param previous_shots: A dictionary of previous shots with coordinates and results.
    """
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
                state = previous_shots.get((LETTERS[col], row + 1), "")
                if state == "Touché":
                    cell_value = 'X'
                elif state == "Manqué":
                    cell_value = 'O'
            row_display.append(f"[{cell_value}]")

        print(" ".join(row_display))

engage()
