#  🔢 Multiplication Table Matrix
#  The program receives two natural numbers on separate lines:
#    n – number of rows,
#    m – number of columns.
#
#  Create an n×m matrix `mult` where mult[i][j] = i * j.
#
#  Output format:
#    Print the multiplication table, with each number printed in a field of width 3 characters
#    (use ljust(3) to align).



def matrix_mult():
    n, m = int(input()), int(input())
    matrix = []
    for i in range(n):
        row_matrix = []
        for j in range(m):
            row_matrix.append(i * j)
        matrix.append(row_matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(str(matrix[i][j]).ljust(2), end=" ")
        print()


# Test__________________________________

matrix_mult()
    