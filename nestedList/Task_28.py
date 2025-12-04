# 🟩 Matrix Filling 4
# The program receives a natural number `n` as input.
# It should create an `n × n` matrix and fill it according to the given example pattern.
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
        if i == j or j == n - i - 1 or (i > j and i > n - j - 1) or (i < j and i < n - j - 1):
            matrix[i][j] = 1



# Test _____________________

for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()