#  💎 Pascal’s Triangle 2
#  The program receives a natural number n as input.
#  Write a program that prints the first n rows of Pascal’s Triangle.
#
#  Input format:
#  A number n (n ≥ 1) is given as input.


    
def pascal(n):

    my_list = [1]

    for i in range(n):
        my_list.append(my_list[i] * (n - i) // (i + 1))

    return my_list

#____________________________________

def pascal2(n):

    result = []

    for i in range(n):
        result.append(pascal(i))

    return result

#____________________________________

num = int(input())

for i in pascal2(num):
    print(*i, sep=" ")
