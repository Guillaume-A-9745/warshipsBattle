#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Définition de la taille de la grille et des lettres de colonne
GRID_SIZE = 10
LETTERS = "ABCDEFGHIJ"
# Constantes des différents états possibles pour une case
SEA, MISSED_SHOT, HIT_SHOT, SUNK_SHOT = 0, 1, 2, 3

# Définir une variable globale pour stocker les coups joués
played_shots = {}

# Position initiale des navires avec des coordonnées et des états
aircraft_carrier = {(2, 2): True, (3, 2): True, (4, 2): True, (5, 2): True, (6, 2): True}  # porte_avion en B2
cruiser = {(1, 4): True, (1, 5): True, (1, 6): True, (1, 7): True}  # croiseur en A4
destroyer = {(3, 5): True, (3, 6): True, (3, 7): True}  # contre_torpilleur en C5
submarine = {(8, 5): True, (9, 5): True, (10, 5): True}  # sous_marin en H5
torpedo_boat = {(5, 9): True, (6, 9): True}  # torpilleur en E9
# Liste des navires
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]
ships_sunk = []


def ask_coord():
    """
    Main function of the game. Manages the flow of the battleship game.
    """
    print('Bienvenue dans la bataille navale :')
    display_grid()
    while ships_list:
        shot_coord = get_user_shot()
        analyze_shot(ships_list, shot_coord)
        display_grid()

    print('Bravo, vous avez coulé tous les navires')


# fonction pour obtenir des coordonnées de tir de l'utilisateur
def get_user_shot():
    """
    function to get firing coordinates from user
    :return: coordinates
    """
    valid_coord = False
    while not valid_coord:
        player_coord = input("Entrez les coordonnées de votre tir (ex. : 'A1', 'H8') : ")
        if 2 <= len(player_coord) <= 3:
            letter, number = player_coord[0], player_coord[1:]
            letter = letter.upper()
            try:
                # détermination de line_no et column_no (comptés à partir de 1)
                line_no = int(number)
                column_no = ord(letter) - ord('A') + 1
                if 1 <= line_no <= GRID_SIZE and letter in LETTERS:
                    valid_coord = True
                    shot_coord = (column_no, line_no)
                    return shot_coord
            except ValueError:
                pass
        print("Coordonnées invalides. Veuillez entrer des coordonnées valides.")


# fonction retournant un booléen indiquant si un navire est touché par un tir aux coordonnées indiquées
def ship_is_hit(ship, shot_coord):
    """
    function returning a boolean indicating if a ship is hit by a shot at the specified coordinates
    :param ship: one ship
    :param shot_coord: coordinates
    :return: True if ship hit, False otherwise.
    """
    if shot_coord in ship:
        ship[shot_coord] = False  # on mémorise ce tir
        grid_square_state(shot_coord)
        return True
    return False


# fonction retournant un booléen indiquant si un navire est coulé (toutes ses cases ont été touchées)
def ship_is_sunk(ship):
    """
    function returning a boolean indicating if a ship is sunk (all its boxes have been touched)
    :param ship: one ship
    :return: True if ship sunk, False otherwise
    """
    if True not in ship.values():
        ships_list.remove(ship)  # le navire est supprimé de la flotte
        ships_sunk.append(ship)
        return True
    return False


# fonction affichant le résultat d'un tir
def analyze_shot(ships, shot_coord):
    """
    function displaying the result of a shot
    :param ships: list of ships
    :param shot_coord: coordinates
    :return: display message
    """
    col_letter = LETTERS[shot_coord[0] - 1]  # Convertir l'indice en lettre
    row_number = shot_coord[1]
    hit_ship = None  # Variable pour suivre si un navire a été touché
    sunk = None
    for ship in ships:
        hit = ship_is_hit(ship, shot_coord)  # On regarde si un navire est touché
        if hit:
            hit_ship = True  # Marquer que le tir a touché un navire
            sunk = ship_is_sunk(ship)  # on regarde si le navire est coulé
    if hit_ship:
        played_shots[(col_letter, row_number)] = "Touché"
        print('Un navire a été touché par votre tir !')
        if sunk:
            print('Le navire touché est coulé !!')
    else:
        played_shots[(col_letter, row_number)] = "Manqué"
        print("Votre tir est tombé dans l'eau")


# fonction retournant l'état de la case passée en paramètre
def grid_square_state(coord):
    """
    function returning the state of the box passed as a parameter
    :param coord: coordinate
    :return: coordinate status
    """
    state = played_shots.get((LETTERS[coord[1] - 1], coord[0]), "")
    return state


# fonction affichant la grille
def display_grid():
    """
    Grid display function
    :return: grid display
    """
    num_rows = GRID_SIZE
    num_cols = GRID_SIZE

    # Créez une grille vide avec des espaces
    grid = [[' ' for _ in range(num_cols)] for _ in range(num_rows)]

    # Affichez les étiquettes des colonnes (A, B, C, ...)
    print("    " + "   ".join(LETTERS))

    # Affichez la grille avec les états des cases
    for row in range(num_rows):
        row_label = str(row + 1).rjust(2)  # Ajoute un espace pour l'alignement
        row_display = [row_label]

        for col in range(num_cols):
            cell_value = grid_square_state((row + 1, col + 1))
            if cell_value == "Touché":
                grid[row][col] = 'X'
                for ship in ships_sunk:
                    for coord in ship:
                        if (col + 1, row + 1) == coord:
                            grid[row][col] = 'W'
            elif cell_value == "Manqué":
                grid[row][col] = 'O'

            row_display.append(f"[{grid[row][col]}]")

        print(" ".join(row_display))


ask_coord()
