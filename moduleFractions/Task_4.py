# ➕➖✖️➗ Fraction Operations
# Two fractions in the format a/b are given.
# Write a program that calculates and outputs their sum, difference, product, and quotient.
# Input format:
# The program receives two non-zero fractions, each on a separate line.
# Output format:
# The program should output the sum, difference, product, and quotient of the two fractions.

# Test ______________________________________

from fractions import Fraction as F

n = input()
m = input()
print(f"{n} + {m} = {F(n) + F(m)}")
print(f"{n} - {m} = {F(n) - F(m)}")
print(f"{n} * {m} = {F(n) * F(m)}")
print(f"{n} / {m} = {F(n) / F(m)}")

