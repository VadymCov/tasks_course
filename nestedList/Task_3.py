#  🌟 Pascal’s Triangle 1
#  Pascal's Triangle is an infinite triangular array of binomial coefficients.
#  At the top and along the sides are ones. Each number is the sum of the two numbers directly above it.
#  
#  Given an input number n, write a program that returns the specified row of Pascal's Triangle as a list (row numbering starts at zero).
#  
#  Input format:
#  A natural number n (n ≥ 0) is given as input.
#  
#  Output format:
#  The program should output the specified row of Pascal's Triangle as a list.

def pascal(n):

    my_list = [1]

    for i in range(n):
        my_list.append(my_list[i] * (n - i) // (i + 1))

    return my_list

n = int(input())
print(pascal(n))