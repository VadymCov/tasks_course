# ❄️ **Snowflake**
# The program receives an odd natural number n as input. Write a program that creates 
# an n×n matrix filled with `.` symbols. Then fill with `*` symbols the middle row 
# and column of the matrix, the main and anti-diagonal of the matrix. Output the 
# resulting matrix to the screen, separating elements with spaces.
# **Input format** The program receives an odd natural number n, (n≥3) as input — 
# the number of rows and columns in the matrix.
# **Output format** The program should output the matrix according to the problem 
# conditions.


n = int(input())

matrix = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (
            i == j or
            i + j + 1 == n or
            j == n // 2 or 
            i == n // 2
        ):
            matrix[i][j] = '*'
            

            
# Test ___________________

for i in matrix:
    print(*i)