# 🔢 **Latin Square**
# A Latin square of order n is a square matrix of size n×n, where each row and 
# each column contains all numbers from 1 to n. Write a program that checks whether 
# a given square matrix is a Latin square.
# **Input format** The program receives a natural number n as input — the number 
# of rows and columns in the matrix, then the matrix elements: n rows, with n numbers 
# in each, separated by spaces.
# **Output format** The program should output `YES` if the matrix is a Latin square, 
# or `NO` otherwise.

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

def test(mtx,  n):
    temp = list(range(1, n + 1))
    for i in range(n):
        row = []
        col = []
        for j in range(n):

            row.append(mtx[i][j])
            col.append(mtx[j][i])
        if (set(temp) != set(row) or
            set(temp) != set(col)):
            return "NO"
        
    return "YES"


# Test______________________
tst = test(matrix, n )
print(tst)