
# 📐 **Diagonals parallel to the main diagonal**
# The program receives a natural number n as input. Write a program that creates 
# an n×n matrix and fills it according to the following rule:
# * on the main diagonal, each element should be the number 0;
# * on the two diagonals adjacent to the main diagonal – number 1;
# * on the next two diagonals – number 2, and so on.
# **Input format** The program receives a natural number n as input — 
# the number of rows and columns in the matrix.
# **Output format** The program should output the matrix according to 
# the problem conditions.

n = int(input())
matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = abs(i - j)


# Test ______________________

for i in matrix:
    print(*i)