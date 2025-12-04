# 🎯 Secondary Diagonal Matrix
# The program receives a natural number `n` as input.
# It should create an `n × n` matrix and fill it according to the following rules:
# - Numbers on the secondary diagonal (from top-right to bottom-left) are `1`.
# - Numbers above this diagonal are `0`.
# - Numbers below this diagonal are `2`.
#
# After filling, the matrix should be printed row by row,
# with elements in each row separated by a single space.
#
# Input format:
# A natural number `n` — the number of rows and columns in the matrix.
#
# Output format:
# The program should print the matrix according to the specified rules.





n = int(input())

matrix =[[0 * n for _ in range(n)] for _ in range(n)]
result = []

for i in range(n):
    temp = []
    for j in range(n):
        matrix[i][n - i - 1] = 1
        if (i >= j and i > n - j - 1) or (i <= j and i > n - j - 1):
            matrix[i][j] = 2



# Test_____________________

for e in matrix:
    print(*e)            
