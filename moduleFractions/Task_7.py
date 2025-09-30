# 📊 Ordered Fractions
#
# Input: A natural number n. Write a program that outputs in ascending order all
# irreducible fractions between 0 and 1, whose denominator does not exceed n.
#
# Input Format
# A natural number n (n > 1).
#
# Output Format
# Output the desired fractions, each on a separate line.
#
# Note. You may need the gcd() function to find the greatest common divisor (GCD)
# of two numbers. The function is implemented in the math module.

# Test _____________________________________________

from fractions import Fraction as F
from math import gcd





n = int(input())
fraction_list = []
for i in range(1, n):
    for j in range(n, 1, -1):
        if i > j:
            break
        if gcd(i, j) == 1:
            fraction_list.append(F(i, j))
            
print(*sorted(fraction_list), sep="\n")
