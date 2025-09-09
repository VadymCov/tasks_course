# 🔄 **Symmetric Matrix**
# Write a program to check if a square matrix is symmetric with respect to 
# the anti-diagonal (secondary diagonal).
# **Input format** The program receives a natural number n as input — the number 
# of rows and columns in the matrix, then the matrix elements.
# **Output format** The program should output `YES` if the matrix is symmetric, 
# and the word `NO` otherwise.


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

def symmetric_matrix(mtx, n ):
    for i in range(n):
        for j in range(n):
            if i + j != n - 1:
                if mtx[i][j] != mtx[n - 1 - j][n - 1 - i]:
                    return 'NO'
    return 'YES'


#Test _________________

print(symmetric_matrix(matrix, n ))