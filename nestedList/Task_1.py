#  🚀 List by example 1
#  The program receives a number n as input. 
#  Write a program that creates and prints, line by line,
#  a list consisting of n lists: [[1, 2, ..., n], ..., [1, 2, ..., n]].
#
#  Input format:
#  A natural number n is given as input.

n = int(input())
for _ in range(n):
    elem = [li for li in range(1, n + 1)]
    print(elem)