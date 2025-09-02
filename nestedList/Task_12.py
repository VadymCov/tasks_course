# 🔍 Maximum in shaded area
# The program receives:
# - A natural number n (the size of a square matrix),
# - Then n rows of integers (matrix elements), each row on a separate line, separated by spaces.
#
# Write a program that prints the maximum element in the shaded area of ​​the matrix.
# (Note: the shaded area includes elements of the secondary diagonal.)

elem = [input().split() for _ in range(int(input()))]
result = []
for i in range(len(elem)):
    for j in range(len(elem)):
        if i >= j:
            result.append(int(elem[i][j]))
print(max(result))