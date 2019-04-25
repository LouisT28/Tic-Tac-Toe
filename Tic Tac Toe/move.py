# code that makes a player move 

CORRECT_INPUTS = [0, 1, 2]
PLAYER_X = 1
PLAYER_O = 2
NO_PLAYER = 0

ENTRY_INVALID = "Entry is not valid"
SQUARE_FULL = "This square is taken"

BLANK = ""

def print_board(game):

        for row in game:
            for current in row:
                if current == 1:
                    print(" X ", end = BLANK)

                elif current == 2:
                    print(" O ", end = BLANK)

                else:
                    print(" _ ", end = BLANK)
            print(BLANK)

def player_move(game, player):
    valid = False
    while not valid:
        try:
            input_row = int(input("Enter a row: "))
            input_column = int(input("Enter a column: "))
            if input_row in CORRECT_INPUTS and input_column in CORRECT_INPUTS:
                valid = is_square_valid(game, input_row, input_column)
                if valid == False:
                    print(SQUARE_FULL)
            
            else:
                print(ENTRY_INVALID)
        except:
            print(ENTRY_INVALID)

    game[input_row][input_column] = player
    print_board(game)

def is_square_valid(game, row, column):
    if game[row][column] == NO_PLAYER:
        return True
    
    else:
        return False
