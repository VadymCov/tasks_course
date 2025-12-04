#  🧮 Print Matrix 2
#  The program receives two natural numbers, n and m, each on a separate line — number of rows and columns.
#  Then n × m words follow (each on a new line), row by row.
#
#  Write a program that reads the matrix elements one by one,
#  prints them in matrix form, then prints an empty line,
#  followed by the same matrix again but transposed
#  (rows become columns).
#
#  Input format:
#  Two numbers n and m (matrix dimensions), followed by n × m words, each on its own line.


n, m = int(input()), int(input())

row = n
column = m

matrix = []

for i in range(row):
    temp_row = []
    for j in range(column):
        temp_row.append(input())
    matrix.append(temp_row)

for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()

print()

for i in range(column):
    for j in range(row):
        print(matrix[j][i], end=" ")
    print()