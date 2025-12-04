# ♕ **Queen moves**
# A queen is placed on an 8×8 chessboard. Mark the position of the queen on the board 
# and all squares that the queen attacks. Mark the square where the queen stands with 
# the letter `Q`, squares that the queen attacks with `*` symbols, fill the remaining 
# squares with dots.
# **Input format** The program receives the coordinates of the queen on the chessboard 
# in chess notation (i.e., in the form `e4`, where the column number is written first 
# (letter from `a` to `h`, left to right), then the row number (digit from 1 to 8, 
# bottom to top)).
# **Output format** The program should display an image of the board on the screen, 
# separating elements with spaces.

n, m = input()

q = 8
m = q - int(m)
d = ord(n) - ord('a')
board = [['.'] * q for _ in range(q)]


for i in range(q):
    for j in range(q):
        if (
            i == m or
            j == d or 
            i + j == m + d  or 
            i - j == m - d
            ):

            board[i][j] = '*'

board[m][d] = 'Q'

# Test _______________

for i in board:
    print(*i)