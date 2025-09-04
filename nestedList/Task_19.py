#  ♻️ Swap Diagonals
#  The program reads:
#    - A natural number n (size of the square matrix),
#    - Then n rows of n integers each (matrix elements).
#
#  Task:
#    For each row, swap the element on the main diagonal (at position [i][i])
#    with the one on the secondary (anti-) diagonal (at position [i][n-1-i]).
#    Print the resulting matrix.
#
#  Input format:
#    then n lines, each with n space-separated integers
#
#  Output:
#    The updated matrix with the diagonals swapped.


def user_input():
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    return matrix


def swap_diagonals(mtx):
    
    n = len(mtx[0]) -1

    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if i == j:
                mtx[i][j], mtx[n - j][i] = mtx[n - j][i], mtx[i][j] 

    for e in mtx:
        print(' '.join(e))
    
    


# Test____________
swap_diagonals(user_input())