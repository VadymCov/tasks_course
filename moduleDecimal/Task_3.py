# 🧮 Mathematical Expression
# A Decimal number d is given as input to the program.
# Write a program that calculates the value of the expression:
# e^d + ln(d) + lg(d) + √d
# Test _______________________________________________

from decimal import Decimal

d = Decimal(input())
result = d.exp() + d.ln() + d.log10() + d.sqrt()
print(result)
