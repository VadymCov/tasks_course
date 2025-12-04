# 🧮 Matrix Filling 2
# The program receives two natural numbers `n` and `m` as input.
# It should create an `n × m` matrix and fill it according to the given example pattern.
#
# Input format:
# Two natural numbers `n` and `m` are given on one line — the number of rows and columns.
#
# Output format:
# The program should print the matrix exactly as shown in the example pattern.




n, m = map(int, input().split())
matrix = [[0 for _ in range(m)]for _ in range(n)]
test = n * m

for i in range(m):
    for j in range(n):
        matrix[j][i] = (i * n) + j + 1




# Test______________________

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()