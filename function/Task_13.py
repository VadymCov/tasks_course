# 🔢 Polynomial Value Problem
# A polynomial of degree n is an expression of the form: aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₂x² + a₁x + a₀
# where aₙ, aₙ₋₁, ..., a₂, a₁, a₀ are the polynomial coefficients (aₙ ≠ 0).
# Input:

# First line: polynomial coefficients (integers) separated by spaces
# Second line: integer value x

# Task:
# Write a program that calculates the value of the given polynomial at the specified value of x.
# Output format:
# The program should output a single number — the value of the given polynomial at the specified value of x.

from functools import reduce
from operator import add, mul, pow


def evaluate(coefficients: list, num: int):
    pow_num = []
    for i in range(len(coefficients) - 1, -1, -1):
        pow_num.append(pow(num, i))
    product = list(map(lambda x, y: mul(int(x), y), coefficients, pow_num))
    result = reduce(add, product, 0)
    return result


coff = input().split()
num = int(input())

print(evaluate(coff, num))
