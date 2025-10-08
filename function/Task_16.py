# 🔢 Interesting Numbers
# Input: Two natural numbers a and b, each on a separate line.
# Write a program using the built-in all() function to find all integers
# from a to b (inclusive) that are divisible by every digit they contain without remainder.

# Output: All such numbers from a to b (inclusive) on one line, space-separated.

# Note: Numbers containing zeros are not interesting and should not be output.

# put your python code here

a, b = int(input()), int(input())
for i in range(a, b + 1):
    list_num = list(map(int, str(i)))
    if 0 not in list_num and all(map(lambda x: i % x == 0, list_num)):
        print(i, end=" ")
