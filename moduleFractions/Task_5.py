# 🔢 **Sum of Fractions 1**
#
# You are given a natural number \( n \). Write a program that computes and outputs the rational number equal to the value of the expression:
#
# \[
# \frac{1}{1^2} + \frac{1}{2^2} + \frac{1}{3^2} + \frac{1}{4^2} + \dots + \frac{1}{n^2}
# \]
#
# **Input Format**
# A natural number \( n \) is given as input.
#
# **Output Format**
# Output the answer to the problem.
#
# **Note 1.** The resulting fraction must be irreducible.

# Test __________________________________

from fractions import Fraction as F

n = int(input())
result = F()
for i in range(1, n + 1):
    result += F(1, i**2)
print(result)
