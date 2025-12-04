#  🌟 More Than the Average
#  Write a program that, for each row of a square matrix,
#  prints the count of elements greater than the arithmetic average of that row.
#
#  Input format:
#    - A natural number n (size of the square matrix),
#    - Followed by n lines, each with n integers separated by spaces.


matrix = [input().split() for _ in range(int(input()))]
result = []

for i in range(len(matrix)):
    temp = 0
    for j in range(len(matrix)):
        average = sum([int(d) for d in matrix[i]]) // len(matrix)
        if int(matrix[i][j]) > average:
            temp += 1
            
    result.append(temp)
    
print(*result, sep="\n")

