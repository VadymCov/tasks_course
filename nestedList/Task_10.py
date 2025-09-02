#  🧮 Matrix Trace
#  The trace of a square matrix is the sum of its main diagonal elements.
#  
#  Input:
#    - A natural number n (matrix dimensions — number of rows and columns),
#    - Followed by n lines, each containing row elements (integers) separated by spaces.
#  
#  Task:
#    Read the square matrix and print the trace (sum of the diagonal elements).


def matrix_trace(n):
    matrix = [input().split() for _ in range(n)]
    result = []
    for i in range(n):
        temp = matrix[i][i]
        result.append(int(temp))
    return sum(result)
            

# Test________________________

print(matrix_trace(int(input())))

