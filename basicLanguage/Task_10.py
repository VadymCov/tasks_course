# Product of numbers
# Write a program that determines whether a given number is the product of two numbers from a given set.
# The program should output YES or NO as the result.
#
# Input format:
# The first line contains a natural number n (1 < n < 1000) — the number of elements in the set.
# Each of the next n lines contains an integer (numbers may repeat).
# Then an integer follows, which may or may not be the product of two distinct numbers from the set.
#
# Output format:
# The program should print YES or NO according to the problem statement.
#
# Note 1: A number from the set cannot be multiplied by itself — the two factors must have different indices.
# Note 2: Use nested loops to solve the task.


n = int(input())
li_n = [int(input()) for _ in range(n)]
x = int(input())

flag = False

for i in range(n):
    for j in range(1+i, n):
        if li_n[i] * li_n[j] == x:
            flag = True
            break
    
if flag:
    print("YES")
else:
    print("NO")


