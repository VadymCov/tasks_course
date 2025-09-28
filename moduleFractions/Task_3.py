# ➗ Fraction Reduction
# Two natural numbers m and n are given.
# Write a program that reduces the fraction m/n and outputs it.
# Input format:
# The program receives two natural numbers, the numerator and denominator of the fraction, each on a separate line.

# Test ________________________________________

from fractions import Fraction as F

n = int(input())
m = int(input())
result = F(n, m)
print(result)
