# ✖️ Task: Matrix Multiplication
# 📥 Input:
#   Two natural numbers n and m — the number of rows and columns in the first matrix,
#   followed by the elements of the first matrix.
#   Then an empty line.
#   Next, two numbers m and k — the number of rows and columns in the second matrix,
#   followed by the elements of the second matrix.
# 📤 Output:
#   The program should output the resulting matrix (product of the two matrices),
#   separating the elements with a space.


def matrix_multiply(matrix1, matrix2):
    n = len(matrix1)
    matrix3 = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix3[i][j] += matrix1[i][k] * matrix2[k][j]
    return matrix3
    


matrix = [list(map(int, input().split())) for _ in range(int(input()))]
m = int(input())
power_matrix = matrix.copy()


for _ in range(m - 1):
    power_matrix = matrix_multiply(matrix, power_matrix)

for i in power_matrix:
    print(*i)