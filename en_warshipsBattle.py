#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Définition de la taille de la grille et des lettres de colonne
GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"

# Initialisation du dictionnaire pour stocker les résultats des tirs précédents
previous_shots = {}

# Position initiale des navires avec des coordonnées et des états
aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # Porte-avion en B2
cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # Croiseur en A4
destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # Contre-torpilleur en C5
submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # Sous-marin en H5
torpedo_boat = {(5, 9): True, (6, 9): True}  # Torpilleur en E9
# Liste des navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]


# Fonction principale du jeu
def engage():
    """
    Main function of the game. Manages the flow of the battleship game.
    """
    print("Welcome to Battleship! Destroy all enemy ships to win.")
    while not all_ships_destroyed(ships_list):
        user_input = input("Enter the coordinates of your shot (example: 'A1' or 'J10'): ")
        coordinate = get_user_shot(user_input)
        result = check_hit(coordinate, ships_list)
        update_previous_shots(coordinate, result)
        display_battlefield(previous_shots, ships_list)  # Afficher la grille avec les tirs précédents

    print("All enemy ships have been sunk. You win!")


# Vérifie si les coordonnées sont valides
def is_valid_coordinate(coordinate):
    """
    Check if the coordinates are valid within the grid.
    :param coordinate: The coordinates as a tuple (column, row).
    :return: bool: True if the coordinates are valid, False otherwise.
    """
    return coordinate[0] in range(1, GRID_SIZE + 1) and coordinate[1] in range(1, GRID_SIZE + 1)


# Vérifie si un tir touche un navire
def check_hit(coordinate, ships):
    """
    Checks if a shot hits a ship.
    :param coordinate: The coordinates of the shot (column, row).
    :param ships: The list of boats.
    :return: bool: True if ship is hit, False otherwise.
    """
    for ship in ships:
        if coordinate in ship:
            ship[coordinate] = False  # Marquer la position du navire comme touchée
            print("Hit!")
            if all(value is False for value in ship.values()):
                print("A ship has been sunk!")
            return True
    print("Miss!")
    return False


# Obtenir les coordonnées du tir de l'utilisateur
def get_user_shot(user_input):
    """
    Function used to obtain the coordinates of the user's shot.
    :param user_input: The coordinates of the user's shot.
    :return: The row and column number as a tuple.
    """
    user_input = user_input.strip().upper()
    if len(user_input) >= 2:
        col_letter, row_str = user_input[0], user_input[1:]
        if col_letter in LETTERS and row_str.isdigit():
            row = int(row_str)
            col = LETTERS.index(col_letter) + 1
            if is_valid_coordinate((col, row)):
                return col, row
    print("Invalid coordinates. Please enter valid coordinates.")
    return get_user_shot(input("Enter the coordinates of your shot (example: 'A1' or 'J10'): "))


# Vérifie si tous les navires ont été détruits
def all_ships_destroyed(ships):
    """
    Checks if all ships have been destroyed.
    :param ships: The list of boats.
    :return: Bool: False if one of them has a value True, True otherwise.
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
    col_letter = LETTERS[coordinate[0] - 1]  # Convertir l'indice en lettre
    row_number = coordinate[1]
    cell_state = "Hit" if result else "Miss"  # Mettre à jour l'état en fonction du résultat
    previous_shots[(col_letter, row_number)] = cell_state


# Affiche la grille avec les tirs précédents
def display_battlefield(shots, ships):
    """
    Display the game grid with the results of previous shots.
    :param ships: The list of boats.
    :param shots: A dictionary of previous shots with coordinates and results.
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
            if shots is not None:
                state = shots.get((LETTERS[col], row + 1), "")
                if state == "Hit":
                    cell_value = 'X'
                    for ship in ships:
                        if all(value is False for value in ship.values()):
                            cell_value = 'W'
                elif state == "Miss":
                    cell_value = 'O'
            row_display.append(f"[{cell_value}]")
        print(" ".join(row_display))


engage()
