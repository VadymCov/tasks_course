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


n, m = map(int, input().split())

matrix_a = [list(map(int,  input().split())) for _ in range(n)]
input()

n2, m2 = map(int, input().split())
matrix_b = [list(map(int,  input().split())) for _ in range(n2)]

matrix_c = [[0] * n for _ in range(n)]


for k in range(n):
    for i in range(m2):
        elem = 0
        for j in range(m):
            elem += matrix_a[k][j] * matrix_b[j][i]
        matrix_c[k][i] = elem

# Test_______________________________

for i in range(len(matrix_c)):
    print(*matrix_c[i])




# Variant second_______________________________________________

n1, m1 = map(int, input().split())
matrix1 = [list(map(int, input().split()))for _ in range(n1)]
input()

n2, m2 = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(n2)]

def multiply_matrix(matrix1, matrix2, col):
    n = len(matrix1)
    result_matrix = [[0] * col for _ in range(n)]

    for i in range(col):
        for j in range(col):
            for k in range(col):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


# Test____________________________
col = len(matrix1)
for i in multiply_matrix(matrix1, matrix2, col):
        print(*i)