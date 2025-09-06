# 🔷 Matrix Filling 3
# The program receives a natural number `n` as input.
# It should create an `n × n` matrix and fill it according to the given example:
# place `1`s on both the main diagonal (top-left to bottom-right)
# and the secondary diagonal (top-right to bottom-left),
# while filling all other positions with `0`s.
#
# Input format:
# A natural number `n` — the number of rows and columns in the matrix.
#
# Output format:
# The program should print the matrix exactly as shown in the example pattern.




n = int(input())

matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        matrix[i][i] = 1
        matrix[i][n - i - 1] = 1
for j in range(n):
    for k in range(n):
        print(str(matrix[j][k]).ljust(3), end = '')
    print()