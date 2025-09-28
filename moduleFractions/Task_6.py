# 🤓 Young Mathematician 
# Alex is in seventh grade and they're studying common fractions with natural numerators and denominators.
# Yesterday in math class, Alex learned that a fraction is proper if its numerator is less than the denominator,
# or irreducible if no equal fraction exists with smaller natural numerator and denominator.
# Alex loves math, so at home he experimented, creating and solving problems with proper irreducible fractions.
# He offers one for you to solve with a computer.
# Input: A natural number n. Write a program finding the largest proper irreducible fraction where numerator + denominator = n.
# Input Format: Natural number n.
# Output Format: Output the answer.


# Test ______________________________________

from fractions import Fraction as F
from math import gcd

n = int(input())

fraction = []
for i in range(n // 2 + 1):
    if gcd(i, n - i) == 1:
        fraction.append(F(i, n - i))

print(fraction[-1])
