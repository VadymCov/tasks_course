#  🔄 Symmetric Matrix Check
#  The program reads:
#    - A natural number n (matrix size),
#    - Then n rows of n integers each (matrix elements).
#
#  Task:
#    Check if the matrix is symmetric with respect to the main diagonal.
#    That means for all i, j: a[i][j] == a[j][i].
#
#  Output:
#    Print YES if symmetric, otherwise NO.



def user_input():
    n = int(input())
    elem = [input().split() for _ in range(n)]
    return elem

def symmetric_matrix_check(mtx):
    for i in range(len(mtx)):
        for j in range(len(mtx)):
            if i > j and mtx[i][j] != mtx[j][i]:
                return 'NO'
    return "YES"




# Test _______________
print(symmetric_matrix_check(user_input()))
