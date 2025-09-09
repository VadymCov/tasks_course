# 🔍 **Maximum in Area 2**
# Write a program that outputs the maximum element in the shaded area of 
# a square matrix. The shaded area is located below the anti-diagonal.
# **Input format** The program receives a natural number n as input — the number 
# of rows and columns in the matrix, then the matrix elements.
# **Output format** The program should output one number — the maximum element 
# in the shaded area of the square matrix.
# **Note.** Elements of the anti-diagonal are also taken into account.

matrix = [list(map(int, input().split())) for _ in range(int(input()))]

result = []
n = len(matrix)
for i in range(n):
    result.append(matrix[i][-1 - i:])




# Test _________________________

print(max(max(result,key=max)))






