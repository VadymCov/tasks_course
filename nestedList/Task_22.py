#  ♞ Knight Moves Map
#  The program reads:
#    - A chessboard position of a knight in algebraic notation (e.g., e4).
#
#  Task:
#    Mark the knight's position with 'N', all squares it can attack with '*',
#    and all other squares with '.' on an 8×8 board. Print the board with spaces between symbols.
#
#  Input format:
#    A single string like "e4" indicating the knight's square (file 'a'-'h', rank '1'-'8').
#
#  Output format:
#    An 8×8 grid of characters separated by spaces.



def board():
    mtx_board = [['.']*8 for _ in range(8)]
    return mtx_board


def knights_move(board):
    x, y = input()
    x = ord(x) - ord('a')
    y = len(board) - int(y)
    board[x][y] = 'N'

    for i in range(len(board)):
        for j in range(len(board)):
            if abs(x - i) * abs(y - j) == 2:
                board[i][j] = "*"

    for k in board:
        print(*k)


        
# Test________________________
knights_move(board())