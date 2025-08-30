#  🌟 List by example 2
#  The program receives a number n as input.
#  Write a program that creates and prints, line by line,
#  a nested list consisting of n lists: [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].
#
#  Input format:
#  A natural number n is given as input to the program.

# 🌟 Solution 2

n = int(input())

for i in range(1, n + 1):
    print(list(range(1, i + 1)))



# 🌟 Solution 2

result = [list(range (1, i + 1)) for i in range(1, int(input()) + 1)]
print(*result, sep="\n")