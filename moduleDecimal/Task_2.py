# 🔢 Sum of the largest and smallest digits
# Complete the code to output the sum of the largest and smallest digits in a Decimal number.

# Test __________________________________________________

from decimal import *

num = Decimal(input())
num_tuple = num.as_tuple()

min_num = False
max_num = max(num_tuple.digits)

if num_tuple.exponent * -1 != len(num_tuple.digits):
    min_num = min(num_tuple.digits)

print(max_num + min_num)
