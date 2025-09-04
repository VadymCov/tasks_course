#  ↕️ Mirror Horizontally
#  The program reads:
#    - A natural number n (size of the square matrix),
#    - Then n rows of n integers each (matrix elements).
#
#  Task:
#    Reflect the matrix across its horizontal axis.
#    That means the first row becomes the last, the second becomes the second-last, etc.
#    Print the mirrored matrix.

def user_input():
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    return matrix

def mirror_horizontally(mtx):
    for i in range(len(mtx) - 1, -1 , -1):
        for j in range(len(mtx)):
            print(mtx[i][j], end=" ")
        print()
        


mirror_horizontally(user_input())