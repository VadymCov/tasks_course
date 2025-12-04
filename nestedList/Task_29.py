# 🟦 Matrix Filling 5
# The program receives two natural numbers `n` and `m` as input.
# It should create an `n × m` matrix and fill it according to the given example pattern.
#
# Input format:
# Two natural numbers `n` and `m` are given on one line — the number of rows and columns.
#
# Output format:
# The program should print the matrix exactly as shown in the example pattern.




n, m = map(int, input().split())
matrix = []

for i in range(n):
    row = []
    for j in range(i, m + i):
        row.append(j % m + 1)
    matrix.append(row)



# Test ______________________________________

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()