#  ↪️ Rotate Matrix 90° Clockwise
#  The program reads:
#    - A natural number n (size of the square matrix),
#    - Then n rows of n integers each (matrix elements).
#
#  Task:
#    Rotate the matrix by 90 degrees clockwise.
#    Print the rotated matrix, numbers separated by a single space.



def user_input():
    n = int(input())
    matrix = [input().split() for _ in range(n)]
    return matrix


def rotate_matrix(mtx):
    m = len(mtx)
    for i in range(m):
        for j in range(m - 1, -1 , -1):
            print(mtx[j][i], end=" ")
        print()


# Test_______________
rotate_matrix(user_input())
