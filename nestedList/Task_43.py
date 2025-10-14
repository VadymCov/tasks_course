# Spiral Filling 🌀🌶️🌶️

# You are given two natural numbers `n` and `m`. Write a program that creates an `n × m`
# matrix filled in a spiral pattern according to the example.

## Input Format
# The program receives two natural numbers `n` and `m` on one line, representing the number
# of rows and columns in the matrix.

# Would you like me to help you implement the solution to this problem? I can guide you through creating
# a Python program that generates a spiral matrix based on the given dimensions.


n = int(input())
m = int(input())

matrix = [[0] * m for _ in range(n)]

top = 0
rights = m - 1
bottom = n - 1
left = 0

num = 1

while top <= bottom and left <= rights:

    for col in range(left, rights + 1):
        matrix[top][col] = num
        num += 1
    top += 1

    for row in range(top, bottom + 1):
        matrix[row][rights] = num
        num += 1
    rights -= 1

    if top <= bottom:
        for col in range(rights, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1

    if left <= rights:
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1

for row in matrix:
    print(" ".join(str(elem).ljust(3) for elem in row))
