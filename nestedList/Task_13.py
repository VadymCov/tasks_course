# 🔎 Maximum in shaded area 2
# A square matrix is ​​given:
# 1) The program receives a natural number n as input
# n is the number of rows and columns in the matrix
# 2) then the matrix elements (integers) one by one, separated by spaces.
#
# Task:
# Find and output the maximum value among all elements of the shaded area.
# The shaded area includes both the main and secondary diagonals, as well as the triangular zones adjacent to them.
#
# Input data:
# First row: n (matrix size)
# Next n rows: each contains n integers (matrix contents)
#
# Output data:
# One integer is the maximum element of the shaded area.

n = int(input())
matrix = []

for i in range(n):
    row = [int(r) for r in input().split()]
    matrix.append(row) 

result = []

for i in range(n):
    for j in range(n):
        if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
            result.append(matrix[i][j])

print(max(result))            
