#  🔮 Magic Square Check
#  The program reads:
#    - A natural number n (size of the square matrix),
#    - Then n rows of n integers each.
#
#  Task:
#    Check if the matrix is a magic square:
#    – It contains all numbers from 1 to n² exactly once,
#    – And all rows, all columns, and both main diagonals sum to the same value.
#
#  Output:
#    Print YES if it's a magic square, otherwise NO.


def magic_square(table):

    temp = sum(table[0])
   
    for i in range(len(table)):
        cnt = []
        col = []
        row = []
        dig_x = []
        dig_y = []

        for j in range(len(table)):
            col.append(table[i][j])
            row.append(table[j][i])
            dig_x.append(table[j][j])
            dig_y.append(table[j][len(table) - 1 - j])

            if table[j].count(table[i][j]) == 1:
                cnt.append(1)
                if len(cnt) > 1:
                    return 'NO'

            if (
                table[j].count(table[j][i]) > 1 or
                table[i][j] > max(max(table, key=max)) or
                table[i][j] < 1
                ):
                return 'NO'
        if ( 
            sum(col) != temp or
            sum(row) != temp or
            sum(dig_x) != temp or
            sum(dig_y) != temp  
            ):
            return 'NO'
    return 'YES'


def user_input():
    n = int(input())
    table = [input().split() for _ in range(n)]

    for i in range(n):
        int_table = []
        for j in range(n):
            int_table.append(int(table[i][j]))
        table[i] = int_table
        
    return table


# Test ______________________________


print(magic_square(user_input()))

