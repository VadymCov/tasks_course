#  ⏸️ Swap Matrix Columns
#  The program receives:
#    - Two natural numbers on separate lines: n (number of rows) and m (number of columns),
#    - Then n rows follow, each with m integers (matrix elements) space-separated,
#    - Finally two natural numbers i and j — the indices of the columns to swap.
#
#  Task:
#    Output the matrix after swapping columns i and j.
#
#  Input format:
#    [n lines of m integers each]

#  Output:
#    The updated matrix, with columns i and j swapped.


def user_input():
    n = int(input())
    m = int(input())

    matrix = [input().split() for _ in range(n) ]
    elem = [int(e) for e in input().split()]

    return matrix, elem

def swap_matrix_columns(mtx, elem):
    i = elem[0]
    j = elem[1]

    for row in range(len(mtx)):
        mtx[row][i],mtx[row][j] = mtx[row][j],mtx[row][i]

    for k in range(len(mtx)):
        print(*mtx[k])



# Test___________________a
matrix,elem = user_input()
swap_matrix_columns(matrix, elem)
