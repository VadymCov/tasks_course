#  🧩 Print Matrix 1
#  The program receives two natural numbers n and m, each on its own line — the number of rows and columns.
#  Then n × m words follow (each on a separate line), row by row.
#  
#  Write a program that reads the matrix elements one by one,
#  then prints them in matrix form.
#
#  Input format:
#  Two numbers n and m (matrix dimensions), then n × m words, each on its own line.


n, m = int(input()), int(input())

row = n
column = m

matrix = []

for r in range(row):
    temp_row = []
    for c in range(column):
        temp_row.append(input())
    matrix.append(temp_row)

for i in matrix:
    print(*i)

