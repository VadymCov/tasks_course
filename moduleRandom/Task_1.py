# 🎯 **Bingo Card Generator**
# For playing bingo, a 5×5 card is required containing different (unique) integers 
# from 1 to 75 (inclusive), with the center cell being empty (it is filled with 
# the number 0).

# Write a program that uses the `random` module to generate and output a random 
# bingo card.

# **Note 1.** For clarity, we recommend allocating exactly 3 characters for 
# outputting each number. Use the string method `ljust()` for this.
# **Note 2.** Example of a possible output:

# 1  16 31 46 61
# 10 30 42 47 68
# 3  18 0  48 63
# 9  19 34 49 70
# 5  20 35 50 65

# Test _______________________________________________________

import random
random_num = random.sample(range(1, 75), 5*5)
random_num[12] = 0
matrix = [[0]*5 for _ in range(5)]

while len(random_num) > 0:
    for i in range(5):
        print(str(random_num[i]).ljust(3), end=" ")
    print()
    del random_num[0:5]