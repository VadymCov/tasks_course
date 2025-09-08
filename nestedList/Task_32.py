# ➕ Task: Matrix Addition
# 📥 Input: Two natural numbers n and m — the number of rows and columns in the matrices.
# 🧮 Then the elements of the first matrix are given, followed by an empty line,
#     and then the elements of the second matrix.
# 📤 Output: The program should output the resulting matrix (sum of the two matrices),
#     separating the elements with a space.


n, m = map(int, input().split())

matrix_a = [list(map(int,  input().split())) for _ in range(n)]
input()
matrix_b = [list(map(int,  input().split())) for _ in range(n)]


matrix_c = []

for i in range(n):
    temp = []
    for j in range(m):
        elem = matrix_a[i][j] + matrix_b[i][j]
        temp.append(elem)
    matrix_c.append(temp)



# Test_________________

for i in range(n):
    for j in range(m):
        print(str(matrix_c[i][j]).ljust(3), end="")
    print()



# Variant second_________________________

def matrix_addition(matrix1, matrix2, col):
    n = len(matrix1)
    result_matrix = [[0] * col for _ in range(n)]

    for i in range(n):
        for j in range(col):
            result_matrix[i][j] += matrix1[i][j] + matrix2[i][j]

    return result_matrix


row, col = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(row)]
input()
matrix2 = [list(map(int, input().split())) for _ in range(row)]


# Test _________________________________________________-

for i in matrix_addition(matrix1, matrix2, col):
    print(*i)
