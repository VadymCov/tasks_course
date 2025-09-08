# 🔄 Task: Fill a matrix diagonally ↙️
# 📥 Input: Two natural numbers n and m are given — the number of rows and columns of the matrix.
# 🧮 The program should create an n × m matrix and fill it "diagonally" according to the given pattern.
# 📤 Output: The program must print the resulting matrix in the specified format.


n, m = map(int, input().split())
matrix = [[0] * m for _ in range(n)]


temp = 1

for k in range(n + m - 1):
    for i in range(n):
        for j in range(m):
            if i+j == k:
                temp += 1
                matrix[i][j] = temp



# Test _______________________________________

for i in range(n):
    for j in range(m):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()
        