# tic tac toe main game, here the 
# main functions are called

from check_win import *
from move import *
                
if __name__ == "__main__":
        win = 0
        game = [[0,0,0],
                [0,0,0],
                [0,0,0]]

        print_board(game)
        while win == NO_PLAYER:
            player_move(game, PLAYER_X)
            win = check_win(game)
            if win == PLAYER_X:
                break
    
            player_move(game, PLAYER_O)
            win = check_win(game)
            if win == PLAYER_O:
                break

        if win == PLAYER_X:
            print("Player X wins!")

        elif win == PLAYER_O:
            print("Player O wins!")

        else:
            print("its a draw")
