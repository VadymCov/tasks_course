#  🏆 Maximum in Table
#  The program receives:
#    - Two natural numbers on separate lines: n (rows) and m (columns),
#    - Then n lines follow, each containing m integers separated by spaces.
#
#  Task:
#    Find the indices (row, column) of the first occurrence of the maximum element in the matrix.
#    If the maximum appears multiple times, pick the one with the smallest row index;
#    if rows tie — pick the one with the smallest column index.
#
#  Input format:
#    [n lines of m integers each]
#
#  Output:
#    Two integers: the row index and the column index (0-based).


def max_table():
    n = int(input())
    m = int(input())

    matrix = []
    for _ in range(n):
        matrix.append([int(i) for i in input().split()])
        
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == max(max(matrix, key=max)):
                return print(f"{i} {j}")
            

# Test________________

max_table()