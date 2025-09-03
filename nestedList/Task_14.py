#  📐 Sums of Matrix Quarters
#  The program receives:
#    - A natural number n (size of the square matrix),
#    - Then n lines of integers, each containing n elements separated by spaces.
#
#  Write a program that computes the sum of elements in each of the four quarters:
#   - upper quarter (above both diagonals),
#   - right quarter (to the right of both diagonals),
#   - lower quarter (below both diagonals),
#   - left quarter (to the left of both diagonals).
#
#  Note: Elements on the main and secondary diagonals are NOT included.
#
#  Input format:
#    First n, then the n x n matrix elements row by row.
#
#  Output format:
#    Print the sums for upper, right, lower, and left quarters, in that order.


def sums_of_quarters(mtx):
    output_sections = [
        "upper quarter :",  
        "right quarter: ",
        "lower quarter: ",
        "left quarter: "
    ]
    sum_quart = [0,0,0,0]
    for row in range(len(mtx)):
        for col in range(len(mtx[row])):
            if col > row < len(mtx[0]) - col - 1:
                sum_quart[0] += mtx[row][col]

            elif col  > row > len(mtx[row]) - col - 1:
                sum_quart[1] += mtx[row][col]

            elif col  < row > len(mtx[row]) - col - 1:
                sum_quart[2] += mtx[row][col]

            elif col  < row < len(mtx[row]) - col -1 :
                sum_quart[3] += mtx[row][col]

    
    for i in range(len(output_sections)):
        print(output_sections[i], sum_quart[i])




def user_input():
    n = int(input())
    matrix = []
    for _ in range(n):
        elem = [
            int(e) for e in input().split()
        ]
        matrix.append(elem)
    return matrix
    
# Test ___________
sums_of_quarters(user_input())