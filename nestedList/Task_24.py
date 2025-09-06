#  ⌛ Chessboard Pattern
#  The program reads:
#    - Two natural numbers n and m on one line (rows and columns).
#
#  Task:
#    Create an n×m matrix filled in a checkerboard style:
#      - Start with '.' in the top-left corner
#      - Alternate '.' and '*' across rows and columns
#    Print the resulting matrix with elements separated by spaces.


n, m = input().split()
matrix = []

for i in range(int(n)):
    row = []
    for j in range(int(m)):
        if i % 2 == 0 and j % 2 == 0:
            row.append('.')
        elif i % 2 == 0 and j % 2 != 0:
            row.append('*')
        elif i % 2 != 0 and j % 2 != 0:
            row.append('.')
        elif i % 2 != 0 and j % 2 == 0:
            row.append('*')

    matrix.append(row)

# Test___________________

for i in matrix:
    print(*i)

