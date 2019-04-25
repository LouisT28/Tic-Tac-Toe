# Code to check wether or not the a player has won.

CORRECT_INPUTS = [0, 1, 2]
PLAYER_X = 1
PLAYER_O = 2
NO_PLAYER = 0

def check_win(game):
    winner_row = checkrows(game)
    if winner_row == NO_PLAYER:
            winner_column = checkcolumns(game)
            if winner_column == NO_PLAYER:
                    winner_diagonal_right = checkdiagonalright(game)
                    if winner_diagonal_right == NO_PLAYER:
                            winner_diagonal_left = checkdiagonalleft(game)

    if (winner_row == PLAYER_X or
        winner_column == PLAYER_X or
        winner_diagonal_right == PLAYER_X or
        winner_diagonal_left == PLAYER_X):
            return PLAYER_X

    elif (winner_row == PLAYER_O or
        winner_column == PLAYER_O or
        winner_diagonal_right == PLAYER_O or
        winner_diagonal_left == PLAYER_O):
            return PLAYER_O
    return NO_PLAYER

def checkrows(game):
    for row in game:
        if row[0] == row[1] == row[2]:
            if row[0] == PLAYER_X:
                return PLAYER_X

            elif row[0] == PLAYER_O:
                return PLAYER_O
    return NO_PLAYER

def checkcolumns(game):
    for column_num in range(len(game)):
        if game[0][column_num] == game[1][column_num] == game[2][column_num]:
            if game[0][column_num] == PLAYER_X:
                return PLAYER_X

            elif game[0][column_num] == PLAYER_O:
                return PLAYER_O
    return 0

def checkdiagonalright(game):
    if game[0][0] == game[1][1] == game[2][2]:
        if game[0][0] == PLAYER_X:
            return PLAYER_X

        elif game[0][0] == PLAYER_O:
            return PLAYER_O
    return NO_PLAYER

def checkdiagonalleft(game):
    if game[0][2] == game[1][1] == game[2][0]:
        if game[0][2] == PLAYER_X:
            return PLAYER_X
        elif game[0][2] == PLAYER_O:
            return PLAYER_O
    return NO_PLAYER
