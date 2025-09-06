# 🐍 Snake Filling
# The program receives two natural numbers `n` and `m` as input.
# It should create an `n × m` matrix and fill it in a "snake" pattern
# according to the given example:
# - The first row is filled left to right with consecutive numbers.
# - The second row is filled right to left.
# - The direction alternates for each subsequent row.
#
# Input format:
# Two natural numbers `n` and `m` are given on one line — the number of rows and columns.
#
# Output format:
# The program should print the matrix exactly as shown in the example pattern.




n, m = map(int, input().split())
matrix = []


for i in range(n):
    temp_row = []
    for j in range(m):
        temp_row.append(i * m + j + 1)
    if i % 2 != 0:
        matrix.append(temp_row[::-1])
    else:
        matrix.append(temp_row)


# Test_________________________________

for i in range(n):
    for j in range(m):
         print(str(matrix[i][j]).ljust(3), end=' ')
    print()