# 🔄 **Matrix Transposition**
# Write a program that transposes a square matrix.
# **Input format** The program receives a natural number n as input — the number 
# of rows and columns in the matrix, then the matrix elements.
# **Output format** The program should output the transposed matrix.
# **Note 1.** A transposed matrix is a matrix obtained from the original matrix 
# by replacing rows with columns.
# **Note 2.** The problem can be solved without using an auxiliary list.

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        print(matrix[j][i], end=" ")
    print()